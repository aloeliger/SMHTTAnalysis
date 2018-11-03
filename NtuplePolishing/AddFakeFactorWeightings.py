import ROOT
import sys
from tqdm import tqdm
from array import array
from math import sqrt
from math import cos

#we'll need these later
#may as well be global too.
DataFile = ROOT.TFile("/data/aloeliger/SMHTTData/Data.root")
DYFile = ROOT.TFile("/data/aloeliger/SMHTTData/DY.root")
WFile = ROOT.TFile("/data/aloeliger/SMHTTData/W.root")
TTChain =  ROOT.TChain("mt_tree")
TTChain.Add("/data/aloeliger/SMHTTData/TTTo2L2Nu.root")
TTChain.Add("/data/aloeliger/SMHTTData/TTToHadronic.root")
TTChain.Add("/data/aloeliger/SMHTTData/TTToSemiLeptonic.root")
VVChain = ROOT.TChain("mt_tree")
VVChain.Add("/data/aloeliger/SMHTTData/WW.root")
VVChain.Add("/data/aloeliger/SMHTTData/WZ.root")
VVChain.Add("/data/aloeliger/SMHTTData/ZZ.root")

Frac_w = 0.0
Frac_tt = 0.0
Frac_real = 0.0
Frac_qcd = 0.0

def AddFakeFactorWeightings(FileToRun):
    ff_file = ROOT.TFile.Open("/data/aloeliger/CMSSW_9_4_0/src/HTTutilities/Jet2TauFakes/data/SM2017/tight/vloose/mt/fakeFactors.root")
    ff = ff_file.Get('ff_comb')

    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    Event_Fake_Factor = array('f',[0])    

    ReweightFile.mt_tree.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')    

    for i in tqdm(range(ReweightFile.mt_tree.GetEntries())):
        ReweightFile.mt_tree.GetEntry(i)
        
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_tree.pt_1,
                              ReweightFile.mt_tree.eta_1,
                              ReweightFile.mt_tree.phi_1,
                              ReweightFile.mt_tree.m_1)
        
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(ReweightFile.mt_tree.pt_2,
                               ReweightFile.mt_tree.eta_2,
                               ReweightFile.mt_tree.phi_2,
                               ReweightFile.mt_tree.m_2)

        MissingMomentumVector = ROOT.TLorentzVector()
        MissingMomentumVector.SetPtEtaPhiM(ReweightFile.mt_tree.met,
                                           0,
                                           ReweightFile.mt_tree.metphi,
                                           0)

        m_vis = (MuVector + TauVector).M()
        TransverseMass = sqrt(2.0*MuVector.Pt()*MissingMomentumVector.Pt()*(1.0-cos(MuVector.DeltaPhi(MissingMomentumVector))))

        inputs = [ReweightFile.mt_tree.pt_2,
                  ReweightFile.mt_tree.l2_decayMode,
                  ReweightFile.mt_tree.njets,
                  m_vis,
                  TransverseMass,
                  ReweightFile.mt_tree.iso_1,
                  Frac_qcd,
                  Frac_w,
                  Frac_tt]

        Event_Fake_Factor[0] = ff.value(len(inputs),array('d',inputs))
        
        ReweightFile.mt_tree.Fill()

    print("Cleaning up Fakes")
    ff.Delete()
    ff_file.Close()

    print("Writing Tree")
    ReweightFile.mt_tree.Write()
    print("Writing File")
    ReweightFile.Write()
    ReweightFile.Close()
        
#This is composed of (W+ZJ+VVJ)/ data events
def CalculateFractionW():
    WJetsEvents = 0.0
    #WJets Sample is all W+Jets
    WJetsEvents += (WFile.mt_tree.GetEntries())*1.0
    #The remainder is gen match = 6 DY and VV
    for i in tqdm(range(DYFile.mt_tree.GetEntries())):
        DYFile.mt_tree.GetEntry(i)
        if(DYFile.mt_tree.gen_match_2 == 6.0):
            WJetsEvents += 1.0
    for i in tqdm(range(VVChain.GetEntries())):
        VVChain.GetEntry(i)
        if(VVChain.gen_match_2 == 6.0):
            WJetsEvents += 1.0
    return (WJetsEvents / DataFile.mt_tree.GetEntries())

#This is composed of (TTJ) / data
def CalculateFractionTT():
    TTJetsEvents = 0.0
    for i in tqdm(range(TTChain.GetEntries())):
        TTChain.GetEntry(i)
        if(TTChain.gen_match_2 == 6.0):
            TTJetsEvents += 1.0
    return (TTJetsEvents / DataFile.mt_tree.GetEntries())

#this is given by (ZTT+TTT+VVT)/data
def CalculateFractionReal():
    RealEvents = 0.0
    #look at DY gen_match_2 < 5
    for i in tqdm(range(DYFile.mt_tree.GetEntries())):
        DYFile.mt_tree.GetEntry(i)
        if(DYFile.mt_tree.gen_match_2 < 5.0):
            RealEvents += 1.0
    #look at TT gen_match_2 < 5
    for i in tqdm(range(TTChain.GetEntries())):
        TTChain.GetEntry(i)
        if(TTChain.gen_match_2 < 5.0):
            RealEvents += 1.0
    #now check the diboson
    for i in tqdm(range(VVChain.GetEntries())):
        VVChain.GetEntry(i)
        if(VVChain.gen_match_2 < 5.0):
            RealEvents += 1.0
    return (RealEvents/DataFile.mt_tree.GetEntries())

if __name__ == "__main__":
    print("Processing Fraction WJets")
    Frac_w = CalculateFractionW()
    print("Processing Fraction tt Jets")
    Frac_tt = CalculateFractionTT()
    print("Processing Fraction Real")
    Frac_real = CalculateFractionReal()
    print("Processing Fraction QCD")
    Frac_qcd = 1.0 -(Frac_w + Frac_tt + Frac_real)    
    for File in sys.argv[1:]:
        print("Processing Fake Factors on "+File)
        AddFakeFactorWeightings(File)
    pass
