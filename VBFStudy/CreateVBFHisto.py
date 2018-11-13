import ROOT
import sys
from tqdm import tqdm
from array import array
import CountVBFEvents as CVBF

def CreateVBFHisto(FileToRun):
    njetsCuts = [2.0,6.0]
    mjjCuts = [100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0]

    njetarray = array('f',njetsCuts)
    mjjarray = array('f',mjjCuts)

    TheEfficiencyHisto = ROOT.TH2F("VetoEfficiency", "VetoEfficiency",len(mjjarray)-1,mjjarray,len(njetarray)-1,njetarray)

    for njetsCut in njetsCuts:
        for mjjCut in mjjCuts:
            Percentage = CVBF.CountVBFEvents(FileToRun,njetsCut,mjjCut)
            print(Percentage)
            TheEfficiencyHisto.Fill(mjjCut,njetsCut,Percentage)
    
    ROOT.gStyle.SetOptStat(0)

    TheEfficiencyHisto.SetOption("COLZ")
    TheEfficiencyHisto.SetTitle("Noisy Jet Veto Signal Efficiency")
    TheEfficiencyHisto.GetXaxis().SetTitle("m_{jj} >")
    TheEfficiencyHisto.GetYaxis().SetTitle("njets >")
    TheEfficiencyHisto.Draw()

    raw_input("Press Enter to Continue...")

if __name__ == "__main__":
    for File in sys.argv[1:]:
        print("Creating VBFHisto...")
        CreateVBFHisto(File)
