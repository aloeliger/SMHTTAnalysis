import ROOT
import sys
from tqdm import tqdm
from array import array
import argparse
import math

def CalculateMT(MuonVector,METVector):
    return math.sqrt(2.0*MuonVector.Pt()*METVector.Pt()*(1.0-math.cos(MuonVector.DeltaPhi(METVector))))

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
    TauPtBinning = array('d',[30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  2000.0])
    nTauPtBins = len(TauPtBinning)-1
    nZeroJetMassBins = int(args.numZeroJetBins)
    ZeroJetResultsRolled = ROOT.TH2F(ZeroJetHistoName,ZeroJetHistoName,nZeroJetMassBins,50.0,150.0, nTauPtBins,TauPtBinning)

    BoostedHistoName = SampleName+"_boosted"
    if(args.UseFakeFactor):
        BoostedHistoName = BoostedHistoName+"_Fake"
    BoostedHistoName = BoostedHistoName+"_Results_Rolled"

    if ResultFile.GetDirectory("mt_boosted") != None:
        mt_boostedDir = ResultFile.GetDirectory("mt_boosted")
    else:
        mt_boostedDir = ResultFile.mkdir("mt_boosted")
    HiggsPtBinning = array('d',[0.0, 100.0, 170.0, 300.0, 9000.0])
    nHPtBins = len(HiggsPtBinning)-1
    nBoostedMassBins=int(args.numBoostedBins)
    BoostedResultsRolled = ROOT.TH2F(BoostedHistoName,BoostedHistoName,nBoostedMassBins,50.0,250.0,nHPtBins,HiggsPtBinning)

    VBFHistoName = SampleName+"_vbf"
    if(args.UseFakeFactor):
        VBFHistoName = VBFHistoName+"_Fake"
    VBFHistoName = VBFHistoName+"_Results_Rolled"

    if ResultFile.GetDirectory("mt_vbf") != None:
        mt_vbfDir = ResultFile.GetDirectory("mt_vbf")
    else:
        mt_vbfDir = ResultFile.mkdir("mt_vbf")
    mjjBinning = array('d',[300.0, 700.0, 1100.0, 1500.0, 9000.0])
    nmjjBins = len(mjjBinning)-1
    nVBFMassBins = int(args.numVBFBins)
    VBFResultsRolled = ROOT.TH2F(VBFHistoName,VBFHistoName,nVBFMassBins,50.0,250.0,nmjjBins,mjjBinning)

    #uncertainties
    #fake factor shapes
    if args.UseFakeFactor:
        #ZeroJet
        ZeroJet_ff_qcd_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_mt_systUp",
                                           ZeroJetHistoName+"_CMS_ff_qcd_mt_systUp",
                                           nZeroJetMassBins,50.0,150.0,
                                           nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_mt_systDown",
                                             ZeroJetHistoName+"_CMS_ff_qcd_mt_systDown",
                                             nZeroJetMassBins,50.0,150.0,
                                             nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      ZeroJetHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      nZeroJetMassBins,50.0,150.0,
                                                      nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      ZeroJetHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      nZeroJetMassBins,50.0,150.0,
                                                      nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_njet1_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_njet1_statUp",
                                                ZeroJetHistoName+"_CMS_ff_tt_njet1_statUp",
                                                nZeroJetMassBins,50.0,150.0,
                                                nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_njet1_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  ZeroJetHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_systUp",
                                          ZeroJetHistoName+"_CMS_ff_tt_systUp",
                                          nZeroJetMassBins,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_ff_tt_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_tt_systDown",
                                            ZeroJetHistoName+"_CMS_ff_tt_systDown",
                                            nZeroJetMassBins,50.0,150.0,
                                            nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet0_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    ZeroJetHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet1_mt_stat_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    ZeroJetHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_syst_UP = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_systUp",
                                         ZeroJetHistoName+"_CMS_ff_w_systUp",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_ff_w_syst_DOWN = ROOT.TH2F(ZeroJetHistoName+"_CMS_ff_w_systDown",
                                           ZeroJetHistoName+"_CMS_ff_w_systDown",
                                           nZeroJetMassBins,50.0,150.0,
                                           nTauPtBins,TauPtBinning)
        #Boosted
        Boosted_ff_qcd_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_mt_systUp",
                                           BoostedHistoName+"_CMS_ff_qcd_mt_systUp",
                                           nBoostedMassBins,50.0,250.0,
                                           nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_mt_systDown",
                                             BoostedHistoName+"_CMS_ff_qcd_mt_systDown",
                                             nBoostedMassBins,50.0,250.0,
                                             nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      BoostedHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                      nBoostedMassBins,50.0,250.0,
                                                      nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      BoostedHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                      nBoostedMassBins,50.0,250.0,
                                                      nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_njet1_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_njet1_statUp",
                                                BoostedHistoName+"_CMS_ff_tt_njet1_statUp",
                                                nBoostedMassBins,50.0,250.0,
                                                nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_njet1_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  BoostedHistoName+"_CMS_ff_tt_njet1_statDown",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_systUp",
                                          BoostedHistoName+"_CMS_ff_tt_systUp",
                                          nBoostedMassBins,50.0,250.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_ff_tt_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_tt_systDown",
                                            BoostedHistoName+"_CMS_ff_tt_systDown",
                                            nBoostedMassBins,50.0,250.0,
                                            nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet0_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  BoostedHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    BoostedHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet1_mt_stat_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  BoostedHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    BoostedHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_ff_w_syst_UP = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_systUp",
                                         BoostedHistoName+"_CMS_ff_w_systUp",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_ff_w_syst_DOWN = ROOT.TH2F(BoostedHistoName+"_CMS_ff_w_systDown",
                                           BoostedHistoName+"_CMS_ff_w_systDown",
                                           nBoostedMassBins,50.0,250.0,
                                           nHPtBins,HiggsPtBinning)
        #VBF
        VBF_ff_qcd_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_mt_systUp",
                                       VBFHistoName+"_CMS_ff_qcd_mt_systUp",
                                       nVBFMassBins,50.0,250.0,
                                       nmjjBins,mjjBinning)
        VBF_ff_qcd_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_mt_systDown",
                                         VBFHistoName+"_CMS_ff_qcd_mt_systDown",
                                         nVBFMassBins,50.0,250.0,
                                         nmjjBins,mjjBinning)
        VBF_ff_qcd_njet0_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                VBFHistoName+"_CMS_ff_qcd_njet0_mt_statUp",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_qcd_njet0_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                  VBFHistoName+"_CMS_ff_qcd_njet0_mt_statDown",
                                                  nVBFMassBins,50.0,250.0,
                                                  nmjjBins,mjjBinning)
        VBF_ff_qcd_njet1_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                VBFHistoName+"_CMS_ff_qcd_njet1_mt_statUp",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_qcd_njet1_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                  VBFHistoName+"_CMS_ff_qcd_njet1_mt_statDown",
                                                  nVBFMassBins,50.0,250.0,
                                                  nmjjBins,mjjBinning)
        VBF_ff_tt_njet1_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_njet1_statUp",
                                            VBFHistoName+"_CMS_ff_tt_njet1_statUp",
                                            nVBFMassBins,50.0,250.0,
                                            nmjjBins,mjjBinning)
        VBF_ff_tt_njet1_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_njet1_statDown",
                                              VBFHistoName+"_CMS_ff_tt_njet1_statDown",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_tt_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_systUp",
                                      VBFHistoName+"_CMS_ff_tt_systUp",
                                      nVBFMassBins,50.0,250.0,
                                      nmjjBins,mjjBinning)
        VBF_ff_tt_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_tt_systDown",
                                        VBFHistoName+"_CMS_ff_tt_systDown",
                                        nVBFMassBins,50.0,250.0,
                                        nmjjBins,mjjBinning)
        VBF_ff_w_njet0_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                              VBFHistoName+"_CMS_ff_w_njet0_mt_statUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_w_njet0_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                VBFHistoName+"_CMS_ff_w_njet0_mt_statDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_w_njet1_mt_stat_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                              VBFHistoName+"_CMS_ff_w_njet1_mt_statUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_ff_w_njet1_mt_stat_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                VBFHistoName+"_CMS_ff_w_njet1_mt_statDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_ff_w_syst_UP = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_systUp",
                                     VBFHistoName+"_CMS_ff_w_systUp",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)
        VBF_ff_w_syst_DOWN = ROOT.TH2F(VBFHistoName+"_CMS_ff_w_systDown",
                                       VBFHistoName+"_CMS_ff_w_systDown",
                                       nVBFMassBins,50.0,250.0,
                                       nmjjBins,mjjBinning)
    #TES shapes
    if args.UseTES:
        ZeroJet_DM0_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prongUp",
                                       ZeroJetHistoName+"_scale_t_1prongUp",
                                       nZeroJetMassBins,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM1_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prong1pizeroUp",
                                       ZeroJetHistoName+"_scale_t_1prong1pizeroUp",
                                       nZeroJetMassBins,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM10_TES_UP = ROOT.TH2F(ZeroJetHistoName+"_scale_t_3prongUp",
                                        ZeroJetHistoName+"_scale_t_3prongUp",
                                        nZeroJetMassBins,50.0,150.0,
                                        nTauPtBins,TauPtBinning)
        ZeroJet_DM0_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prongDown",
                                         ZeroJetHistoName+"_scale_t_1prongDown",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_DM1_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_1prong1pizeroDown",
                                         ZeroJetHistoName+"_scale_t_1prong1pizeroDown",
                                         nZeroJetMassBins,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DM10_TES_DOWN = ROOT.TH2F(ZeroJetHistoName+"_scale_t_3prongDown",
                                          ZeroJetHistoName+"_scale_t_3prongDown",
                                          nZeroJetMassBins,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        
        Boosted_DM0_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_1prongUp",
                                       BoostedHistoName+"_scale_t_1prongUp",
                                       nBoostedMassBins,50.0,250.0,
                                       nHPtBins,HiggsPtBinning)
        Boosted_DM1_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_1prong1pizeroUp",
                                       BoostedHistoName+"_scale_t_1prong1pizeroUp",
                                       nBoostedMassBins,50.0,250.0,
                                       nHPtBins,HiggsPtBinning)
        Boosted_DM10_TES_UP = ROOT.TH2F(BoostedHistoName+"_scale_t_3prongUp",
                                        BoostedHistoName+"_scale_t_3prongUp",
                                        nBoostedMassBins,50.0,250.0,
                                        nHPtBins,HiggsPtBinning)
        Boosted_DM0_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_1prongDown",
                                         BoostedHistoName+"_scale_t_1prongDown",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_DM1_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_1prong1pizeroDown",
                                         BoostedHistoName+"_scale_t_1prong1pizeroDown",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_DM10_TES_DOWN = ROOT.TH2F(BoostedHistoName+"_scale_t_3prongDown",
                                          BoostedHistoName+"_scale_t_3prongDown",
                                          nBoostedMassBins,50.0,250.0,
                                          nHPtBins,HiggsPtBinning)
        VBF_DM0_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_1prongUp",
                                   VBFHistoName+"_scale_t_1prongUp",
                                   nVBFMassBins,50.0,250.0,
                                   nmjjBins,mjjBinning)
        VBF_DM1_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_1prong1pizeroUp",
                                   VBFHistoName+"_scale_t_1prong1pizeroUp",
                                   nVBFMassBins,50.0,250.0,
                                   nmjjBins,mjjBinning)
        VBF_DM10_TES_UP = ROOT.TH2F(VBFHistoName+"_scale_t_3prongUp",
                                    VBFHistoName+"_scale_t_3prongUp",
                                    nVBFMassBins,50.0,250.0,
                                    nmjjBins,mjjBinning)
        VBF_DM0_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_1prongDown",
                                     VBFHistoName+"_scale_t_1prongDown",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)
        VBF_DM1_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_1prong1pizeroDown",
                                     VBFHistoName+"_scale_t_1prong1pizeroDown",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)
        VBF_DM10_TES_DOWN = ROOT.TH2F(VBFHistoName+"_scale_t_3prongDown",
                                      VBFHistoName+"_scale_t_3prongDown",
                                      nVBFMassBins,50.0,250.0,
                                      nmjjBins,mjjBinning)
    #Create the JES uncertainties
    if args.UseJES:
        ZeroJet_JetEta0to3_UP = ROOT.TH2F(ZeroJetHistoName+"_JetEta0to3Up",
                                          ZeroJetHistoName+"_JetEta0to3Up",
                                          nZeroJetMassBins,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_JetEta0to3_DOWN = ROOT.TH2F(ZeroJetHistoName+"_JetEta0to3Down",
                                            ZeroJetHistoName+"_JetEta0to3Down",
                                            nZeroJetMassBins,50.0,150.0,
                                            nTauPtBins,TauPtBinning)
        ZeroJet_JetRelativeBal_UP = ROOT.TH2F(ZeroJetHistoName+"_JetRelativeBalUp",
                                              ZeroJetHistoName+"_JetRelativeBalUp",
                                              nZeroJetMassBins,50.0,150.0,
                                              nTauPtBins,TauPtBinning)
        ZeroJet_JetRelativeBal_DOWN = ROOT.TH2F(ZeroJetHistoName+"_JetRelativeBalDown",
                                                ZeroJetHistoName+"_JetRelativeBalDown",
                                                nZeroJetMassBins,50.0,150.0,
                                                nTauPtBins,TauPtBinning)
        ZeroJet_JetRelativeSample_UP = ROOT.TH2F(ZeroJetHistoName+"_JetRelativeSampleUp",
                                                 ZeroJetHistoName+"_JetRelativeSampleUp",
                                                 nZeroJetMassBins,50.0,150.0,
                                                 nTauPtBins,TauPtBinning)
        ZeroJet_JetRelativeSample_DOWN = ROOT.TH2F(ZeroJetHistoName+"_JetRelativeSampleDown",
                                                   ZeroJetHistoName+"_JetRelativeSampleDown",
                                                   nZeroJetMassBins,50.0,150.0,
                                                   nTauPtBins,TauPtBinning)
        ZeroJet_JetEta3to5_UP = ROOT.TH2F(ZeroJetHistoName+"_JetEta3to5Up",
                                          ZeroJetHistoName+"_JetEta3to5Up",
                                          nZeroJetMassBins,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_JetEta3to5_DOWN = ROOT.TH2F(ZeroJetHistoName+"_JetEta3to5Down",
                                            ZeroJetHistoName+"_JetEta3to5Down",
                                            nZeroJetMassBins,50.0,150.0,
                                            nTauPtBins,TauPtBinning)
        ZeroJet_JetEta0to5_UP = ROOT.TH2F(ZeroJetHistoName+"_JetEta0to5Up",
                                          ZeroJetHistoName+"_JetEta0to5Up",
                                          nZeroJetMassBins,50.0,150.0,
                                          nTauPtBins,TauPtBinning)
        ZeroJet_JetEta0to5_DOWN = ROOT.TH2F(ZeroJetHistoName+"_JetEta0to5Down",
                                            ZeroJetHistoName+"_JetEta0to5Down",
                                            nZeroJetMassBins,50.0,150.0,
                                            nTauPtBins,TauPtBinning)
        Boosted_JetEta0to3_UP = ROOT.TH2F(BoostedHistoName+"_JetEta0to3Up",
                                          BoostedHistoName+"_JetEta0to3Up",
                                          nBoostedMassBins,50.0,250.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_JetEta0to3_DOWN = ROOT.TH2F(BoostedHistoName+"_JetEta0to3Down",
                                            BoostedHistoName+"_JetEta0to3Down",
                                            nBoostedMassBins,50.0,250.0,
                                            nHPtBins,HiggsPtBinning)
        Boosted_JetRelativeBal_UP = ROOT.TH2F(BoostedHistoName+"_JetRelativeBalUp",
                                              BoostedHistoName+"_JetRelativeBalUp",
                                              nBoostedMassBins,50.0,250.0,
                                              nHPtBins,HiggsPtBinning)
        Boosted_JetRelativeBal_DOWN = ROOT.TH2F(BoostedHistoName+"_JetRelativeBalDown",
                                                BoostedHistoName+"_JetRelativeBalDown",
                                                nBoostedMassBins,50.0,250.0,
                                                nHPtBins,HiggsPtBinning)
        Boosted_JetRelativeSample_UP = ROOT.TH2F(BoostedHistoName+"_JetRelativeSampleUp",
                                                 BoostedHistoName+"_JetRelativeSampleUp",
                                                 nBoostedMassBins,50.0,250.0,
                                                 nHPtBins,HiggsPtBinning)
        Boosted_JetRelativeSample_DOWN = ROOT.TH2F(BoostedHistoName+"_JetRelativeSampleDown",
                                                   BoostedHistoName+"_JetRelativeSampleDown",
                                                   nBoostedMassBins,50.0,250.0,
                                                   nHPtBins,HiggsPtBinning)
        Boosted_JetEta3to5_UP = ROOT.TH2F(BoostedHistoName+"_JetEta3to5Up",
                                          BoostedHistoName+"_JetEta3to5Up",
                                          nBoostedMassBins,50.0,250.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_JetEta3to5_DOWN = ROOT.TH2F(BoostedHistoName+"_JetEta3to5Down",
                                            BoostedHistoName+"_JetEta3to5Down",
                                            nBoostedMassBins,50.0,250.0,
                                            nHPtBins,HiggsPtBinning)
        Boosted_JetEta0to5_UP = ROOT.TH2F(BoostedHistoName+"_JetEta0to5Up",
                                          BoostedHistoName+"_JetEta0to5Up",
                                          nBoostedMassBins,50.0,250.0,
                                          nHPtBins,HiggsPtBinning)
        Boosted_JetEta0to5_DOWN = ROOT.TH2F(BoostedHistoName+"_JetEta0to5Down",
                                            BoostedHistoName+"_JetEta0to5Down",
                                            nBoostedMassBins,50.0,250.0,
                                            nHPtBins,HiggsPtBinning)
        VBF_JetEta0to3_UP = ROOT.TH2F(VBFHistoName+"_JetEta0to3Up",
                                      VBFHistoName+"_JetEta0to3Up",
                                      nVBFMassBins,50.0,250.0,
                                      nmjjBins,mjjBinning)
        VBF_JetEta0to3_DOWN = ROOT.TH2F(VBFHistoName+"_JetEta0to3Down",
                                        VBFHistoName+"_JetEta0to3Down",
                                        nVBFMassBins,50.0,250.0,
                                        nmjjBins,mjjBinning)
        VBF_JetRelativeBal_UP = ROOT.TH2F(VBFHistoName+"_JetRelativeBalUp",
                                          VBFHistoName+"_JetRelativeBalUp",
                                          nVBFMassBins,50.0,250.0,
                                          nmjjBins,mjjBinning)
        VBF_JetRelativeBal_DOWN = ROOT.TH2F(VBFHistoName+"_JetRelativeBalDown",
                                            VBFHistoName+"_JetRelativeBalDown",
                                            nVBFMassBins,50.0,250.0,
                                            nmjjBins,mjjBinning)
        VBF_JetRelativeSample_UP = ROOT.TH2F(VBFHistoName+"_JetRelativeSampleUp",
                                             VBFHistoName+"_JetRelativeSampleUp",
                                             nVBFMassBins,50.0,250.0,
                                             nmjjBins,mjjBinning)
        VBF_JetRelativeSample_DOWN = ROOT.TH2F(VBFHistoName+"_JetRelativeSampleDown",
                                               VBFHistoName+"_JetRelativeSampleDown",
                                               nVBFMassBins,50.0,250.0,
                                               nmjjBins,mjjBinning)
        VBF_JetEta3to5_UP = ROOT.TH2F(VBFHistoName+"_JetEta3to5Up",
                                      VBFHistoName+"_JetEta3to5Up",
                                      nVBFMassBins,50.0,250.0,
                                      nmjjBins,mjjBinning)
        VBF_JetEta3to5_DOWN = ROOT.TH2F(VBFHistoName+"_JetEta3to5Down",
                                        VBFHistoName+"_JetEta3to5Down",
                                        nVBFMassBins,50.0,250.0,
                                        nmjjBins,mjjBinning)
        VBF_JetEta0to5_UP = ROOT.TH2F(VBFHistoName+"_JetEta0to5Up",
                                      VBFHistoName+"_JetEta0to5Up",
                                      nVBFMassBins,50.0,250.0,
                                      nmjjBins,mjjBinning)
        VBF_JetEta0to5_DOWN = ROOT.TH2F(VBFHistoName+"_JetEta0to5Down",
                                        VBFHistoName+"_JetEta0to5Down",
                                        nVBFMassBins,50.0,250.0,
                                        nmjjBins,mjjBinning)
        #DYShape
    if args.MakeDYShape:
        ZeroJet_DYShape_UP = ROOT.TH2F(ZeroJetHistoName+"_DYShapeUp",
                                       ZeroJetHistoName+"_DYShapeUp",
                                       nZeroJetMassBins,50.0,150.0,
                                       nTauPtBins,TauPtBinning)
        ZeroJet_DYShape_DOWN = ROOT.TH2F(ZeroJetHistoName+"_DYShapeDown",
                                         ZeroJetHistoName+"_DYShapeDown",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        Boosted_DYShape_UP = ROOT.TH2F(BoostedHistoName+"_DYShapeUp",
                                       BoostedHistoName+"_DYShapeUp",
                                       nBoostedMassBins,50.0,250.0,
                                       nHPtBins,HiggsPtBinning)
        Boosted_DYShape_DOWN = ROOT.TH2F(BoostedHistoName+"_DYShapeDown",
                                         BoostedHistoName+"_DYShapeDown",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        VBF_DYShape_UP = ROOT.TH2F(VBFHistoName+"_DYShapeUp",
                                   VBFHistoName+"_DYShapeUp",
                                   nVBFMassBins,50.0,250.0,
                                   nmjjBins,mjjBinning)
        VBF_DYShape_DOWN = ROOT.TH2F(VBFHistoName+"_DYShapeDown",
                                     VBFHistoName+"_DYShapeDown",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)    
    if args.MakeZLShape:
        ZeroJet_DM0_ZLShape_UP = ROOT.TH2F(ZeroJetHistoName+"_DM0_ZLShapeUp",
                                           ZeroJetHistoName+"_DM0_ZLShapeUp",
                                           nZeroJetMassBins,50.0,150.0,
                                           nTauPtBins,TauPtBinning)
        ZeroJet_DM0_ZLShape_DOWN = ROOT.TH2F(ZeroJetHistoName+"_DM0_ZLShapeDown",
                                             ZeroJetHistoName+"_DM0_ZLShapeDown",
                                             nZeroJetMassBins,50.0,150.0,
                                             nTauPtBins,TauPtBinning)
        ZeroJet_DM1_ZLShape_UP = ROOT.TH2F(ZeroJetHistoName+"_DM1_ZLShapeUp",
                                           ZeroJetHistoName+"_DM1_ZLShapeUp",
                                           nZeroJetMassBins,50.0,150.0,
                                           nTauPtBins,TauPtBinning)
        ZeroJet_DM1_ZLShape_DOWN = ROOT.TH2F(ZeroJetHistoName+"_DM1_ZLShapeDown",
                                             ZeroJetHistoName+"_DM1_ZLShapeDown",
                                             nZeroJetMassBins,50.0,150.0,
                                             nTauPtBins,TauPtBinning)
        Boosted_DM0_ZLShape_UP = ROOT.TH2F(BoostedHistoName+"_DM0_ZLShapeUp",
                                           BoostedHistoName+"_DM0_ZLShapeUp",
                                           nBoostedMassBins,50.0,250.0,
                                           nHPtBins,HiggsPtBinning)
        Boosted_DM0_ZLShape_DOWN = ROOT.TH2F(BoostedHistoName+"_DM0_ZLShapeDown",
                                             BoostedHistoName+"_DM0_ZLShapeDown",
                                             nBoostedMassBins,50.0,250.0,
                                             nHPtBins,HiggsPtBinning)
        Boosted_DM1_ZLShape_UP = ROOT.TH2F(BoostedHistoName+"_DM1_ZLShapeUp",
                                           BoostedHistoName+"_DM1_ZLShapeUp",
                                           nBoostedMassBins,50.0,250.0,
                                           nHPtBins,HiggsPtBinning)
        Boosted_DM1_ZLShape_DOWN = ROOT.TH2F(BoostedHistoName+"_DM1_ZLShapeDown",
                                             BoostedHistoName+"_DM1_ZLShapeDown",
                                             nBoostedMassBins,50.0,250.0,
                                             nHPtBins,HiggsPtBinning)
        VBF_DM0_ZLShape_UP = ROOT.TH2F(VBFHistoName+"_DM0_ZLShapeUp",
                                       VBFHistoName+"_DM0_ZLShapeUp",
                                       nVBFMassBins,50.0,250.0,
                                       nmjjBins,mjjBinning)
        VBF_DM0_ZLShape_DOWN = ROOT.TH2F(VBFHistoName+"_DM0_ZLShapeDown",
                                         VBFHistoName+"_DM0_ZLShapeDown",
                                         nVBFMassBins,50.0,250.0,
                                         nmjjBins,mjjBinning)
        VBF_DM1_ZLShape_UP = ROOT.TH2F(VBFHistoName+"_DM1_ZLShapeUp",
                                       VBFHistoName+"_DM1_ZLShapeUp",
                                       nVBFMassBins,50.0,250.0,
                                       nmjjBins,mjjBinning)
        VBF_DM1_ZLShape_DOWN = ROOT.TH2F(VBFHistoName+"_DM1_ZLShapeDown",
                                         VBFHistoName+"_DM1_ZLShapeDown",
                                         nVBFMassBins,50.0,250.0,
                                         nmjjBins,mjjBinning)
    if args.MakeggHTheoryShape:
        #zero jet shapes, 18 total
        ZeroJet_THU_ggH_Mu_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mu_13TeVUp",
                                               ZeroJetHistoName+"_THU_ggH_Mu_13TeVUp",
                                               nZeroJetMassBins,50.0,150.0,
                                               nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Mu_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mu_13TeVDown",
                                               ZeroJetHistoName+"_THU_ggH_Mu_13TeVDown",
                                               nZeroJetMassBins,50.0,150.0,
                                               nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Res_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Res_13TeVUp",
                                                ZeroJetHistoName+"_THU_ggH_Res_13TeVUp",
                                                nZeroJetMassBins,50.0,150.0,
                                                nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Res_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Res_13TeVDown",
                                                  ZeroJetHistoName+"_THU_ggH_Res_13TeVDown",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Mig01_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mig01_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_Mig01_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Mig01_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Mig12_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mig12_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_Mig12_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_Mig12_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_VBF2j_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_VBF2j_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_VBF3j_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_VBF3j_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_PT60_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_PT60_13TeVUp",
                                                 ZeroJetHistoName+"_THU_ggH_PT60_13TeVUp",
                                                 nZeroJetMassBins,50.0,150.0,
                                                 nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_PT60_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_PT60_13TeVDown",
                                                   ZeroJetHistoName+"_THU_ggH_PT60_13TeVDown",
                                                   nZeroJetMassBins,50.0,150.0,
                                                   nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_PT120_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_PT120_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_PT120_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_PT120_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_PT120_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_PT120_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_qmtop_13TeVUp = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_qmtop_13TeVUp",
                                                  ZeroJetHistoName+"_THU_ggH_qmtop_13TeVUp",
                                                  nZeroJetMassBins,50.0,150.0,
                                                  nTauPtBins,TauPtBinning)
        ZeroJet_THU_ggH_qmtop_13TeVDown = ROOT.TH2F(ZeroJetHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                    ZeroJetHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                    nZeroJetMassBins,50.0,150.0,
                                                    nTauPtBins,TauPtBinning)
        #boosted shapes, 18 total
        Boosted_THU_ggH_Mu_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mu_13TeVUp",
                                               BoostedHistoName+"_THU_ggH_Mu_13TeVUp",
                                               nBoostedMassBins,50.0,250.0,
                                               nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Mu_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mu_13TeVDown",
                                                 BoostedHistoName+"_THU_ggH_Mu_13TeVDown",
                                                 nBoostedMassBins,50.0,250.0,
                                                 nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Res_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Res_13TeVUp",
                                                BoostedHistoName+"_THU_ggH_Res_13TeVUp",
                                                nBoostedMassBins,50.0,250.0,
                                                nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Res_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Res_13TeVDown",
                                                  BoostedHistoName+"_THU_ggH_Res_13TeVDown",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Mig01_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mig01_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_Mig01_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Mig01_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Mig12_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mig12_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_Mig12_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_Mig12_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_VBF2j_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_VBF2j_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_VBF3j_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_VBF3j_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_PT60_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_PT60_13TeVUp",
                                                 BoostedHistoName+"_THU_ggH_PT60_13TeVUp",
                                                 nBoostedMassBins,50.0,250.0,
                                                 nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_PT60_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_PT60_13TeVDown",
                                                   BoostedHistoName+"_THU_ggH_PT60_13TeVDown",
                                                   nBoostedMassBins,50.0,250.0,
                                                   nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_PT120_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_PT120_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_PT120_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_PT120_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_PT120_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_PT120_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_qmtop_13TeVUp = ROOT.TH2F(BoostedHistoName+"_THU_ggH_qmtop_13TeVUp",
                                                  BoostedHistoName+"_THU_ggH_qmtop_13TeVUp",
                                                  nBoostedMassBins,50.0,250.0,
                                                  nHPtBins,HiggsPtBinning)
        Boosted_THU_ggH_qmtop_13TeVDown = ROOT.TH2F(BoostedHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                    BoostedHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                    nBoostedMassBins,50.0,250.0,
                                                    nHPtBins,HiggsPtBinning)
        #VBF shapes, 18 total
        VBF_THU_ggH_Mu_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mu_13TeVUp",
                                           VBFHistoName+"_THU_ggH_Mu_13TeVUp",
                                           nVBFMassBins,50.0,250.0,
                                           nmjjBins,mjjBinning)
        VBF_THU_ggH_Mu_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mu_13TeVDown",
                                             VBFHistoName+"_THU_ggH_Mu_13TeVDown",
                                             nVBFMassBins,50.0,250.0,
                                             nmjjBins,mjjBinning)
        VBF_THU_ggH_Res_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_Res_13TeVUp",
                                            VBFHistoName+"_THU_ggH_Res_13TeVUp",
                                            nVBFMassBins,50.0,250.0,
                                            nmjjBins,mjjBinning)
        VBF_THU_ggH_Res_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_Res_13TeVDown",
                                              VBFHistoName+"_THU_ggH_Res_13TeVDown",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_Mig01_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mig01_13TeVUp",
                                              VBFHistoName+"_THU_ggH_Mig01_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_Mig01_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                VBFHistoName+"_THU_ggH_Mig01_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_THU_ggH_Mig12_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mig12_13TeVUp",
                                              VBFHistoName+"_THU_ggH_Mig12_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_Mig12_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                VBFHistoName+"_THU_ggH_Mig12_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_THU_ggH_VBF2j_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                              VBFHistoName+"_THU_ggH_VBF2j_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_VBF2j_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                VBFHistoName+"_THU_ggH_VBF2j_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_THU_ggH_VBF3j_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                              VBFHistoName+"_THU_ggH_VBF3j_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_VBF3j_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                VBFHistoName+"_THU_ggH_VBF3j_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_THU_ggH_PT60_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_PT60_13TeVUp",
                                             VBFHistoName+"_THU_ggH_PT60_13TeVUp",
                                             nVBFMassBins,50.0,250.0,
                                             nmjjBins,mjjBinning)
        VBF_THU_ggH_PT60_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_PT60_13TeVDown",
                                               VBFHistoName+"_THU_ggH_PT60_13TeVDown",
                                               nVBFMassBins,50.0,250.0,
                                               nmjjBins,mjjBinning)
        VBF_THU_ggH_PT120_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_PT120_13TeVUp",
                                              VBFHistoName+"_THU_ggH_PT120_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_PT120_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_PT120_13TeVDown",
                                                VBFHistoName+"_THU_ggH_PT120_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
        VBF_THU_ggH_qmtop_13TeVUp = ROOT.TH2F(VBFHistoName+"_THU_ggH_qmtop_13TeVUp",
                                              VBFHistoName+"_THU_ggH_qmtop_13TeVUp",
                                              nVBFMassBins,50.0,250.0,
                                              nmjjBins,mjjBinning)
        VBF_THU_ggH_qmtop_13TeVDown = ROOT.TH2F(VBFHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                VBFHistoName+"_THU_ggH_qmtop_13TeVDown",
                                                nVBFMassBins,50.0,250.0,
                                                nmjjBins,mjjBinning)
    if args.MakeRecoilUncertainties:
        ZeroJet_ResolutionUp = ROOT.TH2F(ZeroJetHistoName+"_ResolutionUp",
                                         ZeroJetHistoName+"_ResolutionUp",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_ResolutionDown = ROOT.TH2F(ZeroJetHistoName+"_ResolutionDown",
                                         ZeroJetHistoName+"_ResolutionDown",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_ResponseUp = ROOT.TH2F(ZeroJetHistoName+"_ResponseUp",
                                         ZeroJetHistoName+"_ResponseUp",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        ZeroJet_ResponseDown = ROOT.TH2F(ZeroJetHistoName+"_ResponseDown",
                                         ZeroJetHistoName+"_ResponseDown",
                                         nZeroJetMassBins,50.0,150.0,
                                         nTauPtBins,TauPtBinning)
        Boosted_ResolutionUp = ROOT.TH2F(BoostedHistoName+"_ResolutionUp",
                                         BoostedHistoName+"_ResolutionUp",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_ResolutionDown = ROOT.TH2F(BoostedHistoName+"_ResolutionDown",
                                         BoostedHistoName+"_ResolutionDown",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_ResponseUp = ROOT.TH2F(BoostedHistoName+"_ResponseUp",
                                         BoostedHistoName+"_ResponseUp",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        Boosted_ResponseDown = ROOT.TH2F(BoostedHistoName+"_ResponseDown",
                                         BoostedHistoName+"_ResponseDown",
                                         nBoostedMassBins,50.0,250.0,
                                         nHPtBins,HiggsPtBinning)
        VBF_ResolutionUp = ROOT.TH2F(VBFHistoName+"_ResolutionUp",
                                     VBFHistoName+"_ResolutionUp",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)
        VBF_ResolutionDown = ROOT.TH2F(VBFHistoName+"_ResolutionDown",
                                       VBFHistoName+"_ResolutionDown",
                                       nVBFMassBins,50.0,250.0,
                                       nmjjBins,mjjBinning)
        VBF_ResponseUp = ROOT.TH2F(VBFHistoName+"_ResponseUp",
                                   VBFHistoName+"_ResponseUp",
                                   nVBFMassBins,50.0,250.0,
                                   nmjjBins,mjjBinning)
        VBF_ResponseDown = ROOT.TH2F(VBFHistoName+"_ResponseDown",
                                     VBFHistoName+"_ResponseDown",
                                     nVBFMassBins,50.0,250.0,
                                     nmjjBins,mjjBinning)
    if args.MakeTTbarContamination:
        ZeroJet_TTBarContamination = ROOT.TH2F(ZeroJetHistoName+"_TTBarContamination",
                                               ZeroJetHistoName+"_TTBarContamination",
                                               nZeroJetMassBins,50.0,150.0,
                                               nTauPtBins,TauPtBinning)
        Boosted_TTBarContamination = ROOT.TH2F(BoostedHistoName+"_TTBarContamination",
                                               BoostedHistoName+"_TTBarContamination",
                                               nBoostedMassBins,50.0,250.0,
                                               nHPtBins,HiggsPtBinning)
        VBF_TTBarContamination = ROOT.TH2F(VBFHistoName+"_TTBarContamination",
                                           VBFHistoName+"_TTBarContamination",
                                           nVBFMassBins,50.0,250.0,
                                           nmjjBins,mjjBinning)

    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        TheWeight = TheTree.FinalWeighting
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MetVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_1,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)        
        MetVector.SetPtEtaPhiM(TheTree.met,0,TheTree.metphi,0)
        MT = CalculateMT(MuVector,MetVector)
        if args.UseFakeFactor:
            TheWeight = TheWeight*TheTree.Event_Fake_Factor

        #special thing for the ttbar contamination. 
        #since we don't want to do anything else with these ntuples,
        if args.MakeTTbarContamination:
            if(TauVector.Pt()>30.0 and MuVector.Pt() > 26.0 and MT < 50.0):
                if TheTree.njetsWoNoisyJets == 0:
                    ZeroJet_TTBarContamination.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheTree.FinalWeighting*0.1)
                elif (TheTree.njetsWoNoisyJets >= 2
                      and TheTree.mjjWoNoisyJets>300):
                    VBF_TTBarContamination.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*0.1)
                else:
                    Boosted_TTBarContamination.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*0.1)
            continue
            

        if TheTree.njetsWoNoisyJets == 0:
            if(TauVector.Pt()>30.0 and MuVector.Pt() > 26.0 and MT < 50.0):
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
                if args.MakeDYShape:
                    ZeroJet_DYShape_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting_ZPT_UP)
                    ZeroJet_DYShape_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting_ZPT_DOWN)
                if args.MakeggHTheoryShape:
                    ZeroJet_THU_ggH_Mu_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mu_13TeV))
                    ZeroJet_THU_ggH_Mu_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mu_13TeV))
                    ZeroJet_THU_ggH_Res_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Res_13TeV))
                    ZeroJet_THU_ggH_Res_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Res_13TeV))
                    ZeroJet_THU_ggH_Mig01_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig01_13TeV))
                    ZeroJet_THU_ggH_Mig01_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig01_13TeV))
                    ZeroJet_THU_ggH_Mig12_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig12_13TeV))
                    ZeroJet_THU_ggH_Mig12_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig12_13TeV))
                    ZeroJet_THU_ggH_VBF2j_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF2j_13TeV))
                    ZeroJet_THU_ggH_VBF2j_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF2j_13TeV))
                    ZeroJet_THU_ggH_VBF3j_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF3j_13TeV))
                    ZeroJet_THU_ggH_VBF3j_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF3j_13TeV))
                    ZeroJet_THU_ggH_PT60_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT60_13TeV))
                    ZeroJet_THU_ggH_PT60_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT60_13TeV))
                    ZeroJet_THU_ggH_PT120_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT120_13TeV))
                    ZeroJet_THU_ggH_PT120_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT120_13TeV))
                    ZeroJet_THU_ggH_qmtop_13TeVUp.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_qmtop_13TeV))
                    ZeroJet_THU_ggH_qmtop_13TeVDown.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_qmtop_13TeV))
            if args.UseTES:                
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_UP)
                CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_DOWN)
                
                CorrectedMetVector_UP = ROOT.TLorentzVector()
                CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.TES_MET_UP,0.0,TheTree.TES_METPhi_UP,0.0)
                CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.TES_MET_DOWN,0.0,TheTree.TES_METPhi_DOWN,0.0)

                CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                
                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 0):
                            ZeroJet_DM0_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),CorrectedTauVector_UP.Pt(),TheWeight)                    
                        else:
                            ZeroJet_DM0_TES_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 1):                            
                            ZeroJet_DM1_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),CorrectedTauVector_UP.Pt(),TheWeight)
                        else:
                            ZeroJet_DM1_TES_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 10):                            
                            ZeroJet_DM10_TES_UP.Fill((CorrectedTauVector_UP+MuVector).M(),CorrectedTauVector_UP.Pt(),TheWeight)                        
                        else:
                            ZeroJet_DM10_TES_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 0):
                            ZeroJet_DM0_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),CorrectedTauVector_DOWN.Pt(),TheWeight)                    
                        else:
                            ZeroJet_DM0_TES_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 1):                            
                            ZeroJet_DM1_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),CorrectedTauVector_DOWN.Pt(),TheWeight)
                        else:
                            ZeroJet_DM1_TES_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 10):                            
                            ZeroJet_DM10_TES_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(),CorrectedTauVector_DOWN.Pt(),TheWeight)                        
                        else:
                            ZeroJet_DM10_TES_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)            
            if args.MakeZLShape:
                #This gets split into EES shifts, and MES shifts            
                if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.EES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.EES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.EES_MET_UP,0.0,TheTree.EES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.EES_MET_DOWN,0.0,TheTree.EES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                    
                elif(TheTree.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.MES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.MES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.MES_MET_UP,0.0,TheTree.MES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.MES_MET_DOWN,0.0,TheTree.MES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                else:
                    CorrectedTauVector_UP = TauVector
                    CorrectedTauVector_DOWN = TauVector
                    CorrectedMetVector_UP = MetVector
                    CorrectedMetVector_DOWN = MetVector

                    CorrectedMT_UP = MT
                    CorrectedMT_DOWN = MT

                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 0):
                            ZeroJet_DM0_ZLShape_UP.Fill((CorrectedTauVector_UP+MuVector).M(), CorrectedTauVector_UP.Pt(),TheWeight)
                        else:
                            ZeroJet_DM0_ZLShape_UP.Fill((TauVector+MuVector).M(), TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 1):
                            ZeroJet_DM1_ZLShape_UP.Fill((CorrectedTauVector_UP+MuVector).M(), CorrectedTauVector_UP.Pt(),TheWeight)
                        else:
                            ZeroJet_DM1_ZLShape_UP.Fill((TauVector+MuVector).M(), TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 0):
                            ZeroJet_DM0_ZLShape_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(), CorrectedTauVector_DOWN.Pt(),TheWeight)
                        else:
                            ZeroJet_DM0_ZLShape_DOWN.Fill((TauVector+MuVector).M(), TauVector.Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 0):
                            ZeroJet_DM1_ZLShape_DOWN.Fill((CorrectedTauVector_DOWN+MuVector).M(), CorrectedTauVector_DOWN.Pt(),TheWeight)
                        else:
                            ZeroJet_DM1_ZLShape_DOWN.Fill((TauVector+MuVector).M(), TauVector.Pt(),TheWeight)
            if args.MakeRecoilUncertainties:
                ResolutionCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResolutionCorrectedMetVector_DOWN = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_DOWN = ROOT.TLorentzVector()

                ResolutionCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_resolutionUp,0.0,TheTree.metphi_resolutionUp,0.0)
                ResolutionCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_resolutionDown,0.0,TheTree.metphi_resolutionDown,0.0)
                ResponseCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_responseUp,0.0,TheTree.metphi_responseUp,0.0)
                ResponseCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_responseDown,0.0,TheTree.metphi_responseDown,0.0)

                ResolutionCorrectedMT_UP = CalculateMT(MuVector,ResolutionCorrectedMetVector_UP)
                ResolutionCorrectedMT_DOWN = CalculateMT(MuVector,ResolutionCorrectedMetVector_DOWN)
                ResponseCorrectedMT_UP = CalculateMT(MuVector,ResponseCorrectedMetVector_UP)
                ResponseCorrectedMT_DOWN = CalculateMT(MuVector,ResponseCorrectedMetVector_DOWN)
                if(TauVector.Pt() > 30.0 and MuVector.Pt() > 26.0):
                    if(ResolutionCorrectedMT_UP < 50.0):
                        ZeroJet_ResolutionUp.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheWeight)
                    if(ResolutionCorrectedMT_DOWN < 50.0):
                        ZeroJet_ResolutionDown.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheWeight)
                    if(ResponseCorrectedMT_UP < 50.0):
                        ZeroJet_ResponseUp.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheWeight)
                    if(ResponseCorrectedMT_DOWN < 50.0):
                        ZeroJet_ResponseDown.Fill((MuVector+TauVector).M(),TauVector.Pt(),TheWeight)
                
        #VBF Category
        elif (TheTree.njetsWoNoisyJets >= 2
              and TheTree.mjjWoNoisyJets>300):
            if(TauVector.Pt()>30.0 and MuVector.Pt() > 26.0):
                VBFResultsRolled.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
                #Handle Uncertainties
                if args.UseFakeFactor:
                    VBF_ff_qcd_syst_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_syst_up)
                    VBF_ff_qcd_syst_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_syst_down)
                    VBF_ff_qcd_njet0_mt_stat_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_up)
                    VBF_ff_qcd_njet0_mt_stat_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_down)
                    VBF_ff_qcd_njet1_mt_stat_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_up)
                    VBF_ff_qcd_njet1_mt_stat_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_down)
                    VBF_ff_tt_njet1_stat_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_up)
                    VBF_ff_tt_njet1_stat_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_down)
                    VBF_ff_tt_syst_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_tt_syst_up)
                    VBF_ff_tt_syst_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_tt_syst_down)
                    VBF_ff_w_njet0_mt_stat_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_up)
                    VBF_ff_w_njet0_mt_stat_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_down)
                    VBF_ff_w_njet1_mt_stat_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_up)
                    VBF_ff_w_njet1_mt_stat_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_down)
                    VBF_ff_w_syst_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_syst_up)
                    VBF_ff_w_syst_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*TheTree.ff_w_syst_down)
                if args.MakeDYShape:
                    VBF_DYShape_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting_ZPT_UP)
                    VBF_DYShape_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting_ZPT_DOWN)
                if args.MakeggHTheoryShape:
                    VBF_THU_ggH_Mu_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mu_13TeV))
                    VBF_THU_ggH_Mu_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mu_13TeV))
                    VBF_THU_ggH_Res_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Res_13TeV))
                    VBF_THU_ggH_Res_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Res_13TeV))
                    VBF_THU_ggH_Mig01_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig01_13TeV))
                    VBF_THU_ggH_Mig01_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig01_13TeV))
                    VBF_THU_ggH_Mig12_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig12_13TeV))
                    VBF_THU_ggH_Mig12_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig12_13TeV))
                    VBF_THU_ggH_VBF2j_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF2j_13TeV))
                    VBF_THU_ggH_VBF2j_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF2j_13TeV))
                    VBF_THU_ggH_VBF3j_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF3j_13TeV))
                    VBF_THU_ggH_VBF3j_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF3j_13TeV))
                    VBF_THU_ggH_PT60_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT60_13TeV))
                    VBF_THU_ggH_PT60_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT60_13TeV))
                    VBF_THU_ggH_PT120_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT120_13TeV))
                    VBF_THU_ggH_PT120_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT120_13TeV))
                    VBF_THU_ggH_qmtop_13TeVUp.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_qmtop_13TeV))
                    VBF_THU_ggH_qmtop_13TeVDown.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_qmtop_13TeV))
            if args.UseTES:
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_UP)
                CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_DOWN)
                
                CorrectedMetVector_UP = ROOT.TLorentzVector()
                CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.TES_MET_UP,0.0,TheTree.TES_METPhi_UP,0.0)
                CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.TES_MET_DOWN,0.0,TheTree.TES_METPhi_DOWN,0.0)

                CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                
                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):                        
                        VBF_DM0_TES_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)                                        
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):                        
                        VBF_DM1_TES_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)                    
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):                        
                        VBF_DM10_TES_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)                        
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        VBF_DM0_TES_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)                    
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):                        
                        VBF_DM1_TES_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):                        
                        VBF_DM10_TES_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)                                    
            if args.MakeZLShape:
                #This gets split into EES shifts, and MES shifts            
                if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.EES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.EES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.EES_MET_UP,0.0,TheTree.EES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.EES_MET_DOWN,0.0,TheTree.EES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                    
                elif(TheTree.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.MES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.MES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.MES_MET_UP,0.0,TheTree.MES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.MES_MET_DOWN,0.0,TheTree.MES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)

                else:
                    CorrectedTauVector_UP = TauVector
                    CorrectedTauVector_DOWN = TauVector
                    CorrectedMetVector_UP = MetVector
                    CorrectedMetVector_DOWN = MetVector

                    CorrectedMT_UP = MT
                    CorrectedMT_DOWN = MT
                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        VBF_DM0_ZLShape_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        VBF_DM1_ZLShape_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        VBF_DM0_ZLShape_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        VBF_DM1_ZLShape_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets,TheWeight)
            if args.MakeRecoilUncertainties:
                ResolutionCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResolutionCorrectedMetVector_DOWN = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_DOWN = ROOT.TLorentzVector()

                ResolutionCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_resolutionUp,0.0,TheTree.metphi_resolutionUp,0.0)
                ResolutionCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_resolutionDown,0.0,TheTree.metphi_resolutionDown,0.0)
                ResponseCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_responseUp,0.0,TheTree.metphi_responseUp,0.0)
                ResponseCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_responseDown,0.0,TheTree.metphi_responseDown,0.0)

                ResolutionCorrectedMT_UP = CalculateMT(MuVector,ResolutionCorrectedMetVector_UP)
                ResolutionCorrectedMT_DOWN = CalculateMT(MuVector,ResolutionCorrectedMetVector_DOWN)
                ResponseCorrectedMT_UP = CalculateMT(MuVector,ResponseCorrectedMetVector_UP)
                ResponseCorrectedMT_DOWN = CalculateMT(MuVector,ResponseCorrectedMetVector_DOWN)
                if(TauVector.Pt() > 30.0 and MuVector.Pt() > 26.0):
                    if(ResolutionCorrectedMT_UP < 50.0):
                        VBF_ResolutionUp.Fill(TheTree.m_sv_ResolutionUp,TheTree.mjjWoNoisyJets,TheWeight)
                    if(ResolutionCorrectedMT_DOWN < 50.0):
                        VBF_ResolutionDown.Fill(TheTree.m_sv_ResolutionDown,TheTree.mjjWoNoisyJets,TheWeight)
                    if(ResponseCorrectedMT_UP < 50.0):
                        VBF_ResponseUp.Fill(TheTree.m_sv_ResponseUp,TheTree.mjjWoNoisyJets,TheWeight)
                    if(ResponseCorrectedMT_DOWN < 50.0):
                        VBF_ResponseDown.Fill(TheTree.m_sv_ResponseDown,TheTree.mjjWoNoisyJets,TheWeight)
