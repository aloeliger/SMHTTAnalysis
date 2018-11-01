import ROOT
import sys
import tqdm

ID_SF_File = ROOT.TFile("Weightings/RunBCDEF_SF_ID.root")
ISO_SF_File = ROOT.TFile("Weightings/RunBCDEF_SF_ISO.root")
SingleLeptonTrigger_SF_File = ROOT.TFile("Weightings/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root")

ReweightFile = ROOT.TFile.Open(sys.argv[1])

for i in range(ReweightFile.mt_tree.GetEntries()):
    TheTree.GetEntry(i)
