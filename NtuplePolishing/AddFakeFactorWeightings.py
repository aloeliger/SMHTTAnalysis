import ROOT
import sys
from tqdm import tqdm
from array import array
from math import sqrt
from math import cos

WFracHisto = ROOT.TH1F("WFrac","WFrac", 20,0.0,500.0)
QCDFracHisto = ROOT.TH1F("QCDFrac","QCDFrac", 20,0.0,500.0)
TTFracHisto = ROOT.TH1F("TTFrac","TTFrac", 20,0.0,500.0)
dataFracHisto = ROOT.TH1F("DataFrac","DataFrac", 20,0.0,500.0)
RealFracHisto = ROOT.TH1F("RealFrac","RealFrac", 20,0.0,500.0)

#okay, we just need to fill a few histograms with tau_pt, and vis mass.
def MakeFractions(TheDirectory):
    print("Making fractions...")
    #all Anti iso, then split by categories
    #ZJ: DY MC, take gen_match_2 == 6
    #VVJ: for VV MC, take gen_match_2 == 6
    #TTJ: for TT MC, take gen_match_2 == 6
    #data_obs: just take data 
    #embedded: just take the embedded
    #ZL: DY MC, take gen_match_2 < 5 
    #EWK, not available
    #TTT: for TT MC take gen_match_2 == 5
    #TTL for TT MC take gen_match_2 < 5
    #VVT for VV MC take gen_match_2 == 5
    #VVL for VV MC take gen_match_2 < 5

    #W region :  W+ZJ+VVJ
    #TT region : TTJ
    #Data region: data_obs
    #real region: Embedded+ZL+TTTTTL+VVT+VVL
    #QCD: Data - real - TT- W

    #then we also split up these distributions by tau pt, and vis mass
    #Then, and only then, can we go about using them to calculate
    #fake factors on the anti-isolated data.
    #this doesn't support modularity real well, but what the hey.

    DataFile = ROOT.TFile(TheDirectory+"Data.root")
    DataTree = DataFile.mt_Selected
    
    DYFile = ROOT.TFile(TheDirectory+"DY.root")
    DYTree = DYFile.mt_Selected
    
    #EmbeddedFile = ROOT.TFile(TheDirectory+"Embedded.root")
    #EmbeddedTree = EmbeddedFile.mt_Selected
    
    #ST_t_antitopFile = ROOT.TFile(TheDirectory+"ST_t_antitop.root")
    #ST_t_antitopTree = ST_t_antitopFile.mt_Selected

    #ST_t_topFile = ROOT.TFile(TheDirectory+"ST_t_top.root")
    #ST_t_topTree = ST_t_topFile.mt_Selected

    #ST_tW_antitopFile = ROOT.TFile(TheDirectory+"ST_tW_antitop.root")
    #ST_tW_antitopTree = ST_tW_antitopFile.mt_Selected

    ST_tW_topFile = ROOT.TFile(TheDirectory+"ST_tW_top.root")
    ST_tW_topTree = ST_tW_topFile.mt_Selected

    TTTo2L2NuFile = ROOT.TFile(TheDirectory+"TTTo2L2Nu.root")
    TTTo2L2NuTree = TTTo2L2NuFile.mt_Selected

    TTToHadronicFile = ROOT.TFile(TheDirectory+"TTToHadronic.root")
    TTToHadronicTree = TTToHadronicFile.mt_Selected

    TTToSemiLeptonicFile = ROOT.TFile(TheDirectory+"TTToSemiLeptonic.root")
    TTToSemiLeptonicTree = TTToSemiLeptonicFile.mt_Selected

    #ironically doesn't seem to be used in the 
    #Wjets fraction right now?
    #can't find it in cecile's mess.
    #WFile = ROOT.TFile(TheDirectory+"W.root")
    #WTree  = WFile.mt_Selected
    
    WWFile = ROOT.TFile(TheDirectory+"WW.root")
    WWTree  = WWFile.mt_Selected

    WZFile = ROOT.TFile(TheDirectory+"WZ.root")
    WZTree  = WZFile.mt_Selected
    
    ZZFile = ROOT.TFile(TheDirectory+"ZZ.root")
    ZZTree  = ZZFile.mt_Selected

    WFile = ROOT.TFile(TheDirectory+"W.root")
    WTree = WFile.mt_Selected

    #okay, now we start running trees
    #and doing the stuff.

    WFilledEvents = 0.0
    QCDFilledEvents = 0.0
    TTFilledEvents = 0.0
    dataFilledEvents = 0.0
    RealFilledEvents = 0.0
    RealEventsFromDY = 0.0
    RealEventsFromST = 0.0
    RealEventsFromTT = 0.0
    RealEventsFromVV = 0.0

    AverageRealWeight = 0.0
    AvRealWeightFromDY = 0.0
    AvRealWeightFromST = 0.0
    AvRealWeightFromTT = 0.0
    AvRealWeightFromVV = 0.0

    for i in tqdm(range(DataTree.GetEntries())):
        DataTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(DataTree.pt_1,DataTree.eta_1,DataTree.phi_1,DataTree.m_1)
        TauVector.SetPtEtaPhiM(DataTree.pt_2,DataTree.eta_2,DataTree.phi_2,DataTree.m_2)
        QCDFilledEvents+=1.0
        QCDFracHisto.Fill((TauVector+MuVector).M())
        dataFilledEvents+=1.0
        dataFracHisto.Fill((TauVector+MuVector).M())
    
    for i in tqdm(range(DYTree.GetEntries())):
        DYTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(DYTree.pt_1,DYTree.eta_1,DYTree.phi_1,DYTree.m_1)
        TauVector.SetPtEtaPhiM(DYTree.pt_2,DYTree.eta_2,DYTree.phi_2,DYTree.m_2)        
        #ZJ, fill the W region
        if DYTree.gen_match_2 == 6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),DYTree.FinalWeighting)
        #ZL fill the real region
        elif DYTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromDY+=1.0
            AverageRealWeight += DYTree.FinalWeighting
            AvRealWeightFromDY += DYTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),DYTree.FinalWeighting)
    #no embedded available for 2018 yet
    """
    for i in tqdm(range(EmbeddedTree.GetEntries())):
        EmbeddedTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(EmbeddedTree.pt_1,EmbeddedTree.eta_1,EmbeddedTree.phi_1,EmbeddedTree.m_1)
        TauVector.SetPtEtaPhiM(EmbeddedTree.pt_2,EmbeddedTree.eta_2,EmbeddedTree.phi_2,EmbeddedTree.m_2)
        RealFracHisto.Fill((TauVector+MuVector).M())
     """

    #St->VVT and VVL and VVJ
    #only have ST_tW_top at the moment
    """
    for i in tqdm(range(ST_t_antitopTree.GetEntries())):
        ST_t_antitopTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ST_t_antitopTree.pt_1,ST_t_antitopTree.eta_1,ST_t_antitopTree.phi_1,ST_t_antitopTree.m_1)
        TauVector.SetPtEtaPhiM(ST_t_antitopTree.pt_2,ST_t_antitopTree.eta_2,ST_t_antitopTree.phi_2,ST_t_antitopTree.m_2)
        if ST_t_antitopTree.gen_match_2 <= 5:
            RealFracHisto.Fill((TauVector+MuVector).M(),ST_t_antitopTree.FinalWeighting)
        elif ST_t_antiTopTree.gen_match_2 == 6:
            WFracHisto.Fill((TauVector+MuVector).M(),ST_t_antitopTree.FinalWeighting)

    for i in tqdm(range(ST_t_topTree.GetEntries())):
        ST_t_topTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ST_t_topTree.pt_1,ST_t_topTree.eta_1,ST_t_topTree.phi_1,ST_t_topTree.m_1)
        TauVector.SetPtEtaPhiM(ST_t_topTree.pt_2,ST_t_topTree.eta_2,ST_t_topTree.phi_2,ST_t_topTree.m_2)
        if ST_t_topTree.gen_match_2 <= 5:
            RealFracHisto.Fill((TauVector+MuVector).M(),ST_t_topTree.FinalWeighting)
        if ST_t_topTree.gen_match_2 == 6:
            WFracHisto.Fill((TauVector+MuVector).M(),ST_t_topTree.FinalWeighting)
            
    for i in tqdm(range(ST_tW_antitopTree.GetEntries())):
        ST_tW_antitopTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ST_tW_antitopTree.pt_1,ST_tW_antitopTree.eta_1,ST_tW_antitopTree.phi_1,ST_tW_antitopTree.m_1)
        TauVector.SetPtEtaPhiM(ST_tW_antitopTree.pt_2,ST_tW_antitopTree.eta_2,ST_tW_antitopTree.phi_2,ST_tW_antitopTree.m_2)
        if ST_tW_antitopTree.gen_match_2 <= 5:
            RealFracHisto.Fill((TauVector+MuVector).M(),ST_tW_antitopTree.FinalWeighting)
        if ST_tW_antitopTree.gen_match_2 == 6:
            WFracHisto.Fill((TauVector+MuVector).M(),ST_tW_antitopTree.FinalWeighting)
            """

    for i in tqdm(range(ST_tW_topTree.GetEntries())):
        ST_tW_topTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ST_tW_topTree.pt_1,ST_tW_topTree.eta_1,ST_tW_topTree.phi_1,ST_tW_topTree.m_1)
        TauVector.SetPtEtaPhiM(ST_tW_topTree.pt_2,ST_tW_topTree.eta_2,ST_tW_topTree.phi_2,ST_tW_topTree.m_2)
        if ST_tW_topTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromST+=1.0
            AverageRealWeight+=ST_tW_topTree.FinalWeighting
            AvRealWeightFromST+=ST_tW_topTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),ST_tW_topTree.FinalWeighting)
        if ST_tW_topTree.gen_match_2 == 6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),ST_tW_topTree.FinalWeighting)

    for i in tqdm(range(TTTo2L2NuTree.GetEntries())):
        TTTo2L2NuTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TTTo2L2NuTree.pt_1,TTTo2L2NuTree.eta_1,TTTo2L2NuTree.phi_1,TTTo2L2NuTree.m_1)
        TauVector.SetPtEtaPhiM(TTTo2L2NuTree.pt_2,TTTo2L2NuTree.eta_2,TTTo2L2NuTree.phi_2,TTTo2L2NuTree.m_2)
        if TTTo2L2NuTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromTT+=1.0
            AverageRealWeight+=TTTo2L2NuTree.FinalWeighting
            AvRealWeightFromTT+=TTTo2L2NuTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),TTTo2L2NuTree.FinalWeighting)
        elif TTTo2L2NuTree.gen_match_2 ==6:
            TTFilledEvents+=1.0
            TTFracHisto.Fill((TauVector+MuVector).M(),TTTo2L2NuTree.FinalWeighting)

    for i in tqdm(range(TTToHadronicTree.GetEntries())):
        TTToHadronicTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TTToHadronicTree.pt_1,TTToHadronicTree.eta_1,TTToHadronicTree.phi_1,TTToHadronicTree.m_1)
        TauVector.SetPtEtaPhiM(TTToHadronicTree.pt_2,TTToHadronicTree.eta_2,TTToHadronicTree.phi_2,TTToHadronicTree.m_2)
        if TTToHadronicTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromTT+=1.0
            AverageRealWeight+=TTToHadronicTree.FinalWeighting
            AvRealWeightFromTT+=TTToHadronicTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),TTToHadronicTree.FinalWeighting)
        elif TTToHadronicTree.gen_match_2 ==6:
            TTFilledEvents+=1.0
            TTFracHisto.Fill((TauVector+MuVector).M(),TTToHadronicTree.FinalWeighting)

    for i in tqdm(range(TTToSemiLeptonicTree.GetEntries())):
        TTToSemiLeptonicTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TTToSemiLeptonicTree.pt_1,TTToSemiLeptonicTree.eta_1,TTToSemiLeptonicTree.phi_1,TTToSemiLeptonicTree.m_1)
        TauVector.SetPtEtaPhiM(TTToSemiLeptonicTree.pt_2,TTToSemiLeptonicTree.eta_2,TTToSemiLeptonicTree.phi_2,TTToSemiLeptonicTree.m_2)
        if TTToSemiLeptonicTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromTT+=1.0
            AverageRealWeight+=TTToSemiLeptonicTree.FinalWeighting
            AvRealWeightFromTT+=TTToSemiLeptonicTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),TTToSemiLeptonicTree.FinalWeighting)
        elif TTToSemiLeptonicTree.gen_match_2 ==6:
            TTFilledEvents+=1.0
            TTFracHisto.Fill((TauVector+MuVector).M(),TTToSemiLeptonicTree.FinalWeighting)

    for i in tqdm(range(WWTree.GetEntries())):
        WWTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(WWTree.pt_1,WWTree.eta_1,WWTree.phi_1,WWTree.m_1)
        TauVector.SetPtEtaPhiM(WWTree.pt_2,WWTree.eta_2,WWTree.phi_2,WWTree.m_2)
        if WWTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromVV+=1.0
            AverageRealWeight+=WWTree.FinalWeighting
            AvRealWeightFromVV+=WWTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),WWTree.FinalWeighting)
        elif WWTree.gen_match_2 ==6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),WWTree.FinalWeighting)

    for i in tqdm(range(WZTree.GetEntries())):
        WZTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(WZTree.pt_1,WZTree.eta_1,WZTree.phi_1,WZTree.m_1)
        TauVector.SetPtEtaPhiM(WZTree.pt_2,WZTree.eta_2,WZTree.phi_2,WZTree.m_2)
        if WZTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromVV+=1.0
            AverageRealWeight+=WZTree.FinalWeighting
            AvRealWeightFromVV+=WZTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),WZTree.FinalWeighting)
        elif WZTree.gen_match_2 ==6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),WZTree.FinalWeighting)

    for i in tqdm(range(ZZTree.GetEntries())):
        ZZTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ZZTree.pt_1,ZZTree.eta_1,ZZTree.phi_1,ZZTree.m_1)
        TauVector.SetPtEtaPhiM(ZZTree.pt_2,ZZTree.eta_2,ZZTree.phi_2,ZZTree.m_2)
        if ZZTree.gen_match_2 <= 5:
            RealFilledEvents+=1.0
            RealEventsFromVV+=1.0
            AverageRealWeight+=ZZTree.FinalWeighting
            AvRealWeightFromVV+=ZZTree.FinalWeighting
            RealFracHisto.Fill((TauVector+MuVector).M(),ZZTree.FinalWeighting)
        elif ZZTree.gen_match_2 ==6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),ZZTree.FinalWeighting)
        
    for i in tqdm(range(WTree.GetEntries())):
        WTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(WTree.pt_1,WTree.eta_1,WTree.phi_1,WTree.m_1)
        TauVector.SetPtEtaPhiM(WTree.pt_2,WTree.eta_2,WTree.phi_2,WTree.m_2)
        if WTree.gen_match_2 <= 5:
            RealFilledEvents +=1.0
            RealFracHisto.Fill((TauVector+MuVector).M(),WTree.FinalWeighting)
        elif WTree.gen_match_2 ==6:
            WFilledEvents+=1.0
            WFracHisto.Fill((TauVector+MuVector).M(),WTree.FinalWeighting)

    QCDFracHisto.Add(RealFracHisto,-1)
    QCDFracHisto.Add(TTFracHisto,-1)
    QCDFracHisto.Add(WFracHisto,-1)

    print("WFilledEvents: "+str(WFilledEvents))
    print("QCDFilledEvents: "+str(QCDFilledEvents))
    print("TTFilledEvents: "+str(TTFilledEvents))
    print("dataFilledEvents: "+str(dataFilledEvents))
    print("RealFilledEvents: "+str(RealFilledEvents))
    print("")
    AverageRealWeight = AverageRealWeight/RealFilledEvents
    AvRealWeightFromDY = AvRealWeightFromDY/RealEventsFromDY
    AvRealWeightFromST = AvRealWeightFromST/RealEventsFromST
    AvRealWeightFromTT = AvRealWeightFromTT/RealEventsFromTT
    AvRealWeightFromVV = AvRealWeightFromVV/RealEventsFromVV
    print("AverageRealWeight: "+str(AverageRealWeight))
    print("RealEventsFromDY: "+str(RealEventsFromDY))
    print("RealEventsFromST: "+str(RealEventsFromST))
    print("RealEventsFromTT: "+str(RealEventsFromTT))
    print("RealEventsFromVV: "+str(RealEventsFromVV))
    print("AvRealWeightFromDY: "+str(AvRealWeightFromDY))
    print("AvRealWeightFromST: "+str(AvRealWeightFromST))
    print("AvRealWeightFromTT: "+str(AvRealWeightFromTT))
    print("AvRealWeightFromVV: "+str(AvRealWeightFromVV))

    WCanvas = ROOT.TCanvas("WCanvas","WCanvas")
    WFracHisto.Draw()
    QCDCanvas = ROOT.TCanvas("QCDCanvas","QCDCanvas")
    QCDFracHisto.Draw()
    TTCanvas = ROOT.TCanvas("TTCanvas","TTCanvas")
    TTFracHisto.Draw()
    DataCanvas = ROOT.TCanvas("DataCanvas","DataCanvas")
    dataFracHisto.Draw()
    RealCanvas = ROOT.TCanvas("RealCanvas","RealCanvas")
    RealFracHisto.Draw()    
    raw_input("Press Enter to Continue...")

