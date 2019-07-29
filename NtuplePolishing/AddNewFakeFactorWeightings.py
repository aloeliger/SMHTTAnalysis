import ROOT
from tqdm import tqdm
from array import array
import argparse
import FakeFactorConfiguration as cfg
import AddMTandPZeta

WFracHisto = ROOT.TH2F("WFrac","WFrac",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto = ROOT.TH2F("QCDFrac","QCDFrac",20,0.0,500.0,7,1.0,8.0)
TTFracHisto = ROOT.TH2F("TTFrac","TTFrac",20,0.0,500.0,7,1.0,8.0)
dataFracHisto = ROOT.TH2F("DataFrac","DataFrac",20,0.0,500.0,7,1.0,8.0)
RealFracHisto = ROOT.TH2F("RealFrac","RealFrac",20,0.0,500.0,7,1.0,8.0)

def MakeNtuples(path,ProcessFiles):
    Chain = ROOT.TChain("mt_Selected")
    for Process in ProcessFiles:
        Chain.Add(path+ProcessFiles[Process])
    return Chain

def MakeAllNtuples(args):
    if args.year == "2016":
        FilePath = cfg.ntuple_path_2016
        DataFiles = cfg.Data_Files_2016
        WFiles = cfg.W_Files_2016
        TTFiles = cfg.TT_Files_2016
    elif args.year == "2017":
        FilePath = cfg.ntuple_path_2017
        DataFiles = cfg.Data_Files_2017
        WFiles = cfg.W_Files_2017
        TTFiles = cfg.TT_Files_2017
    elif args.year == "2018":
        FilePath = cfg.ntuple_path_2018
        DataFiles = cfg.Data_Files_2018
        WFiles = cfg.W_Files_2018
        TTFiles = cfg.TT_Files_2018
    DataNtuple = MakeNtuples(FilePath,DataFiles)
    WNtuple = MakeNtuples(FilePath,WFiles)
    TTNtuple = MakeNtuples(FilePath,TTFiles)

    return DataNtuple,WNtuple,TTNtuple

def ProcessNtuple(Ntuple,FakeHistogram,RealHistogram):
    for i in tqdm(range(Ntuple.GetEntries())):
        Ntuple.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(Ntuple.pt_1,Ntuple.eta_1,Ntuple.phi_1,Ntuple.m_1)
        TauVector.SetPtEtaPhiM(Ntuple.pt_2,Ntuple.eta_2,Ntuple.phi_2,Ntuple.m_2)
        if Ntuple.gen_match_2 <= 5:
            RealHistogram.Fill((TauVector+MuVector).M(),ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
        elif Ntuple.gen_match_2 == 6:
            FakeHistogram.Fill((TauVector+MuVector).M(),ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
         
#function for defining what of our usual categories an event falls into
#key:
#1:ZeroJet PTH 0-10
#2:ZeroJet PTH GE10
#3:VBF PTH 0-200
#4:VBF PTH GE 200
#5:Boosted 1J
#6:Boosted GE2J
#7:Anything else
def ClassifyEvent(TheEvent):
    EventCategory = 7

    MuVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    MuVector.SetPtEtaPhiM(TheEvent.pt_1,TheEvent.eta_1,TheEvent.phi_1,TheEvent.m_1)
    TauVector.SetPtEtaPhiM(TheEvent.pt_2,TheEvent.eta_2,TheEvent.phi_2,TheEvent.m_2)
    METVector.SetPtEtaPhiM(TheEvent.met,0.0,TheEvent.metphi,0.0)

    MT = AddMTandPZeta.CalculateMT(MuVector,METVector)
    HiggsPT = (MuVector+TauVector+METVector).Pt()

    #zero jet
    if(TauVector.Pt() >= 30 and MT < 50.0 and TheEvent.njets == 0):
        if(HiggsPT <= 10.0 and HiggsPT > 0.0):
            EventCategory = 1
        elif(HiggsPT > 10.0):
            EventCategory = 2
    elif(TauVector.Pt() >= 30 and MT < 50.0 and TheEvent.njets >= 2 and TheEvent.mjj > 350.0): #vbf
        if(HiggsPT <= 200 and HiggsPT >= 0.0):
            EventCategory = 3
        elif(HiggsPT > 200):
            EventCategory = 4
    else: #boosted
        #boosted 1J
        if(TauVector.Pt() >= 30 and MT < 50 and TheEvent.njets == 1):
            EventCategory = 5
        elif(TauVector.Pt() >= 30 and MT < 50 and TheEvent.njets >= 2):
            EventCategory = 6

    return EventCategory

def MakeFractions(args):
    #get ntuples to make fractions with 
    DataNtuple,WNtuple,TTNtuple=MakeAllNtuples(args)
    #process the data ntuple
    for i in tqdm(range(DataNtuple.GetEntries())):
        DataNtuple.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(DataNtuple.pt_1,DataNtuple.eta_1,DataNtuple.phi_1,DataNtuple.m_1)
        TauVector.SetPtEtaPhiM(DataNtuple.pt_2,DataNtuple.eta_2,DataNtuple.phi_2,DataNtuple.m_2)
        QCDFracHisto.Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))
        dataFracHisto.Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))
    #fill in the remaining ones
    ProcessNtuple(WNtuple,WFracHisto,RealFracHisto)
    ProcessNtuple(TTNtuple,TTFracHisto,RealFracHisto)

    QCDFracHisto.Add(RealFracHisto,-1)
    QCDFracHisto.Add(TTFracHisto,-1)
    QCDFracHisto.Add(WFracHisto,-1)

