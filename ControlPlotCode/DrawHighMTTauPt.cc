#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawHighMTTauPt()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);

  TFile* ResultsFile = new TFile("ExtraControlRegions.root");
  TDirectory* HighMT_TauPt_dir = (TDirectory*) ResultsFile->Get("HighMT_TauPt");
  
  TH1F* data_obs_mt_TauPt = (TH1F*) HighMT_TauPt_dir->Get("data_obs_mt_TauPt");
  THStack* HighMT_TauPt_Stack = (THStack*) HighMT_TauPt_dir->Get("HighMT_TauPt_Stack");
  TLegend* HighMT_Legend = (TLegend*) HighMT_TauPt_dir->Get("TPave");

  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* HighMT_TauPt_StackErrors = MakeStackErrors(HighMT_TauPt_Stack);

  TPad* HighMT_TauPt_Pad = MakeRatioPlot(TheCanvas, HighMT_TauPt_Stack, data_obs_mt_TauPt, "p_{t}^{#tau}", 0.7, 1.3);
  HighMT_TauPt_Pad->SetTickx();
  HighMT_TauPt_Pad->SetTicky();
  
  HighMT_TauPt_Stack->Draw();
  HighMT_TauPt_StackErrors->Draw("SAME e2");
  HighMT_TauPt_Stack->GetYaxis()->SetTitle("Events");
  HighMT_TauPt_Stack->GetYaxis()->SetTitleOffset(1.3);
  HighMT_TauPt_Stack->GetXaxis()->SetLabelSize(0);
  HighMT_TauPt_Stack->SetTitle("High m_{t} Region, p_{t}^{#tau}");
  data_obs_mt_TauPt->Draw("SAME e1");
  HighMT_Legend->Draw();

  CMS_lumi(HighMT_TauPt_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("HighMTTauPt.png");
}
