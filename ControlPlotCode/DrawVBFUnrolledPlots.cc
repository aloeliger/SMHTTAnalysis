#include "TROOT.h"
#include <string>
#include <vector>
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawVBFUnrolledPlots()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* ResultsFile = new TFile("UnrolledHistograms.root");

  //Zero Jet Category Drawing

  TDirectory* VBFDirectory = (TDirectory*)ResultsFile->Get("mt_vbf");
  THStack* VBFStack = (THStack*) VBFDirectory->Get("VBFBackgroundStack");
  TH1F* VBFData = (TH1F*)VBFDirectory->Get("data_obs");
  TH1F* VBF_HiggsUpscaled = (TH1F*)VBFDirectory->Get("Higgs_Upscale");
  TLegend* VBFLegend = (TLegend*) VBFDirectory->Get("TPave");

  TCanvas* CanvasOne = new TCanvas("VBFCanvas","VBFCanvas");  
  //CanvasOne->SetTickx();
  //CanvasOne->SetTicky();
  gStyle->SetGridStyle(0);
  gStyle->SetGridColor(kBlack);
  gStyle->SetOptStat(0);

  TH1F* VBFStackErrors = MakeStackErrors(VBFStack);

  TPad* VBFPad = MakeRatioPlot(CanvasOne, VBFStack, VBFData,"m_{vis}",0.7,1.3);
  VBFPad->SetTickx();
  VBFPad->SetTicky();
  VBFPad->SetGridx();    
  VBFPad->SetLogy();

  //color corrections
  TColor* DYColor = new TColor((4.0*16.0+4.0)/256.0,(9.0*16.0+6.0)/256.0,(12.0*16.0+8.0)/256.0);
  TColor* OtherColor = new TColor((16.0+2.0)/256.0,(12.0*16.0+10.0)/256.0,(13.0*16.0+13.0)/256.0);
  ((TH1F*)VBFStack->GetHists()->FindObject("ZL"))->SetFillColor(DYColor->GetNumber());
  ((TH1F*)VBFStack->GetHists()->FindObject("Other"))->SetFillColor(OtherColor->GetNumber());

  VBFStack->Draw();
  VBFStackErrors->Draw("SAME e2");    
  VBFStack->GetYaxis()->SetTitle("Events/20 GeV");
  VBFStack->GetYaxis()->SetTitleOffset(1.3);
  VBFStack->SetTitle("VBF m_{vis}");
  //resize the ridiculous log plot
  VBFStack->SetMaximum(8000);
  VBFData->Draw("SAME e1");
  VBF_HiggsUpscaled->Draw("SAME HIST");
  VBFLegend->Draw();

  CMS_lumi(VBFPad,0,33);    

  //Splitting grid lines
  int numCategories = 5;
  VBFStack->GetXaxis()->SetNdivisions(-500-numCategories);  

  //Set up the labels
  VBFStack->GetXaxis()->SetLabelSize(0.0);
  //if(CanvasOne->FindObject("pad2")!= NULL) std::cout<<"Found it!"<<std::endl;	
  TPad* RatioPad = (TPad*) CanvasOne->FindObject("pad2");
  TH1F* RatioHist = (TH1F*) RatioPad->FindObject("FinalRatio");
  //generate the bin labels
  int NumBinsInPlot = VBFData->GetNbinsX()/numCategories;
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
	  //std::cout<<"Setting Label #"<<(NumBinsInPlot*(i-1))+j<<" to "<<BinLabels[j-1].c_str()<<std::endl;
	  RatioHist->GetXaxis()->SetBinLabel((NumBinsInPlot*(i-1))+j,BinLabels[j-1].c_str());
	}
    }

  RatioHist->GetXaxis()->SetTitleOffset(1.4);
  RatioPad->SetMargin(0.1,1.0,0.5,1.0);

  VBFPad->cd();  

  //setup the custom slice labels
  TLatex latex;
  latex.SetTextSize(0.037);
  latex.SetTextAlign(13);
  latex.DrawLatex(1.0,10000.0, "0 #leq m_{jj} #leq 300");
  latex.DrawLatex(5.0,10000.0,"300 #leq m_{jj} #leq 700");
  latex.DrawLatex(10.0,10000.0,"700 #leq m_{jj} #leq 1100");
  latex.DrawLatex(15.0,10000.0,"1100 #leq m_{jj} #leq 1500");
  latex.DrawLatex(20.0,1000.0,"1500 #leq m_{jj}");
  

  CanvasOne->Draw();
  CanvasOne->SaveAs("VBFUnrolled.png");
   
}
