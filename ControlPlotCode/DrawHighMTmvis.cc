#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawHighMTmvis()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);

  TFile* ResultsFile = new TFile("ExtraControlRegions.root");
  TDirectory* HighMT_mvis_dir = (TDirectory*) ResultsFile->Get("HighMT_mvis");
  
  TH1F* data_obs_mt_mvis = (TH1F*) HighMT_mvis_dir->Get("data_obs_mt_mvis");
  THStack* HighMT_mvis_Stack = (THStack*) HighMT_mvis_dir->Get("HighMT_mvis_Stack");
  TLegend* HighMT_Legend = (TLegend*) HighMT_mvis_dir->Get("TPave");

  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* HighMT_mvis_StackErrors = MakeStackErrors(HighMT_mvis_Stack);

  TPad* HighMT_mvis_Pad = MakeRatioPlot(TheCanvas, HighMT_mvis_Stack, data_obs_mt_mvis, "m_{vis}", 0.7, 1.3);
  HighMT_mvis_Pad->SetTickx();
  HighMT_mvis_Pad->SetTicky();
  
  HighMT_mvis_Stack->Draw();
  HighMT_mvis_StackErrors->Draw("SAME e2");
  HighMT_mvis_Stack->GetYaxis()->SetTitle("Events");
  HighMT_mvis_Stack->GetYaxis()->SetTitleOffset(1.3);
  HighMT_mvis_Stack->GetXaxis()->SetLabelSize(0);
  HighMT_mvis_Stack->SetTitle("High m_{t} Region, m_{vis}");
  data_obs_mt_mvis->Draw("SAME e1");
  HighMT_Legend->Draw();

  CMS_lumi(HighMT_mvis_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("HighMTmvis.png");
}
