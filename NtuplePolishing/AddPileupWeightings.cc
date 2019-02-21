#include "TROOT.h"
#include "/data/aloeliger/CMSSW_9_4_0/src/PhysicsTools/Utilities/interface/LumiReweightingStandAlone.h"
#include <string>

void AddPileupWeightings(std::string input)
{
  TFile* MyFile = new TFile(input.c_str(),"UPDATE");
  TTree* Tree = (TTree*) MyFile->Get("mutau_tree");
  TH1F* nevents = (TH1F*) MyFile->Get("nevents");
  float TotalNumberOfEvents = nevents->GetBinContent(1);

  float npu;
  float PileupWeight;
  TTree->SetBranchAddress("npu",&npu);

  reweight::LumiReWeighting* LumiWeights_12;
  LumiWeights_12 = new reweight::LumiReWeighting(input.c_str(),
						 "Weightings/MyDataPileupHistogram.root",
						 "pileup_mc",
						 "pileup");

  TBranch* PileupWeightBranch = Tree->Branch("PileupWeight",&PileupWeight)

  int NumberOfEntries = Tree->GetEntries();
  for(int i = 0; i < NumberOfEntries; ++i)
    {
      Tree->GetEntry(i);
      if(i%(NumberOfEntries/20)==0 ||  i==(NumberOfEntries-1)) 
	{	  
	  fprintf(stdout,"["); 
	  for(int NumEquals = 0;NumEquals < i/(NumberOfEntries/20); NumEquals++) fprintf(stdout,"="); 
	  for(int NumSpaces = 0;NumSpaces < 20-(i/(NumberOfEntries/20));NumSpaces++) fprintf(stdout," ");
	  fprintf(stdout,"]\r");
	  if(i==(NumberOfEntries-1)) fprintf(stdout,"[====================]\n");
	  fflush(stdout);
	}
      
      PileupWeight = LumiWeights_12->weight(npu);
      PileupWeightBranch->Fill();
      
    }

  Tree->Write();
  MyFile->Write();
  MyFile->Close();
}
