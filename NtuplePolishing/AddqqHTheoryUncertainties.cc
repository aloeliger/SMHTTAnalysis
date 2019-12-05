#include "TROOT.h"
#include "qq2Hqq_uncert_scheme.h"
#include <string>

void AddqqHTheoryUncertainties(std::string input)
{
  TFile* theFile = new TFile(input.c_str(),"UPDATE");
  TTree* tree = (TTree*) theFile->Get("mt_Selected");

  float Rivet_stage1_1_fine_cat_pTjet30GeV;

  float THU_qqH_yield_up;
  float THU_qqH_PTH200_up;
  float THU_qqH_Mjj60_up;
  float THU_qqH_Mjj120_up;
  float THU_qqH_Mjj350_up;
  float THU_qqH_Mjj700_up;
  float THU_qqH_Mjj1000_up;
  float THU_qqH_Mjj1500_up;
  float THU_qqH_PTH25_up;
  float THU_qqH_JET01_up;
  float THU_qqH_yield_down;
  float THU_qqH_PTH200_down;
  float THU_qqH_Mjj60_down;
  float THU_qqH_Mjj120_down;
  float THU_qqH_Mjj350_down;
  float THU_qqH_Mjj700_down;
  float THU_qqH_Mjj1000_down;
  float THU_qqH_Mjj1500_down;
  float THU_qqH_PTH25_down;
  float THU_qqH_JET01_down;
  
  tree->SetBranchAddress("Rivet_stage1_1_fine_cat_pTjet30GeV",&Rivet_stage1_1_fine_cat_pTjet30GeV);

  TBranch* THU_qqH_yield_up_branch = tree->Branch("THU_qqH_yield_up",&THU_qqH_yield_up);
  TBranch* THU_qqH_PTH200_up_branch = tree->Branch("THU_qqH_PTH200_up",&THU_qqH_PTH200_up);
  TBranch* THU_qqH_Mjj60_up_branch = tree->Branch("THU_qqH_Mjj60_up",&THU_qqH_Mjj60_up);
  TBranch* THU_qqH_Mjj120_up_branch = tree->Branch("THU_qqH_Mjj120_up",&THU_qqH_Mjj120_up);
  TBranch* THU_qqH_Mjj350_up_branch = tree->Branch("THU_qqH_Mjj350_up",&THU_qqH_Mjj350_up);
  TBranch* THU_qqH_Mjj700_up_branch = tree->Branch("THU_qqH_Mjj700_up",&THU_qqH_Mjj700_up);
  TBranch* THU_qqH_Mjj1000_up_branch = tree->Branch("THU_qqH_Mjj1000_up",&THU_qqH_Mjj1000_up);
  TBranch* THU_qqH_Mjj1500_up_branch = tree->Branch("THU_qqH_Mjj1500_up",&THU_qqH_Mjj1500_up);
  TBranch* THU_qqH_PTH25_up_branch = tree->Branch("THU_qqH_PTH25_up",&THU_qqH_PTH25_up);
  TBranch* THU_qqH_JET01_up_branch = tree->Branch("THU_qqH_JET01_up",&THU_qqH_JET01_up);
  TBranch* THU_qqH_yield_down_branch = tree->Branch("THU_qqH_yield_down",&THU_qqH_yield_down);
  TBranch* THU_qqH_PTH200_down_branch = tree->Branch("THU_qqH_PTH200_down",&THU_qqH_PTH200_down);
  TBranch* THU_qqH_Mjj60_down_branch = tree->Branch("THU_qqH_Mjj60_down",&THU_qqH_Mjj60_down);
  TBranch* THU_qqH_Mjj120_down_branch = tree->Branch("THU_qqH_Mjj120_down",&THU_qqH_Mjj120_down);
  TBranch* THU_qqH_Mjj350_down_branch = tree->Branch("THU_qqH_Mjj350_down",&THU_qqH_Mjj350_down);
  TBranch* THU_qqH_Mjj700_down_branch = tree->Branch("THU_qqH_Mjj700_down",&THU_qqH_Mjj700_down);
  TBranch* THU_qqH_Mjj1000_down_branch = tree->Branch("THU_qqH_Mjj1000_down",&THU_qqH_Mjj1000_down);
  TBranch* THU_qqH_Mjj1500_down_branch = tree->Branch("THU_qqH_Mjj1500_down",&THU_qqH_Mjj1500_down);
  TBranch* THU_qqH_PTH25_down_branch = tree->Branch("THU_qqH_PTH25_down",&THU_qqH_PTH25_down);
  TBranch* THU_qqH_JET01_down_branch = tree->Branch("THU_qqH_JET01_down",&THU_qqH_JET01_down);
  
  
  int NumberOfEntries = tree->GetEntries();
    for (int i = 0; i < NumberOfEntries; ++i)
      {
	tree->GetEntry(i);
	if(i%(NumberOfEntries/20)==0 ||  i==(NumberOfEntries-1)) 
	{	  
	  fprintf(stdout,"["); 
	  for(int NumEquals = 0;NumEquals < i/(NumberOfEntries/20); NumEquals++) fprintf(stdout,"="); 
	  for(int NumSpaces = 0;NumSpaces < 20-(i/(NumberOfEntries/20));NumSpaces++) fprintf(stdout," ");
	  fprintf(stdout,"]\r");
	  if(i==(NumberOfEntries-1)) fprintf(stdout,"[====================]\n");
	  fflush(stdout);
	}

	THU_qqH_yield_up = vbf_uncert_stage_1_1(0,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_PTH200_up = vbf_uncert_stage_1_1(1,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj60_up = vbf_uncert_stage_1_1(2,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj120_up = vbf_uncert_stage_1_1(3,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj350_up = vbf_uncert_stage_1_1(4,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj700_up = vbf_uncert_stage_1_1(5,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj1000_up = vbf_uncert_stage_1_1(6,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_Mjj1500_up = vbf_uncert_stage_1_1(7,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_PTH25_up = vbf_uncert_stage_1_1(8,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);
	THU_qqH_JET01_up = vbf_uncert_stage_1_1(9,int(Rivet_stage1_1_fine_cat_pTjet30GeV),1.0);	
	THU_qqH_yield_down = vbf_uncert_stage_1_1(0,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_PTH200_down = vbf_uncert_stage_1_1(1,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj60_down = vbf_uncert_stage_1_1(2,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj120_down = vbf_uncert_stage_1_1(3,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj350_down = vbf_uncert_stage_1_1(4,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj700_down = vbf_uncert_stage_1_1(5,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj1000_down = vbf_uncert_stage_1_1(6,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_Mjj1500_down = vbf_uncert_stage_1_1(7,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_PTH25_down = vbf_uncert_stage_1_1(8,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);
	THU_qqH_JET01_down = vbf_uncert_stage_1_1(9,int(Rivet_stage1_1_fine_cat_pTjet30GeV),-1.0);	
	THU_qqH_yield_up_branch->Fill();
	THU_qqH_PTH200_up_branch->Fill();
	THU_qqH_Mjj60_up_branch->Fill();
	THU_qqH_Mjj120_up_branch->Fill();
	THU_qqH_Mjj350_up_branch->Fill();
	THU_qqH_Mjj700_up_branch->Fill();
	THU_qqH_Mjj1000_up_branch->Fill();
	THU_qqH_Mjj1500_up_branch->Fill();
	THU_qqH_PTH25_up_branch->Fill();
	THU_qqH_JET01_up_branch->Fill();
	THU_qqH_yield_down_branch->Fill();
	THU_qqH_PTH200_down_branch->Fill();
	THU_qqH_Mjj60_down_branch->Fill();
	THU_qqH_Mjj120_down_branch->Fill();
	THU_qqH_Mjj350_down_branch->Fill();
	THU_qqH_Mjj700_down_branch->Fill();
	THU_qqH_Mjj1000_down_branch->Fill();
	THU_qqH_Mjj1500_down_branch->Fill();
	THU_qqH_PTH25_down_branch->Fill();
	THU_qqH_JET01_down_branch->Fill();
      }
  tree->Write();
  theFile->Write();
  theFile->Close();
}
