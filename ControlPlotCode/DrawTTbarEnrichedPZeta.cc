#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawTTbarEnrichedPZeta()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);

  TFile* ResultsFile = new TFile("ExtraControlRegions.root");  
  TDirectory* TTBar_PZeta_dir = (TDirectory*) ResultsFile->Get("TTBar_PZeta");
  
  TH1F* data_obs_tt_PZeta = (TH1F*) TTBar_PZeta_dir->Get("data_obs_tt_PZeta");
  THStack* TTBar_PZeta_Stack = (THStack*) TTBar_PZeta_dir->Get("TTBar_PZeta_Stack");
  TLegend* TTBar_Legend = (TLegend*) TTBar_PZeta_dir->Get("TPave");
  
  TCanvas* TheCanvas = new TCanvas("TheCanvas","TheCanvas");
  TH1F* TTBar_PZeta_StackErrors = MakeStackErrors(TTBar_PZeta_Stack);

  TPad* TTBar_PZeta_Pad = MakeRatioPlot(TheCanvas, TTBar_PZeta_Stack, data_obs_tt_PZeta, "p_{#zeta}", 0.7, 1.3);
  TTBar_PZeta_Pad->SetTickx();
  TTBar_PZeta_Pad->SetTicky();
  
  TTBar_PZeta_Stack->Draw();
  TTBar_PZeta_StackErrors->Draw("SAME e2");
  TTBar_PZeta_Stack->GetYaxis()->SetTitle("Events");
  TTBar_PZeta_Stack->GetYaxis()->SetTitleOffset(1.3);
  TTBar_PZeta_Stack->GetXaxis()->SetLabelSize(0);
  TTBar_PZeta_Stack->SetTitle("b-Tagged Region, p_{#zeta}");
  data_obs_tt_PZeta->Draw("SAME e1");
  TTBar_Legend->Draw();

  CMS_lumi(TTBar_PZeta_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("TTBarPZeta.png");
}
