import ROOT 
import argparse
from array import array
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a final fake ntuple out of components")
    parser.add_argument('DataFile',help="Data file where positive weights come from")
    parser.add_argument('MCFiles',nargs="+",help="MC ntuples where negative weights come from")
    parser.add_argument('--OutFileName',help="Output file name")

    args = parser.parse_args()
    
    FakeFile = ROOT.TFile(args.OutFileName,"RECREATE")

    MergeList = ROOT.TList()

    EntryTotal = 0
    PosFile = ROOT.TFile(args.DataFile)
    MergeList.append(PosFile.mt_Selected)
    EntryTotal+=PosFile.mt_Selected.GetEntries()

    OpenFile = []

    for File in args.MCFiles:        
        print("Adding "+File)        
        MCFile = ROOT.TFile(File)
        OpenFile.append(MCFile)
        FakeFile.cd()
        NewTree = MCFile.mt_Selected.CopyTree("gen_match_2 <= 5")
        EntryTotal += NewTree.GetEntries()
        MergeList.Add(NewTree)
    FakeFile.cd()
    NewNtuple=ROOT.TTree.MergeTrees(MergeList)
    print("New Ntuple Entries: "+str(NewNtuple.GetEntries())+"/"+str(EntryTotal))
    FakeFile.Write()
    FakeFile.Close()
    
