import ROOT
import sys
from array import array
from tqdm import tqdm 
import argparse
import AddCrossSectionWeightings
import AddPileupWeightings
import AddKITMuSFs
import AddZPTReweighting
import math

def AddFinalWeights(FileToRun, args):
    print("")
    print("Creating final weights branch for "+FileToRun)
    print("")

    CheckFile = ROOT.TFile(FileToRun)
    FileName = FileToRun[FileToRun.rfind("/")+1:]

    try: 
        CheckFile.mt_Selected.CrossSectionWeighting
    except:
        print("Failed to find cross section weightings. Adding them...")
        AddCrossSectionWeightings.AddCrossSectionWeightings(FileToRun,args)
    try:
        CheckFile.mt_Selected.ZPTWeighting
    except:
        print("Failed to find ZPT weights. Adding them...")
        AddZPTReweighting.ApplyZPTReweighting(FileToRun,args)
    if FileName != "Data.root" and FileName != "Embedded.root":
        try:
            CheckFile.mt_Selected.PileupWeight
        except:
            print("Failed to find pileup weights. Adding them...")
            AddPileupWeightings.AddPileupWeightings(FileToRun,args)
        try:
            CheckFile.mt_Selected.MuSF
        except:
            print("Failed to find mu scale factors. Adding them...")
            AddKITMuSFs.AddKITMuSFs(FileToRun,args)
    CheckFile.Close()

    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    FinalWeighting = array('f',[0])
    FinalWeighting_ZPT_DOWN = array('f',[0])
    FinalWeighting_ZPT_UP = array('f',[0])
    FinalWeighting_TOP_UP = array('f',[0])
    FinalWeighting_TOP_DOWN = array('f',[0])
    
    TheBranch = ReweightFile.mt_Selected.Branch('FinalWeighting',FinalWeighting,'FinalWeighitng/F')
    TheBranch_ZPT_DOWN = ReweightFile.mt_Selected.Branch('FinalWeighting_ZPT_DOWN',FinalWeighting_ZPT_DOWN,'FinalWeighitng_ZPT_DOWN/F')
    TheBranch_ZPT_UP = ReweightFile.mt_Selected.Branch('FinalWeighting_ZPT_UP',FinalWeighting_ZPT_UP,'FinalWeighting_ZPT_UP/F')
    TheBranch_TOP_UP = ReweightFile.mt_Selected.Branch('FinalWeighting_TOP_UP',FinalWeighting_TOP_UP,'FinalWeighting_TOP_UP/F')
    TheBranch_TOP_DOWN = ReweightFile.mt_Selected.Branch('FinalWeighting_TOP_DOWN',FinalWeighting_TOP_DOWN,'FinalWeighting_TOP_DOWN/F')

    #get the embedded weighting file.
    ScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_v18_2.root")
    ScaleFactorWorkspace = ScaleFactorFile.w

    print("Adding the final weighting...")
    
    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2,ReweightFile.mt_Selected.eta_2,ReweightFile.mt_Selected.phi_2,ReweightFile.mt_Selected.m_2)
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1,ReweightFile.mt_Selected.eta_1,ReweightFile.mt_Selected.phi_1,ReweightFile.mt_Selected.m_1)
        MetVector=ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(ReweightFile.mt_Selected.met,0.0,ReweightFile.mt_Selected.metphi,0.0)

        #all we have for 2018 so far is cross section and pileup weight
        #we're just using 2017 Tau ID SF temporarily
        Weight = ReweightFile.mt_Selected.CrossSectionWeighting        
        
        if(not args.DisablePileupWeighting and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.PileupWeight
            Weight = Weight * ReweightFile.mt_Selected.bweight # add in the btagging weight to MCs
        if( not args.DisableMuSFs and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.MuSF

        if(FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * 0.90 #0.90 tight tau ID
        elif FileName == "Embedded.root":
            pass #need 2018 tau ID on embedded

        if not args.DisableEtaWeighting:
            if(ReweightFile.mt_Selected.gen_match_2 == 2
               or ReweightFile.mt_Selected.gen_match_2 == 4):
                 if(abs(TauVector.Eta())<0.4):
                     Weight = Weight * 1.28
                 elif(abs(TauVector.Eta())<0.8):
                     Weight = Weight * 1.2
                 elif(abs(TauVector.Eta())<1.2):
                     Weight = Weight*1.08
                 elif(abs(TauVector.Eta())<1.7):
                     Weight = Weight*1.0      
                 elif(abs(TauVector.Eta())<2.3):
                     Weight = Weight*2.3

        Trigger24 = (ReweightFile.mt_Selected.passMu24 and ReweightFile.mt_Selected.matchMu24_1 
                 and ReweightFile.mt_Selected.filterMu24_1 and ReweightFile.mt_Selected.pt_1 > 25.0)
        Trigger27 = (ReweightFile.mt_Selected.passMu27 and ReweightFile.mt_Selected.matchMu27_1 
                 and ReweightFile.mt_Selected.filterMu27_1 and ReweightFile.mt_Selected.pt_1 > 25.0)            
        if FileName == "Data.root":
            if (ReweightFile.mt_Selected.run >= 317509): #hps trigger
                Trigger2027 = (ReweightFile.mt_Selected.passMu20HPSTau27 
                               and ReweightFile.mt_Selected.matchMu20HPSTau27_1
                               and ReweightFile.mt_Selected.matchMu20HPSTau27_2
                               and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                               and ReweightFile.mt_Selected.pt_2 > 28
                               and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                               and abs(ReweightFile.mt_Selected.eta_2) < 2.1
                               and ReweightFile.mt_Selected.filterMu20HPSTau27_1
                               and ReweightFile.mt_Selected.filterMu20HPSTau27_2)
            if (ReweightFile.mt_Selected.run < 317509): #non hps trigger
                Trigger2027 = (ReweightFile.mt_Selected.passMu20Tau27 
                               and ReweightFile.mt_Selected.matchMu20Tau27_1
                               and ReweightFile.mt_Selected.matchMu20Tau27_2
                               and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                               and ReweightFile.mt_Selected.pt_2 > 28
                               and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                               and abs(ReweightFile.mt_Selected.eta_2) < 2.1
                               and ReweightFile.mt_Selected.filterMu20Tau27_1
                               and ReweightFile.mt_Selected.filterMu20Tau27_2)
        elif FileName == "Embedded.root": # embedded doesn't match taus
            Trigger24 = (ReweightFile.mt_Selected.passMu24 and ReweightFile.mt_Selected.matchMu24_1 
                         and ReweightFile.mt_Selected.matchEmbFilter_Mu24_1 and ReweightFile.mt_Selected.pt_1 > 25.0)
            Trigger27 = (ReweightFile.mt_Selected.passMu27 and ReweightFile.mt_Selected.matchMu27_1 
                         and ReweightFile.mt_Selected.matchEmbFilter_Mu27_1 and ReweightFile.mt_Selected.pt_1 > 28.0)            
            Trigger2027 = (ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                           and ReweightFile.mt_Selected.pt_2 > 28
                           and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                           and abs(ReweightFile.mt_Selected.eta_2) < 2.1
                           and ReweightFile.mt_Selected.matchEmbFilter_Mu20Tau27_1
                           and (ReweightFile.mt_Selected.matchEmbFilter_Mu20Tau27_2 or ReweightFile.mt_Selected.matchEmbFilter_Mu20HPSTau27_2))
        else: #all hps cross trigger
            Trigger2027 = (ReweightFile.mt_Selected.passMu20HPSTau27 
                           and ReweightFile.mt_Selected.matchMu20HPSTau27_1
                           and ReweightFile.mt_Selected.matchMu20HPSTau27_2
                           and ReweightFile.mt_Selected.pt_1 > 21 and ReweightFile.mt_Selected.pt_1 < 25
                           and ReweightFile.mt_Selected.pt_2 > 28
                           and abs(ReweightFile.mt_Selected.eta_1) < 2.1
                           and abs(ReweightFile.mt_Selected.eta_2) < 2.1
                           and ReweightFile.mt_Selected.filterMu20HPSTau27_1
                           and ReweightFile.mt_Selected.filterMu20HPSTau27_2)

        if not args.DisableEmbeddingReconstructionWeighting:
            if(FileName == "Embedded.root"):
                if ReweightFile.mt_Selected.l2_decayMode == 0:
                    Weight = Weight * 0.975
                elif ReweightFile.mt_Selected.l2_decayMode == 1:
                    Weight = Weight * 0.975 * 1.051
                elif ReweightFile.mt_Selected.l2_decayMode == 10:
                    Weight = Weight * 0.975 * 0.975 * 0.975
                ScaleFactorWorkspace.var("m_pt").setVal(MuVector.Pt())
                ScaleFactorWorkspace.var("m_eta").setVal(MuVector.Eta())
                ScaleFactorWorkspace.var("gt_pt").setVal(MuVector.Pt())
                ScaleFactorWorkspace.var("gt_eta").setVal(MuVector.Eta())                
                ScaleFactorWorkspace.var("gt1_pt").setVal(MuVector.Pt())
                ScaleFactorWorkspace.var("gt1_eta").setVal(MuVector.Eta())
                ScaleFactorWorkspace.var("gt2_pt").setVal(TauVector.Pt())
                ScaleFactorWorkspace.var("gt2_eta").setVal(TauVector.Eta())
                ScaleFactorWorkspace.var("m_iso").setVal(ReweightFile.mt_Selected.iso_1)
                ScaleFactorWorkspace.var("t_pt").setVal(TauVector.Pt())
                Weight=Weight*ScaleFactorWorkspace.function("m_sel_trg_ratio").getVal()
                Weight = Weight * ScaleFactorWorkspace.function("m_sel_idEmb_ratio").getVal()                
                ScaleFactorWorkspace.var("gt_pt").setVal(TauVector.Pt())
                ScaleFactorWorkspace.var("gt_eta").setVal(TauVector.Eta())
                Weight = Weight * ScaleFactorWorkspace.function("m_sel_idEmb_ratio").getVal()
                Weight=Weight*ScaleFactorWorkspace.function("m_iso_binned_embed_kit_ratio").getVal()
                Weight = Weight*ScaleFactorWorkspace.function("m_id_embed_kit_ratio").getVal()
                if(Trigger24 or Trigger27):
                    Weight = Weight*ScaleFactorWorkspace.function("m_trg24_27_embed_kit_ratio").getVal()
                elif(Trigger2027):                                        
                    if ScaleFactorWorkspace.function("m_trg_MuTau_Mu20Leg_embed_kit_ratio").getVal() > 1.2:
                        print ""
                        print("Weight: "+str(ScaleFactorWorkspace.function("m_trg_MuTau_Mu20Leg_embed_kit_ratio").getVal()))
                        print("Mu Vector:")
                        print("Pt: "+str(MuVector.Pt()))
                        print("eta: "+str(MuVector.Eta()))
                    Weight = Weight*ScaleFactorWorkspace.function("m_trg_MuTau_Mu20Leg_embed_kit_ratio").getVal() #This weight causes huge problems
                    #Weight = Weight*ScaleFactorWorkspace.function("mt_emb_LooseChargedIsoPFTau27_kit_ratio").getVal()
                    Weight = Weight*ScaleFactorWorkspace.function("mt_emb_LooseChargedIsoPFTau27_tight_kit_ratio").getVal()
                else:
                    print("Something weird went through our trigger definitions.")
                     
        #top pt reweighting
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
                Weight_TOP_UP = Weight * (2.0 * (topfactor - 1.0) + 1.0)
                Weight_TOP_DOWN = Weight
                Weight = Weight * TopFactor
        
        if not args.DisableZPTWeighting:
            Weight_ZPT_DOWN = Weight * ReweightFile.mt_Selected.ZPTWeighting_DOWN
            Weight_ZPT_UP = Weight * ReweightFile.mt_Selected.ZPTWeighting_UP
            Weight = Weight * ReweightFile.mt_Selected.ZPTWeighting

        #ALWAYS
        if FileName == "Data.root":
            Weight = 1.0
        FinalWeighting[0] = Weight        
        if not args.DisableZPTWeighting:
            FinalWeighting_ZPT_DOWN[0] = Weight_ZPT_DOWN
            FinalWeighting_ZPT_UP[0] = Weight_ZPT_UP
        if not args.DisableTopReweighting and (FileName == "TTToHadronic.root"
                                               or FileName == "TTToSemiLeptonic.root"
                                               or FileName == "TTTo2L2Nu.root"):
            FinalWeighting_TOP_UP[0] = Weight_TOP_UP
            FinalWeighting_TOP_DOWN[0] = Weight_TOP_DOWN
        
        TheBranch.Fill()
        if not args.DisableZPTWeighting:
            TheBranch_ZPT_DOWN.Fill()
            TheBranch_ZPT_UP.Fill()
        if not args.DisableTopReweighting and (FileName == "TTToHadronic.root"
                                               or FileName == "TTToSemiLeptonic.root"
                                               or FileName == "TTTo2L2Nu.root"):
            TheBranch_TOP_UP.Fill()
            TheBranch_TOP_DOWN.Fill()
    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate the final 218 recipe reweighting")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    parser.add_argument('--year',choices=["2016","2017","2018"],help="change the year of the corrections applied",nargs='?',default="2018")
    parser.add_argument('--DisablePileupWeighting',help="Disable the pileup weighting",action="store_true")
    parser.add_argument('--UseInclusiveDY',help="Using only the inclusive DY file",action="store_true")
    parser.add_argument('--DisableMuSFs',help="Disable KIT style mu SFs.",action="store_true")
    parser.add_argument('--DisableEtaWeighting',help="Disable the eta based mu weights.",action="store_true")
    parser.add_argument('--DisableEmbeddingReconstructionWeighting',help="Disable Embedded track and trigger based weights",action="store_true")
    parser.add_argument('--DisableZPTWeighting',help="Disable the ZPT reweighting",action="store_true")
    parser.add_argument('--DisableTopReweighting',help="Disable the top pt based reweighting",action="store_true")
    
    args=parser.parse_args()

    for File in args.Files:        
        AddFinalWeights(File,args)
