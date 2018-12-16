#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawSameSignmvis()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);
  
  TFile* ResultsFile = new TFile("ExtraControlRegions.root");
  TDirectory* SS_mvis_dir = (TDirectory*) ResultsFile->Get("SS_mvis");

  TH1F* data_obs_SS_mvis = (TH1F*) SS_mvis_dir->Get("data_obs_SS_mvis");
  THStack* SS_mvis_Stack = (THStack*) SS_mvis_dir->Get("SS_mvis_Stack");
  TLegend* SS_Legend = (TLegend*) SS_mvis_dir->Get("TPave");

  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* SS_mvis_StackErrors = MakeStackErrors(SS_mvis_Stack);

  TPad* SS_mvis_Pad = MakeRatioPlot(TheCanvas, SS_mvis_Stack, data_obs_SS_mvis, "m_{vis}", 0.7, 1.3);
  SS_mvis_Pad->SetTickx();
  SS_mvis_Pad->SetTicky();

  SS_mvis_Stack->Draw();
  SS_mvis_StackErrors->Draw("SAME e2");
  SS_mvis_Stack->GetYaxis()->SetTitle("Events");
  SS_mvis_Stack->GetYaxis()->SetTitleOffset(1.3);
  SS_mvis_Stack->GetXaxis()->SetLabelSize(0);
  SS_mvis_Stack->SetTitle("Same Sign Region, m_{vis}");
  data_obs_SS_mvis->Draw("SAME e1");
  SS_Legend->Draw();

  CMS_lumi(SS_mvis_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("SSmvis.png");
}
