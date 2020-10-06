import ROOT
from tqdm import tqdm
from array import array
import argparse
import FakeFactorConfiguration as cfg
import ComputeFF2018.FFcode.ApplyFF as ApplyFF

m_svBins = [0.0,50.0,100.0,150.0,200.0,300.0]
nBins = len(m_svBins)-1
theBinning = array('d',m_svBins)
HPTBins = [0.0,45.0,80.0,120.0,200.0,450.0]
nHPTBins = len(HPTBins)-1
theHPTBinning = array('d',HPTBins)

#Let's try splitting these up by triggers.
# see if that helps us deal with the the problem in the 2017 cross trigger?
WFracHisto = ROOT.TH2F("WFrac","WFrac",nBins,theBinning,7,1.0,8.0)
QCDFracHisto = ROOT.TH2F("QCDFrac","QCDFrac",nBins,theBinning,7,1.0,8.0)
TTFracHisto = ROOT.TH2F("TTFrac","TTFrac",nBins,theBinning,7,1.0,8.0)
dataFracHisto = ROOT.TH2F("DataFrac","DataFrac",nBins,theBinning,7,1.0,8.0)
RealFracHisto = ROOT.TH2F("RealFrac","RealFrac",nBins,theBinning,7,1.0,8.0)

#let's also make some differential fraction histos
WFracHisto_Differential = ROOT.TH2F("WFrac_Differential","WFrac_Differential",nBins,theBinning,nHPTBins,theHPTBinning)
QCDFracHisto_Differential = ROOT.TH2F("QCDFrac_Differential","QCDFrac_Differential",nBins,theBinning,nHPTBins,theHPTBinning)
TTFracHisto_Differential = ROOT.TH2F("TTFrac_Differential","TTFrac_Differential",nBins,theBinning,nHPTBins,theHPTBinning)
dataFracHisto_Differential = ROOT.TH2F("dataFrac_Differential","dataFrac_Differential",nBins,theBinning,nHPTBins,theHPTBinning)
RealFracHisto_Differential = ROOT.TH2F("RealFrac_Differential","RealFrac_Differential",nBins,theBinning,nHPTBins,theHPTBinning)

# njets based histograms
WFracHisto_Differential_0jet = ROOT.TH2F("WFrac_Differential_0jet","WFrac_Differential_0jet",nBins,theBinning,nHPTBins,theHPTBinning)
QCDFracHisto_Differential_0jet = ROOT.TH2F("QCDFrac_Differential_0jet","QCDFrac_Differential_0jet",nBins,theBinning,nHPTBins,theHPTBinning)
TTFracHisto_Differential_0jet = ROOT.TH2F("TTFrac_Differential_0jet","TTFrac_Differential_0jet",nBins,theBinning,nHPTBins,theHPTBinning)
dataFracHisto_Differential_0jet = ROOT.TH2F("dataFrac_Differential_0jet","dataFrac_Differential_0jet",nBins,theBinning,nHPTBins,theHPTBinning)
RealFracHisto_Differential_0jet = ROOT.TH2F("RealFrac_Differential_0jet","RealFrac_Differential_0jet",nBins,theBinning,nHPTBins,theHPTBinning)

WFracHisto_Differential_1jet = ROOT.TH2F("WFrac_Differential_1jet","WFrac_Differential_1jet",nBins,theBinning,nHPTBins,theHPTBinning)
QCDFracHisto_Differential_1jet = ROOT.TH2F("QCDFrac_Differential_1jet","QCDFrac_Differential_1jet",nBins,theBinning,nHPTBins,theHPTBinning)
TTFracHisto_Differential_1jet = ROOT.TH2F("TTFrac_Differential_1jet","TTFrac_Differential_1jet",nBins,theBinning,nHPTBins,theHPTBinning)
dataFracHisto_Differential_1jet = ROOT.TH2F("dataFrac_Differential_1jet","dataFrac_Differential_1jet",nBins,theBinning,nHPTBins,theHPTBinning)
RealFracHisto_Differential_1jet = ROOT.TH2F("RealFrac_Differential_1jet","RealFrac_Differential_1jet",nBins,theBinning,nHPTBins,theHPTBinning)

