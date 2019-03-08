import ROOT
import sys
import math
from array import array
from tqdm import tqdm
import argparse

def CalculatePZeta(FileName,args):
    TheFile = ROOT.TFile(FileName,"UPDATE")
    TheTree = TheFile.mutau_tree
    PZetaVis_Value = array('f',[0.])
    PZetaAll_Value = array('f',[0.])
    PZeta_Value = array('f',[0.])
    PZetaVis_Branch = TheTree.Branch("PZetaVis",PZetaVis_Value,"PZetaVis/F")
    PZetaAll_Branch = TheTree.Branch("PZetaAll",PZetaAll_Value,"PZetaAll/F")
    PZeta_Branch = TheTree.Branch("PZeta",PZeta_Value,"PZeta/F")
    
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MetVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        MetVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        leg1x = math.cos(MuVector.Phi())
        leg1y = math.sin(MuVector.Phi())
        leg2x = math.cos(TauVector.Phi())
        leg2y = math.sin(TauVector.Phi())
        zetaX = leg1x+leg2x
        zetaY = leg1y+leg2y
        zetaR = math.sqrt(zetaX*zetaX+zetaY*zetaY)
        if(zetaR > 0.0):
            zetaX = zetaX/zetaR
            zetaY = zetaY/zetaR
        visPx = MuVector.Px()
        visPy = MuVector.Py()
        PZetaVis = visPx*zetaX+visPy*zetaY
        
        px = visPx+MetVector.Px()
        py = visPy+MetVector.Py()
        PZetaAll = px*zetaX+py*zetaY
        
        PZetaVis_Value[0] = PZetaVis
        PZetaAll_Value[0] = PZetaAll
        PZeta_Value[0] = (PZetaAll-1.85*PZetaVis)
        
        PZetaVis_Branch.Fill()
        PZetaAll_Branch.Fill()
        PZeta_Branch.Fill()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach TES branches.")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")

    args = parser.parse_args()

    for File in args.Files:
        print("Adding PZeta branches to "+File)
        CalculatePZeta(File,args)
