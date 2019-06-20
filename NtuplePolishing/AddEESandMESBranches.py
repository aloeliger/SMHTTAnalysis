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

def ApplyEESandMES(File,args):
    TheFile = ROOT.TFile(File,"UPDATE")
    TheTree = TheFile.mt_Selected

    EES_E = array('f',[0.])
    EES_E_UP = array('f',[0.])
    EES_E_DOWN = array('f',[0.])
    EES_Pt = array('f',[0.])
    EES_Pt_UP = array('f',[0.])
    EES_Pt_DOWN = array('f',[0.])

    MES_E = array('f',[0.])
    MES_E_UP = array('f',[0.])
    MES_E_DOWN = array('f',[0.])
    MES_Pt = array('f',[0.])
    MES_Pt_UP = array('f',[0.])
    MES_Pt_DOWN = array('f',[0.])

    EES_MET = array('f',[0.])
    EES_METPhi = array('f',[0.])
    EES_MET_UP = array('f',[0.])
    EES_METPhi_UP = array('f',[0.])
    EES_MET_DOWN = array('f',[0.])
    EES_METPhi_DOWN = array('f',[0.])

    MES_MET = array('f',[0.])
    MES_METPhi = array('f',[0.])
    MES_MET_UP = array('f',[0.])
    MES_METPhi_UP = array('f',[0.])
    MES_MET_DOWN = array('f',[0.])
    MES_METPhi_DOWN = array('f',[0.])

    if(not args.NoEnergyCorrect):
        EES_E_Branch = TheTree.Branch("EES_E",EES_E,"EES_E/F")
        EES_Pt_Branch = TheTree.Branch("EES_Pt",EES_Pt,"EES_Pt/F")
        MES_E_Branch = TheTree.Branch("MES_E",MES_E,"MES_E/F")
        MES_Pt_Branch = TheTree.Branch("MES_Pt",MES_Pt,"MES_Pt/F")

        EES_MET_Branch = TheTree.Branch("EES_MET",EES_MET,"EES_MET/F")
        EES_METPhi_Branch = TheTree.Branch("EES_METPhi",EES_METPhi,"EES_METPhi/F")
        MES_MET_Branch = TheTree.Branch("MES_MET",MES_MET,"MES_MET/F")
        MES_METPhi_Branch = TheTree.Branch("MES_METPhi",MES_METPhi,"MES_METPhi/F")
        
    EES_E_UP_Branch = TheTree.Branch("EES_E_UP",EES_E_UP,"EES_E_UP/F")
    EES_E_DOWN_Branch = TheTree.Branch("EES_E_DOWN",EES_E_DOWN,"EES_E_DOWN/F")
    EES_Pt_UP_Branch = TheTree.Branch("EES_Pt_UP",EES_Pt_UP,"EES_Pt_UP/F")
    EES_Pt_DOWN_Branch = TheTree.Branch("EES_Pt_DOWN",EES_Pt_DOWN,"EES_Pt_DOWN/F")

    MES_E_UP_Branch = TheTree.Branch("MES_E_UP",MES_E_UP,"MES_E_UP/F")
    MES_E_DOWN_Branch = TheTree.Branch("MES_E_DOWN",MES_E_DOWN,"MES_E_DOWN/F")
    MES_Pt_UP_Branch = TheTree.Branch("MES_Pt_UP",MES_Pt_UP,"MES_Pt_UP/F")
    MES_Pt_DOWN_Branch = TheTree.Branch("MES_Pt_DOWN",MES_Pt_DOWN,"MES_Pt_DOWN/F")
    
    EES_MET_UP_Branch = TheTree.Branch("EES_MET_UP",EES_MET_UP,"EES_MET_UP/F")
    EES_METPhi_UP_Branch = TheTree.Branch("EES_METPhi_UP",EES_METPhi_UP,"EES_METPhi_UP/F")
    EES_MET_DOWN_Branch = TheTree.Branch("EES_MET_DOWN",EES_MET_DOWN,"EES_MET_DOWN/F")
    EES_METPhi_DOWN_Branch = TheTree.Branch("EES_METPhi_DOWN",EES_METPhi_DOWN,"EES_METPhi_DOWN/F")
    
    MES_MET_UP_Branch = TheTree.Branch("MES_MET_UP",MES_MET_UP,"MES_MET_UP/F")
    MES_METPhi_UP_Branch = TheTree.Branch("MES_METPhi_UP",MES_METPhi_UP,"MES_METPhi_UP/F")
    MES_MET_DOWN_Branch = TheTree.Branch("MES_MET_DOWN",MES_MET_DOWN,"MES_MET_DOWN/F")
    MES_METPhi_DOWN_Branch = TheTree.Branch("MES_METPhi_DOWN",MES_METPhi_DOWN,"MES_METPhi_DOWN/F")

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        METVector = ROOT.TLorentzVector()
        METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        
        MES_TauVector = ROOT.TLorentzVector()
        MES_TauVector_UP = ROOT.TLorentzVector()
        MES_TauVector_DOWN = ROOT.TLorentzVector()
        
        EES_TauVector = ROOT.TLorentzVector()
        EES_TauVector_UP = ROOT.TLorentzVector()
        EES_TauVector_DOWN = ROOT.TLorentzVector()

        MES_METVector = ROOT.TLorentzVector()
        MES_METVector_UP = ROOT.TLorentzVector()
        MES_METVector_DOWN = ROOT.TLorentzVector()

        EES_METVector = ROOT.TLorentzVector()
        EES_METVector_UP = ROOT.TLorentzVector()
        EES_METVector_DOWN = ROOT.TLorentzVector()

        #2016/2018 MES/EES
        if(args.year == "2018"):
            raise RuntimeError("2018 not implemented yet! Implement me!")
        if(args.year =="2016" or args.year == "2018"):
            #EES
            if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3 ):
                if(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.0
                elif(TheTree.l2_decayMode == 1):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.095
                else:
                    EnergyCorrectFactor = 0.0
                #Do not correct anything to do with the MES
                MES_TauVector = TauVector
                MES_TauVector_UP = TauVector
                MES_TauVector_DOWN = TauVector
                MES_METVector = METVector
                MES_METVector_UP = METVector
                MES_METVector_DOWN = METVector

                #Do correct the EES tau vectors
                EES_TauVector = TauVector * (1.00 + EnergyCorrectFactor)
                EES_TauVector_UP = TauVector * (1.00 +(EnergyCorrectFactor + 0.03))
                EES_TauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor - 0.03))
                EES_METVector = GetCorrectedMetVector(TauVector, EES_TauVector, METVector)
                EES_METVector_UP = GetCorrectedMetVector(TauVector, EES_TauVector_UP, METVector)
                EES_METVector_DOWN = GetCorrectedMetVector(TauVector, EES_TauVector_DOWN, METVector)
                
            #MES
            elif(TheTree.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                if(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.015                        
                elif(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = -0.002
                else:
                    EnergyCorrectFactor = 0.0
                
                #Do not correct anything to do with the EES
                EES_TauVector = TauVector
                EES_TauVector_UP = TauVector
                EES_TauVector_DOWN = TauVector
                EES_METVector = METVector
                EES_METVector_UP = METVector
                EES_METVector_DOWN = METVector

                #Do correct the MES
                MES_TauVector = TauVector * (1.00 + EnergyCorrectFactor)
                MES_TauVector_UP = TauVector * (1.00 + (EnergyCorrectFactor + 0.03))
                MES_TauVector_DOWN = TauVector * (1.00 + (EnergyCorrectFactor - 0.03))
                MES_METVector = GetCorrectedMetVector(TauVector, MES_TauVector, METVector)
                MES_METVector_UP = GetCorrectedMetVector(TauVector, MES_TauVector_UP, METVector)
                MES_METVector_DOWN = GetCorrectedMetVector(TauVector, MES_TauVector_DOWN, METVector)

            #nothing doing. Do trivial things
            else:
                EES_TauVector=TauVector
                EES_TauVector_UP=TauVector
                EES_TauVector_DOWN=TauVector
                EES_METVector=METVector
                EES_METVector_UP=METVector
                EES_METVector_DOWN=METVector

                MES_TauVector = TauVector
                MES_TauVector_UP = TauVector
                MES_TauVector_DOWN = TauVector
                MES_METVector = METVector
                MES_METVector_UP = METVector
                MES_METVector_DOWN = METVector
        #2017 MES/EES
        if(args.year == "2017"):
            #EES
            if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3 ):
                if(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.003
                elif(TheTree.l2_decayMode == 1):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.036
                else:
                    EnergyCorrectFactor = 0.0
                #Do not correct anything to do with the MES
                MES_TauVector = TauVector
                MES_TauVector_UP = TauVector
                MES_TauVector_DOWN = TauVector
                MES_METVector = METVector
                MES_METVector_UP = METVector
                MES_METVector_DOWN = METVector

                #Do correct the EES tau vectors
                EES_TauVector = TauVector * (1.00 + EnergyCorrectFactor)
                EES_TauVector_UP = TauVector * (1.00 +(EnergyCorrectFactor + 0.03))
                EES_TauVector_DOWN = TauVector * (1.00+(EnergyCorrectFactor - 0.03))
                EES_METVector = GetCorrectedMetVector(TauVector, EES_TauVector, METVector)
                EES_METVector_UP = GetCorrectedMetVector(TauVector, EES_TauVector_UP, METVector)
                EES_METVector_DOWN = GetCorrectedMetVector(TauVector, EES_TauVector_DOWN, METVector)
                
            #MES
            elif(TheTree.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                if(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.0                        
                elif(TheTree.l2_decayMode == 0):
                    if args.NoEnergyCorrect:
                        EnergyCorrectFactor = 0.0
                    else:
                        EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.0
                
                #Do not correct anything to do with the EES
                EES_TauVector = TauVector
                EES_TauVector_UP = TauVector
                EES_TauVector_DOWN = TauVector
                EES_METVector = METVector
                EES_METVector_UP = METVector
                EES_METVector_DOWN = METVector

                #Do correct the MES
                MES_TauVector = TauVector * (1.00 + EnergyCorrectFactor)
                MES_TauVector_UP = TauVector * (1.00 + (EnergyCorrectFactor + 0.03))
                MES_TauVector_DOWN = TauVector * (1.00 + (EnergyCorrectFactor - 0.03))
                MES_METVector = GetCorrectedMetVector(TauVector, MES_TauVector, METVector)
                MES_METVector_UP = GetCorrectedMetVector(TauVector, MES_TauVector_UP, METVector)
                MES_METVector_DOWN = GetCorrectedMetVector(TauVector, MES_TauVector_DOWN, METVector)

            #nothing doing. Do trivial things
            else:
                EES_TauVector=TauVector
                EES_TauVector_UP=TauVector
                EES_TauVector_DOWN=TauVector
                EES_METVector=METVector
                EES_METVector_UP=METVector
                EES_METVector_DOWN=METVector

                MES_TauVector = TauVector
                MES_TauVector_UP = TauVector
                MES_TauVector_DOWN = TauVector
                MES_METVector = METVector
                MES_METVector_UP = METVector
                MES_METVector_DOWN = METVector
            #Set Values, Fill, and let's roll
        EES_E[0] = EES_TauVector.E()
        EES_E_UP[0] = EES_TauVector_UP.E()
        EES_E_DOWN[0] = EES_TauVector_DOWN.E()
        EES_Pt[0] = EES_TauVector.Pt()
        EES_Pt_UP[0] = EES_TauVector_UP.Pt()
        EES_Pt_DOWN[0] = EES_TauVector_DOWN.Pt()
        
        MES_E[0] = MES_TauVector.E()
        MES_E_UP[0] = MES_TauVector_UP.E()
        MES_E_DOWN[0] = MES_TauVector_DOWN.E()
        MES_Pt[0] = MES_TauVector.Pt()
        MES_Pt_UP[0] = MES_TauVector_UP.Pt()
        MES_Pt_DOWN[0] = MES_TauVector_DOWN.Pt()
        
        EES_MET[0] = EES_METVector.Pt()
        EES_METPhi[0] = EES_METVector.Phi()
        EES_MET_UP[0] = EES_METVector_UP.Pt()
        EES_METPhi_UP[0] = EES_METVector_UP.Phi()
        EES_MET_DOWN[0] = EES_METVector_DOWN.Pt()
        EES_METPhi_DOWN[0] = EES_METVector_DOWN.Phi()
        
        MES_MET[0] = MES_METVector.Pt()
        MES_METPhi[0] = MES_METVector.Phi()
        MES_MET_UP[0] = MES_METVector_UP.Pt()
        MES_METPhi_UP[0] = MES_METVector_UP.Phi()
        MES_MET_DOWN[0] = MES_METVector_DOWN.Pt()
        MES_METPhi_DOWN[0] = MES_METVector_DOWN.Phi()
        
        if(not args.NoEnergyCorrect):
            EES_E_Branch.Fill()
            EES_Pt_Branch.Fill()
            MES_E_Branch.Fill()
            MES_Pt_Branch.Fill()
            
            EES_MET_Branch.Fill()
            EES_METPhi_Branch.Fill()
            MES_MET_Branch.Fill()
            MES_METPhi_Branch.Fill()
        
        EES_E_UP_Branch.Fill()
        EES_E_DOWN_Branch.Fill()
        EES_Pt_UP_Branch.Fill()
        EES_Pt_DOWN_Branch.Fill()
        
        MES_E_UP_Branch.Fill()
        MES_E_DOWN_Branch.Fill()
        MES_Pt_UP_Branch.Fill()
        MES_Pt_DOWN_Branch.Fill()
        
        EES_MET_UP_Branch.Fill()
        EES_METPhi_UP_Branch.Fill()
        EES_MET_DOWN_Branch.Fill()
        EES_METPhi_DOWN_Branch.Fill()
        
        MES_MET_UP_Branch.Fill()
        MES_METPhi_UP_Branch.Fill()
        MES_MET_DOWN_Branch.Fill()
        MES_METPhi_DOWN_Branch.Fill()
    
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the muon to tau and electron to tau fake energy scale branches")
    parser.add_argument('year',choices=["2016","2017","2018"])
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")
    parser.add_argument('--NoEnergyCorrect',help="Only store uncertainties, do not save corrected energy branches for the tau",action="store_true")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing EES and MES for "+str(File))
        ApplyEESandMES(File,args)
