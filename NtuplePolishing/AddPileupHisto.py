import ROOT
from tqdm import tqdm
import argparse

def AddPileupHisto(File,args):
    UpdateFile = ROOT.TFile(File, "UPDATE")
    TheHisto = ROOT.TH1F("pileup_mc","pileup_mc",80,0.0,80.0)
    try:        
        TheTree = UpdateFile.mutau_tree
    except:
        try:
            TheTree = UpdateFile.mt_Selected
        except:
            print("Can't find a tree I understand!")
            raise

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TheHisto.Fill(TheTree.npu)
        
    TheHisto.Write()
    UpdateFile.Write()
    UpdateFile.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Generate Cecile's \"pileup_mc\" Histogram. ")
    parser.add_argument('Files',nargs="+",help="Files to generate histograms for")

    args = parser.parse_args()
    
    for File in args.Files:
        print("making histo for "+str(File))
        AddPileupHisto(File,args)
