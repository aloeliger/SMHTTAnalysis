import ROOT
import sys
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

def ApplyTESBranches(FileName,Arguments):
    File = ROOT.TFile(FileName,"UPDATE")
    TheTree = File.mt_Selected
    
    CorrectedTauEnergy = array('f',[0.])    
    TES_E_UP = array('f',[0.])
    TES_E_DOWN = array('f',[0.])
    CorrectedTauPt = array('f',[0.])    
    TES_Pt_UP = array('f',[0.])
    TES_Pt_DOWN = array('f',[0.])
    
    TESCorrectedMET = array('f',[0.])
    TESCorrectedMETPhi = array('f',[0.])

    if(not Arguments.NoEnergyCorrections):
        CorrectedTauEnergy_Branch = TheTree.Branch('CorrectedTauEnergy',CorrectedTauEnergy)
        CorrectedTauPt_Branch = TheTree.Branch('CorrectedTauPt',CorrectedTauPt)
        TESCorrectedMET_Branch = TheTree.Branch('TESCorrectedMET',TESCorrectedMET)
        TESCorrectedMETPhi_Branch = TheTree.Branch('TESCorrectedMETPhi',TESCorrectedMETPhi)
    TES_E_UP_Branch = TheTree.Branch('TES_E_UP',TES_E_UP)
    TES_E_DOWN_Branch = TheTree.Branch('TES_E_DOWN',TES_E_DOWN)    
    TES_Pt_UP_Branch = TheTree.Branch('TES_Pt_UP',TES_Pt_UP)
    TES_Pt_DOWN_Branch = TheTree.Branch('TES_Pt_DOWN',TES_Pt_DOWN)

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)        
        CorrectedTauVector = ROOT.TLorentzVector()
        CorrectedTauVector_UP = ROOT.TLorentzVector()
        CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                        
        #2016 TES Corrections
        elif(Arguments.Year == "2016"):
            if(TheTree.l2_decaymode == 0):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0 
                else:
                    EnergyCorrectFactor - 0.005
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.012))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.012))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_Down[0] = CorrectedTauVector_DOWN.Pt()
                
            elif(TheTree.l2_decaymode == 1):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.011
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.012))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.012))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
            elif(TheTree.l2_decaymode == 10):
                if Argument.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.006
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.012))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.012))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_DOWN[0] = CorrectedTauVector_E_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
                
        #2017 TES corrections
        elif(Arguments.Year=="2017"):
            if(TheTree.l2_decaymode == 0):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.007
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.008))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.008))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
            elif(TheTree.l2_decaymode == 1):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.002
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.008))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.008))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_DOWN[0] = CorrectedTauVector_E_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
            elif(TheTree.l2_decaymode == 10):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.001
                CorrectedTauVector = (1.00+EnergyCorrectFactor)*TauVector
                CorrectedTauVector_UP = (1.00+(EnergyCorrectFactor+0.009))*TauVector
                CorrectedTauVector_DOWN = (1.00+(EnergyCorrectFactor-0.009))*TauVector
                
                CorrectedTauEnergy[0] = CorrectedTauVector.E()
                TES_E_UP[0] = CorrectedTauVector_UP.E()
                TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
                CorrectedTauPt[0] = CorrectedTauVector.Pt()
                TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
                TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
            
        #2018 TES corrections
        #NOT YET CALCULATED!
        elif(Arguments.Year == "2018"):
            if(TheTree.l2_decaymode == 0):
                CorrectedTauEnergy[0] = TauVector.E()
                TES_E_UP[0] = TauVector.E()
                TES_E_DOWN[0] = TauVector.E()
                CorrectedTauPt[0] = TauVector.Pt()
                TES_Pt_UP[0] = TauVector.Pt()
                TES_Pt_DOWN[0] = TauVector.Pt()
            elif(TheTree.l2_decaymode == 1):
                CorrectedTauEnergy[0] = TauVector.E()
                TES_UP[0] = TauVector.E()
                TES_DOWN[0] = TauVector.E()
                CorrectedTauPt[0] = TauVector.Pt()
                TES_Pt_UP[0] = TauVector.Pt()
                TES_Pt_DOWN[0] = TauVector.Pt()
            elif(TheTree.l2_decaymode == 10):
                CorrectedTauEnergy[0] = TauVector.E()
                TES_UP[0] = TauVector.E()
                TES_DOWN[0] = TauVector.E()
                CorrectedTauPt[0] = TauVector.Pt()
                TES_Pt_UP[0] = TauVector.Pt()
                TES_Pt_DOWN[0] = TauVector.Pt()
        CorrectedMetVector = GetCorrectedMetVector(TauVector,CorrectedTauVector,MetVector)
        TESCorrectedMET[0] = CorrectedMetVector.Pt()
        TESCorrectedMETPhi[0] = CorrectedMetVector.Phi()
        if(not Arguments.NoEnergyCorrections):
            CorrectedTauEnergy_Branch.Fill()
            CorrectedTauPt_Branch.Fill()
            TESCorrectedMET_Branch.Fill()
            TESCorrectedMETPhi_Branch.Fill()
        TES_E_UP_Branch.Fill()
        TES_E_DOWN_Branch.Fill()
        TES_Pt_UP_Branch.Fill()
        TES_Pt_DOWN_Branch.Fill()

    TheTree.Write('',ROOT.TObject.kOverwrite)
    File.Write()
    File.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach TES branches.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's corrections are to be used")
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")    
    parser.add_argument('--NoEnergyCorrect',help="Only store uncertainties, do not save a corrected Tau Energy Branch",action="store_true")
        
    args = parser.parse_args()
    
    for File in args.Files:
        print("Processing TES for "+str(File))
        ApplyTESBranches(File,args)
