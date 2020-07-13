import ROOT
import math
from array import array
from tqdm import tqdm
import argparse

def CalculateDifferentialHiggsPt(FileName,args):
    theFile = ROOT.TFile(FileName,"UPDATE")
    theTree = theFile.mt_Selected
    differentialHiggsPt = array('f',[0.])
    differentialHiggsPtBranch = theTree.Branch("differentialHiggsPt",differentialHiggsPt,"differentialHiggsPt/F")

    for i in tqdm(range(theTree.GetEntries())):
        theTree.GetEntry(i)
        muVector = ROOT.TLorentzVector()
        tauVector = ROOT.TLorentzVector()
        metVector = ROOT.TLorentzVector()
        muVector.SetPtEtaPhiM(theTree.pt_1,theTree.eta_1,theTree.phi_1,theTree.m_1)
        tauVector.SetPtEtaPhiM(theTree.pt_2,theTree.eta_2,theTree.phi_2,theTree.m_2)
        metVector.SetPtEtaPhiM(theTree.met,0.0,theTree.metphi,0.0)

        if theTree.Rivet_higgsPt > 0 and theTree.Rivet_higgsPt < 45:
            differentialHiggsPt[0] = theTree.HiggsPt
        elif theTree.Rivet_higgsPt >= 45:
            differentialHiggsPt[0] = theTree.HiggsPt * 1.05
        differentialHiggsPtBranch.Fill()
    theTree.Write('',ROOT.TObject.kOverwrite)
    theFile.Write()
    theFile.Close()
if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Generate and attach a slightly corrected higgs pt branch")
    parser.add_argument('Files',nargs='+',help='List of files to run the tool on')

    args = parser.parse_args()
    for File in args.Files:
        print ("Processing: "+File)
        CalculateDifferentialHiggsPt(File,args)