def AddFakeFactorWeightings(FileToRun):
    print("Adding Fake Factors to "+FileToRun)
    ff_file = ROOT.TFile.Open("/data/aloeliger/CMSSW_9_4_0/src/HTTutilities/Jet2TauFakes/data/SM2017/tight/vloose/mt/fakeFactors.root")
    ff = ff_file.Get('ff_comb')

    ReweightFile = ROOT.TFile(FileToRun,"UPDATE")
    Event_Fake_Factor = array('f',[0.])    

    FakeFactorBranch = ReweightFile.mt_Selected.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')

    for i in tqdm(range(ReweightFile.mt_Selected.GetEntries())):
        ReweightFile.mt_Selected.GetEntry(i)

        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_1,
                              ReweightFile.mt_Selected.eta_1,
                              ReweightFile.mt_Selected.phi_1,
                              ReweightFile.mt_Selected.m_1)
        
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(ReweightFile.mt_Selected.pt_2,
                               ReweightFile.mt_Selected.eta_2,
                               ReweightFile.mt_Selected.phi_2,
                               ReweightFile.mt_Selected.m_2)

        MissingMomentumVector = ROOT.TLorentzVector()
        MissingMomentumVector.SetPtEtaPhiM(ReweightFile.mt_Selected.met,
                                           0,
                                           ReweightFile.mt_Selected.metphi,
                                           0)

        FracQCD = QCDFracHisto.GetBinContent(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))/dataFracHisto.GetBinContent(dataFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))
        #print("Num: "+str(QCDFracHisto.GetBinContent(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))))
        #print("\tVisMass: "+str((TauVector+MuVector).M()))
        #print("\tBin: "+str(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M())))
        #print("Denom: "+str(dataFracHisto.GetBinContent(dataFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))))
        #print("FracQCD: "+str(FracQCD))
        FracW = WFracHisto.GetBinContent(WFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))/dataFracHisto.GetBinContent(dataFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))
        FracTT = TTFracHisto.GetBinContent(TTFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))/dataFracHisto.GetBinContent(dataFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()))

        m_vis = (MuVector + TauVector).M()
        TransverseMass = sqrt(2.0*MuVector.Pt()*MissingMomentumVector.Pt()*(1.0-cos(MuVector.DeltaPhi(MissingMomentumVector))))

        inputs = [TauVector.Pt(),
                  ReweightFile.mt_Selected.l2_decayMode,
                  ReweightFile.mt_Selected.njets,
                  m_vis,
                  TransverseMass,
                  ReweightFile.mt_Selected.iso_1,
                  FracQCD,
                  FracW,
                  FracTT]

        Event_Fake_Factor[0] = ff.value(len(inputs),array('d',inputs))

        FakeFactorBranch.Fill()        
    
    ff.Delete()
    ff_file.Close()

    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()
    
if __name__ == "__main__":
    MakeFractions(sys.argv[2])
    AddFakeFactorWeightings(sys.argv[1])

        
