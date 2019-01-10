#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"

void DrawPrelimCutflowPlot()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  gStyle->SetOptStat(0);

  TColor* OtherColor = new TColor((16.0+2.0)/256.0,(12.0*16.0+10.0)/256.0,(13.0*16.0+13.0)/256.0);
 
  TColor* DYColor = new TColor((4.0*16.0+4.0)/256.0,(9.0*16.0+6.0)/256.0,(12.0*16.0+8.0)/256.0);

  TFile* ResultsFile = new TFile("CecileCode/OldCutflowResults.root");

  TH1F* data_obs_Cutflow = (TH1F*) ResultsFile->Get("data_obs_Cutflow");
  TH1F* Fake_Cutflow = (TH1F*) ResultsFile->Get("data_obs_Fake_Cutflow");
  TH1F* embedded_Cutflow = (TH1F*) ResultsFile->Get("embedded_Cutflow");
  TH1F* DY_Cutflow = (TH1F*) ResultsFile->Get("DY_Cutflow");
  TH1F* DYlow_Cutflow = (TH1F*) ResultsFile->Get("DYlow_Cutflow");
  TH1F* TTToHadronic_Cutflow = (TH1F*) ResultsFile->Get("TTToHadronic_Cutflow");
  TH1F* TTTo2L2Nu_Cutflow = (TH1F*) ResultsFile->Get("TTTo2L2Nu_Cutflow");
  TH1F* TTToSemiLeptonic_Cutflow = (TH1F*) ResultsFile->Get("TTToSemiLeptonic_Cutflow");
  TH1F* WW4Q_Cutflow = (TH1F*) ResultsFile->Get("WW4Q_Cutflow");
  TH1F* WWLNuQQ_Cutflow = (TH1F*) ResultsFile->Get("WWLNuQQ_Cutflow");
  TH1F* WZ2L2Q_Cutflow = (TH1F*) ResultsFile->Get("WZ2L2Q_Cutflow");
  TH1F* WZ1L3Nu_Cutflow = (TH1F*) ResultsFile->Get("WZ1L3Nu_Cutflow");
  TH1F* WZ3LNu_Cutflow = (TH1F*) ResultsFile->Get("WZ3LNu_Cutflow");
  TH1F* WZ1L1Nu2Q_Cutflow = (TH1F*) ResultsFile->Get("WZ1L1Nu2Q_Cutflow");
  TH1F* ZZ4L_Cutflow = (TH1F*) ResultsFile->Get("ZZ4L_Cutflow");
  TH1F* ZZ2L2Nu_Cutflow = (TH1F*) ResultsFile->Get("ZZ2L2Nu_Cutflow");
  TH1F* ZZ2L2Q_Cutflow = (TH1F*) ResultsFile->Get("ZZ2L2Q_Cutflow");
  TH1F* ST_t_antitop_Cutflow = (TH1F*) ResultsFile->Get("ST_t_antitop_Cutflow");
  TH1F* ST_t_top_Cutflow = (TH1F*) ResultsFile->Get("ST_t_antitop_Cutflow");
  TH1F* ST_tW_antitop_Cutflow = (TH1F*) ResultsFile->Get("ST_tW_antitop_Cutflow");
  TH1F* ST_tW_top_Cutflow = (TH1F*) ResultsFile->Get("ST_tW_top_Cutflow");
  TH1F* ggH_htt125_Cutflow = (TH1F*) ResultsFile->Get("ggH_htt125_Cutflow");
  TH1F* qqH_htt125_Cutflow = (TH1F*) ResultsFile->Get("qqH_htt125_Cutflow");
  TH1F* WplusH125_Cutflow = (TH1F*) ResultsFile->Get("WplusH125_Cutflow");
  TH1F* WminusH125_Cutflow = (TH1F*) ResultsFile->Get("WminusH125_Cutflow");
  TH1F* ZH125_Cutflow = (TH1F*) ResultsFile->Get("ZH125_Cutflow");
  TH1F* EWKZLL_Cutflow = (TH1F*) ResultsFile->Get("EWKZLL_Cutflow");
  TH1F* EWKZNuNu_Cutflow = (TH1F*) ResultsFile->Get("EWKZNuNu_Cutflow");

  TH1F* DYAll_Cutflow = (TH1F*) DY_Cutflow->Clone();
  DYAll_Cutflow->Add(DYlow_Cutflow);

  TH1F* TT_Cutflow = (TH1F*) TTToHadronic_Cutflow->Clone();
  TT_Cutflow->Add(TTTo2L2Nu_Cutflow);
  TT_Cutflow->Add(TTToSemiLeptonic_Cutflow);

  TH1F* VV_Cutflow = (TH1F*) WW4Q_Cutflow->Clone();
  VV_Cutflow->Add(WWLNuQQ_Cutflow);
  VV_Cutflow->Add(WZ2L2Q_Cutflow);
  VV_Cutflow->Add(WZ1L3Nu_Cutflow);
  VV_Cutflow->Add(WZ3LNu_Cutflow);
  VV_Cutflow->Add(WZ1L1Nu2Q_Cutflow);
  VV_Cutflow->Add(ZZ4L_Cutflow);
  VV_Cutflow->Add(ZZ2L2Nu_Cutflow);
  VV_Cutflow->Add(ZZ4L_Cutflow);
  VV_Cutflow->Add(ZZ2L2Nu_Cutflow);
  VV_Cutflow->Add(ZZ2L2Q_Cutflow);

  TH1F* ST_Cutflow = (TH1F*) ST_t_antitop_Cutflow->Clone();
  ST_Cutflow->Add(ST_t_top_Cutflow);
  ST_Cutflow->Add(ST_tW_antitop_Cutflow);
  ST_Cutflow->Add(ST_tW_top_Cutflow);
  //handle this like we do in the other thing
  VV_Cutflow->Add(ST_Cutflow);

  TH1F* WH_Cutflow = (TH1F*) WplusH125_Cutflow->Clone();
  WH_Cutflow->Add(WminusH125_Cutflow);

  TH1F* EWK_Cutflow = (TH1F*) EWKZLL_Cutflow->Clone();
  EWK_Cutflow->Add(EWKZNuNu_Cutflow);

  TH1F* VH_Cutflow = (TH1F*) WH_Cutflow->Clone();
  VH_Cutflow->Add(ZH125_Cutflow);

  TH1F* AllHiggs_Cutflow = (TH1F*) VH_Cutflow->Clone();
  AllHiggs_Cutflow->Add(ggH_htt125_Cutflow);
  AllHiggs_Cutflow->Add(qqH_htt125_Cutflow);
  AllHiggs_Cutflow->SetNameTitle("AllHiggs_Cutflow","AllHiggs_Cutflow");
  AllHiggs_Cutflow->Scale(30);

  TH1F* Other_Cutflow = (TH1F*) VV_Cutflow->Clone();
  Other_Cutflow->Add(EWK_Cutflow);
  Other_Cutflow->Add(VH_Cutflow);
  Other_Cutflow->Add(ggH_htt125_Cutflow);
  Other_Cutflow->Add(qqH_htt125_Cutflow);

  data_obs_Cutflow->SetMarkerStyle(20);

  Fake_Cutflow->SetLineColor(kBlack);
  Fake_Cutflow->SetFillColor(606);

  embedded_Cutflow->SetLineColor(kBlack);
  embedded_Cutflow->SetFillColor(796);

  DY_Cutflow->SetLineColor(kBlack);
  DY_Cutflow->SetFillColor(DYColor->GetNumber());

  TT_Cutflow->SetLineColor(kBlack);
  TT_Cutflow->SetFillColor(592);
  
  VV_Cutflow->SetLineColor(kBlack);
  VV_Cutflow->SetFillColor(kOrange);

  ggH_htt125_Cutflow->SetLineColor(kBlack);
  ggH_htt125_Cutflow->SetFillColor(kCyan);

  qqH_htt125_Cutflow->SetLineColor(kBlack);
  qqH_htt125_Cutflow->SetFillColor(kGreen);

  WH_Cutflow->SetLineColor(kBlack);
  WH_Cutflow->SetFillColor(kPink+6);

  ZH125_Cutflow->SetLineColor(kBlack);
  ZH125_Cutflow->SetFillColor(kGreen+3);

  EWK_Cutflow->SetLineColor(kBlack);
  EWK_Cutflow->SetFillColor(kBlue-2);

  Other_Cutflow->SetLineColor(kBlack);
  Other_Cutflow->SetFillColor(OtherColor->GetNumber());

  AllHiggs_Cutflow->SetLineColor(kRed);

  THStack* Cutflow_Stack = new THStack("Cutflow_Stack","Cutflow_Stack");
  Cutflow_Stack->Add(Fake_Cutflow, "HIST");
  Cutflow_Stack->Add(embedded_Cutflow,"HIST");
  Cutflow_Stack->Add(DY_Cutflow,"HIST");
  Cutflow_Stack->Add(TT_Cutflow,"HIST");
  Cutflow_Stack->Add(Other_Cutflow,"HIST");

  TLegend* Cutflow_Legend = new TLegend(0.70,0.35,0.88,0.65);
  Cutflow_Legend->AddEntry(Other_Cutflow,"Other","f");
  Cutflow_Legend->AddEntry(TT_Cutflow,"t#bar{t}","f");
  Cutflow_Legend->AddEntry(DY_Cutflow,"Z#rightarrow ll","f");
  Cutflow_Legend->AddEntry(embedded_Cutflow,"Z#rightarrow #tau#tau", "f");
  Cutflow_Legend->AddEntry(Fake_Cutflow,"Fakes","f");
  Cutflow_Legend->AddEntry(AllHiggs_Cutflow,"All Higgs(#times 30)","l");

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

  Cutflow_Stack->SetMaximum(std::max(Cutflow_Stack->GetMaximum(),data_obs_Cutflow->GetMaximum()));  

  Cutflow_Stack->Draw();
  Cutflow_StackErrors->Draw("SAME e2");
  Cutflow_Stack->GetYaxis()->SetTitle("Events");
  Cutflow_Stack->GetYaxis()->SetTitleOffset(1.3);
  Cutflow_Stack->SetTitle("#mu#tau Channel Cutflow");
  data_obs_Cutflow->Draw("SAME e1");
  Cutflow_Legend->Draw();
  AllHiggs_Cutflow->Draw("SAME HIST");

  Cutflow_Stack->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(Cutflow_Pad,0,33);

  TheCanvas->Draw();
  TheCanvas->SaveAs("Cutflow.png");
}
