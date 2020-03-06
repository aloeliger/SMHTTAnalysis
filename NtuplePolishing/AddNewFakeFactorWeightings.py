import ROOT
from tqdm import tqdm
from array import array
import argparse
import FakeFactorConfiguration as cfg
#import AddMTandPZeta
import ComputeFF2018.FFcode.ApplyFF as ApplyFF

#m_svBinning = array('d',[0.0,50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0,350.0])
#m_svBins = [0.0,50.0,70.0,90.0,110.0,130.0,150.0,290.0,350.0]
m_svBins = [0.0,50.0,70.0,90.0,110.0,130.0,150.0,170.0,210.0,250.0,290.0,350.0]
nBins = len(m_svBins)-1
theBinning = array('d',m_svBins)

#Let's try splitting these up by triggers.
# see if that helps us deal with the the problem in the 2017 cross trigger?
WFracHisto = ROOT.TH2F("WFrac","WFrac",nBins,theBinning,7,1.0,8.0)
QCDFracHisto = ROOT.TH2F("QCDFrac","QCDFrac",nBins,theBinning,7,1.0,8.0)
TTFracHisto = ROOT.TH2F("TTFrac","TTFrac",nBins,theBinning,7,1.0,8.0)
dataFracHisto = ROOT.TH2F("DataFrac","DataFrac",nBins,theBinning,7,1.0,8.0)
RealFracHisto = ROOT.TH2F("RealFrac","RealFrac",nBins,theBinning,7,1.0,8.0)

#2016 triggers
WFracHisto_Trigger22 = ROOT.TH2F("WFrac_Trigger22","WFrac_Trigger22",nBins,theBinning,7,1.0,8.0)
QCDFracHisto_Trigger22 = ROOT.TH2F("QCDFrac_Trigger22","QCDFrac_Trigger22",nBins,theBinning,7,1.0,8.0)
TTFracHisto_Trigger22 = ROOT.TH2F("TTFrac_Trigger22","TTFrac_Trigger22",nBins,theBinning,7,1.0,8.0)
dataFracHisto_Trigger22 = ROOT.TH2F("DataFrac_Trigger22","DataFrac_Trigger22",nBins,theBinning,7,1.0,8.0)
RealFracHisto_Trigger22 = ROOT.TH2F("RealFrac_Trigger22","RealFrac_Trigger22",nBins,theBinning,7,1.0,8.0)

WFracHisto_Trigger1920 = ROOT.TH2F("WFrac_Trigger1920","WFrac_Trigger1920",nBins,theBinning,7,1.0,8.0)
QCDFracHisto_Trigger1920 = ROOT.TH2F("QCDFrac_Trigger1920","QCDFrac_Trigger1920",nBins,theBinning,7,1.0,8.0)
TTFracHisto_Trigger1920 = ROOT.TH2F("TTFrac_Trigger1920","TTFrac_Trigger1920",nBins,theBinning,7,1.0,8.0)
dataFracHisto_Trigger1920 = ROOT.TH2F("DataFrac_Trigger1920","DataFrac_Trigger1920",nBins,theBinning,7,1.0,8.0)
RealFracHisto_Trigger1920 = ROOT.TH2F("RealFrac_Trigger1920","RealFrac_Trigger1920",nBins,theBinning,7,1.0,8.0)

#2017 & 2018 triggers
WFracHisto_Trigger24 = ROOT.TH2F("WFrac_Trigger24","WFrac_Trigger24",nBins,theBinning,7,1.0,8.0)
QCDFracHisto_Trigger24 = ROOT.TH2F("QCDFrac_Trigger24","QCDFrac_Trigger24",nBins,theBinning,7,1.0,8.0)
TTFracHisto_Trigger24 = ROOT.TH2F("TTFrac_Trigger24","TTFrac_Trigger24",nBins,theBinning,7,1.0,8.0)
dataFracHisto_Trigger24 = ROOT.TH2F("DataFrac_Trigger24","DataFrac_Trigger24",nBins,theBinning,7,1.0,8.0)
RealFracHisto_Trigger24 = ROOT.TH2F("RealFrac_Trigger24","RealFrac_Trigger24",nBins,theBinning,7,1.0,8.0)

