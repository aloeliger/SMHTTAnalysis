import ROOT
import sys
from array import array
from tqdm import tqdm
import argparse
import AddPileupHisto

def GenerateTheWeights(File,args):
    print("Generating weights for this file...") 
    if args.year == "2016":
        raise RuntimeError("2016 not implemented yet. Implement Me!")
    elif args.year == "2017":
        TheDataFile = ROOT.TFile("Weightings/2017DataPileupHistogram.root")
    elif args.year == "2018":
        TheDataFile = ROOT.TFile("Weightings/2018DataPileupHistogram.root")
    TheFile = ROOT.TFile(File)
    assert(TheDataFile.pileup),"Pileup Histogram for data not provided! Can't be generated!"
    try:
        TheFile.pileup_mc
    except:
        print("Found no Pileup histo in the file...")
        print("Creating it...")
        AddPileupHisto.AddPileupHisto(File,args)
    #reload the file        
    TheFile.Close()    
    TheFile = ROOT.TFile(File)

    #now we make the weighting histogram
    TheWeightsHisto = TheDataFile.pileup.Clone()
    TheWeightsHisto.Scale(1.0/TheWeightsHisto.Integral())
    TheMCHisto = TheFile.pileup_mc.Clone()
    TheMCHisto.Scale(1.0/TheMCHisto.Integral())

    TheWeightsHisto.Divide(TheMCHisto)
    TheWeightsHisto.SetDirectory(0)        

    return TheWeightsHisto

def AddPileupWeightings(File,args):
    WeightHisto = GenerateTheWeights(File,args)    
    TheFile = ROOT.TFile(File,"UPDATE")
    TheTree = TheFile.mt_Selected

    PileupWeight = array('f',[0.])
    PileupBranch = TheTree.Branch("PileupWeight",PileupWeight,"PileupWeight/F")

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)        
        PileupWeight[0] = WeightHisto.GetBinContent(WeightHisto.FindBin(TheTree.npu))        
        PileupBranch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach pileup weighting branches.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select whicn year's corrections are to be used")    
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")
    
    args = parser.parse_args()
    
    for File in args.Files:                  
        AddPileupWeightings(File,args)
