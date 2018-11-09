#include "TROOT.h"
#include "InputManager.cc"

struct OutputDictionary
{
  Float_t run;
  Float_t lumi;
  Float_t evt;
  Float_t NUP;
  Float_t npv;
  Float_t npu;  
  Float_t aMCatNLO_weight;
  Float_t pt_1;
  Float_t phi_1;
  Float_t eta_1;
  Float_t m_1;
  Float_t e_1;
  Float_t q_1;
  Float_t d0_1;
  Float_t dZ_1;
  Float_t iso_1;
  Float_t id_m_medium_1;
  Float_t id_m_tight_1;
  Float_t pt_2;
  Float_t phi_2;
  Float_t eta_2;
  Float_t m_2;
  Float_t e_2;
  Float_t q_2;
  Float_t d0_2;
  Float_t dZ_2;
  Float_t iso_2;
  Float_t l2_decayMode;
  Float_t againstElectronLooseMVA6_2;
  Float_t againstElectronMediumMVA6_2;
  Float_t againstElectronTightMVA6_2;
  Float_t againstElectronVLooseMVA6_2;
  Float_t againstElectronVTightMVA6_2;
  Float_t againstMuonLoose3_2;
  Float_t againstMuonTight3_2;
  Float_t byLooseCombinedIsolationDeltaBetaCorr3Hits_2;
  Float_t byMediumCombinedIsolationDeltaBetaCorr3Hits_2;
  Float_t byTightCombinedIsolationDeltaBetaCorr3Hits_2;
  Float_t byCombinedIsolationDeltaBetaCorrRaw3Hits_2;
  Float_t byLooseCombinedIsolationDeltaBetaCorr3HitsdR03_2;
  Float_t byMediumCombinedIsolationDeltaBetaCorr3HitsdR03_2;
  Float_t byTightCombinedIsolationDeltaBetaCorr3HitsdR03_2;
  Float_t byVLooseIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byVLooseIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byVLooseIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byLooseIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byLooseIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byLooseIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byMediumIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byMediumIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byMediumIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byTightIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byTightIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byTightIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byVTightIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byVTightIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byVTightIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byVVTightIsolationMVArun2v1DBnewDMwLT_2;
  Float_t byVVTightIsolationMVArun2v1DBoldDMwLT_2;
  Float_t byVVTightIsolationMVArun2v1DBdR03oldDMwLT_2;
  Float_t byIsolationMVA3oldDMwoLTraw_2;
  Float_t byIsolationMVA3oldDMwLTraw_2;
  Float_t byIsolationMVA3newDMwoLTraw_2;
  Float_t byIsolationMVA3newDMwLTraw_2;
  Float_t neutralIsoPtSumdR03_2;
  Float_t chargedIsoPtSumdR03_2;
  Float_t byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byLooseIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byMediumIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byTightIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byVTightIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2;
  Float_t byIsolationRerunMVA3oldDMwLTraw_2;
  Float_t byVLooseIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byLooseIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byMediumIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byTightIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byVTightIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byVVTightIsolationRerunMVArun2v2DBoldDMwLT_2;
  Float_t byIsolationRerunMVA3oldDMwLTrawv2_2;
  Float_t chargedIsoPtSum_2;
  Float_t decayModeFinding_2;
  Float_t decayModeFindingNewDMs_2;
  Float_t neutralIsoPtSum_2;
  Float_t puCorrPtSum_2;
  Float_t chargedIso_2;
  Float_t neutralIso_2;
  Float_t puIso_2;
  Float_t photonIso_2;
  Float_t trackpt_2;
  Float_t numGenJets;
  Float_t jetPt_2;
  Float_t charged_signalCone_2;
  Float_t charged_isoCone_2;

  Float_t matchIsoMu27_1;
  Float_t passIsoMu27;

  Float_t pt_top1;
  Float_t pt_top2;
  Float_t genweight;
  Float_t gen_match_2;

  Float_t met;
  Float_t metphi;

  Float_t nbtag;
  Float_t njets;

  //new stuff for mu/tau trigger variables
  Float_t passMu20Tau27;
  Float_t MuonMatchesMu20Tau27;
  Float_t TauMatchesMu20Tau27;
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
    TheTree->Branch("run", &this->GetStagedOutputDictionary()->run, "run/I");
    TheTree->Branch("lumi", &this->GetStagedOutputDictionary()->lumi, "lumi/I");
    TheTree->Branch("evt", &this->GetStagedOutputDictionary()->evt, "evt/I");