WFracHisto_Trigger27 = ROOT.TH2F("WFrac_Trigger27","WFrac_Trigger27",nBins,theBinning,7,1.0,8.0)
QCDFracHisto_Trigger27 = ROOT.TH2F("QCDFrac_Trigger27","QCDFrac_Trigger27",nBins,theBinning,7,1.0,8.0)
TTFracHisto_Trigger27 = ROOT.TH2F("TTFrac_Trigger27","TTFrac_Trigger27",nBins,theBinning,7,1.0,8.0)
dataFracHisto_Trigger27 = ROOT.TH2F("DataFrac_Trigger27","DataFrac_Trigger27",nBins,theBinning,7,1.0,8.0)
RealFracHisto_Trigger27 = ROOT.TH2F("RealFrac_Trigger27","RealFrac_Trigger27",nBins,theBinning,7,1.0,8.0)

WFracHisto_Trigger2027 = ROOT.TH2F("WFrac_Trigger2027","WFrac_Trigger2027",nBins,theBinning,7,1.0,8.0)
QCDFracHisto_Trigger2027 = ROOT.TH2F("QCDFrac_Trigger2027","QCDFrac_Trigger2027",nBins,theBinning,7,1.0,8.0)
TTFracHisto_Trigger2027 = ROOT.TH2F("TTFrac_Trigger2027","TTFrac_Trigger2027",nBins,theBinning,7,1.0,8.0)
dataFracHisto_Trigger2027 = ROOT.TH2F("DataFrac_Trigger2027","DataFrac_Trigger2027",nBins,theBinning,7,1.0,8.0)
RealFracHisto_Trigger2027 = ROOT.TH2F("RealFrac_Trigger2027","RealFrac_Trigger2027",nBins,theBinning,7,1.0,8.0)

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
        #print(path+ProcessFiles[Process])
        Chain.Add(path+ProcessFiles[Process])
    return Chain

def MakeAllNtuples(args):
    if args.year == "2016":
        FilePath = cfg.ntuple_path_2016
        DataFiles = cfg.Data_Files_2016
        WFiles = cfg.W_Files_2016
        TTFiles = cfg.TT_Files_2016
        EmbeddedFiles = cfg.Embedded_Files_2016
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
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
        
    return DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple

def ProcessNtuple(args,Ntuple,HistogramFamily,GenMatches,Sample=""):
    for i in tqdm(range(Ntuple.GetEntries())):
        Ntuple.GetEntry(i)        
        #print(Ntuple.gen_match_2)
        #print(GenMatches)
        #print(Ntuple.gen_match_2 in GenMatches)
        if Ntuple.gen_match_2 in GenMatches:
            #print("Match!")
            HistogramFamily[ClassifyTrigger(args,Ntuple,Sample)].Fill(Ntuple.m_sv,ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
            HistogramFamily["Inclusive"].Fill(Ntuple.m_sv,ClassifyEvent(Ntuple),Ntuple.FinalWeighting)

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

    MT = TheEvent.MT
    HiggsPT = (MuVector+TauVector+METVector).Pt()

    #zero jet
    if(TauVector.Pt() >= 30 and MT < 50.0 and TheEvent.njets == 0):
        if(MuVector.DeltaR(TauVector) > 3.0):
            EventCategory = 1
        elif(MuVector.DeltaR(TauVector) < 3.0):
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
    DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple = MakeAllNtuples(args)    
    #fill in W and tt histograms
    #ProcessNtuple(WNtuple,WFracHisto,RealFracHisto)
    #ProcessNtuple(TTNtuple,TTFracHisto,RealFracHisto)
    ProcessNtuple(args,WNtuple,RealHistos,[1,2,3,4,5])
    ProcessNtuple(args,WNtuple,WHistos,[6])  
    ProcessNtuple(args,TTNtuple,RealHistos,[1,2,3,4,5])
    ProcessNtuple(args,TTNtuple,TTHistos,[6])    
    if not args.UseMC:
        ProcessNtuple(args,EmbeddedNtuple,RealHistos,[5],"Embedded")
    #process the data ntuple
    for i in tqdm(range(DataNtuple.GetEntries())):
        DataNtuple.GetEntry(i)        
        QCDHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))
        QCDHistos["Inclusive"].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))
        dataHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))        
        dataHistos["Inclusive"].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))

    #Perform the subtractions
    for Trigger in QCDHistos:
        QCDHistos[Trigger].Add(RealHistos[Trigger],-1)
        QCDHistos[Trigger].Add(TTHistos[Trigger],-1)
        QCDHistos[Trigger].Add(WHistos[Trigger],-1)

    print("Finalizing Histograms")
    FinalizeFractionHistos(QCDHistos,WHistos,TTHistos)

    print("Writing files...")
    FractionFile = ROOT.TFile("Weightings/FFFractionFile"+args.year+".root","RECREATE")
    for Histo in dataHistos:        
        WHistos[Histo].Write()
        QCDHistos[Histo].Write()
        TTHistos[Histo].Write()
        dataHistos[Histo].Write()
        RealHistos[Histo].Write()
    FractionFile.Close()   
    print("Done Writing files...")

