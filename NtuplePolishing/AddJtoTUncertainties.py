import ROOT 
from array import array
from tqdm import tqdm
import argparse

def GetCorrectedMetVector(TauVector, CorrectedTauVector, MetVector):
    #create tau vector in the transverse plane.
    TransverseTauVector = ROOT.TLorentzVector()
    TransverseTauVector.SetPtEtaPhiM(TauVector.Pt(),0.0,TauVector.Phi(),TauVector.M())
    CorrectedTransverseTauVector = ROOT.TLorentzVector()
    CorrectedTransverseTauVector.SetPtEtaPhiM(CorrectedTauVector.Pt(),0.0,CorrectedTauVector.Phi(),CorrectedTauVector.M())

    CorrectedMetVector = TransverseTauVector-CorrectedTransverseTauVector+MetVector
    return CorrectedMetVector

def AddJtoFUncertainties(FileName,args):
    File = ROOT.TFile(FileName,"UPDATE")
    TheTree = File.mt_Selected
    
    JtoT_E_UP = array('f',[0.])
    JtoT_E_DOWN = array('f',[0.])
    JtoT_Pt_UP = array('f',[0.])
    JtoT_Pt_DOWN = array('f',[0.])
    
    JtoT_MET_UP = array('f',[0.])
    JtoT_METPhi_UP = array('f',[0.])
    JtoT_MET_DOWN = array('f',[0.])
    JtoT_METPhi_DOWN = array('f',[0.])

    JtoT_E_UP_Branch = TheTree.Branch('JtoT_E_UP',JtoT_E_UP,'JtoT_E_UP/F')
    JtoT_E_DOWN_Branch = TheTree.Branch('JtoT_E_DOWN',JtoT_E_DOWN,'JtoT_E_DOWN/F')
    JtoT_Pt_UP_Branch = TheTree.Branch('JtoT_Pt_UP',JtoT_Pt_UP,'JtoT_Pt_UP/F')
    JtoT_Pt_DOWN_Branch = TheTree.Branch('JtoT_Pt_DOWN',JtoT_Pt_DOWN,'JtoT_Pt_DOWN/F')

    JtoT_MET_UP_Branch = TheTree.Branch('JtoT_MET_UP',JtoT_MET_UP,'JtoT_MET_UP/F')
    JtoT_METPhi_UP_Branch = TheTree.Branch('JtoT_METPhi_UP',JtoT_METPhi_UP,'JtoT_METPhi_UP/F')
    JtoT_MET_DOWN_Branch = TheTree.Branch('JtoT_MET_DOWN',JtoT_MET_DOWN,'JtoT_MET_DOWN/F')
    JtoT_METPhi_DOWN_Branch = TheTree.Branch('JtoT_METPhi_DOWN',JtoT_METPhi_DOWN,'JtoT_METPhi_DOWN/F')

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)        

        CorrectedTauVector_UP = ROOT.TLorentzVector()
        CorrectedTauVector_DOWN = ROOT.TLorentzVector()

        CorrectedMetVector_UP = ROOT.TLorentzVector()
        CorrectedMetVector_DOWN = ROOT.TLorentzVector()

        if(TheTree.gen_match_2 != 6):
            CorrectedTauVector_UP = TauVector
            CorrectedTauVector_DOWN = TauVector

            CorrectedMetVector_UP = MetVector
            CorrectedMetVector_DOWN = MetVector
        else:
            CorrectedTauVector_UP = TauVector * 1.2
            CorrectedTauVector_DOWN = TauVector * 0.8

            CorrectedMetVector_UP = GetCorrectedMetVector(TauVector, CorrectedTauVector_UP, MetVector)
            CorrectedMetVector_DOWN = GetCorrectedMetVector(TauVector, CorrectedTauVector_DOWN, MetVector)           
            

        JtoT_E_UP[0] = CorrectedTauVector_UP.E()
        JtoT_E_DOWN[0] = CorrectedTauVector_DOWN.E()
        JtoT_Pt_UP[0] = CorrectedTauVector_UP.Pt()
        JtoT_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
    
        JtoT_MET_UP[0] = CorrectedMetVector_UP.E()
        JtoT_METPhi_UP[0] = CorrectedMetVector_UP.Phi()
        JtoT_MET_DOWN[0] = CorrectedMetVector_DOWN.E()
        JtoT_METPhi_DOWN[0] = CorrectedMetVector_DOWN.Phi()
            
        JtoT_E_UP_Branch.Fill()
        JtoT_E_DOWN_Branch.Fill()
        JtoT_Pt_UP_Branch.Fill()
        JtoT_Pt_DOWN_Branch.Fill()
    
        JtoT_MET_UP_Branch.Fill()
        JtoT_METPhi_UP_Branch.Fill()
        JtoT_MET_DOWN_Branch.Fill()
        JtoT_METPhi_DOWN_Branch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    File.Write()
    File.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate J to T branches for tau IDing.")
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")

    args = parser.parse_args()
    
    for File in args.Files:
        print("Processing J to T for "+str(File))
        AddJtoFUncertainties(File,args)
