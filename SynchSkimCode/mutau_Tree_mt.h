#ifndef THTH_TREE_H
#define	THTH_TREE_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include "TTree.h"
#include "TFile.h"
#include "TSystem.h"
#include "HTauTauTree_mt.h"
#include "RecoilCorrector.h"

using namespace std;
float L1iso, L1pt;
int njets, njetsWoNoisyJets, nbtag, nbtagWoNoisyJets;
float mjj, mjjWoNoisyJets;
float mjjWoNoisyJets_JetRelativeSampleUp, mjjWoNoisyJets_JetRelativeSampleDown, mjjWoNoisyJets_JetRelativeBalUp, mjjWoNoisyJets_JetRelativeBalDown, mjjWoNoisyJets_JetEta0to3Up, mjjWoNoisyJets_JetEta0to3Down, mjjWoNoisyJets_JetEta0to5Up, mjjWoNoisyJets_JetEta0to5Down, mjjWoNoisyJets_JetEta3to5Up, mjjWoNoisyJets_JetEta3to5Down;
int njetsWoNoisyJets_JetRelativeSampleUp, njetsWoNoisyJets_JetRelativeSampleDown, njetsWoNoisyJets_JetRelativeBalUp, njetsWoNoisyJets_JetRelativeBalDown, njetsWoNoisyJets_JetEta0to3Up, njetsWoNoisyJets_JetEta0to3Down, njetsWoNoisyJets_JetEta0to5Up, njetsWoNoisyJets_JetEta0to5Down, njetsWoNoisyJets_JetEta3to5Up, njetsWoNoisyJets_JetEta3to5Down;
float passMu24, passMu27, passMu20Tau27;
float matchMu24_1, matchMu27_1, matchMu20Tau27_1, matchMu20Tau27_2;
float filterMu24_1, filterMu27_1, filterMu20Tau27_1, filterMu20Tau27_2;
float byVVLooseIsolationMVArun2v2DBoldDMwLT_2, byVLooseIsolationMVArun2v2DBoldDMwLT_2, byLooseIsolationMVArun2v2DBoldDMwLT_2, byMediumIsolationMVArun2v2DBoldDMwLT_2, byTightIsolationMVArun2v2DBoldDMwLT_2, byVTightIsolationMVArun2v2DBoldDMwLT_2, byVVTightIsolationMVArun2v2DBoldDMwLT_2, byIsolationMVArun2v2DBoldDMwLTraw_2, byIsolationMVA3oldDMwLTraw_2;
float Rivet_VEta,Rivet_VPt,Rivet_errorCode,Rivet_higgsEta,Rivet_higgsPt,Rivet_nJets25,Rivet_nJets30,Rivet_p4decay_VEta,Rivet_p4decay_VPt,Rivet_prodMode,Rivet_stage0_cat,Rivet_stage1_cat_pTjet25GeV,Rivet_stage1_cat_pTjet30GeV;
unsigned int run, lumi, evt, NUP = -10;
int gen_match_1, gen_match_2=0;
float npu, rho, npv=-1, puweight, weight, numGenJets,jetPt_2;
float e_1, px_1, py_1, pz_1, pt_1, phi_1, eta_1, m_1, q_1, d0_1, dZ_1, mt_1, iso_1, l1_decayMode, isoDB_1;
float e_2, px_2, py_2, pz_2, pt_2, phi_2, eta_2, m_2, q_2, d0_2, dZ_2, mt_2, iso_2, l2_decayMode;
float je_1, jmass_1, jpt_1, jpx_1, jpy_1, jpz_1, jeta_1, jphi_1, jrawf_1, jmva_1, jpfid_1, jpuid_1;
float je_2, jmass_2, jpx_2, jpy_2, jpz_2, jpt_2, jeta_2, jphi_2, jrawf_2, jmva_2, jpfid_2, jpuid_2;
float bpt_1, beta_1, bphi_1, brawf_1, bmva_1, bpfid_1, bpuid_1, bflavor_1;
float bpt_2, beta_2, bphi_2, brawf_2, bmva_2, bpfid_2, bpuid_2, bflavor_2;
float met, metphi, metcov00,metcov01,metcov10,metcov11;
float met_UESDown, met_UESUp, metphi_UESDown, metphi_UESUp;
float top_reweighting, gen_Higgs_pt, gen_Higgs_mass=1.0;
float extraelec_veto, extramuon_veto, dilepton_veto=false;
float met_px, met_py,genpX,genpY,vispX,vispY,metSig,genpT,genM;
float pt_top1, pt_top2, genweight;
float decayModeFinding_2, againstElectronTightMVA6_2, againstElectronVTightMVA6_2, againstElectronVLooseMVA6_2, againstElectronMediumMVA6_2, againstElectronLooseMVA6_2, againstMuonLoose3_2, againstMuonTight3_2;
float flag_BadChargedCandidate, flag_BadPFMuon, flag_EcalDeadCellTriggerPrimitive, flag_HBHENoise, flag_HBHENoiseIso, flag_badCloneMuon, flag_badGlobalMuon, flag_eeBadSc, flag_globalTightHalo2016, flag_goodVertices, flag_globalSuperTightHalo2016, flag_badMuons, flag_duplicateMuons, flag_ecalBadCalib;

