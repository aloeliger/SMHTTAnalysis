import ROOT
from array import array
from tqdm import tqdm 
import math
import argparse
import AddCrossSectionWeightings
import AddZPTReweighting
import AddPileupWeightings
import AddKITMuAndTriggerSFs

def AddFinalWeights(FileToRun,args):
    print("")
    print("Creating final weights branch for: "+FileToRun)
    print("")
    CheckFile = ROOT.TFile(FileToRun)
    #make the name easier to understand
    FileName = FileToRun[FileToRun.rfind("/")+1:]
    #Need cross section weighting. Check for it
    try: 
        CheckFile.mt_Selected.CrossSectionWeighting
    except:
        print("Failed to find cross section weightings. Adding them...")
        AddCrossSectionWeightings.AddCrossSectionWeightings(FileToRun,args)
    try:
        CheckFile.mt_Selected.ZPTWeighting
    except:
        print("Failed to find ZPT Weights. Adding them...")
        AddZPTReweighting.Apply2016ZPTReweighting(FileToRun,args)
    if FileName != "Data.root" and FileName != "Embedded.root":
        try:
            CheckFile.mt_Selected.PileupWeight
        except:
            print("Failed to find pileup weights. Adding them...")
            AddPileupWeightings.AddPileupWeightings(FileToRun,args)
        try:
            CheckFile.mt_Selected.MuAndTriggerSF
        except:
            print("Failed to find muon scale factors. Adding them...")
            AddKITMuAndTriggerSFs.AddKITMuAndTriggerSFs(FileToRun,args)
    CheckFile.Close()

    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")    
    #we create different weights for different shapes.
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

    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1, ReweightFile.mt_Selected.eta_1, ReweightFile.mt_Selected.phi_1, ReweightFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2, ReweightFile.mt_Selected.eta_2, ReweightFile.mt_Selected.phi_2, ReweightFile.mt_Selected.m_2)

        Weight = ReweightFile.mt_Selected.CrossSectionWeighting #cross section
        #if not a data file, pileup reweight it
        if( not args.DisablePileupWeighting and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.PileupWeight
        #possible overlap on trigger SFs?
        if( not args.DisableMuAndTriggerSFs and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.MuAndTriggerSF
        if FileName != "Embedded.root" and FileName != "Data.root":
            Weight = Weight * 0.87

        #mu->tau FR Sf's
        if not args.DisableEtaWeighting:
            if(ReweightFile.mt_Selected.gen_match_2 == 2
               or ReweightFile.mt_Selected.gen_match_2 == 4):
                if(abs(TauVector.Eta())<0.4):
                    Weight=Weight * 1.47
                elif(abs(TauVector.Eta())<0.8):
                    Weight=Weight * 1.55
                elif(abs(TauVector.Eta())<1.2):
                    Weight=Weight * 1.33
                elif(abs(TauVector.Eta())<1.7):
                    Weight=Weight * 1.72
                elif(abs(TauVector.Eta())<2.3):
                    Weight=Weight * 2.50
            elif(ReweightFile.mt_Selected.gen_match_2 == 1
               or ReweightFile.mt_Selected.gen_match_2 ==3):
                if(abs(TauVector.Eta())<1.460):
                    Weight=Weight*1.21
                elif(abs(TauVector.Eta())>=1.559):
                    Weight=Weight*1.38

        #Top PT Reweighting
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
            
        #ZPT Weighting
        if not args.DisableZPTWeighting:
            Weight_ZPT_DOWN = Weight * ReweightFile.mt_Selected.ZPTWeighting_DOWN
            Weight_ZPT_UP = Weight * ReweightFile.mt_Selected.ZPTWeighting_UP
            Weight = Weight * ReweightFile.mt_Selected.ZPTWeighting

        if FileName == "Data.root":
            Weight = 1.0           

        FinalWeighting[0]=Weight
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
    parser = argparse.ArgumentParser(description="Generate the final 2017 recipe reweighting")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    parser.add_argument('--year',choices=["2016","2017","2018"],help="Change the year of the corrections applied",nargs='?',default = "2016")
    parser.add_argument('--DisablePileupWeighting',help="Disable the pileup weighting",action="store_true")
    parser.add_argument('--DisableTopReweighting',help="Disable top reweighting",action="store_true")
    parser.add_argument('--DisableZPTWeighting',help="Disable Z Pt reweighting",action="store_true")
    parser.add_argument('--DisableEtaWeighting',help="Disable the Eta based reweighting",action="store_true")
    parser.add_argument('--UseInclusiveDY',help="Option for using non DY#.root files in cross section weighting",action="store_true")
    parser.add_argument('--DisableMuAndTriggerSFs',help="Disable the KIT style muon scale factors",action="store_true")    

    args = parser.parse_args()    

    for File in args.Files:        
        AddFinalWeights(File,args)