    TheTree->Branch("NUP", &this->GetStagedOutputDictionary()->NUP, "NUP/I");
    TheTree->Branch("npv", &this->GetStagedOutputDictionary()->npv, "npv/F");
    TheTree->Branch("npu", &this->GetStagedOutputDictionary()->npu, "npu/F");
    TheTree->Branch("amcatNLO_weight", &this->GetStagedOutputDictionary()->aMCatNLO_weight, "aMCatNLO_weight/F");
    
    TheTree->Branch("pt_1", &this->GetStagedOutputDictionary()->pt_1, "pt_1/F");
    TheTree->Branch("phi_1", &this->GetStagedOutputDictionary()->phi_1, "phi_1/F");
    TheTree->Branch("eta_1", &this->GetStagedOutputDictionary()->eta_1, "eta_1/F");
    TheTree->Branch("m_1", &this->GetStagedOutputDictionary()->m_1, "m_1/F");
    TheTree->Branch("e_1", &this->GetStagedOutputDictionary()->e_1, "e_1/F");
    TheTree->Branch("q_1", &this->GetStagedOutputDictionary()->q_1, "q_1/F");
    TheTree->Branch("d0_1", &this->GetStagedOutputDictionary()->d0_1, "d0_1/F");
    TheTree->Branch("dZ_1", &this->GetStagedOutputDictionary()->dZ_1, "dZ_1/F");
    TheTree->Branch("iso_1", &this->GetStagedOutputDictionary()->iso_1, "iso_1/F");
    TheTree->Branch("id_m_medium_1", &this->GetStagedOutputDictionary()->id_m_medium_1, "id_m_medium_1/F");
    TheTree->Branch("id_m_tight_1", &this->GetStagedOutputDictionary()->id_m_tight_1, "id_m_tight_1/F");

