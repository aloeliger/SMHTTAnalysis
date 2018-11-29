#include "TROOT.h"
#include <string>
#include "HTT-utilities/RecoilCorrections/src/MEtSys.cc"

void GenerateRecoilCorrectionUncertainties(string FileToRun)
{
  TFile* TheFile = new TFile(FileToRun.c_str(),"UPDATE");
  TTree* TheTree = (TTree*) TheFile->Get("mutau_tree");
  
  //met system
  Float_t met_px;
  Float_t met_py;

  //full lepton system
  Float_t genpX;
  Float_t genpY;

  //Visible Lepton sytem
  Float_t vispX;
  Float_t vispY;

  Int_t njets;  

  float Met_UP_X;
  float Met_UP_Y;
  float Met_DOWN_X;
  float Met_DOWN_Y;

  TheTree->SetBranchAddress("met_px",&met_px);
  TheTree->SetBranchAddress("met_py",&met_py);
  TheTree->SetBranchAddress("genpX",&genpX);
  TheTree->SetBranchAddress("genpY",&genpY);
  TheTree->SetBranchAddress("vispX",&vispX);
  TheTree->SetBranchAddress("vispY",&vispY);
  TheTree->SetBranchAddress("njets",&njets);  

  TBranch* UpBranch_X = TheTree->Branch("met_RecUnc_X_UP",&Met_UP_X);
  TBranch* UpBranch_Y = TheTree->Branch("met_RecUnc_Y_UP",&Met_UP_Y);
  TBranch* DownBranch_X = TheTree->Branch("met_RecUnc_X_DOWN",&Met_DOWN_X);
  TBranch* DownBranch_Y = TheTree->Branch("met_RecUnc_Y_DOWN",&Met_DOWN_Y);
  //setup the Metsys file
  MEtSys metSys("HTT-utilities/RecoilCorrections/data/MEtSys.root");
  
  string FileName;
  if(FileToRun.find("/") != string::npos) FileName = FileToRun.substr(FileToRun.rfind("/"));
  else FileName = FileToRun;
    
  int Process = 0;
  if(FileName.find("WW") != string::npos
     || FileName.find("WZ") != string::npos
     || FileName.find("ZZ") != string::npos
     || FileName.find("VV") != string::npos
     || FileName.find("ST") != string::npos) 
    {
      std::cout<<"Using Process Type: EWK"<<std::endl;
      Process= MEtSys::ProcessType::EWK;
    }
  else if(FileName.find("TTTo") != string::npos) 
    {
      std::cout<<"Using Process Type: TOP"<<std::endl;
      Process = MEtSys::ProcessType::TOP;
    }
  else 
    {
      std::cout<<"Using Process Type: BOSON"<<std::endl;
      Process = MEtSys::ProcessType::BOSON;
    }

  int NumberOfEntries = TheTree->GetEntries();
  for(int i =0; i < NumberOfEntries; ++i)
    {
      TheTree->GetEntry(i);
      if(i%(NumberOfEntries/20)==0 ||  i==(NumberOfEntries-1)) 
	{	  
	  fprintf(stdout,"<"); 
	  for(int NumEquals = 0;NumEquals < i/(NumberOfEntries/20); NumEquals++) fprintf(stdout,"="); 
	  for(int NumSpaces = 0;NumSpaces < 20-(i/(NumberOfEntries/20));NumSpaces++) fprintf(stdout," ");
	  fprintf(stdout,">\r");
	  if(i==(NumberOfEntries-1)) fprintf(stdout,"<====================>\n");
	  fflush(stdout);
	}
      

      //do the met systematic Whatever.
      metSys.ApplyMEtSys(met_px,met_py,
 			 genpX,genpY,
			 vispX,vispY,
			 njets,
			 Process,
			 MEtSys::SysType::Response,
			 MEtSys::SysShift::Up,
			 Met_UP_X, Met_UP_Y 
			 );

      metSys.ApplyMEtSys(met_px,met_py,
 			 genpX,genpY,
			 vispX,vispY,
			 njets,
			 Process,
			 MEtSys::SysType::Response,
			 MEtSys::SysShift::Down,
			 Met_DOWN_X, Met_DOWN_Y
			 );
      UpBranch_X->Fill();
      UpBranch_Y->Fill();
      DownBranch_X->Fill();
      DownBranch_Y->Fill();

    }
  TheFile->cd();
  TheTree->Write();
  TheFile->Write();
  TheFile->Close();
}
