import ROOT
from tqdm import tqdm

OldFile = ROOT.TFile("OldDiagnosticFile.root")
NewFile = ROOT.TFile("NewDiagnosticFile.root")

OldDebugTree = OldFile.DebugTree
NewDebugTree = NewFile.DebugTree

MatchedEvents = 0
UnMatchedEvents = 0
ContentMatchedEvents = 0

print("Running new event scan...")

for i in tqdm(range(NewDebugTree.GetEntries())):
    NewDebugTree.GetEntry(i)    

    #print("New Event Run: "+str(NewEvent.run))
    #print("New Event Lumi: "+str(NewEvent.lumi))
    #print("New Event evt: "+str(NewEvent.evt))
    #this takes too long to search
    #We're fortunate that things are stored in ascending order
    #could implement three back to back binary searches        
    for j in range(OldDebugTree.GetEntries()):
        OldDebugTree.GetEntry(j)
        if(OldDebugTree.run > NewDebugTree.run):
            UnMatchedEvents+=1            
            break
        elif(OldDebugTree.run < NewDebugTree.run):            
            continue
        else:
            if(OldDebugTree.lumi > NewDebugTree.lumi):
                UnMatchedEvents+=1                
                break
            elif(OldDebugTree.lumi < NewDebugTree.lumi):                
                continue
            else:
                if(OldDebugTree.evt > NewDebugTree.evt):
                    UnMatchedEvents+=1                    
                    break
                elif(OldDebugTree.evt < NewDebugTree.evt):
                    continue
                else:
                    MatchedEvents+=1
                    break
    

print("New Events: "+str(NewDebugTree.GetEntries()))
print("New Events with match in old:" +str(MatchedEvents))
print("New Events with no match in old: "+str(UnMatchedEvents))
