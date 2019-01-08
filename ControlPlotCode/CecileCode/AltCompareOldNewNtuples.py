import ROOT
from tqdm import tqdm

OldFile = ROOT.TFile("/data/ccaillol/smhmt_svfitted_15nov_svfit/Data.root")
NewFile = ROOT.TFile("/data/ccaillol/smhmt_3jan_svfit/Data.root")

OldTree = OldFile.mutau_tree
NewTree = NewFile.mutau_tree

MatchedEvents = 0
UnMatchedEvents = 0
ContentMatchedEvents = 0

print("Running new event scan...")

for i in tqdm(range(NewTree.GetEntries())):
    NewTree.GetEntry(i)    

    #print("New Event Run: "+str(NewEvent.run))
    #print("New Event Lumi: "+str(NewEvent.lumi))
    #print("New Event evt: "+str(NewEvent.evt))
    #this takes too long to search
    #We're fortunate that things are stored in ascending order
    #could implement three back to back binary searches        
    for j in range(OldTree.GetEntries()):
        OldTree.GetEntry(j)
        if(OldTree.run > NewTree.run):
            UnMatchedEvents+=1            
            break
        elif(OldTree.run < NewTree.run):            
            continue
        else:
            if(OldTree.lumi > NewTree.lumi):
                UnMatchedEvents+=1                
                break
            elif(OldTree.lumi < NewTree.lumi):                
                continue
            else:
                if(OldTree.evt > NewTree.evt):
                    UnMatchedEvents+=1                    
                    break
                elif(OldTree.evt < NewTree.evt):                    
                    continue
                else:
                    MatchedEvents+=1                    
                    break
    if(i%100 == 0 and i != 0):
        print('{:} Processed, New events matched to an old event {:}'.format(i,MatchedEvents))
    

print("New Events: "+str(NewTree.GetEntries()))
print("New Events with match in old:" +str(MatchedEvents))
print("New Events with no match in old: "+str(UnMatchedEvents))