RecoilCorrector recoilPFMetCorrector("SMH_et_2017/HTT-utilities/RecoilCorrections/data/Type1_PFMET_2017.root");

void fillTree(TTree *Run_Tree, HTauTauTree_mt *tree, int entry_tree, int recoil, bool ismc){
    tree->GetEntry(entry_tree);
    run = tree->run;
    lumi = tree->lumi;
    evt =tree->evt;
    genweight = tree->GenWeight;

    passMu24=tree->IsoMu24Pass;
    passMu27=tree->IsoMu27Pass;
    passMu20Tau27=tree->Mu20Tau27Pass;

    matchMu24_1=tree->mMatchesIsoMu24Path;
    matchMu27_1=tree->mMatchesIsoMu27Path;
    matchMu20Tau27_1=tree->mMatchesIsoMu20Tau27Path;
    matchMu20Tau27_2=tree->tMatchesIsoMu20Tau27Path;
    filterMu24_1=tree->mMatchesIsoMu24Filter;
    filterMu27_1=tree->mMatchesIsoMu27Filter;
    filterMu20Tau27_1=tree->mMatchesIsoMu20Tau27Filter;
    filterMu20Tau27_2=tree->tMatchesIsoMu20Tau27Filter;

    Rivet_VEta=tree->Rivet_VEta;
    Rivet_VPt=tree->Rivet_VPt;
    Rivet_errorCode=tree->Rivet_errorCode;
    Rivet_higgsEta=tree->Rivet_higgsEta;
    Rivet_higgsPt=tree->Rivet_higgsPt;
    Rivet_nJets25=tree->Rivet_nJets25;
    Rivet_nJets30=tree->Rivet_nJets30;
    Rivet_p4decay_VEta=tree->Rivet_p4decay_VEta;
    Rivet_p4decay_VPt=tree->Rivet_p4decay_VPt;
    Rivet_prodMode=tree->Rivet_prodMode;
    Rivet_stage0_cat=tree->Rivet_stage0_cat;
    Rivet_stage1_cat_pTjet25GeV=tree->Rivet_stage1_cat_pTjet25GeV;
    Rivet_stage1_cat_pTjet30GeV=tree->Rivet_stage1_cat_pTjet30GeV;

    genpX=tree->genpX;
    genpY=tree->genpY;
    vispX=tree->vispX;
    vispY=tree->vispY;
    genpT=tree->genpT;
    genM=tree->genM;

    flag_BadChargedCandidate = tree->Flag_BadChargedCandidateFilter;
    flag_BadPFMuon = tree->Flag_BadPFMuonFilter;
    flag_EcalDeadCellTriggerPrimitive = tree->Flag_EcalDeadCellTriggerPrimitiveFilter;
    flag_HBHENoise = tree->Flag_HBHENoiseFilter;
    flag_HBHENoiseIso = tree->Flag_HBHENoiseIsoFilter;
    flag_badMuons = tree->Flag_badMuons;
    flag_duplicateMuons = tree->Flag_duplicateMuons;
    flag_ecalBadCalib = tree->Flag_ecalBadCalibFilter;
    flag_eeBadSc = tree->Flag_eeBadScFilter;
    flag_globalSuperTightHalo2016 = tree->Flag_globalSuperTightHalo2016Filter;
    flag_globalTightHalo2016 = tree->Flag_globalTightHalo2016Filter;
    flag_goodVertices = tree->Flag_goodVertices;

    metSig=tree->metSig;
    metcov00=tree->metcov00_DESYlike;
    metcov01=tree->metcov01_DESYlike;
    metcov10=tree->metcov10_DESYlike;
    metcov11=tree->metcov11_DESYlike;

    numGenJets=tree->numGenJets;
    jetPt_2=tree->tJetPt;

    gen_Higgs_pt=tree->genpT;
    gen_Higgs_mass=tree->genM;

    pt_top1=tree->topQuarkPt1;
    pt_top2=tree->topQuarkPt2;

    weight=tree->GenWeight;

    njets = tree->jetVeto30;
    nbtag = tree->bjetDeepCSVVeto20Medium;
    njetsWoNoisyJets = tree->jetVeto30WoNoisyJets;
    njetsWoNoisyJets_JetRelativeSampleUp = tree->jetVeto30WoNoisyJets_JetRelativeSampleUp;
    njetsWoNoisyJets_JetRelativeSampleDown = tree->jetVeto30WoNoisyJets_JetRelativeSampleDown;
    njetsWoNoisyJets_JetEta3to5Up = tree->jetVeto30WoNoisyJets_JetEta3to5Up;
    njetsWoNoisyJets_JetEta3to5Down = tree->jetVeto30WoNoisyJets_JetEta3to5Down;
    njetsWoNoisyJets_JetEta0to5Up = tree->jetVeto30WoNoisyJets_JetEta0to5Up;
    njetsWoNoisyJets_JetEta0to5Down = tree->jetVeto30WoNoisyJets_JetEta0to5Down;
    njetsWoNoisyJets_JetEta0to3Up = tree->jetVeto30WoNoisyJets_JetEta0to3Up;
    njetsWoNoisyJets_JetEta0to3Down = tree->jetVeto30WoNoisyJets_JetEta0to3Down;
    njetsWoNoisyJets_JetRelativeBalUp = tree->jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets;
    njetsWoNoisyJets_JetRelativeBalDown = tree->jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets;
    nbtagWoNoisyJets = tree->bjetDeepCSVVeto20MediumWoNoisyJets;

    gen_match_1=tree->mZTTGenMatching;
    gen_match_2=tree->tZTTGenMatching;

    TLorentzVector tau1;
    TLorentzVector tau2;
    tau1.SetPtEtaPhiM(tree->mPt,tree->mEta,tree->mPhi,tree->mMass);
    tau2.SetPtEtaPhiM(tree->tPt,tree->tEta,tree->tPhi,tree->tMass);

    TLorentzVector mymet;
    mymet.SetPtEtaPhiM(tree->type1_pfMetEt,0,tree->type1_pfMetPhi,0);
    float pfmetcorr_ex=mymet.Px();
    float pfmetcorr_ey=mymet.Py();

    TLorentzVector mymet_UESUp;
    mymet_UESUp.SetPtEtaPhiM(tree->type1_pfMet_shiftedPt_UnclusteredEnUp,0,tree->type1_pfMet_shiftedPhi_UnclusteredEnUp,0);
    float pfmetcorr_ex_UESUp=mymet_UESUp.Px();
    float pfmetcorr_ey_UESUp=mymet_UESUp.Py();

    TLorentzVector mymet_UESDown;
    mymet_UESDown.SetPtEtaPhiM(tree->type1_pfMet_shiftedPt_UnclusteredEnDown,0,tree->type1_pfMet_shiftedPhi_UnclusteredEnDown,0);
    float pfmetcorr_ex_UESDown=mymet_UESDown.Px();
    float pfmetcorr_ey_UESDown=mymet_UESDown.Py();

    if (recoil==1){
         recoilPFMetCorrector.CorrectByMeanResolution(
         mymet.Px(), // uncorrected type I pf met px (float)
         mymet.Py(), // uncorrected type I pf met py (float)
         tree->genpX, // generator Z/W/Higgs px (float)
         tree->genpY, // generator Z/W/Higgs py (float)
         tree->vispX, // generator visible Z/W/Higgs px (float)
         tree->vispY, // generator visible Z/W/Higgs py (float)
         tree->jetVeto30WoNoisyJets+1,  // number of jets (hadronic jet multiplicity) (int)
         pfmetcorr_ex, // corrected type I pf met px (float)
         pfmetcorr_ey  // corrected type I pf met py (float)
        );
    }
    if (recoil==2){
        recoilPFMetCorrector.CorrectByMeanResolution(
        mymet.Px(), // uncorrected type I pf met px (float)
        mymet.Py(), // uncorrected type I pf met py (float)
        tree->genpX, // generator Z/W/Higgs px (float)
        tree->genpY, // generator Z/W/Higgs py (float)
        tree->vispX, // generator visible Z/W/Higgs px (float)
        tree->vispY, // generator visible Z/W/Higgs py (float)
        tree->jetVeto30WoNoisyJets,  // number of jets (hadronic jet multiplicity) (int)
        pfmetcorr_ex, // corrected type I pf met px (float)
        pfmetcorr_ey  // corrected type I pf met py (float)
        );
    }

    if (recoil==1){
         recoilPFMetCorrector.CorrectByMeanResolution(
         mymet_UESDown.Px(), // uncorrected type I pf met px (float)
         mymet_UESDown.Py(), // uncorrected type I pf met py (float)
         tree->genpX, // generator Z/W/Higgs px (float)
         tree->genpY, // generator Z/W/Higgs py (float)
         tree->vispX, // generator visible Z/W/Higgs px (float)
         tree->vispY, // generator visible Z/W/Higgs py (float)
         tree->jetVeto30WoNoisyJets+1,  // number of jets (hadronic jet multiplicity) (int)
         pfmetcorr_ex_UESDown, // corrected type I pf met px (float)
         pfmetcorr_ey_UESDown  // corrected type I pf met py (float)
        );
    }
    if (recoil==2){
        recoilPFMetCorrector.CorrectByMeanResolution(
        mymet_UESDown.Px(), // uncorrected type I pf met px (float)
        mymet_UESDown.Py(), // uncorrected type I pf met py (float)
        tree->genpX, // generator Z/W/Higgs px (float)
        tree->genpY, // generator Z/W/Higgs py (float)
        tree->vispX, // generator visible Z/W/Higgs px (float)
        tree->vispY, // generator visible Z/W/Higgs py (float)
        tree->jetVeto30WoNoisyJets,  // number of jets (hadronic jet multiplicity) (int)
        pfmetcorr_ex_UESDown, // corrected type I pf met px (float)
        pfmetcorr_ey_UESDown  // corrected type I pf met py (float)
        );
    }

    if (recoil==1){
         recoilPFMetCorrector.CorrectByMeanResolution(
         mymet_UESUp.Px(), // uncorrected type I pf met px (float)
         mymet_UESUp.Py(), // uncorrected type I pf met py (float)
         tree->genpX, // generator Z/W/Higgs px (float)
         tree->genpY, // generator Z/W/Higgs py (float)
         tree->vispX, // generator visible Z/W/Higgs px (float)
         tree->vispY, // generator visible Z/W/Higgs py (float)
         tree->jetVeto30WoNoisyJets+1,  // number of jets (hadronic jet multiplicity) (int)
         pfmetcorr_ex_UESUp, // corrected type I pf met px (float)
         pfmetcorr_ey_UESUp  // corrected type I pf met py (float)
        );
    }
    if (recoil==2){
        recoilPFMetCorrector.CorrectByMeanResolution(
        mymet_UESUp.Px(), // uncorrected type I pf met px (float)
        mymet_UESUp.Py(), // uncorrected type I pf met py (float)
        tree->genpX, // generator Z/W/Higgs px (float)
        tree->genpY, // generator Z/W/Higgs py (float)
        tree->vispX, // generator visible Z/W/Higgs px (float)
        tree->vispY, // generator visible Z/W/Higgs py (float)
        tree->jetVeto30WoNoisyJets,  // number of jets (hadronic jet multiplicity) (int)
        pfmetcorr_ex_UESUp, // corrected type I pf met px (float)
        pfmetcorr_ey_UESUp  // corrected type I pf met py (float)
        );
    }

    mymet.SetPxPyPzE(pfmetcorr_ex,pfmetcorr_ey,0,sqrt(pfmetcorr_ex*pfmetcorr_ex+pfmetcorr_ey*pfmetcorr_ey));
    mymet_UESUp.SetPxPyPzE(pfmetcorr_ex_UESUp,pfmetcorr_ey_UESUp,0,sqrt(pfmetcorr_ex_UESUp*pfmetcorr_ex_UESUp+pfmetcorr_ey_UESUp*pfmetcorr_ey_UESUp));
    mymet_UESDown.SetPxPyPzE(pfmetcorr_ex_UESDown,pfmetcorr_ey_UESDown,0,sqrt(pfmetcorr_ex_UESDown*pfmetcorr_ex_UESDown+pfmetcorr_ey_UESDown*pfmetcorr_ey_UESDown));

    if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==0){
        mymet=mymet+tau2-1.007*tau2;
        mymet_UESDown=mymet_UESDown+tau2-1.007*tau2;
        mymet_UESUp=mymet_UESUp+tau2-1.007*tau2;
    }
    else if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==1){
        mymet=mymet+tau2-0.998*tau2;
        mymet_UESDown=mymet_UESDown+tau2-0.998*tau2;
        mymet_UESUp=mymet_UESUp+tau2-0.998*tau2;
    }
    else if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==10){
        mymet=mymet+tau2-1.001*tau2;
        mymet_UESDown=mymet_UESDown+tau2-1.001*tau2;
        mymet_UESUp=mymet_UESUp+tau2-1.001*tau2;
    }

    met=mymet.Pt();
    metphi=mymet.Phi();
    met_px=mymet.Px();
    met_py=mymet.Py();
    met_UESUp=mymet_UESUp.Pt();
    metphi_UESUp=mymet_UESUp.Phi();
    met_UESDown=mymet_UESDown.Pt();
    metphi_UESDown=mymet_UESDown.Phi();

    if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==0) tau2=tau2*1.007;
    else if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==1) tau2=tau2*0.998;
    else if (ismc && tree->tZTTGenMatching==5 && tree->tDecayMode==10) tau2=tau2*1.001;

    l2_decayMode=tree->tDecayMode;

    m_1 = tau1.M();
    e_1 = tau1.E();
    pt_1 = tau1.Pt();
    phi_1 = tau1.Phi();
    eta_1 = tau1.Eta();
    dZ_1 = tree->mPVDZ;
    d0_1 = tree->mPVDXY;
    iso_1 = tree->mRelPFIsoDBDefault;
    q_1 = tree->mCharge;

    m_2 = tau2.M();
    if (tree->tDecayMode==0) m_2=tree->tMass;
    e_2 = tau2.E();
    pt_2 = tau2.Pt();
    phi_2 = tau2.Phi();
    eta_2 = tau2.Eta();
    dZ_2 = tree->tPVDZ;
    d0_2=tree->tPVDXY;
    iso_2=tree->tByIsolationMVArun2v1DBoldDMwLTraw;
    q_2 = tree->tCharge;

    againstMuonTight3_2 = tree->tAgainstMuonTight3;
    againstMuonLoose3_2 = tree->tAgainstMuonLoose3;
    againstElectronVLooseMVA6_2 = tree->tAgainstElectronVLooseMVA6;
    againstElectronLooseMVA6_2 = tree->tAgainstElectronLooseMVA6;
    againstElectronMediumMVA6_2 = tree->tAgainstElectronMediumMVA6;
    againstElectronTightMVA6_2 = tree->tAgainstElectronTightMVA6;
    againstElectronVTightMVA6_2 = tree->tAgainstElectronVTightMVA6;
    byIsolationMVA3oldDMwLTraw_2=tree->tRerunMVArun2v2DBoldDMwLTraw;
    byVVLooseIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTVVLoose;
    byVLooseIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTVLoose;
    byLooseIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTLoose;
    byMediumIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTMedium;
    byTightIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTTight;
    byVTightIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTVTight;
    byVVTightIsolationMVArun2v2DBoldDMwLT_2 = tree->tRerunMVArun2v2DBoldDMwLTVVTight;

    decayModeFinding_2=tree->tDecayModeFinding;

    jpt_1=tree->j1ptWoNoisyJets;
    jpt_2=tree->j2ptWoNoisyJets;
    jeta_1=tree->j1etaWoNoisyJets;
    jeta_2=tree->j2etaWoNoisyJets;
    jphi_1=tree->j1phiWoNoisyJets;
    jphi_2=tree->j2phiWoNoisyJets;
    bpt_1=tree->jb1ptWoNoisyJets;
    bpt_2=tree->jb2ptWoNoisyJets;
    beta_1=tree->jb1etaWoNoisyJets;
    beta_2=tree->jb2etaWoNoisyJets;
    bphi_1=tree->jb1phiWoNoisyJets;
    bphi_2=tree->jb2phiWoNoisyJets;
    bflavor_1=tree->jb1hadronflavor;
    bflavor_2=tree->jb2hadronflavor;
    mjj=tree->vbfMass;
    mjjWoNoisyJets=tree->vbfMassWoNoisyJets;

  mjjWoNoisyJets_JetRelativeBalUp=tree->vbfMassWoNoisyJets_JetRelativeBalUp;
  mjjWoNoisyJets_JetRelativeBalDown=tree->vbfMassWoNoisyJets_JetRelativeBalDown;
  mjjWoNoisyJets_JetRelativeSampleUp=tree->vbfMassWoNoisyJets_JetRelativeSampleUp;
  mjjWoNoisyJets_JetRelativeSampleDown=tree->vbfMassWoNoisyJets_JetRelativeSampleDown;
  mjjWoNoisyJets_JetEta0to3Up=tree->vbfMassWoNoisyJets_JetEta0to3Up;
  mjjWoNoisyJets_JetEta0to3Down=tree->vbfMassWoNoisyJets_JetEta0to3Down;
  mjjWoNoisyJets_JetEta3to5Up=tree->vbfMassWoNoisyJets_JetEta3to5Up;
  mjjWoNoisyJets_JetEta3to5Down=tree->vbfMassWoNoisyJets_JetEta3to5Down;
  mjjWoNoisyJets_JetEta0to5Up=tree->vbfMassWoNoisyJets_JetEta0to5Up;
  mjjWoNoisyJets_JetEta0to5Down=tree->vbfMassWoNoisyJets_JetEta0to5Down;

  NUP=tree->NUP;
  npu=tree->nTruePU;
  npv=tree->nvtx;

  L1iso=tree->tL1IsoTauMatch;
  L1pt=tree->tL1IsoTauPt;

  Run_Tree->Fill();
}

#endif


