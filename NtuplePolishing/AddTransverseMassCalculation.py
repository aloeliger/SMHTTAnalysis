import ROOT
import math
from array import array
from tqdm import tqdm
import argparse

def CalculateTransverseMass(FileName,args):
    TheFile = ROOT.TFile(FileName,"UPDATE")
    TheTree = TheFile.mutau_tree
    TransverseMass_Value = array('f',[0.])
    TransverseMass_Branch = TheTree.Branch("TransverseMass",TransverseMass_Value,"TransverseMass/F")
    
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MetVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        MetVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)

        TransverseMass = math.sqrt(2.0*MuVector.Pt()*MetVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector))))
        TransverseMass_Value[0] = TransverseMass
        TransverseMass_Branch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()

if __name__== "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach a transverse mass branch.")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")

    args = parser.parse_args()
    for File in args.Files:
        print("Adding transverse mass branch to "+File)
        CalculateTransverseMass(File,args)
