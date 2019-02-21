import ROOT
import sys
import math
from array import array
from tqdm import tqdm

def CalculatePZeta(FileName):
    TheFile = ROOT.TFile(FileName,"UPDATE")
    TheTree = TheFile.mt_tree
    PZeta_Value = array('f',[0.])
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
        PZeta = px*zetaX+py*zetaY
        
        PZeta_Value[0] = (PZeta-0.85*PZetaVis)
        PZeta_Branch.Write()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()

if __name__ == "__main__":
    for File in sys.argv[1:]:
        print("Adding PZeta branch to "+File)
        CaulculatePZeta(File)
