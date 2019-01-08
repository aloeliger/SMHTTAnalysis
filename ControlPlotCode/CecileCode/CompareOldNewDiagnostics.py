import ROOT
from tqdm import tqdm

OldFile = ROOT.TFile("OldDiagnosticFile.root")
NewFile = ROOT.TFile("NewDiagnosticFile.root")

OldDebugTree = OldFile.DebugTree
NewDebugTree = NewFile.DebugTree

MatchedEvents = 0
UnMatchedEvents = 0
ContentMatchedEvents = 0
TotalNewEvents = 0
HasMatch = False

print("Running new event scan...")

for i in tqdm(range(NewDebugTree.GetEntries())):
    NewDebugTree.GetEntry(i)
    TotalNewEvents+=1        
    HasMatch=False
    #print("New Event Run: "+str(NewEvent.run))
    #print("New Event Lumi: "+str(NewEvent.lumi))
    #print("New Event evt: "+str(NewEvent.evt))
    #this takes too long to search
    #We're fortunate that things are stored in ascending order
    #could implement three back to back binary searches    
    LeftBound = 0
    RightBound = OldDebugTree.GetEntries()-1
    while(LeftBound <= RightBound):
        
        SearchPoint = (LeftBound+RightBound)/2
        OldDebugTree.GetEntry(SearchPoint)
        
        if(OldDebugTree.run > NewDebugTree.run):
            RightBound = SearchPoint - 1
        elif(OldDebugTree.run < NewDebugTree.run):
            LeftBound = SearchPoint + 1
        else:
            if(OldDebugTree.lumi > NewDebugTree.lumi):
                RightBound = SearchPoint - 1
            elif(OldDebugTree.lumi < NewDebugTree.lumi):
                LeftBound = SearchPoint + 1
            else:
                if(OldDebugTree.evt > NewDebugTree.evt):
                    RightBound = SearchPoint - 1
                elif(OldDebugTree.evt < NewDebugTree.evt):
                    LeftBound = SearchPoint+1
                #Found a match!
                else:
                    MatchedEvents+=1
                    HasMatch=True
                    if(NewDebugTree.byTightIsolationMVArun2v2DBoldDMwLT_2 != OldDebugTree.byTightIsolationMVArun2v2DBoldDMwLT_2):
                        print("Mismatch:")
                        print("run: "+str(NewDebugTree.run))
                        print("lumi: "+str(NewDebugTree.lumi))
                        print("evt: "+str(NewDebugTree.evt))
                        print("New Tight Isolation: "+str(NewDebugTree.byTightIsolationMVArun2v2DBoldDMwLT_2))
                        print("Old Tight Isolation: "+str(OldDebugTree.byTightIsolationMVArun2v2DBoldDMwLT_2))
                        print()
                    else:
                        ContentMatchedEvents+=1
                    break

    if(not HasMatch):
        UnMatchedEvents+=1

print("New Events: "+str(TotalNewEvents))
print("New Events with match in old:" +str(MatchedEvents))
print("New Events with no match in old: "+str(UnMatchedEvents))
print("Content Matched Events: "+str(ContentMatchedEvents))
