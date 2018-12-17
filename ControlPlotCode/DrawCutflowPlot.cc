#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawCutflowPlot()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);

  TFile* ResultsFile = new TFile("CutflowPlots.root");

  TH1F* data_obs_Cutflow = (TH1F*) ResultsFile->Get("data_obs_Cutflow");
  THStack* Cutflow_Stack = (THStack*) ResultsFile->Get("Cutflow_Stack");
  TLegend* Cutflow_Legend = (TLegend*) ResultsFile->Get("TPave");

  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* Cutflow_StackErrors = MakeStackErrors(Cutflow_Stack);

  TPad* Cutflow_Pad = MakeRatioPlot(TheCanvas, Cutflow_Stack, data_obs_Cutflow, "", 0.7, 1.3);
  Cutflow_Pad->SetTickx();
  Cutflow_Pad->SetTicky();
  
  //set up the the custom alphanumeric bin labels
  TPad* RatioPad = (TPad*) TheCanvas->FindObject("pad2");
  TH1F* RatioHist = (TH1F*) RatioPad->FindObject("FinalRatio");
  
  RatioHist->GetXaxis()->SetBinLabel(1,"Skim Cuts");
  RatioHist->GetXaxis()->SetBinLabel(2,"Basic Eta Requirements");
  RatioHist->GetXaxis()->SetBinLabel(3,"Trigger pt,eta Requirements");
  RatioHist->GetXaxis()->SetBinLabel(4,"Antilepton Vetoes");
  RatioHist->GetXaxis()->SetBinLabel(5,"b-tag Veto");
  RatioHist->GetXaxis()->SetBinLabel(6,"Additional Tau Requirements");
  RatioHist->GetXaxis()->SetBinLabel(7,"Opposite Sign Selection");
  RatioHist->GetXaxis()->SetBinLabel(8,"Transverse Mass Cut");
  RatioHist->GetXaxis()->SetBinLabel(9,"Isolation");

  Cutflow_Stack->Draw();
  Cutflow_StackErrors->Draw("SAME e2");
  Cutflow_Stack->GetYaxis()->SetTitle("Events");
  Cutflow_Stack->GetYaxis()->SetTitleOffset(1.3);
  Cutflow_Stack->SetTitle("#mu#tau Channel Cutflow");
  data_obs_Cutflow->Draw("SAME e1");
  Cutflow_Legend->Draw();

  CMS_lumi(Cutflow_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("Cutflow.png");
}
