import ROOT
import sys
from array import array
from tqdm import tqdm
import argparse
import AddDiTauTriggerFactor

def ApplyZPTReweighting(File,args):
    FileName = File[File.rfind("/")+1:]    

    ReweightFile = ROOT.TFile(File,"UPDATE")
    TheTree=ReweightFile.mt_Selected
    
    ZPTWeighting = array('f',[0.])
    ZPTWeighting_DOWN = array('f',[0.])
    ZPTWeighting_UP = array('f',[0.])
    
    ZPTWeighting_Branch = TheTree.Branch("ZPTWeighting",ZPTWeighting,"ZPTWeighting/F")
    ZPTWeighting_Branch_DOWN = TheTree.Branch("ZPTWeighting_DOWN",ZPTWeighting_DOWN,"ZPTWeighting_DOWN/F")
    ZPTWeighting_Branch_UP = TheTree.Branch("ZPTWeighting_UP",ZPTWeighting_UP,"ZPTWeighting_UP/F")    

    SecondScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_2017_v2.root")
    SecondWorkSpace = SecondScaleFactorFile.w    
    
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1, ReweightFile.mt_Selected.eta_1, ReweightFile.mt_Selected.phi_1, ReweightFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2, ReweightFile.mt_Selected.eta_2, ReweightFile.mt_Selected.phi_2, ReweightFile.mt_Selected.m_2)

        ZPTWeighting[0]=1.0
        ZPTWeighting_DOWN[0] = 0.9 * ZPTWeighting[0]
        ZPTWeighting_UP[0] = 1.1 * ZPTWeighting[0]

        if(FileName != "Embedded.root"
           and FileName != "Data.root"):
            SecondWorkSpace.var("m_pt").setVal(MuVector.Pt())
            SecondWorkSpace.var("m_eta").setVal(MuVector.Eta())
            SecondWorkSpace.var("z_gen_mass").setVal(TheTree.genM)
            SecondWorkSpace.var("z_gen_pt").setVal(TheTree.genpT)            
            NominalWeight = SecondWorkSpace.function("zptmass_weight_nom").getVal()
            if(FileName == "DY.root"):
                ZPTWeighting[0] = ZPTWeighting[0] * NominalWeight            

        #create the shape stuff
        ZPTWeighting_DOWN[0] = 0.9 * ZPTWeighting[0]
        ZPTWeighting_UP[0] = 1.1 * ZPTWeighting[0]

        #ALWAYS. Also don't mess with embedded here
        if (FileName == "Data.root"
            or FileName == "Embedded.root"):
            ZPTWeighting[0] = 1.0
            ZPTWeighting_DOWN[0] = 1.0
            ZPTWeighting_UP[0] = 1.0

        ZPTWeighting_Branch.Fill()
        ZPTWeighting_Branch_DOWN.Fill()
        ZPTWeighting_Branch_UP.Fill()
        
    ReweightFile.cd()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

def Apply2016ZPTReweighting(File,args):
    FileName = File[File.rfind("/")+1:]    

    ReweightFile = ROOT.TFile(File,"UPDATE")
    TheTree=ReweightFile.mt_Selected
    
    ZPTWeighting = array('f',[0.])
    ZPTWeighting_DOWN = array('f',[0.])
    ZPTWeighting_UP = array('f',[0.])
    
    ZPTWeighting_Branch = TheTree.Branch("ZPTWeighting",ZPTWeighting,"ZPTWeighting/F")
    ZPTWeighting_Branch_DOWN = TheTree.Branch("ZPTWeighting_DOWN",ZPTWeighting_DOWN,"ZPTWeighting_DOWN/F")
    ZPTWeighting_Branch_UP = TheTree.Branch("ZPTWeighting_UP",ZPTWeighting_UP,"ZPTWeighting_UP/F")    

    ZPTWeightsFile = SecondScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/zpt_weights_2016_BtoH.root")
    ZPTWeightsHisto = ZPTWeightsFile.Get("zptmass_histo")

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1, ReweightFile.mt_Selected.eta_1, ReweightFile.mt_Selected.phi_1, ReweightFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2, ReweightFile.mt_Selected.eta_2, ReweightFile.mt_Selected.phi_2, ReweightFile.mt_Selected.m_2)

        ZPTWeighting[0]=1.0
        ZPTWeighting_DOWN[0] = 0.9 * ZPTWeighting[0]
        ZPTWeighting_UP[0] = 1.1 * ZPTWeighting[0]

        if(FileName != "Embedded.root"
           and FileName != "Data.root"):
            ZPTWeighting[0] = ZPTWeightsHisto.GetBinContent(ZPTWeightsHisto.GetXaxis().FindBin(TheTree.genM),
                                                            ZPTWeightsHisto.GetYaxis().FindBin(TheTree.genpT))            
        #this isn't quite correct
        ZPTWeighting_UP[0] = 1.0+(ZPTWeighting[0]-1.0)*1.1
        ZPTWeighting_DOWN[0] = 1.0+(ZPTWeighting[0]-1.0)*0.9        

        if(FileName == "Data.root"
           or FileName == "Embedded.root"):
            ZPTWeighting[0] = 1.0
            ZPTWeighting_UP[0] = 1.0
            ZPTWeighting_DOWN[0] = 1.0

        ZPTWeighting_Branch.Fill()
        ZPTWeighting_Branch_DOWN.Fill()
        ZPTWeighting_Branch_UP.Fill()
        
    ReweightFile.cd()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Make and attach ZPT reweighting branches.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's corrections are to be used")
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")

    args = parser.parse_args()

    for File in args.Files:
        print("Applying ZPT reweighting to "+str(File))
        if (args.year == "2017" and args.year=="2017"):
            ApplyZPTReweighting(File,args)
        elif args.year == "2016":
            Apply2016ZPTReweighting(File,args)
