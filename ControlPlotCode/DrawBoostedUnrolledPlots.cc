#include "TROOT.h"
#include <string>
#include <vector>
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawBoostedUnrolledPlots()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* ResultsFile = new TFile("UnrolledHistograms.root");

  TDirectory* BoostedDirectory = (TDirectory*)ResultsFile->Get("mt_boosted");
  THStack* BoostedStack = (THStack*) BoostedDirectory->Get("BoostedBackgroundStack");
  TH1F* BoostedData = (TH1F*)BoostedDirectory->Get("data_obs");
  TH1F* Boosted_HiggsUpscale = (TH1F*)BoostedDirectory->Get("Higgs_Upscale");
  TLegend* BoostedLegend = (TLegend*) BoostedDirectory->Get("TPave");

  TCanvas* CanvasOne = new TCanvas("BoostedCanvas","BoostedCanvas");  
  //CanvasOne->SetTickx();
  //CanvasOne->SetTicky();
  gStyle->SetGridStyle(0);
  gStyle->SetGridColor(kBlack);
  gStyle->SetOptStat(0);

  TH1F* BoostedStackErrors = MakeStackErrors(BoostedStack);

  TPad* BoostedPad = MakeRatioPlot(CanvasOne, BoostedStack, BoostedData,"m_{vis}",0.7,1.3);
  BoostedPad->SetTickx();
  BoostedPad->SetTicky();
  BoostedPad->SetGridx();  

  BoostedStack->Draw();
  BoostedStackErrors->Draw("SAME e2");    
  BoostedStack->GetYaxis()->SetTitle("Events/5 GeV");
  BoostedStack->GetYaxis()->SetTitleOffset(1.3);
  BoostedStack->SetTitle("Boosted m_{vis}");
  //resize the log plot
  BoostedStack->SetMaximum(10000);
  BoostedData->Draw("SAME e1");
  Boosted_HiggsUpscale->Draw("SAME HIST");
  BoostedLegend->Draw();

  CMS_lumi(BoostedPad,0,33);    

  //Splitting grid lines
  int numCategories = 6;
  BoostedStack->GetXaxis()->SetNdivisions(-500-numCategories);  

  //Set up the labels
  BoostedStack->GetXaxis()->SetLabelSize(0.0);
  //if(CanvasOne->FindObject("pad2")!= NULL) std::cout<<"Found it!"<<std::endl;
  TPad* RatioPad = (TPad*) CanvasOne->FindObject("pad2");
  TH1F* RatioHist = (TH1F*) RatioPad->FindObject("FinalRatio");
  //generate the bin labels
  int NumBinsInPlot = BoostedData->GetNbinsX()/numCategories;
  std::vector<string> BinLabels;  
  Float_t UpperEnd = 150.0;
  Float_t LowerEnd = 50.0;
  Float_t Difference = UpperEnd-LowerEnd;
  Float_t Increment = Difference/((float)NumBinsInPlot);
  for(int j = 1; j<= NumBinsInPlot; ++j)
    {
      string LowEndString = std::to_string(LowerEnd+(j-1)*Increment);
      string HighEndString = std::to_string(LowerEnd+j*Increment);
      LowEndString.erase(LowEndString.find_last_not_of('0'),std::string::npos);
      HighEndString.erase(HighEndString.find_last_not_of('0'),std::string::npos);
      string TheLabel = (LowEndString
			 +"-"
			 +HighEndString);
      //std::cout<<TheLabel<<std::endl;
      BinLabels.push_back(TheLabel);
    }  
  for(int i = 1; i<= numCategories; ++i)
    {
      for(int j = 1; j<= NumBinsInPlot; ++j)
	{
	  //std::cout<<"Setting Label #"<<(20*(i-1))+j<<" to "<<BinLabels[j-1].c_str()<<std::endl;
	  RatioHist->GetXaxis()->SetBinLabel((20*(i-1))+j,BinLabels[j-1].c_str());
	}
    }

  RatioHist->GetXaxis()->SetTitleOffset(1.4);
  RatioPad->SetMargin(0.1,1.0,0.5,1.0);

  BoostedPad->cd();
  BoostedPad->SetLogy();

  //setup the custom slice labels
  TLatex latex;
  latex.SetTextSize(0.025);
  latex.SetTextAlign(13);
  latex.DrawLatex(5.0,10000.0,"0 #leq p_{t}^{#mu#tau} #leq 100");
  latex.DrawLatex(20.0,10000.0,"100 #leq p_{t}^{#mu#tau} #leq 150");
  latex.DrawLatex(40.0,10000.0,"150 #leq p_{t}^{#mu#tau} #leq 200");
  latex.DrawLatex(60.0,10000.0,"200 #leq p_{t}^{#mu#tau} #leq 250");  
  latex.DrawLatex(80.0,10000.0,"250 #leq p_{t}^{#mu#tau} #leq 300");
  latex.DrawLatex(100.0,2000.0,"300 #leq p_{t}^{#mu#tau}");

  CanvasOne->Draw();
  CanvasOne->SaveAs("BoostedUnrolled.png");
}
