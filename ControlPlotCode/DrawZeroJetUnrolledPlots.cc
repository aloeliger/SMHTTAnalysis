#include "TROOT.h"
#include <string>
#include <vector>
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawZeroJetUnrolledPlots()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* ResultsFile = new TFile("UnrolledHistograms.root");

  //Zero Jet Category Drawing

  TDirectory* ZeroJetDirectory = (TDirectory*)ResultsFile->Get("mt_0jet");
  THStack* ZeroJetStack = (THStack*) ZeroJetDirectory->Get("ZeroJetBackgroundStack");
  TH1F* ZeroJetData = (TH1F*)ZeroJetDirectory->Get("data_obs");
  TH1F* ZeroJet_HiggsUpscale = (TH1F*)ZeroJetDirectory->Get("Higgs_Upscale");
  TLegend* ZeroJetLegend = (TLegend*) ZeroJetDirectory->Get("TPave");

  TCanvas* CanvasOne = new TCanvas("ZeroJetCanvas","ZeroJetCanvas");  
  //CanvasOne->SetTickx();
  //CanvasOne->SetTicky();
  gStyle->SetGridStyle(0);
  gStyle->SetGridColor(kBlack);
  gStyle->SetOptStat(0);

  TH1F* ZeroJetStackErrors = MakeStackErrors(ZeroJetStack);

  TPad* ZeroJetPad = MakeRatioPlot(CanvasOne, ZeroJetStack, ZeroJetData,"m_{vis}",0.7,1.3);
  ZeroJetPad->SetTickx();
  ZeroJetPad->SetTicky();
  ZeroJetPad->SetGridx();  

  ZeroJetStack->Draw();
  ZeroJetStackErrors->Draw("SAME e2");    
  ZeroJetStack->GetYaxis()->SetTitle("Events/5 GeV");
  ZeroJetStack->GetYaxis()->SetTitleOffset(1.3);
  ZeroJetStack->SetTitle("0 Jet m_{vis}");
  ZeroJetData->Draw("SAME e1");
  ZeroJet_HiggsUpscale->Draw("SAME HIST");
  ZeroJetLegend->Draw();

  CMS_lumi(ZeroJetPad,0,33);    

  //Splitting grid lines
  int numCategories = 4;
  ZeroJetStack->GetXaxis()->SetNdivisions(-500-numCategories);  

  //Set up the labels
  ZeroJetStack->GetXaxis()->SetLabelSize(0.0);
  //if(CanvasOne->FindObject("pad2")!= NULL) std::cout<<"Found it!"<<std::endl;
  TPad* RatioPad = (TPad*) CanvasOne->FindObject("pad2");
  TH1F* RatioHist = (TH1F*) RatioPad->FindObject("FinalRatio");
  //generate the bin labels
  int NumBinsInPlot = ZeroJetData->GetNbinsX()/numCategories;
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
  //RatioPad->SetTopMargin(1.5);
  //RatioPad->SetBottomMargin(0.55);

  ZeroJetPad->cd();

  //setup the custom slice labels
  TLatex latex;
  latex.SetTextSize(0.025);
  latex.SetTextAlign(13);
  latex.DrawLatex(5.0,9000.0,"30.0 #leq #tau_{p_{t}} #leq 35.0");
  latex.DrawLatex(20.0,9000.0,"35.0 #leq #tau_{p_{t}} #leq 40.0");
  latex.DrawLatex(40.0,9000.0,"40.0 #leq #tau_{p_{t}} #leq 50.0");
  latex.DrawLatex(60.0,7000.0,"50.0 #leq #tau_{p_{t}}");

  CanvasOne->Draw();
  CanvasOne->SaveAs("ZeroJetUnrolled.png");
  
  
}