#Okay, let's make a change for our benefit reading this,
#let's change it so that the fractions of this are calculated in place in the 
#histograms that should represent them.
def FinalizeFractionHistos(QCDHistoFamily,WHistoFamily,TTHistoFamily):
    # let's pick out a histogram
    for Trigger in QCDHistoFamily:
        QCDHisto = QCDHistoFamily[Trigger].Clone()
        WHisto = WHistoFamily[Trigger].Clone()
        TTHisto = TTHistoFamily[Trigger].Clone()
        QCDHisto.Reset()
        WHisto.Reset()
        TTHisto.Reset()
        #print('\n'+Trigger)
        #loop over X
        for j in range(1,QCDHisto.GetYaxis().GetNbins()+1):
            for i in range(1,QCDHisto.GetXaxis().GetNbins()+1):            
                QCDContribution = QCDHistoFamily[Trigger].GetBinContent(i,j)
                if QCDContribution < 0:
                    QCDContribution = 0
                #print("i,j: "+str(i)+","+str(j))
                #print("QCD: "+str(QCDContribution))
                #print("W: "+str(WHistoFamily[Trigger].GetBinContent(i,j)))
                #print("TT: "+str(TTHistoFamily[Trigger].GetBinContent(i,j)))
                Denom = QCDContribution + WHistoFamily[Trigger].GetBinContent(i,j) + TTHistoFamily[Trigger].GetBinContent(i,j)
                try:
                    FracQCD = QCDContribution / Denom
                    FracW = WHistoFamily[Trigger].GetBinContent(i,j) / Denom
                    FracTT = TTHistoFamily[Trigger].GetBinContent(i,j) / Denom
                except ZeroDivisionError:
                    #print("Denom Zero!")
                    #print("Trigger: "+Trigger+" "+str(i)+","+str(j))
                    #print("QCD: "+str(QCDHistoFamily[Trigger].GetBinContent(i,j)))
                    #print("W: "+str(WHistoFamily[Trigger].GetBinContent(i,j)))
                    #print("TT: "+str(TTHistoFamily[Trigger].GetBinContent(i,j)))
                    #let's just do some quick estimating
                    if i <= 2:
                        FracQCD = 1.0
                        FracW = 0
                        FracTT = 0
                    else:
                        FracQCD = 0.0
                        FracW = 1.0
                        FracTT = 0.0                    
                #print("FracQCD: "+str(FracQCD))
                #print("FracW: "+str(FracW))
                #print("FracTT: "+str(FracTT))
                QCDHisto.SetBinContent(i,j, FracQCD)
                WHisto.SetBinContent(i,j, FracW)
                TTHisto.SetBinContent(i,j, FracTT)
        QCDHistoFamily[Trigger] = QCDHisto
        WHistoFamily[Trigger] = WHisto
        TTHistoFamily[Trigger] = TTHisto

