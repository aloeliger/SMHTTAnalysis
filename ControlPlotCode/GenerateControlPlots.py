import ROOT
import sys
from tqdm import tqdm
import argparse
import math

def GenerateControlPlots(TheFile,OutFile,args):
    #Let's start with 6 possible control plots
    # Tau pt, Tau Eta, Mu Pt, Mu Eta, MET, MET phi.
    TheHisto = TheFile[TheFile.rfind("/")+1:]    
    TheHisto = TheHisto.split(".")[0]
    FullHistoName = TheHisto+"_"+args.Year
    UseFakeFactor = False
    try:
        if TheFile in args.UseFakeFactorOnFiles:
            UseFakeFactor = True
    except:
        pass    
    
    print("Histogram Name: "+FullHistoName)

    TreeFile = ROOT.TFile(TheFile)
    TheTree = TreeFile.mt_Selected    

    TauPtHisto = ROOT.TH1F(FullHistoName+"_TauPt",FullHistoName+"_TauPt",20,0.0,200.0)
    TauEtaHisto = ROOT.TH1F(FullHistoName+"_TauEta",FullHistoName+"_TauEta",45, -2.5, 2.5)
    MuPtHisto  = ROOT.TH1F(FullHistoName+"_MuPt",FullHistoName+"_MuPt",20,20.0,120.0)
    MuEtaHisto = ROOT.TH1F(FullHistoName+"_MuEta",FullHistoName+"_MuEta",48,-2.4,2.4)
    METHisto = ROOT.TH1F(FullHistoName+"_MET",FullHistoName+"_MET",20,0.0,200.0)
    METPhiHisto = ROOT.TH1F(FullHistoName+"_METPhi",FullHistoName+"_METPhi",20,-3.14,3.14)
    mvisHisto = ROOT.TH1F(FullHistoName+"_mvis",FullHistoName+"_mvis",20,0.0,200.0)
    msvHisto = ROOT.TH1F(FullHistoName+"_msv",FullHistoName+"_msv",20,0.0,200.0)
    NJetsHisto = ROOT.TH1F(FullHistoName+"_Njets",FullHistoName+"_Njets",6,0.0,6.0)
    HiggsPtHisto = ROOT.TH1F(FullHistoName+"_HiggsPt",FullHistoName+"_HiggsPt",20,20.0,120.0)
    mjjHisto = ROOT.TH1F(FullHistoName+"_mjj",FullHistoName+"_mjj",20,0.0,500.0)
    LeadingJetEtaHisto = ROOT.TH1F(FullHistoName+"_j1eta",FullHistoName+"_j1eta", 100, -5.0, 5.0)
    LeadingJetPtHisto = ROOT.TH1F(FullHistoName+"_j1pt",FullHistoName+"_j1pt",100,0.0,200.0)
    TriggerHisto = ROOT.TH1F(FullHistoName+"_trigger",FullHistoName+"_trigger",3,0.0,3.0)

    TauPtHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_TauPt",FullHistoName+"_genmatch_low_TauPt",20,0.0,200.0)
    TauEtaHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_TauEta",FullHistoName+"_genmatch_low_TauEta",45, -2.5, 2.5)
    MuPtHisto_DYll  = ROOT.TH1F(FullHistoName+"_genmatch_low_MuPt",FullHistoName+"_genmatch_low_MuPt",20,20.0,120.0)
    MuEtaHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_MuEta",FullHistoName+"_genmatch_low_MuEta",48,-2.4,2.4)
    METHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_MET",FullHistoName+"_genmatch_low_MET",20,0.0,200.0)
    METPhiHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_METPhi",FullHistoName+"_genmatch_low_METPhi",20,-3.14,3.14)
    mvisHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_mvis",FullHistoName+"_genmatch_low_mvis",20,0.0,200.0)
    msvHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_msv",FullHistoName+"_genmatch_low_msv",20,0.0,200.0)
    NJetsHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_Njets",FullHistoName+"_genmatch_low_Njets",6,0.0,6.0)
    HiggsPtHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_HiggsPt",FullHistoName+"_genmatch_low_HiggsPt",20,20.0,120.0)
    mjjHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_mjj",FullHistoName+"_genmatch_low_mjj",20,0.0,500.0)
    LeadingJetEtaHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_j1eta",FullHistoName+"_genmatch_low_j1eta", 100, -5.0, 5.0)
    LeadingJetPtHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_j1pt",FullHistoName+"_genmatch_low_j1pt",100,0.0,200.0)
    TriggerHisto_DYll = ROOT.TH1F(FullHistoName+"_genmatch_low_trigger",FullHistoName+"_genmatch_low_trigger",3,0.0,3.0)

    TauPtHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_TauPt",FullHistoName+"_genmatch_tt_TauPt",20,0.0,200.0)
    TauEtaHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_TauEta",FullHistoName+"_genmatch_tt_TauEta",45, -2.5, 2.5)
    MuPtHisto_DYtt  = ROOT.TH1F(FullHistoName+"_genmatch_tt_MuPt",FullHistoName+"_genmatch_tt_MuPt",20,20.0,120.0)
    MuEtaHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_MuEta",FullHistoName+"_genmatch_tt_MuEta",48,-2.4,2.4)
    METHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_MET",FullHistoName+"_genmatch_tt_MET",20,0.0,200.0)
    METPhiHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_METPhi",FullHistoName+"_genmatch_tt_METPhi",20,-3.14,3.14)
    mvisHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_mvis",FullHistoName+"_genmatch_tt_mvis",20,0.0,200.0)
    msvHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_msv",FullHistoName+"_genmatch_tt_msv",20,0.0,200.0)
    NJetsHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_Njets",FullHistoName+"_genmatch_tt_Njets",6,0.0,6.0)
    HiggsPtHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_HiggsPt",FullHistoName+"_genmatch_tt_HiggsPt",20,20.0,120.0)
    mjjHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_mjj",FullHistoName+"_genmatch_tt_mjj",20,0.0,500.0)
    LeadingJetEtaHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_j1eta",FullHistoName+"_genmatch_tt_j1eta", 100, -5.0, 5.0)
    LeadingJetPtHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_j1pt",FullHistoName+"_genmatch_tt_j1pt",100,0.0,200.0)
    TriggerHisto_DYtt = ROOT.TH1F(FullHistoName+"_genmatch_tt_trigger",FullHistoName+"_genmatch_tt_trigger",3,0.0,3.0)

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)        
        METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        MT = math.sqrt(2.0*MuVector.Pt()*METVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(METVector))))

        if args.Year == "2018":
            Trigger24 = (TheTree.passMu24 and TheTree.matchMu24_1 
                         and TheTree.filterMu24_1 and TheTree.pt_1 > 25.0)
            Trigger27 = (TheTree.passMu27 and TheTree.matchMu27_1 
                         and TheTree.filterMu27_1 and TheTree.pt_1 > 28.0)
            if TheHisto == "Data":
                if (TheTree.run >= 317509): #hps trigger, no filter
                    Trigger2027 = (TheTree.passMu20HPSTau27 
                                   and TheTree.matchMu20HPSTau27_1
                                   and TheTree.matchMu20HPSTau27_2
                                   and TheTree.pt_1 > 21 and TheTree.pt_1 < 25
                                   and TheTree.pt_2 > 28)
                if (TheTree.run < 317509): #non hps trigger, can filter
                    Trigger2027 = (TheTree.passMu20Tau27 
                                   and TheTree.matchMu20Tau27_1
                                   and TheTree.matchMu20Tau27_2
                                   and TheTree.pt_1 > 21 and TheTree.pt_1 < 25
                                   and TheTree.pt_2 > 28
                                   and TheTree.filterMu20Tau27_1
                                   and TheTree.filterMu20Tau27_2)
            elif TheHisto == "Embedded": # embedded doesn't need to match taus.
                Trigger24 = (TheTree.passMu24 and TheTree.matchMu24_1 
                             and TheTree.matchEmbFilter_Mu24_1 and TheTree.pt_1 > 25.0)
                Trigger27 = (TheTree.passMu27 and TheTree.matchMu27_1 
                             and TheTree.matchEmbFilter_Mu27_1 and TheTree.pt_1 > 28.0)            
                Trigger2027 = (TheTree.pt_1 > 21 and TheTree.pt_1 < 25
                               and TheTree.pt_2 > 28
                               and abs(TheTree.eta_1) < 2.1
                               and abs(TheTree.eta_2) < 2.1
                               and TheTree.matchEmbFilter_Mu20Tau27_1
                               and (TheTree.matchEmbFilter_Mu20Tau27_2 or TheTree.matchEmbFilter_Mu20HPSTau27_2))
            else: #all hps cross trigger, ignore HPS filters
                Trigger2027 = (TheTree.passMu20HPSTau27 
                               and TheTree.matchMu20HPSTau27_1
                               and TheTree.matchMu20HPSTau27_2
                               and TheTree.pt_1 > 21 and TheTree.pt_1 < 25
                               and TheTree.pt_2 > 28)                

        elif args.Year == "2017":
            Trigger24 = (TheTree.passMu24 and TheTree.matchMu24_1 
                         and TheTree.filterMu24_1 and TheTree.pt_1 > 25.0)
            Trigger27 = (TheTree.passMu27 and TheTree.matchMu27_1 
                         and TheTree.filterMu27_1 and TheTree.pt_1 > 28.0)
            Trigger2027 = (TheTree.passMu20Tau27 and TheTree.matchMu20Tau27_1 
                           and TheTree.filterMu20Tau27_1                    
                           and TheTree.filterMu20Tau27_2
                           and TheTree.pt_1 > 21 and TheTree.pt_2 > 31 
                           and TheTree.pt_1 < 25
                           and abs(TheTree.eta_2) < 2.1
                           and abs(TheTree.eta_1) < 2.1)
    #no tau trigger matching in embedded
            if(TheHisto == "Embedded"):
                Trigger2027 = (#TheTree.passMu20Tau27 
                               #and TheTree.matchMu20Tau27_1 
                               #and TheTree.filterMu20Tau27_1
                    #and TheTree.pt_1 > 21 and TheTree.pt_2 > 31 
                    TheTree.pt_1 > 21 and TheTree.pt_2 > 31 
                    and TheTree.pt_1 < 25
                    and abs(TheTree.eta_2) < 2.1
                    and abs(TheTree.eta_1 ) 
< 2.1)                
        elif args.Year == "2016":
            Trigger22 = (TheTree.pt_1 >23.0 and abs(TheTree.eta_1)<2.1 
                         and ((TheTree.passMu22eta2p1 and TheTree.matchMu22eta2p1_1 and TheTree.filterMu22eta2p1_1) 
                              or (TheTree.passTkMu22eta2p1 and TheTree.matchTkMu22eta2p1_1 and TheTree.filterTkMu22eta2p1_1)))
            Trigger1920 = (TheTree.pt_1 > 20.0 and TheTree.pt_1 < 23.0 and TheTree.pt_2 > 21.0 
                           and ((TheTree.passMu19Tau20 and TheTree.matchMu19Tau20_1 and TheTree.matchMu19Tau20_2 and TheTree.filterMu19Tau20_1 and TheTree.filterMu19Tau20_2) 
                                or (TheTree.passMu19Tau20SingleL1 and TheTree.matchMu19Tau20SingleL1_1 and TheTree.matchMu19Tau20SingleL1_2 and TheTree.filterMu19Tau20SingleL1_1 and TheTree.filterMu19Tau20SingleL1_2)))
            
        if(MT > 50.0):
            continue        
        
        TheWeighting = TheTree.FinalWeighting        
        if UseFakeFactor:
            TheWeighting = TheWeighting*TheTree.Event_Fake_Factor
        
        TauPtHisto.Fill(TauVector.Pt(),TheWeighting)
        TauEtaHisto.Fill(TauVector.Eta(),TheWeighting)
        MuPtHisto.Fill(MuVector.Pt(),TheWeighting)
        MuEtaHisto.Fill(MuVector.Eta(),TheWeighting)
        METHisto.Fill(TheTree.met,TheWeighting)
        METPhiHisto.Fill(TheTree.metphi,TheWeighting)
        mvisHisto.Fill((TauVector+MuVector).M(),TheWeighting)
        msvHisto.Fill(TheTree.m_sv,TheWeighting)
        NJetsHisto.Fill(TheTree.njets,TheWeighting)
        HiggsPtHisto.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
        mjjHisto.Fill(TheTree.mjj,TheWeighting)
        if TheTree.njets > 0:
            LeadingJetEtaHisto.Fill(TheTree.jeta_1,TheWeighting)
            LeadingJetPtHisto.Fill(TheTree.jpt_1,TheWeighting)
            
        if args.Year == "2018" or args.Year == "2017":
            if Trigger24:
                TriggerHisto.Fill(0,TheWeighting)
            if Trigger27:
                TriggerHisto.Fill(1,TheWeighting)
            if Trigger2027:
                TriggerHisto.Fill(2,TheWeighting)
        else:
            if Trigger22:
                TriggerHisto.Fill(0,TheWeighting)
            if Trigger1920:
                TriggerHisto.Fill(1,TheWeighting)
        
        if args.Year == "2016":
            if (TheHisto == "DY" and TheTree.gen_match_2 <5):
                TauPtHisto_DYll.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYll.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYll.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYll.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYll.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYll.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYll.Fill((TauVector+MuVector).M(),TheWeighting)
                msvHisto_DYll.Fill(TheTree.m_sv,TheWeighting)
                NJetsHisto_DYll.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYll.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYll.Fill(TheTree.mjj,TheWeighting)                
                if TheTree.njets > 0:
                    LeadingJetEtaHisto_DYll.Fill(TheTree.jeta_1,TheWeighting)
                    LeadingJetPtHisto_DYll.Fill(TheTree.jpt_1,TheWeighting)
                if args.Year == "2018" or args.Year == "2017":
                    if Trigger24:
                        TriggerHisto_DYll.Fill(0,TheWeighting)
                    if Trigger27:
                        TriggerHisto_DYll.Fill(1,TheWeighting)
                    if Trigger2027:
                        TriggerHisto_DYll.Fill(2,TheWeighting)
                elif args.Year == "2016":
                    if Trigger22:
                        TriggerHisto_DYll.Fill(0,TheWeighting)
                    if Trigger1920:
                        TriggerHisto_DYll.Fill(1,TheWeighting)

            elif(TheHisto == "DY" and TheTree.gen_match_2 ==5):
                TauPtHisto_DYtt.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYtt.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYtt.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYtt.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYtt.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYtt.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYtt.Fill((TauVector+MuVector).M(),TheWeighting)
                msvHisto_DYtt.Fill(TheTree.m_sv,TheWeighting)
                NJetsHisto_DYtt.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYtt.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYtt.Fill(TheTree.mjj,TheWeighting)
                if TheTree.njets > 0:
                    LeadingJetEtaHisto_DYtt.Fill(TheTree.jeta_1,TheWeighting)
                    LeadingJetPtHisto_DYtt.Fill(TheTree.jpt_1,TheWeighting)
                if args.Year == "2018" or args.Year == "2017":
                    if Trigger24:
                        TriggerHisto_DYtt.Fill(0,TheWeighting)
                    if Trigger27:
                        TriggerHisto_DYtt.Fill(1,TheWeighting)
                    if Trigger2027:
                        TriggerHisto_DYtt.Fill(2,TheWeighting)
                elif args.Year == "2016":
                    if Trigger22:
                        TriggerHisto_DYtt.Fill(0,TheWeighting)
                    if Trigger1920:
                        TriggerHisto_DYtt.Fill(1,TheWeighting)
                            
        elif args.Year == "2018" or args.Year == "2017":
            if (TheHisto == "DY" and TheTree.gen_match_2 <5):
                TauPtHisto_DYll.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYll.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYll.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYll.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYll.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYll.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYll.Fill((TauVector+MuVector).M(),TheWeighting)
                msvHisto_DYll.Fill(TheTree.m_sv,TheWeighting)
                NJetsHisto_DYll.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYll.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYll.Fill(TheTree.mjj,TheWeighting)
                if TheTree.njets > 0:
                    LeadingJetEtaHisto_DYll.Fill(TheTree.jeta_1,TheWeighting)
                    LeadingJetPtHisto_DYll.Fill(TheTree.jpt_1,TheWeighting)
                if Trigger24:
                    TriggerHisto_DYll.Fill(0,TheWeighting)
                if Trigger27:
                    TriggerHisto_DYll.Fill(1,TheWeighting)
                if Trigger2027:
                    TriggerHisto_DYll.Fill(2,TheWeighting)

            elif TheHisto == "Embedded":
                TauPtHisto_DYtt.Fill(TauVector.Pt(),TheWeighting)
                TauEtaHisto_DYtt.Fill(TauVector.Eta(),TheWeighting)
                MuPtHisto_DYtt.Fill(MuVector.Pt(),TheWeighting)
                MuEtaHisto_DYtt.Fill(MuVector.Eta(),TheWeighting)
                METHisto_DYtt.Fill(TheTree.met,TheWeighting)
                METPhiHisto_DYtt.Fill(TheTree.metphi,TheWeighting)
                mvisHisto_DYtt.Fill((TauVector+MuVector).M(),TheWeighting)
                msvHisto_DYtt.Fill(TheTree.m_sv,TheWeighting)
                NJetsHisto_DYtt.Fill(TheTree.njets,TheWeighting)
                HiggsPtHisto_DYtt.Fill((TauVector+MuVector+METVector).Pt(),TheWeighting)
                mjjHisto_DYtt.Fill(TheTree.mjj,TheWeighting)
                if TheTree.njets > 0:
                    LeadingJetEtaHisto_DYtt.Fill(TheTree.jeta_1,TheWeighting)
                    LeadingJetPtHisto_DYtt.Fill(TheTree.jpt_1,TheWeighting)
                if Trigger24:
                    TriggerHisto_DYtt.Fill(0,TheWeighting)
                if Trigger27:
                    TriggerHisto_DYtt.Fill(1,TheWeighting)
                if Trigger2027:
                    TriggerHisto_DYtt.Fill(2,TheWeighting)

    OutFile.cd()
    TauPtHisto.Write()
    TauEtaHisto.Write()
    MuPtHisto.Write()
    MuEtaHisto.Write()
    METHisto.Write()
    METPhiHisto.Write()
    mvisHisto.Write()
    msvHisto.Write()
    NJetsHisto.Write()
    HiggsPtHisto.Write()
    mjjHisto.Write()
    LeadingJetEtaHisto.Write()
    LeadingJetPtHisto.Write()
    TriggerHisto.Write()

    if args.Year == "2016":        
        if(TheHisto == "DY"):
            TauPtHisto_DYll.Write()
            TauEtaHisto_DYll.Write()
            MuPtHisto_DYll.Write()
            MuEtaHisto_DYll.Write()
            METHisto_DYll.Write()
            METPhiHisto_DYll.Write()
            mvisHisto_DYll.Write()
            msvHisto_DYll.Write()
            NJetsHisto_DYll.Write()
            HiggsPtHisto_DYll.Write()
            mjjHisto_DYll.Write()
            LeadingJetEtaHisto_DYll.Write()
            LeadingJetPtHisto_DYll.Write()
            TriggerHisto_DYll.Write()
            
            TauPtHisto_DYtt.Write()
            TauEtaHisto_DYtt.Write()
            MuPtHisto_DYtt.Write()
            MuEtaHisto_DYtt.Write()
            METHisto_DYtt.Write()
            METPhiHisto_DYtt.Write()
            mvisHisto_DYtt.Write()
            msvHisto_DYtt.Write()
            NJetsHisto_DYtt.Write()
            HiggsPtHisto_DYtt.Write()
            mjjHisto_DYtt.Write()
            LeadingJetEtaHisto_DYtt.Write()
            LeadingJetPtHisto_DYtt.Write()
            TriggerHisto_DYtt.Write()

    if args.Year == "2018" or args.Year == "2017":        
        if TheHisto == "Embedded":
            TauPtHisto_DYtt.Write()
            TauEtaHisto_DYtt.Write()
            MuPtHisto_DYtt.Write()
            MuEtaHisto_DYtt.Write()
            METHisto_DYtt.Write()
            METPhiHisto_DYtt.Write()
            mvisHisto_DYtt.Write()
            msvHisto_DYtt.Write()
            NJetsHisto_DYtt.Write()
            HiggsPtHisto_DYtt.Write()
            mjjHisto_DYtt.Write()
            LeadingJetEtaHisto_DYtt.Write()
            LeadingJetPtHisto_DYtt.Write()
            TriggerHisto_DYtt.Write()

        elif TheHisto == "DY":
            TauPtHisto_DYll.Write()
            TauEtaHisto_DYll.Write()
            MuPtHisto_DYll.Write()
            MuEtaHisto_DYll.Write()
            METHisto_DYll.Write()
            METPhiHisto_DYll.Write()
            mvisHisto_DYll.Write()
            msvHisto_DYll.Write()
            NJetsHisto_DYll.Write()
            HiggsPtHisto_DYll.Write()
            mjjHisto_DYll.Write()
            LeadingJetEtaHisto_DYll.Write()
            LeadingJetPtHisto_DYll.Write()
            TriggerHisto_DYll.Write()            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate control plots.")
    parser.add_argument('Year',choices=["2016","2017","2018"],help="Select which year's plots to generate.")
    parser.add_argument('Files',nargs="+",help="List of files to generate control plots from.")
    parser.add_argument('--UseFakeFactorOnFiles',nargs="+",help="Use the file's fake factor weightings when making plots for these files.")
    
    args = parser.parse_args()

    OutFile = ROOT.TFile("TemporaryFiles/ControlRegion_"+args.Year+".root","RECREATE")
        
    for File in args.Files:
        print("Making control plots for: "+File)
        GenerateControlPlots(File,OutFile,args)
