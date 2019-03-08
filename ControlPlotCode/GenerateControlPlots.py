import ROOT
import sys
from tqdm import tqdm
import argparse

def GenerateControlPlots(TheFile,args):
    #Let's start with 6 possible control plots
    # Tau pt, Tau Eta, Mu Pt, Mu Eta, MET, MET phi.
    TheHisto = TheFile[TheFile.rfind("/")+1:]    
    TheHisto = TheHisto.split(".")[0]
    FullHistoName = TheHisto+"_"+args.Year
    if args.UseFakeFactor:
        FullHistoName=FullHistoName+"_Fake_"
    
    print("Histogram Name: "+FullHistoName)

    TreeFile = ROOT.TFile(TheFile)
    TheTree = TreeFile.mt_Selected

    TauPtHisto = ROOT.TH1F(FullHistoName+"_TauPt",FullHistoName+"_TauPt",20,20.0,120.0)
    TauEtaHisto = ROOT.TH1F(FullHistoName+"_TauEta",FullHistoName+"_TauEta",26, -2.3, 2.3)
    MuPtHisto  = ROOT.TH1F(FullHistoName+"_MuPt",FullHistoName+"_MuPt",20,20.0,120.0)
    MuEtaHisto = ROOT.TH1F(FullHistoName+"_MuEta",FullHistoName+"_MuEta",26,-2.3,2.3)
    METHisto = ROOT.TH1F(FullHistoName+"_MET",FullHistoName+"_MET",20,0.0,200.0)

    METPhiHisto = ROOT.TH1F(FullHistoName+"_METPhi",FullHistoName+"_METPhi",20,-3.14,3.14)
    mvisHisto = ROOT.TH1F(FullHistoName+"_mvis",FullHistoName+"_mvis",20,50.0,150.0)
    NJetsHisto = ROOT.TH1F(FullHistoName+"_Njets",FullHistoName+"_Njets",6,0.0,6.0)
    HiggsPtHisto = ROOT.TH1F(FullHistoName+"_HiggsPt",FullHistoName+"_HiggsPt",20,20.0,120.0)
    mjjHisto = ROOT.TH1F(FullHistoName+"_mjj",FullHistoName+"_mjj",20,0.0,500.0)

    TauPtHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_TauPt",FullHistoName+"_genmatch_low_TauPt",20,20.0,120.0)
    TauEtaHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_TauEta",FullHistoName+"_genmatch_low_TauEta",26, -2.3, 2.3)
    MuPtHisto_DYll  = ROOT.TH1F(FullHistoName+"_genmatch_low_MuPt",FullHistoName+"_genmatch_low_MuPt",20,20.0,120.0)
    MuEtaHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_MuEta",FullHistoName+"_genmatch_low_MuEta",26,-2.3,2.3)
    METHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_MET",FullHistoName+"_genmatch_low_MET",20,0.0,200.0)
    METPhiHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_METPhi",FullHistoName+"_genmatch_low_METPhi",20,-3.14,3.14)

    mvisHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_mvis",FullHistoName+"_genmatch_low_mvis",20,50.0,150.0)
    NJetsHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_Njets",FullHistoName+"_genmatch_low_Njets",6,0.0,6.0)
    HiggsPtHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_HiggsPt",FullHistoName+"_genmatch_low_HiggsPt",20,20.0,120.0)
    mjjHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_mjj",FullHistoName+"_genmatch_low_mjj",20,0.0,500.0)

    TauPtHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_TauPt",FullHistoName+"_genmatch_tt_TauPt",20,20.0,120.0)
    TauEtaHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_TauEta",FullHistoName+"_genmatch_tt_TauEta",26, -2.3, 2.3)
    MuPtHisto_DYtt  = ROOT.TH1F(FullHistoName+"_genmatch_tt_MuPt",FullHistoName+"_genmatch_tt_MuPt",20,20.0,120.0)
    MuEtaHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_MuEta",FullHistoName+"_genmatch_tt_MuEta",26,-2.3,2.3)
    METHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_MET",FullHistoName+"_genmatch_tt_MET",20,0.0,200.0)
    METPhiHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_METPhi",FullHistoName+"_genmatch_tt_METPhi",20,-3.14,3.14)
    
    mvisHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_mvis",FullHistoName+"_genmatch_tt_mvis",20,50.0,150.0)
    NJetsHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_Njets",FullHistoName+"_genmatch_tt_Njets",6,0.0,6.0)
    HiggsPtHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_HiggsPt",FullHistoName+"_genmatch_tt_HiggsPt",20,20.0,120.0)
    mjjHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_mjj",FullHistoName+"_genmatch_tt_mjj",20,0.0,500.0)
    

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)        
        METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        
        if(TauVector.Pt()<30.0 or MuVector.Pt() < 26.0):
            continue
        TheWeighting = TheTree.FinalWeighting
        if args.UseFakeFactor:
            TheWeighting = TheWeighting*TheTree.Event_Fake_Factor 

        TauPtHisto.Fill(TauVector.Pt(),TheWeighting)
        TauEtaHisto.Fill(TauVector.Eta(),TheWeighting)
        MuPtHisto.Fill(MuVector.Pt(),TheWeighting)
        MuEtaHisto.Fill(MuVector.Eta(),TheWeighting)
        METHisto.Fill(TheTree.met,TheWeighting)
        METPhiHisto.Fill(TheTree.metphi,TheWeighting)
        mvisHisto.Fill((TauVector+MuVector).M(),TheWeighting)
        NJetsHisto.Fill(TheTree.njets,TheWeighting)
        HiggsPtHisto.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
        mjjHisto.Fill(TheTree.mjj,TheWeighting)
        
        if args.Year == "2018":
            if (TheHisto == "DY" and TheTree.gen_match_2 <5):
                TauPtHisto_DYll.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYll.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYll.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYll.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYll.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYll.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYll.Fill((TauVector+MuVector).M(),TheWeighting)
                NJetsHisto_DYll.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYll.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYll.Fill(TheTree.mjj,TheWeighting)

            elif(TheHisto == "DY" and TheTree.gen_match_2 ==5):
                TauPtHisto_DYtt.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYtt.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYtt.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYtt.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYtt.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYtt.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYtt.Fill((TauVector+MuVector).M(),TheWeighting)
                NJetsHisto_DYtt.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYtt.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYtt.Fill(TheTree.mjj,TheWeighting)
        elif args.Year == "2017":
            if (TheHisto == "DY" and TheTree.gen_match_2 <5):
                TauPtHisto_DYll.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYll.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYll.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYll.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYll.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYll.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYll.Fill((TauVector+MuVector).M(),TheWeighting)
                NJetsHisto_DYll.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYll.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYll.Fill(TheTree.mjj,TheWeighting)

            elif TheHisto == "Embedded":
                TauPtHisto_DYtt.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYtt.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYtt.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYtt.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYtt.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYtt.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYtt.Fill((TauVector+MuVector).M(),TheWeighting)
                NJetsHisto_DYtt.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYtt.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
    
    OutFile = ROOT.TFile("TemporaryFiles/ControlRegion.root","UPDATE")
    TauPtHisto.Write()
    TauEtaHisto.Write()
    MuPtHisto.Write()
    MuEtaHisto.Write()
    METHisto.Write()
    METPhiHisto.Write()
    mvisHisto.Write()
    NJetsHisto.Write()
    HiggsPtHisto.Write()
    mjjHisto.Write()

    if args.Year == "2018":        
        if(TheHisto == "DY"):
            TauPtHisto_DYll.Write()
            TauEtaHisto_DYll.Write()
            MuPtHisto_DYll.Write()
            MuEtaHisto_DYll.Write()
            METHisto_DYll.Write()
            METPhiHisto_DYll.Write()
            mvisHisto_DYll.Write()
            NJetsHisto_DYll.Write()
            HiggsPtHisto_DYll.Write()
            mjjHisto_DYll.Write()
            
            TauPtHisto_DYtt.Write()
            TauEtaHisto_DYtt.Write()
            MuPtHisto_DYtt.Write()
            MuEtaHisto_DYtt.Write()
            METHisto_DYtt.Write()
            METPhiHisto_DYtt.Write()
            mvisHisto_DYtt.Write()
            NJetsHisto_DYtt.Write()
            HiggsPtHisto_DYtt.Write()
            mjjHisto_DYtt.Write()

    if args.Year == "2017":
        print("Writing 2017 version of DY...")
        if TheHisto == "Embedded":
            TauPtHisto_DYtt.Write()
            TauEtaHisto_DYtt.Write()
            MuPtHisto_DYtt.Write()
            MuEtaHisto_DYtt.Write()
            METHisto_DYtt.Write()
            METPhiHisto_DYtt.Write()
            mvisHisto_DYtt.Write()
            NJetsHisto_DYtt.Write()
            HiggsPtHisto_DYtt.Write()
            mjjHisto_DYtt.Write()

        elif TheHisto == "DY":
            TauPtHisto_DYll.Write()
            TauEtaHisto_DYll.Write()
            MuPtHisto_DYll.Write()
            MuEtaHisto_DYll.Write()
            METHisto_DYll.Write()
            METPhiHisto_DYll.Write()
            mvisHisto_DYll.Write()
            NJetsHisto_DYll.Write()
            HiggsPtHisto_DYll.Write()
            mjjHisto_DYll.Write()
    OutFile.Write()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate control plots.")
    parser.add_argument('Year',choices=["2016","2017","2018"],help="Select which year's plots to generate.")
    parser.add_argument('Files',nargs="+",help="List of files to generate control plots from.")
    parser.add_argument('--UseFakeFactor',help="Use the file's fake factor weightings when making plots for this file.",action="store_true")
    
    args = parser.parse_args()
        
    for File in args.Files:
        print("Making control plots for: "+File)
        GenerateControlPlots(File,args)