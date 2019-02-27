import ROOT
import sys
from array import array
from tqdm import tqdm 
import math
import argparse

def AddFinalWeights(FileToRun,args):
    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    FileName = FileToRun[FileToRun.rfind("/")+1:]
    FinalWeighting = array('f',[0])

    TheBranch = ReweightFile.mt_Selected.Branch('FinalWeighting',FinalWeighting,'FinalWeighitng/F')
    
    FirstScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_v17_5.root")
    FirstWorkSpace = FirstScaleFactorFile.w

    SecondScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_2017_v2.root")
    SecondWorkSpace = SecondScaleFactorFile.w

    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1, ReweightFile.mt_Selected.eta_1, ReweightFile.mt_Selected.phi_1, ReweightFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2, ReweightFile.mt_Selected.eta_2, ReweightFile.mt_Selected.phi_2, ReweightFile.mt_Selected.m_2)

        Weight = ReweightFile.mt_Selected.CrossSectionWeighting #cross section
        #cecile includes genweight in lumi calc...
        
        #cecile says that embedded weights start as the genweight
        if FileName == "Embedded.root": 
            Weight = ReweightFile.mt_Selected.genweight 

        #Tau ID weighting
        if FileName != "Embedded.root" and FileName != "Data.root":
            Weight = Weight * 0.89
        elif FileName == "Embedded.root":
            Weight = Weight * 0.97

        #I don't know what the heck this correction is:
        #but Cecile has it
        if not args.DisableEtaWeighting:
            if(ReweightFile.mt_Selected.gen_match_2 == 2
               or ReweightFile.mt_Selected.gen_match_2 == 4):
                if(abs(TauVector.Eta())<0.8):
                    Weight = Weight * 1.29
                elif(abs(TauVector.Eta())<1/2):
                    Weight = Weight * 1.14
                elif(abs(TauVector.Eta())):
                    Weight = Weight*0.93
                elif(abs(TauVector.Eta())):
                    Weight = Weight*1.61                                

        Trigger24 = (ReweightFile.mt_Selected.passMu24 and ReweightFile.mt_Selected.matchMu24_1 
                 and ReweightFile.mt_Selected.filterMu24_1 and ReweightFile.mt_Selected.pt_1 > 25.0)
        Trigger27 = (ReweightFile.mt_Selected.passMu27 and ReweightFile.mt_Selected.matchMu27_1 
                 and ReweightFile.mt_Selected.filterMu27_1 and ReweightFile.mt_Selected.pt_1 > 28.0)
        Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 and ReweightFile.mt_Selected.matchMu20Tau27_1 
                   and ReweightFile.mt_Selected.filterMu20Tau27_1                    
                   and ReweightFile.mt_Selected.filterMu20Tau27_2
                   and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_2 > 31 
                   and ReweightFile.mt_Selected.pt_1 < 25
                   and abs(ReweightFile.mt_Selected.eta_2 < 2.1))
    #no tau trigger matching in embedded
        if(FileName == "Embedded.root"):
            Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 and ReweightFile.mt_Selected.matchMu20Tau27_1 
                           and ReweightFile.mt_Selected.filterMu20Tau27_1
                           and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_2 > 31 
                           and ReweightFile.mt_Selected.pt_1 < 25
                           and abs(ReweightFile.mt_Selected.eta_2 < 2.1))
            
        #Embedded trigger whatever
        if not args.DisableEmbeddingReconstructionWeighting:
            if(FileName == "Embedded.root"):
                if ReweightFile.mt_Selected.l2_decayMode == 0:
                    Weight = Weight * 0.975
                elif ReweightFile.mt_Selected.l2_decayMode == 1:
                    Weight = Weight * 0.975 * 1.051
                elif ReweightFile.mt_Selected.l2_decayMode == 10:
                    Weight = Weight * 0.975 * 0.975 * 0.975
                FirstWorkSpace.var("m_pt").setVal(MuVector.Pt())
                FirstWorkSpace.var("m_eta").setVal(MuVector.Eta())
                FirstWorkSpace.var("gt_pt").setVal(MuVector.Pt())
                FirstWorkSpace.var("gt_eta").setVal(MuVector.Eta())
                Weight = Weight * FirstWorkSpace.function("m_sel_idEmb_ratio").getVal()
                FirstWorkSpace.var("gt_pt").setVal(TauVector.Pt())
                FirstWorkSpace.var("gt_eta").setVal(TauVector.Eta())
                Weight = Weight * FirstWorkSpace.function("m_sel_idEmb_ratio").getVal()
                FirstWorkSpace.var("gt1_pt").setVal(MuVector.Pt())
                FirstWorkSpace.var("gt1_eta").setVal(MuVector.Eta())
                FirstWorkSpace.var("gt2_pt").setVal(TauVector.Pt())
                FirstWorkSpace.var("gt2_eta").setVal(TauVector.Eta())
                Weight=Weight*FirstWorkSpace.function("m_sel_trg_ratio").getVal()
                Weight=Weight*FirstWorkSpace.function("m_iso_binned_embed_kit_ratio").getVal()
                Weight = Weight*FirstWorkSpace.function("m_id_embed_kit_ratio").getVal()
                if(Trigger24 or Trigger27):
                    Weight = Weight*FirstWorkSpace.function("m_trg24_27_embed_kit_ratio").getVal()
                
        #Top pT reweighting
        if not args.DisableTopReweighting:
            TopFactor = 1.0
            if(FileName == "TTToHadronic.root"
               or FileName == "TTToSemiLeptonic.root"
               or FileName == "TTTo2L2Nu.root"):
                pttop1 = ReweightFile.mt_Selected.pt_top1
                if pttop1 > 400:
                    pttop1 = 400
                pttop2 = ReweightFile.mt_Selected.pt_top2
                if pttop2 > 400:
                    pttop2 = 400
                topfactor = math.sqrt(math.exp(0.0615-0.0005*pttop1)*math.exp(0.0615-0.0005*pttop2))
                Weight = Weight * TopFactor
        
        #ZPT Weighting
        if not args.DisableZPTReweighting:
            ZPTWeight = 1.0
            if(FileName != "Embedded.root"
               and FileName != "Data.root"):
                SecondWorkSpace.var("m_pt").setVal(MuVector.Pt())
                SecondWorkSpace.var("m_eta").setVal(MuVector.Eta())
                SecondWorkSpace.var("z_gen_mass").setVal(ReweightFile.mt_Selected.genM)
                SecondWorkSpace.var("z_gen_pt").setVal(ReweightFile.mt_Selected.genpT)
                Weight=Weight*SecondWorkSpace.function("m_iso_kit_ratio").getVal()
                Weight=Weight*SecondWorkSpace.function("m_id_kit_ratio").getVal()
                ZPTWeight = SecondWorkSpace.function("zptmass_weight_nom").getVal()
                if(FileName == "DY.root"):
                    Weight = Weight * ZPTWeight
                if(Trigger24 or Trigger27):
                    Weight = Weight * SecondWorkSpace.function("m_trg24_27_kit_data").getVal()/SecondWorkSpace.function("m_trg24_27_kit_mc").getVal()
                else:
                    Weight = Weight * (SecondWorkSpace.function("m_trg20_data").getVal()/SecondWorkSpace.function("m_trg20_mc").getVal())*ReweightFile.mt_Selected.DiTauTriggerWeight
        
                    
        #ALWAYS
        if FileName == "Data.root":
            Weight = 1.0           

        FinalWeighting[0]=Weight
        
        TheBranch.Fill()
    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate the final 2017 reweighting")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    parser.add_argument('--DisableGenWeighting',help="Disable genweighting",action="store_true")
    parser.add_argument('--DisableEtaWeighting',help="Disable the Eta based reweighting",action="store_true")
    parser.add_argument('--DisableEmbeddingReconstructionWeighting',help="Disable Embedded track and trigger based weights",action="store_true")
    parser.add_argument('--DisableTopReweighting',help="Disable top reweighting",action="store_true")
    parser.add_argument('--DisableZPTReweighting',help="Disable Z Pt reweighting",action="store_true")
    
    args = parser.parse_args()

    for File in args.Files:
        print("Creating final weights branch for: "+File)
        AddFinalWeights(File,args)
