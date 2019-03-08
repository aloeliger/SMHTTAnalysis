import ROOT
import sys
import argparse
import os

def PruneBranch(TheFile,args):
    PruneFile = ROOT.TFile(TheFile,"UPDATE")
    if args.TauIDNtuple:
        TheTree = PruneFile.mutau_tree
    else:
        TheTree= PruneFile.mt_Selected
    
    NewFile = ROOT.TFile("Temporary.root","RECREATE")
    AlreadyGrabbedItems = []
    
    for Thing in PruneFile.GetListOfKeys():
        if Thing.GetName() not in AlreadyGrabbedItems:
            obj = PruneFile.Get(Thing.GetName())
            NewFile.cd()
            if type(obj) == type(ROOT.TTree()):
                try:
                    obj.GetBranch(args.Branch).SetStatus(0)
                except:
                    print("Didn't find the branch: "+args.Branch+" in: "+obj.GetName())
                obj = obj.CloneTree(-1,"fast")
            obj.Write()
            AlreadyGrabbedItems.append(Thing.GetName())
    NewFile.Write()
    #clobber the old file with the old branch in place
    os.system("mv Temporary.root "+TheFile)

if __name__== "__main__":
    parser = argparse.ArgumentParser(description="Create identical trees without the specified branches")
    parser.add_argument('Branch',help = "Name of the branch to be pruned from the files")
    parser.add_argument('Files',nargs="+",help="List of files to remove the selected branch from")
    parser.add_argument('--TauIDNtuple',help="Grab the trees as if it were a Tau ID Setup",action="store_true")
    
    args = parser.parse_args()
    
    for File in args.Files:
        print("Pruning "+args.Branch+" from "+File)
        PruneBranch(File,args)
