import ROOT
import sys
from tqdm import tqdm
from array import array
import argparse

def AddCrossSectionWeightings(FileToRun,args):
    
    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")        
    TheTree=ReweightFile.mt_Selected
    CrossSectionWeighting = array('f',[0.])
    TheBranch = TheTree.Branch("CrossSectionWeighting",CrossSectionWeighting,"CrossSectionWeighting/F")
    #I believe this is the correct distribution to get?
    TotalNumberOfEvents = ReweightFile.eventCount.GetBinContent(1)    
    FileName = FileToRun[FileToRun.rfind("/")+1:]
    print(FileName)
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        #let's differentiate between 2017 and 2018
        LHCLumi = 0        
        if(args.year == "2017"):            
            LHCLumi = 41.557e15                        
        elif(args.year == "2018"):
            LHCLumi = 59.97e15
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
        else:
            print("Unrecognized input sample! Defaulting to unweighted events!")
            CrossSection = 1.0        
        if(FileName != "Data.root" and FileName != "Embedded.root"):
            CrossSectionWeighting[0] = CrossSection * LHCLumi / TotalNumberOfEvents
        else:
            CrossSectionWeighting[0] = 1.0
        #2017
        if(args.year == "2017"):
            if(FileName == "DY.root"):                
                CrossSectionWeighting[0] = 2.665
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 0.5517
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 1.066
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 0.5977
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 0.2933
            elif(FileName == "W.root"):
                CrossSectionWeighting[0] = 32.7
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 7.05
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 13.89
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 2.27
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 1.05
        #2018
        elif(args.year == "2018"):
            if(FileName == "DY.root"):                
                CrossSectionWeighting[0] = 3.7
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 0.64
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 0.56
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 1.13
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 0.84
            elif(FileName == "W.root"):
                CrossSectionWeighting[0] = 62.95
                if ReweightFile.mt_Selected.numGenJets == 1:
                    CrossSectionWeighting[0] = 17.95
                elif ReweightFile.mt_Selected.numGenJets == 2:
                    CrossSectionWeighting[0] = 4.56
                elif ReweightFile.mt_Selected.numGenJets == 3:
                    CrossSectionWeighting[0] = 3.14
                elif ReweightFile.mt_Selected.numGenJets == 4:
                    CrossSectionWeighting[0] = 3.25
        #print("Cross Section: "+str(CrossSection))
        #print("Total Number Of Events:"+str(TotalNumberOfEvents))
        #print("LHCLumi: "+str(LHCLumi))        
        #print("Cross Section Weighting: "+str(CrossSectionWeighting[0]))
        TheBranch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Generate and attach the crosss section weighting branch.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's cross sections are to be used")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")
    
    args = parser.parse_args()

    for File in args.Files:
        print("Processing the cross sections weights for "+File)
        AddCrossSectionWeightings(File,args)
        
    
