#include "TROOT.h"
#include "OutputManager.cc"

class EventManager
{
 public:  
  InputManager* TheInputManager;
  OutputManager* TheOutputManager;
  
  EventManager()
    {
      TheInputManager = new InputManager();
      TheOutputManager = new OutputManager();
    }
  ~EventManager()
    {
      delete TheInputManager;
      delete TheOutputManager;
    }
  void AttachInputChainToVariables(TChain* TheChain)
  {
    TheInputManager->AttachChainToVariables(TheChain);
  }
  void AttachOutputTreeToVariables(TTree* TheTree)
  {
    TheOutputManager->AttachTreeToVariables(TheTree);
  }  

  //check if we're a good event using the input values. 
  // obnoxious, but may be beneficial in the long run.
  bool IsGoodEvent()
  {
    bool EventValid = true;
    //matches a trigger
    if(!TheInputManager->GetInputDictionary()->IsoMu27Pass || !TheInputManager->GetInputDictionary()->Mu20Tau27Pass) EventValid = false;
    //Look for distance between the mu and tau    
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
    Float_t DeltaR = MuVector.DeltaR(TauVector);
    if(DeltaR < 0.5) EventValid = false;
    //check that the pt's work with the stiched together triggers
    if(TheInputManager->GetInputDictionary()->IsoMu27Pass && !TheInputManager->GetInputDictionary()->Mu20Tau27Pass) 
      {
	if(!(TheInputManager->GetInputDictionary()->mPt > 29.0))EventValid = false;
      }
    else if(TheInputManager->GetInputDictionary()->Mu20Tau27Pass && !TheInputManager->GetInputDictionary()->IsoMu27Pass)
      {
	if(!(TheInputManager->GetInputDictionary()->mPt > 22.0 && TheInputManager->GetInputDictionary()->tPt > 29.0)) EventValid = false;
      }
    else if (TheInputManager->GetInputDictionary()->IsoMu27Pass && TheInputManager->GetInputDictionary()->Mu20Tau27Pass)
      {
	if(!(TheInputManager->GetInputDictionary()->mPt > 29.0 && TheInputManager->GetInputDictionary()->tPt > 29.0)) EventValid = false;
      }
    //Look at event etas    
    //original iso mu 27 etas
    if( TheInputManager->GetInputDictionary()->IsoMu27Pass && 
	(fabs(TheInputManager->GetInputDictionary()->mEta > 2.4) || 
	 fabs(TheInputManager->GetInputDictionary()->tEta>2.3))) EventValid = false;
    //new cross trigger etas only allow out to 2.1 for both
    if(TheInputManager->GetInputDictionary()->Mu20Tau27Pass && 
       (fabs(TheInputManager->GetInputDictionary()->mEta) > 2.1 || 
	fabs(TheInputManager->GetInputDictionary()->tEta) > 2.1)) EventValid = false;    
    
    //make sure we have no charge greater than 1 for the tau
    if(TheInputManager->GetInputDictionary()->tCharge > 1) EventValid = false;
    //match muon conditions (iso and ID)
    if(!TheInputManager->GetInputDictionary()->mPFIDMedium || TheInputManager->GetInputDictionary()->mRelPFIsoDBDefault > 0.15 ) EventValid = false;
    //cecile here has electron and muon vetos of some stripe?
    if(TheInputManager->GetInputDictionary()->eVetoZTTp001dxyzR0>0) EventValid = false;
    if(TheInputManager->GetInputDictionary()->muVetoZTTp001dxyzR0>1) EventValid = false;
    //if dimuon Veto > 0 continue?
    if(TheInputManager->GetInputDictionary()->dimuonVeto>0) EventValid = false;
    //tau meets anti muon tight
    if(!TheInputManager->GetInputDictionary()->tAgainstMuonTight3) EventValid = false;
    // tau meets anti Electron VLoose
    if(!TheInputManager->GetInputDictionary()->tAgainstElectronVLooseMVA6) EventValid = false;    
    return EventValid;
  }
  
};