    TheTree->Branch("pt_2", &this->GetStagedOutputDictionary()->pt_2, "pt_2/F");
    TheTree->Branch("phi_2", &this->GetStagedOutputDictionary()->phi_2, "phi_2/F");
    TheTree->Branch("eta_2", &this->GetStagedOutputDictionary()->eta_2, "eta_2/F");
    TheTree->Branch("m_2", &this->GetStagedOutputDictionary()->m_2, "m_2/F");
    TheTree->Branch("e_2", &this->GetStagedOutputDictionary()->e_2, "e_2/F");
    TheTree->Branch("q_2", &this->GetStagedOutputDictionary()->q_2, "q_2/F");
    TheTree->Branch("d0_2", &this->GetStagedOutputDictionary()->d0_2, "d0_2/F");
    TheTree->Branch("dZ_2", &this->GetStagedOutputDictionary()->dZ_2, "dZ_2/F");
    TheTree->Branch("iso_2", &this->GetStagedOutputDictionary()->iso_2, "iso_2/F");
    TheTree->Branch("l2_decayMode", &this->GetStagedOutputDictionary()->l2_decayMode, "l2_decayMode/F");
    TheTree->Branch("againstElectronLooseMVA6_2", &this->GetStagedOutputDictionary()->againstElectronLooseMVA6_2, "againstElectronLooseMVA6_2/F");
    TheTree->Branch("againstElectronMediumMVA6_2", &this->GetStagedOutputDictionary()->againstElectronMediumMVA6_2, "againstElectronMediumMVA6_2/F");
    TheTree->Branch("againstElectronTightMVA6_2", &this->GetStagedOutputDictionary()->againstElectronTightMVA6_2, "againstElectronTightMVA6_2/F");
    TheTree->Branch("againstElectronVLooseMVA6_2", &this->GetStagedOutputDictionary()->againstElectronVLooseMVA6_2, "againstElectronVLooseMVA6_2/F");
    TheTree->Branch("againstElectronVTightMVA6_2", &this->GetStagedOutputDictionary()->againstElectronVTightMVA6_2, "againstElectronVTightMVA6_2/F");
    TheTree->Branch("againstMuonLoose3_2", &this->GetStagedOutputDictionary()->againstMuonLoose3_2, "againstMuonLoose3_2/F");
    TheTree->Branch("againstMuonTight3_2", &this->GetStagedOutputDictionary()->againstMuonTight3_2, "againstMuonTight3_2/F");
    TheTree->Branch("byLooseCombinedIsolationDeltaBetaCorr3Hits_2", &this->GetStagedOutputDictionary()->byLooseCombinedIsolationDeltaBetaCorr3Hits_2, "byLooseCombinedIsolationDeltaBetaCorr3Hits_2/F");
    TheTree->Branch("byMediumCombinedIsolationDeltaBetaCorr3Hits_2", &this->GetStagedOutputDictionary()->byMediumCombinedIsolationDeltaBetaCorr3Hits_2, "byMediumCombinedIsolationDeltaBetaCorr3Hits_2/F");
    TheTree->Branch("byTightCombinedIsolationDeltaBetaCorr3Hits_2", &this->GetStagedOutputDictionary()->byTightCombinedIsolationDeltaBetaCorr3Hits_2, "byTightCombinedIsolationDeltaBetaCorr3Hits_2/F");
    TheTree->Branch("byCombinedIsolationDeltaBetaCorrRaw3Hits_2", &this->GetStagedOutputDictionary()->byCombinedIsolationDeltaBetaCorrRaw3Hits_2, "byCombinedIsolationDeltaBetaCorrRaw3Hits_2/F");
    TheTree->Branch("byLooseCombinedIsolationDeltaBetaCorr3HitsdR03_2", &this->GetStagedOutputDictionary()->byLooseCombinedIsolationDeltaBetaCorr3HitsdR03_2, "byLooseCombinedIsolationDeltaBetaCorr3HitsdR03_2/F");
    TheTree->Branch("byMediumCombinedIsolationDeltaBetaCorr3HitsdR03_2", &this->GetStagedOutputDictionary()->byMediumCombinedIsolationDeltaBetaCorr3HitsdR03_2, "byMediumCombinedIsolationDeltaBetaCorr3HitsdR03_2/F");
    TheTree->Branch("byTightCombinedIsolationDeltaBetaCorr3HitsdR03_2", &this->GetStagedOutputDictionary()->byTightCombinedIsolationDeltaBetaCorr3HitsdR03_2, "byTightCombinedIsolationDeltaBetaCorr3HitsdR03_2/F");
    TheTree->Branch("byVLooseIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationMVArun2v1DBnewDMwLT_2, "byVLooseIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byVLooseIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationMVArun2v1DBoldDMwLT_2, "byVLooseIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byVLooseIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationMVArun2v1DBdR03oldDMwLT_2, "byVLooseIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byLooseIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationMVArun2v1DBnewDMwLT_2, "byLooseIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byLooseIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationMVArun2v1DBoldDMwLT_2, "byLooseIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byLooseIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationMVArun2v1DBdR03oldDMwLT_2, "byLooseIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byMediumIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationMVArun2v1DBnewDMwLT_2, "byMediumIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byMediumIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationMVArun2v1DBoldDMwLT_2, "byMediumIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byMediumIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationMVArun2v1DBdR03oldDMwLT_2, "byMediumIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byTightIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationMVArun2v1DBnewDMwLT_2, "byTightIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byTightIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationMVArun2v1DBoldDMwLT_2, "byTightIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byTightIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationMVArun2v1DBdR03oldDMwLT_2, "byTightIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byVTightIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationMVArun2v1DBnewDMwLT_2, "byVTightIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byVTightIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationMVArun2v1DBoldDMwLT_2, "byVTightIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byVTightIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationMVArun2v1DBdR03oldDMwLT_2, "byVTightIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byVVTightIsolationMVArun2v1DBnewDMwLT_2", &this->GetStagedOutputDictionary()->byVVTightIsolationMVArun2v1DBnewDMwLT_2, "byVVTightIsolationMVArun2v1DBnewDMwLT_2/F");
    TheTree->Branch("byVVTightIsolationMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVVTightIsolationMVArun2v1DBoldDMwLT_2, "byVVTightIsolationMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byVVTightIsolationMVArun2v1DBdR03oldDMwLT_2", &this->GetStagedOutputDictionary()->byVVTightIsolationMVArun2v1DBdR03oldDMwLT_2, "byVVTightIsolationMVArun2v1DBdR03oldDMwLT_2/F");
    TheTree->Branch("byIsolationMVA3oldDMwoLTraw_2", &this->GetStagedOutputDictionary()->byIsolationMVA3oldDMwoLTraw_2, "byIsolationMVA3oldDMwoLTraw_2/F");
    TheTree->Branch("byIsolationMVA3oldDMwLTraw_2", &this->GetStagedOutputDictionary()->byIsolationMVA3oldDMwLTraw_2, "byIsolationMVA3oldDMwLTraw_2/F");
    TheTree->Branch("byIsolationMVA3newDMwoLTraw_2", &this->GetStagedOutputDictionary()->byIsolationMVA3newDMwoLTraw_2, "byIsolationMVA3newDMwoLTraw_2/F");
    TheTree->Branch("byIsolationMVA3newDMwLTraw_2", &this->GetStagedOutputDictionary()->byIsolationMVA3newDMwLTraw_2, "byIsolationMVA3newDMwLTraw_2/F");
    
    TheTree->Branch("neutralIsoPtSumdR03_2", &this->GetStagedOutputDictionary()->neutralIsoPtSumdR03_2, "neutralIsoPtSumdR03_2/F");
    TheTree->Branch("chargedIsoPtSumdR03_2", &this->GetStagedOutputDictionary()->chargedIsoPtSumdR03_2, "chargedIsoPtSumdR03_2/F");
    
    TheTree->Branch("byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2, "byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byLooseIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationRerunMVArun2v1DBoldDMwLT_2, "byLooseIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byMediumIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationRerunMVArun2v1DBoldDMwLT_2, "byMediumIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byTightIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationRerunMVArun2v1DBoldDMwLT_2, "byTightIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byVTightIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationRerunMVArun2v1DBoldDMwLT_2, "byVTightIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2, "byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2/F");
    TheTree->Branch("byIsolationRerunMVA3oldDMwLTraw_2", &this->GetStagedOutputDictionary()->byIsolationRerunMVA3oldDMwLTraw_2, "byIsolationRerunMVA3oldDMwLTraw_2/F");
    
    TheTree->Branch("byVLooseIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVLooseIsolationRerunMVArun2v2DBoldDMwLT_2, "byVLooseIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byLooseIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byLooseIsolationRerunMVArun2v2DBoldDMwLT_2, "byLooseIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byMediumIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byMediumIsolationRerunMVArun2v2DBoldDMwLT_2, "byMediumIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byTightIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byTightIsolationRerunMVArun2v2DBoldDMwLT_2, "byTightIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byVTightIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVTightIsolationRerunMVArun2v2DBoldDMwLT_2, "byVTightIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byVVTightIsolationRerunMVArun2v2DBoldDMwLT_2", &this->GetStagedOutputDictionary()->byVVTightIsolationRerunMVArun2v2DBoldDMwLT_2, "byVVTightIsolationRerunMVArun2v2DBoldDMwLT_2/F");
    TheTree->Branch("byIsolationRerunMVA3oldDMwLTrawv2_2", &this->GetStagedOutputDictionary()->byIsolationRerunMVA3oldDMwLTrawv2_2, "byIsolationRerunMVA3oldDMwLTrawv2_2/F");
    
    TheTree->Branch("chargedIsoPtSum_2", &this->GetStagedOutputDictionary()->chargedIsoPtSum_2, "chargedIsoPtSum_2/F");
    TheTree->Branch("decayModeFinding_2", &this->GetStagedOutputDictionary()->decayModeFinding_2, "decayModeFinding_2/F");
    TheTree->Branch("decayModeFindingNewDMs_2", &this->GetStagedOutputDictionary()->decayModeFindingNewDMs_2, "decayModeFindingNewDMs_2/F");
    TheTree->Branch("neutralIsoPtSum_2", &this->GetStagedOutputDictionary()->neutralIsoPtSum_2, "neutralIsoPtSum_2/F");
    TheTree->Branch("puCorrPtSum_2", &this->GetStagedOutputDictionary()->puCorrPtSum_2, "puCorrPtSum_2/F");
    TheTree->Branch("chargedIso_2", &this->GetStagedOutputDictionary()->chargedIso_2, "chargedIso_2/F");
    TheTree->Branch("neutralIso_2", &this->GetStagedOutputDictionary()->neutralIso_2, "neutralIso_2/F");
    TheTree->Branch("puIso_2", &this->GetStagedOutputDictionary()->puIso_2, "puIso_2/F");
    TheTree->Branch("photonIso_2", &this->GetStagedOutputDictionary()->photonIso_2, "photonIso_2/F");
    TheTree->Branch("trackpt_2", &this->GetStagedOutputDictionary()->trackpt_2, "trackpt_2/F");
    TheTree->Branch("numGenJets", &this->GetStagedOutputDictionary()->numGenJets, "numGenJets/F");
    TheTree->Branch("jetPt_2", &this->GetStagedOutputDictionary()->jetPt_2, "jetPt_2/F");
    TheTree->Branch("charged_signalCone_2", &this->GetStagedOutputDictionary()->charged_signalCone_2, "charged_this->GetStagedOutputDictionary()->signalCone_2/F");
    TheTree->Branch("charged_isoCone_2", &this->GetStagedOutputDictionary()->charged_isoCone_2, "charged_isoCone_2/F");
    
    TheTree->Branch("matchIsoMu27_1", &this->GetStagedOutputDictionary()->matchIsoMu27_1, "matchIsoMu27_1/F");
    TheTree->Branch("passIsoMu27", &this->GetStagedOutputDictionary()->passIsoMu27, "passIsoMu27/F");

    TheTree->Branch("pt_top1", &this->GetStagedOutputDictionary()->pt_top1, "pt_top1/F");
    TheTree->Branch("pt_top2", &this->GetStagedOutputDictionary()->pt_top2, "pt_top2/F");
    TheTree->Branch("genweight", &this->GetStagedOutputDictionary()->genweight, "genweight/F");
    TheTree->Branch("gen_match_2", &this->GetStagedOutputDictionary()->gen_match_2, "gen_match_2/F");

    TheTree->Branch("met", &this->GetStagedOutputDictionary()->met, "met/F");
    TheTree->Branch("metphi", &this->GetStagedOutputDictionary()->metphi, "metphi/F");

    TheTree->Branch("nbtag", &this->GetStagedOutputDictionary()->nbtag, "nbtag/F");
    TheTree->Branch("njets", &this->GetStagedOutputDictionary()->njets, "njets/F");
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
    this->GetCurrentOutputDictionary()->run = TheInputManager->GetInputDictionary()->run;
    this->GetCurrentOutputDictionary()->lumi = TheInputManager->GetInputDictionary()->lumi;
    this->GetCurrentOutputDictionary()->evt = TheInputManager->GetInputDictionary()->evt;
    this->GetCurrentOutputDictionary()->NUP = TheInputManager->GetInputDictionary()->NUP;
    this->GetCurrentOutputDictionary()->npv = TheInputManager->GetInputDictionary()->nvtx;
    this->GetCurrentOutputDictionary()->npu = TheInputManager->GetInputDictionary()->nTruePU;
    this->GetCurrentOutputDictionary()->aMCatNLO_weight = TheInputManager->GetInputDictionary()->GenWeight;
    
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
    this->GetCurrentOutputDictionary()->q_1 = TheInputManager->GetInputDictionary()->mCharge;
    this->GetCurrentOutputDictionary()->d0_1 = TheInputManager->GetInputDictionary()->mPVDXY;
    this->GetCurrentOutputDictionary()->dZ_1 = TheInputManager->GetInputDictionary()->mPVDZ;
    this->GetCurrentOutputDictionary()->iso_1 = TheInputManager->GetInputDictionary()->mRelPFIsoDBDefault;
    this->GetCurrentOutputDictionary()->id_m_medium_1 = TheInputManager->GetInputDictionary()->mPFIDMedium;
    this->GetCurrentOutputDictionary()->id_m_tight_1 = TheInputManager->GetInputDictionary()->mCutBasedIdTight;    
    
    this->GetCurrentOutputDictionary()->pt_2 = TauVector.Pt();
    this->GetCurrentOutputDictionary()->phi_2 = TauVector.Phi();
    this->GetCurrentOutputDictionary()->eta_2 = TauVector.Eta();
    this->GetCurrentOutputDictionary()->m_2 = TauVector.M();
    this->GetCurrentOutputDictionary()->e_2 = TauVector.E();
    this->GetCurrentOutputDictionary()->q_2 = TheInputManager->GetInputDictionary()->tCharge;
    this->GetCurrentOutputDictionary()->d0_2 = TheInputManager->GetInputDictionary()->tPVDXY;
    this->GetCurrentOutputDictionary()->dZ_2 = TheInputManager->GetInputDictionary()->tPVDZ;
    this->GetCurrentOutputDictionary()->iso_2 = TheInputManager->GetInputDictionary()->tByIsolationMVArun2v1DBoldDMwLTraw;
    this->GetCurrentOutputDictionary()->dZ_2 = TheInputManager->GetInputDictionary()->tPVDZ;
    this->GetCurrentOutputDictionary()->l2_decayMode = TheInputManager->GetInputDictionary()->tDecayMode;
    this->GetCurrentOutputDictionary()->againstElectronLooseMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronLooseMVA6;
    this->GetCurrentOutputDictionary()->againstElectronMediumMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronMediumMVA6;
    this->GetCurrentOutputDictionary()->againstElectronTightMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronTightMVA6;
    this->GetCurrentOutputDictionary()->againstElectronVLooseMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronVLooseMVA6;
    this->GetCurrentOutputDictionary()->againstElectronVTightMVA6_2 = TheInputManager->GetInputDictionary()->tAgainstElectronVTightMVA6;
    this->GetCurrentOutputDictionary()->againstMuonLoose3_2 = TheInputManager->GetInputDictionary()->tAgainstMuonLoose3;
    this->GetCurrentOutputDictionary()->againstMuonTight3_2 = TheInputManager->GetInputDictionary()->tAgainstMuonTight3;
    this->GetCurrentOutputDictionary()->byLooseCombinedIsolationDeltaBetaCorr3Hits_2 = TheInputManager->GetInputDictionary()->tByLooseCombinedIsolationDeltaBetaCorr3Hits;
    this->GetCurrentOutputDictionary()->byMediumCombinedIsolationDeltaBetaCorr3Hits_2 = TheInputManager->GetInputDictionary()->tByMediumCombinedIsolationDeltaBetaCorr3Hits;
    this->GetCurrentOutputDictionary()->byTightCombinedIsolationDeltaBetaCorr3Hits_2 = TheInputManager->GetInputDictionary()->tByTightCombinedIsolationDeltaBetaCorr3Hits;
    this->GetCurrentOutputDictionary()->byCombinedIsolationDeltaBetaCorrRaw3Hits_2 = TheInputManager->GetInputDictionary()->tByCombinedIsolationDeltaBetaCorrRaw3Hits;
    this->GetCurrentOutputDictionary()->byVLooseIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByVLooseIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byVLooseIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByVLooseIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byLooseIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByLooseIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byLooseIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByLooseIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byMediumIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByMediumIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byMediumIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByMediumIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byTightIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByTightIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byTightIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByTightIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byVTightIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByVTightIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byVTightIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByVTightIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byVVTightIsolationMVArun2v1DBnewDMwLT_2 = TheInputManager->GetInputDictionary()->tByVVTightIsolationMVArun2v1DBnewDMwLT;
    this->GetCurrentOutputDictionary()->byVVTightIsolationMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tByVVTightIsolationMVArun2v1DBoldDMwLT;
    this->GetCurrentOutputDictionary()->byIsolationMVA3oldDMwoLTraw_2 = TheInputManager->GetInputDictionary()->tByIsolationMVArun2v1DBoldDMwLTraw;
    this->GetCurrentOutputDictionary()->byIsolationMVA3newDMwoLTraw_2 = TheInputManager->GetInputDictionary()->tByIsolationMVArun2v1DBnewDMwLTraw;
    this->GetCurrentOutputDictionary()->byIsolationMVA3newDMwLTraw_2 = TheInputManager->GetInputDictionary()->tByIsolationMVArun2v1DBnewDMwLTraw;
    this->GetCurrentOutputDictionary()->byVLooseIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTVLoose;
    this->GetCurrentOutputDictionary()->byLooseIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTLoose;
    this->GetCurrentOutputDictionary()->byMediumIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTMedium;
    this->GetCurrentOutputDictionary()->byTightIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTTight;
    this->GetCurrentOutputDictionary()->byVTightIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTVTight;
    this->GetCurrentOutputDictionary()->byVVTightIsolationRerunMVArun2v1DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTVVTight;
    this->GetCurrentOutputDictionary()->byIsolationRerunMVA3oldDMwLTraw_2  = TheInputManager->GetInputDictionary()->tRerunMVArun2v1DBoldDMwLTraw;
    this->GetCurrentOutputDictionary()->byVLooseIsolationRerunMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTVLoose;
    this->GetCurrentOutputDictionary()->byLooseIsolationRerunMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTLoose;
    this->GetCurrentOutputDictionary()->byMediumIsolationRerunMVArun2v2DBoldDMwLT_2  = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTMedium;
    this->GetCurrentOutputDictionary()->byTightIsolationRerunMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTTight;
    this->GetCurrentOutputDictionary()->byVTightIsolationRerunMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTVTight;
    this->GetCurrentOutputDictionary()->byVVTightIsolationRerunMVArun2v2DBoldDMwLT_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTVVTight;
    this->GetCurrentOutputDictionary()->byIsolationRerunMVA3oldDMwLTrawv2_2 = TheInputManager->GetInputDictionary()->tRerunMVArun2v2DBoldDMwLTraw;
    this->GetCurrentOutputDictionary()->neutralIsoPtSum_2 = TheInputManager->GetInputDictionary()->tNeutralIsoPtSum;
    this->GetCurrentOutputDictionary()->chargedIsoPtSum_2 = TheInputManager->GetInputDictionary()->tChargedIsoPtSum;
    this->GetCurrentOutputDictionary()->decayModeFinding_2 = TheInputManager->GetInputDictionary()->tDecayModeFinding;
    this->GetCurrentOutputDictionary()->decayModeFindingNewDMs_2 = TheInputManager->GetInputDictionary()->tDecayModeFindingNewDMs;
    this->GetCurrentOutputDictionary()->puCorrPtSum_2 = TheInputManager->GetInputDictionary()->tPuCorrPtSum;
    this->GetCurrentOutputDictionary()->chargedIso_2 = TheInputManager->GetInputDictionary()->tChargedIsoPtSum;
    this->GetCurrentOutputDictionary()->neutralIso_2 = TheInputManager->GetInputDictionary()->tNeutralIsoPtSum;
    this->GetCurrentOutputDictionary()->puIso_2 = TheInputManager->GetInputDictionary()->tPuCorrPtSum;
    this->GetCurrentOutputDictionary()->photonIso_2 = TheInputManager->GetInputDictionary()->tPhotonPtSumOutsideSignalCone;
    this->GetCurrentOutputDictionary()->trackpt_2 = TheInputManager->GetInputDictionary()->tLeadTrackPt;
    this->GetCurrentOutputDictionary()->numGenJets = TheInputManager->GetInputDictionary()->numGenJets;
    this->GetCurrentOutputDictionary()->jetPt_2 = TheInputManager->GetInputDictionary()->tJetPt;
    this->GetCurrentOutputDictionary()->charged_signalCone_2 = TheInputManager->GetInputDictionary()->tNChrgHadrSignalCands;
    this->GetCurrentOutputDictionary()->charged_isoCone_2 = TheInputManager->GetInputDictionary()->tNChrgHadrIsolationCands;
    this->GetCurrentOutputDictionary()->matchIsoMu27_1 = TheInputManager->GetInputDictionary()->mMatchesIsoMu27Path;
    this->GetCurrentOutputDictionary()->passIsoMu27 = TheInputManager->GetInputDictionary()->IsoMu27Pass;
    
    this->GetCurrentOutputDictionary()->pt_top1 = TheInputManager->GetInputDictionary()->topQuarkPt1;
    this->GetCurrentOutputDictionary()->pt_top2 = TheInputManager->GetInputDictionary()->topQuarkPt2;
    //this->GetCurrentOutputDictionary()->genweight = ;
    this->GetCurrentOutputDictionary()->gen_match_2 = TheInputManager->GetInputDictionary()->tZTTGenMatching;

    TLorentzVector MetVector;
    MetVector.SetPtEtaPhiM(TheInputManager->GetInputDictionary()->type1_pfMetEt,
			   0,
			   TheInputManager->GetInputDictionary()->type1_pfMetPhi,
			   0);
    this->GetCurrentOutputDictionary()->met = MetVector.Pt();
    this->GetCurrentOutputDictionary()->metphi = MetVector.Phi();

    this->GetCurrentOutputDictionary()->nbtag = TheInputManager->GetInputDictionary()->bjetCISVVeto20Medium;
    this->GetCurrentOutputDictionary()->njets = TheInputManager->GetInputDictionary()->jetVeto30;    
    //new trigger variables
    this->GetCurrentOutputDictionary()->passMu20Tau27 = TheInputManager->GetInputDictionary()->Mu20Tau27Pass;
    this->GetCurrentOutputDictionary()->MuonMatchesMu20Tau27 = TheInputManager->GetInputDictionary()->mMatchesIsoMu20Tau27Path;
    this->GetCurrentOutputDictionary()->TauMatchesMu20Tau27 = TheInputManager->GetInputDictionary()->tMatchesIsoMu20Tau27Path;
  }
  
};
