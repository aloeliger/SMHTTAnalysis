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

    FakeFactorBranch = ReweightFile.mt_tree.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')

    TauPTHisto = ROOT.TH1F("TauPT","TauPT", 20, 0, 200.0)
    TauDecayModeHisto = ROOT.TH1F("TauDecayMode", "TauDecayMode", 11, 0.0, 11.0)
    NJetsHisto = ROOT.TH1F("NJetsHisto","NJetsHisto", 20, 0.0, 20.0)
    m_visHisto = ROOT.TH1F("m_visHisto","m_visHisto", 20, 0.0, 200.0)
    TransverseMassHisto = ROOT.TH1F("TransverseMass","TransverseMass", 20, 0.0, 200.0)
    IsoParameterHisto = ROOT.TH1F("IsoParameterHisto","IsoParameterHisto", 20, 0.0, 1.0)
    

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
                  0.155,#Frac_qcd,
                  0.830,#Frac_w,
                  0.0016]#Frac_tt]

        TauPTHisto.Fill(ReweightFile.mt_tree.pt_2)
        TauDecayModeHisto.Fill(ReweightFile.mt_tree.l2_decayMode)
        NJetsHisto.Fill(ReweightFile.mt_tree.njets)
        m_visHisto.Fill(m_vis)
        TransverseMassHisto.Fill(TransverseMass)
        IsoParameterHisto.Fill(ReweightFile.mt_tree.iso_1)

        Event_Fake_Factor[0] = ff.value(len(inputs),array('d',inputs))                
        
        FakeFactorBranch.Fill()

    ff.Delete()
    ff_file.Close()        
    
    DiagnosticFile = ROOT.TFile("Diagnostics.root","RECREATE")
    TauPTHisto.Write()
    TauDecayModeHisto.Write()
    NJetsHisto.Write()
    m_visHisto.Write()
    TransverseMassHisto.Write()
    IsoParameterHisto.Write()

    ReweightFile.cd()
    ReweightFile.mt_tree.Write()    
    ReweightFile.Write()
    ReweightFile.Close()    

    raw_input("Press Enter to continue...")
        
#Okay, we may need to take a stab at this in the actual signal region to get proper fractions
#how do we do that? I barely know what the signal region is at this point.
#let's just make a thing we pass a whatever too and it checks the stuff and tells us if we're good
#From there we'll put in the old Tau ID signal region selection and we'll take stab?
"""
def IsSelectedEvent(TheTree):
    IsGoodEvent = True

    MuVector = ROOT.TLorentzVector(TheTree.pt_1, TheTree.eta_1, TheTree.phi_1, TheTree.e_1)
    TauVector = ROOT.TLorentzVector(TheTree.pt_2, TheTree.eta_2, TheTree.phi_2, TheTree.e_2)
    
    if(TheTree.pt_1 < 30.0 or abs(TheTree.eta_1) > 2,4 or not TheTree.id_m_medium_1 or TheTree.iso_1 > 0.15 or 
       abs(TheTree.dZ_1) > 0.2 or abs(d0_1) > 0.045 or not TheTree.matchIsoMu27_1)

"""

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
    print(WJetsEvents / DataFile.mt_tree.GetEntries())
    return (WJetsEvents / DataFile.mt_tree.GetEntries())

#This is composed of (TTJ) / data
def CalculateFractionTT():
    TTJetsEvents = 0.0
    for i in tqdm(range(TTChain.GetEntries())):
        TTChain.GetEntry(i)
        if(TTChain.gen_match_2 == 6.0):
            TTJetsEvents += 1.0
    print (TTJetsEvents / DataFile.mt_tree.GetEntries())
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
    print(RealEvents/DataFile.mt_tree.GetEntries())
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
    print(Frac_qcd)
    for File in sys.argv[1:]:
        print("Processing Fake Factors on "+File)
        AddFakeFactorWeightings(File)        
    
