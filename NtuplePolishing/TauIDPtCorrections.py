import ROOT
import sys
import argparse
import os
from array import array
from tqdm import tqdm

def GetCorrectedMetVector(TauVector, CorrectedTauVector, MetVector):
    #create tau vector in the transverse plane.
    TransverseTauVector = ROOT.TLorentzVector()
    TransverseTauVector.SetPtEtaPhiM(TauVector.Pt(),0.0,TauVector.Phi(),TauVector.M())
    CorrectedTransverseTauVector = ROOT.TLorentzVector()
    CorrectedTransverseTauVector.SetPtEtaPhiM(CorrectedTauVector.Pt(),0.0,CorrectedTauVector.Phi(),CorrectedTauVector.M())

    CorrectedMetVector = TransverseTauVector-CorrectedTransverseTauVector+MetVector
    return CorrectedMetVector

def TauIDPtCorrections(FileName,args):
    TheFile = ROOT.TFile(FileName)
    OldTree = TheFile.mutau_tree

    NewFile = ROOT.TFile("Temporary.root","RECREATE")
    AlreadyGrabbedItems=[]

    OldTree.GetBranch("pt_2").SetStatus(0)
    OldTree.GetBranch("met").SetStatus(0)
    OldTree.GetBranch("metphi").SetStatus(0)
    
    NewTree = OldTree.CloneTree(0)

    OldTree.GetBranch("pt_2").SetStatus(1)
    OldTree.GetBranch("met").SetStatus(1)
    OldTree.GetBranch("metphi").SetStatus(1)
    
    CorrectedTauEnergy = array('f',[0.])
    CorrectedTauPt = array('f',[0.])    
    
    TESCorrectedMET = array('f',[0.])
    TESCorrectedMETPhi = array('f',[0.])

    NewPtBranch = NewTree.Branch('pt_2',CorrectedTauPt,'pt_2/F')
    NewEnergyBranch = NewTree.Branch('e_2',CorrectedTauEnergy,'e_2/F')
    NewMetBranch = NewTree.Branch('met',TESCorrectedMET,'met/F')
    NewMetPhiBranch = NewTree.Branch('metphi',TESCorrectedMETPhi,'metphi/F')

    for i in tqdm(range(OldTree.GetEntries())):
        OldTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(OldTree.pt_2,OldTree.eta_2,OldTree.phi_2,OldTree.m_2)
        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(OldTree.met,0,OldTree.metphi,0)
        
        NewTauVector = ROOT.TLorentzVector()
        if(OldTree.l2_decayMode == 0):
            NewTauVector = TauVector * 1.007
            CorrectedTauPt[0] = NewTauVector.Pt()
            CorrectedTauEnergy[0] = NewTauVector.E()
            NewMetVector = GetCorrectedMetVector(TauVector, NewTauVector, MetVector)
            TESCorrectedMET[0] = NewMetVector.Pt()
            TESCorrectedMETPhi[0] = NewMetVector.Phi()
            
        elif(OldTree.l2_decayMode == 1):
            NewTauVector = TauVector * 0.998
            CorrectedTauPt[0] = NewTauVector.Pt()
            CorrectedTauEnergy[0] = NewTauVector.E()
            NewMetVector = GetCorrectedMetVector(TauVector, NewTauVector, MetVector)
            TESCorrectedMET[0] = NewMetVector.Pt()
            TESCorrectedMETPhi[0] = NewMetVector.Phi()

        elif(OldTree.l2_decayMode == 10):
            NewTauVector = TauVector * 1.001
            CorrectedTauPt[0] = NewTauVector.Pt()
            CorrectedTauEnergy[0] = NewTauVector.E()
            NewMetVector = GetCorrectedMetVector(TauVector, NewTauVector, MetVector)
            TESCorrectedMET[0] = NewMetVector.Pt()
            TESCorrectedMETPhi[0] = NewMetVector.Phi()
        else:
            CorrectedTauPt[0] = TauVector.Pt()
            CorrectedTauEnergy[0] = TauVector.E()
            TESCorrectedMET[0] = MetVector.Pt()
            TESCorrectedMETPhi[0] = MetVector.Phi()
            
        #if(i%1000 == 0):
        #    print("\nDM: "+str(OldTree.l2_decayMode))
        #    print("Filling: "+str(CorrectedTauPt[0])+" "+str(CorrectedTauEnergy[0])+" "+str(TESCorrectedMET[0])+" "+str(TESCorrectedMETPhi[0]))
        #    print("Original: "+str(OldTree.pt_2)+" "+str(OldTree.met)+" "+str(OldTree.metphi))
            
        NewTree.Fill()
        
    
    NewFile.cd()
    #now we have a new tree, transfer everything that isn't 
    #now let's get this written to a new file.
    for Thing in TheFile.GetListOfKeys():
        if Thing.GetName() not in AlreadyGrabbedItems:
            obj = TheFile.Get(Thing.GetName())
            if type(obj) == type(ROOT.TTree()):
                continue
            obj.Write()
            AlreadyGrabbedItems.append(Thing.GetName())
    NewTree.Write()
    NewFile.Write()
    os.system("mv Temporary.root "+FileName)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="replaces tau and met branches with TES corrected values")
    parser.add_argument('Files',nargs="+",help="List of files to correct")

    args = parser.parse_args()

    for File in args.Files:
        print("TES Correcting "+File)
        TauIDPtCorrections(File,args)
