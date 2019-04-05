import ROOT
import sys
from array import array
from tqdm import tqdm 

def AddFinalWeights(FileToRun):
    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    FinalWeighting = array('f',[0])

    TheBranch = ReweightFile.mt_Selected.Branch('FinalWeighting',FinalWeighting,'FinalWeighitng/F')
    
    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)

        #At this point, the only weights available for 2018 are cross section,
        #and a 2017 Tau ID that we're calling hunky dory
        FileName = FileToRun[FileToRun.rfind("/")+1:]
        if(FileName != "Data.root" and FileName != "Embedded.root"):
            FinalWeighting[0] = ReweightFile.mt_Selected.CrossSectionWeighting * 0.89 #0.89 tight tau SF
        else:
            FinalWeighting[0] = 1.0
        TheBranch.Fill()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    for File in sys.argv[1:]:
        print("Creating final weights branch for: "+File)
        AddFinalWeights(File)
