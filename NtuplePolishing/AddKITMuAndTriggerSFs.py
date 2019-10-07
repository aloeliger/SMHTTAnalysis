import ROOT
import argparse
import getSF
import os
from tqdm import tqdm
from array import array
import AddDiTauTriggerFactor

#based on lepton efficiences (interface) class present at https://github.com/CMS-HTT
class KITMuSF:
    def __init__(self):
        self.eff_data = {}
        self.eff_mc = {}
        self.etaBinsH = ROOT.TH1D()

    def SetAxisBins(self,graph):
        NPOINTS = graph.GetN()
        dummylist = []
        for i in range(NPOINTS+1):
            dummylist.append(0)
        AXISBINS = array('d',dummylist)
        for i in range(NPOINTS):
            AXISBINS[i] = (graph.GetX()[i] - graph.GetErrorXlow(i))
        AXISBINS[NPOINTS] = (graph.GetX()[NPOINTS-1]+graph.GetErrorXhigh(NPOINTS-1))
        graph.GetXaxis().Set(NPOINTS,AXISBINS)

    def check_SameBinning(self,graph1,graph2):
        haveSameBins = False
        n1 = graph1.GetXaxis().GetNbins()
        n2 = graph2.GetXaxis().GetNbins()

        if(n1 != n2):
            return False
        else:
            haveSameBins=True
            nbins = n1
            for i in range(nbins):
                x1 = graph1.GetXaxis().GetXbins().GetArray()[i]
                x2 = graph2.GetXaxis().GetXbins().GetArray()[i]
                haveSameBins = haveSameBins and (x1 == x2)
        return haveSameBins

    def init_ScaleFactors(self,inputRootFile):
        fileIn = ROOT.TFile(inputRootFile)
        if fileIn.IsZombie():        
            raise RuntimeError("Zombine fileIn")
        HistoBaseName="ZMass"
        self.etaBinsH=fileIn.Get("etaBinsH")
        self.etaBinsH.SetDirectory(0)
        nEtaBins = self.etaBinsH.GetNbinsX()
        for i in range(nEtaBins):
            etaLabel = self.etaBinsH.GetXaxis().GetBinLabel(i+1)
            GraphName = HistoBaseName+etaLabel+"_Data"
            if fileIn.GetListOfKeys().Contains(GraphName):
                self.eff_data[etaLabel]=fileIn.Get(GraphName)
                self.SetAxisBins(self.eff_data[etaLabel])
            else:
                self.eff_data[etaLabel]=0
        
            GraphName=HistoBaseName+etaLabel+"_MC"
            if(fileIn.GetListOfKeys().Contains(GraphName)):
                self.eff_mc[etaLabel] = fileIn.Get(GraphName)
                self.SetAxisBins(self.eff_mc[etaLabel])
            else:
                self.eff_mc[etaLabel]=0
        
            if(self.eff_data[etaLabel] != 0 and self.eff_mc[etaLabel] != 0):
                sameBinning = self.check_SameBinning(self.eff_data[etaLabel], self.eff_mc[etaLabel])
                if not sameBinning:
                    raise RuntimeError("Checking the same binning has returned different binning for mc and data")

    def FindEtaLabel(self,Eta, Which):        
        Eta = abs(Eta)        
        #FIXME
        binNumber = self.etaBinsH.GetXaxis().FindFixBin(Eta)
        EtaLabel = self.etaBinsH.GetXaxis().GetBinLabel(binNumber)
    
        if (Which == "data"):
            if not EtaLabel in self.eff_data:
                print("Error in finding EtaLabel in self.eff_data")
            elif(Which == "mc"):
                if not EtaLabel in self.eff_mc:
                    print("Error in finding EtaLabel in self.eff_mc")
        return EtaLabel

    def FindPtBin(self,eff_map,EtaLabel,Pt):
        Npoints = eff_map[EtaLabel].GetN()
        ptMAX = (eff_map[EtaLabel].GetX()[Npoints-1])+(eff_map[EtaLabel].GetErrorXhigh(Npoints-1))
        ptMIN = (eff_map[EtaLabel].GetX()[0])-(eff_map[EtaLabel].GetErrorXlow(0))
        if (Pt >= ptMAX):
            return Npoints
        elif(Pt < ptMIN):
            print("WARNING in ScaleFactor::get_EfficiencyData(double pt, double eta) from LepEffInterface/src/ScaleFactor.cc: pT too low (pt = " + str(Pt) + "), min value is " + str(ptMIN))
            return -99
        else:
            return eff_map[EtaLabel].GetXaxis().FindFixBin(Pt)

    def get_EfficiencyData(self,pt,eta):
        label = self.FindEtaLabel(eta,"data")
        ptbin = self.FindPtBin(self.eff_data,label,pt)
        if(ptbin==-99):
            eff=1
        else:
            eff = self.eff_data[label].GetY()[ptbin-1]

        if(eff > 1):
            print("Warning, Data eff over flow")
            print(eff)
            eff =1
        elif(eff < 0):
            print("Warning, Data eff under flow")
            print(eff)
            eff = 1
    
        return eff

    def get_EfficiencyMC(self,pt,eta):
        label = self.FindEtaLabel(eta,"mc")
        ptbin = self.FindPtBin(self.eff_mc,label,pt)
        if(ptbin==-99):
            eff = 1
        else:
            eff=self.eff_mc[label].GetY()[ptbin-1]

        if(eff > 1):
            print("Warning, MC eff over flow")
            eff =1
        elif(eff < 0):
            print("Warning, MC eff under flow")
            eff = 1
    
        return eff

    def get_ScaleFactor(self,pt,eta):
        efficiency_data = self.get_EfficiencyData(pt,eta)
        efficiency_mc = self.get_EfficiencyMC(pt,eta)
        if efficiency_mc != 0:
            SF=efficiency_data/efficiency_mc
        else:
            SF=1
        return SF

