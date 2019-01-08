import ROOT
from tqdm import tqdm

OldFile = ROOT.TFile("/data/ccaillol/smhmt_svfitted_15nov_svfit/Data.root")
NewFile = ROOT.TFile("/data/ccaillol/smhmt_3jan_svfit/Data.root")

OldTree = OldFile.mutau_tree
NewTree = NewFile.mutau_tree

print("Checking for event matches...")

OldTreeLowerBound = 0

MatchedEvents = 0
UnMatchedEvents = 0

HasMatch = False

for i in tqdm(range(NewTree.GetEntries())):
    NewTree.GetEntry(i)    
    
    LeftBound = 0
    RightBound = OldTree.GetEntries()-1

    while(LeftBound <= RightBound):

        SearchPoint = (LeftBound+RightBound)/2
        OldTree.GetEntry(SearchPoint)
        
        if(OldTree.run > NewTree.run):
            RightBound = SearchPoint - 1
        elif(OldTree.run < NewTree.run):
            LeftBound = SearchPoint + 1
        else:
            if(OldTree.lumi > NewTree.lumi):
                RightBound = SearchPoint - 1
            elif(OldTree.lumi < NewTree.lumi):
                LeftBound = SearchPoint + 1
            else:
                if(OldTree.evt > NewTree.evt):
                    RightBound = SearchPoint - 1
                elif(OldTree.evt < NewTree.evt):
                    LeftBound = SearchPoint+1
                #Found a match!
                else:
                    HasMatch = True
                    LeftBound = SearchPoint
                    MatchedEvents+=1                    

    if(not HasMatch):
        UnMatchedEvents+=1
    #Update us on how we're doing
    if(i%1000 == 0 and i != 0):
        print()
        print('{:} Processed, New events matched to an old event {:}'.format(i,MatchedEvents))

print("Total New Events: "+str(NewTree.GetEntries()))
print("Matched New Events: "+str(MatchedEvents))
print("Unmatched New Events: "+str(UnMatchedEvents))
