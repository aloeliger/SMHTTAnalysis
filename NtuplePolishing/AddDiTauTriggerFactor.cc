#include "TROOT.h"
#include "SFtautrigger.h"
#include <string>
#include "Python.h"

static PyObject * DiTauTriggerFactorWrapper(PyObject *self, PyObject *args)
{
  float_t pt_2,eta_2,phi_2

    if(!PyArg_ParseTuple(args,"fff", &pt_2, &eta_2, &phi_2))
    {
      return NULL;
    }
  
  TFile* fTylerN = new TFile("Weightings/tauTriggerEfficiencies2017_New.root");
  TFile* fTyler= new TFile("Weightings/tauTriggerEfficiencies2017.root");
  
  TH1F* mTauData_ = (TH1F*) fTylerN->Get("hist_MuTauTriggerEfficiency_tightTauMVA_DATA");
  TH1F* mTauMC_ = (TH1F*) fTylerN->Get("hist_MuTauTriggerEfficiency_tightTauMVA_MC");
  TH2F* mTauEtaPhiData_ =(TH2F*) fTyler->Get("muTau_tight_DATA");
  TH2F* mTauEtaPhiMC_ =(TH2F*) fTyler->Get("muTau_tight_MC");
  TH2F* mTauEtaPhiAvgData_ =(TH2F*) fTyler->Get("muTau_tight_AVG_DATA");
  TH2F* mTauEtaPhiAvgMC_ =(TH2F*) fTyler->Get("muTau_tight_AVG_MC");

  float DiTauTriggerWeight = getDiTauScaleFactor(pt_2,eta_2,phi_2,0,mTauMC_,mTauEtaPhiMC_,mTauEtaPhiAvgMC_,mTauData_,mTauEtaPhiData_,mTauEtaPhiAvgData_);

  return PyBuildValue("f",DiTauTriggerWeight);

}

static PyMethodDef DiTauTriggerMethods[] = 
  {
    {"DiTauTriggerWrapper",DiTauTriggerWrapper,METH_VARARGS,"Get the DiTau Trigger Scale Factor"},
    {NULL,NULL,0,NULL}
  };

PyMODINIT_FUNC initDiTau(void)
{
  (void) Py_InitModile("DiTauTriggerWrapper",DiTauTriggerMethods);
}

void AddDiTauTriggerFactor(std::string input)
{
  std::cout<<"Setting up file and tree..."<<std::endl;
  TFile* TheFile = new TFile(input.c_str(), "UPDATE");
  TTree* Tree = (TTree*) TheFile->Get("mt_Selected");
  TH1F* eventCount = (TH1F*) TheFile->Get("eventCount");
  float TotalNumberOfEvents = eventCount->GetBinContent(1);

  float_t pt_2,eta_2,phi_2;
  
  Tree->SetBranchAddress("pt_2",&pt_2);
  Tree->SetBranchAddress("eta_2",&eta_2);
  Tree->SetBranchAddress("phi_2",&phi_2);
  
  TFile* fTylerN = new TFile("Weightings/tauTriggerEfficiencies2017_New.root");
  TFile* fTyler= new TFile("Weightings/tauTriggerEfficiencies2017.root");
  
  TH1F* mTauData_ = (TH1F*) fTylerN->Get("hist_MuTauTriggerEfficiency_tightTauMVA_DATA");
  TH1F* mTauMC_ = (TH1F*) fTylerN->Get("hist_MuTauTriggerEfficiency_tightTauMVA_MC");
  TH2F* mTauEtaPhiData_ =(TH2F*) fTyler->Get("muTau_tight_DATA");
  TH2F* mTauEtaPhiMC_ =(TH2F*) fTyler->Get("muTau_tight_MC");
  TH2F* mTauEtaPhiAvgData_ =(TH2F*) fTyler->Get("muTau_tight_AVG_DATA");
  TH2F* mTauEtaPhiAvgMC_ =(TH2F*) fTyler->Get("muTau_tight_AVG_MC");
  
  float DiTauTriggerWeight;
  std::cout<<"Branching..."<<std::endl;
  TBranch* DiTauTriggerBranch = Tree->Branch("DiTauTriggerWeight",&DiTauTriggerWeight);
  
  std::cout<<"Adding Scale Factors..."<<std::endl;
  int NumberOfEntries = Tree->GetEntries();
  for(int i = 0; i < NumberOfEntries; ++i)
    {
      Tree->GetEntry(i);
      if(i >=20 )
	{
	  if(i%(NumberOfEntries/20)==0 ||  i==(NumberOfEntries-1)) 
	    {	  
	      fprintf(stdout,"["); 
	      for(int NumEquals = 0;NumEquals < i/(NumberOfEntries/20); NumEquals++) fprintf(stdout,"="); 
	      for(int NumSpaces = 0;NumSpaces < 20-(i/(NumberOfEntries/20));NumSpaces++) fprintf(stdout," ");
	      fprintf(stdout,"]\r");
	      if(i==(NumberOfEntries-1)) fprintf(stdout,"[====================]\n");
	      fflush(stdout);
	    }
	}
      
      DiTauTriggerWeight = getDiTauScaleFactor(pt_2,eta_2,phi_2,0,mTauMC_,mTauEtaPhiMC_,mTauEtaPhiAvgMC_,mTauData_,mTauEtaPhiData_,mTauEtaPhiAvgData_);
      DiTauTriggerBranch->Fill();
    }
  TheFile->cd();
  Tree->Write();
  TheFile->Write();
  TheFile->Close();
}
