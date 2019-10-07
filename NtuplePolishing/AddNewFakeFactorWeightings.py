import ROOT
from tqdm import tqdm
from array import array
import argparse
import FakeFactorConfiguration as cfg
import AddMTandPZeta

#new way of accessing 
def get_raw_FF(pt,fct):
    ff=1.0
    ff=fct.Eval(pt)    
    #if(pt>80):
    #    ff=fct.Eval(80)
    return ff

def get_mvis_closure(mvis,fct):
    corr = 1.0
    corr = fct.Eval(mvis)
    if(mvis>350):
        corr=fct.Eval(350)
    #if (mvis<50):
    #    corr=fct.Eval(50)
    return corr

def get_mt_closure(mt, fct):
    corr=1.0
    corr=fct.Eval(mt)
    #if (mt>120):
    #    corr=fct.Eval(120)
    return corr

def get_ff(pt, mt, mvis, njets, frac_tt, frac_qcd, frac_w, fct_raw_qcd_0, fct_raw_qcd_1, fct_raw_w_0, fct_raw_w_1, fct_raw_tt, fct_mvisclosure_qcd, fct_mvisclosure_w,fct_mvisclosure_tt, fct_mtcorrection_w, fct_OSSScorrection_qcd):
    ff_qcd = 1.0
    ff_w = 0
    ff_tt = 1.0
    
    #Raw ff
    if(njets==0):
        ff_qcd=get_raw_FF(pt,fct_raw_qcd_0)
        ff_w=get_raw_FF(pt,fct_raw_w_0)
    else:
        ff_qcd=get_raw_FF(pt,fct_raw_qcd_0)
        ff_w=get_raw_FF(pt,fct_raw_w_0)
    ff_tt=get_raw_FF(pt,fct_raw_tt)

    #mvis closure
    ff_qcd = ff_qcd*get_mvis_closure(mvis,fct_mvisclosure_qcd)
    ff_w = ff_w*get_mvis_closure(mvis,fct_mvisclosure_w)
    ff_tt = ff_tt*get_mvis_closure(mvis,fct_mvisclosure_tt)

    #MT and OSSS corrections
    ff_w = ff_w*get_mt_closure(mt,fct_mtcorrection_w)
    ff_qcd = ff_qcd*get_mvis_closure(mvis,fct_OSSScorrection_qcd)
    
    ff_cmb = frac_tt*ff_tt + frac_qcd*ff_qcd + frac_w*ff_w
    return ff_cmb

