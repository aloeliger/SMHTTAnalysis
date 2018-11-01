import ROOT
import sys
from tqdm import tqdm
from array import array

def AddMuWeightingsToEvent(FileToRun):
    ID_SF_File = ROOT.TFile.Open("Weightings/RunBCDEF_SF_ID.root")
    ISO_SF_File = ROOT.TFile.Open("Weightings/RunBCDEF_SF_ISO.root")
    SingleLeptonTrigger_SF_File = ROOT.TFile.Open("Weightings/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root")

    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    Mu_ID_SF = array('f',[0])
    Mu_Iso_SF = array('f',[0])
    Mu_Trigger_SF = array('f',[0])

    ReweightFile.mt_tree.Branch('Mu_ID_SF',Mu_ID_SF,'Mu_ID_SF/F')
    ReweightFile.mt_tree.Branch('Mu_Iso_SF',Mu_Iso_SF,'Mu_Iso_SF/F')
#ReweightFile.mt_tree.Branch('Mu_Trigger_SF',Mu_Iso_SF,'Mu_Trigger_SF/F')

    for i in tqdm(range(ReweightFile.mt_tree.GetEntries())):
        ReweightFile.mt_tree.GetEntry(i)
    #ReweightFile.mt_tree.pt_1 gets the muon pt
    #ReweightFile.mt_tree.eta_1 gets the muon eta    
        Mu_ID_SF[0] = ID_SF_File.NUM_MediumID_DEN_genTracks_pt_abseta.GetBinContent(ID_SF_File.NUM_MediumID_DEN_genTracks_pt_abseta.FindBin(ReweightFile.mt_tree.pt_1,abs(ReweightFile.mt_tree.eta_1)))
        Mu_Iso_SF[0] = ISO_SF_File.NUM_TightRelIso_DEN_MediumID_pt_abseta.GetBinContent(ISO_SF_File.NUM_TightRelIso_DEN_MediumID_pt_abseta.FindBin(ReweightFile.mt_tree.pt_1,abs(ReweightFile.mt_tree.eta_1)))

        ReweightFile.mt_tree.Fill()

    ReweightFile.mt_tree.Write()
    ReweightFile.Write()
    ReweightFile.Close()

if __name__ == "__main__":
    for File in sys.argv[1:]:
        print("Processing Muon ID and Iso SF's on "+File)
        AddMuWeightingsToEvent(File)