WFracHisto_Differential_ge2jet = ROOT.TH2F("WFrac_Differential_ge2jet","WFrac_Differential_ge2jet",nBins,theBinning,nHPTBins,theHPTBinning)
QCDFracHisto_Differential_ge2jet = ROOT.TH2F("QCDFrac_Differential_ge2jet","QCDFrac_Differential_ge2jet",nBins,theBinning,nHPTBins,theHPTBinning)
TTFracHisto_Differential_ge2jet = ROOT.TH2F("TTFrac_Differential_ge2jet","TTFrac_Differential_ge2jet",nBins,theBinning,nHPTBins,theHPTBinning)
dataFracHisto_Differential_ge2jet = ROOT.TH2F("dataFrac_Differential_ge2jet","dataFrac_Differential_ge2jet",nBins,theBinning,nHPTBins,theHPTBinning)
RealFracHisto_Differential_ge2jet = ROOT.TH2F("RealFrac_Differential_ge2jet","RealFrac_Differential_ge2jet",nBins,theBinning,nHPTBins,theHPTBinning)

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
    "Trigger2027": WFracHisto_Trigger2027,
    'Differential':WFracHisto_Differential,
    'Differential_0jet':WFracHisto_Differential_0jet,
    'Differential_1jet':WFracHisto_Differential_1jet,
    'Differential_ge2jet':WFracHisto_Differential_ge2jet,
    }

QCDHistos = {
    "Inclusive": QCDFracHisto,
    "Trigger22": QCDFracHisto_Trigger22,
    "Trigger1920": QCDFracHisto_Trigger1920,
    "Trigger24": QCDFracHisto_Trigger24,
    "Trigger27": QCDFracHisto_Trigger27,
    "Trigger2027": QCDFracHisto_Trigger2027,
    'Differential': QCDFracHisto_Differential,
    'Differential_0jet':QCDFracHisto_Differential_0jet,
    'Differential_1jet':QCDFracHisto_Differential_1jet,
    'Differential_ge2jet':QCDFracHisto_Differential_ge2jet,
    }

TTHistos = {
    "Inclusive": TTFracHisto,
    "Trigger22": TTFracHisto_Trigger22,
    "Trigger1920": TTFracHisto_Trigger1920,
    "Trigger24": TTFracHisto_Trigger24,
    "Trigger27": TTFracHisto_Trigger27,
    "Trigger2027": TTFracHisto_Trigger2027,
    'Differential':TTFracHisto_Differential,
    'Differential_0jet':TTFracHisto_Differential_0jet,
    'Differential_1jet':TTFracHisto_Differential_1jet,
    'Differential_ge2jet':TTFracHisto_Differential_ge2jet,
    }

dataHistos = {
    "Inclusive": dataFracHisto,
    "Trigger22": dataFracHisto_Trigger22,
    "Trigger1920": dataFracHisto_Trigger1920,
    "Trigger24": dataFracHisto_Trigger24,
    "Trigger27": dataFracHisto_Trigger27,
    "Trigger2027": dataFracHisto_Trigger2027,
    'Differential':dataFracHisto_Differential,
    'Differential_0jet':dataFracHisto_Differential_0jet,
    'Differential_1jet':dataFracHisto_Differential_1jet,
    'Differential_ge2jet':dataFracHisto_Differential_ge2jet,
    }