#Let's try splitting these up by triggers.
# see if that helps us deal with the the problem in the 2017 cross trigger?
WFracHisto = ROOT.TH2F("WFrac","WFrac",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto = ROOT.TH2F("QCDFrac","QCDFrac",20,0.0,500.0,7,1.0,8.0)
TTFracHisto = ROOT.TH2F("TTFrac","TTFrac",20,0.0,500.0,7,1.0,8.0)
dataFracHisto = ROOT.TH2F("DataFrac","DataFrac",20,0.0,500.0,7,1.0,8.0)
RealFracHisto = ROOT.TH2F("RealFrac","RealFrac",20,0.0,500.0,7,1.0,8.0)

#2016 triggers
WFracHisto_Trigger22 = ROOT.TH2F("WFrac_Trigger22","WFrac_Trigger22",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto_Trigger22 = ROOT.TH2F("QCDFrac_Trigger22","QCDFrac_Trigger22",20,0.0,500.0,7,1.0,8.0)
TTFracHisto_Trigger22 = ROOT.TH2F("TTFrac_Trigger22","TTFrac_Trigger22",20,0.0,500.0,7,1.0,8.0)
dataFracHisto_Trigger22 = ROOT.TH2F("DataFrac_Trigger22","DataFrac_Trigger22",20,0.0,500.0,7,1.0,8.0)
RealFracHisto_Trigger22 = ROOT.TH2F("RealFrac_Trigger22","RealFrac_Trigger22",20,0.0,500.0,7,1.0,8.0)

WFracHisto_Trigger1920 = ROOT.TH2F("WFrac_Trigger1920","WFrac_Trigger1920",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto_Trigger1920 = ROOT.TH2F("QCDFrac_Trigger1920","QCDFrac_Trigger1920",20,0.0,500.0,7,1.0,8.0)
TTFracHisto_Trigger1920 = ROOT.TH2F("TTFrac_Trigger1920","TTFrac_Trigger1920",20,0.0,500.0,7,1.0,8.0)
dataFracHisto_Trigger1920 = ROOT.TH2F("DataFrac_Trigger1920","DataFrac_Trigger1920",20,0.0,500.0,7,1.0,8.0)
RealFracHisto_Trigger1920 = ROOT.TH2F("RealFrac_Trigger1920","RealFrac_Trigger1920",20,0.0,500.0,7,1.0,8.0)

#2017 & 2018 triggers
WFracHisto_Trigger24 = ROOT.TH2F("WFrac_Trigger24","WFrac_Trigger24",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto_Trigger24 = ROOT.TH2F("QCDFrac_Trigger24","QCDFrac_Trigger24",20,0.0,500.0,7,1.0,8.0)
TTFracHisto_Trigger24 = ROOT.TH2F("TTFrac_Trigger24","TTFrac_Trigger24",20,0.0,500.0,7,1.0,8.0)
dataFracHisto_Trigger24 = ROOT.TH2F("DataFrac_Trigger24","DataFrac_Trigger24",20,0.0,500.0,7,1.0,8.0)
RealFracHisto_Trigger24 = ROOT.TH2F("RealFrac_Trigger24","RealFrac_Trigger24",20,0.0,500.0,7,1.0,8.0)

WFracHisto_Trigger27 = ROOT.TH2F("WFrac_Trigger27","WFrac_Trigger27",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto_Trigger27 = ROOT.TH2F("QCDFrac_Trigger27","QCDFrac_Trigger27",20,0.0,500.0,7,1.0,8.0)
TTFracHisto_Trigger27 = ROOT.TH2F("TTFrac_Trigger27","TTFrac_Trigger27",20,0.0,500.0,7,1.0,8.0)
dataFracHisto_Trigger27 = ROOT.TH2F("DataFrac_Trigger27","DataFrac_Trigger27",20,0.0,500.0,7,1.0,8.0)
RealFracHisto_Trigger27 = ROOT.TH2F("RealFrac_Trigger27","RealFrac_Trigger27",20,0.0,500.0,7,1.0,8.0)

WFracHisto_Trigger2027 = ROOT.TH2F("WFrac_Trigger2027","WFrac_Trigger2027",20,0.0,500.0,7,1.0,8.0)
QCDFracHisto_Trigger2027 = ROOT.TH2F("QCDFrac_Trigger2027","QCDFrac_Trigger2027",20,0.0,500.0,7,1.0,8.0)
TTFracHisto_Trigger2027 = ROOT.TH2F("TTFrac_Trigger2027","TTFrac_Trigger2027",20,0.0,500.0,7,1.0,8.0)
dataFracHisto_Trigger2027 = ROOT.TH2F("DataFrac_Trigger2027","DataFrac_Trigger2027",20,0.0,500.0,7,1.0,8.0)
RealFracHisto_Trigger2027 = ROOT.TH2F("RealFrac_Trigger2027","RealFrac_Trigger2027",20,0.0,500.0,7,1.0,8.0)

WHistos = {
    "Inclusive": WFracHisto,
    "Trigger22": WFracHisto_Trigger22,
    "Trigger1920": WFracHisto_Trigger1920,
    "Trigger24": WFracHisto_Trigger24,
    "Trigger27": WFracHisto_Trigger27,
    "Trigger2027": WFracHisto_Trigger2027
    }

QCDHistos = {
    "Inclusive": QCDFracHisto,
    "Trigger22": QCDFracHisto_Trigger22,
    "Trigger1920": QCDFracHisto_Trigger1920,
    "Trigger24": QCDFracHisto_Trigger24,
    "Trigger27": QCDFracHisto_Trigger27,
    "Trigger2027": QCDFracHisto_Trigger2027
    }

TTHistos = {
    "Inclusive": TTFracHisto,
    "Trigger22": TTFracHisto_Trigger22,
    "Trigger1920": TTFracHisto_Trigger1920,
    "Trigger24": TTFracHisto_Trigger24,
    "Trigger27": TTFracHisto_Trigger27,
    "Trigger2027": TTFracHisto_Trigger2027
    }

dataHistos = {
    "Inclusive": dataFracHisto,
    "Trigger22": dataFracHisto_Trigger22,
    "Trigger1920": dataFracHisto_Trigger1920,
    "Trigger24": dataFracHisto_Trigger24,
    "Trigger27": dataFracHisto_Trigger27,
    "Trigger2027": dataFracHisto_Trigger2027
    }

RealHistos = {
    "Inclusive": RealFracHisto,
    "Trigger22": RealFracHisto_Trigger22,
    "Trigger1920": RealFracHisto_Trigger1920,
    "Trigger24": RealFracHisto_Trigger24,
    "Trigger27": RealFracHisto_Trigger27,
    "Trigger2027": RealFracHisto_Trigger2027
    }

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
        EmbeddedFiles = cfg.Embedded_Files_2017
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
    elif args.year == "2018":
        FilePath = cfg.ntuple_path_2018
        DataFiles = cfg.Data_Files_2018
        WFiles = cfg.W_Files_2018
        TTFiles = cfg.TT_Files_2018
        EmbeddedFiles = cfg.Embedded_Files_2017
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
    DataNtuple = MakeNtuples(FilePath,DataFiles)
    DataNtuple.SetNameTitle("Data","Data")
    WNtuple = MakeNtuples(FilePath,WFiles)
    WNtuple.SetNameTitle("W","W")
    TTNtuple = MakeNtuples(FilePath,TTFiles)
    TTNtuple.SetNameTitle("TT","TT")

    if args.year=="2016":
        return DataNtuple,WNtuple,TTNtuple
    else:
        return DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple

def ProcessNtuple(args,Ntuple,HistogramFamily,GenMatches,Sample=""):
    for i in tqdm(range(Ntuple.GetEntries())):
        Ntuple.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(Ntuple.pt_1,Ntuple.eta_1,Ntuple.phi_1,Ntuple.m_1)
        TauVector.SetPtEtaPhiM(Ntuple.pt_2,Ntuple.eta_2,Ntuple.phi_2,Ntuple.m_2)
        if Ntuple.gen_match_2 in GenMatches:
            HistogramFamily[ClassifyTrigger(args,Ntuple,Sample)].Fill((TauVector+MuVector).M(),ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
            HistogramFamily["Inclusive"].Fill((TauVector+MuVector).M(),ClassifyEvent(Ntuple),Ntuple.FinalWeighting)

def ClassifyTrigger(args,TheEvent,Sample=""):
    if args.year == "2017" or args.year == "2018":
        if TheEvent.Trigger24:
            return "Trigger24"
        elif TheEvent.Trigger27:
            return "Trigger27"
        elif TheEvent.Trigger2027:
            return "Trigger2027"    
    elif args.year == "2016":        
        if TheEvent.Trigger22:
            return "Trigger22"
        elif TheEvent.Trigger1920:
            return "Trigger1920"

    print "Failed to find a proper trigger! returning a default!"
    if args.year == "2016":
        return "Trigger22"
    if args.year == "2017":
        return "Trigger24"
    if args.year == "2018":
        return "Trigger24"
    
         
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
    if args.year == "2016":
        DataNtuple,WNtuple,TTNtuple=MakeAllNtuples(args)
    else:
        DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple=MakeAllNtuples(args)
    #process the data ntuple
    for i in tqdm(range(DataNtuple.GetEntries())):
        DataNtuple.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(DataNtuple.pt_1,DataNtuple.eta_1,DataNtuple.phi_1,DataNtuple.m_1)
        TauVector.SetPtEtaPhiM(DataNtuple.pt_2,DataNtuple.eta_2,DataNtuple.phi_2,DataNtuple.m_2)
        QCDHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))
        QCDHistos["Inclusive"].Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))
        dataHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))        
        dataHistos["Inclusive"].Fill((TauVector+MuVector).M(),ClassifyEvent(DataNtuple))
    #fill in the remaining ones
    #ProcessNtuple(WNtuple,WFracHisto,RealFracHisto)
    #ProcessNtuple(TTNtuple,TTFracHisto,RealFracHisto)
    ProcessNtuple(args,WNtuple,WHistos,[6])
    ProcessNtuple(args,WNtuple,RealHistos,[1,2,3,4,5])
    ProcessNtuple(args,TTNtuple,TTHistos,[6])
    ProcessNtuple(args,TTNtuple,RealHistos,[1,2,3,4,5])
    if args.year!="2016" and not args.UseMC:
        ProcessNtuple(args,EmbeddedNtuple,RealHistos,[6],"Embedded")

    #Perform the subtractions
    for Trigger in QCDHistos:
        QCDHistos[Trigger].Add(RealHistos[Trigger],-1)
        QCDHistos[Trigger].Add(TTHistos[Trigger],-1)
        QCDHistos[Trigger].Add(WHistos[Trigger],-1)
    FractionFile = ROOT.TFile("Weightings/FFFractionFile"+args.year+".root","RECREATE")
    for Histo in dataHistos:
        WHistos[Histo].Write()
        QCDHistos[Histo].Write()
        TTHistos[Histo].Write()
        dataHistos[Histo].Write()
        RealHistos[Histo].Write()
    

