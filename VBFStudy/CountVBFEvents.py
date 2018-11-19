import ROOT 
import sys
from tqdm import tqdm
from array import array

def CountVBFEvents(FileToRun, njetsCut, mjjCut):
    VBFFile = ROOT.TFile.Open(FileToRun)
    TheTree = VBFFile.mt_tree
    
    NoVetoPass = 0.0
    VetoPass = 0.0
    NumSignificantMismatches = 0.0
    NumVetoPassNotNoVeto = 0.0

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        if(TheTree.gen_match_2 == 5):
            if(TheTree.mjj > mjjCut and TheTree.njets > njetsCut):
                NoVetoPass += 1.0
            if(TheTree.mjjWoNoisyJets > mjjCut and TheTree.njetsWoNoisyJets > njetsCut):
                VetoPass += 1.0
            if(TheTree.mjjWoNoisyJets > 50.0 and not TheTree.mjj > 50.0 ):
                #Print("mjj w/o noisy jets is higher than mjj")
                #Print("i: "+str(i))
                #print("mjj: "+str(TheTree.mjj))
                #print("mjj wo noisyjets: "+str(TheTree.mjjWoNoisyJets))            
                NumVetoPassNotNoVeto += 1.0
            if(not (TheTree.mjj == 0 or TheTree.mjjWoNoisyJets == 0) and (TheTree.mjj / TheTree.mjjWoNoisyJets > 1.1 or TheTree.mjj / TheTree.mjjWoNoisyJets < 0.9)):
                #print("Significant Mismatch!")
                #print("mjj: "+str(TheTree.mjj))
                #print("mjj wo noisyjets: "+str(TheTree.mjjWoNoisyJets))
                NumSignificantMismatches += 1.0
                
    #print("Number Of Events where veto'd mass passes the cut but the non veto'd does not: "+str(NumVetoPassNotNoVeto))
    #print("Number of Events with significant mismatch between mjj and mjjWoNoisyJets: "+str(NumSignificantMismatches))

    #print("Signal Events Passing Cuts without Vetos: "+str(NoVetoPass))
    #print("Signal Events Passing Cuts with Vetos: "+str(VetoPass))
    return (VetoPass/NoVetoPass)

if __name__ == "__main__":
    for File in sys.argv[1:]:
        print("Counting VBF Events...")
        CountVBFEvents(File,-1.0,50)
