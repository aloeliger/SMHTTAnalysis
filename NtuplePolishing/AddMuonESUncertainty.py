import ROOT
import sys
from array import array
from tqdm import tqdm
import argparse

def GetCorrectedMetVector(MuVector, CorrectedMuVector, MetVector):
    #Create mu vector in the transverse plane.
    TransverseMuVector = ROOT.TLorentzVector()
    TransverseMuVector.SetPtEtaPhiM(MuVector.Pt(),0.0,MuVector.Phi(),MuVector.M())
    CorrectedTransverseMuVector = ROOT.TLorentzVector()
    CorrectedTransverseMuVector.SetPtEtaPhiM(CorrectedMuVector.Pt(),0.0,CorrectedMuVector.Phi(),CorrectedMuVector.M())

    CorrectedMetVector = TransverseMuVector-CorrectedMuVector+MetVector
    return CorrectedMetVector

def AddMuonESUncertainty(FileName,args):
    File = ROOT.TFile(FileName,"UPDATE")
    TheTree = File.mt_Selected

    muonES_E_UP = array('f',[0.])
    muonES_E_DOWN = array('f',[0.])
    muonES_Pt_UP = array('f',[0.])
    muonES_Pt_DOWN = array('f',[0.])

    muonES_MET_UP = array('f',[0.])
    muonES_MET_DOWN = array('f',[0.])
    muonES_METPhi_UP = array('f',[0.])
    muonES_METPhi_DOWN = array('f',[0.])

    muonES_E_UP_Branch = TheTree.Branch('muonES_E_UP',muonES_E_UP,'muonES_E_UP/F')
    muonES_E_DOWN_Branch = TheTree.Branch('muonES_E_DOWN',muonES_E_DOWN,'muonES_E_DOWN/F')
    muonES_Pt_UP_Branch = TheTree.Branch('muonES_Pt_UP',muonES_Pt_UP,'muonES_Pt_UP/F')
    muonES_Pt_DOWN_Branch = TheTree.Branch('muonES_Pt_DOWN',muonES_Pt_DOWN,'muonES_Pt_DOWN/F')

    muonES_MET_UP_Branch = TheTree.Branch('muonES_MET_UP',muonES_MET_UP,'muonES_MET_UP/F')
    muonES_MET_DOWN_Branch = TheTree.Branch('muonES_MET_DOWN',muonES_MET_DOWN,'muonES_MET_DOWN/F')
    muonES_METPhi_UP_Branch = TheTree.Branch('muonES_METPhi_UP',muonES_METPhi_UP,'muonES_METPhi_UP/F')
    muonES_METPhi_DOWN_Branch = TheTree.Branch('muonES_METPhi_DOWN',muonES_METPhi_DOWN,'muonES_METPhi_DOWN/F')

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        MuonVector = ROOT.TLorentzVector()
        MuonVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        CorrectedMuonVector_UP = ROOT.TLorentzVector()
        CorrectedMuonvector_DOWN = ROOT.TLorentzVector()

        if(TheTree.eta_1 >= -2.4 and TheTree.eta_1 < -2.1):
            CorrectedMuonVector_UP = MuonVector * (1.0+0.027)
            CorrectedMuonVector_DOWN = MuonVector * (1.0-0.027)
        elif(TheTree.eta_1 >= -2.1 and TheTree.eta_1 < -1.2):
            CorrectedMuonVector_UP = MuonVector * (1.0+0.009)
            CorrectedMuonVector_DOWN = MuonVector * (1.0-0.009)
        elif(TheTree.eta_1 >= -1.2 and TheTree.eta_1 < 1.2):
            CorrectedMuonVector_UP = MuonVector * (1.0+0.004)
            CorrectedMuonVector_DOWN = MuonVector * (1.0-0.004)
        elif(TheTree.eta_1 >= 1.2 and TheTree.eta_1 < 2.1):
            CorrectedMuonVector_UP = MuonVector * (1.0+0.009)
            CorrectedMuonVector_DOWN = MuonVector * (1.0-0.009)
        elif(TheTree.eta_1 >= 2.1 and TheTree.eta_1 <2.4):
            CorrectedMuonVector_UP = MuonVector*(1.0+0.017)
            CorrectedMuonVector_DOWN = MuonVector*(1.0-0.017)
        else:
            raise RuntimeError("Muon outside of eta bounds: "+str(TheTree.eta_1))

        CorrectedMetVector_UP = GetCorrectedMetVector(MuonVector,CorrectedMuonVector_UP,MetVector)
        CorrectedMetVector_DOWN = GetCorrectedMetVector(MuonVector,CorrectedMuonVector_DOWN,MetVector)
        
        muonES_E_UP[0] = CorrectedMuonVector_UP.E()
        muonES_E_DOWN[0] = CorrectedMuonVector_DOWN.E()
        muonES_Pt_UP[0] = CorrectedMuonVector_UP.Pt()
        muonES_Pt_DOWN[0] = CorrectedMuonVector_DOWN.Pt()

        muonES_MET_UP[0] = CorrectedMetVector_UP.Pt()
        muonES_MET_DOWN[0] = CorrectedMetVector_DOWN.Pt()
        muonES_METPhi_UP[0] = CorrectedMetVector_UP.Phi()
        muonES_METPhi_DOWN[0] = CorrectedMetVector_DOWN.Phi()
        
        muonES_E_UP_Branch.Fill()
        muonES_E_DOWN_Branch.Fill()
        muonES_Pt_UP_Branch.Fill()
        muonES_Pt_DOWN_Branch.Fill()

        muonES_MET_UP_Branch.Fill()
        muonES_MET_DOWN_Branch.Fill()
        muonES_METPhi_UP_Branch.Fill()
        muonES_METPhi_DOWN_Branch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    File.Write()
    File.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach muonES (genuine identified muon) uncertainty branches")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's corerctions are to be used")
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")

    args = parser.parse_args()
    
    for File in args.Files:
        print("Processing muonES for "+str(File))
        AddMuonESUncertainty(File,args)
