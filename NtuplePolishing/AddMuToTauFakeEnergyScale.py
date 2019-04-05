import ROOT
import sys
from array import array
from tqdm import tqdm
import argparse
import ApplyTESBranches

def AddMutotauFakeEnergyScale(FileName,Arguments):
    File = ROOT.TFile=(FileName,"UPDATE")
    TheTree = File.mt_Selected

    MTTF_E_UP = array('f',[0.])
    MTTF_E_DOWN = array('f',[0.])
    MTTF_PT_UP = array('f',[0.])
    MTTF_PT_DOWN = array('f',[0.])
    
    MTTF_E_UP_Branch = TheTree.Branch('MuToTauFake_E_UP',MTTF_E_UP)
    MTTF_E_DOWN_Branch = TheTree.Branch('MuToTauFake_E_DOWN',MTTF_E_DOWN)
    MTTF_PT_UP_Branch = TheTree.Branch('MuToTauFake_PT_UP',MTTF_PT_UP)
    MTTF_PT_DOWN_Branch = TheTree.Branch('MuToTauFake_PT_DOWN',MTTF_PT_DOWN)

    CorrectedTauVector_UP = ROOT.TLorentzVector()
    CorrectedTauVector_DOWN = ROOT.TLorentzVector()

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTre.phi_2,TheTree.m_2)

        CorrectedTauVector_UP = 1.02*TauVector
        CorrectedTauVector_DOWN = 0.98*TauVector

        MTTF_E_UP[0] = CorrectedTauVector_UP.E()
        MTTF_E_DOWN[0] = CorrectedTauVector_DOWN.E()
        MTTF_PT_UP[0] = CorrectedTauVector_UP.Pt()
        MTTFF_PT_DOWN[0] = CorrectedTauVector_DOWN.Pt()
        
        MTTF_E_UP_Branch.Fill()
        MTTF_E_DOWN_Branch.Fill()
        MTTF_PT_UP_Branch.Fill()
        MTTF_PT_DOWN_Branch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    File.Write()
    File.Close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Generate and attach mu-to-tau-fake energy uncertainty branches.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="What year's samples?")
    parser.add_argument('Files',nargs="+","List of the files to run the tool on.")

    args = parser.parse_args()

    for File in args.Files():
        print("Processing the mu-to-tau-fake energy uncertainties for: "+str(File))
        AddMutotauFakeEnergyScale(File,args)
