#include "TROOT.h"
#include <iostream>
#include <fstream>
#include <string>
#include "EventManager.cc"

void SkimChannel(string FileName, string OutFileName)
{
  TChain* ChannelChain = new TChain("mt/final/Ntuple");
  TH1F *EventCounter;
  TH1D *EventCounterWeights;
  TFile* HistoFile;
  bool FirstLoadedFile = true;
  string path="";
  string line="";
  ifstream ParamFile (FileName.c_str());
  
  TH1F* pileup_mc = new TH1F("pileup_mc","pileup_mc", 80, 0.0, 80.0);
  
  if(ParamFile.is_open())
    {
      int LinesProcessed = 0;
      while(getline(ParamFile,line))
	{
	  ++LinesProcessed;
	  std::cout<<"Processed Parameter File Through Line: "<<LinesProcessed<<"\r";
	  if(line.find(".root") != string::npos)
	    {
	      //std::cout<<"Added File: "<<line<<std::endl;
	      ChannelChain->Add((path+"/"+line).c_str());
	      HistoFile = new TFile((path+"/"+line).c_str(),"READ");
	      if(FirstLoadedFile)
		{		  		  
		  EventCounter = (TH1F*) HistoFile->Get("mt/eventCount")->Clone();
		  EventCounterWeights = (TH1D*) HistoFile->Get("mt/summedWeights")->Clone();
		  FirstLoadedFile = false;
		}
	      else
		{		  
		  EventCounter->Add( (TH1F*) HistoFile->Get("mt/eventCount")->Clone());
		  EventCounterWeights->Add( (TH1D*) HistoFile->Get("mt/summedWeights")->Clone());
		  HistoFile->Close();
		}	      
	    }
	  else if(line.find("/") != string::npos)
	    {
	      //std::cout<<"Changed Path to: "<<line<<std::endl;
	      path = line;
	    }
	  else
	    {
	      std::cout<<"Unrecognized Input in File!"<<std::endl;
	      std::cout<<"It is: "+line<<std::endl;
	    }	  
	}
      std::cout<<std::endl;
      std::cout<<"Done Processing Parameter File."<<std::endl;
      std::cout<<std::endl;
      //got the input chain all ready to roll,
      //1.) get an event definition in place
      //   a.) it should have all the variables necessary for input/output
      //   b.) a method for assigning them 
      //   c.) possible cuts, or a way of determining if an event is good.
      TTree* OutputTree = new TTree("mt_tree", "mt_tree");
      EventManager* TheEventManager = new EventManager();
      TheEventManager->AttachInputChainToVariables(ChannelChain);
      TheEventManager->AttachOutputTreeToVariables(OutputTree);
      long NumEntries = ChannelChain->GetEntries();
      int NumFills = 0;
      int NumFailed = 0;
      int NumDuplicates =0;
      std::cout<<"Processed Entries: "<<NumEntries<<std::endl;
      for(long i = 0; i < NumEntries; ++i)
	{	  
	  ChannelChain->GetEntry(i);
	  if(NumEntries>20)
	    {
	      if(i%(NumEntries/20)==0 ||  i==(NumEntries-1))
		{
		  fprintf(stdout,"<");
		  for(int NumEquals = 0;NumEquals < i/(NumEntries/20); NumEquals++) fprintf(stdout,"=");
		  for(int NumSpaces = 0;NumSpaces < 20-(i/(NumEntries/20));NumSpaces++) fprintf(stdout," ");
		  fprintf(stdout,">\r");
		  if(i==(NumEntries-1)) fprintf(stdout,"<====================>\n");
		}
	    }	 
	  
	  pileup_mc->Fill(TheEventManager->TheInputManager->GetInputDictionary()->nTruePU);
	  
	  if(!TheEventManager->IsGoodEvent()) 
	    {
	      ++NumFailed;
	      continue;
	    }
	  
	  //now let's put the input into the output
	  TheEventManager->TheOutputManager->TranslateInputToOutput(TheEventManager->TheInputManager);
	  
	  if(i == 0)
	    {
	      //first event. Staged simply becomes current
	      *TheEventManager->TheOutputManager->GetStagedOutputDictionary() =  *TheEventManager->TheOutputManager->GetCurrentOutputDictionary();
	    }
	  else if(TheEventManager->TheOutputManager->GetCurrentOutputDictionary()->evt == 
		  TheEventManager->TheOutputManager->GetStagedOutputDictionary()->evt)
	    {
	      ++NumDuplicates;
	      //decide what happens.
	      // cecile has a very strange way of handling this that I will just implement directly
	      // she looks at whether the current mupt is greater than the old
	      // or if if the the new muon is greater than the old minus a bit plus the tau pt is greater than the old
	      // if these things happen, then the currently considered event gets staged.
	      if(TheEventManager->TheOutputManager->GetCurrentOutputDictionary()->pt_1 > TheEventManager->TheOutputManager->GetStagedOutputDictionary()->pt_1 
		 or (TheEventManager->TheOutputManager->GetCurrentOutputDictionary()->pt_1 > TheEventManager->TheOutputManager->GetStagedOutputDictionary()->pt_1-0.00001 and 
		     TheEventManager->TheOutputManager->GetCurrentOutputDictionary()->pt_2 > TheEventManager->TheOutputManager->GetStagedOutputDictionary()->pt_2))
		{
		  *TheEventManager->TheOutputManager->GetStagedOutputDictionary() = *TheEventManager->TheOutputManager->GetCurrentOutputDictionary();
		}
	    }
	  else
	    {
	      //no other similar evt nums to compare. fill and stage the next.
	      ++NumFills;
	      OutputTree->Fill();
	      *TheEventManager->TheOutputManager->GetStagedOutputDictionary() = *TheEventManager->TheOutputManager->GetCurrentOutputDictionary();
	    }
	}
      //fill the last event we have staged
      ++NumFills;
      OutputTree->Fill();
      std::cout<<"Filled Events: "<<NumFills<<std::endl;
      std::cout<<"Failed Events: "<<NumFailed<<std::endl;
      std::cout<<"Duplicate Events: "<<NumDuplicates<<std::endl;
      std::cout<<"Writing your file"<<std::endl;
      TFile* OutFile = new TFile(OutFileName.c_str(),"RECREATE");
      std::cout<<"Tree..."<<std::endl;
      OutputTree->Write();
      std::cout<<"Event Numbers..."<<std::endl;
      EventCounter->Write();
      std::cout<<"Event Weights..."<<std::endl;
      EventCounterWeights->Write();
      std::cout<<"Pileup Histogram..."<<std::endl;
      pileup_mc->Write();
      
      std::cout<<"Closing the files..."<<std::endl;
      OutFile->Close();
      
      ParamFile.close();      
      std::cout<<"Have a nice day!"<<std::endl;
    }
  else std::cout<<"Failed To Open File!"<<std::endl;
    
}
