import ROOT
from array import array
from tqdm import tqdm
import argparse
import AddDiTauTriggerFactor

def AddMCTriggerScaleFactors(File,args):
    FileName = File[File.rfind("/")+1:]

    CheckFile = ROOT.TFile(File)
    try:
        CheckFile.mt_Selected.DiTauTriggerWeight
    except:
        print("Failed to find ditau trigger factors. Adding them...")
        AddDiTauTriggerFactor.AddDiTauTriggerFactor(File,args)
    CheckFile.Close()

    SecondScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_2017_v2.root")
    SecondWorkSpace = SecondScaleFactorFile.w    
    
    ReweightFile = ROOT.TFile(File,"UPDATE")
    TheTree=ReweightFile.mt_Selected

    TriggerSF = array('f',[0.])

    TriggerSF_Branch = TheTree.Branch("TriggerSF",TriggerSF,"TriggerSF/F")

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1, ReweightFile.mt_Selected.eta_1, ReweightFile.mt_Selected.phi_1, ReweightFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2, ReweightFile.mt_Selected.eta_2, ReweightFile.mt_Selected.phi_2, ReweightFile.mt_Selected.m_2)

        TriggerSF[0] = 1.0

        if args.year == "2016":
            raise RuntimeError("2016 not implemented! Implement me!")
        elif args.year == "2017":
            Trigger24 = (ReweightFile.mt_Selected.passMu24 and ReweightFile.mt_Selected.matchMu24_1 
                         and ReweightFile.mt_Selected.filterMu24_1 and ReweightFile.mt_Selected.pt_1 > 25.0)
            Trigger27 = (ReweightFile.mt_Selected.passMu27 and ReweightFile.mt_Selected.matchMu27_1 
                         and ReweightFile.mt_Selected.filterMu27_1 and ReweightFile.mt_Selected.pt_1 > 28.0)
            Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 and ReweightFile.mt_Selected.matchMu20Tau27_1 
                           and ReweightFile.mt_Selected.filterMu20Tau27_1                    
                           and ReweightFile.mt_Selected.filterMu20Tau27_2
                           and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_2 > 31 
                           and ReweightFile.mt_Selected.pt_1 < 25
                           and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                           and abs(ReweightFile.mt_Selected.eta_2) < 2.1)
    #no tau trigger matching in embedded
            if(FileName == "Embedded.root"):
                Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 and ReweightFile.mt_Selected.matchMu20Tau27_1 
                               and ReweightFile.mt_Selected.filterMu20Tau27_1
                               and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_2 > 31 
                               and ReweightFile.mt_Selected.pt_1 < 25
                               and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                               and abs(ReweightFile.mt_Selected.eta_2) < 2.1)
        elif args.year == "2018":
            Trigger24 = (ReweightFile.mt_Selected.passMu24 and ReweightFile.mt_Selected.matchMu24_1 
                         and ReweightFile.mt_Selected.filterMu24_1 and ReweightFile.mt_Selected.pt_1 > 25.0)
            Trigger27 = (ReweightFile.mt_Selected.passMu27 and ReweightFile.mt_Selected.matchMu27_1 
                         and ReweightFile.mt_Selected.filterMu27_1 and ReweightFile.mt_Selected.pt_1 > 28.0)            
            if(FileName == "Data.root"):
                if (ReweightFile.mt_Selected.run >= 317509): #hps trigger, no filter
                    Trigger2027 = (ReweightFile.mt_Selected.passMu20HPSTau27 
                                   and ReweightFile.mt_Selected.matchMu20HPSTau27_1
                                   and ReweightFile.mt_Selected.matchMu20HPSTau27_2
                                   and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                                   and ReweightFile.mt_Selected.pt_2 > 28)
                    if (ReweightFile.mt_Selected.run < 317509): #non hps trigger, can filter
                        Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 
                                       and ReweightFile.mt_Selected.matchMu20Tau27_1
                                       and ReweightFile.mt_Selected.matchMu20Tau27_2
                                       and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                                       and ReweightFile.mt_Selected.pt_2 > 28
                                       and ReweightFile.mt_Selected.filterMu20Tau27_1
                                       and ReweightFile.mt_Selected.filterMu20Tau27_2)
            else: #all hps cross trigger, ignore HPS filters
                Trigger2027 = (ReweightFile.mt_Selected.passMu20HPSTau27 
                               and ReweightFile.mt_Selected.matchMu20HPSTau27_1
                               and ReweightFile.mt_Selected.matchMu20HPSTau27_2
                               and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                               and ReweightFile.mt_Selected.pt_2 > 28)

        #Actually make the dang trigger scale factor
        #but don't do it to embedded ordata
        if FileName != "Embedded.root" and FileName != "Data.root":
            if Trigger24 or Trigger27:
                TriggerSF[0] = TriggerSF[0] * (SecondWorkSpace.function("m_trg24_27_kit_data").getVal() / SecondWorkSpace.function("m_trg24_27_kit_mc").getVal())
            else:
                TriggerSF[0] = TriggerSF[0] * (SecondWorkSpace.function("m_trg20_data").getVal()/SecondWorkSpace.function("m_trg20_mc").getVal()) * TheTree.DiTauTriggerWeight
        TriggerSF_Branch.Fill()
    ReweightFile.cd()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make and attach MC Trigger SF branches")
    parser.add_argument('year',choices=['2016','2017','2018'],help="Select which year's corrections are to be used")
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")

    args = parser.parse_args()
    
    for File in args.Files:
        print("Applying MC trigger SFs to "+str(File))
        AddMCTriggerScaleFactors(File,args)
