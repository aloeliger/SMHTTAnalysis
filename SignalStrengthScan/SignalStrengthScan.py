import ROOT
from tqdm import tqdm
from array import array
import argparse
import math

def GetVariableMaxMin(VariableName,args):
    FirstTestFile = True
    VarMax = 0.0
    VarMin = 0.0
    for TestFileName in args.Files:
        TestFile = ROOT.TFile(TestFileName)
        TestTree = TestFile.mt_Selected
        if FirstTestFile:
            VarMax = TestTree.GetMaximum(VariableName)
            VarMin = TestTree.GetMinimum(VariableName)
        else:
            if TestTree.GetMaximum(VariableName) > VarMax:
                VarMax = TestTree.GetMaximum(VariableName)
            if TestTree.GetMinimum(VariableName) < VarMin:
                VarMin = TestTree.GetMinimum(VariableName)
    return VarMax,VarMin

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 2D s/root(b) plot s")
    parser.add_argument('Files',nargs="+",help="List of files to generate the plots from.")
    parser.add_argument('--ScanVariables',nargs="+",help="List of variables to try to scan over")
    parser.add_argument('--UseFakeFactorOnFiles',nargs="+",help="Use the file's fake factor weighting when calculating final weights for these files")

    args = parser.parse_args()

    HistogramDictionary = {}    

    for TheFile in args.Files:
        TreeFile = ROOT.TFile(TheFile)
        TheTree = TreeFile.mt_Selected
        TheHisto = TheFile[TheFile.rfind("/")+1:]
        TheHisto = TheHisto.split(".")[0]
        UseFakeFactor = False
        try:
            if TheFile in args.UseFakeFactorOnFiles:
                UseFakeFactor = True
        except:
            pass
        if UseFakeFactor:
            TheHisto = TheHisto+"_Fake"
        #generate all the histograms
        for VariableName in args.ScanVariables:
            FullHistoName = TheHisto+"_"+VariableName
            #okay, we need to determine the maximum and minimum possible boundary for use in this variable            
            MaxVal,MinVal = GetVariableMaxMin(VariableName,args)
            ScanHisto = ROOT.TH2F(FullHistoName,FullHistoName,10,50.0,150.0,20,MaxVal,MinVal)            
            HistogramDictionary[FullHistoName] = ScanHisto            
        #start filling all the histograms
        print("Running: "+TheFile)
        for i in tqdm(range(TheTree.GetEntries())):
            TheTree.GetEntry(i)
            MuVector = ROOT.TLorentzVector()
            TauVector = ROOT.TLorentzVector()
            METVector = ROOT.TLorentzVector()
            MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
            TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)        
            METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
            VisibleMass = (TauVector+MuVector).M()
            MT = math.sqrt(2.0*MuVector.Pt()*METVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(METVector))))
            if(MT > 50.0):
                continue
            TheWeighting = TheTree.FinalWeighting
            if UseFakeFactor:
                TheWeighting = TheWeighting*TheTree.Event_Fake_Factor

            for VariableName in args.ScanVariables:
                HistogramDictionary[TheHisto+"_"+VariableName].Fill(VisibleMass,TheTree.GetLeaf(VariableName).GetValue(),TheWeighting)
    #okay, we should have all thehistograms filled and we can start making s/root(b) things for everything?
    print(HistogramDictionary)
    BackgroundList = [
        "ST_tW_top",
        "EWKZLL",
        "TTTo2L2Nu",
        "TTToHadronic",
        "ST_tW_antitop",
        "ST_tW_antitop",
        "WZ",
        "ST_t_antitop",
        "ST_t_antitop",
        "TTToSemiLeptonic",
        "Data_Fake",
        "ST_t_top",
        "DY",
        "ZZ",
        "WW",
        "EWKZNuNu"
        ]
    SignalList = [
        "ZH",
        "ggH",
        "WHPlus",
        "WHMinus",
        "VBF"
        ]    
    for VariableName in args.ScanVariables:
        MaxVal,MinVal = GetVariableMaxMin(VariableName,args)
        SignalBackgroundHisto = ROOT.TH2F(VariableName+"_S/sqroot(B)",+VariableName+"_S/sqroot(B)",10,50.0,150.0,20,MaxVal,MinVal)
         SignalHisto = ROOT.TH2F(VariableName+"_S",VariableName+"_S",10,50.0,150.0,20,MaxVal,MinVal)
         BackgroundHisto = ROOT.TH2F(VariableName+"_B",VariableName+"_B",10,50.0,150.0,20,MaxVal,MinVal)
         for Background in BackgroundList:
             BackgroundHisto.Add(HistogramDictionary[Background+"_"+VariableName])
         for Signal in SignalList:
             SignalHisto.Add(HistogramDictionary[Signal+"_"+VariableName])
         for x in range(SignalBackgroundHisto.GetNbinsX()):
             for y in range (SignalBackgroundHisto.GetNbinsY()):
                 SignalBackgroundHisto.SetBinContent(x,y,SignalHisto.GetBinContent(x,y)/math.sqrt(BackgroundHisto.GetBinContent(x,y)))
