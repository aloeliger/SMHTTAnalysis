import ROOT
import sys
from tqdm import tqdm
from array import array

def AddCrossSectionWeightings(FileToRun):
    
    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    CrossSectionWeighting = array('f',[0])

    TheBranch = ReweightFile.mt_tree.Branch('CrossSectionWeighting',CrossSectionWeighting,'CrossSectionWeighting/F')

    #I believe this is the correct distribution to get?
    TotalNumberOfEvents = ReweightFile.eventCount.GetBinContent(1)    

    for i in tqdm(range(ReweightFile.mt_tree.GetEntries())):
        ReweightFile.mt_tree.GetEntry(i)
        
        LHCLumi = 41.557e15
        if ("WW.root" in FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 118.7e-12 / TotalNumberOfEvents
        elif ("WZ.root" in FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 47.13e-12 / TotalNumberOfEvents
        elif("ZZ.root" in FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 16.523e-12 / TotalNumberOfEvents
        elif("W.root" in FileToRun
             or "W1.root" in FileToRun
             or "W2.root" in FileToRun
             or "W3.root" in FileToRun
             or "W4.root" in FileToRun):
            if(ReweightFile.mt_tree.numGenJets==0):
                CrossSectionWeighting[0] = 110.1887
            elif(ReweightFile.mt_tree.numGenJets==1):
                CrossSectionWeighting[0] = 14.1549
            elif(ReweightFile.mt_tree.numGenJets==2):
                CrossSectionWeighting[0] = 7.43847
            elif(ReweightFile.mt_tree.numGenJets==3):
                CrossSectionWeighting[0] = 2.40205
            elif(ReweightFile.mt_tree.numGenJets==4):
                CrossSectionWeighting[0] = 2.14075
        elif("TTTo2L2Nu.root" in FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 88.34e-12 / TotalNumberOfEvents
        elif("TTToHadronic.root" in FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 377.96e-12 / TotalNumberOfEvents
        elif("TTToSemiLeptonic.root" in  FileToRun):
            CrossSectionWeighting[0] = LHCLumi * 365.45e-12 / TotalNumberOfEvents
        elif("DY.root" in FileToRun
             or "DY1.root" in FileToRun
             or "DY2.root" in FileToRun
             or "DY3.root" in FileToRun
             or "DY4.root" in FileToRun):
            if(ReweightFile.mt_tree.numGenJets==0):
                CrossSectionWeighting[0] = 3.009
            elif(ReweightFile.mt_tree.numGenJets==1):
                CrossSectionWeighting[0] = 0.589
            elif(ReweightFile.mt_tree.numGenJets==2):
                CrossSectionWeighting[0] = 0.612
            elif(ReweightFile.mt_tree.numGenJets==3):
                CrossSectionWeighting[0] = 0.767
            elif(ReweightFile.mt_tree.numGenJets==4):
                CrossSectionWeighting[0] = 0.690
        elif("Data.root" in  FileToRun):
            CrossSectionWeighting[0] = 1.0
        else:
            print("Unrecognized input sample! Defaulting to unweighted events!")
            
        #print("Cross Section Weighting: "+str(CrossSectionWeighting))
        TheBranch.Fill()

    ReweightFile.mt_tree.Write()
    ReweightFile.Write()
    ReweightFile.Close()

if __name__ == "__main__":
    for File in sys.argv[1:]:
        print("Processing the cross sections weights for "+File)
        AddCrossSectionWeightings(File)
