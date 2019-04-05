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
    EES_E_UP_Branch = TheTree.Branch("EES_E_UP",EES_E_UP,"EES_E_UP/F")
    EES_E_DOWN_Branch = TheTree.Branch("EES_E_DOWN",EES_E_DOWN,"EES_E_DOWN/F")
    EES_Pt_UP_Branch = TheTree.Branch("EES_Pt_UP",EES_Pt_UP,"EES_Pt_UP/F")
    EES_Pt_DOWN_Branch = TheTree.Branch("EES_Pt_DOWN".EES_Pt_DOWN,"EES_Pt_DOWN/F")

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

    for i in tqdm(range(TheTree,GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        METVector = ROOT.TLorentzVector()
        METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        CorrectedTauVector = ROOT.TLorentzVector()
        CorrectedTauVector_UP = ROOT.TLorentzVector()
        CorrectedTauVector_DOWN = ROOT.TLorentzVector()

        #2016/2018 MES/EES
        if(args.year =="2016" or args.year == "2018"):
            raise RuntimeError("2018 and 2016 not impletmented yet! Implement me!")
        #2017 MES/EES
        if(args.year == "2017"):
            #EES
            if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3 ):
                if args.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.0
                
            #MES
            elif(TheTrre.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                if():
                if args.NoEnergyCorrect:
                    EnergyCorrectFactor = 0.0
                else:
                    EnergyCorrectFactor = 0.0
                CorrectedTauVector
            #nothing doing. Do trivial things
            else:
            
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the muon to tau and electron to tau fake energy scale branches")
    parser.add_argument('year',choices=["2016","2017","2018"])
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")
    parser.add_argument('--NoEnergyCorrect',help="Only store uncertainties, do not save corrected energy branches for the tau")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing EES and MES for "+str(File))
        ApplyEESandMES(File,args)
