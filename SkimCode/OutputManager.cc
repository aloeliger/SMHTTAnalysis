#include "TROOT.h"
#include "InputManager.cc"

struct OutputDictionary
{  
  
  Float  Rivet_higgsPt;
  Float  Rivet_nJets30;
  Float  Rivet_stage0_cat;
  Float  Rivet_stage1_cat_pTjet30GeV;
  Float  passMu24;
  Float  passMu27;
  Float  passMu20Tau27;
  Float  matchMu24_1;
  Float  matchMu27_1;
  Float  matchMu20Tau27_1;
  Float  matchMu20Tau27_2;
  Float  filterMu24_1;
  Float  filterMu27_1;
  Float  filterMu20Tau27_1;
  Float  filterMu20Tau27_2;
  Float  run;
  Float  lumi;
  Float  evt;
  Float  npv;
  Float  pt_1;
  Float  phi_1;
  Float  eta_1;
  Float  iso_1;
  Float  m_1;
  Float  q_1;
  Float  nbtag;
  Float  nbtagWoNoisyJets;
  Float  q_2;
  Float  pt_2;
  Float  eta_2;
  Float  m_2;
  Float  phi_2;  
  Float  m_sv;
  Float  m_sv_DOWN;
  Float  m_sv_UP;
  Float  m_sv_UESUp;
  Float  m_sv_UESDown;  
  Float  met;
  Float  metphi;
  Float  met_UESUp;
  Float  metphi_UESDown;
  Float  njets;
  Float  njetsWoNoisyJets;
  Float  njetsWoNoisyJets_JetEta0to3Down;
  Float  njetsWoNoisyJets_JetEta0to3Up;
  Float  njetsWoNoisyJets_JetRelativeSampleDown;
  Float  njetsWoNoisyJets_JetRelativeSampleUp;
  Float  njetsWoNoisyJets_JetRelativeBalDown;
  Float  njetsWoNoisyJets_JetRelativeBalUp;
  Float  njetsWoNoisyJets_JetEta0to5Down;
  Float  njetsWoNoisyJets_JetEta0to5Up;
  Float  njetsWoNoisyJets_JetEta3to5Down;
  Float  njetsWoNoisyJets_JetEta3to5Up;
  Float  jpt_1;
  Float  jeta_1;
  Float  jphi_1;
  Float  jpt_2;
  Float  jeta_2;
  Float  jphi_2;
  Float  bpt_1;
  Float  beta_1;
  Float  bphi_1;
  Float  bpt_2;
  Float  beta_2;
  Float  bphi_2;
  Float  bflavor_1;
  Float  bflavor_2;
  Float  mjj;
  Float  mjjWoNoisyJets_JetEta0to3Down;
  Float  mjjWoNoisyJets_JetEta0to3Up;
  Float  mjjWoNoisyJets_JetEta3to5Down;
  Float  mjjWoNoisyJets_JetEta3to5Up;
  Float  mjjWoNoisyJets_JetEta0to5Down;
  Float  mjjWoNoisyJets_JetEta0to5Up;
  Float  mjjWoNoisyJets_JetRelativeBalDown;
  Float  mjjWoNoisyJets_JetRelativeBalUp;
  Float  mjjWoNoisyJets_JetRelativeSampleDown;
  Float  mjjWoNoisyJets_JetRelativeSampleUp;
  Float  mjjWoNoisyJets;
  Float  genweight;
  Float  byVLooseIsolationMVArun2v2DBoldDMwLT_2;
  Float  byLooseIsolationMVArun2v2DBoldDMwLT_2;
  Float  byMediumIsolationMVArun2v2DBoldDMwLT_2;
  Float  byTightIsolationMVArun2v2DBoldDMwLT_2;
  Float  byVTightIsolationMVArun2v2DBoldDMwLT_2;
  Float  byIsolationMVA3oldDMwLTraw_2;
  Float  l2_decayMode;
  Float  againstElectronTightMVA6_2;
  Float  againstMuonLoose3_2;
  Float  gen_match_1;
  Float  gen_match_2;
  Float  npu;
  Float  genpT;
  Float  genM;
  Float  pt_top1;
  Float  pt_top2;
  Float  numGenJets;
  Float  flag_BadChargedCandidate;
  Float  flag_BadPFMuon;
  Float  flag_EcalDeadCellTriggerPrimitive;
  Float  flag_HBHENoise;
  Float  flag_HBHENoiseIso;
  Float  flag_eeBadSc;
  Float  flag_globalTightHalo2016;
  Float  flag_goodVertices;
  Float  flag_globalSuperTightHalo2016;
  Float  flag_ecalBadCalib;
  Float  flag_duplicateMuons;
  Float  flag_badMuons;
};


