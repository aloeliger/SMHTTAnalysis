//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Dec  4 03:18:37 2018 by ROOT version 6.10/09
// from TTree Ntuple/Expression Ntuple
// found on file: /hdfs/store/user/caillol/SMHTT_2017_29nov/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8__94X_mc2017_realistic_v14-v1/make_ntuples_cfg-922E611C-D741-E811-89D2-001E673D2EE9.root
//////////////////////////////////////////////////////////

#ifndef HTauTauTree_mt_h
#define HTauTauTree_mt_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class HTauTauTree_mt {
public :
   TTree          *_tree;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Float_t         DoubleMediumTau35Group;
   Float_t         DoubleMediumTau35Pass;
   Float_t         DoubleMediumTau35Prescale;
   Float_t         DoubleMediumTau40Group;
   Float_t         DoubleMediumTau40Pass;
   Float_t         DoubleMediumTau40Prescale;
   Float_t         DoubleTightTau35Group;
   Float_t         DoubleTightTau35Pass;
   Float_t         DoubleTightTau35Prescale;
   Float_t         DoubleTightTau40Group;
   Float_t         DoubleTightTau40Pass;
   Float_t         DoubleTightTau40Prescale;
   Float_t         Ele24Tau30Group;
   Float_t         Ele24Tau30Pass;
   Float_t         Ele24Tau30Prescale;
   Float_t         Ele27WPTightGroup;
   Float_t         Ele27WPTightPass;
   Float_t         Ele27WPTightPrescale;
   Float_t         Ele32WPTightGroup;
   Float_t         Ele32WPTightPass;
   Float_t         Ele32WPTightPrescale;
   Float_t         Ele35WPTightGroup;
   Float_t         Ele35WPTightPass;
   Float_t         Ele35WPTightPrescale;
   Float_t         EmbPtWeight;
   Float_t         Eta;
   Float_t         Flag_BadChargedCandidateFilter;
   Float_t         Flag_BadPFMuonFilter;
   Float_t         Flag_EcalDeadCellTriggerPrimitiveFilter;
   Float_t         Flag_HBHENoiseFilter;
   Float_t         Flag_HBHENoiseIsoFilter;
   Float_t         Flag_badMuons;
   Float_t         Flag_duplicateMuons;
   Float_t         Flag_ecalBadCalibFilter;
   Float_t         Flag_eeBadScFilter;
   Float_t         Flag_globalSuperTightHalo2016Filter;
   Float_t         Flag_globalTightHalo2016Filter;
   Float_t         Flag_goodVertices;
   Float_t         GenWeight;
   Float_t         Ht;
   Float_t         IsoMu20Group;
   Float_t         IsoMu20Pass;
   Float_t         IsoMu20Prescale;
   Float_t         IsoMu24Group;
   Float_t         IsoMu24Pass;
   Float_t         IsoMu24Prescale;
   Float_t         IsoMu24_eta2p1Group;
   Float_t         IsoMu24_eta2p1Pass;
   Float_t         IsoMu24_eta2p1Prescale;
   Float_t         IsoMu27Group;
   Float_t         IsoMu27Pass;
   Float_t         IsoMu27Prescale;
   Float_t         LT;
   Float_t         Mass;
   Float_t         MassError;
   Float_t         MassErrord1;
   Float_t         MassErrord2;
   Float_t         MassErrord3;
   Float_t         MassErrord4;
   Float_t         Mt;
   Float_t         Mu20Tau27Group;
   Float_t         Mu20Tau27Pass;
   Float_t         Mu20Tau27Prescale;
   Float_t         Mu50Group;
   Float_t         Mu50Pass;
   Float_t         Mu50Prescale;
   Float_t         NUP;
   Float_t         Phi;
   Float_t         Pt;
   Float_t         Rivet_VEta;
   Float_t         Rivet_VPt;
   Float_t         Rivet_errorCode;
   Float_t         Rivet_higgsEta;
   Float_t         Rivet_higgsPt;
   Float_t         Rivet_nJets25;
   Float_t         Rivet_nJets30;
   Float_t         Rivet_p4decay_VEta;
   Float_t         Rivet_p4decay_VPt;
   Float_t         Rivet_prodMode;
   Float_t         Rivet_stage0_cat;
   Float_t         Rivet_stage1_cat_pTjet25GeV;
   Float_t         Rivet_stage1_cat_pTjet30GeV;
   Float_t         bjetCISVVeto20Loose;
   Float_t         bjetCISVVeto20Medium;
   Float_t         bjetCISVVeto20MediumWoNoisyJets;
   Float_t         bjetCISVVeto20Tight;
   Float_t         bjetCISVVeto30Loose;
   Float_t         bjetCISVVeto30Medium;
   Float_t         bjetCISVVeto30Tight;
   Float_t         bjetDeepCSVVeto20Loose;
   Float_t         bjetDeepCSVVeto20Medium;
   Float_t         bjetDeepCSVVeto20MediumWoNoisyJets;
   Float_t         bjetDeepCSVVeto20Tight;
   Float_t         bjetDeepCSVVeto30Loose;
   Float_t         bjetDeepCSVVeto30Medium;
   Float_t         bjetDeepCSVVeto30Tight;
   Float_t         charge;
   Float_t         dielectronVeto;
   Float_t         dimuonVeto;
   Float_t         doubleE_23_12Group;
   Float_t         doubleE_23_12Pass;
   Float_t         doubleE_23_12Prescale;
   Float_t         doubleE_23_12_DZGroup;
   Float_t         doubleE_23_12_DZPass;
   Float_t         doubleE_23_12_DZPrescale;
   Float_t         doubleMuDZGroup;
   Float_t         doubleMuDZPass;
   Float_t         doubleMuDZPrescale;
   Float_t         doubleMuDZminMass3p8Group;
   Float_t         doubleMuDZminMass3p8Pass;
   Float_t         doubleMuDZminMass3p8Prescale;
   Float_t         doubleMuDZminMass8Group;
   Float_t         doubleMuDZminMass8Pass;
   Float_t         doubleMuDZminMass8Prescale;
   Float_t         eVetoMVAIso;
   Float_t         eVetoZTTp001dxyz;
   Float_t         eVetoZTTp001dxyzR0;
   ULong64_t       evt;
   Float_t         genEta;
   Float_t         genHTT;
   Float_t         genM;
   Float_t         genMass;
   Float_t         genPhi;
   Float_t         genpT;
   Float_t         genpX;
   Float_t         genpY;
   Int_t           isdata;
   Int_t           isembed;
   Float_t         j1csv;
   Float_t         j1csvWoNoisyJets;
   Float_t         j1eta;
   Float_t         j1etaWoNoisyJets;
   Float_t         j1hadronflavor;
   Float_t         j1hadronflavorWoNoisyJets;
   Float_t         j1phi;
   Float_t         j1phiWoNoisyJets;
   Float_t         j1pt;
   Float_t         j1ptWoNoisyJets;
   Float_t         j1ptWoNoisyJets_JetEta0to3Down;
   Float_t         j1ptWoNoisyJets_JetEta0to3Up;
   Float_t         j1ptWoNoisyJets_JetEta0to5Down;
   Float_t         j1ptWoNoisyJets_JetEta0to5Up;
   Float_t         j1ptWoNoisyJets_JetEta3to5Down;
   Float_t         j1ptWoNoisyJets_JetEta3to5Up;
   Float_t         j1ptWoNoisyJets_JetRelativeBalDown;
   Float_t         j1ptWoNoisyJets_JetRelativeBalUp;
   Float_t         j1ptWoNoisyJets_JetRelativeSampleDown;
   Float_t         j1ptWoNoisyJets_JetRelativeSampleUp;
   Float_t         j2csv;
   Float_t         j2csvWoNoisyJets;
   Float_t         j2eta;
   Float_t         j2etaWoNoisyJets;
   Float_t         j2hadronflavor;
   Float_t         j2hadronflavorWoNoisyJets;
   Float_t         j2phi;
   Float_t         j2phiWoNoisyJets;
   Float_t         j2pt;
   Float_t         j2ptWoNoisyJets;
   Float_t         j2ptWoNoisyJets_JetEta0to3Down;
   Float_t         j2ptWoNoisyJets_JetEta0to3Up;
   Float_t         j2ptWoNoisyJets_JetEta0to5Down;
   Float_t         j2ptWoNoisyJets_JetEta0to5Up;
   Float_t         j2ptWoNoisyJets_JetEta3to5Down;
   Float_t         j2ptWoNoisyJets_JetEta3to5Up;
   Float_t         j2ptWoNoisyJets_JetRelativeBalDown;
   Float_t         j2ptWoNoisyJets_JetRelativeBalUp;
   Float_t         j2ptWoNoisyJets_JetRelativeSampleDown;
   Float_t         j2ptWoNoisyJets_JetRelativeSampleUp;
   Float_t         jb1csv;
   Float_t         jb1csvWoNoisyJets;
   Float_t         jb1eta;
   Float_t         jb1etaWoNoisyJets;
   Float_t         jb1hadronflavor;
   Float_t         jb1hadronflavorWoNoisyJets;
   Float_t         jb1phi;
   Float_t         jb1phiWoNoisyJets;
   Float_t         jb1pt;
   Float_t         jb1ptWoNoisyJets;
   Float_t         jb2csv;
   Float_t         jb2csvWoNoisyJets;
   Float_t         jb2eta;
   Float_t         jb2etaWoNoisyJets;
   Float_t         jb2hadronflavor;
   Float_t         jb2hadronflavorWoNoisyJets;
   Float_t         jb2phi;
   Float_t         jb2phiWoNoisyJets;
   Float_t         jb2pt;
   Float_t         jb2ptWoNoisyJets;
   Float_t         jetVeto20;
   Float_t         jetVeto20WoNoisyJets;
   Float_t         jetVeto20_JetEnDown;
   Float_t         jetVeto20_JetEnUp;
   Float_t         jetVeto30;
   Float_t         jetVeto30WoNoisyJets;
   Float_t         jetVeto30WoNoisyJets_JetEta0to3Down;
   Float_t         jetVeto30WoNoisyJets_JetEta0to3Up;
   Float_t         jetVeto30WoNoisyJets_JetEta0to5Down;
   Float_t         jetVeto30WoNoisyJets_JetEta0to5Up;
   Float_t         jetVeto30WoNoisyJets_JetEta3to5Down;
   Float_t         jetVeto30WoNoisyJets_JetEta3to5Up;
   Float_t         jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets;
   Float_t         jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets;
   Float_t         jetVeto30WoNoisyJets_JetRelativeSampleDown;
   Float_t         jetVeto30WoNoisyJets_JetRelativeSampleUp;
   Float_t         jetVeto30WoNoisyJets_JetTotalDown;
   Float_t         jetVeto30WoNoisyJets_JetTotalUp;
   Float_t         jetVeto30_JetAbsoluteFlavMapDown;
   Float_t         jetVeto30_JetAbsoluteFlavMapUp;
   Float_t         jetVeto30_JetAbsoluteMPFBiasDown;
   Float_t         jetVeto30_JetAbsoluteMPFBiasUp;
   Float_t         jetVeto30_JetAbsoluteScaleDown;
   Float_t         jetVeto30_JetAbsoluteScaleUp;
   Float_t         jetVeto30_JetAbsoluteStatDown;
   Float_t         jetVeto30_JetAbsoluteStatUp;
   Float_t         jetVeto30_JetClosureDown;
   Float_t         jetVeto30_JetClosureUp;
   Float_t         jetVeto30_JetEnDown;
   Float_t         jetVeto30_JetEnUp;
   Float_t         jetVeto30_JetEta0to3Down;
   Float_t         jetVeto30_JetEta0to3Up;
   Float_t         jetVeto30_JetEta0to5Down;
   Float_t         jetVeto30_JetEta0to5Up;
   Float_t         jetVeto30_JetEta3to5Down;
   Float_t         jetVeto30_JetEta3to5Up;
   Float_t         jetVeto30_JetFlavorQCDDown;
   Float_t         jetVeto30_JetFlavorQCDUp;
   Float_t         jetVeto30_JetFragmentationDown;
   Float_t         jetVeto30_JetFragmentationUp;
   Float_t         jetVeto30_JetPileUpDataMCDown;
   Float_t         jetVeto30_JetPileUpDataMCUp;
   Float_t         jetVeto30_JetPileUpPtBBDown;
   Float_t         jetVeto30_JetPileUpPtBBUp;
   Float_t         jetVeto30_JetPileUpPtEC1Down;
   Float_t         jetVeto30_JetPileUpPtEC1Up;
   Float_t         jetVeto30_JetPileUpPtEC2Down;
   Float_t         jetVeto30_JetPileUpPtEC2Up;
   Float_t         jetVeto30_JetPileUpPtHFDown;
   Float_t         jetVeto30_JetPileUpPtHFUp;
   Float_t         jetVeto30_JetPileUpPtRefDown;
   Float_t         jetVeto30_JetPileUpPtRefUp;
   Float_t         jetVeto30_JetRelativeBalDown;
   Float_t         jetVeto30_JetRelativeBalUp;
   Float_t         jetVeto30_JetRelativeFSRDown;
   Float_t         jetVeto30_JetRelativeFSRUp;
   Float_t         jetVeto30_JetRelativeJEREC1Down;
   Float_t         jetVeto30_JetRelativeJEREC1Up;
   Float_t         jetVeto30_JetRelativeJEREC2Down;
   Float_t         jetVeto30_JetRelativeJEREC2Up;
   Float_t         jetVeto30_JetRelativeJERHFDown;
   Float_t         jetVeto30_JetRelativeJERHFUp;
   Float_t         jetVeto30_JetRelativePtBBDown;
   Float_t         jetVeto30_JetRelativePtBBUp;
   Float_t         jetVeto30_JetRelativePtEC1Down;
   Float_t         jetVeto30_JetRelativePtEC1Up;
   Float_t         jetVeto30_JetRelativePtEC2Down;
   Float_t         jetVeto30_JetRelativePtEC2Up;
   Float_t         jetVeto30_JetRelativePtHFDown;
   Float_t         jetVeto30_JetRelativePtHFUp;
   Float_t         jetVeto30_JetRelativeSampleDown;
   Float_t         jetVeto30_JetRelativeSampleUp;
   Float_t         jetVeto30_JetRelativeStatECDown;
   Float_t         jetVeto30_JetRelativeStatECUp;
   Float_t         jetVeto30_JetRelativeStatFSRDown;
   Float_t         jetVeto30_JetRelativeStatFSRUp;
   Float_t         jetVeto30_JetRelativeStatHFDown;
   Float_t         jetVeto30_JetRelativeStatHFUp;
   Float_t         jetVeto30_JetSinglePionECALDown;
   Float_t         jetVeto30_JetSinglePionECALUp;
   Float_t         jetVeto30_JetSinglePionHCALDown;
   Float_t         jetVeto30_JetSinglePionHCALUp;
   Float_t         jetVeto30_JetTimePtEtaDown;
   Float_t         jetVeto30_JetTimePtEtaUp;
   Float_t         jetVeto30_JetTotalDown;
   Float_t         jetVeto30_JetTotalUp;
   Int_t           lumi;
   Float_t         mBestTrackType;
   Float_t         mCharge;
   Float_t         mChi2LocalPosition;
   Float_t         mComesFromHiggs;
   Float_t         mCutBasedIdGlobalHighPt;
   Float_t         mCutBasedIdLoose;
   Float_t         mCutBasedIdMedium;
   Float_t         mCutBasedIdMediumPrompt;
   Float_t         mCutBasedIdTight;
   Float_t         mCutBasedIdTrkHighPt;
   Float_t         mEcalIsoDR03;
   Float_t         mEffectiveArea2011;
   Float_t         mEffectiveArea2012;
   Float_t         mEta;
   Float_t         mEta_MuonEnDown;
   Float_t         mEta_MuonEnUp;
   Float_t         mGenCharge;
   Float_t         mGenDirectPromptTauDecayFinalState;
   Float_t         mGenEnergy;
   Float_t         mGenEta;
   Float_t         mGenIsPrompt;
   Float_t         mGenMotherPdgId;
   Float_t         mGenParticle;
   Float_t         mGenPdgId;
   Float_t         mGenPhi;
   Float_t         mGenPrompt;
   Float_t         mGenPromptFinalState;
   Float_t         mGenPromptTauDecay;
   Float_t         mGenPt;
   Float_t         mGenTauDecay;
   Float_t         mGenVZ;
   Float_t         mGenVtxPVMatch;
   Float_t         mHcalIsoDR03;
   Float_t         mIP3D;
   Float_t         mIP3DErr;
   Float_t         mIsGlobal;
   Float_t         mIsPFMuon;
   Float_t         mIsTracker;
   Float_t         mIsoDB03;
   Float_t         mIsoDB04;
   Float_t         mJetArea;
   Float_t         mJetBtag;
   Float_t         mJetDR;
   Float_t         mJetEtaEtaMoment;
   Float_t         mJetEtaPhiMoment;
   Float_t         mJetEtaPhiSpread;
   Float_t         mJetHadronFlavour;
   Float_t         mJetPFCISVBtag;
   Float_t         mJetPartonFlavour;
   Float_t         mJetPhiPhiMoment;
   Float_t         mJetPt;
   Float_t         mLowestMll;
   Float_t         mMass;
   Float_t         mMatchedStations;
   Float_t         mMatchesIsoMu20Tau27Filter;
   Float_t         mMatchesIsoMu20Tau27Path;
   Float_t         mMatchesIsoMu24Filter;
   Float_t         mMatchesIsoMu24Path;
   Float_t         mMatchesIsoMu27Filter;
   Float_t         mMatchesIsoMu27Path;
   Float_t         mMiniIsoLoose;
   Float_t         mMiniIsoMedium;
   Float_t         mMiniIsoTight;
   Float_t         mMiniIsoVeryTight;
   Float_t         mMuonHits;
   Float_t         mMvaLoose;
   Float_t         mMvaMedium;
   Float_t         mMvaTight;
   Float_t         mNearestZMass;
   Float_t         mNormTrkChi2;
   Float_t         mNormalizedChi2;
   Float_t         mPFChargedHadronIsoR04;
   Float_t         mPFChargedIso;
   Float_t         mPFIDLoose;
   Float_t         mPFIDMedium;
   Float_t         mPFIDTight;
   Float_t         mPFIsoLoose;
   Float_t         mPFIsoMedium;
   Float_t         mPFIsoTight;
   Float_t         mPFIsoVeryLoose;
   Float_t         mPFIsoVeryTight;
   Float_t         mPFNeutralHadronIsoR04;
   Float_t         mPFNeutralIso;
   Float_t         mPFPUChargedIso;
   Float_t         mPFPhotonIso;
   Float_t         mPFPhotonIsoR04;
   Float_t         mPFPileupIsoR04;
   Float_t         mPVDXY;
   Float_t         mPVDZ;
   Float_t         mPhi;
   Float_t         mPhi_MuonEnDown;
   Float_t         mPhi_MuonEnUp;
   Float_t         mPixHits;
   Float_t         mPt;
   Float_t         mPt_MuonEnDown;
   Float_t         mPt_MuonEnUp;
   Float_t         mRelPFIsoDBDefault;
   Float_t         mRelPFIsoDBDefaultR04;
   Float_t         mRelPFIsoRho;
   Float_t         mRho;
   Float_t         mSIP2D;
   Float_t         mSIP3D;
   Float_t         mSegmentCompatibility;
   Float_t         mSoftCutBasedId;
   Float_t         mTkIsoLoose;
   Float_t         mTkIsoTight;
   Float_t         mTkLayersWithMeasurement;
   Float_t         mTrkIsoDR03;
   Float_t         mTrkKink;
   Int_t           mTypeCode;
   Float_t         mVZ;
   Float_t         mValidFraction;
   Float_t         mZTTGenMatching;
   Float_t         m_t_DR;
   Float_t         m_t_Mass;
   Float_t         m_t_doubleL1IsoTauMatch;
   Float_t         metSig;
   Float_t         metcov00;
   Float_t         metcov00_DESYlike;
   Float_t         metcov01;
   Float_t         metcov01_DESYlike;
   Float_t         metcov10;
   Float_t         metcov10_DESYlike;
   Float_t         metcov11;
   Float_t         metcov11_DESYlike;
   Float_t         mu12e23DZGroup;
   Float_t         mu12e23DZPass;
   Float_t         mu12e23DZPrescale;
   Float_t         mu12e23Group;
   Float_t         mu12e23Pass;
   Float_t         mu12e23Prescale;
   Float_t         mu23e12DZGroup;
   Float_t         mu23e12DZPass;
   Float_t         mu23e12DZPrescale;
   Float_t         mu23e12Group;
   Float_t         mu23e12Pass;
   Float_t         mu23e12Prescale;
   Float_t         muGlbIsoVetoPt10;
   Float_t         muVetoZTTp001dxyz;
   Float_t         muVetoZTTp001dxyzR0;
   Float_t         nTruePU;
   Float_t         npNLO;
   Float_t         numGenJets;
   Float_t         nvtx;
   Float_t         processID;
   Float_t         puppiMetEt;
   Float_t         puppiMetPhi;
   Float_t         pvChi2;
   Float_t         pvDX;
   Float_t         pvDY;
   Float_t         pvDZ;
   Int_t           pvIsFake;
   Int_t           pvIsValid;
   Float_t         pvNormChi2;
   Float_t         pvRho;
   Float_t         pvX;
   Float_t         pvY;
   Float_t         pvZ;
   Float_t         pvndof;
   Float_t         raw_pfMetEt;
   Float_t         raw_pfMetPhi;
   Float_t         recoilDaught;
   Float_t         recoilWithMet;
   Float_t         rho;
   Int_t           run;
   Float_t         tAgainstElectronLooseMVA6;
   Float_t         tAgainstElectronMVA6Raw;
   Float_t         tAgainstElectronMVA6category;
   Float_t         tAgainstElectronMediumMVA6;
   Float_t         tAgainstElectronTightMVA6;
   Float_t         tAgainstElectronVLooseMVA6;
   Float_t         tAgainstElectronVTightMVA6;
   Float_t         tAgainstMuonLoose3;
   Float_t         tAgainstMuonTight3;
   Float_t         tByCombinedIsolationDeltaBetaCorrRaw3Hits;
   Float_t         tByIsolationMVArun2v1DBdR03oldDMwLTraw;
   Float_t         tByIsolationMVArun2v1DBnewDMwLTraw;
   Float_t         tByIsolationMVArun2v1DBoldDMwLTraw;
   Float_t         tByLooseCombinedIsolationDeltaBetaCorr3Hits;
   Float_t         tByLooseIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByLooseIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByLooseIsolationMVArun2v1DBoldDMwLT;
   Float_t         tByMediumCombinedIsolationDeltaBetaCorr3Hits;
   Float_t         tByMediumIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByMediumIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByMediumIsolationMVArun2v1DBoldDMwLT;
   Float_t         tByPhotonPtSumOutsideSignalCone;
   Float_t         tByTightCombinedIsolationDeltaBetaCorr3Hits;
   Float_t         tByTightIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByTightIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByTightIsolationMVArun2v1DBoldDMwLT;
   Float_t         tByVLooseIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByVLooseIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByVLooseIsolationMVArun2v1DBoldDMwLT;
   Float_t         tByVTightIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByVTightIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByVTightIsolationMVArun2v1DBoldDMwLT;
   Float_t         tByVVTightIsolationMVArun2v1DBdR03oldDMwLT;
   Float_t         tByVVTightIsolationMVArun2v1DBnewDMwLT;
   Float_t         tByVVTightIsolationMVArun2v1DBoldDMwLT;
   Float_t         tCharge;
   Float_t         tChargedIsoPtSum;
   Float_t         tChargedIsoPtSumdR03;
   Float_t         tComesFromHiggs;
   Float_t         tDecayMode;
   Float_t         tDecayModeFinding;
   Float_t         tDecayModeFindingNewDMs;
   Float_t         tEta;
   Float_t         tFootprintCorrection;
   Float_t         tFootprintCorrectiondR03;
   Float_t         tGenCharge;
   Float_t         tGenDecayMode;
   Float_t         tGenEnergy;
   Float_t         tGenEta;
   Float_t         tGenJetEta;
   Float_t         tGenJetPt;
   Float_t         tGenMotherEnergy;
   Float_t         tGenMotherEta;
   Float_t         tGenMotherPdgId;
   Float_t         tGenMotherPhi;
   Float_t         tGenMotherPt;
   Float_t         tGenPdgId;
   Float_t         tGenPhi;
   Float_t         tGenPt;
   Float_t         tGenStatus;
   Float_t         tJetArea;
   Float_t         tJetBtag;
   Float_t         tJetDR;
   Float_t         tJetEtaEtaMoment;
   Float_t         tJetEtaPhiMoment;
   Float_t         tJetEtaPhiSpread;
   Float_t         tJetHadronFlavour;
   Float_t         tJetPFCISVBtag;
   Float_t         tJetPartonFlavour;
   Float_t         tJetPhiPhiMoment;
   Float_t         tJetPt;
   Float_t         tL1IsoTauMatch;
   Float_t         tL1IsoTauPt;
   Float_t         tLeadTrackPt;
   Float_t         tLowestMll;
   Float_t         tMass;
   Float_t         tMatchesDoubleMediumTau35Filter;
   Float_t         tMatchesDoubleMediumTau35Path;
   Float_t         tMatchesDoubleMediumTau40Filter;
   Float_t         tMatchesDoubleMediumTau40Path;
   Float_t         tMatchesDoubleTightTau35Filter;
   Float_t         tMatchesDoubleTightTau35Path;
   Float_t         tMatchesDoubleTightTau40Filter;
   Float_t         tMatchesDoubleTightTau40Path;
   Float_t         tMatchesEle24Tau30Filter;
   Float_t         tMatchesEle24Tau30Path;
   Float_t         tMatchesIsoMu20Tau27Filter;
   Float_t         tMatchesIsoMu20Tau27Path;
   Float_t         tNChrgHadrIsolationCands;
   Float_t         tNChrgHadrSignalCands;
   Float_t         tNGammaSignalCands;
   Float_t         tNNeutralHadrSignalCands;
   Float_t         tNSignalCands;
   Float_t         tNearestZMass;
   Float_t         tNeutralIsoPtSum;
   Float_t         tNeutralIsoPtSumWeight;
   Float_t         tNeutralIsoPtSumWeightdR03;
   Float_t         tNeutralIsoPtSumdR03;
   Float_t         tPVDXY;
   Float_t         tPVDZ;
   Float_t         tPhi;
   Float_t         tPhotonPtSumOutsideSignalCone;
   Float_t         tPhotonPtSumOutsideSignalConedR03;
   Float_t         tPt;
   Float_t         tPuCorrPtSum;
   Float_t         tRerunMVArun2v1DBoldDMwLTLoose;
   Float_t         tRerunMVArun2v1DBoldDMwLTMedium;
   Float_t         tRerunMVArun2v1DBoldDMwLTTight;
   Float_t         tRerunMVArun2v1DBoldDMwLTVLoose;
   Float_t         tRerunMVArun2v1DBoldDMwLTVTight;
   Float_t         tRerunMVArun2v1DBoldDMwLTVVTight;
   Float_t         tRerunMVArun2v1DBoldDMwLTraw;
   Float_t         tRerunMVArun2v2DBoldDMwLTLoose;
   Float_t         tRerunMVArun2v2DBoldDMwLTMedium;
   Float_t         tRerunMVArun2v2DBoldDMwLTTight;
   Float_t         tRerunMVArun2v2DBoldDMwLTVLoose;
   Float_t         tRerunMVArun2v2DBoldDMwLTVTight;
   Float_t         tRerunMVArun2v2DBoldDMwLTVVLoose;
   Float_t         tRerunMVArun2v2DBoldDMwLTVVTight;
   Float_t         tRerunMVArun2v2DBoldDMwLTraw;
   Float_t         tVZ;
   Float_t         tZTTGenDR;
   Float_t         tZTTGenEta;
   Float_t         tZTTGenMatching;
   Float_t         tZTTGenPhi;
   Float_t         tZTTGenPt;
   Float_t         tauVetoPt20Loose3HitsVtx;
   Float_t         tauVetoPt20TightMVALTVtx;
   Float_t         topQuarkPt1;
   Float_t         topQuarkPt2;
   Float_t         tripleEGroup;
   Float_t         tripleEPass;
   Float_t         tripleEPrescale;
   Float_t         tripleMu12_10_5Group;
   Float_t         tripleMu12_10_5Pass;
   Float_t         tripleMu12_10_5Prescale;
   Float_t         type1_pfMetEt;
   Float_t         type1_pfMetPhi;
   Float_t         type1_pfMet_shiftedPhi_JetEnDown;
   Float_t         type1_pfMet_shiftedPhi_JetEnUp;
   Float_t         type1_pfMet_shiftedPhi_JetEta0to3Down;
   Float_t         type1_pfMet_shiftedPhi_JetEta0to3Up;
   Float_t         type1_pfMet_shiftedPhi_JetEta0to5Down;
   Float_t         type1_pfMet_shiftedPhi_JetEta0to5Up;
   Float_t         type1_pfMet_shiftedPhi_JetEta3to5Down;
   Float_t         type1_pfMet_shiftedPhi_JetEta3to5Up;
   Float_t         type1_pfMet_shiftedPhi_JetRelativeBalDown;
   Float_t         type1_pfMet_shiftedPhi_JetRelativeBalUp;
   Float_t         type1_pfMet_shiftedPhi_JetRelativeSampleDown;
   Float_t         type1_pfMet_shiftedPhi_JetRelativeSampleUp;
   Float_t         type1_pfMet_shiftedPhi_JetResDown;
   Float_t         type1_pfMet_shiftedPhi_JetResUp;
   Float_t         type1_pfMet_shiftedPhi_JetTotalDown;
   Float_t         type1_pfMet_shiftedPhi_JetTotalUp;
   Float_t         type1_pfMet_shiftedPhi_UnclusteredEnDown;
   Float_t         type1_pfMet_shiftedPhi_UnclusteredEnUp;
   Float_t         type1_pfMet_shiftedPt_JetEnDown;
   Float_t         type1_pfMet_shiftedPt_JetEnUp;
   Float_t         type1_pfMet_shiftedPt_JetEta0to3Down;
   Float_t         type1_pfMet_shiftedPt_JetEta0to3Up;
   Float_t         type1_pfMet_shiftedPt_JetEta0to5Down;
   Float_t         type1_pfMet_shiftedPt_JetEta0to5Up;
   Float_t         type1_pfMet_shiftedPt_JetEta3to5Down;
   Float_t         type1_pfMet_shiftedPt_JetEta3to5Up;
   Float_t         type1_pfMet_shiftedPt_JetRelativeBalDown;
   Float_t         type1_pfMet_shiftedPt_JetRelativeBalUp;
   Float_t         type1_pfMet_shiftedPt_JetRelativeSampleDown;
   Float_t         type1_pfMet_shiftedPt_JetRelativeSampleUp;
   Float_t         type1_pfMet_shiftedPt_JetResDown;
   Float_t         type1_pfMet_shiftedPt_JetResUp;
   Float_t         type1_pfMet_shiftedPt_JetTotalDown;
   Float_t         type1_pfMet_shiftedPt_JetTotalUp;
   Float_t         type1_pfMet_shiftedPt_UnclusteredEnDown;
   Float_t         type1_pfMet_shiftedPt_UnclusteredEnUp;
   Float_t         vbfDeta;
   Float_t         vbfJetVeto20;
   Float_t         vbfJetVeto30;
   Float_t         vbfMass;
   Float_t         vbfMassWoNoisyJets;
   Float_t         vbfMassWoNoisyJets_JetEta0to3Down;
   Float_t         vbfMassWoNoisyJets_JetEta0to3Up;
   Float_t         vbfMassWoNoisyJets_JetEta0to5Down;
   Float_t         vbfMassWoNoisyJets_JetEta0to5Up;
   Float_t         vbfMassWoNoisyJets_JetEta3to5Down;
   Float_t         vbfMassWoNoisyJets_JetEta3to5Up;
   Float_t         vbfMassWoNoisyJets_JetRelativeBalDown;
   Float_t         vbfMassWoNoisyJets_JetRelativeBalUp;
   Float_t         vbfMassWoNoisyJets_JetRelativeSampleDown;
   Float_t         vbfMassWoNoisyJets_JetRelativeSampleUp;
   Float_t         vbfMassWoNoisyJets_JetTotalDown;
   Float_t         vbfMassWoNoisyJets_JetTotalUp;
   Float_t         vbfMass_JetAbsoluteFlavMapDown;
   Float_t         vbfMass_JetAbsoluteFlavMapUp;
   Float_t         vbfMass_JetAbsoluteMPFBiasDown;
   Float_t         vbfMass_JetAbsoluteMPFBiasUp;
   Float_t         vbfMass_JetAbsoluteScaleDown;
   Float_t         vbfMass_JetAbsoluteScaleUp;
   Float_t         vbfMass_JetAbsoluteStatDown;
   Float_t         vbfMass_JetAbsoluteStatUp;
   Float_t         vbfMass_JetClosureDown;
   Float_t         vbfMass_JetClosureUp;
   Float_t         vbfMass_JetEta0to3Down;
   Float_t         vbfMass_JetEta0to3Up;
   Float_t         vbfMass_JetEta0to5Down;
   Float_t         vbfMass_JetEta0to5Up;
   Float_t         vbfMass_JetEta3to5Down;
   Float_t         vbfMass_JetEta3to5Up;
   Float_t         vbfMass_JetFlavorQCDDown;
   Float_t         vbfMass_JetFlavorQCDUp;
   Float_t         vbfMass_JetFragmentationDown;
   Float_t         vbfMass_JetFragmentationUp;
   Float_t         vbfMass_JetPileUpDataMCDown;
   Float_t         vbfMass_JetPileUpDataMCUp;
   Float_t         vbfMass_JetPileUpPtBBDown;
   Float_t         vbfMass_JetPileUpPtBBUp;
   Float_t         vbfMass_JetPileUpPtEC1Down;
   Float_t         vbfMass_JetPileUpPtEC1Up;
   Float_t         vbfMass_JetPileUpPtEC2Down;
   Float_t         vbfMass_JetPileUpPtEC2Up;
   Float_t         vbfMass_JetPileUpPtHFDown;
   Float_t         vbfMass_JetPileUpPtHFUp;
   Float_t         vbfMass_JetPileUpPtRefDown;
   Float_t         vbfMass_JetPileUpPtRefUp;
   Float_t         vbfMass_JetRelativeBalDown;
   Float_t         vbfMass_JetRelativeBalUp;
   Float_t         vbfMass_JetRelativeFSRDown;
   Float_t         vbfMass_JetRelativeFSRUp;
   Float_t         vbfMass_JetRelativeJEREC1Down;
   Float_t         vbfMass_JetRelativeJEREC1Up;
   Float_t         vbfMass_JetRelativeJEREC2Down;
   Float_t         vbfMass_JetRelativeJEREC2Up;
   Float_t         vbfMass_JetRelativeJERHFDown;
   Float_t         vbfMass_JetRelativeJERHFUp;
   Float_t         vbfMass_JetRelativePtBBDown;
   Float_t         vbfMass_JetRelativePtBBUp;
   Float_t         vbfMass_JetRelativePtEC1Down;
   Float_t         vbfMass_JetRelativePtEC1Up;
   Float_t         vbfMass_JetRelativePtEC2Down;
   Float_t         vbfMass_JetRelativePtEC2Up;
   Float_t         vbfMass_JetRelativePtHFDown;
   Float_t         vbfMass_JetRelativePtHFUp;
   Float_t         vbfMass_JetRelativeSampleDown;
   Float_t         vbfMass_JetRelativeSampleUp;
   Float_t         vbfMass_JetRelativeStatECDown;
   Float_t         vbfMass_JetRelativeStatECUp;
   Float_t         vbfMass_JetRelativeStatFSRDown;
   Float_t         vbfMass_JetRelativeStatFSRUp;
   Float_t         vbfMass_JetRelativeStatHFDown;
   Float_t         vbfMass_JetRelativeStatHFUp;
   Float_t         vbfMass_JetSinglePionECALDown;
   Float_t         vbfMass_JetSinglePionECALUp;
   Float_t         vbfMass_JetSinglePionHCALDown;
   Float_t         vbfMass_JetSinglePionHCALUp;
   Float_t         vbfMass_JetTimePtEtaDown;
   Float_t         vbfMass_JetTimePtEtaUp;
   Float_t         vbfMass_JetTotalDown;
   Float_t         vbfMass_JetTotalUp;
   Float_t         vbfNJets20;
   Float_t         vbfNJets30;
   Float_t         vbfj1eta;
   Float_t         vbfj1pt;
   Float_t         vbfj2eta;
   Float_t         vbfj2pt;
   Float_t         vispX;
   Float_t         vispY;
   Int_t           idx;

   // List of branches
   TBranch        *b_DoubleMediumTau35Group;   //!
   TBranch        *b_DoubleMediumTau35Pass;   //!
   TBranch        *b_DoubleMediumTau35Prescale;   //!
   TBranch        *b_DoubleMediumTau40Group;   //!
   TBranch        *b_DoubleMediumTau40Pass;   //!
   TBranch        *b_DoubleMediumTau40Prescale;   //!
   TBranch        *b_DoubleTightTau35Group;   //!
   TBranch        *b_DoubleTightTau35Pass;   //!
   TBranch        *b_DoubleTightTau35Prescale;   //!
   TBranch        *b_DoubleTightTau40Group;   //!
   TBranch        *b_DoubleTightTau40Pass;   //!
   TBranch        *b_DoubleTightTau40Prescale;   //!
   TBranch        *b_Ele24Tau30Group;   //!
   TBranch        *b_Ele24Tau30Pass;   //!
   TBranch        *b_Ele24Tau30Prescale;   //!
   TBranch        *b_Ele27WPTightGroup;   //!
   TBranch        *b_Ele27WPTightPass;   //!
   TBranch        *b_Ele27WPTightPrescale;   //!
   TBranch        *b_Ele32WPTightGroup;   //!
   TBranch        *b_Ele32WPTightPass;   //!
   TBranch        *b_Ele32WPTightPrescale;   //!
   TBranch        *b_Ele35WPTightGroup;   //!
   TBranch        *b_Ele35WPTightPass;   //!
   TBranch        *b_Ele35WPTightPrescale;   //!
   TBranch        *b_EmbPtWeight;   //!
   TBranch        *b_Eta;   //!
   TBranch        *b_Flag_BadChargedCandidateFilter;   //!
   TBranch        *b_Flag_BadPFMuonFilter;   //!
   TBranch        *b_Flag_EcalDeadCellTriggerPrimitiveFilter;   //!
   TBranch        *b_Flag_HBHENoiseFilter;   //!
   TBranch        *b_Flag_HBHENoiseIsoFilter;   //!
   TBranch        *b_Flag_badMuons;   //!
   TBranch        *b_Flag_duplicateMuons;   //!
   TBranch        *b_Flag_ecalBadCalibFilter;   //!
   TBranch        *b_Flag_eeBadScFilter;   //!
   TBranch        *b_Flag_globalSuperTightHalo2016Filter;   //!
   TBranch        *b_Flag_globalTightHalo2016Filter;   //!
   TBranch        *b_Flag_goodVertices;   //!
   TBranch        *b_GenWeight;   //!
   TBranch        *b_Ht;   //!
   TBranch        *b_IsoMu20Group;   //!
   TBranch        *b_IsoMu20Pass;   //!
   TBranch        *b_IsoMu20Prescale;   //!
   TBranch        *b_IsoMu24Group;   //!
   TBranch        *b_IsoMu24Pass;   //!
   TBranch        *b_IsoMu24Prescale;   //!
   TBranch        *b_IsoMu24_eta2p1Group;   //!
   TBranch        *b_IsoMu24_eta2p1Pass;   //!
   TBranch        *b_IsoMu24_eta2p1Prescale;   //!
   TBranch        *b_IsoMu27Group;   //!
   TBranch        *b_IsoMu27Pass;   //!
   TBranch        *b_IsoMu27Prescale;   //!
   TBranch        *b_LT;   //!
   TBranch        *b_Mass;   //!
   TBranch        *b_MassError;   //!
   TBranch        *b_MassErrord1;   //!
   TBranch        *b_MassErrord2;   //!
   TBranch        *b_MassErrord3;   //!
   TBranch        *b_MassErrord4;   //!
   TBranch        *b_Mt;   //!
   TBranch        *b_Mu20Tau27Group;   //!
   TBranch        *b_Mu20Tau27Pass;   //!
   TBranch        *b_Mu20Tau27Prescale;   //!
   TBranch        *b_Mu50Group;   //!
   TBranch        *b_Mu50Pass;   //!
   TBranch        *b_Mu50Prescale;   //!
   TBranch        *b_NUP;   //!
   TBranch        *b_Phi;   //!
   TBranch        *b_Pt;   //!
   TBranch        *b_Rivet_VEta;   //!
   TBranch        *b_Rivet_VPt;   //!
   TBranch        *b_Rivet_errorCode;   //!
   TBranch        *b_Rivet_higgsEta;   //!
   TBranch        *b_Rivet_higgsPt;   //!
   TBranch        *b_Rivet_nJets25;   //!
   TBranch        *b_Rivet_nJets30;   //!
   TBranch        *b_Rivet_p4decay_VEta;   //!
   TBranch        *b_Rivet_p4decay_VPt;   //!
   TBranch        *b_Rivet_prodMode;   //!
   TBranch        *b_Rivet_stage0_cat;   //!
   TBranch        *b_Rivet_stage1_cat_pTjet25GeV;   //!
   TBranch        *b_Rivet_stage1_cat_pTjet30GeV;   //!
   TBranch        *b_bjetCISVVeto20Loose;   //!
   TBranch        *b_bjetCISVVeto20Medium;   //!
   TBranch        *b_bjetCISVVeto20MediumWoNoisyJets;   //!
   TBranch        *b_bjetCISVVeto20Tight;   //!
   TBranch        *b_bjetCISVVeto30Loose;   //!
   TBranch        *b_bjetCISVVeto30Medium;   //!
   TBranch        *b_bjetCISVVeto30Tight;   //!
   TBranch        *b_bjetDeepCSVVeto20Loose;   //!
   TBranch        *b_bjetDeepCSVVeto20Medium;   //!
   TBranch        *b_bjetDeepCSVVeto20MediumWoNoisyJets;   //!
   TBranch        *b_bjetDeepCSVVeto20Tight;   //!
   TBranch        *b_bjetDeepCSVVeto30Loose;   //!
   TBranch        *b_bjetDeepCSVVeto30Medium;   //!
   TBranch        *b_bjetDeepCSVVeto30Tight;   //!
   TBranch        *b_charge;   //!
   TBranch        *b_dielectronVeto;   //!
   TBranch        *b_dimuonVeto;   //!
   TBranch        *b_doubleE_23_12Group;   //!
   TBranch        *b_doubleE_23_12Pass;   //!
   TBranch        *b_doubleE_23_12Prescale;   //!
   TBranch        *b_doubleE_23_12_DZGroup;   //!
   TBranch        *b_doubleE_23_12_DZPass;   //!
   TBranch        *b_doubleE_23_12_DZPrescale;   //!
   TBranch        *b_doubleMuDZGroup;   //!
   TBranch        *b_doubleMuDZPass;   //!
   TBranch        *b_doubleMuDZPrescale;   //!
   TBranch        *b_doubleMuDZminMass3p8Group;   //!
   TBranch        *b_doubleMuDZminMass3p8Pass;   //!
   TBranch        *b_doubleMuDZminMass3p8Prescale;   //!
   TBranch        *b_doubleMuDZminMass8Group;   //!
   TBranch        *b_doubleMuDZminMass8Pass;   //!
   TBranch        *b_doubleMuDZminMass8Prescale;   //!
   TBranch        *b_eVetoMVAIso;   //!
   TBranch        *b_eVetoZTTp001dxyz;   //!
   TBranch        *b_eVetoZTTp001dxyzR0;   //!
   TBranch        *b_evt;   //!
   TBranch        *b_genEta;   //!
   TBranch        *b_genHTT;   //!
   TBranch        *b_genM;   //!
   TBranch        *b_genMass;   //!
   TBranch        *b_genPhi;   //!
   TBranch        *b_genpT;   //!
   TBranch        *b_genpX;   //!
   TBranch        *b_genpY;   //!
   TBranch        *b_isdata;   //!
   TBranch        *b_isembed;   //!
   TBranch        *b_j1csv;   //!
   TBranch        *b_j1csvWoNoisyJets;   //!
   TBranch        *b_j1eta;   //!
   TBranch        *b_j1etaWoNoisyJets;   //!
   TBranch        *b_j1hadronflavor;   //!
   TBranch        *b_j1hadronflavorWoNoisyJets;   //!
   TBranch        *b_j1phi;   //!
   TBranch        *b_j1phiWoNoisyJets;   //!
   TBranch        *b_j1pt;   //!
   TBranch        *b_j1ptWoNoisyJets;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta0to3Down;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta0to3Up;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta0to5Down;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta0to5Up;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta3to5Down;   //!
   TBranch        *b_j1ptWoNoisyJets_JetEta3to5Up;   //!
   TBranch        *b_j1ptWoNoisyJets_JetRelativeBalDown;   //!
   TBranch        *b_j1ptWoNoisyJets_JetRelativeBalUp;   //!
   TBranch        *b_j1ptWoNoisyJets_JetRelativeSampleDown;   //!
   TBranch        *b_j1ptWoNoisyJets_JetRelativeSampleUp;   //!
   TBranch        *b_j2csv;   //!
   TBranch        *b_j2csvWoNoisyJets;   //!
   TBranch        *b_j2eta;   //!
   TBranch        *b_j2etaWoNoisyJets;   //!
   TBranch        *b_j2hadronflavor;   //!
   TBranch        *b_j2hadronflavorWoNoisyJets;   //!
   TBranch        *b_j2phi;   //!
   TBranch        *b_j2phiWoNoisyJets;   //!
   TBranch        *b_j2pt;   //!
   TBranch        *b_j2ptWoNoisyJets;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta0to3Down;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta0to3Up;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta0to5Down;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta0to5Up;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta3to5Down;   //!
   TBranch        *b_j2ptWoNoisyJets_JetEta3to5Up;   //!
   TBranch        *b_j2ptWoNoisyJets_JetRelativeBalDown;   //!
   TBranch        *b_j2ptWoNoisyJets_JetRelativeBalUp;   //!
   TBranch        *b_j2ptWoNoisyJets_JetRelativeSampleDown;   //!
   TBranch        *b_j2ptWoNoisyJets_JetRelativeSampleUp;   //!
   TBranch        *b_jb1csv;   //!
   TBranch        *b_jb1csvWoNoisyJets;   //!
   TBranch        *b_jb1eta;   //!
   TBranch        *b_jb1etaWoNoisyJets;   //!
   TBranch        *b_jb1hadronflavor;   //!
   TBranch        *b_jb1hadronflavorWoNoisyJets;   //!
   TBranch        *b_jb1phi;   //!
   TBranch        *b_jb1phiWoNoisyJets;   //!
   TBranch        *b_jb1pt;   //!
   TBranch        *b_jb1ptWoNoisyJets;   //!
   TBranch        *b_jb2csv;   //!
   TBranch        *b_jb2csvWoNoisyJets;   //!
   TBranch        *b_jb2eta;   //!
   TBranch        *b_jb2etaWoNoisyJets;   //!
   TBranch        *b_jb2hadronflavor;   //!
   TBranch        *b_jb2hadronflavorWoNoisyJets;   //!
   TBranch        *b_jb2phi;   //!
   TBranch        *b_jb2phiWoNoisyJets;   //!
   TBranch        *b_jb2pt;   //!
   TBranch        *b_jb2ptWoNoisyJets;   //!
   TBranch        *b_jetVeto20;   //!
   TBranch        *b_jetVeto20WoNoisyJets;   //!
   TBranch        *b_jetVeto20_JetEnDown;   //!
   TBranch        *b_jetVeto20_JetEnUp;   //!
   TBranch        *b_jetVeto30;   //!
   TBranch        *b_jetVeto30WoNoisyJets;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta0to3Down;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta0to3Up;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta0to5Down;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta0to5Up;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta3to5Down;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetEta3to5Up;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetRelativeSampleDown;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetRelativeSampleUp;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetTotalDown;   //!
   TBranch        *b_jetVeto30WoNoisyJets_JetTotalUp;   //!
   TBranch        *b_jetVeto30_JetAbsoluteFlavMapDown;   //!
   TBranch        *b_jetVeto30_JetAbsoluteFlavMapUp;   //!
   TBranch        *b_jetVeto30_JetAbsoluteMPFBiasDown;   //!
   TBranch        *b_jetVeto30_JetAbsoluteMPFBiasUp;   //!
   TBranch        *b_jetVeto30_JetAbsoluteScaleDown;   //!
   TBranch        *b_jetVeto30_JetAbsoluteScaleUp;   //!
   TBranch        *b_jetVeto30_JetAbsoluteStatDown;   //!
   TBranch        *b_jetVeto30_JetAbsoluteStatUp;   //!
   TBranch        *b_jetVeto30_JetClosureDown;   //!
   TBranch        *b_jetVeto30_JetClosureUp;   //!
   TBranch        *b_jetVeto30_JetEnDown;   //!
   TBranch        *b_jetVeto30_JetEnUp;   //!
   TBranch        *b_jetVeto30_JetEta0to3Down;   //!
   TBranch        *b_jetVeto30_JetEta0to3Up;   //!
   TBranch        *b_jetVeto30_JetEta0to5Down;   //!
   TBranch        *b_jetVeto30_JetEta0to5Up;   //!
   TBranch        *b_jetVeto30_JetEta3to5Down;   //!
   TBranch        *b_jetVeto30_JetEta3to5Up;   //!
   TBranch        *b_jetVeto30_JetFlavorQCDDown;   //!
   TBranch        *b_jetVeto30_JetFlavorQCDUp;   //!
   TBranch        *b_jetVeto30_JetFragmentationDown;   //!
   TBranch        *b_jetVeto30_JetFragmentationUp;   //!
   TBranch        *b_jetVeto30_JetPileUpDataMCDown;   //!
   TBranch        *b_jetVeto30_JetPileUpDataMCUp;   //!
   TBranch        *b_jetVeto30_JetPileUpPtBBDown;   //!
   TBranch        *b_jetVeto30_JetPileUpPtBBUp;   //!
   TBranch        *b_jetVeto30_JetPileUpPtEC1Down;   //!
   TBranch        *b_jetVeto30_JetPileUpPtEC1Up;   //!
   TBranch        *b_jetVeto30_JetPileUpPtEC2Down;   //!
   TBranch        *b_jetVeto30_JetPileUpPtEC2Up;   //!
   TBranch        *b_jetVeto30_JetPileUpPtHFDown;   //!
   TBranch        *b_jetVeto30_JetPileUpPtHFUp;   //!
   TBranch        *b_jetVeto30_JetPileUpPtRefDown;   //!
   TBranch        *b_jetVeto30_JetPileUpPtRefUp;   //!
   TBranch        *b_jetVeto30_JetRelativeBalDown;   //!
   TBranch        *b_jetVeto30_JetRelativeBalUp;   //!
   TBranch        *b_jetVeto30_JetRelativeFSRDown;   //!
   TBranch        *b_jetVeto30_JetRelativeFSRUp;   //!
   TBranch        *b_jetVeto30_JetRelativeJEREC1Down;   //!
   TBranch        *b_jetVeto30_JetRelativeJEREC1Up;   //!
   TBranch        *b_jetVeto30_JetRelativeJEREC2Down;   //!
   TBranch        *b_jetVeto30_JetRelativeJEREC2Up;   //!
   TBranch        *b_jetVeto30_JetRelativeJERHFDown;   //!
   TBranch        *b_jetVeto30_JetRelativeJERHFUp;   //!
   TBranch        *b_jetVeto30_JetRelativePtBBDown;   //!
   TBranch        *b_jetVeto30_JetRelativePtBBUp;   //!
   TBranch        *b_jetVeto30_JetRelativePtEC1Down;   //!
   TBranch        *b_jetVeto30_JetRelativePtEC1Up;   //!
   TBranch        *b_jetVeto30_JetRelativePtEC2Down;   //!
   TBranch        *b_jetVeto30_JetRelativePtEC2Up;   //!
   TBranch        *b_jetVeto30_JetRelativePtHFDown;   //!
   TBranch        *b_jetVeto30_JetRelativePtHFUp;   //!
   TBranch        *b_jetVeto30_JetRelativeSampleDown;   //!
   TBranch        *b_jetVeto30_JetRelativeSampleUp;   //!
   TBranch        *b_jetVeto30_JetRelativeStatECDown;   //!
   TBranch        *b_jetVeto30_JetRelativeStatECUp;   //!
   TBranch        *b_jetVeto30_JetRelativeStatFSRDown;   //!
   TBranch        *b_jetVeto30_JetRelativeStatFSRUp;   //!
   TBranch        *b_jetVeto30_JetRelativeStatHFDown;   //!
   TBranch        *b_jetVeto30_JetRelativeStatHFUp;   //!
   TBranch        *b_jetVeto30_JetSinglePionECALDown;   //!
   TBranch        *b_jetVeto30_JetSinglePionECALUp;   //!
   TBranch        *b_jetVeto30_JetSinglePionHCALDown;   //!
   TBranch        *b_jetVeto30_JetSinglePionHCALUp;   //!
   TBranch        *b_jetVeto30_JetTimePtEtaDown;   //!
   TBranch        *b_jetVeto30_JetTimePtEtaUp;   //!
   TBranch        *b_jetVeto30_JetTotalDown;   //!
   TBranch        *b_jetVeto30_JetTotalUp;   //!
   TBranch        *b_lumi;   //!
   TBranch        *b_mBestTrackType;   //!
   TBranch        *b_mCharge;   //!
   TBranch        *b_mChi2LocalPosition;   //!
   TBranch        *b_mComesFromHiggs;   //!
   TBranch        *b_mCutBasedIdGlobalHighPt;   //!
   TBranch        *b_mCutBasedIdLoose;   //!
   TBranch        *b_mCutBasedIdMedium;   //!
   TBranch        *b_mCutBasedIdMediumPrompt;   //!
   TBranch        *b_mCutBasedIdTight;   //!
   TBranch        *b_mCutBasedIdTrkHighPt;   //!
   TBranch        *b_mEcalIsoDR03;   //!
   TBranch        *b_mEffectiveArea2011;   //!
   TBranch        *b_mEffectiveArea2012;   //!
   TBranch        *b_mEta;   //!
   TBranch        *b_mEta_MuonEnDown;   //!
   TBranch        *b_mEta_MuonEnUp;   //!
   TBranch        *b_mGenCharge;   //!
   TBranch        *b_mGenDirectPromptTauDecayFinalState;   //!
   TBranch        *b_mGenEnergy;   //!
   TBranch        *b_mGenEta;   //!
   TBranch        *b_mGenIsPrompt;   //!
   TBranch        *b_mGenMotherPdgId;   //!
   TBranch        *b_mGenParticle;   //!
   TBranch        *b_mGenPdgId;   //!
   TBranch        *b_mGenPhi;   //!
   TBranch        *b_mGenPrompt;   //!
   TBranch        *b_mGenPromptFinalState;   //!
   TBranch        *b_mGenPromptTauDecay;   //!
   TBranch        *b_mGenPt;   //!
   TBranch        *b_mGenTauDecay;   //!
   TBranch        *b_mGenVZ;   //!
   TBranch        *b_mGenVtxPVMatch;   //!
   TBranch        *b_mHcalIsoDR03;   //!
   TBranch        *b_mIP3D;   //!
   TBranch        *b_mIP3DErr;   //!
   TBranch        *b_mIsGlobal;   //!
   TBranch        *b_mIsPFMuon;   //!
   TBranch        *b_mIsTracker;   //!
   TBranch        *b_mIsoDB03;   //!
   TBranch        *b_mIsoDB04;   //!
   TBranch        *b_mJetArea;   //!
   TBranch        *b_mJetBtag;   //!
   TBranch        *b_mJetDR;   //!
   TBranch        *b_mJetEtaEtaMoment;   //!
   TBranch        *b_mJetEtaPhiMoment;   //!
   TBranch        *b_mJetEtaPhiSpread;   //!
   TBranch        *b_mJetHadronFlavour;   //!
   TBranch        *b_mJetPFCISVBtag;   //!
   TBranch        *b_mJetPartonFlavour;   //!
   TBranch        *b_mJetPhiPhiMoment;   //!
   TBranch        *b_mJetPt;   //!
   TBranch        *b_mLowestMll;   //!
   TBranch        *b_mMass;   //!
   TBranch        *b_mMatchedStations;   //!
   TBranch        *b_mMatchesIsoMu20Tau27Filter;   //!
   TBranch        *b_mMatchesIsoMu20Tau27Path;   //!
   TBranch        *b_mMatchesIsoMu24Filter;   //!
   TBranch        *b_mMatchesIsoMu24Path;   //!
   TBranch        *b_mMatchesIsoMu27Filter;   //!
   TBranch        *b_mMatchesIsoMu27Path;   //!
   TBranch        *b_mMiniIsoLoose;   //!
   TBranch        *b_mMiniIsoMedium;   //!
   TBranch        *b_mMiniIsoTight;   //!
   TBranch        *b_mMiniIsoVeryTight;   //!
   TBranch        *b_mMuonHits;   //!
   TBranch        *b_mMvaLoose;   //!
   TBranch        *b_mMvaMedium;   //!
   TBranch        *b_mMvaTight;   //!
   TBranch        *b_mNearestZMass;   //!
   TBranch        *b_mNormTrkChi2;   //!
   TBranch        *b_mNormalizedChi2;   //!
   TBranch        *b_mPFChargedHadronIsoR04;   //!
   TBranch        *b_mPFChargedIso;   //!
   TBranch        *b_mPFIDLoose;   //!
   TBranch        *b_mPFIDMedium;   //!
   TBranch        *b_mPFIDTight;   //!
   TBranch        *b_mPFIsoLoose;   //!
   TBranch        *b_mPFIsoMedium;   //!
   TBranch        *b_mPFIsoTight;   //!
   TBranch        *b_mPFIsoVeryLoose;   //!
   TBranch        *b_mPFIsoVeryTight;   //!
   TBranch        *b_mPFNeutralHadronIsoR04;   //!
   TBranch        *b_mPFNeutralIso;   //!
   TBranch        *b_mPFPUChargedIso;   //!
   TBranch        *b_mPFPhotonIso;   //!
   TBranch        *b_mPFPhotonIsoR04;   //!
   TBranch        *b_mPFPileupIsoR04;   //!
   TBranch        *b_mPVDXY;   //!
   TBranch        *b_mPVDZ;   //!
   TBranch        *b_mPhi;   //!
   TBranch        *b_mPhi_MuonEnDown;   //!
   TBranch        *b_mPhi_MuonEnUp;   //!
   TBranch        *b_mPixHits;   //!
   TBranch        *b_mPt;   //!
   TBranch        *b_mPt_MuonEnDown;   //!
   TBranch        *b_mPt_MuonEnUp;   //!
   TBranch        *b_mRelPFIsoDBDefault;   //!
   TBranch        *b_mRelPFIsoDBDefaultR04;   //!
   TBranch        *b_mRelPFIsoRho;   //!
   TBranch        *b_mRho;   //!
   TBranch        *b_mSIP2D;   //!
   TBranch        *b_mSIP3D;   //!
   TBranch        *b_mSegmentCompatibility;   //!
   TBranch        *b_mSoftCutBasedId;   //!
   TBranch        *b_mTkIsoLoose;   //!
   TBranch        *b_mTkIsoTight;   //!
   TBranch        *b_mTkLayersWithMeasurement;   //!
   TBranch        *b_mTrkIsoDR03;   //!
   TBranch        *b_mTrkKink;   //!
   TBranch        *b_mTypeCode;   //!
   TBranch        *b_mVZ;   //!
   TBranch        *b_mValidFraction;   //!
   TBranch        *b_mZTTGenMatching;   //!
   TBranch        *b_m_t_DR;   //!
   TBranch        *b_m_t_Mass;   //!
   TBranch        *b_m_t_doubleL1IsoTauMatch;   //!
   TBranch        *b_metSig;   //!
   TBranch        *b_metcov00;   //!
   TBranch        *b_metcov00_DESYlike;   //!
   TBranch        *b_metcov01;   //!
   TBranch        *b_metcov01_DESYlike;   //!
   TBranch        *b_metcov10;   //!
   TBranch        *b_metcov10_DESYlike;   //!
   TBranch        *b_metcov11;   //!
   TBranch        *b_metcov11_DESYlike;   //!
   TBranch        *b_mu12e23DZGroup;   //!
   TBranch        *b_mu12e23DZPass;   //!
   TBranch        *b_mu12e23DZPrescale;   //!
   TBranch        *b_mu12e23Group;   //!
   TBranch        *b_mu12e23Pass;   //!
   TBranch        *b_mu12e23Prescale;   //!
   TBranch        *b_mu23e12DZGroup;   //!
   TBranch        *b_mu23e12DZPass;   //!
   TBranch        *b_mu23e12DZPrescale;   //!
   TBranch        *b_mu23e12Group;   //!
   TBranch        *b_mu23e12Pass;   //!
   TBranch        *b_mu23e12Prescale;   //!
   TBranch        *b_muGlbIsoVetoPt10;   //!
   TBranch        *b_muVetoZTTp001dxyz;   //!
   TBranch        *b_muVetoZTTp001dxyzR0;   //!
   TBranch        *b_nTruePU;   //!
   TBranch        *b_npNLO;   //!
   TBranch        *b_numGenJets;   //!
   TBranch        *b_nvtx;   //!
   TBranch        *b_processID;   //!
   TBranch        *b_puppiMetEt;   //!
   TBranch        *b_puppiMetPhi;   //!
   TBranch        *b_pvChi2;   //!
   TBranch        *b_pvDX;   //!
   TBranch        *b_pvDY;   //!
   TBranch        *b_pvDZ;   //!
   TBranch        *b_pvIsFake;   //!
   TBranch        *b_pvIsValid;   //!
   TBranch        *b_pvNormChi2;   //!
   TBranch        *b_pvRho;   //!
   TBranch        *b_pvX;   //!
   TBranch        *b_pvY;   //!
   TBranch        *b_pvZ;   //!
   TBranch        *b_pvndof;   //!
   TBranch        *b_raw_pfMetEt;   //!
   TBranch        *b_raw_pfMetPhi;   //!
   TBranch        *b_recoilDaught;   //!
   TBranch        *b_recoilWithMet;   //!
   TBranch        *b_rho;   //!
   TBranch        *b_run;   //!
   TBranch        *b_tAgainstElectronLooseMVA6;   //!
   TBranch        *b_tAgainstElectronMVA6Raw;   //!
   TBranch        *b_tAgainstElectronMVA6category;   //!
   TBranch        *b_tAgainstElectronMediumMVA6;   //!
   TBranch        *b_tAgainstElectronTightMVA6;   //!
   TBranch        *b_tAgainstElectronVLooseMVA6;   //!
   TBranch        *b_tAgainstElectronVTightMVA6;   //!
   TBranch        *b_tAgainstMuonLoose3;   //!
   TBranch        *b_tAgainstMuonTight3;   //!
   TBranch        *b_tByCombinedIsolationDeltaBetaCorrRaw3Hits;   //!
   TBranch        *b_tByIsolationMVArun2v1DBdR03oldDMwLTraw;   //!
   TBranch        *b_tByIsolationMVArun2v1DBnewDMwLTraw;   //!
   TBranch        *b_tByIsolationMVArun2v1DBoldDMwLTraw;   //!
   TBranch        *b_tByLooseCombinedIsolationDeltaBetaCorr3Hits;   //!
   TBranch        *b_tByLooseIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByLooseIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByLooseIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tByMediumCombinedIsolationDeltaBetaCorr3Hits;   //!
   TBranch        *b_tByMediumIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByMediumIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByMediumIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tByPhotonPtSumOutsideSignalCone;   //!
   TBranch        *b_tByTightCombinedIsolationDeltaBetaCorr3Hits;   //!
   TBranch        *b_tByTightIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByTightIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByTightIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tByVLooseIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByVLooseIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByVLooseIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tByVTightIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByVTightIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByVTightIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tByVVTightIsolationMVArun2v1DBdR03oldDMwLT;   //!
   TBranch        *b_tByVVTightIsolationMVArun2v1DBnewDMwLT;   //!
   TBranch        *b_tByVVTightIsolationMVArun2v1DBoldDMwLT;   //!
   TBranch        *b_tCharge;   //!
   TBranch        *b_tChargedIsoPtSum;   //!
   TBranch        *b_tChargedIsoPtSumdR03;   //!
   TBranch        *b_tComesFromHiggs;   //!
   TBranch        *b_tDecayMode;   //!
   TBranch        *b_tDecayModeFinding;   //!
   TBranch        *b_tDecayModeFindingNewDMs;   //!
   TBranch        *b_tEta;   //!
   TBranch        *b_tFootprintCorrection;   //!
   TBranch        *b_tFootprintCorrectiondR03;   //!
   TBranch        *b_tGenCharge;   //!
   TBranch        *b_tGenDecayMode;   //!
   TBranch        *b_tGenEnergy;   //!
   TBranch        *b_tGenEta;   //!
   TBranch        *b_tGenJetEta;   //!
   TBranch        *b_tGenJetPt;   //!
   TBranch        *b_tGenMotherEnergy;   //!
   TBranch        *b_tGenMotherEta;   //!
   TBranch        *b_tGenMotherPdgId;   //!
   TBranch        *b_tGenMotherPhi;   //!
   TBranch        *b_tGenMotherPt;   //!
   TBranch        *b_tGenPdgId;   //!
   TBranch        *b_tGenPhi;   //!
   TBranch        *b_tGenPt;   //!
   TBranch        *b_tGenStatus;   //!
   TBranch        *b_tJetArea;   //!
   TBranch        *b_tJetBtag;   //!
   TBranch        *b_tJetDR;   //!
   TBranch        *b_tJetEtaEtaMoment;   //!
   TBranch        *b_tJetEtaPhiMoment;   //!
   TBranch        *b_tJetEtaPhiSpread;   //!
   TBranch        *b_tJetHadronFlavour;   //!
   TBranch        *b_tJetPFCISVBtag;   //!
   TBranch        *b_tJetPartonFlavour;   //!
   TBranch        *b_tJetPhiPhiMoment;   //!
   TBranch        *b_tJetPt;   //!
   TBranch        *b_tL1IsoTauMatch;   //!
   TBranch        *b_tL1IsoTauPt;   //!
   TBranch        *b_tLeadTrackPt;   //!
   TBranch        *b_tLowestMll;   //!
   TBranch        *b_tMass;   //!
   TBranch        *b_tMatchesDoubleMediumTau35Filter;   //!
   TBranch        *b_tMatchesDoubleMediumTau35Path;   //!
   TBranch        *b_tMatchesDoubleMediumTau40Filter;   //!
   TBranch        *b_tMatchesDoubleMediumTau40Path;   //!
   TBranch        *b_tMatchesDoubleTightTau35Filter;   //!
   TBranch        *b_tMatchesDoubleTightTau35Path;   //!
   TBranch        *b_tMatchesDoubleTightTau40Filter;   //!
   TBranch        *b_tMatchesDoubleTightTau40Path;   //!
   TBranch        *b_tMatchesEle24Tau30Filter;   //!
   TBranch        *b_tMatchesEle24Tau30Path;   //!
   TBranch        *b_tMatchesIsoMu20Tau27Filter;   //!
   TBranch        *b_tMatchesIsoMu20Tau27Path;   //!
   TBranch        *b_tNChrgHadrIsolationCands;   //!
   TBranch        *b_tNChrgHadrSignalCands;   //!
   TBranch        *b_tNGammaSignalCands;   //!
   TBranch        *b_tNNeutralHadrSignalCands;   //!
   TBranch        *b_tNSignalCands;   //!
   TBranch        *b_tNearestZMass;   //!
   TBranch        *b_tNeutralIsoPtSum;   //!
   TBranch        *b_tNeutralIsoPtSumWeight;   //!
   TBranch        *b_tNeutralIsoPtSumWeightdR03;   //!
   TBranch        *b_tNeutralIsoPtSumdR03;   //!
   TBranch        *b_tPVDXY;   //!
   TBranch        *b_tPVDZ;   //!
   TBranch        *b_tPhi;   //!
   TBranch        *b_tPhotonPtSumOutsideSignalCone;   //!
   TBranch        *b_tPhotonPtSumOutsideSignalConedR03;   //!
   TBranch        *b_tPt;   //!
   TBranch        *b_tPuCorrPtSum;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTLoose;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTMedium;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTTight;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTVLoose;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTVTight;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTVVTight;   //!
   TBranch        *b_tRerunMVArun2v1DBoldDMwLTraw;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTLoose;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTMedium;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTTight;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTVLoose;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTVTight;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTVVLoose;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTVVTight;   //!
   TBranch        *b_tRerunMVArun2v2DBoldDMwLTraw;   //!
   TBranch        *b_tVZ;   //!
   TBranch        *b_tZTTGenDR;   //!
   TBranch        *b_tZTTGenEta;   //!
   TBranch        *b_tZTTGenMatching;   //!
   TBranch        *b_tZTTGenPhi;   //!
   TBranch        *b_tZTTGenPt;   //!
   TBranch        *b_tauVetoPt20Loose3HitsVtx;   //!
   TBranch        *b_tauVetoPt20TightMVALTVtx;   //!
   TBranch        *b_topQuarkPt1;   //!
   TBranch        *b_topQuarkPt2;   //!
   TBranch        *b_tripleEGroup;   //!
   TBranch        *b_tripleEPass;   //!
   TBranch        *b_tripleEPrescale;   //!
   TBranch        *b_tripleMu12_10_5Group;   //!
   TBranch        *b_tripleMu12_10_5Pass;   //!
   TBranch        *b_tripleMu12_10_5Prescale;   //!
   TBranch        *b_type1_pfMetEt;   //!
   TBranch        *b_type1_pfMetPhi;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEnDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEnUp;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta0to3Down;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta0to3Up;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta0to5Down;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta0to5Up;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta3to5Down;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetEta3to5Up;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetRelativeBalDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetRelativeBalUp;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetRelativeSampleDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetRelativeSampleUp;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetResDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetResUp;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetTotalDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_JetTotalUp;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_UnclusteredEnDown;   //!
   TBranch        *b_type1_pfMet_shiftedPhi_UnclusteredEnUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEnDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEnUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta0to3Down;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta0to3Up;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta0to5Down;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta0to5Up;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta3to5Down;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetEta3to5Up;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetRelativeBalDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetRelativeBalUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetRelativeSampleDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetRelativeSampleUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetResDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetResUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetTotalDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_JetTotalUp;   //!
   TBranch        *b_type1_pfMet_shiftedPt_UnclusteredEnDown;   //!
   TBranch        *b_type1_pfMet_shiftedPt_UnclusteredEnUp;   //!
   TBranch        *b_vbfDeta;   //!
   TBranch        *b_vbfJetVeto20;   //!
   TBranch        *b_vbfJetVeto30;   //!
   TBranch        *b_vbfMass;   //!
   TBranch        *b_vbfMassWoNoisyJets;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta0to3Down;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta0to3Up;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta0to5Down;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta0to5Up;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta3to5Down;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetEta3to5Up;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetRelativeBalDown;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetRelativeBalUp;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetRelativeSampleDown;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetRelativeSampleUp;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetTotalDown;   //!
   TBranch        *b_vbfMassWoNoisyJets_JetTotalUp;   //!
   TBranch        *b_vbfMass_JetAbsoluteFlavMapDown;   //!
   TBranch        *b_vbfMass_JetAbsoluteFlavMapUp;   //!
   TBranch        *b_vbfMass_JetAbsoluteMPFBiasDown;   //!
   TBranch        *b_vbfMass_JetAbsoluteMPFBiasUp;   //!
   TBranch        *b_vbfMass_JetAbsoluteScaleDown;   //!
   TBranch        *b_vbfMass_JetAbsoluteScaleUp;   //!
   TBranch        *b_vbfMass_JetAbsoluteStatDown;   //!
   TBranch        *b_vbfMass_JetAbsoluteStatUp;   //!
   TBranch        *b_vbfMass_JetClosureDown;   //!
   TBranch        *b_vbfMass_JetClosureUp;   //!
   TBranch        *b_vbfMass_JetEta0to3Down;   //!
   TBranch        *b_vbfMass_JetEta0to3Up;   //!
   TBranch        *b_vbfMass_JetEta0to5Down;   //!
   TBranch        *b_vbfMass_JetEta0to5Up;   //!
   TBranch        *b_vbfMass_JetEta3to5Down;   //!
   TBranch        *b_vbfMass_JetEta3to5Up;   //!
   TBranch        *b_vbfMass_JetFlavorQCDDown;   //!
   TBranch        *b_vbfMass_JetFlavorQCDUp;   //!
   TBranch        *b_vbfMass_JetFragmentationDown;   //!
   TBranch        *b_vbfMass_JetFragmentationUp;   //!
   TBranch        *b_vbfMass_JetPileUpDataMCDown;   //!
   TBranch        *b_vbfMass_JetPileUpDataMCUp;   //!
   TBranch        *b_vbfMass_JetPileUpPtBBDown;   //!
   TBranch        *b_vbfMass_JetPileUpPtBBUp;   //!
   TBranch        *b_vbfMass_JetPileUpPtEC1Down;   //!
   TBranch        *b_vbfMass_JetPileUpPtEC1Up;   //!
   TBranch        *b_vbfMass_JetPileUpPtEC2Down;   //!
   TBranch        *b_vbfMass_JetPileUpPtEC2Up;   //!
   TBranch        *b_vbfMass_JetPileUpPtHFDown;   //!
   TBranch        *b_vbfMass_JetPileUpPtHFUp;   //!
   TBranch        *b_vbfMass_JetPileUpPtRefDown;   //!
   TBranch        *b_vbfMass_JetPileUpPtRefUp;   //!
   TBranch        *b_vbfMass_JetRelativeBalDown;   //!
   TBranch        *b_vbfMass_JetRelativeBalUp;   //!
   TBranch        *b_vbfMass_JetRelativeFSRDown;   //!
   TBranch        *b_vbfMass_JetRelativeFSRUp;   //!
   TBranch        *b_vbfMass_JetRelativeJEREC1Down;   //!
   TBranch        *b_vbfMass_JetRelativeJEREC1Up;   //!
   TBranch        *b_vbfMass_JetRelativeJEREC2Down;   //!
   TBranch        *b_vbfMass_JetRelativeJEREC2Up;   //!
   TBranch        *b_vbfMass_JetRelativeJERHFDown;   //!
   TBranch        *b_vbfMass_JetRelativeJERHFUp;   //!
   TBranch        *b_vbfMass_JetRelativePtBBDown;   //!
   TBranch        *b_vbfMass_JetRelativePtBBUp;   //!
   TBranch        *b_vbfMass_JetRelativePtEC1Down;   //!
   TBranch        *b_vbfMass_JetRelativePtEC1Up;   //!
   TBranch        *b_vbfMass_JetRelativePtEC2Down;   //!
   TBranch        *b_vbfMass_JetRelativePtEC2Up;   //!
   TBranch        *b_vbfMass_JetRelativePtHFDown;   //!
   TBranch        *b_vbfMass_JetRelativePtHFUp;   //!
   TBranch        *b_vbfMass_JetRelativeSampleDown;   //!
   TBranch        *b_vbfMass_JetRelativeSampleUp;   //!
   TBranch        *b_vbfMass_JetRelativeStatECDown;   //!
   TBranch        *b_vbfMass_JetRelativeStatECUp;   //!
   TBranch        *b_vbfMass_JetRelativeStatFSRDown;   //!
   TBranch        *b_vbfMass_JetRelativeStatFSRUp;   //!
   TBranch        *b_vbfMass_JetRelativeStatHFDown;   //!
   TBranch        *b_vbfMass_JetRelativeStatHFUp;   //!
   TBranch        *b_vbfMass_JetSinglePionECALDown;   //!
   TBranch        *b_vbfMass_JetSinglePionECALUp;   //!
   TBranch        *b_vbfMass_JetSinglePionHCALDown;   //!
   TBranch        *b_vbfMass_JetSinglePionHCALUp;   //!
   TBranch        *b_vbfMass_JetTimePtEtaDown;   //!
   TBranch        *b_vbfMass_JetTimePtEtaUp;   //!
   TBranch        *b_vbfMass_JetTotalDown;   //!
   TBranch        *b_vbfMass_JetTotalUp;   //!
   TBranch        *b_vbfNJets20;   //!
   TBranch        *b_vbfNJets30;   //!
   TBranch        *b_vbfj1eta;   //!
   TBranch        *b_vbfj1pt;   //!
   TBranch        *b_vbfj2eta;   //!
   TBranch        *b_vbfj2pt;   //!
   TBranch        *b_vispX;   //!
   TBranch        *b_vispY;   //!
   TBranch        *b_idx;   //!

   // methods
   HTauTauTree_mt (TTree* tree); //ctor
   ~HTauTauTree_mt();
   void Init(TTree* tree);
   Int_t GetEntry(int entry);
   Long64_t GetEntries();
   TTree* GetTree();
};

