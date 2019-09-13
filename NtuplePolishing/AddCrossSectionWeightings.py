import ROOT
import sys
from tqdm import tqdm
from array import array
import argparse

def DefineCrossSectionArguments(parser):
    pass

def AddCrossSectionWeightings(FileToRun,args):
    
    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")        
    TheTree=ReweightFile.mt_Selected
    CrossSectionWeighting = array('f',[0.])
    TheBranch = TheTree.Branch("CrossSectionWeighting",CrossSectionWeighting,"CrossSectionWeighting/F")
    #I believe this is the correct distribution to get?
    TotalNumberOfEvents = ReweightFile.eventCount.GetBinContent(2)    
    FileName = FileToRun[FileToRun.rfind("/")+1:]

    #let's differentiate between 2017 and 2018
    LHCLumi = 0        
    if(args.year == "2017"):            
        LHCLumi = 41.557e15                        
    elif(args.year == "2018"):
        LHCLumi = 59.74e15
    elif(args.year == "2016"):
        LHCLumi = 35.92e15

    #print(FileName)

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)        
        #start checking known samples
        CrossSection = 0.0
        if FileName == "DY.root":            
            CrossSection = 6225.42e-12        
        elif FileName == "TTTo2L2Nu.root":
            CrossSection = 88.29e-12
        elif FileName == "TTToSemiLeptonic.root":
            CrossSection = 365.35e-12
        elif FileName == "TTToHadronic.root":
            CrossSection = 377.96e-12
        elif FileName == "W.root":
            CrossSection = 61526.7e-12
        elif FileName == "Data.root":
            CrossSection = 1.0
        elif FileName == "Embedded.root":
            CrossSection = 1.0
        elif FileName == "ST_tW_antitop.root":
            CrossSection = 35.85e-12
        elif FileName == "ST_tW_top.root":
            CrossSection = 35.85e-12
        elif FileName == "ST_t_antitop.root":
            CrossSection = 26.23e-12
        elif FileName == "ST_t_top.root":
            CrossSection = 44.07e-12
        elif FileName == "ggH.root":
            CrossSection = 48.58e-12*0.0627
        elif FileName == "VBF.root":
            CrossSection = 3.782e-12*0.0627
        elif FileName == "WHPlus.root":
            CrossSection = 0.840e-12 * 0.0627
        elif FileName == "WHMinus.root":
            CrossSection = 0.5328e-12 * 0.0627
        elif FileName == "ZH.root":
            CrossSection = 0.8839e-12 * 0.0627
        elif FileName == "ZZ.root":
            CrossSection = 16.523e-12 * 0.0627
        elif FileName == "WZ.root":
            CrossSection = 47.13e-12
        elif FileName == "WW.root":
            CrossSection = 118.7e-12 * 0.0627
        elif FileName == "EWKZLL.root":
            CrossSection = 4.321e-12 * 0.0627
        elif FileName == "EWKZNuNu.root":
            CrossSection = 10.66e-12 * 0.0627        
        elif FileName == "TT.root":
            CrossSection = 831.76e-12
        elif FileName == "WW1L1Nu2Q.root":
            CrossSection = 49.997e-12
        elif FileName == "WZ1L1Nu2Q.root":
            CrossSection = 10.71e-12
        elif FileName == "WZ1L3Nu.root":
            CrossSection = 3.05e-12
        elif FileName == "WZ2L2Q.root":
            CrossSection = 5.595e-12
        elif FileName == "WZJLLLNu.root":
            CrossSection = 4.708e-12
        elif FileName == "ZZ4L.root":
            CrossSection = 1.212e-12
        elif FileName == "ZZ2L2Q.root":
            CrossSection = 3.22e-12
        else:
            print("Unrecognized input sample! Defaulting to unweighted events!")
            CrossSection = 1.0        
        if(FileName != "Data.root" and FileName != "Embedded.root"):
            CrossSectionWeighting[0] = CrossSection * LHCLumi / TotalNumberOfEvents
        else:
            CrossSectionWeighting[0] = 1.0
                
        #2017
        if(args.year == "2017"):
            if(FileName == "DY.root" and not args.UseInclusiveDY):
                CrossSectionWeighting[0] = 2.6458
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 0.8485
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 1.04686
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 1.6833
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 0.52944
            elif(FileName == "W.root"):
                CrossSectionWeighting[0] = 57.3077
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 4.15987
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 4.0297
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 2.36054
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 2.14099
        #2018
        elif(args.year == "2018"):
            if(FileName == "DY.root" and not args.UseInclusiveDY):
                CrossSectionWeighting[0] = 3.7118
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 0.64516
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 0.56494
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 0.61413
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 1.11472
            elif(FileName == "W.root"):
                CrossSectionWeighting[0] = 51.7495
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 10.8788
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 5.2527
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 3.10898
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 3.0223
        elif (args.year=="2016"):
            if(FileName == "DY.root" and not args.UseInclusiveDY):
                CrossSectionWeighting[0] = 1.5317
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 0.55526
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 0.51796
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 0.51866
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 0.51536
            elif(FileName == "W.root"):
                CrossSectionWeighting[0] = 25.427
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 6.8324
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 2.09433
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 0.687224
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 2.1343

        if(FileName != "Data.root"):
            CrossSectionWeighting[0] = CrossSectionWeighting[0] * TheTree.genweight            
            
        TheBranch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Generate and attach the crosss section weighting branch.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's cross sections are to be used")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    parser.add_argument('--UseInclusiveDY',help="Use only the inclusive DY sample (weight by nnlo cross section)",action="store_true")
    
    args = parser.parse_args()

    for File in args.Files:
        print("Processing the cross sections weights for "+File)
        AddCrossSectionWeightings(File,args)
        
    