def AddFakeFactorWeightings(FileName,args):
    print("Adding Fake Factors to "+FileName)
    if args.year == "2017":
        ff_file = ROOT.TFile.Open("/data/aloeliger/CMSSW_9_4_0/src/HTTutilities/Jet2TauFakes/data/SM2017/tight/vloose/mt/fakeFactors.root")
    elif args.year == "2018":
        ff_file = ROOT.TFile.Open("/data/aloeliger/CMSSW_9_4_0/src/HTTutilities/Jet2TauFakes/data2018/SM2018/tight/vloose/mt/fakeFactors.root")
    elif args.year == "2016":
        ff_file = ROOT.TFile.Open("/data/aloeliger/CMSSW_9_4_0/src/HTTutilities/Jet2TauFakes/data2016/SM2016_ML/tight/mt/fakeFactors_tight.root")
    print("Retrieving Fake Factors from file")
    ff = ff_file.Get('ff_comb')

    print("Retrieving reweight file and making branches")
    ReweightFile = ROOT.TFile(FileName,"UPDATE")
    Event_Fake_Factor = array('f',[0.])    
    
    ff_qcd_syst_up = array('f',[0.])
    ff_qcd_syst_down = array('f',[0.])
    ff_qcd_dm0_njet0_stat_up = array('f',[0.])
    ff_qcd_dm0_njet0_stat_down = array('f',[0.])
    ff_qcd_dm0_njet1_stat_up = array('f',[0.])
    ff_qcd_dm0_njet1_stat_down = array('f',[0.])
    ff_w_syst_up = array('f',[0.])
    ff_w_syst_down = array('f',[0.])
    ff_w_dm0_njet0_stat_up = array('f',[0.])
    ff_w_dm0_njet0_stat_down = array('f',[0.])
    ff_w_dm0_njet1_stat_up = array('f',[0.])
    ff_w_dm0_njet1_stat_down = array('f',[0.])
    ff_tt_syst_up = array('f',[0.])
    ff_tt_syst_down = array('f',[0.])
    ff_tt_dm0_njet0_stat_up = array('f',[0.])
    ff_tt_dm0_njet0_stat_down = array('f',[0.])
    ff_tt_dm0_njet1_stat_up = array('f',[0.])
    ff_tt_dm0_njet1_stat_down = array('f',[0.])

    FakeFactorBranch = ReweightFile.mt_Selected.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')    
    ff_qcd_syst_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_syst_up',ff_qcd_syst_up,'ff_qcd_syst_up/F')
    ff_qcd_syst_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_syst_down',ff_qcd_syst_down,'ff_qcd_syst_down/F')
    ff_qcd_dm0_njet0_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_dm0_njet0_stat_up',ff_qcd_dm0_njet0_stat_up,'ff_qcd_dm0_njet0_stat_up/F')
    ff_qcd_dm0_njet0_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_dm0_njet0_stat_down',ff_qcd_dm0_njet0_stat_down,'ff_qcd_dm0_njet0_stat_down/F')
    ff_qcd_dm0_njet1_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_dm0_njet1_stat_up',ff_qcd_dm0_njet1_stat_up,'ff_qcd_dm0_njet1_stat_up/F')
    ff_qcd_dm0_njet1_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_dm0_njet1_stat_down',ff_qcd_dm0_njet1_stat_down,'ff_qcd_dm0_njet1_stat_down/F')

    ff_w_syst_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_syst_up',ff_w_syst_up,'ff_w_syst_up/F')
    ff_w_syst_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_syst_down',ff_w_syst_down,'ff_w_syst_down/F')
    ff_w_dm0_njet0_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_dm0_njet0_stat_up',ff_w_dm0_njet0_stat_up,'ff_w_dm0_njet0_stat_up/F')
    ff_w_dm0_njet0_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_dm0_njet0_stat_down',ff_w_dm0_njet0_stat_down,'ff_w_dm0_njet0_stat_down/F')
    ff_w_dm0_njet1_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_dm0_njet1_stat_up',ff_w_dm0_njet1_stat_up,'ff_w_dm0_njet1_stat_up/F')
    ff_w_dm0_njet1_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_dm0_njet1_stat_down',ff_w_dm0_njet1_stat_down,'ff_w_dm0_njet1_stat_down/F')

    ff_tt_syst_up_Branch = ReweightFile.mt_Selected.Branch('ff_tt_syst_up',ff_tt_syst_up,'ff_tt_syst_up/F')
    ff_tt_syst_down_Branch = ReweightFile.mt_Selected.Branch('ff_tt_syst_down',ff_tt_syst_down,'ff_tt_syst_down/F')
    ff_tt_dm0_njet0_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_tt_dm0_njet0_stat_up',ff_tt_dm0_njet0_stat_up,'ff_tt_dm0_njet0_stat_up/F')
    ff_tt_dm0_njet0_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_tt_dm0_njet0_stat_down',ff_tt_dm0_njet0_stat_down,'ff_tt_dm0_njet0_stat_down/F')
    ff_tt_dm0_njet1_stat_up_Branch = ReweightFile.mt_Selected.Branch('ff_tt_dm0_njet1_stat_up',ff_tt_dm0_njet1_stat_up,'ff_tt_dm0_njet1_stat_up/F')
    ff_tt_dm0_njet1_stat_down_Branch = ReweightFile.mt_Selected.Branch('ff_tt_dm0_njet1_stat_down',ff_tt_dm0_njet1_stat_down,'ff_w_dm0_njet1_stat_down/F')
    
    print("Looping...")
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

        #now we need to compute proper fractions now
        EventClassification = ClassifyEvent(ReweightFile.mt_Selected)
        Denom = ( QCDFracHisto.GetBinContent(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) + 
                  WFracHisto.GetBinContent(WFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) + 
                  TTFracHisto.GetBinContent(TTFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) )
        try:
            FracQCD = QCDFracHisto.GetBinContent(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom
            FracW = WFracHisto.GetBinContent(WFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom
            FracTT = TTFracHisto.GetBinContent(TTFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom
        except ZeroDivisionError:
            print("Denom zero!")
            print("Denom: "+str(Denom))
            print("QCD Content: "+str(QCDFracHisto.GetBinContent(QCDFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification)))
            print("W Content: "+str(WFracHisto.GetBinContent(WFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification))) 
            print("TT Content: "+str(TTFracHisto.GetBinContent(TTFracHisto.GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification)))
            print("mass: "+str((TauVector+MuVector).M()))
            print("Event classification: "+str(EventClassification))
            FracQCD = 0.0
            FracW = 0.0
            FracTT = 0.0

        m_vis = (MuVector + TauVector).M()
        TransverseMass = AddMTandPZeta.CalculateMT(MuVector,MissingMomentumVector)

        inputs = [TauVector.Pt(),
                  ReweightFile.mt_Selected.l2_decayMode,
                  ReweightFile.mt_Selected.njets,
                  m_vis,
                  TransverseMass,
                  ReweightFile.mt_Selected.iso_1,
                  FracQCD,
                  FracW,
                  FracTT]
        #print("FracQCD: "+str(FracQCD))
        #print("FracW: "+str(FracW))
        #print("FracTT: "+str(FracTT))

        if args.IsNegative:
            Modifier = -1.0
        else:
            Modifier = 1.0
        
        Event_Fake_Factor[0] = ff.value(len(inputs),array('d',inputs)) * Modifier
        ff_qcd_syst_up[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_syst_up') * Modifier
        ff_qcd_syst_down[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_syst_down') * Modifier
        ff_qcd_dm0_njet0_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_dm0_njet0_stat_up') * Modifier
        ff_qcd_dm0_njet0_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_dm0_njet0_stat_down') * Modifier
        ff_qcd_dm0_njet1_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_dm0_njet1_stat_up') * Modifier
        ff_qcd_dm0_njet1_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_qcd_dm0_njet1_stat_down') * Modifier
        ff_w_syst_up[0] = ff.value(len(inputs),array('d',inputs),'ff_w_syst_up') * Modifier 
        ff_w_syst_down[0] = ff.value(len(inputs),array('d',inputs),'ff_w_syst_down') * Modifier
        ff_w_dm0_njet0_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_w_dm0_njet0_stat_up') * Modifier
        ff_w_dm0_njet0_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_w_dm0_njet0_stat_down') * Modifier
        ff_w_dm0_njet1_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_w_dm0_njet1_stat_up') * Modifier
        ff_w_dm0_njet1_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_w_dm0_njet1_stat_down') * Modifier
        ff_tt_syst_up[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_syst_up') * Modifier
        ff_tt_syst_down[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_syst_down') * Modifier * Modifier
        ff_tt_dm0_njet0_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_dm0_njet0_stat_up') * Modifier
        ff_tt_dm0_njet0_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_dm0_njet0_stat_down') * Modifier
        ff_tt_dm0_njet1_stat_up[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_dm0_njet1_stat_up') * Modifier
        ff_tt_dm0_njet1_stat_down[0] = ff.value(len(inputs),array('d',inputs),'ff_tt_dm0_njet1_stat_down') * Modifier

        FakeFactorBranch.Fill()
        ff_qcd_syst_up_Branch.Fill()
        ff_qcd_syst_down_Branch.Fill()
        ff_qcd_dm0_njet0_stat_up_Branch.Fill()
        ff_qcd_dm0_njet0_stat_down_Branch.Fill()
        ff_qcd_dm0_njet1_stat_up_Branch.Fill()
        ff_qcd_dm0_njet1_stat_down_Branch.Fill()
        ff_w_syst_up_Branch.Fill()
        ff_w_syst_down_Branch.Fill()
        ff_w_dm0_njet0_stat_up_Branch.Fill()
        ff_w_dm0_njet0_stat_down_Branch.Fill()
        ff_w_dm0_njet1_stat_up_Branch.Fill()
        ff_w_dm0_njet1_stat_down_Branch.Fill()
        ff_tt_syst_up_Branch.Fill()
        ff_tt_syst_down_Branch.Fill()
        ff_tt_dm0_njet0_stat_up_Branch.Fill()
        ff_tt_dm0_njet0_stat_down_Branch.Fill()
        ff_tt_dm0_njet1_stat_up_Branch.Fill()
        ff_tt_dm0_njet1_stat_down_Branch.Fill()
            
    ff.Delete()
    ff_file.Close()

    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate and attach fake factor weighting branches.")
    parser.add_argument('--year',choices=["2016","2017","2018"],help="Running year",required=True)
    parser.add_argument('--files',nargs="+",help="Files to add the factors to",required=True)
    parser.add_argument('--IsNegative',help="Make the fake factors negative to support subtraction of MC",action="store_true")
    args = parser.parse_args()

    MakeFractions(args)

    for filename in args.files:
        AddFakeFactorWeightings(filename,args)