HTauTauTree_mt::HTauTauTree_mt (TTree* tree)
{
    Init(tree);
}

HTauTauTree_mt::~HTauTauTree_mt() {}

void HTauTauTree_mt::Init(TTree* tree)
{
   // Set object pointer

   // Set branch addresses and branch pointers
   if (!tree) return;
   _tree = tree;
   _tree->SetMakeClass(1); // needed especially when compiling

   _tree->SetBranchAddress("DoubleMediumTau35Group", &DoubleMediumTau35Group, &b_DoubleMediumTau35Group);
   _tree->SetBranchAddress("DoubleMediumTau35Pass", &DoubleMediumTau35Pass, &b_DoubleMediumTau35Pass);
   _tree->SetBranchAddress("DoubleMediumTau35Prescale", &DoubleMediumTau35Prescale, &b_DoubleMediumTau35Prescale);
   _tree->SetBranchAddress("DoubleMediumTau40Group", &DoubleMediumTau40Group, &b_DoubleMediumTau40Group);
   _tree->SetBranchAddress("DoubleMediumTau40Pass", &DoubleMediumTau40Pass, &b_DoubleMediumTau40Pass);
   _tree->SetBranchAddress("DoubleMediumTau40Prescale", &DoubleMediumTau40Prescale, &b_DoubleMediumTau40Prescale);
   _tree->SetBranchAddress("DoubleTightTau35Group", &DoubleTightTau35Group, &b_DoubleTightTau35Group);
   _tree->SetBranchAddress("DoubleTightTau35Pass", &DoubleTightTau35Pass, &b_DoubleTightTau35Pass);
   _tree->SetBranchAddress("DoubleTightTau35Prescale", &DoubleTightTau35Prescale, &b_DoubleTightTau35Prescale);
   _tree->SetBranchAddress("DoubleTightTau40Group", &DoubleTightTau40Group, &b_DoubleTightTau40Group);
   _tree->SetBranchAddress("DoubleTightTau40Pass", &DoubleTightTau40Pass, &b_DoubleTightTau40Pass);
   _tree->SetBranchAddress("DoubleTightTau40Prescale", &DoubleTightTau40Prescale, &b_DoubleTightTau40Prescale);
   _tree->SetBranchAddress("Ele24Tau30Group", &Ele24Tau30Group, &b_Ele24Tau30Group);
   _tree->SetBranchAddress("Ele24Tau30Pass", &Ele24Tau30Pass, &b_Ele24Tau30Pass);
   _tree->SetBranchAddress("Ele24Tau30Prescale", &Ele24Tau30Prescale, &b_Ele24Tau30Prescale);
   _tree->SetBranchAddress("Ele27WPTightGroup", &Ele27WPTightGroup, &b_Ele27WPTightGroup);
   _tree->SetBranchAddress("Ele27WPTightPass", &Ele27WPTightPass, &b_Ele27WPTightPass);
   _tree->SetBranchAddress("Ele27WPTightPrescale", &Ele27WPTightPrescale, &b_Ele27WPTightPrescale);
   _tree->SetBranchAddress("Ele32WPTightGroup", &Ele32WPTightGroup, &b_Ele32WPTightGroup);
   _tree->SetBranchAddress("Ele32WPTightPass", &Ele32WPTightPass, &b_Ele32WPTightPass);
   _tree->SetBranchAddress("Ele32WPTightPrescale", &Ele32WPTightPrescale, &b_Ele32WPTightPrescale);
   _tree->SetBranchAddress("Ele35WPTightGroup", &Ele35WPTightGroup, &b_Ele35WPTightGroup);
   _tree->SetBranchAddress("Ele35WPTightPass", &Ele35WPTightPass, &b_Ele35WPTightPass);
   _tree->SetBranchAddress("Ele35WPTightPrescale", &Ele35WPTightPrescale, &b_Ele35WPTightPrescale);
   _tree->SetBranchAddress("EmbPtWeight", &EmbPtWeight, &b_EmbPtWeight);
   _tree->SetBranchAddress("Eta", &Eta, &b_Eta);
   _tree->SetBranchAddress("Flag_BadChargedCandidateFilter", &Flag_BadChargedCandidateFilter, &b_Flag_BadChargedCandidateFilter);
   _tree->SetBranchAddress("Flag_BadPFMuonFilter", &Flag_BadPFMuonFilter, &b_Flag_BadPFMuonFilter);
   _tree->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter, &b_Flag_EcalDeadCellTriggerPrimitiveFilter);
   _tree->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter, &b_Flag_HBHENoiseFilter);
   _tree->SetBranchAddress("Flag_HBHENoiseIsoFilter", &Flag_HBHENoiseIsoFilter, &b_Flag_HBHENoiseIsoFilter);
   _tree->SetBranchAddress("Flag_badMuons", &Flag_badMuons, &b_Flag_badMuons);
   _tree->SetBranchAddress("Flag_duplicateMuons", &Flag_duplicateMuons, &b_Flag_duplicateMuons);
   _tree->SetBranchAddress("Flag_ecalBadCalibFilter", &Flag_ecalBadCalibFilter, &b_Flag_ecalBadCalibFilter);
   _tree->SetBranchAddress("Flag_eeBadScFilter", &Flag_eeBadScFilter, &b_Flag_eeBadScFilter);
   _tree->SetBranchAddress("Flag_globalSuperTightHalo2016Filter", &Flag_globalSuperTightHalo2016Filter, &b_Flag_globalSuperTightHalo2016Filter);
   _tree->SetBranchAddress("Flag_globalTightHalo2016Filter", &Flag_globalTightHalo2016Filter, &b_Flag_globalTightHalo2016Filter);
   _tree->SetBranchAddress("Flag_goodVertices", &Flag_goodVertices, &b_Flag_goodVertices);
   _tree->SetBranchAddress("GenWeight", &GenWeight, &b_GenWeight);
   _tree->SetBranchAddress("Ht", &Ht, &b_Ht);
   _tree->SetBranchAddress("IsoMu20Group", &IsoMu20Group, &b_IsoMu20Group);
   _tree->SetBranchAddress("IsoMu20Pass", &IsoMu20Pass, &b_IsoMu20Pass);
   _tree->SetBranchAddress("IsoMu20Prescale", &IsoMu20Prescale, &b_IsoMu20Prescale);
   _tree->SetBranchAddress("IsoMu24Group", &IsoMu24Group, &b_IsoMu24Group);
   _tree->SetBranchAddress("IsoMu24Pass", &IsoMu24Pass, &b_IsoMu24Pass);
   _tree->SetBranchAddress("IsoMu24Prescale", &IsoMu24Prescale, &b_IsoMu24Prescale);
   _tree->SetBranchAddress("IsoMu24_eta2p1Group", &IsoMu24_eta2p1Group, &b_IsoMu24_eta2p1Group);
   _tree->SetBranchAddress("IsoMu24_eta2p1Pass", &IsoMu24_eta2p1Pass, &b_IsoMu24_eta2p1Pass);
   _tree->SetBranchAddress("IsoMu24_eta2p1Prescale", &IsoMu24_eta2p1Prescale, &b_IsoMu24_eta2p1Prescale);
   _tree->SetBranchAddress("IsoMu27Group", &IsoMu27Group, &b_IsoMu27Group);
   _tree->SetBranchAddress("IsoMu27Pass", &IsoMu27Pass, &b_IsoMu27Pass);
   _tree->SetBranchAddress("IsoMu27Prescale", &IsoMu27Prescale, &b_IsoMu27Prescale);
   _tree->SetBranchAddress("LT", &LT, &b_LT);
   _tree->SetBranchAddress("Mass", &Mass, &b_Mass);
   _tree->SetBranchAddress("MassError", &MassError, &b_MassError);
   _tree->SetBranchAddress("MassErrord1", &MassErrord1, &b_MassErrord1);
   _tree->SetBranchAddress("MassErrord2", &MassErrord2, &b_MassErrord2);
   _tree->SetBranchAddress("MassErrord3", &MassErrord3, &b_MassErrord3);
   _tree->SetBranchAddress("MassErrord4", &MassErrord4, &b_MassErrord4);
   _tree->SetBranchAddress("Mt", &Mt, &b_Mt);
   _tree->SetBranchAddress("Mu20Tau27Group", &Mu20Tau27Group, &b_Mu20Tau27Group);
   _tree->SetBranchAddress("Mu20Tau27Pass", &Mu20Tau27Pass, &b_Mu20Tau27Pass);
   _tree->SetBranchAddress("Mu20Tau27Prescale", &Mu20Tau27Prescale, &b_Mu20Tau27Prescale);
   _tree->SetBranchAddress("Mu50Group", &Mu50Group, &b_Mu50Group);
   _tree->SetBranchAddress("Mu50Pass", &Mu50Pass, &b_Mu50Pass);
   _tree->SetBranchAddress("Mu50Prescale", &Mu50Prescale, &b_Mu50Prescale);
   _tree->SetBranchAddress("NUP", &NUP, &b_NUP);
   _tree->SetBranchAddress("Phi", &Phi, &b_Phi);
   _tree->SetBranchAddress("Pt", &Pt, &b_Pt);
   _tree->SetBranchAddress("Rivet_VEta", &Rivet_VEta, &b_Rivet_VEta);
   _tree->SetBranchAddress("Rivet_VPt", &Rivet_VPt, &b_Rivet_VPt);
   _tree->SetBranchAddress("Rivet_errorCode", &Rivet_errorCode, &b_Rivet_errorCode);
   _tree->SetBranchAddress("Rivet_higgsEta", &Rivet_higgsEta, &b_Rivet_higgsEta);
   _tree->SetBranchAddress("Rivet_higgsPt", &Rivet_higgsPt, &b_Rivet_higgsPt);
   _tree->SetBranchAddress("Rivet_nJets25", &Rivet_nJets25, &b_Rivet_nJets25);
   _tree->SetBranchAddress("Rivet_nJets30", &Rivet_nJets30, &b_Rivet_nJets30);
   _tree->SetBranchAddress("Rivet_p4decay_VEta", &Rivet_p4decay_VEta, &b_Rivet_p4decay_VEta);
   _tree->SetBranchAddress("Rivet_p4decay_VPt", &Rivet_p4decay_VPt, &b_Rivet_p4decay_VPt);
   _tree->SetBranchAddress("Rivet_prodMode", &Rivet_prodMode, &b_Rivet_prodMode);
   _tree->SetBranchAddress("Rivet_stage0_cat", &Rivet_stage0_cat, &b_Rivet_stage0_cat);
   _tree->SetBranchAddress("Rivet_stage1_cat_pTjet25GeV", &Rivet_stage1_cat_pTjet25GeV, &b_Rivet_stage1_cat_pTjet25GeV);
   _tree->SetBranchAddress("Rivet_stage1_cat_pTjet30GeV", &Rivet_stage1_cat_pTjet30GeV, &b_Rivet_stage1_cat_pTjet30GeV);
   _tree->SetBranchAddress("bjetCISVVeto20Loose", &bjetCISVVeto20Loose, &b_bjetCISVVeto20Loose);
   _tree->SetBranchAddress("bjetCISVVeto20Medium", &bjetCISVVeto20Medium, &b_bjetCISVVeto20Medium);
   _tree->SetBranchAddress("bjetCISVVeto20MediumWoNoisyJets", &bjetCISVVeto20MediumWoNoisyJets, &b_bjetCISVVeto20MediumWoNoisyJets);
   _tree->SetBranchAddress("bjetCISVVeto20Tight", &bjetCISVVeto20Tight, &b_bjetCISVVeto20Tight);
   _tree->SetBranchAddress("bjetCISVVeto30Loose", &bjetCISVVeto30Loose, &b_bjetCISVVeto30Loose);
   _tree->SetBranchAddress("bjetCISVVeto30Medium", &bjetCISVVeto30Medium, &b_bjetCISVVeto30Medium);
   _tree->SetBranchAddress("bjetCISVVeto30Tight", &bjetCISVVeto30Tight, &b_bjetCISVVeto30Tight);
   _tree->SetBranchAddress("bjetDeepCSVVeto20Loose", &bjetDeepCSVVeto20Loose, &b_bjetDeepCSVVeto20Loose);
   _tree->SetBranchAddress("bjetDeepCSVVeto20Medium", &bjetDeepCSVVeto20Medium, &b_bjetDeepCSVVeto20Medium);
   _tree->SetBranchAddress("bjetDeepCSVVeto20MediumWoNoisyJets", &bjetDeepCSVVeto20MediumWoNoisyJets, &b_bjetDeepCSVVeto20MediumWoNoisyJets);
   _tree->SetBranchAddress("bjetDeepCSVVeto20Tight", &bjetDeepCSVVeto20Tight, &b_bjetDeepCSVVeto20Tight);
   _tree->SetBranchAddress("bjetDeepCSVVeto30Loose", &bjetDeepCSVVeto30Loose, &b_bjetDeepCSVVeto30Loose);
   _tree->SetBranchAddress("bjetDeepCSVVeto30Medium", &bjetDeepCSVVeto30Medium, &b_bjetDeepCSVVeto30Medium);
   _tree->SetBranchAddress("bjetDeepCSVVeto30Tight", &bjetDeepCSVVeto30Tight, &b_bjetDeepCSVVeto30Tight);
   _tree->SetBranchAddress("charge", &charge, &b_charge);
   _tree->SetBranchAddress("dielectronVeto", &dielectronVeto, &b_dielectronVeto);
   _tree->SetBranchAddress("dimuonVeto", &dimuonVeto, &b_dimuonVeto);
   _tree->SetBranchAddress("doubleE_23_12Group", &doubleE_23_12Group, &b_doubleE_23_12Group);
   _tree->SetBranchAddress("doubleE_23_12Pass", &doubleE_23_12Pass, &b_doubleE_23_12Pass);
   _tree->SetBranchAddress("doubleE_23_12Prescale", &doubleE_23_12Prescale, &b_doubleE_23_12Prescale);
   _tree->SetBranchAddress("doubleE_23_12_DZGroup", &doubleE_23_12_DZGroup, &b_doubleE_23_12_DZGroup);
   _tree->SetBranchAddress("doubleE_23_12_DZPass", &doubleE_23_12_DZPass, &b_doubleE_23_12_DZPass);
   _tree->SetBranchAddress("doubleE_23_12_DZPrescale", &doubleE_23_12_DZPrescale, &b_doubleE_23_12_DZPrescale);
   _tree->SetBranchAddress("doubleMuDZGroup", &doubleMuDZGroup, &b_doubleMuDZGroup);
   _tree->SetBranchAddress("doubleMuDZPass", &doubleMuDZPass, &b_doubleMuDZPass);
   _tree->SetBranchAddress("doubleMuDZPrescale", &doubleMuDZPrescale, &b_doubleMuDZPrescale);
   _tree->SetBranchAddress("doubleMuDZminMass3p8Group", &doubleMuDZminMass3p8Group, &b_doubleMuDZminMass3p8Group);
   _tree->SetBranchAddress("doubleMuDZminMass3p8Pass", &doubleMuDZminMass3p8Pass, &b_doubleMuDZminMass3p8Pass);
   _tree->SetBranchAddress("doubleMuDZminMass3p8Prescale", &doubleMuDZminMass3p8Prescale, &b_doubleMuDZminMass3p8Prescale);
   _tree->SetBranchAddress("doubleMuDZminMass8Group", &doubleMuDZminMass8Group, &b_doubleMuDZminMass8Group);
   _tree->SetBranchAddress("doubleMuDZminMass8Pass", &doubleMuDZminMass8Pass, &b_doubleMuDZminMass8Pass);
   _tree->SetBranchAddress("doubleMuDZminMass8Prescale", &doubleMuDZminMass8Prescale, &b_doubleMuDZminMass8Prescale);
   _tree->SetBranchAddress("eVetoMVAIso", &eVetoMVAIso, &b_eVetoMVAIso);
   _tree->SetBranchAddress("eVetoZTTp001dxyz", &eVetoZTTp001dxyz, &b_eVetoZTTp001dxyz);
   _tree->SetBranchAddress("eVetoZTTp001dxyzR0", &eVetoZTTp001dxyzR0, &b_eVetoZTTp001dxyzR0);
   _tree->SetBranchAddress("evt", &evt, &b_evt);
   _tree->SetBranchAddress("genEta", &genEta, &b_genEta);
   _tree->SetBranchAddress("genHTT", &genHTT, &b_genHTT);
   _tree->SetBranchAddress("genM", &genM, &b_genM);
   _tree->SetBranchAddress("genMass", &genMass, &b_genMass);
   _tree->SetBranchAddress("genPhi", &genPhi, &b_genPhi);
   _tree->SetBranchAddress("genpT", &genpT, &b_genpT);
   _tree->SetBranchAddress("genpX", &genpX, &b_genpX);
   _tree->SetBranchAddress("genpY", &genpY, &b_genpY);
   _tree->SetBranchAddress("isdata", &isdata, &b_isdata);
   _tree->SetBranchAddress("isembed", &isembed, &b_isembed);
   _tree->SetBranchAddress("j1csv", &j1csv, &b_j1csv);
   _tree->SetBranchAddress("j1csvWoNoisyJets", &j1csvWoNoisyJets, &b_j1csvWoNoisyJets);
   _tree->SetBranchAddress("j1eta", &j1eta, &b_j1eta);
   _tree->SetBranchAddress("j1etaWoNoisyJets", &j1etaWoNoisyJets, &b_j1etaWoNoisyJets);
   _tree->SetBranchAddress("j1hadronflavor", &j1hadronflavor, &b_j1hadronflavor);
   _tree->SetBranchAddress("j1hadronflavorWoNoisyJets", &j1hadronflavorWoNoisyJets, &b_j1hadronflavorWoNoisyJets);
   _tree->SetBranchAddress("j1phi", &j1phi, &b_j1phi);
   _tree->SetBranchAddress("j1phiWoNoisyJets", &j1phiWoNoisyJets, &b_j1phiWoNoisyJets);
   _tree->SetBranchAddress("j1pt", &j1pt, &b_j1pt);
   _tree->SetBranchAddress("j1ptWoNoisyJets", &j1ptWoNoisyJets, &b_j1ptWoNoisyJets);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta0to3Down", &j1ptWoNoisyJets_JetEta0to3Down, &b_j1ptWoNoisyJets_JetEta0to3Down);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta0to3Up", &j1ptWoNoisyJets_JetEta0to3Up, &b_j1ptWoNoisyJets_JetEta0to3Up);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta0to5Down", &j1ptWoNoisyJets_JetEta0to5Down, &b_j1ptWoNoisyJets_JetEta0to5Down);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta0to5Up", &j1ptWoNoisyJets_JetEta0to5Up, &b_j1ptWoNoisyJets_JetEta0to5Up);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta3to5Down", &j1ptWoNoisyJets_JetEta3to5Down, &b_j1ptWoNoisyJets_JetEta3to5Down);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetEta3to5Up", &j1ptWoNoisyJets_JetEta3to5Up, &b_j1ptWoNoisyJets_JetEta3to5Up);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetRelativeBalDown", &j1ptWoNoisyJets_JetRelativeBalDown, &b_j1ptWoNoisyJets_JetRelativeBalDown);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetRelativeBalUp", &j1ptWoNoisyJets_JetRelativeBalUp, &b_j1ptWoNoisyJets_JetRelativeBalUp);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetRelativeSampleDown", &j1ptWoNoisyJets_JetRelativeSampleDown, &b_j1ptWoNoisyJets_JetRelativeSampleDown);
   _tree->SetBranchAddress("j1ptWoNoisyJets_JetRelativeSampleUp", &j1ptWoNoisyJets_JetRelativeSampleUp, &b_j1ptWoNoisyJets_JetRelativeSampleUp);
   _tree->SetBranchAddress("j2csv", &j2csv, &b_j2csv);
   _tree->SetBranchAddress("j2csvWoNoisyJets", &j2csvWoNoisyJets, &b_j2csvWoNoisyJets);
   _tree->SetBranchAddress("j2eta", &j2eta, &b_j2eta);
   _tree->SetBranchAddress("j2etaWoNoisyJets", &j2etaWoNoisyJets, &b_j2etaWoNoisyJets);
   _tree->SetBranchAddress("j2hadronflavor", &j2hadronflavor, &b_j2hadronflavor);
   _tree->SetBranchAddress("j2hadronflavorWoNoisyJets", &j2hadronflavorWoNoisyJets, &b_j2hadronflavorWoNoisyJets);
   _tree->SetBranchAddress("j2phi", &j2phi, &b_j2phi);
   _tree->SetBranchAddress("j2phiWoNoisyJets", &j2phiWoNoisyJets, &b_j2phiWoNoisyJets);
   _tree->SetBranchAddress("j2pt", &j2pt, &b_j2pt);
   _tree->SetBranchAddress("j2ptWoNoisyJets", &j2ptWoNoisyJets, &b_j2ptWoNoisyJets);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta0to3Down", &j2ptWoNoisyJets_JetEta0to3Down, &b_j2ptWoNoisyJets_JetEta0to3Down);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta0to3Up", &j2ptWoNoisyJets_JetEta0to3Up, &b_j2ptWoNoisyJets_JetEta0to3Up);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta0to5Down", &j2ptWoNoisyJets_JetEta0to5Down, &b_j2ptWoNoisyJets_JetEta0to5Down);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta0to5Up", &j2ptWoNoisyJets_JetEta0to5Up, &b_j2ptWoNoisyJets_JetEta0to5Up);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta3to5Down", &j2ptWoNoisyJets_JetEta3to5Down, &b_j2ptWoNoisyJets_JetEta3to5Down);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetEta3to5Up", &j2ptWoNoisyJets_JetEta3to5Up, &b_j2ptWoNoisyJets_JetEta3to5Up);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetRelativeBalDown", &j2ptWoNoisyJets_JetRelativeBalDown, &b_j2ptWoNoisyJets_JetRelativeBalDown);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetRelativeBalUp", &j2ptWoNoisyJets_JetRelativeBalUp, &b_j2ptWoNoisyJets_JetRelativeBalUp);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetRelativeSampleDown", &j2ptWoNoisyJets_JetRelativeSampleDown, &b_j2ptWoNoisyJets_JetRelativeSampleDown);
   _tree->SetBranchAddress("j2ptWoNoisyJets_JetRelativeSampleUp", &j2ptWoNoisyJets_JetRelativeSampleUp, &b_j2ptWoNoisyJets_JetRelativeSampleUp);
   _tree->SetBranchAddress("jb1csv", &jb1csv, &b_jb1csv);
   _tree->SetBranchAddress("jb1csvWoNoisyJets", &jb1csvWoNoisyJets, &b_jb1csvWoNoisyJets);
   _tree->SetBranchAddress("jb1eta", &jb1eta, &b_jb1eta);
   _tree->SetBranchAddress("jb1etaWoNoisyJets", &jb1etaWoNoisyJets, &b_jb1etaWoNoisyJets);
   _tree->SetBranchAddress("jb1hadronflavor", &jb1hadronflavor, &b_jb1hadronflavor);
   _tree->SetBranchAddress("jb1hadronflavorWoNoisyJets", &jb1hadronflavorWoNoisyJets, &b_jb1hadronflavorWoNoisyJets);
   _tree->SetBranchAddress("jb1phi", &jb1phi, &b_jb1phi);
   _tree->SetBranchAddress("jb1phiWoNoisyJets", &jb1phiWoNoisyJets, &b_jb1phiWoNoisyJets);
   _tree->SetBranchAddress("jb1pt", &jb1pt, &b_jb1pt);
   _tree->SetBranchAddress("jb1ptWoNoisyJets", &jb1ptWoNoisyJets, &b_jb1ptWoNoisyJets);
   _tree->SetBranchAddress("jb2csv", &jb2csv, &b_jb2csv);
   _tree->SetBranchAddress("jb2csvWoNoisyJets", &jb2csvWoNoisyJets, &b_jb2csvWoNoisyJets);
   _tree->SetBranchAddress("jb2eta", &jb2eta, &b_jb2eta);
   _tree->SetBranchAddress("jb2etaWoNoisyJets", &jb2etaWoNoisyJets, &b_jb2etaWoNoisyJets);
   _tree->SetBranchAddress("jb2hadronflavor", &jb2hadronflavor, &b_jb2hadronflavor);
   _tree->SetBranchAddress("jb2hadronflavorWoNoisyJets", &jb2hadronflavorWoNoisyJets, &b_jb2hadronflavorWoNoisyJets);
   _tree->SetBranchAddress("jb2phi", &jb2phi, &b_jb2phi);
   _tree->SetBranchAddress("jb2phiWoNoisyJets", &jb2phiWoNoisyJets, &b_jb2phiWoNoisyJets);
   _tree->SetBranchAddress("jb2pt", &jb2pt, &b_jb2pt);
   _tree->SetBranchAddress("jb2ptWoNoisyJets", &jb2ptWoNoisyJets, &b_jb2ptWoNoisyJets);
   _tree->SetBranchAddress("jetVeto20", &jetVeto20, &b_jetVeto20);
   _tree->SetBranchAddress("jetVeto20WoNoisyJets", &jetVeto20WoNoisyJets, &b_jetVeto20WoNoisyJets);
   _tree->SetBranchAddress("jetVeto20_JetEnDown", &jetVeto20_JetEnDown, &b_jetVeto20_JetEnDown);
   _tree->SetBranchAddress("jetVeto20_JetEnUp", &jetVeto20_JetEnUp, &b_jetVeto20_JetEnUp);
   _tree->SetBranchAddress("jetVeto30", &jetVeto30, &b_jetVeto30);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets", &jetVeto30WoNoisyJets, &b_jetVeto30WoNoisyJets);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta0to3Down", &jetVeto30WoNoisyJets_JetEta0to3Down, &b_jetVeto30WoNoisyJets_JetEta0to3Down);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta0to3Up", &jetVeto30WoNoisyJets_JetEta0to3Up, &b_jetVeto30WoNoisyJets_JetEta0to3Up);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta0to5Down", &jetVeto30WoNoisyJets_JetEta0to5Down, &b_jetVeto30WoNoisyJets_JetEta0to5Down);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta0to5Up", &jetVeto30WoNoisyJets_JetEta0to5Up, &b_jetVeto30WoNoisyJets_JetEta0to5Up);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta3to5Down", &jetVeto30WoNoisyJets_JetEta3to5Down, &b_jetVeto30WoNoisyJets_JetEta3to5Down);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetEta3to5Up", &jetVeto30WoNoisyJets_JetEta3to5Up, &b_jetVeto30WoNoisyJets_JetEta3to5Up);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets", &jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets, &b_jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets", &jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets, &b_jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetRelativeSampleDown", &jetVeto30WoNoisyJets_JetRelativeSampleDown, &b_jetVeto30WoNoisyJets_JetRelativeSampleDown);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetRelativeSampleUp", &jetVeto30WoNoisyJets_JetRelativeSampleUp, &b_jetVeto30WoNoisyJets_JetRelativeSampleUp);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetTotalDown", &jetVeto30WoNoisyJets_JetTotalDown, &b_jetVeto30WoNoisyJets_JetTotalDown);
   _tree->SetBranchAddress("jetVeto30WoNoisyJets_JetTotalUp", &jetVeto30WoNoisyJets_JetTotalUp, &b_jetVeto30WoNoisyJets_JetTotalUp);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteFlavMapDown", &jetVeto30_JetAbsoluteFlavMapDown, &b_jetVeto30_JetAbsoluteFlavMapDown);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteFlavMapUp", &jetVeto30_JetAbsoluteFlavMapUp, &b_jetVeto30_JetAbsoluteFlavMapUp);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteMPFBiasDown", &jetVeto30_JetAbsoluteMPFBiasDown, &b_jetVeto30_JetAbsoluteMPFBiasDown);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteMPFBiasUp", &jetVeto30_JetAbsoluteMPFBiasUp, &b_jetVeto30_JetAbsoluteMPFBiasUp);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteScaleDown", &jetVeto30_JetAbsoluteScaleDown, &b_jetVeto30_JetAbsoluteScaleDown);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteScaleUp", &jetVeto30_JetAbsoluteScaleUp, &b_jetVeto30_JetAbsoluteScaleUp);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteStatDown", &jetVeto30_JetAbsoluteStatDown, &b_jetVeto30_JetAbsoluteStatDown);
   _tree->SetBranchAddress("jetVeto30_JetAbsoluteStatUp", &jetVeto30_JetAbsoluteStatUp, &b_jetVeto30_JetAbsoluteStatUp);
   _tree->SetBranchAddress("jetVeto30_JetClosureDown", &jetVeto30_JetClosureDown, &b_jetVeto30_JetClosureDown);
   _tree->SetBranchAddress("jetVeto30_JetClosureUp", &jetVeto30_JetClosureUp, &b_jetVeto30_JetClosureUp);
   _tree->SetBranchAddress("jetVeto30_JetEnDown", &jetVeto30_JetEnDown, &b_jetVeto30_JetEnDown);
   _tree->SetBranchAddress("jetVeto30_JetEnUp", &jetVeto30_JetEnUp, &b_jetVeto30_JetEnUp);
   _tree->SetBranchAddress("jetVeto30_JetEta0to3Down", &jetVeto30_JetEta0to3Down, &b_jetVeto30_JetEta0to3Down);
   _tree->SetBranchAddress("jetVeto30_JetEta0to3Up", &jetVeto30_JetEta0to3Up, &b_jetVeto30_JetEta0to3Up);
   _tree->SetBranchAddress("jetVeto30_JetEta0to5Down", &jetVeto30_JetEta0to5Down, &b_jetVeto30_JetEta0to5Down);
   _tree->SetBranchAddress("jetVeto30_JetEta0to5Up", &jetVeto30_JetEta0to5Up, &b_jetVeto30_JetEta0to5Up);
   _tree->SetBranchAddress("jetVeto30_JetEta3to5Down", &jetVeto30_JetEta3to5Down, &b_jetVeto30_JetEta3to5Down);
   _tree->SetBranchAddress("jetVeto30_JetEta3to5Up", &jetVeto30_JetEta3to5Up, &b_jetVeto30_JetEta3to5Up);
   _tree->SetBranchAddress("jetVeto30_JetFlavorQCDDown", &jetVeto30_JetFlavorQCDDown, &b_jetVeto30_JetFlavorQCDDown);
   _tree->SetBranchAddress("jetVeto30_JetFlavorQCDUp", &jetVeto30_JetFlavorQCDUp, &b_jetVeto30_JetFlavorQCDUp);
   _tree->SetBranchAddress("jetVeto30_JetFragmentationDown", &jetVeto30_JetFragmentationDown, &b_jetVeto30_JetFragmentationDown);
   _tree->SetBranchAddress("jetVeto30_JetFragmentationUp", &jetVeto30_JetFragmentationUp, &b_jetVeto30_JetFragmentationUp);
   _tree->SetBranchAddress("jetVeto30_JetPileUpDataMCDown", &jetVeto30_JetPileUpDataMCDown, &b_jetVeto30_JetPileUpDataMCDown);
   _tree->SetBranchAddress("jetVeto30_JetPileUpDataMCUp", &jetVeto30_JetPileUpDataMCUp, &b_jetVeto30_JetPileUpDataMCUp);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtBBDown", &jetVeto30_JetPileUpPtBBDown, &b_jetVeto30_JetPileUpPtBBDown);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtBBUp", &jetVeto30_JetPileUpPtBBUp, &b_jetVeto30_JetPileUpPtBBUp);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtEC1Down", &jetVeto30_JetPileUpPtEC1Down, &b_jetVeto30_JetPileUpPtEC1Down);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtEC1Up", &jetVeto30_JetPileUpPtEC1Up, &b_jetVeto30_JetPileUpPtEC1Up);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtEC2Down", &jetVeto30_JetPileUpPtEC2Down, &b_jetVeto30_JetPileUpPtEC2Down);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtEC2Up", &jetVeto30_JetPileUpPtEC2Up, &b_jetVeto30_JetPileUpPtEC2Up);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtHFDown", &jetVeto30_JetPileUpPtHFDown, &b_jetVeto30_JetPileUpPtHFDown);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtHFUp", &jetVeto30_JetPileUpPtHFUp, &b_jetVeto30_JetPileUpPtHFUp);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtRefDown", &jetVeto30_JetPileUpPtRefDown, &b_jetVeto30_JetPileUpPtRefDown);
   _tree->SetBranchAddress("jetVeto30_JetPileUpPtRefUp", &jetVeto30_JetPileUpPtRefUp, &b_jetVeto30_JetPileUpPtRefUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeBalDown", &jetVeto30_JetRelativeBalDown, &b_jetVeto30_JetRelativeBalDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeBalUp", &jetVeto30_JetRelativeBalUp, &b_jetVeto30_JetRelativeBalUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeFSRDown", &jetVeto30_JetRelativeFSRDown, &b_jetVeto30_JetRelativeFSRDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeFSRUp", &jetVeto30_JetRelativeFSRUp, &b_jetVeto30_JetRelativeFSRUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJEREC1Down", &jetVeto30_JetRelativeJEREC1Down, &b_jetVeto30_JetRelativeJEREC1Down);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJEREC1Up", &jetVeto30_JetRelativeJEREC1Up, &b_jetVeto30_JetRelativeJEREC1Up);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJEREC2Down", &jetVeto30_JetRelativeJEREC2Down, &b_jetVeto30_JetRelativeJEREC2Down);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJEREC2Up", &jetVeto30_JetRelativeJEREC2Up, &b_jetVeto30_JetRelativeJEREC2Up);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJERHFDown", &jetVeto30_JetRelativeJERHFDown, &b_jetVeto30_JetRelativeJERHFDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeJERHFUp", &jetVeto30_JetRelativeJERHFUp, &b_jetVeto30_JetRelativeJERHFUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtBBDown", &jetVeto30_JetRelativePtBBDown, &b_jetVeto30_JetRelativePtBBDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtBBUp", &jetVeto30_JetRelativePtBBUp, &b_jetVeto30_JetRelativePtBBUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtEC1Down", &jetVeto30_JetRelativePtEC1Down, &b_jetVeto30_JetRelativePtEC1Down);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtEC1Up", &jetVeto30_JetRelativePtEC1Up, &b_jetVeto30_JetRelativePtEC1Up);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtEC2Down", &jetVeto30_JetRelativePtEC2Down, &b_jetVeto30_JetRelativePtEC2Down);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtEC2Up", &jetVeto30_JetRelativePtEC2Up, &b_jetVeto30_JetRelativePtEC2Up);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtHFDown", &jetVeto30_JetRelativePtHFDown, &b_jetVeto30_JetRelativePtHFDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativePtHFUp", &jetVeto30_JetRelativePtHFUp, &b_jetVeto30_JetRelativePtHFUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeSampleDown", &jetVeto30_JetRelativeSampleDown, &b_jetVeto30_JetRelativeSampleDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeSampleUp", &jetVeto30_JetRelativeSampleUp, &b_jetVeto30_JetRelativeSampleUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatECDown", &jetVeto30_JetRelativeStatECDown, &b_jetVeto30_JetRelativeStatECDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatECUp", &jetVeto30_JetRelativeStatECUp, &b_jetVeto30_JetRelativeStatECUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatFSRDown", &jetVeto30_JetRelativeStatFSRDown, &b_jetVeto30_JetRelativeStatFSRDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatFSRUp", &jetVeto30_JetRelativeStatFSRUp, &b_jetVeto30_JetRelativeStatFSRUp);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatHFDown", &jetVeto30_JetRelativeStatHFDown, &b_jetVeto30_JetRelativeStatHFDown);
   _tree->SetBranchAddress("jetVeto30_JetRelativeStatHFUp", &jetVeto30_JetRelativeStatHFUp, &b_jetVeto30_JetRelativeStatHFUp);
   _tree->SetBranchAddress("jetVeto30_JetSinglePionECALDown", &jetVeto30_JetSinglePionECALDown, &b_jetVeto30_JetSinglePionECALDown);
   _tree->SetBranchAddress("jetVeto30_JetSinglePionECALUp", &jetVeto30_JetSinglePionECALUp, &b_jetVeto30_JetSinglePionECALUp);
   _tree->SetBranchAddress("jetVeto30_JetSinglePionHCALDown", &jetVeto30_JetSinglePionHCALDown, &b_jetVeto30_JetSinglePionHCALDown);
   _tree->SetBranchAddress("jetVeto30_JetSinglePionHCALUp", &jetVeto30_JetSinglePionHCALUp, &b_jetVeto30_JetSinglePionHCALUp);
   _tree->SetBranchAddress("jetVeto30_JetTimePtEtaDown", &jetVeto30_JetTimePtEtaDown, &b_jetVeto30_JetTimePtEtaDown);
   _tree->SetBranchAddress("jetVeto30_JetTimePtEtaUp", &jetVeto30_JetTimePtEtaUp, &b_jetVeto30_JetTimePtEtaUp);
   _tree->SetBranchAddress("jetVeto30_JetTotalDown", &jetVeto30_JetTotalDown, &b_jetVeto30_JetTotalDown);
   _tree->SetBranchAddress("jetVeto30_JetTotalUp", &jetVeto30_JetTotalUp, &b_jetVeto30_JetTotalUp);
   _tree->SetBranchAddress("lumi", &lumi, &b_lumi);
   _tree->SetBranchAddress("mBestTrackType", &mBestTrackType, &b_mBestTrackType);
   _tree->SetBranchAddress("mCharge", &mCharge, &b_mCharge);
   _tree->SetBranchAddress("mChi2LocalPosition", &mChi2LocalPosition, &b_mChi2LocalPosition);
   _tree->SetBranchAddress("mComesFromHiggs", &mComesFromHiggs, &b_mComesFromHiggs);
   _tree->SetBranchAddress("mCutBasedIdGlobalHighPt", &mCutBasedIdGlobalHighPt, &b_mCutBasedIdGlobalHighPt);
   _tree->SetBranchAddress("mCutBasedIdLoose", &mCutBasedIdLoose, &b_mCutBasedIdLoose);
   _tree->SetBranchAddress("mCutBasedIdMedium", &mCutBasedIdMedium, &b_mCutBasedIdMedium);
   _tree->SetBranchAddress("mCutBasedIdMediumPrompt", &mCutBasedIdMediumPrompt, &b_mCutBasedIdMediumPrompt);
   _tree->SetBranchAddress("mCutBasedIdTight", &mCutBasedIdTight, &b_mCutBasedIdTight);
   _tree->SetBranchAddress("mCutBasedIdTrkHighPt", &mCutBasedIdTrkHighPt, &b_mCutBasedIdTrkHighPt);
   _tree->SetBranchAddress("mEcalIsoDR03", &mEcalIsoDR03, &b_mEcalIsoDR03);
   _tree->SetBranchAddress("mEffectiveArea2011", &mEffectiveArea2011, &b_mEffectiveArea2011);
   _tree->SetBranchAddress("mEffectiveArea2012", &mEffectiveArea2012, &b_mEffectiveArea2012);
   _tree->SetBranchAddress("mEta", &mEta, &b_mEta);
   _tree->SetBranchAddress("mEta_MuonEnDown", &mEta_MuonEnDown, &b_mEta_MuonEnDown);
   _tree->SetBranchAddress("mEta_MuonEnUp", &mEta_MuonEnUp, &b_mEta_MuonEnUp);
   _tree->SetBranchAddress("mGenCharge", &mGenCharge, &b_mGenCharge);
   _tree->SetBranchAddress("mGenDirectPromptTauDecayFinalState", &mGenDirectPromptTauDecayFinalState, &b_mGenDirectPromptTauDecayFinalState);
   _tree->SetBranchAddress("mGenEnergy", &mGenEnergy, &b_mGenEnergy);
   _tree->SetBranchAddress("mGenEta", &mGenEta, &b_mGenEta);
   _tree->SetBranchAddress("mGenIsPrompt", &mGenIsPrompt, &b_mGenIsPrompt);
   _tree->SetBranchAddress("mGenMotherPdgId", &mGenMotherPdgId, &b_mGenMotherPdgId);
   _tree->SetBranchAddress("mGenParticle", &mGenParticle, &b_mGenParticle);
   _tree->SetBranchAddress("mGenPdgId", &mGenPdgId, &b_mGenPdgId);
   _tree->SetBranchAddress("mGenPhi", &mGenPhi, &b_mGenPhi);
   _tree->SetBranchAddress("mGenPrompt", &mGenPrompt, &b_mGenPrompt);
   _tree->SetBranchAddress("mGenPromptFinalState", &mGenPromptFinalState, &b_mGenPromptFinalState);
   _tree->SetBranchAddress("mGenPromptTauDecay", &mGenPromptTauDecay, &b_mGenPromptTauDecay);
   _tree->SetBranchAddress("mGenPt", &mGenPt, &b_mGenPt);
   _tree->SetBranchAddress("mGenTauDecay", &mGenTauDecay, &b_mGenTauDecay);
   _tree->SetBranchAddress("mGenVZ", &mGenVZ, &b_mGenVZ);
   _tree->SetBranchAddress("mGenVtxPVMatch", &mGenVtxPVMatch, &b_mGenVtxPVMatch);
   _tree->SetBranchAddress("mHcalIsoDR03", &mHcalIsoDR03, &b_mHcalIsoDR03);
   _tree->SetBranchAddress("mIP3D", &mIP3D, &b_mIP3D);
   _tree->SetBranchAddress("mIP3DErr", &mIP3DErr, &b_mIP3DErr);
   _tree->SetBranchAddress("mIsGlobal", &mIsGlobal, &b_mIsGlobal);
   _tree->SetBranchAddress("mIsPFMuon", &mIsPFMuon, &b_mIsPFMuon);
   _tree->SetBranchAddress("mIsTracker", &mIsTracker, &b_mIsTracker);
   _tree->SetBranchAddress("mIsoDB03", &mIsoDB03, &b_mIsoDB03);
   _tree->SetBranchAddress("mIsoDB04", &mIsoDB04, &b_mIsoDB04);
   _tree->SetBranchAddress("mJetArea", &mJetArea, &b_mJetArea);
   _tree->SetBranchAddress("mJetBtag", &mJetBtag, &b_mJetBtag);
   _tree->SetBranchAddress("mJetDR", &mJetDR, &b_mJetDR);
   _tree->SetBranchAddress("mJetEtaEtaMoment", &mJetEtaEtaMoment, &b_mJetEtaEtaMoment);
   _tree->SetBranchAddress("mJetEtaPhiMoment", &mJetEtaPhiMoment, &b_mJetEtaPhiMoment);
   _tree->SetBranchAddress("mJetEtaPhiSpread", &mJetEtaPhiSpread, &b_mJetEtaPhiSpread);
   _tree->SetBranchAddress("mJetHadronFlavour", &mJetHadronFlavour, &b_mJetHadronFlavour);
   _tree->SetBranchAddress("mJetPFCISVBtag", &mJetPFCISVBtag, &b_mJetPFCISVBtag);
   _tree->SetBranchAddress("mJetPartonFlavour", &mJetPartonFlavour, &b_mJetPartonFlavour);
   _tree->SetBranchAddress("mJetPhiPhiMoment", &mJetPhiPhiMoment, &b_mJetPhiPhiMoment);
   _tree->SetBranchAddress("mJetPt", &mJetPt, &b_mJetPt);
   _tree->SetBranchAddress("mLowestMll", &mLowestMll, &b_mLowestMll);
   _tree->SetBranchAddress("mMass", &mMass, &b_mMass);
   _tree->SetBranchAddress("mMatchedStations", &mMatchedStations, &b_mMatchedStations);
   _tree->SetBranchAddress("mMatchesIsoMu20Tau27Filter", &mMatchesIsoMu20Tau27Filter, &b_mMatchesIsoMu20Tau27Filter);
   _tree->SetBranchAddress("mMatchesIsoMu20Tau27Path", &mMatchesIsoMu20Tau27Path, &b_mMatchesIsoMu20Tau27Path);
   _tree->SetBranchAddress("mMatchesIsoMu24Filter", &mMatchesIsoMu24Filter, &b_mMatchesIsoMu24Filter);
   _tree->SetBranchAddress("mMatchesIsoMu24Path", &mMatchesIsoMu24Path, &b_mMatchesIsoMu24Path);
   _tree->SetBranchAddress("mMatchesIsoMu27Filter", &mMatchesIsoMu27Filter, &b_mMatchesIsoMu27Filter);
   _tree->SetBranchAddress("mMatchesIsoMu27Path", &mMatchesIsoMu27Path, &b_mMatchesIsoMu27Path);
   _tree->SetBranchAddress("mMiniIsoLoose", &mMiniIsoLoose, &b_mMiniIsoLoose);
   _tree->SetBranchAddress("mMiniIsoMedium", &mMiniIsoMedium, &b_mMiniIsoMedium);
   _tree->SetBranchAddress("mMiniIsoTight", &mMiniIsoTight, &b_mMiniIsoTight);
   _tree->SetBranchAddress("mMiniIsoVeryTight", &mMiniIsoVeryTight, &b_mMiniIsoVeryTight);
   _tree->SetBranchAddress("mMuonHits", &mMuonHits, &b_mMuonHits);
   _tree->SetBranchAddress("mMvaLoose", &mMvaLoose, &b_mMvaLoose);
   _tree->SetBranchAddress("mMvaMedium", &mMvaMedium, &b_mMvaMedium);
   _tree->SetBranchAddress("mMvaTight", &mMvaTight, &b_mMvaTight);
   _tree->SetBranchAddress("mNearestZMass", &mNearestZMass, &b_mNearestZMass);
   _tree->SetBranchAddress("mNormTrkChi2", &mNormTrkChi2, &b_mNormTrkChi2);
   _tree->SetBranchAddress("mNormalizedChi2", &mNormalizedChi2, &b_mNormalizedChi2);
   _tree->SetBranchAddress("mPFChargedHadronIsoR04", &mPFChargedHadronIsoR04, &b_mPFChargedHadronIsoR04);
   _tree->SetBranchAddress("mPFChargedIso", &mPFChargedIso, &b_mPFChargedIso);
   _tree->SetBranchAddress("mPFIDLoose", &mPFIDLoose, &b_mPFIDLoose);
   _tree->SetBranchAddress("mPFIDMedium", &mPFIDMedium, &b_mPFIDMedium);
   _tree->SetBranchAddress("mPFIDTight", &mPFIDTight, &b_mPFIDTight);
   _tree->SetBranchAddress("mPFIsoLoose", &mPFIsoLoose, &b_mPFIsoLoose);
   _tree->SetBranchAddress("mPFIsoMedium", &mPFIsoMedium, &b_mPFIsoMedium);
   _tree->SetBranchAddress("mPFIsoTight", &mPFIsoTight, &b_mPFIsoTight);
   _tree->SetBranchAddress("mPFIsoVeryLoose", &mPFIsoVeryLoose, &b_mPFIsoVeryLoose);
   _tree->SetBranchAddress("mPFIsoVeryTight", &mPFIsoVeryTight, &b_mPFIsoVeryTight);
   _tree->SetBranchAddress("mPFNeutralHadronIsoR04", &mPFNeutralHadronIsoR04, &b_mPFNeutralHadronIsoR04);
   _tree->SetBranchAddress("mPFNeutralIso", &mPFNeutralIso, &b_mPFNeutralIso);
   _tree->SetBranchAddress("mPFPUChargedIso", &mPFPUChargedIso, &b_mPFPUChargedIso);
   _tree->SetBranchAddress("mPFPhotonIso", &mPFPhotonIso, &b_mPFPhotonIso);
   _tree->SetBranchAddress("mPFPhotonIsoR04", &mPFPhotonIsoR04, &b_mPFPhotonIsoR04);
   _tree->SetBranchAddress("mPFPileupIsoR04", &mPFPileupIsoR04, &b_mPFPileupIsoR04);
   _tree->SetBranchAddress("mPVDXY", &mPVDXY, &b_mPVDXY);
   _tree->SetBranchAddress("mPVDZ", &mPVDZ, &b_mPVDZ);
   _tree->SetBranchAddress("mPhi", &mPhi, &b_mPhi);
   _tree->SetBranchAddress("mPhi_MuonEnDown", &mPhi_MuonEnDown, &b_mPhi_MuonEnDown);
   _tree->SetBranchAddress("mPhi_MuonEnUp", &mPhi_MuonEnUp, &b_mPhi_MuonEnUp);
   _tree->SetBranchAddress("mPixHits", &mPixHits, &b_mPixHits);
   _tree->SetBranchAddress("mPt", &mPt, &b_mPt);
   _tree->SetBranchAddress("mPt_MuonEnDown", &mPt_MuonEnDown, &b_mPt_MuonEnDown);
   _tree->SetBranchAddress("mPt_MuonEnUp", &mPt_MuonEnUp, &b_mPt_MuonEnUp);
   _tree->SetBranchAddress("mRelPFIsoDBDefault", &mRelPFIsoDBDefault, &b_mRelPFIsoDBDefault);
   _tree->SetBranchAddress("mRelPFIsoDBDefaultR04", &mRelPFIsoDBDefaultR04, &b_mRelPFIsoDBDefaultR04);
   _tree->SetBranchAddress("mRelPFIsoRho", &mRelPFIsoRho, &b_mRelPFIsoRho);
   _tree->SetBranchAddress("mRho", &mRho, &b_mRho);
   _tree->SetBranchAddress("mSIP2D", &mSIP2D, &b_mSIP2D);
   _tree->SetBranchAddress("mSIP3D", &mSIP3D, &b_mSIP3D);
   _tree->SetBranchAddress("mSegmentCompatibility", &mSegmentCompatibility, &b_mSegmentCompatibility);
   _tree->SetBranchAddress("mSoftCutBasedId", &mSoftCutBasedId, &b_mSoftCutBasedId);
   _tree->SetBranchAddress("mTkIsoLoose", &mTkIsoLoose, &b_mTkIsoLoose);
   _tree->SetBranchAddress("mTkIsoTight", &mTkIsoTight, &b_mTkIsoTight);
   _tree->SetBranchAddress("mTkLayersWithMeasurement", &mTkLayersWithMeasurement, &b_mTkLayersWithMeasurement);
   _tree->SetBranchAddress("mTrkIsoDR03", &mTrkIsoDR03, &b_mTrkIsoDR03);
   _tree->SetBranchAddress("mTrkKink", &mTrkKink, &b_mTrkKink);
   _tree->SetBranchAddress("mTypeCode", &mTypeCode, &b_mTypeCode);
   _tree->SetBranchAddress("mVZ", &mVZ, &b_mVZ);
   _tree->SetBranchAddress("mValidFraction", &mValidFraction, &b_mValidFraction);
   _tree->SetBranchAddress("mZTTGenMatching", &mZTTGenMatching, &b_mZTTGenMatching);
   _tree->SetBranchAddress("m_t_DR", &m_t_DR, &b_m_t_DR);
   _tree->SetBranchAddress("m_t_Mass", &m_t_Mass, &b_m_t_Mass);
   _tree->SetBranchAddress("m_t_doubleL1IsoTauMatch", &m_t_doubleL1IsoTauMatch, &b_m_t_doubleL1IsoTauMatch);
   _tree->SetBranchAddress("metSig", &metSig, &b_metSig);
   _tree->SetBranchAddress("metcov00", &metcov00, &b_metcov00);
   _tree->SetBranchAddress("metcov00_DESYlike", &metcov00_DESYlike, &b_metcov00_DESYlike);
   _tree->SetBranchAddress("metcov01", &metcov01, &b_metcov01);
   _tree->SetBranchAddress("metcov01_DESYlike", &metcov01_DESYlike, &b_metcov01_DESYlike);
   _tree->SetBranchAddress("metcov10", &metcov10, &b_metcov10);
   _tree->SetBranchAddress("metcov10_DESYlike", &metcov10_DESYlike, &b_metcov10_DESYlike);
   _tree->SetBranchAddress("metcov11", &metcov11, &b_metcov11);
   _tree->SetBranchAddress("metcov11_DESYlike", &metcov11_DESYlike, &b_metcov11_DESYlike);
   _tree->SetBranchAddress("mu12e23DZGroup", &mu12e23DZGroup, &b_mu12e23DZGroup);
   _tree->SetBranchAddress("mu12e23DZPass", &mu12e23DZPass, &b_mu12e23DZPass);
   _tree->SetBranchAddress("mu12e23DZPrescale", &mu12e23DZPrescale, &b_mu12e23DZPrescale);
   _tree->SetBranchAddress("mu12e23Group", &mu12e23Group, &b_mu12e23Group);
   _tree->SetBranchAddress("mu12e23Pass", &mu12e23Pass, &b_mu12e23Pass);
   _tree->SetBranchAddress("mu12e23Prescale", &mu12e23Prescale, &b_mu12e23Prescale);
   _tree->SetBranchAddress("mu23e12DZGroup", &mu23e12DZGroup, &b_mu23e12DZGroup);
   _tree->SetBranchAddress("mu23e12DZPass", &mu23e12DZPass, &b_mu23e12DZPass);
   _tree->SetBranchAddress("mu23e12DZPrescale", &mu23e12DZPrescale, &b_mu23e12DZPrescale);
   _tree->SetBranchAddress("mu23e12Group", &mu23e12Group, &b_mu23e12Group);
   _tree->SetBranchAddress("mu23e12Pass", &mu23e12Pass, &b_mu23e12Pass);
   _tree->SetBranchAddress("mu23e12Prescale", &mu23e12Prescale, &b_mu23e12Prescale);
   _tree->SetBranchAddress("muGlbIsoVetoPt10", &muGlbIsoVetoPt10, &b_muGlbIsoVetoPt10);
   _tree->SetBranchAddress("muVetoZTTp001dxyz", &muVetoZTTp001dxyz, &b_muVetoZTTp001dxyz);
   _tree->SetBranchAddress("muVetoZTTp001dxyzR0", &muVetoZTTp001dxyzR0, &b_muVetoZTTp001dxyzR0);
   _tree->SetBranchAddress("nTruePU", &nTruePU, &b_nTruePU);
   _tree->SetBranchAddress("npNLO", &npNLO, &b_npNLO);
   _tree->SetBranchAddress("numGenJets", &numGenJets, &b_numGenJets);
   _tree->SetBranchAddress("nvtx", &nvtx, &b_nvtx);
   _tree->SetBranchAddress("processID", &processID, &b_processID);
   _tree->SetBranchAddress("puppiMetEt", &puppiMetEt, &b_puppiMetEt);
   _tree->SetBranchAddress("puppiMetPhi", &puppiMetPhi, &b_puppiMetPhi);
   _tree->SetBranchAddress("pvChi2", &pvChi2, &b_pvChi2);
   _tree->SetBranchAddress("pvDX", &pvDX, &b_pvDX);
   _tree->SetBranchAddress("pvDY", &pvDY, &b_pvDY);
   _tree->SetBranchAddress("pvDZ", &pvDZ, &b_pvDZ);
   _tree->SetBranchAddress("pvIsFake", &pvIsFake, &b_pvIsFake);
   _tree->SetBranchAddress("pvIsValid", &pvIsValid, &b_pvIsValid);
   _tree->SetBranchAddress("pvNormChi2", &pvNormChi2, &b_pvNormChi2);
   _tree->SetBranchAddress("pvRho", &pvRho, &b_pvRho);
   _tree->SetBranchAddress("pvX", &pvX, &b_pvX);
   _tree->SetBranchAddress("pvY", &pvY, &b_pvY);
   _tree->SetBranchAddress("pvZ", &pvZ, &b_pvZ);
   _tree->SetBranchAddress("pvndof", &pvndof, &b_pvndof);
   _tree->SetBranchAddress("raw_pfMetEt", &raw_pfMetEt, &b_raw_pfMetEt);
   _tree->SetBranchAddress("raw_pfMetPhi", &raw_pfMetPhi, &b_raw_pfMetPhi);
   _tree->SetBranchAddress("recoilDaught", &recoilDaught, &b_recoilDaught);
   _tree->SetBranchAddress("recoilWithMet", &recoilWithMet, &b_recoilWithMet);
   _tree->SetBranchAddress("rho", &rho, &b_rho);
   _tree->SetBranchAddress("run", &run, &b_run);
   _tree->SetBranchAddress("tAgainstElectronLooseMVA6", &tAgainstElectronLooseMVA6, &b_tAgainstElectronLooseMVA6);
   _tree->SetBranchAddress("tAgainstElectronMVA6Raw", &tAgainstElectronMVA6Raw, &b_tAgainstElectronMVA6Raw);
   _tree->SetBranchAddress("tAgainstElectronMVA6category", &tAgainstElectronMVA6category, &b_tAgainstElectronMVA6category);
   _tree->SetBranchAddress("tAgainstElectronMediumMVA6", &tAgainstElectronMediumMVA6, &b_tAgainstElectronMediumMVA6);
   _tree->SetBranchAddress("tAgainstElectronTightMVA6", &tAgainstElectronTightMVA6, &b_tAgainstElectronTightMVA6);
   _tree->SetBranchAddress("tAgainstElectronVLooseMVA6", &tAgainstElectronVLooseMVA6, &b_tAgainstElectronVLooseMVA6);
   _tree->SetBranchAddress("tAgainstElectronVTightMVA6", &tAgainstElectronVTightMVA6, &b_tAgainstElectronVTightMVA6);
   _tree->SetBranchAddress("tAgainstMuonLoose3", &tAgainstMuonLoose3, &b_tAgainstMuonLoose3);
   _tree->SetBranchAddress("tAgainstMuonTight3", &tAgainstMuonTight3, &b_tAgainstMuonTight3);
   _tree->SetBranchAddress("tByCombinedIsolationDeltaBetaCorrRaw3Hits", &tByCombinedIsolationDeltaBetaCorrRaw3Hits, &b_tByCombinedIsolationDeltaBetaCorrRaw3Hits);
   _tree->SetBranchAddress("tByIsolationMVArun2v1DBdR03oldDMwLTraw", &tByIsolationMVArun2v1DBdR03oldDMwLTraw, &b_tByIsolationMVArun2v1DBdR03oldDMwLTraw);
   _tree->SetBranchAddress("tByIsolationMVArun2v1DBnewDMwLTraw", &tByIsolationMVArun2v1DBnewDMwLTraw, &b_tByIsolationMVArun2v1DBnewDMwLTraw);
   _tree->SetBranchAddress("tByIsolationMVArun2v1DBoldDMwLTraw", &tByIsolationMVArun2v1DBoldDMwLTraw, &b_tByIsolationMVArun2v1DBoldDMwLTraw);
   _tree->SetBranchAddress("tByLooseCombinedIsolationDeltaBetaCorr3Hits", &tByLooseCombinedIsolationDeltaBetaCorr3Hits, &b_tByLooseCombinedIsolationDeltaBetaCorr3Hits);
   _tree->SetBranchAddress("tByLooseIsolationMVArun2v1DBdR03oldDMwLT", &tByLooseIsolationMVArun2v1DBdR03oldDMwLT, &b_tByLooseIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByLooseIsolationMVArun2v1DBnewDMwLT", &tByLooseIsolationMVArun2v1DBnewDMwLT, &b_tByLooseIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByLooseIsolationMVArun2v1DBoldDMwLT", &tByLooseIsolationMVArun2v1DBoldDMwLT, &b_tByLooseIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tByMediumCombinedIsolationDeltaBetaCorr3Hits", &tByMediumCombinedIsolationDeltaBetaCorr3Hits, &b_tByMediumCombinedIsolationDeltaBetaCorr3Hits);
   _tree->SetBranchAddress("tByMediumIsolationMVArun2v1DBdR03oldDMwLT", &tByMediumIsolationMVArun2v1DBdR03oldDMwLT, &b_tByMediumIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByMediumIsolationMVArun2v1DBnewDMwLT", &tByMediumIsolationMVArun2v1DBnewDMwLT, &b_tByMediumIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByMediumIsolationMVArun2v1DBoldDMwLT", &tByMediumIsolationMVArun2v1DBoldDMwLT, &b_tByMediumIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tByPhotonPtSumOutsideSignalCone", &tByPhotonPtSumOutsideSignalCone, &b_tByPhotonPtSumOutsideSignalCone);
   _tree->SetBranchAddress("tByTightCombinedIsolationDeltaBetaCorr3Hits", &tByTightCombinedIsolationDeltaBetaCorr3Hits, &b_tByTightCombinedIsolationDeltaBetaCorr3Hits);
   _tree->SetBranchAddress("tByTightIsolationMVArun2v1DBdR03oldDMwLT", &tByTightIsolationMVArun2v1DBdR03oldDMwLT, &b_tByTightIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByTightIsolationMVArun2v1DBnewDMwLT", &tByTightIsolationMVArun2v1DBnewDMwLT, &b_tByTightIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByTightIsolationMVArun2v1DBoldDMwLT", &tByTightIsolationMVArun2v1DBoldDMwLT, &b_tByTightIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tByVLooseIsolationMVArun2v1DBdR03oldDMwLT", &tByVLooseIsolationMVArun2v1DBdR03oldDMwLT, &b_tByVLooseIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByVLooseIsolationMVArun2v1DBnewDMwLT", &tByVLooseIsolationMVArun2v1DBnewDMwLT, &b_tByVLooseIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByVLooseIsolationMVArun2v1DBoldDMwLT", &tByVLooseIsolationMVArun2v1DBoldDMwLT, &b_tByVLooseIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tByVTightIsolationMVArun2v1DBdR03oldDMwLT", &tByVTightIsolationMVArun2v1DBdR03oldDMwLT, &b_tByVTightIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByVTightIsolationMVArun2v1DBnewDMwLT", &tByVTightIsolationMVArun2v1DBnewDMwLT, &b_tByVTightIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByVTightIsolationMVArun2v1DBoldDMwLT", &tByVTightIsolationMVArun2v1DBoldDMwLT, &b_tByVTightIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tByVVTightIsolationMVArun2v1DBdR03oldDMwLT", &tByVVTightIsolationMVArun2v1DBdR03oldDMwLT, &b_tByVVTightIsolationMVArun2v1DBdR03oldDMwLT);
   _tree->SetBranchAddress("tByVVTightIsolationMVArun2v1DBnewDMwLT", &tByVVTightIsolationMVArun2v1DBnewDMwLT, &b_tByVVTightIsolationMVArun2v1DBnewDMwLT);
   _tree->SetBranchAddress("tByVVTightIsolationMVArun2v1DBoldDMwLT", &tByVVTightIsolationMVArun2v1DBoldDMwLT, &b_tByVVTightIsolationMVArun2v1DBoldDMwLT);
   _tree->SetBranchAddress("tCharge", &tCharge, &b_tCharge);
   _tree->SetBranchAddress("tChargedIsoPtSum", &tChargedIsoPtSum, &b_tChargedIsoPtSum);
   _tree->SetBranchAddress("tChargedIsoPtSumdR03", &tChargedIsoPtSumdR03, &b_tChargedIsoPtSumdR03);
   _tree->SetBranchAddress("tComesFromHiggs", &tComesFromHiggs, &b_tComesFromHiggs);
   _tree->SetBranchAddress("tDecayMode", &tDecayMode, &b_tDecayMode);
   _tree->SetBranchAddress("tDecayModeFinding", &tDecayModeFinding, &b_tDecayModeFinding);
   _tree->SetBranchAddress("tDecayModeFindingNewDMs", &tDecayModeFindingNewDMs, &b_tDecayModeFindingNewDMs);
   _tree->SetBranchAddress("tEta", &tEta, &b_tEta);
   _tree->SetBranchAddress("tFootprintCorrection", &tFootprintCorrection, &b_tFootprintCorrection);
   _tree->SetBranchAddress("tFootprintCorrectiondR03", &tFootprintCorrectiondR03, &b_tFootprintCorrectiondR03);
   _tree->SetBranchAddress("tGenCharge", &tGenCharge, &b_tGenCharge);
   _tree->SetBranchAddress("tGenDecayMode", &tGenDecayMode, &b_tGenDecayMode);
   _tree->SetBranchAddress("tGenEnergy", &tGenEnergy, &b_tGenEnergy);
   _tree->SetBranchAddress("tGenEta", &tGenEta, &b_tGenEta);
   _tree->SetBranchAddress("tGenJetEta", &tGenJetEta, &b_tGenJetEta);
   _tree->SetBranchAddress("tGenJetPt", &tGenJetPt, &b_tGenJetPt);
   _tree->SetBranchAddress("tGenMotherEnergy", &tGenMotherEnergy, &b_tGenMotherEnergy);
   _tree->SetBranchAddress("tGenMotherEta", &tGenMotherEta, &b_tGenMotherEta);
   _tree->SetBranchAddress("tGenMotherPdgId", &tGenMotherPdgId, &b_tGenMotherPdgId);
   _tree->SetBranchAddress("tGenMotherPhi", &tGenMotherPhi, &b_tGenMotherPhi);
   _tree->SetBranchAddress("tGenMotherPt", &tGenMotherPt, &b_tGenMotherPt);
   _tree->SetBranchAddress("tGenPdgId", &tGenPdgId, &b_tGenPdgId);
   _tree->SetBranchAddress("tGenPhi", &tGenPhi, &b_tGenPhi);
   _tree->SetBranchAddress("tGenPt", &tGenPt, &b_tGenPt);
   _tree->SetBranchAddress("tGenStatus", &tGenStatus, &b_tGenStatus);
   _tree->SetBranchAddress("tJetArea", &tJetArea, &b_tJetArea);
   _tree->SetBranchAddress("tJetBtag", &tJetBtag, &b_tJetBtag);
   _tree->SetBranchAddress("tJetDR", &tJetDR, &b_tJetDR);
   _tree->SetBranchAddress("tJetEtaEtaMoment", &tJetEtaEtaMoment, &b_tJetEtaEtaMoment);
   _tree->SetBranchAddress("tJetEtaPhiMoment", &tJetEtaPhiMoment, &b_tJetEtaPhiMoment);
   _tree->SetBranchAddress("tJetEtaPhiSpread", &tJetEtaPhiSpread, &b_tJetEtaPhiSpread);
   _tree->SetBranchAddress("tJetHadronFlavour", &tJetHadronFlavour, &b_tJetHadronFlavour);
   _tree->SetBranchAddress("tJetPFCISVBtag", &tJetPFCISVBtag, &b_tJetPFCISVBtag);
   _tree->SetBranchAddress("tJetPartonFlavour", &tJetPartonFlavour, &b_tJetPartonFlavour);
   _tree->SetBranchAddress("tJetPhiPhiMoment", &tJetPhiPhiMoment, &b_tJetPhiPhiMoment);
   _tree->SetBranchAddress("tJetPt", &tJetPt, &b_tJetPt);
   _tree->SetBranchAddress("tL1IsoTauMatch", &tL1IsoTauMatch, &b_tL1IsoTauMatch);
   _tree->SetBranchAddress("tL1IsoTauPt", &tL1IsoTauPt, &b_tL1IsoTauPt);
   _tree->SetBranchAddress("tLeadTrackPt", &tLeadTrackPt, &b_tLeadTrackPt);
   _tree->SetBranchAddress("tLowestMll", &tLowestMll, &b_tLowestMll);
   _tree->SetBranchAddress("tMass", &tMass, &b_tMass);
   _tree->SetBranchAddress("tMatchesDoubleMediumTau35Filter", &tMatchesDoubleMediumTau35Filter, &b_tMatchesDoubleMediumTau35Filter);
   _tree->SetBranchAddress("tMatchesDoubleMediumTau35Path", &tMatchesDoubleMediumTau35Path, &b_tMatchesDoubleMediumTau35Path);
   _tree->SetBranchAddress("tMatchesDoubleMediumTau40Filter", &tMatchesDoubleMediumTau40Filter, &b_tMatchesDoubleMediumTau40Filter);
   _tree->SetBranchAddress("tMatchesDoubleMediumTau40Path", &tMatchesDoubleMediumTau40Path, &b_tMatchesDoubleMediumTau40Path);
   _tree->SetBranchAddress("tMatchesDoubleTightTau35Filter", &tMatchesDoubleTightTau35Filter, &b_tMatchesDoubleTightTau35Filter);
   _tree->SetBranchAddress("tMatchesDoubleTightTau35Path", &tMatchesDoubleTightTau35Path, &b_tMatchesDoubleTightTau35Path);
   _tree->SetBranchAddress("tMatchesDoubleTightTau40Filter", &tMatchesDoubleTightTau40Filter, &b_tMatchesDoubleTightTau40Filter);
   _tree->SetBranchAddress("tMatchesDoubleTightTau40Path", &tMatchesDoubleTightTau40Path, &b_tMatchesDoubleTightTau40Path);
   _tree->SetBranchAddress("tMatchesEle24Tau30Filter", &tMatchesEle24Tau30Filter, &b_tMatchesEle24Tau30Filter);
   _tree->SetBranchAddress("tMatchesEle24Tau30Path", &tMatchesEle24Tau30Path, &b_tMatchesEle24Tau30Path);
   _tree->SetBranchAddress("tMatchesIsoMu20Tau27Filter", &tMatchesIsoMu20Tau27Filter, &b_tMatchesIsoMu20Tau27Filter);
   _tree->SetBranchAddress("tMatchesIsoMu20Tau27Path", &tMatchesIsoMu20Tau27Path, &b_tMatchesIsoMu20Tau27Path);
   _tree->SetBranchAddress("tNChrgHadrIsolationCands", &tNChrgHadrIsolationCands, &b_tNChrgHadrIsolationCands);
   _tree->SetBranchAddress("tNChrgHadrSignalCands", &tNChrgHadrSignalCands, &b_tNChrgHadrSignalCands);
   _tree->SetBranchAddress("tNGammaSignalCands", &tNGammaSignalCands, &b_tNGammaSignalCands);
   _tree->SetBranchAddress("tNNeutralHadrSignalCands", &tNNeutralHadrSignalCands, &b_tNNeutralHadrSignalCands);
   _tree->SetBranchAddress("tNSignalCands", &tNSignalCands, &b_tNSignalCands);
   _tree->SetBranchAddress("tNearestZMass", &tNearestZMass, &b_tNearestZMass);
   _tree->SetBranchAddress("tNeutralIsoPtSum", &tNeutralIsoPtSum, &b_tNeutralIsoPtSum);
   _tree->SetBranchAddress("tNeutralIsoPtSumWeight", &tNeutralIsoPtSumWeight, &b_tNeutralIsoPtSumWeight);
   _tree->SetBranchAddress("tNeutralIsoPtSumWeightdR03", &tNeutralIsoPtSumWeightdR03, &b_tNeutralIsoPtSumWeightdR03);
   _tree->SetBranchAddress("tNeutralIsoPtSumdR03", &tNeutralIsoPtSumdR03, &b_tNeutralIsoPtSumdR03);
   _tree->SetBranchAddress("tPVDXY", &tPVDXY, &b_tPVDXY);
   _tree->SetBranchAddress("tPVDZ", &tPVDZ, &b_tPVDZ);
   _tree->SetBranchAddress("tPhi", &tPhi, &b_tPhi);
   _tree->SetBranchAddress("tPhotonPtSumOutsideSignalCone", &tPhotonPtSumOutsideSignalCone, &b_tPhotonPtSumOutsideSignalCone);
   _tree->SetBranchAddress("tPhotonPtSumOutsideSignalConedR03", &tPhotonPtSumOutsideSignalConedR03, &b_tPhotonPtSumOutsideSignalConedR03);
   _tree->SetBranchAddress("tPt", &tPt, &b_tPt);
   _tree->SetBranchAddress("tPuCorrPtSum", &tPuCorrPtSum, &b_tPuCorrPtSum);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTLoose", &tRerunMVArun2v1DBoldDMwLTLoose, &b_tRerunMVArun2v1DBoldDMwLTLoose);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTMedium", &tRerunMVArun2v1DBoldDMwLTMedium, &b_tRerunMVArun2v1DBoldDMwLTMedium);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTTight", &tRerunMVArun2v1DBoldDMwLTTight, &b_tRerunMVArun2v1DBoldDMwLTTight);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTVLoose", &tRerunMVArun2v1DBoldDMwLTVLoose, &b_tRerunMVArun2v1DBoldDMwLTVLoose);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTVTight", &tRerunMVArun2v1DBoldDMwLTVTight, &b_tRerunMVArun2v1DBoldDMwLTVTight);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTVVTight", &tRerunMVArun2v1DBoldDMwLTVVTight, &b_tRerunMVArun2v1DBoldDMwLTVVTight);
   _tree->SetBranchAddress("tRerunMVArun2v1DBoldDMwLTraw", &tRerunMVArun2v1DBoldDMwLTraw, &b_tRerunMVArun2v1DBoldDMwLTraw);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTLoose", &tRerunMVArun2v2DBoldDMwLTLoose, &b_tRerunMVArun2v2DBoldDMwLTLoose);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTMedium", &tRerunMVArun2v2DBoldDMwLTMedium, &b_tRerunMVArun2v2DBoldDMwLTMedium);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTTight", &tRerunMVArun2v2DBoldDMwLTTight, &b_tRerunMVArun2v2DBoldDMwLTTight);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTVLoose", &tRerunMVArun2v2DBoldDMwLTVLoose, &b_tRerunMVArun2v2DBoldDMwLTVLoose);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTVTight", &tRerunMVArun2v2DBoldDMwLTVTight, &b_tRerunMVArun2v2DBoldDMwLTVTight);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTVVLoose", &tRerunMVArun2v2DBoldDMwLTVVLoose, &b_tRerunMVArun2v2DBoldDMwLTVVLoose);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTVVTight", &tRerunMVArun2v2DBoldDMwLTVVTight, &b_tRerunMVArun2v2DBoldDMwLTVVTight);
   _tree->SetBranchAddress("tRerunMVArun2v2DBoldDMwLTraw", &tRerunMVArun2v2DBoldDMwLTraw, &b_tRerunMVArun2v2DBoldDMwLTraw);
   _tree->SetBranchAddress("tVZ", &tVZ, &b_tVZ);
   _tree->SetBranchAddress("tZTTGenDR", &tZTTGenDR, &b_tZTTGenDR);
   _tree->SetBranchAddress("tZTTGenEta", &tZTTGenEta, &b_tZTTGenEta);
   _tree->SetBranchAddress("tZTTGenMatching", &tZTTGenMatching, &b_tZTTGenMatching);
   _tree->SetBranchAddress("tZTTGenPhi", &tZTTGenPhi, &b_tZTTGenPhi);
   _tree->SetBranchAddress("tZTTGenPt", &tZTTGenPt, &b_tZTTGenPt);
   _tree->SetBranchAddress("tauVetoPt20Loose3HitsVtx", &tauVetoPt20Loose3HitsVtx, &b_tauVetoPt20Loose3HitsVtx);
   _tree->SetBranchAddress("tauVetoPt20TightMVALTVtx", &tauVetoPt20TightMVALTVtx, &b_tauVetoPt20TightMVALTVtx);
   _tree->SetBranchAddress("topQuarkPt1", &topQuarkPt1, &b_topQuarkPt1);
   _tree->SetBranchAddress("topQuarkPt2", &topQuarkPt2, &b_topQuarkPt2);
   _tree->SetBranchAddress("tripleEGroup", &tripleEGroup, &b_tripleEGroup);
   _tree->SetBranchAddress("tripleEPass", &tripleEPass, &b_tripleEPass);
   _tree->SetBranchAddress("tripleEPrescale", &tripleEPrescale, &b_tripleEPrescale);
   _tree->SetBranchAddress("tripleMu12_10_5Group", &tripleMu12_10_5Group, &b_tripleMu12_10_5Group);
   _tree->SetBranchAddress("tripleMu12_10_5Pass", &tripleMu12_10_5Pass, &b_tripleMu12_10_5Pass);
   _tree->SetBranchAddress("tripleMu12_10_5Prescale", &tripleMu12_10_5Prescale, &b_tripleMu12_10_5Prescale);
   _tree->SetBranchAddress("type1_pfMetEt", &type1_pfMetEt, &b_type1_pfMetEt);
   _tree->SetBranchAddress("type1_pfMetPhi", &type1_pfMetPhi, &b_type1_pfMetPhi);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEnDown", &type1_pfMet_shiftedPhi_JetEnDown, &b_type1_pfMet_shiftedPhi_JetEnDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEnUp", &type1_pfMet_shiftedPhi_JetEnUp, &b_type1_pfMet_shiftedPhi_JetEnUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta0to3Down", &type1_pfMet_shiftedPhi_JetEta0to3Down, &b_type1_pfMet_shiftedPhi_JetEta0to3Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta0to3Up", &type1_pfMet_shiftedPhi_JetEta0to3Up, &b_type1_pfMet_shiftedPhi_JetEta0to3Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta0to5Down", &type1_pfMet_shiftedPhi_JetEta0to5Down, &b_type1_pfMet_shiftedPhi_JetEta0to5Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta0to5Up", &type1_pfMet_shiftedPhi_JetEta0to5Up, &b_type1_pfMet_shiftedPhi_JetEta0to5Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta3to5Down", &type1_pfMet_shiftedPhi_JetEta3to5Down, &b_type1_pfMet_shiftedPhi_JetEta3to5Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetEta3to5Up", &type1_pfMet_shiftedPhi_JetEta3to5Up, &b_type1_pfMet_shiftedPhi_JetEta3to5Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetRelativeBalDown", &type1_pfMet_shiftedPhi_JetRelativeBalDown, &b_type1_pfMet_shiftedPhi_JetRelativeBalDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetRelativeBalUp", &type1_pfMet_shiftedPhi_JetRelativeBalUp, &b_type1_pfMet_shiftedPhi_JetRelativeBalUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetRelativeSampleDown", &type1_pfMet_shiftedPhi_JetRelativeSampleDown, &b_type1_pfMet_shiftedPhi_JetRelativeSampleDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetRelativeSampleUp", &type1_pfMet_shiftedPhi_JetRelativeSampleUp, &b_type1_pfMet_shiftedPhi_JetRelativeSampleUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetResDown", &type1_pfMet_shiftedPhi_JetResDown, &b_type1_pfMet_shiftedPhi_JetResDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetResUp", &type1_pfMet_shiftedPhi_JetResUp, &b_type1_pfMet_shiftedPhi_JetResUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetTotalDown", &type1_pfMet_shiftedPhi_JetTotalDown, &b_type1_pfMet_shiftedPhi_JetTotalDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_JetTotalUp", &type1_pfMet_shiftedPhi_JetTotalUp, &b_type1_pfMet_shiftedPhi_JetTotalUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_UnclusteredEnDown", &type1_pfMet_shiftedPhi_UnclusteredEnDown, &b_type1_pfMet_shiftedPhi_UnclusteredEnDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPhi_UnclusteredEnUp", &type1_pfMet_shiftedPhi_UnclusteredEnUp, &b_type1_pfMet_shiftedPhi_UnclusteredEnUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEnDown", &type1_pfMet_shiftedPt_JetEnDown, &b_type1_pfMet_shiftedPt_JetEnDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEnUp", &type1_pfMet_shiftedPt_JetEnUp, &b_type1_pfMet_shiftedPt_JetEnUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta0to3Down", &type1_pfMet_shiftedPt_JetEta0to3Down, &b_type1_pfMet_shiftedPt_JetEta0to3Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta0to3Up", &type1_pfMet_shiftedPt_JetEta0to3Up, &b_type1_pfMet_shiftedPt_JetEta0to3Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta0to5Down", &type1_pfMet_shiftedPt_JetEta0to5Down, &b_type1_pfMet_shiftedPt_JetEta0to5Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta0to5Up", &type1_pfMet_shiftedPt_JetEta0to5Up, &b_type1_pfMet_shiftedPt_JetEta0to5Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta3to5Down", &type1_pfMet_shiftedPt_JetEta3to5Down, &b_type1_pfMet_shiftedPt_JetEta3to5Down);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetEta3to5Up", &type1_pfMet_shiftedPt_JetEta3to5Up, &b_type1_pfMet_shiftedPt_JetEta3to5Up);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetRelativeBalDown", &type1_pfMet_shiftedPt_JetRelativeBalDown, &b_type1_pfMet_shiftedPt_JetRelativeBalDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetRelativeBalUp", &type1_pfMet_shiftedPt_JetRelativeBalUp, &b_type1_pfMet_shiftedPt_JetRelativeBalUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetRelativeSampleDown", &type1_pfMet_shiftedPt_JetRelativeSampleDown, &b_type1_pfMet_shiftedPt_JetRelativeSampleDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetRelativeSampleUp", &type1_pfMet_shiftedPt_JetRelativeSampleUp, &b_type1_pfMet_shiftedPt_JetRelativeSampleUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetResDown", &type1_pfMet_shiftedPt_JetResDown, &b_type1_pfMet_shiftedPt_JetResDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetResUp", &type1_pfMet_shiftedPt_JetResUp, &b_type1_pfMet_shiftedPt_JetResUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetTotalDown", &type1_pfMet_shiftedPt_JetTotalDown, &b_type1_pfMet_shiftedPt_JetTotalDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_JetTotalUp", &type1_pfMet_shiftedPt_JetTotalUp, &b_type1_pfMet_shiftedPt_JetTotalUp);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_UnclusteredEnDown", &type1_pfMet_shiftedPt_UnclusteredEnDown, &b_type1_pfMet_shiftedPt_UnclusteredEnDown);
   _tree->SetBranchAddress("type1_pfMet_shiftedPt_UnclusteredEnUp", &type1_pfMet_shiftedPt_UnclusteredEnUp, &b_type1_pfMet_shiftedPt_UnclusteredEnUp);
   _tree->SetBranchAddress("vbfDeta", &vbfDeta, &b_vbfDeta);
   _tree->SetBranchAddress("vbfJetVeto20", &vbfJetVeto20, &b_vbfJetVeto20);
   _tree->SetBranchAddress("vbfJetVeto30", &vbfJetVeto30, &b_vbfJetVeto30);
   _tree->SetBranchAddress("vbfMass", &vbfMass, &b_vbfMass);
   _tree->SetBranchAddress("vbfMassWoNoisyJets", &vbfMassWoNoisyJets, &b_vbfMassWoNoisyJets);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta0to3Down", &vbfMassWoNoisyJets_JetEta0to3Down, &b_vbfMassWoNoisyJets_JetEta0to3Down);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta0to3Up", &vbfMassWoNoisyJets_JetEta0to3Up, &b_vbfMassWoNoisyJets_JetEta0to3Up);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta0to5Down", &vbfMassWoNoisyJets_JetEta0to5Down, &b_vbfMassWoNoisyJets_JetEta0to5Down);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta0to5Up", &vbfMassWoNoisyJets_JetEta0to5Up, &b_vbfMassWoNoisyJets_JetEta0to5Up);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta3to5Down", &vbfMassWoNoisyJets_JetEta3to5Down, &b_vbfMassWoNoisyJets_JetEta3to5Down);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetEta3to5Up", &vbfMassWoNoisyJets_JetEta3to5Up, &b_vbfMassWoNoisyJets_JetEta3to5Up);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetRelativeBalDown", &vbfMassWoNoisyJets_JetRelativeBalDown, &b_vbfMassWoNoisyJets_JetRelativeBalDown);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetRelativeBalUp", &vbfMassWoNoisyJets_JetRelativeBalUp, &b_vbfMassWoNoisyJets_JetRelativeBalUp);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetRelativeSampleDown", &vbfMassWoNoisyJets_JetRelativeSampleDown, &b_vbfMassWoNoisyJets_JetRelativeSampleDown);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetRelativeSampleUp", &vbfMassWoNoisyJets_JetRelativeSampleUp, &b_vbfMassWoNoisyJets_JetRelativeSampleUp);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetTotalDown", &vbfMassWoNoisyJets_JetTotalDown, &b_vbfMassWoNoisyJets_JetTotalDown);
   _tree->SetBranchAddress("vbfMassWoNoisyJets_JetTotalUp", &vbfMassWoNoisyJets_JetTotalUp, &b_vbfMassWoNoisyJets_JetTotalUp);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteFlavMapDown", &vbfMass_JetAbsoluteFlavMapDown, &b_vbfMass_JetAbsoluteFlavMapDown);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteFlavMapUp", &vbfMass_JetAbsoluteFlavMapUp, &b_vbfMass_JetAbsoluteFlavMapUp);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteMPFBiasDown", &vbfMass_JetAbsoluteMPFBiasDown, &b_vbfMass_JetAbsoluteMPFBiasDown);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteMPFBiasUp", &vbfMass_JetAbsoluteMPFBiasUp, &b_vbfMass_JetAbsoluteMPFBiasUp);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteScaleDown", &vbfMass_JetAbsoluteScaleDown, &b_vbfMass_JetAbsoluteScaleDown);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteScaleUp", &vbfMass_JetAbsoluteScaleUp, &b_vbfMass_JetAbsoluteScaleUp);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteStatDown", &vbfMass_JetAbsoluteStatDown, &b_vbfMass_JetAbsoluteStatDown);
   _tree->SetBranchAddress("vbfMass_JetAbsoluteStatUp", &vbfMass_JetAbsoluteStatUp, &b_vbfMass_JetAbsoluteStatUp);
   _tree->SetBranchAddress("vbfMass_JetClosureDown", &vbfMass_JetClosureDown, &b_vbfMass_JetClosureDown);
   _tree->SetBranchAddress("vbfMass_JetClosureUp", &vbfMass_JetClosureUp, &b_vbfMass_JetClosureUp);
   _tree->SetBranchAddress("vbfMass_JetEta0to3Down", &vbfMass_JetEta0to3Down, &b_vbfMass_JetEta0to3Down);
   _tree->SetBranchAddress("vbfMass_JetEta0to3Up", &vbfMass_JetEta0to3Up, &b_vbfMass_JetEta0to3Up);
   _tree->SetBranchAddress("vbfMass_JetEta0to5Down", &vbfMass_JetEta0to5Down, &b_vbfMass_JetEta0to5Down);
   _tree->SetBranchAddress("vbfMass_JetEta0to5Up", &vbfMass_JetEta0to5Up, &b_vbfMass_JetEta0to5Up);
   _tree->SetBranchAddress("vbfMass_JetEta3to5Down", &vbfMass_JetEta3to5Down, &b_vbfMass_JetEta3to5Down);
   _tree->SetBranchAddress("vbfMass_JetEta3to5Up", &vbfMass_JetEta3to5Up, &b_vbfMass_JetEta3to5Up);
   _tree->SetBranchAddress("vbfMass_JetFlavorQCDDown", &vbfMass_JetFlavorQCDDown, &b_vbfMass_JetFlavorQCDDown);
   _tree->SetBranchAddress("vbfMass_JetFlavorQCDUp", &vbfMass_JetFlavorQCDUp, &b_vbfMass_JetFlavorQCDUp);
   _tree->SetBranchAddress("vbfMass_JetFragmentationDown", &vbfMass_JetFragmentationDown, &b_vbfMass_JetFragmentationDown);
   _tree->SetBranchAddress("vbfMass_JetFragmentationUp", &vbfMass_JetFragmentationUp, &b_vbfMass_JetFragmentationUp);
   _tree->SetBranchAddress("vbfMass_JetPileUpDataMCDown", &vbfMass_JetPileUpDataMCDown, &b_vbfMass_JetPileUpDataMCDown);
   _tree->SetBranchAddress("vbfMass_JetPileUpDataMCUp", &vbfMass_JetPileUpDataMCUp, &b_vbfMass_JetPileUpDataMCUp);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtBBDown", &vbfMass_JetPileUpPtBBDown, &b_vbfMass_JetPileUpPtBBDown);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtBBUp", &vbfMass_JetPileUpPtBBUp, &b_vbfMass_JetPileUpPtBBUp);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtEC1Down", &vbfMass_JetPileUpPtEC1Down, &b_vbfMass_JetPileUpPtEC1Down);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtEC1Up", &vbfMass_JetPileUpPtEC1Up, &b_vbfMass_JetPileUpPtEC1Up);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtEC2Down", &vbfMass_JetPileUpPtEC2Down, &b_vbfMass_JetPileUpPtEC2Down);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtEC2Up", &vbfMass_JetPileUpPtEC2Up, &b_vbfMass_JetPileUpPtEC2Up);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtHFDown", &vbfMass_JetPileUpPtHFDown, &b_vbfMass_JetPileUpPtHFDown);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtHFUp", &vbfMass_JetPileUpPtHFUp, &b_vbfMass_JetPileUpPtHFUp);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtRefDown", &vbfMass_JetPileUpPtRefDown, &b_vbfMass_JetPileUpPtRefDown);
   _tree->SetBranchAddress("vbfMass_JetPileUpPtRefUp", &vbfMass_JetPileUpPtRefUp, &b_vbfMass_JetPileUpPtRefUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeBalDown", &vbfMass_JetRelativeBalDown, &b_vbfMass_JetRelativeBalDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeBalUp", &vbfMass_JetRelativeBalUp, &b_vbfMass_JetRelativeBalUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeFSRDown", &vbfMass_JetRelativeFSRDown, &b_vbfMass_JetRelativeFSRDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeFSRUp", &vbfMass_JetRelativeFSRUp, &b_vbfMass_JetRelativeFSRUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeJEREC1Down", &vbfMass_JetRelativeJEREC1Down, &b_vbfMass_JetRelativeJEREC1Down);
   _tree->SetBranchAddress("vbfMass_JetRelativeJEREC1Up", &vbfMass_JetRelativeJEREC1Up, &b_vbfMass_JetRelativeJEREC1Up);
   _tree->SetBranchAddress("vbfMass_JetRelativeJEREC2Down", &vbfMass_JetRelativeJEREC2Down, &b_vbfMass_JetRelativeJEREC2Down);
   _tree->SetBranchAddress("vbfMass_JetRelativeJEREC2Up", &vbfMass_JetRelativeJEREC2Up, &b_vbfMass_JetRelativeJEREC2Up);
   _tree->SetBranchAddress("vbfMass_JetRelativeJERHFDown", &vbfMass_JetRelativeJERHFDown, &b_vbfMass_JetRelativeJERHFDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeJERHFUp", &vbfMass_JetRelativeJERHFUp, &b_vbfMass_JetRelativeJERHFUp);
   _tree->SetBranchAddress("vbfMass_JetRelativePtBBDown", &vbfMass_JetRelativePtBBDown, &b_vbfMass_JetRelativePtBBDown);
   _tree->SetBranchAddress("vbfMass_JetRelativePtBBUp", &vbfMass_JetRelativePtBBUp, &b_vbfMass_JetRelativePtBBUp);
   _tree->SetBranchAddress("vbfMass_JetRelativePtEC1Down", &vbfMass_JetRelativePtEC1Down, &b_vbfMass_JetRelativePtEC1Down);
   _tree->SetBranchAddress("vbfMass_JetRelativePtEC1Up", &vbfMass_JetRelativePtEC1Up, &b_vbfMass_JetRelativePtEC1Up);
   _tree->SetBranchAddress("vbfMass_JetRelativePtEC2Down", &vbfMass_JetRelativePtEC2Down, &b_vbfMass_JetRelativePtEC2Down);
   _tree->SetBranchAddress("vbfMass_JetRelativePtEC2Up", &vbfMass_JetRelativePtEC2Up, &b_vbfMass_JetRelativePtEC2Up);
   _tree->SetBranchAddress("vbfMass_JetRelativePtHFDown", &vbfMass_JetRelativePtHFDown, &b_vbfMass_JetRelativePtHFDown);
   _tree->SetBranchAddress("vbfMass_JetRelativePtHFUp", &vbfMass_JetRelativePtHFUp, &b_vbfMass_JetRelativePtHFUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeSampleDown", &vbfMass_JetRelativeSampleDown, &b_vbfMass_JetRelativeSampleDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeSampleUp", &vbfMass_JetRelativeSampleUp, &b_vbfMass_JetRelativeSampleUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatECDown", &vbfMass_JetRelativeStatECDown, &b_vbfMass_JetRelativeStatECDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatECUp", &vbfMass_JetRelativeStatECUp, &b_vbfMass_JetRelativeStatECUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatFSRDown", &vbfMass_JetRelativeStatFSRDown, &b_vbfMass_JetRelativeStatFSRDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatFSRUp", &vbfMass_JetRelativeStatFSRUp, &b_vbfMass_JetRelativeStatFSRUp);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatHFDown", &vbfMass_JetRelativeStatHFDown, &b_vbfMass_JetRelativeStatHFDown);
   _tree->SetBranchAddress("vbfMass_JetRelativeStatHFUp", &vbfMass_JetRelativeStatHFUp, &b_vbfMass_JetRelativeStatHFUp);
   _tree->SetBranchAddress("vbfMass_JetSinglePionECALDown", &vbfMass_JetSinglePionECALDown, &b_vbfMass_JetSinglePionECALDown);
   _tree->SetBranchAddress("vbfMass_JetSinglePionECALUp", &vbfMass_JetSinglePionECALUp, &b_vbfMass_JetSinglePionECALUp);
   _tree->SetBranchAddress("vbfMass_JetSinglePionHCALDown", &vbfMass_JetSinglePionHCALDown, &b_vbfMass_JetSinglePionHCALDown);
   _tree->SetBranchAddress("vbfMass_JetSinglePionHCALUp", &vbfMass_JetSinglePionHCALUp, &b_vbfMass_JetSinglePionHCALUp);
   _tree->SetBranchAddress("vbfMass_JetTimePtEtaDown", &vbfMass_JetTimePtEtaDown, &b_vbfMass_JetTimePtEtaDown);
   _tree->SetBranchAddress("vbfMass_JetTimePtEtaUp", &vbfMass_JetTimePtEtaUp, &b_vbfMass_JetTimePtEtaUp);
   _tree->SetBranchAddress("vbfMass_JetTotalDown", &vbfMass_JetTotalDown, &b_vbfMass_JetTotalDown);
   _tree->SetBranchAddress("vbfMass_JetTotalUp", &vbfMass_JetTotalUp, &b_vbfMass_JetTotalUp);
   _tree->SetBranchAddress("vbfNJets20", &vbfNJets20, &b_vbfNJets20);
   _tree->SetBranchAddress("vbfNJets30", &vbfNJets30, &b_vbfNJets30);
   _tree->SetBranchAddress("vbfj1eta", &vbfj1eta, &b_vbfj1eta);
   _tree->SetBranchAddress("vbfj1pt", &vbfj1pt, &b_vbfj1pt);
   _tree->SetBranchAddress("vbfj2eta", &vbfj2eta, &b_vbfj2eta);
   _tree->SetBranchAddress("vbfj2pt", &vbfj2pt, &b_vbfj2pt);
   _tree->SetBranchAddress("vispX", &vispX, &b_vispX);
   _tree->SetBranchAddress("vispY", &vispY, &b_vispY);
   _tree->SetBranchAddress("idx", &idx, &b_idx);
}

Int_t HTauTauTree_mt::GetEntry(int entry)
{
    return _tree->GetEntry(entry);
}

Long64_t HTauTauTree_mt::GetEntries()
{
    return _tree->GetEntries();
}

TTree* HTauTauTree_mt::GetTree()
{
    return _tree;
}

#endif