def AddFakeFactorWeightings(FileName,args):
    print("Adding deep tau fake factors to "+FileName)
    RawFF = ROOT.TFile("Weightings/DeepFFs/uncorrected_fakefactors_mt.root")
    ff_qcd_0jet = RawFF.Get("rawFF_mt_qcd_0jet")
    ff_qcd_1jet = RawFF.Get("rawFF_mt_qcd_1jet")
    ff_w_0jet = RawFF.Get("rawFF_mt_w_0jet")
    ff_w_1jet = RawFF.Get("rawFF_mt_w_1jet")
    ff_tt_0jet = RawFF.Get("mc_rawFF_mt_tt")
    
    fmvisclosure = ROOT.TFile("Weightings/DeepFFs/FF_corrections_1.root")
    mvisclosure_qcd = fmvisclosure.Get("closure_mvis_mt_qcd")
    mvisclosure_w = fmvisclosure.Get("closure_mvis_mt_w")
    mvisclosure_tt = fmvisclosure.Get("closure_mvis_mt_ttmc")
    
    fossclosure = ROOT.TFile("Weightings/DeepFFs/FF_QCDcorrectionOSSS.root")
    osssclosure_qcd = fossclosure.Get("closure_mvis_mt_qcd")
    mtclosure_w = fossclosure.Get("closure_mt_mt_w")

    print("Retrieving reweight file and making branches")
    ReweightFile = ROOT.TFile(FileName,"UPDATE")
    Event_Fake_Factor = array('f',[0.])    

    FakeFactorBranch = ReweightFile.mt_Selected.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')    

    Sample = ""
    if FileName.find("Data") > 0:
        Sample = "Data"
    elif FileName.find("Embedded") > 0:
        Sample = "Embedded"

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
        TriggerClassification = ClassifyTrigger(args,ReweightFile.mt_Selected,Sample)        


        Denom = ( QCDHistos[TriggerClassification].GetBinContent(QCDHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) + 
                  WHistos[TriggerClassification].GetBinContent(WHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) + 
                  TTHistos[TriggerClassification].GetBinContent(TTHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) )
        try:
            FracQCD = QCDHistos[TriggerClassification].GetBinContent(QCDHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom
            FracW = WHistos[TriggerClassification].GetBinContent(WHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom
            FracTT = TTHistos[TriggerClassification].GetBinContent(TTHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification) / Denom            
        except ZeroDivisionError:
            print("Denom zero!")
            print("Denom: "+str(Denom))
            print("QCD Content: "+str(QCDHistos[TriggerClassification].GetBinContent(QCDHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification)))
            print("W Content: "+str(WHistos[TriggerClassification].GetBinContent(WHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification))) 
            print("TT Content: "+str(TTHistos[TriggerClassification].GetBinContent(TTHistos[TriggerClassification].GetXaxis().FindBin((TauVector+MuVector).M()),EventClassification)))
            print("mass: "+str((TauVector+MuVector).M()))
            print("Event classification: "+str(EventClassification))
            FracQCD = 0.0
            FracW = 0.0
            FracTT = 0.0        

        m_vis = (MuVector + TauVector).M()
        TransverseMass = AddMTandPZeta.CalculateMT(MuVector,MissingMomentumVector)
        
        if args.IsNegative:
            Modifier = -1.0
        else:
            Modifier = 1.0

        Event_Fake_Factor[0] = get_ff(TauVector.Pt(),
                                      TransverseMass,
                                      m_vis,
                                      ReweightFile.mt_Selected.njets,
                                      FracTT,
                                      FracQCD,
                                      FracW,
                                      ff_qcd_0jet,
                                      ff_qcd_1jet,
                                      ff_w_0jet,
                                      ff_w_1jet,
                                      ff_tt_0jet,
                                      mvisclosure_qcd,
                                      mvisclosure_w,
                                      mvisclosure_tt,
                                      mtclosure_w,
                                      osssclosure_qcd) * Modifier        

        FakeFactorBranch.Fill()
    ReweightFile.cd()
    ReweightFile.mt_Selected.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate and attach fake factor weighting branches.")
    parser.add_argument('--year',choices=["2016","2017","2018"],help="Running year",required=True)
    parser.add_argument('--files',nargs="+",help="Files to add the factors to",required=True)
    parser.add_argument('--IsNegative',help="Make the fake factors negative to support subtraction of MC",action="store_true")
    parser.add_argument('--DontRecomputeFractions',help="Read the fake factor fraction histos from file isntead of computing them",action="store_true")
    parser.add_argument('--UseMC',help="Perform all calculations ignoring embedded distributions if available",action="store_true")
    args = parser.parse_args()

    if(not args.DontRecomputeFractions):
        MakeFractions(args)
    else:
        FractionFile = ROOT.TFile("Weightings/FFFractionFile"+args.year+".root")
        for Histo in dataHistos:
            WHistos[Histo] = FractionFile.Get(WHistos[Histo].GetName())
            QCDHistos[Histo] = FractionFile.Get(QCDHistos[Histo].GetName())
            TTHistos[Histo] = FractionFile.Get(TTHistos[Histo].GetName())
            dataHistos[Histo] = FractionFile.Get(dataHistos[Histo].GetName())
            RealHistos[Histo] = FractionFile.Get(RealHistos[Histo].GetName())

    for filename in args.files:
        AddFakeFactorWeightings(filename,args)