class OutputManager
{
 private:
  OutputDictionary* TheStagedOutputDictionary;
  OutputDictionary* TheCurrentOutputDictionary;
 public:
  OutputManager()
    {
      TheStagedOutputDictionary = new OutputDictionary;
      TheCurrentOutputDictionary = new OutputDictionary;
    }
  ~OutputManager()
    {
      delete TheStagedOutputDictionary;
      delete TheCurrentOutputDictionary;
    }
  
  void AttachTreeToVariables(TTree* TheTree)
  {
    //TheTree->Branch("run", &this->GetStagedOutputDictionary()->run, "run/I");
    TheTree->Branch("Rivet_higgsPt", &this->GetStagedOutputDictionary()->Rivet_higgsPt, "Rivet_higgsPt/F");
    TheTree->Branch("Rivet_nJets30", &this->GetStagedOutputDictionary()->Rivet_nJets30, "Rivet_nJets30/F");
    TheTree->Branch("Rivet_stage0_cat", &this->GetStagedOutputDictionary()->Rivet_stage0_cat, "Rivet_stage0_cat/F");
    TheTree->Branch("Rivet_stage1_cat_pTjet30GeV", &this->GetStagedOutputDictionary()->Rivet_stage1_cat_pTjet30GeV, "Rivet_stage1_cat_pTjet30GeV/F");
    TheTree->Branch("passMu24", &this->GetStagedOutputDictionary()->passMu24, "passMu24/F");
    TheTree->Branch("passMu27", &this->GetStagedOutputDictionary()->passMu27, "passMu27/F");
    TheTree->Branch("passMu20Tau27", &this->GetStagedOutputDictionary()->passMu20Tau27, "passMu20Tau27/F");
    TheTree->Branch("matchMu24_1", &this->GetStagedOutputDictionary()->matchMu24_1, "matchMu24_1/F");
    TheTree->Branch("matchMu27_1", &this->GetStagedOutputDictionary()->matchMu27_1, "matchMu27_1/F");
    TheTree->Branch("matchMu20Tau27_1", &this->GetStagedOutputDictionary()->matchMu20Tau27_1, "matchMu20Tau27_1/F");
    TheTree->Branch("matchMu20Tau27_2", &this->GetStagedOutputDictionary()->matchMu20Tau27_2, "matchMu20Tau27_2/F");
    TheTree->Branch("filterMu24_1", &this->GetStagedOutputDictionary()->filterMu24_1, "filterMu24_1/F");
    TheTree->Branch("filterMu27_1", &this->GetStagedOutputDictionary()->filterMu27_1, "filterMu27_1/F");
    TheTree->Branch("filterMu20Tau27_1", &this->GetStagedOutputDictionary()->filterMu20Tau27_1, "filterMu20Tau27_1/F");
    TheTree->Branch("filterMu20Tau27_2", &this->GetStagedOutputDictionary()->filterMu20Tau27_2, "filterMu20Tau27_2/F");
    TheTree->Branch("run", &this->GetStagedOutputDictionary()->run, "run/F");
    TheTree->Branch("lumi", &this->GetStagedOutputDictionary()->lumi, "lumi/F");
    TheTree->Branch("evt", &this->GetStagedOutputDictionary()->evt, "evt/F");
    TheTree->Branch("npv", &this->GetStagedOutputDictionary()->npv, "npv/F");
    TheTree->Branch("pt_1", &this->GetStagedOutputDictionary()->pt_1, "pt_1/F");
    TheTree->Branch("phi_1", &this->GetStagedOutputDictionary()->phi_1, "phi_1/F");
    TheTree->Branch("eta_1", &this->GetStagedOutputDictionary()->eta_1, "eta_1/F");
    TheTree->Branch("iso_1", &this->GetStagedOutputDictionary()->iso_1, "iso_1/F");
    TheTree->Branch("m_1", &this->GetStagedOutputDictionary()->m_1, "m_1/F");
    TheTree->Branch("q_1", &this->GetStagedOutputDictionary()->q_1, "q_1/F");
    TheTree->Branch("nbtag", &this->GetStagedOutputDictionary()->nbtag, "nbtag/F");
    TheTree->Branch("nbtagWoNoisyJets", &this->GetStagedOutputDictionary()->nbtagWoNoisyJets, "nbtagWoNoisyJets/F");
    TheTree->Branch("q_2", &this->GetStagedOutputDictionary()->q_2, "q_2/F");
    TheTree->Branch("pt_2", &this->GetStagedOutputDictionary()->pt_2, "pt_2/F");
    TheTree->Branch("eta_2", &this->GetStagedOutputDictionary()->eta_2, "eta_2/F");
    TheTree->Branch("m_2", &this->GetStagedOutputDictionary()->m_2, "m_2/F");
    TheTree->Branch("phi_2", &this->GetStagedOutputDictionary()->phi_2, "phi_2/F");    
    TheTree->Branch("m_sv", &this->GetStagedOutputDictionary()->m_sv, "m_sv/F");
    TheTree->Branch("m_sv_DOWN", &this->GetStagedOutputDictionary()->m_sv_DOWN, "m_sv_DOWN/F");
    TheTree->Branch("m_sv_UP", &this->GetStagedOutputDictionary()->m_sv_UP, "m_sv_UP/F");
    TheTree->Branch("m_sv_UESUp", &this->GetStagedOutputDictionary()->m_sv_UESUp, "m_sv_UESUp/F");
    TheTree->Branch("m_sv_UESDown", &this->GetStagedOutputDictionary()->m_sv_UESDown, "m_sv_UESDown/F");    
    TheTree->Branch("met", &this->GetStagedOutputDictionary()->met, "met/F");
    TheTree->Branch("metphi", &this->GetStagedOutputDictionary()->metphi, "metphi/F");
    TheTree->Branch("met_UESUp", &this->GetStagedOutputDictionary()->met_UESUp, "met_UESUp/F");
    TheTree->Branch("metphi_UESDown", &this->GetStagedOutputDictionary()->metphi_UESDown, "metphi_UESDown/F");
    TheTree->Branch("njets", &this->GetStagedOutputDictionary()->njets, "njets/F");
    TheTree->Branch("njetsWoNoisyJets", &this->GetStagedOutputDictionary()->njetsWoNoisyJets, "njetsWoNoisyJets/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta0to3Down", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta0to3Down, "njetsWoNoisyJets_JetEta0to3Down/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta0to3Up", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta0to3Up, "njetsWoNoisyJets_JetEta0to3Up/F");
    TheTree->Branch("njetsWoNoisyJets_JetRelativeSampleDown", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetRelativeSampleDown, "njetsWoNoisyJets_JetRelativeSampleDown/F");
    TheTree->Branch("njetsWoNoisyJets_JetRelativeSampleUp", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetRelativeSampleUp, "njetsWoNoisyJets_JetRelativeSampleUp/F");
    TheTree->Branch("njetsWoNoisyJets_JetRelativeBalDown", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetRelativeBalDown, "njetsWoNoisyJets_JetRelativeBalDown/F");
    TheTree->Branch("njetsWoNoisyJets_JetRelativeBalUp", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetRelativeBalUp, "njetsWoNoisyJets_JetRelativeBalUp/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta0to5Down", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta0to5Down, "njetsWoNoisyJets_JetEta0to5Down/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta0to5Up", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta0to5Up, "njetsWoNoisyJets_JetEta0to5Up/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta3to5Down", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta3to5Down, "njetsWoNoisyJets_JetEta3to5Down/F");
    TheTree->Branch("njetsWoNoisyJets_JetEta3to5Up", &this->GetStagedOutputDictionary()->njetsWoNoisyJets_JetEta3to5Up, "njetsWoNoisyJets_JetEta3to5Up/F");
    TheTree->Branch("jpt_1", &this->GetStagedOutputDictionary()->jpt_1, "jpt_1/F");
    TheTree->Branch("jeta_1", &this->GetStagedOutputDictionary()->jeta_1, "jeta_1/F");
    TheTree->Branch("jphi_1", &this->GetStagedOutputDictionary()->jphi_1, "jphi_1/F");
    TheTree->Branch("jpt_2", &this->GetStagedOutputDictionary()->jpt_2, "jpt_2/F");
    TheTree->Branch("jeta_2", &this->GetStagedOutputDictionary()->jeta_2, "jeta_2/F");
    TheTree->Branch("jphi_2", &this->GetStagedOutputDictionary()->jphi_2, "jphi_2/F");
    TheTree->Branch("bpt_1", &this->GetStagedOutputDictionary()->bpt_1, "bpt_1/F");
    TheTree->Branch("beta_1", &this->GetStagedOutputDictionary()->beta_1, "beta_1/F");
    TheTree->Branch("bphi_1", &this->GetStagedOutputDictionary()->bphi_1, "bphi_1/F");
    TheTree->Branch("bpt_2", &this->GetStagedOutputDictionary()->bpt_2, "bpt_2/F");
    TheTree->Branch("beta_2", &this->GetStagedOutputDictionary()->beta_2, "beta_2/F");
    TheTree->Branch("bphi_2", &this->GetStagedOutputDictionary()->bphi_2, "bphi_2/F");
    TheTree->Branch("bflavor_1", &this->GetStagedOutputDictionary()->bflavor_1, "bflavor_1/F");
    TheTree->Branch("bflavor_2", &this->GetStagedOutputDictionary()->bflavor_2, "bflavor_2/F");
    TheTree->Branch("mjj", &this->GetStagedOutputDictionary()->mjj, "mjj/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta0to3Down", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta0to3Down, "mjjWoNoisyJets_JetEta0to3Down/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta0to3Up", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta0to3Up, "mjjWoNoisyJets_JetEta0to3Up/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta3to5Down", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta3to5Down, "mjjWoNoisyJets_JetEta3to5Down/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta3to5Up", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta3to5Up, "mjjWoNoisyJets_JetEta3to5Up/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta0to5Down", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta0to5Down, "mjjWoNoisyJets_JetEta0to5Down/F");
    TheTree->Branch("mjjWoNoisyJets_JetEta0to5Up", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetEta0to5Up, "mjjWoNoisyJets_JetEta0to5Up/F");
    TheTree->Branch("mjjWoNoisyJets_JetRelativeBalDown", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetRelativeBalDown, "mjjWoNoisyJets_JetRelativeBalDown/F");
    TheTree->Branch("mjjWoNoisyJets_JetRelativeBalUp", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetRelativeBalUp, "mjjWoNoisyJets_JetRelativeBalUp/F");
    TheTree->Branch("mjjWoNoisyJets_JetRelativeSampleDown", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetRelativeSampleDown, "mjjWoNoisyJets_JetRelativeSampleDown/F");
    TheTree->Branch("mjjWoNoisyJets_JetRelativeSampleUp", &this->GetStagedOutputDictionary()->mjjWoNoisyJets_JetRelativeSampleUp, "mjjWoNoisyJets_JetRelativeSampleUp/F");
    TheTree->Branch("mjjWoNoisyJets", &this->GetStagedOutputDictionary()->mjjWoNoisyJets, "mjjWoNoisyJets/F");
    TheTree->Branch("genweight", &this->GetStagedOutputDictionary()->genweight, "genweight/F");
    TheTree->Branch("byVLooseIsolationMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationMVArun2v2DBoldDMwLT_2, "byVLooseIsolationMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byLooseIsolationMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationMVArun2v2DBoldDMwLT_2, "byLooseIsolationMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byMediumIsolationMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationMVArun2v2DBoldDMwLT_2, "byMediumIsolationMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byTightIsolationMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationMVArun2v2DBoldDMwLT_2, "byTightIsolationMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byVTightIsolationMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationMVArun2v2DBoldDMwLT_2, "byVTightIsolationMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byIsolationMVA3oldDMwLTraw_2", &this->GetStagedOutputDictionary()->byIsolationMVA3oldDMwLTraw_2, "byIsolationMVA3oldDMwLTraw_2/F");
    TheTree->Branch("l2_decayMode", &this->GetStagedOutputDictionary()->l2_decayMode, "l2_decayMode/F");
    TheTree->Branch("againstElectronTightMVA6_2", &this->GetStagedOutputDictionary()->againstElectronTightMVA6_2, "againstElectronTightMVA6_2/F");
    TheTree->Branch("againstMuonLoose3_2", &this->GetStagedOutputDictionary()->againstMuonLoose3_2, "againstMuonLoose3_2/F");
    TheTree->Branch("gen_match_1", &this->GetStagedOutputDictionary()->gen_match_1, "gen_match_1/F");
    TheTree->Branch("gen_match_2", &this->GetStagedOutputDictionary()->gen_match_2, "gen_match_2/F");
    TheTree->Branch("npu", &this->GetStagedOutputDictionary()->npu, "npu/F");
    TheTree->Branch("genpT", &this->GetStagedOutputDictionary()->genpT, "genpT/F");
    TheTree->Branch("genM", &this->GetStagedOutputDictionary()->genM, "genM/F");
    TheTree->Branch("pt_top1", &this->GetStagedOutputDictionary()->pt_top1, "pt_top1/F");
    TheTree->Branch("pt_top2", &this->GetStagedOutputDictionary()->pt_top2, "pt_top2/F");
    TheTree->Branch("numGenJets", &this->GetStagedOutputDictionary()->numGenJets, "numGenJets/F");
    TheTree->Branch("flag_BadChargedCandidate", &this->GetStagedOutputDictionary()->flag_BadChargedCandidate, "flag_BadChargedCandidate/F");
    TheTree->Branch("flag_BadPFMuon", &this->GetStagedOutputDictionary()->flag_BadPFMuon, "flag_BadPFMuon/F");
    TheTree->Branch("flag_EcalDeadCellTriggerPrimitive", &this->GetStagedOutputDictionary()->flag_EcalDeadCellTriggerPrimitive, "flag_EcalDeadCellTriggerPrimitive/F");
    TheTree->Branch("flag_HBHENoise", &this->GetStagedOutputDictionary()->flag_HBHENoise, "flag_HBHENoise/F");
    TheTree->Branch("flag_HBHENoiseIso", &this->GetStagedOutputDictionary()->flag_HBHENoiseIso, "flag_HBHENoiseIso/F");
    TheTree->Branch("flag_eeBadSc", &this->GetStagedOutputDictionary()->flag_eeBadSc, "flag_eeBadSc/F");
    TheTree->Branch("flag_globalTightHalo2016", &this->GetStagedOutputDictionary()->flag_globalTightHalo2016, "flag_globalTightHalo2016/F");
    TheTree->Branch("flag_goodVertices", &this->GetStagedOutputDictionary()->flag_goodVertices, "flag_goodVertices/F");
    TheTree->Branch("flag_globalSuperTightHalo2016", &this->GetStagedOutputDictionary()->flag_globalSuperTightHalo2016, "flag_globalSuperTightHalo2016/F");
    TheTree->Branch("flag_ecalBadCalib", &this->GetStagedOutputDictionary()->flag_ecalBadCalib, "flag_ecalBadCalib/F");
    TheTree->Branch("flag_duplicateMuons", &this->GetStagedOutputDictionary()->flag_duplicateMuons, "flag_duplicateMuons/F");
    TheTree->Branch("flag_badMuons", &this->GetStagedOutputDictionary()->flag_badMuons, "flag_badMuons/F");
  }

  OutputDictionary* GetStagedOutputDictionary()
  {
    return TheStagedOutputDictionary;
  }
  OutputDictionary* GetCurrentOutputDictionary()
  {
    return TheCurrentOutputDictionary;
  }

  void TranslateInputToOutput(InputManager* TheInputManager)
  {
    //basic 4 vector stuff, should never change much
    TLorentzVector MuVector;
    MuVector.SetPtEtaPhiM(TheInputManager->GetInputDictionary()->mPt,
			  TheInputManager->GetInputDictionary()->mEta,
			  TheInputManager->GetInputDictionary()->mPhi,
			  TheInputManager->GetInputDictionary()->mMass);
    TLorentzVector TauVector;
    TauVector.SetPtEtaPhiM(TheInputManager->GetInputDictionary()->tPt,
			   TheInputManager->GetInputDictionary()->tEta,
			   TheInputManager->GetInputDictionary()->tPhi,
			   TheInputManager->GetInputDictionary()->tMass);    

    this->GetCurrentOutputDictionary()->pt_1 = MuVector.Pt();
    this->GetCurrentOutputDictionary()->phi_1 = MuVector.Phi();
    this->GetCurrentOutputDictionary()->eta_1 = MuVector.Eta();
    this->GetCurrentOutputDictionary()->m_1 = MuVector.M();
    this->GetCurrentOutputDictionary()->e_1 = MuVector.E();

    this->GetCurrentOutputDictionary()->pt_2 = TauVector.Pt();
    this->GetCurrentOutputDictionary()->phi_2 = TauVector.Phi();
    this->GetCurrentOutputDictionary()->eta_2 = TauVector.Eta();
    this->GetCurrentOutputDictionary()->m_2 = TauVector.M();
    this->GetCurrentOutputDictionary()->e_2 = TauVector.E();
    
    //met vector
    TLorentzVector MetVector;
    MetVector.SetPtEtaPhiM(TheInputManager->GetInputDictionary()->type1_pfMetEt,
			   0,
			   TheInputManager->GetInputDictionary()->type1_pfMetPhi,
			   0);
    this->GetCurrentOutputDictionary()->met = MetVector.Pt();
    this->GetCurrentOutputDictionary()->metphi = MetVector.Phi();

    //rest of the stuff.
    this->GetCurrentOutputDictionary()->Rivet_higgsPt = TheInputManager->GetInputDictionary()->Rivet_higgsPt;
    this->GetCurrentOutputDictionary()->Rivet_nJets30 = TheInputManager->GetInputDictionary()->Rivet_nJets30;
    this->GetCurrentOutputDictionary()->Rivet_stage0_cat = TheInputManager->GetInputDictionary()->Rivet_stage0_cat;
    this->GetCurrentOutputDictionary()->Rivet_stage1_cat_pTjet30GeV = TheInputManager->GetInputDictionary()->Rivet_stage1_cat_pTjet30GeV;
    this->GetCurrentOutputDictionary()->passMu24 = TheInputManager->GetInputDictionary()->IsoMu24Pass;
    this->GetCurrentOutputDictionary()->passMu27 = TheInputManager->GetInputDictionary()->IsoMu27Pass;
    this->GetCurrentOutputDictionary()->passMu20Tau27 = TheInputManager->GetInputDictionary()->Mu20Tau27Pass;
    this->GetCurrentOutputDictionary()->matchMu24_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu24Path;
    this->GetCurrentOutputDictionary()->matchMu27_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu27Path;
    this->GetCurrentOutputDictionary()->matchMu20Tau27_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu20Tau27Path;
    this->GetCurrentOutputDictionary()->matchMu20Tau27_2 = TheInputManager->GetInputDictionary()->tMatchesIsoMu20Tau27Path;
    this->GetCurrentOutputDictionary()->filterMu24_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu24Filter;
    this->GetCurrentOutputDictionary()->filterMu27_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu27Filter;
    this->GetCurrentOutputDictionary()->filterMu20Tau27_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu20Tau27Filter;
    this->GetCurrentOutputDictionary()->filterMu20Tau27_2 = TheInputManager->GetInputDictionary()->tMatchesIsoMu20Tau27Filter;
    this->GetCurrentOutputDictionary()->run = TheInputManager->GetInputDictionary()->run;
    this->GetCurrentOutputDictionary()->lumi = TheInputManager->GetInputDictionary()->lumi;
    this->GetCurrentOutputDictionary()->evt = TheInputManager->GetInputDictionary()->evt;
    this->GetCurrentOutputDictionary()->npv = TheInputManager->GetInputDictionary()->nvtx;
    this->GetCurrentOutputDictionary()->iso_1 = TheInputManager->GetInputDictionary()->mRelPFIsoDBDefault;
    this->GetCurrentOutputDictionary()->q_1 = TheInputManager->GetInputDictionary()->mCharge;
    this->GetCurrentOutputDictionary()->nbtag = TheInputManager->GetInputDictionary()->bjetDeepCSVVeto20Medium;
    this->GetCurrentOutputDictionary()->nbtagWoNoisyJets = TheInputManager->GetInputDictionary()->bjetDeepCSVVeto20MediumWoNoisyJets;
    this->GetCurrentOutputDictionary()->q_2 = TheInputManager->GetInputDictionary()->q_2;
    /*
    this->GetCurrentOutputDictionary()->m_sv = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->m_sv_DOWN = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->m_sv_UP = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->m_sv_UESUp = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->m_sv_UESDown = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->met_UESUp = TheInputManager->GetInputDictionary()->;
    this->GetCurrentOutputDictionary()->metphi_UESDown = TheInputManager->GetInputDictionary()->;
    */
    this->GetCurrentOutputDictionary()->njets = TheInputManager->GetInputDictionary()->jetVeto30;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta0to3Down = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta0to3Down;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta0to3Up = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta0to3Up;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetRelativeSampleDown = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetRelativeSampleDown;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetRelativeSampleUp = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetRelativeSampleUp;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetRelativeBalDown = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetRelativeBalUp = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta0to5Down = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta0to5Down;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta0to5Up = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta0to5Up;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta3to5Down = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta3to5Down;
    this->GetCurrentOutputDictionary()->njetsWoNoisyJets_JetEta3to5Up = TheInputManager->GetInputDictionary()->jetVeto30WoNoisyJets_JetEta3to5Up;
    this->GetCurrentOutputDictionary()->jpt_1 = TheInputManager->GetInputDictionary()->j1ptWoNoisyJets;
    this->GetCurrentOutputDictionary()->jeta_1 = TheInputManager->GetInputDictionary()->j1etaWoNoisyJets;
    this->GetCurrentOutputDictionary()->jphi_1 = TheInputManager->GetInputDictionary()->j1phiWoNoisyJets;
    this->GetCurrentOutputDictionary()->jpt_2 = TheInputManager->GetInputDictionary()->j2ptWoNoisyJets;
    this->GetCurrentOutputDictionary()->jeta_2 = TheInputManager->GetInputDictionary()->j2etaWoNoisyJets;
    this->GetCurrentOutputDictionary()->jphi_2 = TheInputManager->GetInputDictionary()->j2phiWoNoisyJets;
    this->GetCurrentOutputDictionary()->bpt_1 = TheInputManager->GetInputDictionary()->jb1ptWoNoisyJets;
    this->GetCurrentOutputDictionary()->beta_1 = TheInputManager->GetInputDictionary()->jb1etaWoNoisyJets;
    this->GetCurrentOutputDictionary()->bphi_1 = TheInputManager->GetInputDictionary()->jb1phiWoNoisyJets;
    this->GetCurrentOutputDictionary()->bpt_2 = TheInputManager->GetInputDictionary()->jb2ptWoNoisyJets;
    this->GetCurrentOutputDictionary()->beta_2 = TheInputManager->GetInputDictionary()->jb2etaWoNoisyJets;
    this->GetCurrentOutputDictionary()->bphi_2 = TheInputManager->GetInputDictionary()->jb2phiWoNoisyJets;
    this->GetCurrentOutputDictionary()->bflavor_1 = TheInputManager->GetInputDictionary()->jb1hadronflavor;
    this->GetCurrentOutputDictionary()->bflavor_2 = TheInputManager->GetInputDictionary()->jb2hadronflavor;
    this->GetCurrentOutputDictionary()->mjj = TheInputManager->GetInputDictionary()->vbfMass;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta0to3Down = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta0to3Down;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta0to3Up = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta0to3Up;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta3to5Down = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta3to5Down;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta3to5Up = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta3to5Up;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta0to5Down = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta0to5Down;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetEta0to5Up = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetEta0to5Up;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetRelativeBalDown = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetRelativeBalDown;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetRelativeBalUp = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetRelativeBalUp;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetRelativeSampleDown = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetRelativeSampleDown;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets_JetRelativeSampleUp = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets_JetRelativeSampleUp;
    this->GetCurrentOutputDictionary()->mjjWoNoisyJets = TheInputManager->GetInputDictionary()->vbfMassWoNoisyJets;
    this->GetCurrentOutputDictionary()->genweight = TheInputManager->GetInputDictionary()->GenWeight;
    this->GetCurrentOutputDictionary()->byVLooseIsolationMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTVLoose;
    this->GetCurrentOutputDictionary()->byLooseIsolationMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTLoose;
    this->GetCurrentOutputDictionary()->byMediumIsolationMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTMedium;
    this->GetCurrentOutputDictionary()->byTightIsolationMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTTight;
    this->GetCurrentOutputDictionary()->byVTightIsolationMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTVTight;
    this->GetCurrentOutputDictionary()->byIsolationMVA3oldDMwLTraw_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTraw;
    this->GetCurrentOutputDictionary()->l2_decayMode = TheInputManager->GetInputDictionary()->tDecayMode;
    this->GetCurrentOutputDictionary()->againstElectronTightMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronTightMVA6;
    this->GetCurrentOutputDictionary()->againstMuonLoose3_2 = TheInputManager->GetInputDictionary()->tAgainstMuonLoose3;
    this->GetCurrentOutputDictionary()->gen_match_1 = TheInputManager->GetInputDictionary()->mZTTGenMatching;
    this->GetCurrentOutputDictionary()->gen_match_2 = TheInputManager->GetInputDictionary()->tZTTGenMatching;
    this->GetCurrentOutputDictionary()->npu = TheInputManager->GetInputDictionary()->nTruePU;
    this->GetCurrentOutputDictionary()->genpT = TheInputManager->GetInputDictionary()->genpT;
    this->GetCurrentOutputDictionary()->genM = TheInputManager->GetInputDictionary()->genM;
    this->GetCurrentOutputDictionary()->pt_top1 = TheInputManager->GetInputDictionary()->topQuarkPt1;
    this->GetCurrentOutputDictionary()->pt_top2 = TheInputManager->GetInputDictionary()->topQuarkPt2;
    this->GetCurrentOutputDictionary()->numGenJets = TheInputManager->GetInputDictionary()->numGenJets;
    this->GetCurrentOutputDictionary()->flag_BadChargedCandidate = TheInputManager->GetInputDictionary()->Flag_BadChargedCandidateFilter;
    this->GetCurrentOutputDictionary()->flag_BadPFMuon = TheInputManager->GetInputDictionary()->Flag_BadPFMuonFilter;
    this->GetCurrentOutputDictionary()->flag_EcalDeadCellTriggerPrimitive = TheInputManager->GetInputDictionary()->Flag_EcalDeadCellTriggerPrimitiveFilter;
    this->GetCurrentOutputDictionary()->flag_HBHENoise = TheInputManager->GetInputDictionary()->Flag_HBHENoiseFilter;
    this->GetCurrentOutputDictionary()->flag_HBHENoiseIso = TheInputManager->GetInputDictionary()->Flag_HBHENoiseIsoFilter;
    this->GetCurrentOutputDictionary()->flag_eeBadSc = TheInputManager->GetInputDictionary()->Flag_eeBadScFilter;
    this->GetCurrentOutputDictionary()->flag_globalTightHalo2016 = TheInputManager->GetInputDictionary()->Flag_globalSuperTightHalo2016Filter;
    this->GetCurrentOutputDictionary()->flag_goodVertices = TheInputManager->GetInputDictionary()->Flag_goodVertices;
    this->GetCurrentOutputDictionary()->flag_globalSuperTightHalo2016 = TheInputManager->GetInputDictionary()->Flag_globalSuperTightHalo2016Filter;
    this->GetCurrentOutputDictionary()->flag_ecalBadCalib = TheInputManager->GetInputDictionary()->Flag_ecalBadCalibFilter;
    this->GetCurrentOutputDictionary()->flag_duplicateMuons = TheInputManager->GetInputDictionary()->Flag_duplicateMuons;
    this->GetCurrentOutputDictionary()->flag_badMuons = TheInputManager->GetInputDictionary()->Flag_badMuons;
  }
  
};