RealHistos = {
    "Inclusive": RealFracHisto,
    "Trigger22": RealFracHisto_Trigger22,
    "Trigger1920": RealFracHisto_Trigger1920,
    "Trigger24": RealFracHisto_Trigger24,
    "Trigger27": RealFracHisto_Trigger27,
    "Trigger2027": RealFracHisto_Trigger2027,
    'Differential':RealFracHisto_Differential,
    'Differential_0jet':RealFracHisto_Differential_0jet,
    'Differential_1jet':RealFracHisto_Differential_1jet,
    'Differential_ge2jet':RealFracHisto_Differential_ge2jet,
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
        OtherFiles = cfg.Other_Files_2016
        EmbeddedFiles = cfg.Embedded_Files_2016
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
    elif args.year == "2017":
        FilePath = cfg.ntuple_path_2017
        DataFiles = cfg.Data_Files_2017
        WFiles = cfg.W_Files_2017
        TTFiles = cfg.TT_Files_2017
        OtherFiles = cfg.Other_Files_2017
        EmbeddedFiles = cfg.Embedded_Files_2017
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
    elif args.year == "2018":
        FilePath = cfg.ntuple_path_2018
        DataFiles = cfg.Data_Files_2018
        WFiles = cfg.W_Files_2018
        TTFiles = cfg.TT_Files_2018
        OtherFiles = cfg.Other_Files_2018
        EmbeddedFiles = cfg.Embedded_Files_2017
        EmbeddedNtuple = MakeNtuples(FilePath,EmbeddedFiles)
        EmbeddedNtuple.SetNameTitle("Embedded","Embedded")
    DataNtuple = MakeNtuples(FilePath,DataFiles)
    print("DataNtuple: "+str(DataNtuple.GetEntries()))
    DataNtuple.SetNameTitle("Data","Data")
    WNtuple = MakeNtuples(FilePath,WFiles)
    print("W: "+str(WNtuple.GetEntries()))
    WNtuple.SetNameTitle("W","W")
    TTNtuple = MakeNtuples(FilePath,TTFiles)
    print("TT: "+str(TTNtuple.GetEntries()))
    TTNtuple.SetNameTitle("TT","TT")

    OtherNtuple = MakeNtuples(FilePath,OtherFiles)
        
    return DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple,OtherNtuple

def ProcessNtuple(args,Ntuple,HistogramFamily,GenMatches,Sample=""):
    for i in tqdm(range(Ntuple.GetEntries())):
        Ntuple.GetEntry(i)        
        #print(Ntuple.gen_match_2)
        #print(GenMatches)
        #print(Ntuple.gen_match_2 in GenMatches)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(Ntuple.pt_1,Ntuple.eta_1,Ntuple.phi_1,Ntuple.m_1)
        TauVector.SetPtEtaPhiM(Ntuple.pt_2,Ntuple.eta_2,Ntuple.phi_2,Ntuple.m_2)
        METVector.SetPtEtaPhiM(Ntuple.met,0.0,Ntuple.metphi,0.0)
        HiggsPT = (MuVector+TauVector+METVector).Pt()        
        if Ntuple.gen_match_2 in GenMatches:
            #print("Match!")
            HistogramFamily[ClassifyTrigger(args,Ntuple,Sample)].Fill(Ntuple.m_sv,ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
            HistogramFamily["Inclusive"].Fill(Ntuple.m_sv,ClassifyEvent(Ntuple),Ntuple.FinalWeighting)
            HistogramFamily['Differential'].Fill(Ntuple.m_sv,HiggsPT,Ntuple.FinalWeighting)
            if Ntuple.njets == 0:
                HistogramFamily['Differential_0jet'].Fill(Ntuple.m_sv,HiggsPT,Ntuple.FinalWeighting)
            elif Ntuple.njets == 1:
                HistogramFamily['Differential_1jet'].Fill(Ntuple.m_sv,HiggsPT,Ntuple.FinalWeighting)
            else:
                HistogramFamily['Differential_ge2jet'].Fill(Ntuple.m_sv,HiggsPT,Ntuple.FinalWeighting)

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
    DataNtuple,WNtuple,TTNtuple,EmbeddedNtuple,OtherNtuple = MakeAllNtuples(args)    
    #fill in W and tt histograms
    #ProcessNtuple(WNtuple,WFracHisto,RealFracHisto)
    #ProcessNtuple(TTNtuple,TTFracHisto,RealFracHisto)     
    #print("Real TT")
    ProcessNtuple(args,TTNtuple,RealHistos,[1,2,3,4,5])
    #print("TT 6:")
    ProcessNtuple(args,TTNtuple,TTHistos,[6])
    #ProcessNtuple(args,WNtuple,RealHistos,[1,2,3,4,5]) #there is no "real" in these
    ProcessNtuple(args,WNtuple,WHistos,[6])      
    ProcessNtuple(args,OtherNtuple,RealHistos,[1,2,3,4,5,6])
    if not args.UseMC:
        ProcessNtuple(args,EmbeddedNtuple,RealHistos,[1,2,3,4,5],"Embedded")
    #process the data ntuple
    print("Filling the data/QCD histograms")
    nHighHPT = 0
    for i in tqdm(range(DataNtuple.GetEntries())):
        DataNtuple.GetEntry(i)        
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(DataNtuple.pt_1,DataNtuple.eta_1,DataNtuple.phi_1,DataNtuple.m_1)
        TauVector.SetPtEtaPhiM(DataNtuple.pt_2,DataNtuple.eta_2,DataNtuple.phi_2,DataNtuple.m_2)
        METVector.SetPtEtaPhiM(DataNtuple.met,0.0,DataNtuple.metphi,0.0)
        HiggsPT = DataNtuple.HiggsPt#(MuVector+TauVector+METVector).Pt()
        
        if HiggsPT > 200:
            nHighHPT+=1
        
        QCDHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))
        QCDHistos["Inclusive"].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))
        QCDHistos["Differential"].Fill(DataNtuple.m_sv,HiggsPT)
                
        dataHistos[ClassifyTrigger(args,DataNtuple,"Data")].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))        
        dataHistos["Inclusive"].Fill(DataNtuple.m_sv,ClassifyEvent(DataNtuple))
        dataHistos["Differential"].Fill(DataNtuple.m_sv,HiggsPT)
        if DataNtuple.njets == 0:
            QCDHistos["Differential_0jet"].Fill(DataNtuple.m_sv,HiggsPT)
            dataHistos["Differential_0jet"].Fill(DataNtuple.m_sv,HiggsPT)
        elif DataNtuple.njets == 1:
            QCDHistos["Differential_1jet"].Fill(DataNtuple.m_sv,HiggsPT)
            dataHistos["Differential_1jet"].Fill(DataNtuple.m_sv,HiggsPT)
        else:
            QCDHistos["Differential_ge2jet"].Fill(DataNtuple.m_sv,HiggsPT)
            dataHistos["Differential_ge2jet"].Fill(DataNtuple.m_sv,HiggsPT)
        
    print("High HPT events: "+str(nHighHPT))

    #Perform the subtractions
    #CanvasOne = ROOT.TCanvas("CanvasOne","CanvasOne")
    #print("QCD bins before subtraction:")
    #QCDHistos["Inclusive"].Draw("COLZ TEXT")
    #CanvasThree = ROOT.TCanvas("CanvasThree","CanvasThree")
    #RealHistos["Inclusive"].Draw("COLZ TEXT")
    #CanvasFour = ROOT.TCanvas("CanvasFour","CanvasFour")
    #TTHistos["Inclusive"].Draw("COLZ TEXT")
    #CanvasFive = ROOT.TCanvas("CanvasFive","CanvasFive")
    #WHistos["Inclusive"].Draw("COLZ TEXT")    
    #raw_input('Press Enter To Continue...')
    for Trigger in QCDHistos:
        QCDHistos[Trigger].Add(RealHistos[Trigger],-1)
        QCDHistos[Trigger].Add(TTHistos[Trigger],-1)
        QCDHistos[Trigger].Add(WHistos[Trigger],-1)
    #CanvasTwo = ROOT.TCanvas("CanvasTwo","CanvasTwo")
    #print("QCD bins after subtraction: ")
    #QCDHistos["Inclusive"].Draw("COLZ TEXT")
    #raw_input('Press Enter To Continue...')

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
    if args.isDifferential:
        if args.year == '2016':
            theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2016_Differential/",'mt',isDifferential=True,attempt0JetMETCorrection=True)
        elif args.year == '2017':
            theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2017_Differential/",'mt',isDifferential=True)
        elif args.year == '2018':
            theFFApplicationTool = ApplyFF.FFApplicationTool("Weightings/DeepFFs2018_Differential/",'mt',isDifferential=True)
    else:
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

    #mtclosure_w_unc1_up = array('f',[0.])
    #mtclosure_w_unc1_down = array('f',[0.])
    #mtclosure_w_unc2_up = array('f',[0.])
    #mtclosure_w_unc2_down = array('f',[0.])
    pthclosure_w_up = array('f',[0.])
    pthclosure_w_down = array('f',[0.])

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

    #mtclosure_w_unc1_up_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc1_up',mtclosure_w_unc1_up,'mtclosure_w_unc1_up/F')
    #mtclosure_w_unc1_down_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc1_down',mtclosure_w_unc1_down,'mtclosure_w_unc1_down/F')
    #mtclosure_w_unc2_up_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc2_up',mtclosure_w_unc2_up,'mtclosure_w_unc2_up/F')
    #mtclosure_w_unc2_down_Branch = ReweightFile.mt_Selected.Branch('mtclosure_w_unc2_down',mtclosure_w_unc2_down,'mtclosure_w_unc2_down/F')
    pthclosure_w_up_Branch = ReweightFile.mt_Selected.Branch('pthclosure_w_up',pthclosure_w_up,'pthclosure_w_up/F')
    pthclosure_w_down_Branch = ReweightFile.mt_Selected.Branch('pthclosure_w_down',pthclosure_w_down,'pthclosure_w_down/F')

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

        HPT = ReweightFile.mt_Selected.HiggsPt#(MuVector + TauVector + MissingMomentumVector).Pt()

        #now we need to compute proper fractions now        
        EventClassification = ClassifyEvent(ReweightFile.mt_Selected)
        TriggerClassification = ClassifyTrigger(args,ReweightFile.mt_Selected,Sample)                
        
        if args.isDifferential:
            if ReweightFile.mt_Selected.njets == 0:
                FracQCD = QCDHistos["Differential_0jet"].GetBinContent(QCDHistos["Differential_0jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),QCDHistos["Differential_0jet"].GetYaxis().FindBin(HPT))
                FracW = WHistos["Differential_0jet"].GetBinContent(WHistos["Differential_0jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),WHistos["Differential_0jet"].GetYaxis().FindBin(HPT))
                FracTT = TTHistos["Differential_0jet"].GetBinContent(TTHistos["Differential_0jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),TTHistos["Differential_0jet"].GetYaxis().FindBin(HPT))
            elif ReweightFile.mt_Selected.njets == 1:
                FracQCD = QCDHistos["Differential_1jet"].GetBinContent(QCDHistos["Differential_1jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),QCDHistos["Differential_1jet"].GetYaxis().FindBin(HPT))
                FracW = WHistos["Differential_1jet"].GetBinContent(WHistos["Differential_1jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),WHistos["Differential_1jet"].GetYaxis().FindBin(HPT))
                FracTT = TTHistos["Differential_1jet"].GetBinContent(TTHistos["Differential_1jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),TTHistos["Differential_1jet"].GetYaxis().FindBin(HPT))
            else:
                FracQCD = QCDHistos["Differential_ge2jet"].GetBinContent(QCDHistos["Differential_ge2jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),QCDHistos["Differential_ge2jet"].GetYaxis().FindBin(HPT))
                FracW = WHistos["Differential_ge2jet"].GetBinContent(WHistos["Differential_ge2jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),WHistos["Differential_ge2jet"].GetYaxis().FindBin(HPT))
                FracTT = TTHistos["Differential_ge2jet"].GetBinContent(TTHistos["Differential_ge2jet"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),TTHistos["Differential_ge2jet"].GetYaxis().FindBin(HPT))
        else:
            FracQCD = QCDHistos["Inclusive"].GetBinContent(QCDHistos["Inclusive"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)
            FracW = WHistos["Inclusive"].GetBinContent(WHistos["Inclusive"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)
            FracTT = TTHistos["Inclusive"].GetBinContent(TTHistos["Inclusive"].GetXaxis().FindBin(ReweightFile.mt_Selected.m_sv),EventClassification)            
        #if EventClassification == 1 or EventClassification == 2:
        #    FracQCD = 0.24
        #    FracW = 0.75
        #    FracTT = 0.01

        #if ReweightFile.mt_Selected.njets == 0 and ReweightFile.mt_Selected.met > 60.0:
        #    FracW = 1.0
        #    FracQCD = 0.0
        #    FracTT = 0.0        
            
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

        Event_Fake_Factor[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW) * Modifier                                
        
        """
        if ReweightFile.mt_Selected.njets == 1 and ReweightFile.mt_Selected.m_sv > 130 and ReweightFile.mt_Selected.m_sv < 290 and HPT > 120 and HPT < 200:
            print("Run: "+str(ReweightFile.mt_Selected.run))
            print("Lumi: "+str(ReweightFile.mt_Selected.lumi))
            print("Evt: "+str(ReweightFile.mt_Selected.evt))
            print("m_sv: "+str(ReweightFile.mt_Selected.m_sv))
            print("TauPt: "+str(TauVector.Pt()))
            print("MuPt: "+str(MuVector.Pt()))
            print("Frac_QCD: "+str(FracQCD))
            print("Frac_W: "+str(FracW))
            print("Frac_TT: "+str(FracTT))
            print("Event Fake Factor: "+str(Event_Fake_Factor[0]))
            print ''
        """
        
        ff_qcd_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc1','up') * Modifier                
        ff_qcd_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc1','down') * Modifier                
        ff_qcd_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc2','up') * Modifier                
        ff_qcd_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_0jet_unc2','down') * Modifier                
        ff_qcd_1jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc1','up') * Modifier                
        ff_qcd_1jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc1','down') * Modifier                
        ff_qcd_1jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc2','up') * Modifier                
        ff_qcd_1jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_1jet_unc2','down') * Modifier                
        ff_qcd_2jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc1','up') * Modifier                
        ff_qcd_2jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc1','down') * Modifier                
        ff_qcd_2jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc2','up') * Modifier                
        ff_qcd_2jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_qcd_2jet_unc2','down') * Modifier                
        
        ff_w_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc1','up') * Modifier                
        ff_w_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc1','down') * Modifier            
        ff_w_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc2','up') * Modifier                
        ff_w_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_0jet_unc2','down') * Modifier                
        ff_w_1jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc1','up') * Modifier                
        ff_w_1jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc1','down') * Modifier                
        ff_w_1jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc2','up') * Modifier                
        ff_w_1jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_1jet_unc2','down') * Modifier            
        ff_w_2jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc1','up') * Modifier                
        ff_w_2jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc1','down') * Modifier                
        
        ff_w_2jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc2','up') * Modifier                
        ff_w_2jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_w_2jet_unc2','down') * Modifier            
        ff_tt_0jet_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc1','up') * Modifier 

        ff_tt_0jet_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc1','down') * Modifier                
        ff_tt_0jet_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc2','up') * Modifier                
        ff_tt_0jet_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'ff_tt_0jet_unc2','down') * Modifier                
        #mtclosure_w_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc1','up') * Modifier                
        #mtclosure_w_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc1','down') * Modifier                        
        #mtclosure_w_unc2_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc2','up') * Modifier                
        #mtclosure_w_unc2_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'mtclosure_w_unc2','down') * Modifier                        
        pthclosure_w_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'pthclosure_w','up') * Modifier                
        pthclosure_w_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'pthclosure_w','down') * Modifier                

        lptclosure_xtrg_qcd_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_qcd','up') * Modifier
        lptclosure_xtrg_qcd_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_qcd','down') * Modifier
        lptclosure_xtrg_w_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_w','up') * Modifier
        lptclosure_xtrg_w_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_w','down') * Modifier        
        lptclosure_xtrg_tt_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_tt','up') * Modifier
        lptclosure_xtrg_tt_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_xtrg_tt','down') * Modifier
    
        lptclosure_qcd_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_qcd','up') * Modifier
        lptclosure_qcd_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_qcd','down') * Modifier
        lptclosure_w_0jet_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_w','up') * Modifier
        lptclosure_w_0jet_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_w','down') * Modifier
        lptclosure_tt_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_tt','up') * Modifier
        lptclosure_tt_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'lptclosure_tt','down') * Modifier
        osssclosure_qcd_unc1_up[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'osssclosure_qcd','up') * Modifier                
        osssclosure_qcd_unc1_down[0] = theFFApplicationTool.get_ff(TauVector.Pt(),TransverseMass,m_vis,MuVector.Pt(),TauVector.DeltaR(MuVector),ReweightFile.mt_Selected.met,ReweightFile.mt_Selected.njets,HPT,CrossTrigger,FracTT,FracQCD,FracW,'osssclosure_qcd','down') * Modifier           

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
        
        #mtclosure_w_unc1_up_Branch.Fill()
        #mtclosure_w_unc1_down_Branch.Fill()
        #mtclosure_w_unc2_up_Branch.Fill()
        #mtclosure_w_unc2_down_Branch.Fill()
        pthclosure_w_up_Branch.Fill()
        pthclosure_w_down_Branch.Fill()
        
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
    parser.add_argument('--isDifferential',help='perform the calculation using differential specialized factors and fractions',action='store_true')
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
