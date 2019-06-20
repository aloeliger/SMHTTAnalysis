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
    
    TES_E = array('f',[0.])    
    TES_E_UP = array('f',[0.])
    TES_E_DOWN = array('f',[0.])
    TES_Pt = array('f',[0.])    
    TES_Pt_UP = array('f',[0.])
    TES_Pt_DOWN = array('f',[0.])
    
    TES_MET = array('f',[0.])
    TES_METPhi = array('f',[0.])
    
    TES_MET_UP = array('f',[0.])
    TES_METPhi_UP = array('f',[0.])
    TES_MET_DOWN = array('f',[0.])
    TES_METPhi_DOWN = array('f',[0.])

    if(not Arguments.NoEnergyCorrect):
        TES_E_Branch = TheTree.Branch('TES_E',TES_E,"TES_E/F")
        TES_Pt_Branch = TheTree.Branch('TES_Pt',TES_Pt,"TES_Pt/F")
        TES_MET_Branch = TheTree.Branch('TES_MET',TES_MET,"TES_MET/F")
        TES_METPhi_Branch = TheTree.Branch('TES_METPhi',TES_METPhi,"TES_METPhi/F")
    TES_E_UP_Branch = TheTree.Branch('TES_E_UP',TES_E_UP,"TES_E_UP/F")
    TES_E_DOWN_Branch = TheTree.Branch('TES_E_DOWN',TES_E_DOWN,"TES_E_DOWN/F")    
    TES_Pt_UP_Branch = TheTree.Branch('TES_Pt_UP',TES_Pt_UP,"TES_Pt_UP/F")
    TES_Pt_DOWN_Branch = TheTree.Branch('TES_Pt_DOWN',TES_Pt_DOWN,"TES_Pt_DOWN/F")
    TES_MET_UP_Branch = TheTree.Branch('TES_MET_UP',TES_MET_UP,"TES_MET_UP/F")
    TES_METPhi_UP_Branch = TheTree.Branch('TES_METPhi_UP',TES_METPhi_UP,'TES_METPhi_UP/F')
    TES_MET_DOWN_Branch = TheTree.Branch('TES_MET_DOWN',TES_MET_DOWN,'TES_MET_DOWN/F')
    TES_METPhi_DOWN_Branch = TheTree.Branch('TES_METPhi_DOWN',TES_METPhi_DOWN,'TES_METPhi_DOWN/F')

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
        if(Arguments.year == "2016"):
            if(TheTree.gen_match_2 != 5):
                CorrectedTauVector = TauVector
                CorrectedTauVector_UP = TauVector
                CorrectedTauVector_DOWN = TauVector
                
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 0):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0 
                else:
                    EnergyCorrectFactor = -0.006
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.010))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.010))
                                
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 1):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.005
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.009))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.009))

            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 10):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.0
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.011))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.011))
                
            TES_E[0] = CorrectedTauVector.E()
            TES_E_UP[0] = CorrectedTauVector_UP.E()
            TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
            TES_Pt[0] = CorrectedTauVector.Pt()
            TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
            TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()
                
                
        #2017 TES corrections
        elif(Arguments.year=="2017"):
            if(TheTree.gen_match_2 != 5):
                CorrectedTauVector = TauVector
                CorrectedTauVector_UP = TauVector
                CorrectedTauVector_DOWN = TauVector
            
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 0):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.007
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.008))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.008))
                                
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 1):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.002
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.008))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.008))
                                
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 10):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.001
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.009))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.009))
                
            TES_E[0] = CorrectedTauVector.E()
            TES_E_UP[0] = CorrectedTauVector_UP.E()
            TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
            TES_Pt[0] = CorrectedTauVector.Pt()
            TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
            TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()    
            
        #2018 TES corrections        
        elif(Arguments.year == "2018"):
            if(TheTree.gen_match_2 != 5):
                CorrectedTauVector = TauVector
                CorrectedTauVector_UP = TauVector
                CorrectedTauVector_DOWN = TauVector
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 0):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.013
                CorrectedTauVector = TauVector * (1.00+(EnergyCorrectFactor))
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor + 0.011))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor - 0.011))
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 1):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.005
                CorrectedTauVector = TauVector * (1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector * (1.00+(EnergyCorrectFactor+0.009))
                CorrectedTauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor-0.009))
            elif(TheTree.gen_match_2 == 5 and TheTree.l2_decayMode == 10):
                if Arguments.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = -0.012                
                CorrectedTauVector = TauVector*(1.00+EnergyCorrectFactor)
                CorrectedTauVector_UP = TauVector*(1.00+(EnergyCorrectFactor + 0.008))
                CorrectedTauVector_DOWN = TauVector*(1.00+(EnergyCorrectFactor - 0.008))
            
            TES_E[0] = CorrectedTauVector.E()
            TES_E_UP[0] = CorrectedTauVector_UP.E()
            TES_E_DOWN[0] = CorrectedTauVector_DOWN.E()
            TES_Pt[0] = CorrectedTauVector.Pt()
            TES_Pt_UP[0] = CorrectedTauVector_UP.Pt()
            TES_Pt_DOWN[0] = CorrectedTauVector_DOWN.Pt()    

        CorrectedMetVector = GetCorrectedMetVector(TauVector,CorrectedTauVector,MetVector)
        CorrectedMetVector_UP  = GetCorrectedMetVector(TauVector,CorrectedTauVector_UP,MetVector)
        CorrectedMetVector_DOWN = GetCorrectedMetVector(TauVector,CorrectedTauVector_DOWN,MetVector)
        TES_MET[0] = CorrectedMetVector.Pt()
        TES_METPhi[0] = CorrectedMetVector.Phi()
        TES_MET_UP[0] = CorrectedMetVector_UP.Pt()
        TES_METPhi_UP[0] = CorrectedMetVector_UP.Phi()
        TES_MET_DOWN[0] = CorrectedMetVector_DOWN.Pt()
        TES_METPhi_DOWN[0] = CorrectedMetVector_DOWN.Phi()
        if(not Arguments.NoEnergyCorrect):
            TES_E_Branch.Fill()
            TES_Pt_Branch.Fill()
            TES_MET_Branch.Fill()
            TES_METPhi_Branch.Fill()
        TES_E_UP_Branch.Fill()
        TES_E_DOWN_Branch.Fill()
        TES_Pt_UP_Branch.Fill()
        TES_Pt_DOWN_Branch.Fill()
        TES_MET_UP_Branch.Fill()
        TES_METPhi_UP_Branch.Fill()
        TES_MET_DOWN_Branch.Fill()
        TES_METPhi_DOWN_Branch.Fill()

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
