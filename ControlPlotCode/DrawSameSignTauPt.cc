#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawSameSignTauPt()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);
  
  TFile* ResultsFile = new TFile("ExtraControlRegions.root");
  TDirectory* SS_TauPt_dir = (TDirectory*) ResultsFile->Get("SS_TauPt");

  TH1F* data_obs_SS_TauPt = (TH1F*) SS_TauPt_dir->Get("data_obs_SS_TauPt");
  THStack* SS_TauPt_Stack = (THStack*) SS_TauPt_dir->Get("SS_TauPt_Stack");
  TLegend* SS_Legend = (TLegend*) SS_TauPt_dir->Get("TPave");

  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* SS_TauPt_StackErrors = MakeStackErrors(SS_TauPt_Stack);

  TPad* SS_TauPt_Pad = MakeRatioPlot(TheCanvas, SS_TauPt_Stack, data_obs_SS_TauPt, "m_{vis}", 0.7, 1.3);
  SS_TauPt_Pad->SetTickx();
  SS_TauPt_Pad->SetTicky();

  SS_TauPt_Stack->Draw();
  SS_TauPt_StackErrors->Draw("SAME e2");
  SS_TauPt_Stack->GetYaxis()->SetTitle("Events");
  SS_TauPt_Stack->GetYaxis()->SetTitleOffset(1.3);
  SS_TauPt_Stack->GetXaxis()->SetLabelSize(0);
  SS_TauPt_Stack->SetTitle("Same Sign Region, p_{t}^{#tau}");
  data_obs_SS_TauPt->Draw("SAME e1");
  SS_Legend->Draw();

  CMS_lumi(SS_TauPt_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("SSTauPt.png");
}