#boosted category
        else:
            if(TauVector.Pt()>30.0 and MuVector.Pt() > 26.0):
                BoostedResultsRolled.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #Handle Uncertainties
                if args.UseFakeFactor:
                    Boosted_ff_qcd_syst_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_up)
                    Boosted_ff_qcd_syst_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_syst_down)
                    Boosted_ff_qcd_njet0_mt_stat_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_up)
                    Boosted_ff_qcd_njet0_mt_stat_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet0_stat_down)
                    Boosted_ff_qcd_njet1_mt_stat_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_up)
                    Boosted_ff_qcd_njet1_mt_stat_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_qcd_dm0_njet1_stat_down)
                    Boosted_ff_tt_njet1_stat_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_up)
                    Boosted_ff_tt_njet1_stat_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_tt_dm0_njet1_stat_down)
                    Boosted_ff_tt_syst_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_up)
                    Boosted_ff_tt_syst_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_tt_syst_down)
                    Boosted_ff_w_njet0_mt_stat_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_up)
                    Boosted_ff_w_njet0_mt_stat_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet0_stat_down)
                    Boosted_ff_w_njet1_mt_stat_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_up)
                    Boosted_ff_w_njet1_mt_stat_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_dm0_njet1_stat_down)
                    Boosted_ff_w_syst_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_up)
                    Boosted_ff_w_syst_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting*TheTree.ff_w_syst_down)
                if args.MakeDYShape:
                    Boosted_DYShape_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting_ZPT_UP)
                    Boosted_DYShape_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheTree.FinalWeighting_ZPT_DOWN)
                if args.MakeggHTheoryShape:
                    Boosted_THU_ggH_Mu_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mu_13TeV))
                    Boosted_THU_ggH_Mu_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mu_13TeV))
                    Boosted_THU_ggH_Res_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Res_13TeV))
                    Boosted_THU_ggH_Res_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Res_13TeV))
                    Boosted_THU_ggH_Mig01_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig01_13TeV))
                    Boosted_THU_ggH_Mig01_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig01_13TeV))
                    Boosted_THU_ggH_Mig12_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_Mig12_13TeV))
                    Boosted_THU_ggH_Mig12_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_Mig12_13TeV))
                    Boosted_THU_ggH_VBF2j_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF2j_13TeV))
                    Boosted_THU_ggH_VBF2j_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF2j_13TeV))
                    Boosted_THU_ggH_VBF3j_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_VBF3j_13TeV))
                    Boosted_THU_ggH_VBF3j_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_VBF3j_13TeV))
                    Boosted_THU_ggH_PT60_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT60_13TeV))
                    Boosted_THU_ggH_PT60_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT60_13TeV))
                    Boosted_THU_ggH_PT120_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_PT120_13TeV))
                    Boosted_THU_ggH_PT120_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_PT120_13TeV))
                    Boosted_THU_ggH_qmtop_13TeVUp.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0+TheTree.THU_ggH_qmtop_13TeV))
                    Boosted_THU_ggH_qmtop_13TeVDown.Fill(TheTree.m_sv,(TauVector+MuVector+MetVector).Pt(),TheTree.FinalWeighting*(1.0-TheTree.THU_ggH_qmtop_13TeV))
            if args.UseTES:
                CorrectedTauVector_UP = ROOT.TLorentzVector()
                CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.TES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_UP)
                CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.TES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.TES_E_DOWN)
                
                CorrectedMetVector_UP = ROOT.TLorentzVector()
                CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.TES_MET_UP,0.0,TheTree.TES_METPhi_UP,0.0)
                CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.TES_MET_DOWN,0.0,TheTree.TES_METPhi_DOWN,0.0)

                CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                
                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 0):
                            Boosted_DM0_TES_UP.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_UP+CorrectedMetVector_UP).Pt(),TheWeight)
                        else:
                            Boosted_DM0_TES_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 1):
                            Boosted_DM1_TES_UP.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_UP+CorrectedMetVector_UP).Pt(),TheWeight)
                        else:
                            Boosted_DM1_TES_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_UP.Pt() > 30 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):                        
                        if(TheTree.l2_decayMode == 10):
                            Boosted_DM10_TES_UP.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_UP+CorrectedMetVector_UP).Pt(),TheWeight)                        
                        else:
                            Boosted_DM10_TES_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)                        
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):
                        if(TheTree.l2_decayMode == 0):
                            Boosted_DM0_TES_DOWN.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_DOWN+CorrectedMetVector_UP).Pt(),TheWeight)                    
                        else:
                            Boosted_DM0_TES_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)                    
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30)):                        
                        if(TheTree.l2_decayMode == 1):
                            Boosted_DM1_TES_DOWN.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_DOWN+CorrectedMetVector_DOWN).Pt(),TheWeight)
                        else:
                            Boosted_DM1_TES_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 10 and CorrectedTauVector_DOWN.Pt() > 30 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30)):                        
                        if():
                            Boosted_DM10_TES_DOWN.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_DOWN+CorrectedMetVector_DOWN).Pt(),TheWeight)
                        else:
                            Boosted_DM10_TES_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)            
            if args.MakeZLShape:
                #This gets split into EES shifts, and MES shifts            
                if(TheTree.gen_match_2 == 1 or TheTree.gen_match_2 == 3):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.EES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.EES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.EES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.EES_MET_UP,0.0,TheTree.EES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.EES_MET_DOWN,0.0,TheTree.EES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)
                    
                elif(TheTree.gen_match_2 == 2 or TheTree.gen_match_2 == 4):
                    CorrectedTauVector_UP = ROOT.TLorentzVector()
                    CorrectedTauVector_DOWN = ROOT.TLorentzVector()
                    CorrectedTauVector_UP.SetPtEtaPhiE(TheTree.MES_Pt_UP,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_UP)
                    CorrectedTauVector_DOWN.SetPtEtaPhiE(TheTree.MES_Pt_DOWN,TheTree.eta_2,TheTree.phi_2,TheTree.MES_E_DOWN)

                    CorrectedMetVector_UP = ROOT.TLorentzVector()
                    CorrectedMetVector_DOWN = ROOT.TLorentzVector()
                    CorrectedMetVector_UP.SetPtEtaPhiM(TheTree.MES_MET_UP,0.0,TheTree.MES_METPhi_UP,0.0)
                    CorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.MES_MET_DOWN,0.0,TheTree.MES_METPhi_DOWN,0.0)

                    CorrectedMT_UP = CalculateMT(MuVector,CorrectedMetVector_UP)
                    CorrectedMT_DOWN = CalculateMT(MuVector,CorrectedMetVector_DOWN)                
                    
                else:
                    CorrectedTauVector_UP = TauVector
                    CorrectedTauVector_DOWN = TauVector
                    CorrectedMetVector_UP = MetVector
                    CorrectedMetVector_DOWN = MetVector

                    CorrectedMT_UP = MT
                    CorrectedMT_DOWN = MT
                    
                if(MuVector.Pt() > 26):
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 0):
                            Boosted_DM0_ZLShape_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                        else:
                            Boosted_DM0_ZLShape_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_UP.Pt() > 30.0 and CorrectedMT_UP < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 1):
                            Boosted_DM1_ZLShape_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                        else:
                            Boosted_DM1_ZLShape_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 0 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 1 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 0):
                            Boosted_DM0_ZLShape_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                        else:
                            Boosted_DM0_ZLShape_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                    if((TheTree.l2_decayMode == 1 and CorrectedTauVector_DOWN.Pt() > 30.0 and CorrectedMT_DOWN < 50.0)
                       or (TheTree.l2_decayMode == 0 and TauVector.Pt() > 30.0 and MT < 50.0)
                       or (TheTree.l2_decayMode == 10 and TauVector.Pt() > 30.0 and MT < 50.0)):
                        if(TheTree.l2_decayMode == 1):
                            Boosted_DM1_ZLShape_DOWN.Fill(TheTree.m_sv,(MuVector+CorrectedTauVector_DOWN+CorrectedMetVector_DOWN).Pt(),TheWeight)
                        else:
                            Boosted_DM1_ZLShape_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
            if args.MakeRecoilUncertainties:
                ResolutionCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResolutionCorrectedMetVector_DOWN = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_UP = ROOT.TLorentzVector()
                ResponseCorrectedMetVector_DOWN = ROOT.TLorentzVector()

                ResolutionCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_resolutionUp,0.0,TheTree.metphi_resolutionUp,0.0)
                ResolutionCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_resolutionDown,0.0,TheTree.metphi_resolutionDown,0.0)
                ResponseCorrectedMetVector_UP.SetPtEtaPhiM(TheTree.met_responseUp,0.0,TheTree.metphi_responseUp,0.0)
                ResponseCorrectedMetVector_DOWN.SetPtEtaPhiM(TheTree.met_responseDown,0.0,TheTree.metphi_responseDown,0.0)

                ResolutionCorrectedMT_UP = CalculateMT(MuVector,ResolutionCorrectedMetVector_UP)
                ResolutionCorrectedMT_DOWN = CalculateMT(MuVector,ResolutionCorrectedMetVector_DOWN)
                ResponseCorrectedMT_UP = CalculateMT(MuVector,ResponseCorrectedMetVector_UP)
                ResponseCorrectedMT_DOWN = CalculateMT(MuVector,ResponseCorrectedMetVector_DOWN)
                if(TauVector.Pt() > 30.0 and MuVector.Pt() > 26.0):
                    if(ResolutionCorrectedMT_UP < 50.0):
                        Boosted_ResolutionUp.Fill(TheTree.m_sv_ResolutionUp,(TauVector+MuVector+ResolutionCorrectedMetVector_UP).Pt(),TheWeight)
                    if(ResolutionCorrectedMT_DOWN < 50.0):
                        Boosted_ResolutionDown.Fill(TheTree.m_sv_ResolutionDown,(TauVector+MuVector+ResolutionCorrectedMetVector_DOWN).Pt(),TheWeight)
                    if(ResponseCorrectedMT_UP < 50.0):
                        Boosted_ResponseUp.Fill(TheTree.m_sv_ResponseUp,(TauVector+MuVector+ResponseCorrectedMetVector_UP).Pt(),TheWeight)
                    if(ResponseCorrectedMT_DOWN < 50.0):
                        Boosted_ResponseDown.Fill(TheTree.m_sv_ResponseDown,(TauVector+MuVector+ResponseCorrectedMetVector_DOWN).Pt(),TheWeight)
        if args.UseJES:
            #create correct met vectors
            MetVector_JetEta0to3_UP = ROOT.TLorentzVector()
            MetVector_JetEta0to3_DOWN = ROOT.TLorentzVector()
            MetVector_JetRelativeBal_UP = ROOT.TLorentzVector()
            MetVector_JetRelativeBal_DOWN = ROOT.TLorentzVector()
            MetVector_JetRelativeSample_UP = ROOT.TLorentzVector()
            MetVector_JetRelativeSample_DOWN = ROOT.TLorentzVector()
            MetVector_JetEta3to5_UP = ROOT.TLorentzVector()
            MetVector_JetEta3to5_DOWN = ROOT.TLorentzVector()
            MetVector_JetEta0to5_UP = ROOT.TLorentzVector()
            MetVector_JetEta0to5_DOWN = ROOT.TLorentzVector()

            MetVector_JetEta0to3_UP.SetPtEtaPhiM(TheTree.met_JetEta0to3Up,0,TheTree.metphi_JetEta0to3Up,0)
            MetVector_JetEta0to3_DOWN.SetPtEtaPhiM(TheTree.met_JetEta0to3Down,0,TheTree.metphi_JetEta0to3Down,0)
            MetVector_JetRelativeBal_UP.SetPtEtaPhiM(TheTree.met_JetRelativeBalUp,0,TheTree.metphi_JetRelativeBalUp,0)
            MetVector_JetRelativeBal_DOWN.SetPtEtaPhiM(TheTree.met_JetRelativeBalDown,0,TheTree.metphi_JetRelativeBalDown,0)
            MetVector_JetRelativeSample_UP.SetPtEtaPhiM(TheTree.met_JetRelativeSampleUp,0,TheTree.metphi_JetRelativeSampleUp,0)
            MetVector_JetRelativeSample_DOWN.SetPtEtaPhiM(TheTree.met_JetRelativeSampleDown,0,TheTree.metphi_JetRelativeSampleDown,0)
            MetVector_JetEta3to5_UP.SetPtEtaPhiM(TheTree.met_JetEta3to5Up,0,TheTree.metphi_JetEta3to5Up,0)
            MetVector_JetEta3to5_DOWN.SetPtEtaPhiM(TheTree.met_JetEta3to5Down,0,TheTree.metphi_JetEta3to5Down,0)
            MetVector_JetEta0to5_UP.SetPtEtaPhiM(TheTree.met_JetEta0to5Up,0,TheTree.metphi_JetEta0to5Up,0)
            MetVector_JetEta0to5_DOWN.SetPtEtaPhiM(TheTree.met_JetEta0to5Down,0,TheTree.metphi_JetEta0to5Down,0)

            #calculate the various transverse masses needed to for the various criteria
            MT_JetEta0to3_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to3_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to3_UP))))
            MT_JetEta0to3_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to3_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to3_DOWN))))
            MT_JetRelativeBal_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeBal_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeBal_UP))))
            MT_JetRelativeBal_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeBal_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeBal_DOWN))))
            MT_JetRelativeSample_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeSample_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeSample_UP))))
            MT_JetRelativeSample_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeSample_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeSample_DOWN))))
            MT_JetEta3to5_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta3to5_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta3to5_UP))))
            MT_JetEta3to5_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta3to5_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta3to5_DOWN))))
            MT_JetEta0to5_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to5_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to5_UP))))
            MT_JetEta0to5_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to5_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to5_DOWN))))
            
            #now we split up and define the various categories,
            #first things first, everything must pass basic tau whatever
            if(TauVector.Pt() > 30.0 and MuVector.Pt() > 26.0):
                #define the JetEta0to3_UP area
                if(MT_JetEta0to3_UP < 50.0):
                    #ZeroJet JetEta0to3_UP
                    if TheTree.njetsWoNoisyJets_JetEta0to3Up == 0:
                        ZeroJet_JetEta0to3_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta0to3Up >=2
                          and TheTree.mjjWoNoisyJets_JetEta0to3Up > 300):
                        VBF_JetEta0to3_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta0to3Up,TheWeight)
                    else:
                        Boosted_JetEta0to3_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetEta0to3_DOWN area
                if(MT_JetEta0to3_DOWN < 50.0):
                    #ZeroJet JetEta0to3_DOWN
                    if TheTree.njetsWoNoisyJets_JetEta0to3Down == 0:
                        ZeroJet_JetEta0to3_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta0to3Down >=2
                          and TheTree.mjjWoNoisyJets_JetEta0to3Down > 300):
                        VBF_JetEta0to3_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta0to3Down,TheWeight)
                    else:
                        Boosted_JetEta0to3_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetRelativeBal_UP area
                if(MT_JetRelativeBal_UP < 50.0):
                    #ZeroJet JetRelativeBal_UP
                    if TheTree.njetsWoNoisyJets_JetRelativeBalUp == 0:
                        ZeroJet_JetRelativeBal_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetRelativeBalUp >=2
                          and TheTree.mjjWoNoisyJets_JetRelativeBalUp > 300):
                        VBF_JetRelativeBal_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetRelativeBalUp,TheWeight)
                    else:
                        Boosted_JetRelativeBal_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetRelativeBal_DOWN area
                if(MT_JetRelativeBal_DOWN < 50.0):
                    #ZeroJet JetRelativeBal_DOWN
                    if TheTree.njetsWoNoisyJets_JetRelativeBalDown == 0:
                        ZeroJet_JetRelativeBal_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetRelativeBalDown >=2
                          and TheTree.mjjWoNoisyJets_JetRelativeBalDown > 300):
                        VBF_JetRelativeBal_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetRelativeBalDown,TheWeight)
                    else:
                        Boosted_JetRelativeBal_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetRelativeSample_UP area
                if(MT_JetRelativeSample_UP < 50.0):
                    #ZeroJet JetRelativeSample_UP
                    if TheTree.njetsWoNoisyJets_JetRelativeSampleUp == 0:
                        ZeroJet_JetRelativeSample_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetRelativeSampleUp >=2
                          and TheTree.mjjWoNoisyJets_JetRelativeSampleUp > 300):
                        VBF_JetRelativeSample_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetRelativeSampleUp,TheWeight)
                    else:
                        Boosted_JetRelativeSample_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetRelativeSample_DOWN area
                if(MT_JetRelativeSample_DOWN < 50.0):
                    #ZeroJet JetRelativeSample_DOWN
                    if TheTree.njetsWoNoisyJets_JetRelativeSampleDown == 0:
                        ZeroJet_JetRelativeSample_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetRelativeSampleDown >=2
                          and TheTree.mjjWoNoisyJets_JetRelativeSampleDown > 300):
                        VBF_JetRelativeSample_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetRelativeSampleDown,TheWeight)
                    else:
                        Boosted_JetRelativeSample_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetEta3to5_UP area
                if(MT_JetEta3to5_UP < 50.0):
                    #ZeroJet JetEta3to5_UP
                    if TheTree.njetsWoNoisyJets_JetEta3to5Up == 0:
                        ZeroJet_JetEta3to5_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta3to5Up >=2
                          and TheTree.mjjWoNoisyJets_JetEta3to5Up > 300):
                        VBF_JetEta3to5_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta3to5Up,TheWeight)
                    else:
                        Boosted_JetEta3to5_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetEta3to5_DOWN area
                if(MT_JetEta3to5_DOWN < 50.0):
                    #ZeroJet JetEta3to5_DOWN
                    if TheTree.njetsWoNoisyJets_JetEta3to5Down == 0:
                        ZeroJet_JetEta3to5_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta3to5Down >=2
                          and TheTree.mjjWoNoisyJets_JetEta3to5Down > 300):
                        VBF_JetEta3to5_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta3to5Down,TheWeight)
                    else:
                        Boosted_JetEta3to5_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetEta0to5_UP area
                if(MT_JetEta0to5_UP < 50.0):
                    #ZeroJet JetEta0to5_UP
                    if TheTree.njetsWoNoisyJets_JetEta0to5Up == 0:
                        ZeroJet_JetEta0to5_UP.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta0to5Up >=2
                          and TheTree.mjjWoNoisyJets_JetEta0to5Up > 300):
                        VBF_JetEta0to5_UP.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta0to5Up,TheWeight)
                    else:
                        Boosted_JetEta0to5_UP.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)
                #define the JetEta0to5_DOWN area
                if(MT_JetEta0to5_DOWN < 50.0):
                    #ZeroJet JetEta0to5_DOWN
                    if TheTree.njetsWoNoisyJets_JetEta0to5Down == 0:
                        ZeroJet_JetEta0to5_DOWN.Fill((TauVector+MuVector).M(),TauVector.Pt(),TheWeight)
                    elif (TheTree.njetsWoNoisyJets_JetEta0to5Down >=2
                          and TheTree.mjjWoNoisyJets_JetEta0to5Down > 300):
                        VBF_JetEta0to5_DOWN.Fill(TheTree.m_sv,TheTree.mjjWoNoisyJets_JetEta0to5Down,TheWeight)
                    else:
                        Boosted_JetEta0to5_DOWN.Fill(TheTree.m_sv,(MuVector+TauVector+MetVector).Pt(),TheWeight)                            

    mt_0jetDir.cd()
    if not args.MakeTTbarContamination:
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
        if args.UseJES:
            ZeroJet_JetEta0to3_UP.Write()
            ZeroJet_JetEta0to3_DOWN.Write()
            ZeroJet_JetRelativeBal_UP.Write()
            ZeroJet_JetRelativeBal_DOWN.Write()
            ZeroJet_JetRelativeSample_UP.Write()
            ZeroJet_JetRelativeSample_DOWN.Write()
            ZeroJet_JetEta3to5_UP.Write()
            ZeroJet_JetEta3to5_DOWN.Write()
            ZeroJet_JetEta0to5_UP.Write()
            ZeroJet_JetEta0to5_DOWN.Write()
        if args.MakeDYShape:
            ZeroJet_DYShape_UP.Write()
            ZeroJet_DYShape_DOWN.Write()
        if args.MakeZLShape:
            ZeroJet_DM0_ZLShape_UP.Write()
            ZeroJet_DM0_ZLShape_DOWN.Write()
            ZeroJet_DM1_ZLShape_UP.Write()
            ZeroJet_DM1_ZLShape_DOWN.Write()
        if args.MakeggHTheoryShape:
            ZeroJet_THU_ggH_Mu_13TeVUp.Write()
            ZeroJet_THU_ggH_Mu_13TeVDown.Write()
            ZeroJet_THU_ggH_Res_13TeVUp.Write()
            ZeroJet_THU_ggH_Res_13TeVDown.Write()
            ZeroJet_THU_ggH_Mig01_13TeVUp.Write()
            ZeroJet_THU_ggH_Mig01_13TeVDown.Write()
            ZeroJet_THU_ggH_Mig12_13TeVUp.Write()
            ZeroJet_THU_ggH_Mig12_13TeVDown.Write()
            ZeroJet_THU_ggH_VBF2j_13TeVUp.Write()
            ZeroJet_THU_ggH_VBF2j_13TeVDown.Write()
            ZeroJet_THU_ggH_VBF3j_13TeVUp.Write()
            ZeroJet_THU_ggH_VBF3j_13TeVDown.Write()
            ZeroJet_THU_ggH_PT60_13TeVUp.Write()
            ZeroJet_THU_ggH_PT60_13TeVDown.Write()
            ZeroJet_THU_ggH_PT120_13TeVUp.Write()
            ZeroJet_THU_ggH_PT120_13TeVDown.Write()
            ZeroJet_THU_ggH_qmtop_13TeVUp.Write()
            ZeroJet_THU_ggH_qmtop_13TeVDown.Write()
        if args.MakeRecoilUncertainties:
            ZeroJet_ResolutionUp.Write()
            ZeroJet_ResolutionDown.Write()
            ZeroJet_ResponseUp.Write()
            ZeroJet_ResponseDown.Write()
    else:
        ZeroJet_TTBarContamination.Write()
        
    mt_boostedDir.cd()
    if not args.MakeTTbarContamination:
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
        if args.UseJES:
            Boosted_JetEta0to3_UP.Write()
            Boosted_JetEta0to3_DOWN.Write()
            Boosted_JetRelativeBal_UP.Write()
            Boosted_JetRelativeBal_DOWN.Write()
            Boosted_JetRelativeSample_UP.Write()
            Boosted_JetRelativeSample_DOWN.Write()
            Boosted_JetEta3to5_UP.Write()
            Boosted_JetEta3to5_DOWN.Write()
            Boosted_JetEta0to5_UP.Write()
            Boosted_JetEta0to5_DOWN.Write()
        if args.MakeDYShape:
            Boosted_DYShape_UP.Write()
            Boosted_DYShape_DOWN.Write()
        if args.MakeZLShape:
            Boosted_DM0_ZLShape_UP.Write()
            Boosted_DM0_ZLShape_DOWN.Write()
            Boosted_DM1_ZLShape_UP.Write()
            Boosted_DM1_ZLShape_DOWN.Write()
        if args.MakeggHTheoryShape:
            Boosted_THU_ggH_Mu_13TeVUp.Write()
            Boosted_THU_ggH_Mu_13TeVDown.Write()
            Boosted_THU_ggH_Res_13TeVUp.Write()
            Boosted_THU_ggH_Res_13TeVDown.Write()
            Boosted_THU_ggH_Mig01_13TeVUp.Write()
            Boosted_THU_ggH_Mig01_13TeVDown.Write()
            Boosted_THU_ggH_Mig12_13TeVUp.Write()
            Boosted_THU_ggH_Mig12_13TeVDown.Write()
            Boosted_THU_ggH_VBF2j_13TeVUp.Write()
            Boosted_THU_ggH_VBF2j_13TeVDown.Write()
            Boosted_THU_ggH_VBF3j_13TeVUp.Write()
            Boosted_THU_ggH_VBF3j_13TeVDown.Write()
            Boosted_THU_ggH_PT60_13TeVUp.Write()
            Boosted_THU_ggH_PT60_13TeVDown.Write()
            Boosted_THU_ggH_PT120_13TeVUp.Write()
            Boosted_THU_ggH_PT120_13TeVDown.Write()
            Boosted_THU_ggH_qmtop_13TeVUp.Write()
            Boosted_THU_ggH_qmtop_13TeVDown.Write()
        if args.MakeRecoilUncertainties:
            Boosted_ResolutionUp.Write()
            Boosted_ResolutionDown.Write()
            Boosted_ResponseUp.Write()
            Boosted_ResponseDown.Write()
    else:
        Boosted_TTBarContamination.Write()
    
    mt_vbfDir.cd()
    if not args.MakeTTbarContamination:
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
        if args.UseJES:
            VBF_JetEta0to3_UP.Write()
            VBF_JetEta0to3_DOWN.Write()
            VBF_JetRelativeBal_UP.Write()
            VBF_JetRelativeBal_DOWN.Write()
            VBF_JetRelativeSample_UP.Write()
            VBF_JetRelativeSample_DOWN.Write()
            VBF_JetEta3to5_UP.Write()
            VBF_JetEta3to5_DOWN.Write()
            VBF_JetEta0to5_UP.Write()
            VBF_JetEta0to5_DOWN.Write()
        if args.MakeDYShape:
            VBF_DYShape_UP.Write()
            VBF_DYShape_DOWN.Write()
        if args.MakeZLShape:
            VBF_DM0_ZLShape_UP.Write()
            VBF_DM0_ZLShape_DOWN.Write()
            VBF_DM1_ZLShape_UP.Write()
            VBF_DM1_ZLShape_DOWN.Write()
        if args.MakeggHTheoryShape:
            VBF_THU_ggH_Mu_13TeVUp.Write()
            VBF_THU_ggH_Mu_13TeVDown.Write()
            VBF_THU_ggH_Res_13TeVUp.Write()
            VBF_THU_ggH_Res_13TeVDown.Write()
            VBF_THU_ggH_Mig01_13TeVUp.Write()
            VBF_THU_ggH_Mig01_13TeVDown.Write()
            VBF_THU_ggH_Mig12_13TeVUp.Write()
            VBF_THU_ggH_Mig12_13TeVDown.Write()
            VBF_THU_ggH_VBF2j_13TeVUp.Write()
            VBF_THU_ggH_VBF2j_13TeVDown.Write()
            VBF_THU_ggH_VBF3j_13TeVUp.Write()
            VBF_THU_ggH_VBF3j_13TeVDown.Write()
            VBF_THU_ggH_PT60_13TeVUp.Write()
            VBF_THU_ggH_PT60_13TeVDown.Write()
            VBF_THU_ggH_PT120_13TeVUp.Write()
            VBF_THU_ggH_PT120_13TeVDown.Write()
            VBF_THU_ggH_qmtop_13TeVUp.Write()
            VBF_THU_ggH_qmtop_13TeVDown.Write()
        if args.MakeRecoilUncertainties:
            VBF_ResolutionUp.Write()
            VBF_ResolutionDown.Write()
            VBF_ResponseUp.Write()
            VBF_ResponseDown.Write()
    else:
        VBF_TTBarContamination.Write()
    
    ResultFile.Write()
    ResultFile.Close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate rolled plots to be unrolled and fed to Combine.")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's plots are to be made")
    parser.add_argument('Files',nargs="+",help = "Files to run the tool on")
    parser.add_argument('--UseFakeFactor',help = "Use the file's fake factor weighting when making plots for this file.", action="store_true")
    parser.add_argument('--UseTES',help="Create the TES Uncertainty plots on these files",action="store_true")
    parser.add_argument('--UseJES',help="Create the JES Uncertainty plots on these files", action="store_true")
    parser.add_argument('--numZeroJetBins',nargs="?",help="Number of bins in zero jet category (m_vis 50-150)",default="20")
    parser.add_argument('--numBoostedBins',nargs="?",help="Number of bins in boosted category (m_sv 50-250)",default = "20")
    parser.add_argument('--numVBFBins',nargs="?",help="Number of bins in VBF category (m_sv 50-250)",default="20")
    parser.add_argument('--MakeDYShape',help="Make the DY shape using the UP-DOWN ZPT weights",action="store_true")
    parser.add_argument('--MakeZLShape',help="Make the ZL shape using EES and MES uncertainties",action="store_true")
    parser.add_argument('--MakeggHTheoryShape',help="Make the ggH Theory Uncertainty shape", action = "store_true")
    parser.add_argument('--MakeRecoilUncertainties',help="make recoil correction uncertainty plots",action="store_true")
    parser.add_argument('--MakeTTbarContamination',help="Make TTbar contamination plots (and only ttbar contamination plots!)",action="store_true")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing RolledHistograms for"+str(File))
        GenerateRolledPlots(File,args)
        
