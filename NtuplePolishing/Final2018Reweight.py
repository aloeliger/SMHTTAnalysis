import ROOT
import sys
from array import array
from tqdm import tqdm 
import argparse
import AddCrossSectionWeightings
import AddPileupWeightings
import AddKITMuSFs

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
    TheBranch = ReweightFile.mt_Selected.Branch('FinalWeighting',FinalWeighting,'FinalWeighitng/F')
    
    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2,ReweightFile.mt_Selected.eta_2,ReweightFile.mt_Selected.phi_2,ReweightFile.mt_Selected.m_2)
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2,ReweightFile.mt_Selected.eta_1,ReweightFile.mt_Selected.phi_2,ReweightFile.mt_Selected.m_1)
        MetVector=ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(ReweightFile.mt_Selected.met,0.0,ReweightFile.mt_Selected.metphi,0.0)

        #all we have for 2018 so far is cross section and pileup weight
        #we're just using 2017 Tau ID SF temporarily
        Weight = ReweightFile.mt_Selected.CrossSectionWeighting        
        
        if(not args.DisablePileupWeighting and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.PileupWeight
        if( not args.DisableMuSFs and FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * ReweightFile.mt_Selected.MuSF

        if(FileName != "Data.root" and FileName != "Embedded.root"):
            Weight = Weight * 0.89 #0.89 tight tau ID

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

        #ALWAYS
        if FileName == "Data.root":
            Weight = 1.0
        FinalWeighting[0] = Weight
        TheBranch.Fill()
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
    
    args=parser.parse_args()

    for File in args.Files:        
        AddFinalWeights(File,args)