def AddFakeFactorWeightings(FileName,args):
    print("Adding deep tau fake factors to "+FileName)    
    if args.year == '2016':
        theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2016/","mt")
    elif args.year == '2017':
        theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2017/","mt")
    elif args.year == '2018':
        theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2018/","mt")        
        #theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2018-Cecile/","et")                

    print("Retrieving reweight file and making branches")
    ReweightFile = ROOT.TFile(FileName,"UPDATE")
    Event_Fake_Factor = array('f',[0.])    

    ff_qcd_0jet_unc1_up = array('f',[0.])
    ff_qcd_0jet_unc1_down = array('f',[0.])
    ff_qcd_0jet_unc2_up = array('f',[0.])
    ff_qcd_0jet_unc2_down = array('f',[0.])
    ff_qcd_1jet_unc1_up = array('f',[0.])
    ff_qcd_1jet_unc1_down = array('f',[0.])
    ff_qcd_1jet_unc2_up = array('f',[0.])
    ff_qcd_1jet_unc2_down = array('f',[0.])
    ff_qcd_2jet_unc1_up = array('f',[0.])
    ff_qcd_2jet_unc1_down = array('f',[0.])
    ff_qcd_2jet_unc2_up = array('f',[0.])
    ff_qcd_2jet_unc2_down = array('f',[0.])

    ff_w_0jet_unc1_up = array('f',[0.])
    ff_w_0jet_unc1_down = array('f',[0.])
    ff_w_0jet_unc2_up = array('f',[0.])
    ff_w_0jet_unc2_down = array('f',[0.])
    ff_w_1jet_unc1_up = array('f',[0.])
    ff_w_1jet_unc1_down = array('f',[0.])
    ff_w_1jet_unc2_up = array('f',[0.])
    ff_w_1jet_unc2_down = array('f',[0.])
    ff_w_2jet_unc1_up = array('f',[0.])
    ff_w_2jet_unc1_down = array('f',[0.])
    ff_w_2jet_unc2_up = array('f',[0.])
    ff_w_2jet_unc2_down = array('f',[0.])
    
    ff_tt_0jet_unc1_up = array('f',[0.])
    ff_tt_0jet_unc1_down = array('f',[0.])
    ff_tt_0jet_unc2_up = array('f',[0.])
    ff_tt_0jet_unc2_down = array('f',[0.])

    """
    mvisclosure_qcd_0jet_up = array('f',[0.])
    mvisclosure_qcd_0jet_down = array('f',[0.])    
    mvisclosure_w_0jet_up = array('f',[0.])
    mvisclosure_w_0jet_down = array('f',[0.])
    mvisclosure_qcd_1jet_up = array('f',[0.])
    mvisclosure_qcd_1jet_down = array('f',[0.])    
    mvisclosure_w_1jet_up = array('f',[0.])
    mvisclosure_w_1jet_down = array('f',[0.])
    mvisclosure_qcd_2jet_up = array('f',[0.])
    mvisclosure_qcd_2jet_down = array('f',[0.])    
    mvisclosure_w_2jet_up = array('f',[0.])
    mvisclosure_w_2jet_down = array('f',[0.])
    mvisclosure_tt_up = array('f',[0.])
    mvisclosure_tt_down = array('f',[0.])    
    """
    lptclosure_xtrg_qcd_0jet_up = array('f',[0.])
    lptclosure_xtrg_qcd_0jet_down = array('f',[0.])
    lptclosure_xtrg_w_0jet_up = array('f',[0.])
    lptclosure_xtrg_w_0jet_down = array('f',[0.])
    lptclosure_xtrg_tt_up = array('f',[0.])
    lptclosure_xtrg_tt_down = array('f',[0.])

    lptclosure_qcd_0jet_up = array('f',[0.])
    lptclosure_qcd_0jet_down = array('f',[0.])
    lptclosure_w_0jet_up = array('f',[0.])
    lptclosure_w_0jet_down = array('f',[0.])
    lptclosure_tt_up = array('f',[0.])
    lptclosure_tt_down = array('f',[0.])

    mtclosure_w_unc1_up = array('f',[0.])
    mtclosure_w_unc1_down = array('f',[0.])
    mtclosure_w_unc2_up = array('f',[0.])
    mtclosure_w_unc2_down = array('f',[0.])

    osssclosure_qcd_unc1_up = array('f',[0.])
    osssclosure_qcd_unc1_down = array('f',[0.])

    FakeFactorBranch = ReweightFile.mt_Selected.Branch('Event_Fake_Factor',Event_Fake_Factor,'Event_Fake_Factor/F')    
    
    ff_qcd_0jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_0jet_unc1_up',ff_qcd_0jet_unc1_up,'ff_qcd_0jet_unc1_up/F')
    ff_qcd_0jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_0jet_unc1_down',ff_qcd_0jet_unc1_down,'ff_qcd_0jet_unc1_down/F')
    ff_qcd_0jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_0jet_unc2_up',ff_qcd_0jet_unc2_up,'ff_qcd_0jet_unc2_up/F')
    ff_qcd_0jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_0jet_unc2_down',ff_qcd_0jet_unc2_down,'ff_qcd_0jet_unc2_down/F')
    ff_qcd_1jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_1jet_unc1_up',ff_qcd_1jet_unc1_up,'ff_qcd_1jet_unc1_up/F')
    ff_qcd_1jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_1jet_unc1_down',ff_qcd_1jet_unc1_down,'ff_qcd_1jet_unc1_down/F')
    ff_qcd_1jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_1jet_unc2_up',ff_qcd_1jet_unc2_up,'ff_qcd_1jet_unc2_up/F')
    ff_qcd_1jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_1jet_unc2_down',ff_qcd_1jet_unc2_down,'ff_qcd_1jet_unc2_down/F')
    ff_qcd_2jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_2jet_unc1_up',ff_qcd_2jet_unc1_up,'ff_qcd_2jet_unc1_up/F')
    ff_qcd_2jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_2jet_unc1_down',ff_qcd_2jet_unc1_down,'ff_qcd_2jet_unc1_down/F')
    ff_qcd_2jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_2jet_unc2_up',ff_qcd_2jet_unc2_up,'ff_qcd_2jet_unc2_up/F')
    ff_qcd_2jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_qcd_2jet_unc2_down',ff_qcd_2jet_unc2_down,'ff_qcd_2jet_unc2_down/F')

    ff_w_0jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_0jet_unc1_up',ff_w_0jet_unc1_up,'ff_w_0jet_unc1_up/F')
    ff_w_0jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_0jet_unc1_down',ff_w_0jet_unc1_down,'ff_w_0jet_unc1_down/F')
    ff_w_0jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_0jet_unc2_up',ff_w_0jet_unc2_up,'ff_w_0jet_unc2_up/F')
    ff_w_0jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_0jet_unc2_down',ff_w_0jet_unc2_down,'ff_w_0jet_unc2_down/F')
    ff_w_1jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_1jet_unc1_up',ff_w_1jet_unc1_up,'ff_w_1jet_unc1_up/F')
    ff_w_1jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_1jet_unc1_down',ff_w_1jet_unc1_down,'ff_w_1jet_unc1_down/F')
    ff_w_1jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_1jet_unc2_up',ff_w_1jet_unc2_up,'ff_w_1jet_unc2_up/F')
    ff_w_1jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_1jet_unc2_down',ff_w_1jet_unc2_down,'ff_w_1jet_unc2_down/F')
    ff_w_2jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_2jet_unc1_up',ff_w_2jet_unc1_up,'ff_w_2jet_unc1_up/F')
    ff_w_2jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_2jet_unc1_down',ff_w_2jet_unc1_down,'ff_w_2jet_unc1_down/F')
    ff_w_2jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_w_2jet_unc2_up',ff_w_2jet_unc2_up,'ff_w_2jet_unc2_up/F')
    ff_w_2jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_w_2jet_unc2_down',ff_w_2jet_unc2_down,'ff_w_2jet_unc2_down/F')

    ff_tt_0jet_unc1_up_Branch = ReweightFile.mt_Selected.Branch('ff_tt_0jet_unc1_up',ff_tt_0jet_unc1_up,'ff_tt_0jet_unc1_up/F')
    ff_tt_0jet_unc1_down_Branch = ReweightFile.mt_Selected.Branch('ff_tt_0jet_unc1_down',ff_tt_0jet_unc1_down,'ff_tt_0jet_unc1_down/F')
    ff_tt_0jet_unc2_up_Branch = ReweightFile.mt_Selected.Branch('ff_tt_0jet_unc2_up',ff_tt_0jet_unc2_up,'ff_tt_0jet_unc2_up/F')
    ff_tt_0jet_unc2_down_Branch = ReweightFile.mt_Selected.Branch('ff_tt_0jet_unc2_down',ff_tt_0jet_unc2_down,'ff_tt_0jet_unc2_down/F')

    """
    mvisclosure_qcd_0jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_0jet_up',mvisclosure_qcd_0jet_up,'mvisclosure_qcd_0jet_up/F')
    mvisclosure_qcd_0jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_0jet_down',mvisclosure_qcd_0jet_down,'mvisclosure_qcd_0jet_down/F')    
    mvisclosure_w_0jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_0jet_up',mvisclosure_w_0jet_up,'mvisclosure_w_0jet_up/F')
    mvisclosure_w_0jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_0jet_down',mvisclosure_w_0jet_down,'mvisclosure_w_0jet_down/F')
    mvisclosure_qcd_1jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_1jet_up',mvisclosure_qcd_1jet_up,'mvisclosure_qcd_1jet_up/F')
    mvisclosure_qcd_1jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_1jet_down',mvisclosure_qcd_1jet_down,'mvisclosure_qcd_1jet_down/F')    
    mvisclosure_w_1jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_1jet_up',mvisclosure_w_1jet_up,'mvisclosure_w_1jet_up/F')
    mvisclosure_w_1jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_1jet_down',mvisclosure_w_1jet_down,'mvisclosure_w_1jet_down/F')
    mvisclosure_qcd_2jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_2jet_up',mvisclosure_qcd_2jet_up,'mvisclosure_qcd_2jet_up/F')
    mvisclosure_qcd_2jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_qcd_2jet_down',mvisclosure_qcd_2jet_down,'mvisclosure_qcd_2jet_down/F')    
    mvisclosure_w_2jet_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_2jet_up',mvisclosure_w_2jet_up,'mvisclosure_w_2jet_up/F')
    mvisclosure_w_2jet_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_w_2jet_down',mvisclosure_w_2jet_down,'mvisclosure_w_2jet_down/F')
    
    mvisclosure_tt_up_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_tt_up',mvisclosure_tt_up,'mvisclosure_tt_up/F')
    mvisclosure_tt_down_Branch = ReweightFile.mt_Selected.Branch('mvisclosure_tt_down',mvisclosure_tt_down,'mvisclosure_tt_down/F')    
    """
    lptclosure_xtrg_qcd_0jet_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_qcd_0jet_up',lptclosure_xtrg_qcd_0jet_up, 'lptclosure_xtrg_qcd_0jet_up/F')
    lptclosure_xtrg_qcd_0jet_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_qcd_0jet_down',lptclosure_xtrg_qcd_0jet_down, 'lptclosure_xtrg_qcd_0jet_down/F')
    lptclosure_xtrg_w_0jet_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_w_0jet_up',lptclosure_xtrg_w_0jet_up, 'lptclosure_xtrg_w_0jet_up/F')
    lptclosure_xtrg_w_0jet_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_w_0jet_down',lptclosure_xtrg_w_0jet_down, 'lptclosure_xtrg_w_0jet_down/F')
    lptclosure_xtrg_tt_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_tt_up',lptclosure_xtrg_tt_up, 'lptclosure_xtrg_tt_up/F')
    lptclosure_xtrg_tt_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_xtrg_tt_down',lptclosure_xtrg_tt_down, 'lptclosure_xtrg_tt_down/F')
    lptclosure_qcd_0jet_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_qcd_0jet_up',lptclosure_qcd_0jet_up, 'lptclosure_qcd_0jet_up/F')
    lptclosure_qcd_0jet_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_qcd_0jet_down',lptclosure_qcd_0jet_down, 'lptclosure_qcd_0jet_down/F')
    lptclosure_w_0jet_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_w_0jet_up',lptclosure_w_0jet_up, 'lptclosure_w_0jet_up/F')
    lptclosure_w_0jet_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_w_0jet_down',lptclosure_w_0jet_down, 'lptclosure_w_0jet_down/F')
    lptclosure_tt_up_Branch = ReweightFile.mt_Selected.Branch('lptclosure_tt_up',lptclosure_tt_up, 'lptclosure_tt_up/F')
    lptclosure_tt_down_Branch = ReweightFile.mt_Selected.Branch('lptclosure_tt_down',lptclosure_tt_down, 'lptclosure_tt_down/F')

    mtclosure_w_unc1_up_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc1_up',mtclosure_w_unc1_up,'mtclosure_w_unc1_up/F')
    mtclosure_w_unc1_down_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc1_down',mtclosure_w_unc1_down,'mtclosure_w_unc1_down/F')
    mtclosure_w_unc2_up_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc2_up',mtclosure_w_unc2_up,'mtclosure_w_unc2_up/F')
    mtclosure_w_unc2_down_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc2_down',mtclosure_w_unc2_down,'mtclosure_w_unc2_down/F')

    osssclosure_qcd_unc1_up_Branch = ReweightFile.mt_Selected.Branch('osssclosure_qcd_unc1_up',osssclosure_qcd_unc1_up,'osssclosure_qcd_unc1_up/F')
    osssclosure_qcd_unc1_down_Branch = ReweightFile.mt_Selected.Branch('osssclosure_qcd_unc1_down',osssclosure_qcd_unc1_down,'osssclosure_qcd_unc1_down/F')

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
        
        FracQCD = QCDHistos[TriggerClassification].GetBinContent(QCDHistos[TriggerClassification].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)
        FracW = WHistos[TriggerClassification].GetBinContent(WHistos[TriggerClassification].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)
        FracTT = TTHistos[TriggerClassification].GetBinContent(TTHistos[TriggerClassification].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)            

        if ReweightFile.mt_Selected.njets == 0 and ReweightFile.mt_Selected.met > 60.0:
            FracW = 1.0
            FracQCD = 0.0
            FracTT = 0.0        
            
        m_vis = (MuVector + TauVector).M()
        TransverseMass = ReweightFile.mt_Selected.MT#AddMTandPZeta.CalculateMT(MuVector,MissingMomentumVector)

        CrossTrigger = False
        if ((args.year=="2016" and ReweightFile.mt_Selected.Trigger1920)
            or ((args.year=="2017" or args.year=="2018") and ReweightFile.mt_Selected.Trigger2027)):
            CrossTrigger = True
        
        if args.IsNegative:
            Modifier = -1.0
        else:
            Modifier = 1.0

        Event_Fake_Factor[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW) * Modifier                
        #if ReweightFile.mt_Selected.njets == 0:
        #    print("Event Fake Factor: "+str(Event_Fake_Factor[0]))
        ff_qcd_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc1','up') * Modifier                
        ff_qcd_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc1','down') * Modifier                
        ff_qcd_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc2','up') * Modifier                
        ff_qcd_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc2','down') * Modifier                
        ff_qcd_1jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc1','up') * Modifier                
        ff_qcd_1jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc1','down') * Modifier                
        ff_qcd_1jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc2','up') * Modifier                
        ff_qcd_1jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc2','down') * Modifier                
        ff_qcd_2jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc1','up') * Modifier                
        ff_qcd_2jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc1','down') * Modifier                
        ff_qcd_2jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc2','up') * Modifier                
        ff_qcd_2jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc2','down') * Modifier                
        
        ff_w_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc1','up') * Modifier                
        ff_w_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc1','down') * Modifier            
        ff_w_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc2','up') * Modifier                
        ff_w_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc2','down') * Modifier                
        ff_w_1jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc1','up') * Modifier                
        ff_w_1jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc1','down') * Modifier                
        ff_w_1jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc2','up') * Modifier                
        ff_w_1jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc2','down') * Modifier            
        ff_w_2jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc1','up') * Modifier                
        ff_w_2jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc1','down') * Modifier                
        
        ff_w_2jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc2','up') * Modifier                
        ff_w_2jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc2','down') * Modifier            
        
        ff_tt_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc1','up') * Modifier                
        ff_tt_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc1','down') * Modifier                
        ff_tt_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc2','up') * Modifier                
        ff_tt_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc2','down') * Modifier                
        """
        mvisclosure_qcd_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_0jet','up') * Modifier                
        mvisclosure_qcd_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_0jet','down') * Modifier
        mvisclosure_w_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_0jet','up') * Modifier                
        mvisclosure_w_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_0jet','down') * Modifier                
        mvisclosure_qcd_1jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_1jet','up') * Modifier                
        mvisclosure_qcd_1jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_1jet','down') * Modifier
        mvisclosure_w_1jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_1jet','up') * Modifier                
        mvisclosure_w_1jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_1jet','down') * Modifier                
        mvisclosure_qcd_2jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_2jet','up') * Modifier                
        mvisclosure_qcd_2jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_qcd_2jet','down') * Modifier
        mvisclosure_w_2jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_2jet','up') * Modifier                
        mvisclosure_w_2jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_w_2jet','down') * Modifier                
        
        mvisclosure_tt_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_tt','up') * Modifier                
        mvisclosure_tt_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mvisclosure_tt','down') * Modifier
        """

        mtclosure_w_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc1','up') * Modifier                
        mtclosure_w_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc1','down') * Modifier                        
        mtclosure_w_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc2','up') * Modifier                
        mtclosure_w_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc2','down') * Modifier                        

        lptclosure_xtrg_qcd_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_qcd','up') * Modifier
        lptclosure_xtrg_qcd_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_qcd','down') * Modifier
        lptclosure_xtrg_w_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_w','up') * Modifier
        lptclosure_xtrg_w_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_w','down') * Modifier        
        lptclosure_xtrg_tt_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_tt','up') * Modifier
        lptclosure_xtrg_tt_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_tt','down') * Modifier
    
        lptclosure_qcd_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_qcd','up') * Modifier
        lptclosure_qcd_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_qcd','down') * Modifier
        lptclosure_w_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_w','up') * Modifier
        lptclosure_w_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_w','down') * Modifier
        lptclosure_tt_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_tt','up') * Modifier
        lptclosure_tt_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_tt','down') * Modifier
        osssclosure_qcd_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'osssclosure_qcd','up') * Modifier                
        osssclosure_qcd_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,CrossTrigger,FracTT,FracQCD,FracW,'osssclosure_qcd','down') * Modifier                

        FakeFactorBranch.Fill()
        ff_qcd_0jet_unc1_up_Branch.Fill()
        ff_qcd_0jet_unc1_down_Branch.Fill()
        ff_qcd_0jet_unc2_up_Branch.Fill()
        ff_qcd_0jet_unc2_down_Branch.Fill()
        ff_qcd_1jet_unc1_up_Branch.Fill()
        ff_qcd_1jet_unc1_down_Branch.Fill()
        ff_qcd_1jet_unc2_up_Branch.Fill()
        ff_qcd_1jet_unc2_down_Branch.Fill()
        ff_qcd_2jet_unc1_up_Branch.Fill()
        ff_qcd_2jet_unc1_down_Branch.Fill()
        ff_qcd_2jet_unc2_up_Branch.Fill()
        ff_qcd_2jet_unc2_down_Branch.Fill()
        
        ff_w_0jet_unc1_up_Branch.Fill()
        ff_w_0jet_unc1_down_Branch.Fill()
        ff_w_0jet_unc2_up_Branch.Fill()
        ff_w_0jet_unc2_down_Branch.Fill()
        ff_w_1jet_unc1_up_Branch.Fill()
        ff_w_1jet_unc1_down_Branch.Fill()
        ff_w_1jet_unc2_up_Branch.Fill()
        ff_w_1jet_unc2_down_Branch.Fill()
        ff_w_2jet_unc1_up_Branch.Fill()
        ff_w_2jet_unc1_down_Branch.Fill()
        ff_w_2jet_unc2_up_Branch.Fill()
        ff_w_2jet_unc2_down_Branch.Fill()
    
        ff_tt_0jet_unc1_up_Branch.Fill()
        ff_tt_0jet_unc1_down_Branch.Fill()
        ff_tt_0jet_unc2_up_Branch.Fill()
        ff_tt_0jet_unc2_down_Branch.Fill()
        
        """
        mvisclosure_qcd_0jet_up_Branch.Fill()
        mvisclosure_qcd_0jet_down_Branch.Fill()
        mvisclosure_w_0jet_up_Branch.Fill()
        mvisclosure_w_0jet_down_Branch.Fill()
        mvisclosure_qcd_1jet_up_Branch.Fill()
        mvisclosure_qcd_1jet_down_Branch.Fill()
        mvisclosure_w_1jet_up_Branch.Fill()
        mvisclosure_w_1jet_down_Branch.Fill()
        mvisclosure_qcd_2jet_up_Branch.Fill()
        mvisclosure_qcd_2jet_down_Branch.Fill()
        mvisclosure_w_2jet_up_Branch.Fill()
        mvisclosure_w_2jet_down_Branch.Fill()
        mvisclosure_tt_up_Branch.Fill()
        mvisclosure_tt_down_Branch.Fill()
        """

        lptclosure_xtrg_qcd_0jet_up_Branch.Fill()
        lptclosure_xtrg_qcd_0jet_down_Branch.Fill()
        lptclosure_xtrg_w_0jet_up_Branch.Fill()
        lptclosure_xtrg_w_0jet_down_Branch.Fill()
        lptclosure_xtrg_tt_up_Branch.Fill()
        lptclosure_xtrg_tt_down_Branch.Fill()
        lptclosure_qcd_0jet_up_Branch.Fill()
        lptclosure_qcd_0jet_down_Branch.Fill()
        lptclosure_w_0jet_up_Branch.Fill()
        lptclosure_w_0jet_down_Branch.Fill()
        lptclosure_tt_up_Branch.Fill()
        lptclosure_tt_down_Branch.Fill()
        
        mtclosure_w_unc1_up_Branch.Fill()
        mtclosure_w_unc1_down_Branch.Fill()
        mtclosure_w_unc2_up_Branch.Fill()
        mtclosure_w_unc2_down_Branch.Fill()
        
        osssclosure_qcd_unc1_up_Branch.Fill()
        osssclosure_qcd_unc1_down_Branch.Fill()
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
        
    ("Retrieving fractions...")
    FractionFile = ROOT.TFile("Weightings/FFFractionFile"+args.year+".root")
    for Histo in dataHistos:
        WHistos[Histo] = FractionFile.Get(WHistos[Histo].GetName())
        QCDHistos[Histo] = FractionFile.Get(QCDHistos[Histo].GetName())
        TTHistos[Histo] = FractionFile.Get(TTHistos[Histo].GetName())
        dataHistos[Histo] = FractionFile.Get(dataHistos[Histo].GetName())
        RealHistos[Histo] = FractionFile.Get(RealHistos[Histo].GetName())   
    
    print("Creating the fake factors.")
    for filename in args.files:
        AddFakeFactorWeightings(filename,args)
