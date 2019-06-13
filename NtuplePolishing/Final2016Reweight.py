import ROOT
from array import array
from tqdm import tqdm 
import math
import argparse
import AddCrossSectionWeightings
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

    TheBranch = ReweightFile.mt_Selected.Branch('FinalWeighting',FinalWeighting,'FinalWeighitng/F')

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

        if FileName == "Data.root":
            Weight = 1.0           

        FinalWeighting[0]=Weight
        TheBranch.Fill()
    
    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate the final 2017 recipe reweighting")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    parser.add_argument('--year',choices=["2016","2017","2018"],help="Change the year of the corrections applied",nargs='?',default = "2016")
    parser.add_argument('--DisablePileupWeighting',help="Disable the pileup weighting",action="store_true")
    parser.add_argument('--UseInclusiveDY',help="Option for using non DY#.root files in cross section weighting",action="store_true")
    parser.add_argument('--DisableMuAndTriggerSFs',help="Disable the KIT style muon scale factors",action="store_true")    

    args = parser.parse_args()    

    for File in args.Files:        
        AddFinalWeights(File,args)