def AddKITMuAndTriggerSFs(File,args):    
    CheckFile = ROOT.TFile(File)
    try:
        CheckFile.mt_Selected.DiTauTriggerWeight
    except:
        print("Failed to find ditau trigger factors. Adding them...")
        AddDiTauTriggerFactor.AddDiTauTriggerFactor(File,args)
    CheckFile.Close()

    TheFile = ROOT.TFile(File,"UPDATE")
    TheTree = TheFile.mt_Selected

    MuAndTriggerSF = array('f',[0.])
    MuAndTriggerSF_Branch = TheTree.Branch("MuAndTriggerSF",MuAndTriggerSF,"MuAndTriggerSF/F")
    
    IDIso = KITMuSF()
    if args.year == "2016":
        IDIso.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2016BtoH/Muon_IdIso_IsoLt0p15_2016BtoH_eff.root")
        IsoMu22SF = KITMuSF()
        IsoMu22SF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2016BtoH/Muon_Mu22OR_eta2p1_eff.root")
        CrossTriggerSF = KITMuSF()
        CrossTriggerSF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2016BtoH/Muon_Mu19leg_2016BtoH_eff.root")
        TauLegFactor = getSF.SFReader("triggerSF/mu-tau/trigger_sf_mt.root",interpolate=False)

    elif args.year == "2017":
        IDIso.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2017/Muon_IdIso_IsoLt0.15_eff_RerecoFall17.root")
        IsoMu24or27SF = KITMuSF()
        IsoMu24or27SF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2017/Muon_IsoMu24orIsoMu27.root")        
        CrossTriggerSF = KITMuSF()
        CrossTriggerSF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2017/Muon_MuTau_IsoMu20.root")

    elif args.year == "2018":
        IDIso.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2018/Muon_Run2018_IdIso.root")
        IsoMu24or27SF = KITMuSF()
        IsoMu24or27SF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2018/Muon_Run2018_IsoMu24orIsoMu27.root")
        CrossTriggerSF = KITMuSF()
        CrossTriggerSF.init_ScaleFactors("/data/aloeliger/CMSSW_9_4_0/src/LeptonEfficiencies/Muon/Run2018/Muon_Run2018_IsoMu20.root")
        

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        IDIsoSF = IDIso.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
        #decide which trigger we're using
        if args.year=="2016":
            if (TheTree.Trigger22):
                TriggerSF = IsoMu22SF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
            elif (TheTree.Trigger1920):
                TriggerSF = CrossTriggerSF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
                TriggerSF = TriggerSF * TauLegFactor.getSF(TauVector.Pt(),TauVector.Eta(), tau_isocut="TightIso",genuine=(TheTree.gen_match_2 == 6),tau_dm = TheTree.l2_decayMode)
            else:
                print("WARNING! Something fell through our 2016 trigger definitions!")                
                
                TriggerSF = 1
        elif args.year=="2017":
            if(TheTree.Trigger2027):
                TriggerSF = CrossTriggerSF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
                TriggerSF = TriggerSF*TheTree.DiTauTriggerWeight
            elif(TheTree.Trigger24):
                TriggerSF = IsoMu24or27SF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
            elif(TheTree.Trigger27):
                TriggerSF = IsoMu24or27SF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())                
            else:
                print("WARNING! Something fell through our 2017 trigger definitions!")
                TriggerSF = 1
                
        elif args.year=="2018":
            if(TheTree.Trigger24 or TheTree.Trigger27):
                TriggerSF = IsoMu24or27SF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
            elif (TheTree.Trigger2027):
                 TriggerSF = CrossTriggerSF.get_ScaleFactor(MuVector.Pt(),MuVector.Eta())
                 TriggerSF = TriggerSF*TheTree.DiTauTriggerWeight
            else:
                print("WARNING! Something fell through our 2018 trigger definitions!")
                TriggerSF = 1

        MuAndTriggerSF[0] = IDIsoSF * TriggerSF
        MuAndTriggerSF_Branch.Fill()
    TheFile.cd()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    TheFile.Write()
    TheFile.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create and add KIT style muon SF branches")
    parser.add_argument('year',choices=["2016","2017","2018"])
    parser.add_argument('Files',nargs="+",help="List of the files to run the tool on")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing KIT style mu and trigger SFs for "+str(File))
        AddKITMuAndTriggerSFs(File,args)
