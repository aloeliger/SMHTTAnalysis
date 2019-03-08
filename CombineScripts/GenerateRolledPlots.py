import ROOT
import sys
from tqdm import tqdm
from array import array
import argparse

def GenerateRolledPlots(File,args):
    
    InputFile = ROOT.TFile(File)
    TheTree = InputFile.mt_Selected

    SampleName = File[File.rfind("/")+1:]
    SampleName = SampleName.split(".")[0]
    
    ResultFile = ROOT.TFile("Results.root","UPDATE")

    ZeroJetHistoName = SampleName+"_0jet"
    if(args.UseFakeFactor):
        ZeroJetHistoName = ZeroJetHistoName+"_Fake"
    ZeroJetHistoName = ZeroJetHistoName+"_Results_Rolled"
    
    if ResultFile.GetDirectory("mt_0jet") != None:
        mt_0jetDir = ResultFile.GetDirectory("mt_0jet")
    else:
        mt_0jetDir = ResultFile.mkdir("mt_0jet")
    TauPtBinning = array('d',[30.0,35.0,40.0,50.0,5000.0])
    nTauPtBins = len(TauPtBinning)-1
    ZeroJetResultsRolled = ROOT.TH2F(ZeroJetHistoName,ZeroJetHistoName,20,50.0,150.0, nTauPtBins,TauPtBinning)

    BoostedHistoName = SampleName+"_boosted"
    if(args.UseFakeFactor):
        BoostedHistoName = BoostedHistoName+"_Fake"
    BoostedHistoName = BoostedHistoName+"_Results_Rolled"

    if ResultFile.GetDirectory("mt_boosted") != None:
        mt_boostedDir = ResultFile.GetDirectory("mt_boosted")
    else:
        mt_boostedDir = ResultFile.mkdir("mt_boosted")
    HiggsPtBinning = array('d',[0.0, 30.0, 60.0, 100.0, 150.0, 9000.0])
    nHPtBins = len(HiggsPtBinning)-1
    BoostedResultsRolled = ROOT.TH2F(BoostedHistoName,BoostedHistoName,20,50.0,150.0,nHPtBins,HiggsPtBinning)

    VBFHistoName = SampleName+"_vbf"
    if(args.UseFakeFactor):
        VBFHistoName = VBFHistoName+"_Fake"
    VBFHistoName = VBFHistoName+"_Results_Rolled"

    if ResultFile.GetDirectory("mt_vbf") != None:
        mt_vbfDir = ResultFile.GetDirectory("mt_vbf")
    else:
        mt_vbfDir = ResultFile.mkdir("mt_vbf")
    mjjBinning = array('d',[0.0,100.0,200.0,300.0,9000.0])
    nmjjBins = len(mjjBinning)-1
    VBFResultsRolled = ROOT.TH2F(VBFHistoName,VBFHistoName,20,50.0,150.0,nmjjBins,mjjBinning)

    #uncertainties
    #fake factor shapes
    if args.UseFakeFactor:
        #ZeroJet
        ZeroJet_ff_qcd_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_mt_systUp",
                                        ZeroJetHistoName+"_CMS_ff_qcd_mt_systUp",
                                        20,50.0,150.0,
                                        nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_mt_systDown",
                                          ZeroJetHistoName+"_CMS_ff_qcd_mt_systDown",
                                          20,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    20,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      20,50.0,150.0,
                                                      nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    20,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      20,50.0,150.0,
                                                      nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_njet1_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_njet1_statUp",
                                                ZeroJetHistoName+"_CMS_ff_tt_njet1_statUp",
                                                20,50.0,150.0,
                                                nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_njet1_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  ZeroJetHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  20,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_systUp",
                                          ZeroJetHistoName+"_CMS_ff_tt_systUp",
                                          20,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_systDown",
                                            ZeroJetHistoName+"_CMS_ff_tt_systDown",
                                            20,50.0,150.0,
                                            nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet0_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  20,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    20,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet1_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  20,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    20,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_systUp",
                                         ZeroJetHistoName+"_CMS_ff_w_systUp",
                                         20,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_systDown",
                                           ZeroJetHistoName+"_CMS_ff_w_systDown",
                                           20,50.0,150.0,
                                           nTauPtBins,TauPtBinning)
        #Boosted
        Boosted_ff_qcd_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_mt_systUp",
                                        BoostedHistoName+"_CMS_ff_qcd_mt_systUp",
                                        20,50.0,150.0,
                                        nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_mt_systDown",
                                          BoostedHistoName+"_CMS_ff_qcd_mt_systDown",
                                          20,50.0,150.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    20,50.0,150.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      20,50.0,150.0,
                                                      nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                      BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                      20,50.0,150.0,
                                                      nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      20,50.0,150.0,
                                                      nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_njet1_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_njet1_statUp",
                                                BoostedHistoName+"_CMS_ff_tt_njet1_statUp",
                                                20,50.0,150.0,
                                                nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_njet1_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  BoostedHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  20,50.0,150.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_systUp",
                                          BoostedHistoName+"_CMS_ff_tt_systUp",
                                          20,50.0,150.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_systDown",
                                            BoostedHistoName+"_CMS_ff_tt_systDown",
                                            20,50.0,150.0,
                                            nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet0_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  BoostedHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  20,50.0,150.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    BoostedHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    20,50.0,150.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet1_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  BoostedHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  20,50.0,150.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    BoostedHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    20,50.0,150.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_w_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_systUp",
                                         BoostedHistoName+"_CMS_ff_w_systUp",
                                         20,50.0,150.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_ff_w_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_systDown",
                                           BoostedHistoName+"_CMS_ff_w_systDown",
                                           20,50.0,150.0,
                                           nHPtBins,HiggsPtBinning)
        #VBF
        VBF_ff_qcd_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_mt_systUp",
                                       VBFHistoName+"_CMS_ff_qcd_mt_systUp",
                                       20,50.0,150.0,
                                       nmjjBins,mjjBinning)
        VBF_ff_qcd_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_mt_systDown",
                                         VBFHistoName+"_CMS_ff_qcd_mt_systDown",
                                         20,50.0,150.0,
                                         nmjjBins,mjjBinning)
        VBF_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                VBFHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                20,50.0,150.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                  VBFHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                  20,50.0,150.0,
                                                  nmjjBins,mjjBinning)
        VBF_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                VBFHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                20,50.0,150.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                  VBFHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                  20,50.0,150.0,
                                                  nmjjBins,mjjBinning)
        VBF_ff_tt_njet1_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_njet1_statUp",
                                            VBFHistoName+"_CMS_ff_tt_njet1_statUp",
                                            20,50.0,150.0,
                                            nmjjBins,mjjBinning)
        VBF_ff_tt_njet1_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_njet1_statDown",
                                              VBFHistoName+"_CMS_ff_tt_njet1_statDown",
                                              20,50.0,150.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_tt_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_systUp",
                                      VBFHistoName+"_CMS_ff_tt_systUp",
                                      20,50.0,150.0,
                                      nmjjBins,mjjBinning)
        VBF_ff_tt_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_systDown",
                                        VBFHistoName+"_CMS_ff_tt_systDown",
                                        20,50.0,150.0,
                                        nmjjBins,mjjBinning)
        VBF_ff_w_njet0_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                              VBFHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                              20,50.0,150.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                VBFHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                20,50.0,150.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_w_njet1_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                              VBFHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                              20,50.0,150.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                VBFHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                20,50.0,150.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_w_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_systUp",
                                     VBFHistoName+"_CMS_ff_w_systUp",
                                     20,50.0,150.0,
                                     nmjjBins,mjjBinning)
        VBF_ff_w_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_systDown",
                                       VBFHistoName+"_CMS_ff_w_systDown",
                                       20,50.0,150.0,
                                       nmjjBins,mjjBinning)
    #TES shapes
    if args.UseTES:
        ZeroJet_DM0_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prongUp",
                                       ZeroJetHistoName+"_scale_t_1prongUp",
                                       20,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM1_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prong1pizeroUp",
                                       ZeroJetHistoName+"_scale_t_1prong1pizeroUp",
                                       20,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM10_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_3prongUp",
                                        ZeroJetHistoName+"_scale_t_3prongUp",
                                        20,50.0,150.0,
                                        nTauPtBins,TauPtBinning)
        ZeroJet_DM0_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prongDown",
                                         ZeroJetHistoName+"_scale_t_1prongDown",
                                         20,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_DM1_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prong1pizeroDown",
                                       ZeroJetHistoName+"_scale_t_1prong1pizeroDown",
                                       20,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM10_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_3prongDown",
                                          ZeroJetHistoName+"_scale_t_3prongDown",
                                          20,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        
        Boosted_DM0_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_1prongUp",
                                       BoostedHistoName+"_scale_t_1prongUp",
                                       20,50.0,150.0,
                                       nHPtBins,HiggsPtBinning)
        Boosted_DM1_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_1prong1pizeroUp",
                                       BoostedHistoName+"_scale_t_1prong1pizeroUp",
                                       20,50.0,150.0,
                                       nHPtBins,HiggsPtBinning)
        Boosted_DM10_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_3prongUp",
                                        BoostedHistoName+"_scale_t_3prongUp",
                                        20,50.0,150.0,
                                        nHPtBins,HiggsPtBinning)
        Boosted_DM0_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_1prongDown",
                                         BoostedHistoName+"_scale_t_1prongDown",
                                         20,50.0,150.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_DM1_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_1prong1pizeroDown",
                                         BoostedHistoName+"_scale_t_1prong1pizeroDown",
                                         20,50.0,150.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_DM10_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_3prongDown",
                                          BoostedHistoName+"_scale_t_3prongDown",
                                          20,50.0,150.0,
                                          nHPtBins,HiggsPtBinning)
        VBF_DM0_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_1prongUp",
                                   VBFHistoName+"_scale_t_1prongUp",
                                   20,50.0,150.0,
                                   nmjjBins,mjjBinning)
        VBF_DM1_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_1prong1pizeroUp",
                                   VBFHistoName+"_scale_t_1prong1pizeroUp",
                                   20,50.0,150.0,
                                   nmjjBins,mjjBinning)
        VBF_DM10_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_3prongUp",
                                    VBFHistoName+"_scale_t_3prongUp",
                                    20,50.0,150.0,
                                    nmjjBins,mjjBinning)
        VBF_DM0_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_1prongDown",
                                     VBFHistoName+"_scale_t_1prongDown",
                                     20,50.0,150.0,
                                     nmjjBins,mjjBinning)
        VBF_DM1_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_1prong1pizeroDown",
                                     VBFHistoName+"_scale_t_1prong1pizeroDown",
                                     20,50.0,150.0,
                                     nmjjBins,mjjBinning)
        VBF_DM10_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_3prongDown",
                                      VBFHistoName+"_scale_t_3prongDown",
                                      20,50.0,150.0,
                                      nmjjBins,mjjBinning)
        

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TheWeight = TheTree.FinalWeighting
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        if args.UseFakeFactor:
            TheWeight = TheWeight*TheTree.Event_Fake_Factor

        if TheTree.njets == 0:
            ZeroJetResultsRolled.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheWeight)
            #Handle Uncertainties
            if args.UseFakeFactor:
                ZeroJet_ff_qcd_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_up)
                ZeroJet_ff_qcd_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_down)
                ZeroJet_ff_qcd_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_up)
                ZeroJet_ff_qcd_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_down)
                ZeroJet_ff_qcd_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_up)
                ZeroJet_ff_qcd_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_down)
                ZeroJet_ff_tt_njet1_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_up)
                ZeroJet_ff_tt_njet1_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_down)
                ZeroJet_ff_tt_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_up)
                ZeroJet_ff_tt_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_down)
                ZeroJet_ff_w_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_up)
                ZeroJet_ff_w_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_down)
                ZeroJet_ff_w_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_up)
                ZeroJet_ff_w_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_down)
                ZeroJet_ff_w_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_up)
                ZeroJet_ff_w_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_down)
            if args.UseTES:
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiM(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                CorrectedTauVector_DOWN.SetPtEtaPhiM(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                if(TheTree.l2_decayMode == 0):
                    ZeroJet_DM0_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM0_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 1):
                    ZeroJet_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    ZeroJet_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 10):
                    ZeroJet_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM10_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    ZeroJet_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    ZeroJet_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
        
        elif TheTree.njets == 1:
            BoostedResultsRolled.Fill((MuVector+TauVector).M(),(MuVector+TauVector).Pt(),TheWeight)
            #Handle Uncertainties
            if args.UseFakeFactor:
                Boosted_ff_qcd_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_up)
                Boosted_ff_qcd_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_down)
                Boosted_ff_qcd_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_up)
                Boosted_ff_qcd_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_down)
                Boosted_ff_qcd_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_up)
                Boosted_ff_qcd_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_down)
                Boosted_ff_tt_njet1_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_up)
                Boosted_ff_tt_njet1_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_down)
                Boosted_ff_tt_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_up)
                Boosted_ff_tt_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_down)
                Boosted_ff_w_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_up)
                Boosted_ff_w_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_down)
                Boosted_ff_w_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_up)
                Boosted_ff_w_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_down)
                Boosted_ff_w_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_up)
                Boosted_ff_w_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_down)
            if args.UseTES:
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiM(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                CorrectedTauVector_DOWN.SetPtEtaPhiM(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                if(TheTree.l2_decayMode == 0):
                    Boosted_DM0_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM0_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 1):
                    Boosted_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    Boosted_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 10):
                    Boosted_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM10_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    Boosted_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    Boosted_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
            
        elif TheTree.njets == 2:
            VBFResultsRolled.Fill((MuVector+TauVector).M(),TheTree.mjj,TheWeight)
            #Handle Uncertainties
            if args.UseFakeFactor:
                VBF_ff_qcd_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_up)
                VBF_ff_qcd_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_down)
                VBF_ff_qcd_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_up)
                VBF_ff_qcd_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_down)
                VBF_ff_qcd_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_up)
                VBF_ff_qcd_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_down)
                VBF_ff_tt_njet1_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_up)
                VBF_ff_tt_njet1_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_down)
                VBF_ff_tt_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_up)
                VBF_ff_tt_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_down)
                VBF_ff_w_njet0_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_up)
                VBF_ff_w_njet0_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_down)
                VBF_ff_w_njet1_mt_stat_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_up)
                VBF_ff_w_njet1_mt_stat_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_down)
                VBF_ff_w_syst_UP.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_up)
                VBF_ff_w_syst_DOWN.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_down)
            if args.UseTES:
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiM(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                CorrectedTauVector_DOWN.SetPtEtaPhiM(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
                if(TheTree.l2_decayMode == 0):
                    VBF_DM0_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    VBF_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM0_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 1):
                    VBF_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    VBF_DM10_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    
                elif(TheTree.l2_decayMode == 10):
                    VBF_DM0_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_UP.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM10_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),TheWeight)
                    VBF_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TheWeight)
                    VBF_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),TheWeight)

    mt_0jetDir.cd()
    ZeroJetResultsRolled.Write()
    #Write shape uncertainties
    if args.UseFakeFactor:
        ZeroJet_ff_qcd_syst_UP.Write()
        ZeroJet_ff_qcd_syst_DOWN.Write()
        ZeroJet_ff_qcd_njet0_mt_stat_UP.Write()
        ZeroJet_ff_qcd_njet0_mt_stat_DOWN.Write()
        ZeroJet_ff_qcd_njet1_mt_stat_UP.Write()
        ZeroJet_ff_qcd_njet1_mt_stat_DOWN.Write()
        ZeroJet_ff_tt_njet1_stat_UP.Write()
        ZeroJet_ff_tt_njet1_stat_DOWN.Write()
        ZeroJet_ff_tt_syst_UP.Write()
        ZeroJet_ff_tt_syst_DOWN.Write()
        ZeroJet_ff_w_njet0_mt_stat_UP.Write()
        ZeroJet_ff_w_njet0_mt_stat_DOWN.Write()
        ZeroJet_ff_w_njet1_mt_stat_UP.Write()
        ZeroJet_ff_w_njet1_mt_stat_DOWN.Write()
        ZeroJet_ff_w_syst_UP.Write()
        ZeroJet_ff_w_syst_DOWN.Write()
    if args.UseTES:
        ZeroJet_DM0_TES_UP.Write()
        ZeroJet_DM1_TES_UP.Write()
        ZeroJet_DM10_TES_UP.Write()
        ZeroJet_DM0_TES_DOWN.Write()
        ZeroJet_DM1_TES_DOWN.Write()
        ZeroJet_DM10_TES_DOWN.Write()

    mt_boostedDir.cd()
    BoostedResultsRolled.Write()
    #Write shape uncertainties
    if args.UseFakeFactor:
        Boosted_ff_qcd_syst_UP.Write()
        Boosted_ff_qcd_syst_DOWN.Write()
        Boosted_ff_qcd_njet0_mt_stat_UP.Write()
        Boosted_ff_qcd_njet0_mt_stat_DOWN.Write()
        Boosted_ff_qcd_njet1_mt_stat_UP.Write()
        Boosted_ff_qcd_njet1_mt_stat_DOWN.Write()
        Boosted_ff_tt_njet1_stat_UP.Write()
        Boosted_ff_tt_njet1_stat_DOWN.Write()
        Boosted_ff_tt_syst_UP.Write()
        Boosted_ff_tt_syst_DOWN.Write()
        Boosted_ff_w_njet0_mt_stat_UP.Write()
        Boosted_ff_w_njet0_mt_stat_DOWN.Write()
        Boosted_ff_w_njet1_mt_stat_UP.Write()
        Boosted_ff_w_njet1_mt_stat_DOWN.Write()
        Boosted_ff_w_syst_UP.Write()
        Boosted_ff_w_syst_DOWN.Write()
    if args.UseTES:
        Boosted_DM0_TES_UP.Write()
        Boosted_DM1_TES_UP.Write()
        Boosted_DM10_TES_UP.Write()
        Boosted_DM0_TES_DOWN.Write()
        Boosted_DM1_TES_DOWN.Write()
        Boosted_DM10_TES_DOWN.Write()
    
    mt_vbfDir.cd()
    VBFResultsRolled.Write()
    #Write Shape Uncertainties
    if args.UseFakeFactor:
        VBF_ff_qcd_syst_UP.Write()
        VBF_ff_qcd_syst_DOWN.Write()
        VBF_ff_qcd_njet0_mt_stat_UP.Write()
        VBF_ff_qcd_njet0_mt_stat_DOWN.Write()
        VBF_ff_qcd_njet1_mt_stat_UP.Write()
        VBF_ff_qcd_njet1_mt_stat_DOWN.Write()
        VBF_ff_tt_njet1_stat_UP.Write()
        VBF_ff_tt_njet1_stat_DOWN.Write()
        VBF_ff_tt_syst_UP.Write()
        VBF_ff_tt_syst_DOWN.Write()
        VBF_ff_w_njet0_mt_stat_UP.Write()
        VBF_ff_w_njet0_mt_stat_DOWN.Write()
        VBF_ff_w_njet1_mt_stat_UP.Write()
        VBF_ff_w_njet1_mt_stat_DOWN.Write()
        VBF_ff_w_syst_UP.Write()
        VBF_ff_w_syst_DOWN.Write()
    if args.UseTES:
        VBF_DM0_TES_UP.Write()
        VBF_DM1_TES_UP.Write()
        VBF_DM10_TES_UP.Write()
        VBF_DM0_TES_DOWN.Write()
        VBF_DM1_TES_DOWN.Write()
        VBF_DM10_TES_DOWN.Write()
    
    ResultFile.Write()
    ResultFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate rolled plots to be unrolled and fed to Combine.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's plots are to be made")
    parser.add_argument('Files',nargs="+",help = "Files to run the tool on")
    parser.add_argument('--UseFakeFactor',help = "Use the file's fake factor weighting when making plots for this file.", action="store_true")
    parser.add_argument('--UseTES',help="Create the TES Uncertainty plots on these files",action="store_true")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing RolledHistograms for"+str(File))
        GenerateRolledPlots(File,args)
        
