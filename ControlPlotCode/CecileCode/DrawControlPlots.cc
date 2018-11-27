#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"

void DrawControlPlots()
{
  setTDRStyle();

  writeExtraText=true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* HistoFile = new TFile("ControlFile.root","READ");

  /*

  TCanvas* CanvasOne = new TCanvas("CanvasOne","MuPt",550,550);
  CanvasOne->SetTickx();
  CanvasOne->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_MuPt = (TH1F*) HistoFile->Get("data_obs_MuPt");
  TH1F* data_obs_Fake_MuPt = (TH1F*) HistoFile->Get("data_obs_Fake_MuPt");
  TH1F* embedded_MuPt = (TH1F*) HistoFile->Get("embedded_MuPt");
  TH1F* DY_MuPt = (TH1F*) HistoFile->Get("DY_MuPt");
  TH1F* DYlow_MuPt = (TH1F*) HistoFile->Get("DYlow_MuPt");
  TH1F* TTToHadronic_MuPt = (TH1F*) HistoFile->Get("TTToHadronic_MuPt");
  TH1F* TTTo2L2Nu_MuPt = (TH1F*) HistoFile->Get("TTTo2L2Nu_MuPt");
  TH1F* TTToSemiLeptonic_MuPt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_MuPt");
  TH1F* WW4Q_MuPt = (TH1F*) HistoFile->Get("WW4Q_MuPt");
  TH1F* WWLNuQQ_MuPt = (TH1F*) HistoFile->Get("WWLNuQQ_MuPt");
  TH1F* WZ2L2Q_MuPt = (TH1F*) HistoFile->Get("WZ2L2Q_MuPt");
  TH1F* WZ1L3Nu_MuPt = (TH1F*) HistoFile->Get("WZ1L3Nu_MuPt");
  TH1F* WZ3LNu_MuPt = (TH1F*) HistoFile->Get("WZ3LNu_MuPt");
  TH1F* WZ1L1Nu2Q_MuPt = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_MuPt");
  TH1F* ZZ4L_MuPt = (TH1F*) HistoFile->Get("ZZ4L_MuPt");
  TH1F* ZZ2L2Nu_MuPt = (TH1F*) HistoFile->Get("ZZ2L2Nu_MuPt");
  TH1F* ZZ2L2Q_MuPt = (TH1F*) HistoFile->Get("ZZ2L2Q_MuPt");
  TH1F* ST_t_antitop_MuPt = (TH1F*) HistoFile->Get("ST_t_antitop_MuPt");
  TH1F* ST_t_top_MuPt = (TH1F*) HistoFile->Get("ST_t_top_MuPt");
  TH1F* ST_tW_antitop_MuPt = (TH1F*) HistoFile->Get("ST_tW_antitop_MuPt");
  TH1F* ST_tW_top_MuPt = (TH1F*) HistoFile->Get("ST_tW_top_MuPt");
  TH1F* ggH_htt125_MuPt = (TH1F*) HistoFile->Get("ggH_htt125_MuPt");
  TH1F* qqH_htt125_MuPt = (TH1F*) HistoFile->Get("qqH_htt125_MuPt");  
  TH1F* WplusH125_MuPt = (TH1F*) HistoFile->Get("WplusH125_MuPt");
  TH1F* WminusH125_MuPt = (TH1F*) HistoFile->Get("WminusH125_MuPt");
  TH1F* ZH125_MuPt = (TH1F*) HistoFile->Get("ZH125_MuPt");
  TH1F* EWKZLL_MuPt = (TH1F*) HistoFile->Get("EWKZLL_MuPt");
  TH1F* EWKZNuNu_MuPt = (TH1F*) HistoFile->Get("EWKZNuNu_MuPt");

  TH1F* DYFinal_MuPt = (TH1F*) DY_MuPt->Clone();
  DYFinal_MuPt->Add(DYlow_MuPt);
  
  TH1F* TTFinal_MuPt = (TH1F*) TTToHadronic_MuPt->Clone();
  TTFinal_MuPt->Add(TTTo2L2Nu_MuPt);
  TTFinal_MuPt->Add(TTToSemiLeptonic_MuPt);
  
  TH1F* VVFinal_MuPt = (TH1F*) WW4Q_MuPt->Clone();
  VVFinal_MuPt->Add(WWLNuQQ_MuPt);
  VVFinal_MuPt->Add(WZ2L2Q_MuPt);
  VVFinal_MuPt->Add(WZ1L3Nu_MuPt);
  VVFinal_MuPt->Add(WZ3LNu_MuPt);
  VVFinal_MuPt->Add(WZ1L1Nu2Q_MuPt);
  VVFinal_MuPt->Add(ZZ4L_MuPt);
  VVFinal_MuPt->Add(ZZ2L2Nu_MuPt);
  VVFinal_MuPt->Add(ZZ2L2Q_MuPt);
  
  TH1F* STFinal_MuPt = (TH1F*) ST_t_antitop_MuPt->Clone();
  STFinal_MuPt->Add(ST_t_top_MuPt);
  STFinal_MuPt->Add(ST_tW_antitop_MuPt);
  STFinal_MuPt->Add(ST_tW_top_MuPt);

  TH1F* VHFinal_MuPt = (TH1F*) WplusH125_MuPt->Clone();
  VHFinal_MuPt->Add(WminusH125_MuPt);
  VHFinal_MuPt->Add(ZH125_MuPt);

  TH1F* EWKFinal_MuPt = (TH1F*) EWKZLL_MuPt->Clone();
  EWKFinal_MuPt->Add(EWKZNuNu_MuPt);

  data_obs_MuPt->SetMarkerStyle(20);
  data_obs_MuPt->Sumw2();
  
  data_obs_Fake_MuPt->SetFillColor(kRed);
  data_obs_Fake_MuPt->SetLineColor(kBlack);

  embedded_MuPt->SetFillColor(kYellow);
  embedded_MuPt->SetLineColor(kBlack);

  DYFinal_MuPt->SetFillColor(kBlue);
  DYFinal_MuPt->SetLineColor(kBlack);

  TTFinal_MuPt->SetFillColor(kViolet-3);
  TTFinal_MuPt->SetLineColor(kBlack);

  VVFinal_MuPt->SetFillColor(kPink-3);
  VVFinal_MuPt->SetLineColor(kBlack);

  STFinal_MuPt->SetFillColor(kGreen);
  STFinal_MuPt->SetLineColor(kBlack);

  qqH_htt125_MuPt->SetFillColor(kCyan);
  qqH_htt125_MuPt->SetLineColor(kBlack);

  ggH_htt125_MuPt->SetFillColor(kCyan);
  ggH_htt125_MuPt->SetLineColor(kBlack);

  VHFinal_MuPt->SetFillColor(kOrange);
  VHFinal_MuPt->SetLineColor(kBlack);

  EWKFinal_MuPt->SetFillColor(kBlue-2);
  EWKFinal_MuPt->SetLineColor(kBlack);
  
  THStack* BackgroundStack_MuPt = new THStack("BackgroundStack_MuPt","BackgroundStack_MuPt");
  BackgroundStack_MuPt->Add(data_obs_Fake_MuPt,"hist");
  BackgroundStack_MuPt->Add(DYFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(embedded_MuPt,"hist");
  BackgroundStack_MuPt->Add(TTFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(VVFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(STFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(qqH_htt125_MuPt,"hist");
  BackgroundStack_MuPt->Add(ggH_htt125_MuPt,"hist");
  BackgroundStack_MuPt->Add(VHFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(EWKFinal_MuPt,"hist");

  TH1F* BackgroundStack_MuPt_Errors = MakeStackErrors(BackgroundStack_MuPt);

  TPad* PlotPad_MuPt = MakeRatioPlot(CanvasOne, BackgroundStack_MuPt, data_obs_MuPt,"#mu Pt");

  BackgroundStack_MuPt->SetMaximum(max(BackgroundStack_MuPt->GetMaximum(),data_obs_MuPt->GetMaximum()));

  BackgroundStack_MuPt->Draw();
  BackgroundStack_MuPt_Errors->Draw("SAME e2");
  BackgroundStack_MuPt->SetTitle("#mu Pt");
  data_obs_MuPt->Draw("SAME e1");
  BackgroundStack_MuPt->GetYaxis()->SetTitle("Events");
  BackgroundStack_MuPt->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_MuPt,0,33);

  TLegend* Legend_MuPt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_MuPt->AddEntry(embedded_MuPt,"embedded","f");
  Legend_MuPt->AddEntry(DYFinal_MuPt, "Other DY","f");
  Legend_MuPt->AddEntry(TTFinal_MuPt,"t#bar{t}","f");
  Legend_MuPt->AddEntry(VVFinal_MuPt,"Dibsoson","f");
  Legend_MuPt->AddEntry(STFinal_MuPt,"Single Top","f");
  Legend_MuPt->AddEntry(qqH_htt125_MuPt,"qqh","f");
  Legend_MuPt->AddEntry(ggH_htt125_MuPt,"ggH","f");
  Legend_MuPt->AddEntry(VHFinal_MuPt,"VH","f");
  Legend_MuPt->AddEntry(EWKFinal_MuPt,"EWK","f");
  Legend_MuPt->AddEntry(data_obs_Fake_MuPt,"Fakes","f");

  Legend_MuPt->Draw();

  //tau pt plot

  TCanvas* CanvasTwo = new TCanvas("CanvasTwo","TauPt",550,550);
  CanvasTwo->SetTickx();
  CanvasTwo->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_TauPt = (TH1F*) HistoFile->Get("data_obs_TauPt");
  TH1F* data_obs_Fake_TauPt = (TH1F*) HistoFile->Get("data_obs_Fake_TauPt");
  TH1F* embedded_TauPt = (TH1F*) HistoFile->Get("embedded_TauPt");
  TH1F* DY_TauPt = (TH1F*) HistoFile->Get("DY_TauPt");
  TH1F* DYlow_TauPt = (TH1F*) HistoFile->Get("DYlow_TauPt");
  TH1F* TTToHadronic_TauPt = (TH1F*) HistoFile->Get("TTToHadronic_TauPt");
  TH1F* TTTo2L2Nu_TauPt = (TH1F*) HistoFile->Get("TTTo2L2Nu_TauPt");
  TH1F* TTToSemiLeptonic_TauPt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_TauPt");
  TH1F* WW4Q_TauPt = (TH1F*) HistoFile->Get("WW4Q_TauPt");
  TH1F* WWLNuQQ_TauPt = (TH1F*) HistoFile->Get("WWLNuQQ_TauPt");
  TH1F* WZ2L2Q_TauPt = (TH1F*) HistoFile->Get("WZ2L2Q_TauPt");
  TH1F* WZ1L3Nu_TauPt = (TH1F*) HistoFile->Get("WZ1L3Nu_TauPt");
  TH1F* WZ3LNu_TauPt = (TH1F*) HistoFile->Get("WZ3LNu_TauPt");
  TH1F* WZ1L1Nu2Q_TauPt = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_TauPt");
  TH1F* ZZ4L_TauPt = (TH1F*) HistoFile->Get("ZZ4L_TauPt");
  TH1F* ZZ2L2Nu_TauPt = (TH1F*) HistoFile->Get("ZZ2L2Nu_TauPt");
  TH1F* ZZ2L2Q_TauPt = (TH1F*) HistoFile->Get("ZZ2L2Q_TauPt");
  TH1F* ST_t_antitop_TauPt = (TH1F*) HistoFile->Get("ST_t_antitop_TauPt");
  TH1F* ST_t_top_TauPt = (TH1F*) HistoFile->Get("ST_t_top_TauPt");
  TH1F* ST_tW_antitop_TauPt = (TH1F*) HistoFile->Get("ST_tW_antitop_TauPt");
  TH1F* ST_tW_top_TauPt = (TH1F*) HistoFile->Get("ST_tW_top_TauPt");
  TH1F* ggH_htt125_TauPt = (TH1F*) HistoFile->Get("ggH_htt125_TauPt");
  TH1F* qqH_htt125_TauPt = (TH1F*) HistoFile->Get("qqH_htt125_TauPt");  
  TH1F* WplusH125_TauPt = (TH1F*) HistoFile->Get("WplusH125_TauPt");
  TH1F* WminusH125_TauPt = (TH1F*) HistoFile->Get("WminusH125_TauPt");
  TH1F* ZH125_TauPt = (TH1F*) HistoFile->Get("ZH125_TauPt");
  TH1F* EWKZLL_TauPt = (TH1F*) HistoFile->Get("EWKZLL_TauPt");
  TH1F* EWKZNuNu_TauPt = (TH1F*) HistoFile->Get("EWKZNuNu_TauPt");

  TH1F* DYFinal_TauPt = (TH1F*) DY_TauPt->Clone();
  DYFinal_TauPt->Add(DYlow_TauPt);
  
  TH1F* TTFinal_TauPt = (TH1F*) TTToHadronic_TauPt->Clone();
  TTFinal_TauPt->Add(TTTo2L2Nu_TauPt);
  TTFinal_TauPt->Add(TTToSemiLeptonic_TauPt);
  
  TH1F* VVFinal_TauPt = (TH1F*) WW4Q_TauPt->Clone();
  VVFinal_TauPt->Add(WWLNuQQ_TauPt);
  VVFinal_TauPt->Add(WZ2L2Q_TauPt);
  VVFinal_TauPt->Add(WZ1L3Nu_TauPt);
  VVFinal_TauPt->Add(WZ3LNu_TauPt);
  VVFinal_TauPt->Add(WZ1L1Nu2Q_TauPt);
  VVFinal_TauPt->Add(ZZ4L_TauPt);
  VVFinal_TauPt->Add(ZZ2L2Nu_TauPt);
  VVFinal_TauPt->Add(ZZ2L2Q_TauPt);
  
  TH1F* STFinal_TauPt = (TH1F*) ST_t_antitop_TauPt->Clone();
  STFinal_TauPt->Add(ST_t_top_TauPt);
  STFinal_TauPt->Add(ST_tW_antitop_TauPt);
  STFinal_TauPt->Add(ST_tW_top_TauPt);

  TH1F* VHFinal_TauPt = (TH1F*) WplusH125_TauPt->Clone();
  VHFinal_TauPt->Add(WminusH125_TauPt);
  VHFinal_TauPt->Add(ZH125_TauPt);

  TH1F* EWKFinal_TauPt = (TH1F*) EWKZLL_TauPt->Clone();
  EWKFinal_TauPt->Add(EWKZNuNu_TauPt);

  data_obs_TauPt->SetMarkerStyle(20);
  data_obs_TauPt->Sumw2();
  
  data_obs_Fake_TauPt->SetFillColor(kRed);
  data_obs_Fake_TauPt->SetLineColor(kBlack);

  embedded_TauPt->SetFillColor(kYellow);
  embedded_TauPt->SetLineColor(kBlack);

  DYFinal_TauPt->SetFillColor(kBlue);
  DYFinal_TauPt->SetLineColor(kBlack);

  TTFinal_TauPt->SetFillColor(kViolet-3);
  TTFinal_TauPt->SetLineColor(kBlack);

  VVFinal_TauPt->SetFillColor(kPink-3);
  VVFinal_TauPt->SetLineColor(kBlack);

  STFinal_TauPt->SetFillColor(kGreen);
  STFinal_TauPt->SetLineColor(kBlack);

  qqH_htt125_TauPt->SetFillColor(kCyan);
  qqH_htt125_TauPt->SetLineColor(kBlack);

  ggH_htt125_TauPt->SetFillColor(kCyan);
  ggH_htt125_TauPt->SetLineColor(kBlack);

  VHFinal_TauPt->SetFillColor(kOrange);
  VHFinal_TauPt->SetLineColor(kBlack);

  EWKFinal_TauPt->SetFillColor(kBlue-2);
  EWKFinal_TauPt->SetLineColor(kBlack);
  
  THStack* BackgroundStack_TauPt = new THStack("BackgroundStack_TauPt","BackgroundStack_TauPt");
  BackgroundStack_TauPt->Add(data_obs_Fake_TauPt,"hist");
  BackgroundStack_TauPt->Add(DYFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(embedded_TauPt,"hist");
  BackgroundStack_TauPt->Add(TTFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(VVFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(STFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(qqH_htt125_TauPt,"hist");
  BackgroundStack_TauPt->Add(ggH_htt125_TauPt,"hist");
  BackgroundStack_TauPt->Add(VHFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(EWKFinal_TauPt,"hist");

  TH1F* BackgroundStack_TauPt_Errors = MakeStackErrors(BackgroundStack_TauPt);

  TPad* PlotPad_TauPt = MakeRatioPlot(CanvasTwo, BackgroundStack_TauPt, data_obs_TauPt,"#tau Pt");

  BackgroundStack_TauPt->SetMaximum(max(BackgroundStack_TauPt->GetMaximum(),data_obs_TauPt->GetMaximum()));

  BackgroundStack_TauPt->Draw();
  BackgroundStack_TauPt_Errors->Draw("SAME e2");
  BackgroundStack_TauPt->SetTitle("#tau Pt");
  data_obs_TauPt->Draw("SAME e1");
  BackgroundStack_TauPt->GetYaxis()->SetTitle("Events");
  BackgroundStack_TauPt->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_TauPt,0,33);

  TLegend* Legend_TauPt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_TauPt->AddEntry(embedded_TauPt,"embedded","f");
  Legend_TauPt->AddEntry(DYFinal_TauPt, "Other DY","f");
  Legend_TauPt->AddEntry(TTFinal_TauPt,"t#bar{t}","f");
  Legend_TauPt->AddEntry(VVFinal_TauPt,"Dibsoson","f");
  Legend_TauPt->AddEntry(STFinal_TauPt,"Single Top","f");
  Legend_TauPt->AddEntry(qqH_htt125_TauPt,"qqh","f");
  Legend_TauPt->AddEntry(ggH_htt125_TauPt,"ggH","f");
  Legend_TauPt->AddEntry(VHFinal_TauPt,"VH","f");
  Legend_TauPt->AddEntry(EWKFinal_TauPt,"EWK","f");
  Legend_TauPt->AddEntry(data_obs_Fake_TauPt,"Fakes","f");

  Legend_TauPt->Draw();
  
  //Mu Eta
  TCanvas* CanvasThree = new TCanvas("CanvasThree","MuEta",550,550);
  CanvasThree->SetTickx();
  CanvasThree->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_MuEta = (TH1F*) HistoFile->Get("data_obs_MuEta");
  TH1F* data_obs_Fake_MuEta = (TH1F*) HistoFile->Get("data_obs_Fake_MuEta");
  TH1F* embedded_MuEta = (TH1F*) HistoFile->Get("embedded_MuEta");
  TH1F* DY_MuEta = (TH1F*) HistoFile->Get("DY_MuEta");
  TH1F* DYlow_MuEta = (TH1F*) HistoFile->Get("DYlow_MuEta");
  TH1F* TTToHadronic_MuEta = (TH1F*) HistoFile->Get("TTToHadronic_MuEta");
  TH1F* TTTo2L2Nu_MuEta = (TH1F*) HistoFile->Get("TTTo2L2Nu_MuEta");
  TH1F* TTToSemiLeptonic_MuEta = (TH1F*) HistoFile->Get("TTToSemiLeptonic_MuEta");
  TH1F* WW4Q_MuEta = (TH1F*) HistoFile->Get("WW4Q_MuEta");
  TH1F* WWLNuQQ_MuEta = (TH1F*) HistoFile->Get("WWLNuQQ_MuEta");
  TH1F* WZ2L2Q_MuEta = (TH1F*) HistoFile->Get("WZ2L2Q_MuEta");
  TH1F* WZ1L3Nu_MuEta = (TH1F*) HistoFile->Get("WZ1L3Nu_MuEta");
  TH1F* WZ3LNu_MuEta = (TH1F*) HistoFile->Get("WZ3LNu_MuEta");
  TH1F* WZ1L1Nu2Q_MuEta = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_MuEta");
  TH1F* ZZ4L_MuEta = (TH1F*) HistoFile->Get("ZZ4L_MuEta");
  TH1F* ZZ2L2Nu_MuEta = (TH1F*) HistoFile->Get("ZZ2L2Nu_MuEta");
  TH1F* ZZ2L2Q_MuEta = (TH1F*) HistoFile->Get("ZZ2L2Q_MuEta");
  TH1F* ST_t_antitop_MuEta = (TH1F*) HistoFile->Get("ST_t_antitop_MuEta");
  TH1F* ST_t_top_MuEta = (TH1F*) HistoFile->Get("ST_t_top_MuEta");
  TH1F* ST_tW_antitop_MuEta = (TH1F*) HistoFile->Get("ST_tW_antitop_MuEta");
  TH1F* ST_tW_top_MuEta = (TH1F*) HistoFile->Get("ST_tW_top_MuEta");
  TH1F* ggH_htt125_MuEta = (TH1F*) HistoFile->Get("ggH_htt125_MuEta");
  TH1F* qqH_htt125_MuEta = (TH1F*) HistoFile->Get("qqH_htt125_MuEta");  
  TH1F* WplusH125_MuEta = (TH1F*) HistoFile->Get("WplusH125_MuEta");
  TH1F* WminusH125_MuEta = (TH1F*) HistoFile->Get("WminusH125_MuEta");
  TH1F* ZH125_MuEta = (TH1F*) HistoFile->Get("ZH125_MuEta");
  TH1F* EWKZLL_MuEta = (TH1F*) HistoFile->Get("EWKZLL_MuEta");
  TH1F* EWKZNuNu_MuEta = (TH1F*) HistoFile->Get("EWKZNuNu_MuEta");

  TH1F* DYFinal_MuEta = (TH1F*) DY_MuEta->Clone();
  DYFinal_MuEta->Add(DYlow_MuEta);
  
  TH1F* TTFinal_MuEta = (TH1F*) TTToHadronic_MuEta->Clone();
  TTFinal_MuEta->Add(TTTo2L2Nu_MuEta);
  TTFinal_MuEta->Add(TTToSemiLeptonic_MuEta);
  
  TH1F* VVFinal_MuEta = (TH1F*) WW4Q_MuEta->Clone();
  VVFinal_MuEta->Add(WWLNuQQ_MuEta);
  VVFinal_MuEta->Add(WZ2L2Q_MuEta);
  VVFinal_MuEta->Add(WZ1L3Nu_MuEta);
  VVFinal_MuEta->Add(WZ3LNu_MuEta);
  VVFinal_MuEta->Add(WZ1L1Nu2Q_MuEta);
  VVFinal_MuEta->Add(ZZ4L_MuEta);
  VVFinal_MuEta->Add(ZZ2L2Nu_MuEta);
  VVFinal_MuEta->Add(ZZ2L2Q_MuEta);
  
  TH1F* STFinal_MuEta = (TH1F*) ST_t_antitop_MuEta->Clone();
  STFinal_MuEta->Add(ST_t_top_MuEta);
  STFinal_MuEta->Add(ST_tW_antitop_MuEta);
  STFinal_MuEta->Add(ST_tW_top_MuEta);

  TH1F* VHFinal_MuEta = (TH1F*) WplusH125_MuEta->Clone();
  VHFinal_MuEta->Add(WminusH125_MuEta);
  VHFinal_MuEta->Add(ZH125_MuEta);

  TH1F* EWKFinal_MuEta = (TH1F*) EWKZLL_MuEta->Clone();
  EWKFinal_MuEta->Add(EWKZNuNu_MuEta);

  data_obs_MuEta->SetMarkerStyle(20);
  data_obs_MuEta->Sumw2();
  
  data_obs_Fake_MuEta->SetFillColor(kRed);
  data_obs_Fake_MuEta->SetLineColor(kBlack);

  embedded_MuEta->SetFillColor(kYellow);
  embedded_MuEta->SetLineColor(kBlack);

  DYFinal_MuEta->SetFillColor(kBlue);
  DYFinal_MuEta->SetLineColor(kBlack);

  TTFinal_MuEta->SetFillColor(kViolet-3);
  TTFinal_MuEta->SetLineColor(kBlack);

  VVFinal_MuEta->SetFillColor(kPink-3);
  VVFinal_MuEta->SetLineColor(kBlack);

  STFinal_MuEta->SetFillColor(kGreen);
  STFinal_MuEta->SetLineColor(kBlack);

  qqH_htt125_MuEta->SetFillColor(kCyan);
  qqH_htt125_MuEta->SetLineColor(kBlack);

  ggH_htt125_MuEta->SetFillColor(kCyan);
  ggH_htt125_MuEta->SetLineColor(kBlack);

  VHFinal_MuEta->SetFillColor(kOrange);
  VHFinal_MuEta->SetLineColor(kBlack);

  EWKFinal_MuEta->SetFillColor(kBlue-2);
  EWKFinal_MuEta->SetLineColor(kBlack);
  
  THStack* BackgroundStack_MuEta = new THStack("BackgroundStack_MuEta","BackgroundStack_MuEta");
  BackgroundStack_MuEta->Add(data_obs_Fake_MuEta,"hist");
  BackgroundStack_MuEta->Add(DYFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(embedded_MuEta,"hist");
  BackgroundStack_MuEta->Add(TTFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(VVFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(STFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(qqH_htt125_MuEta,"hist");
  BackgroundStack_MuEta->Add(ggH_htt125_MuEta,"hist");
  BackgroundStack_MuEta->Add(VHFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(EWKFinal_MuEta,"hist");

  TH1F* BackgroundStack_MuEta_Errors = MakeStackErrors(BackgroundStack_MuEta);

  TPad* PlotPad_MuEta = MakeRatioPlot(CanvasThree, BackgroundStack_MuEta, data_obs_MuEta,"#mu Eta");

  BackgroundStack_MuEta->SetMaximum(max(BackgroundStack_MuEta->GetMaximum(),data_obs_MuEta->GetMaximum()));

  BackgroundStack_MuEta->Draw();
  BackgroundStack_MuEta_Errors->Draw("SAME e2");
  BackgroundStack_MuEta->SetTitle("#mu Eta");
  data_obs_MuEta->Draw("SAME e1");
  BackgroundStack_MuEta->GetYaxis()->SetTitle("Events");
  BackgroundStack_MuEta->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_MuEta,0,33);

  TLegend* Legend_MuEta = new TLegend(0.1,0.7,0.3,0.9);
  Legend_MuEta->AddEntry(embedded_MuEta,"embedded","f");
  Legend_MuEta->AddEntry(DYFinal_MuEta, "Other DY","f");
  Legend_MuEta->AddEntry(TTFinal_MuEta,"t#bar{t}","f");
  Legend_MuEta->AddEntry(VVFinal_MuEta,"Dibsoson","f");
  Legend_MuEta->AddEntry(STFinal_MuEta,"Single Top","f");
  Legend_MuEta->AddEntry(qqH_htt125_MuEta,"qqh","f");
  Legend_MuEta->AddEntry(ggH_htt125_MuEta,"ggH","f");
  Legend_MuEta->AddEntry(VHFinal_MuEta,"VH","f");
  Legend_MuEta->AddEntry(EWKFinal_MuEta,"EWK","f");
  Legend_MuEta->AddEntry(data_obs_Fake_MuEta,"Fakes","f");

  Legend_MuEta->Draw();

  //Tau Eta
  
  TCanvas* CanvasFour = new TCanvas("CanvasFour","TauEta",550,550);
  CanvasFour->SetTickx();
  CanvasFour->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_TauEta = (TH1F*) HistoFile->Get("data_obs_TauEta");
  TH1F* data_obs_Fake_TauEta = (TH1F*) HistoFile->Get("data_obs_Fake_TauEta");
  TH1F* embedded_TauEta = (TH1F*) HistoFile->Get("embedded_TauEta");
  TH1F* DY_TauEta = (TH1F*) HistoFile->Get("DY_TauEta");
  TH1F* DYlow_TauEta = (TH1F*) HistoFile->Get("DYlow_TauEta");
  TH1F* TTToHadronic_TauEta = (TH1F*) HistoFile->Get("TTToHadronic_TauEta");
  TH1F* TTTo2L2Nu_TauEta = (TH1F*) HistoFile->Get("TTTo2L2Nu_TauEta");
  TH1F* TTToSemiLeptonic_TauEta = (TH1F*) HistoFile->Get("TTToSemiLeptonic_TauEta");
  TH1F* WW4Q_TauEta = (TH1F*) HistoFile->Get("WW4Q_TauEta");
  TH1F* WWLNuQQ_TauEta = (TH1F*) HistoFile->Get("WWLNuQQ_TauEta");
  TH1F* WZ2L2Q_TauEta = (TH1F*) HistoFile->Get("WZ2L2Q_TauEta");
  TH1F* WZ1L3Nu_TauEta = (TH1F*) HistoFile->Get("WZ1L3Nu_TauEta");
  TH1F* WZ3LNu_TauEta = (TH1F*) HistoFile->Get("WZ3LNu_TauEta");
  TH1F* WZ1L1Nu2Q_TauEta = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_TauEta");
  TH1F* ZZ4L_TauEta = (TH1F*) HistoFile->Get("ZZ4L_TauEta");
  TH1F* ZZ2L2Nu_TauEta = (TH1F*) HistoFile->Get("ZZ2L2Nu_TauEta");
  TH1F* ZZ2L2Q_TauEta = (TH1F*) HistoFile->Get("ZZ2L2Q_TauEta");
  TH1F* ST_t_antitop_TauEta = (TH1F*) HistoFile->Get("ST_t_antitop_TauEta");
  TH1F* ST_t_top_TauEta = (TH1F*) HistoFile->Get("ST_t_top_TauEta");
  TH1F* ST_tW_antitop_TauEta = (TH1F*) HistoFile->Get("ST_tW_antitop_TauEta");
  TH1F* ST_tW_top_TauEta = (TH1F*) HistoFile->Get("ST_tW_top_TauEta");
  TH1F* ggH_htt125_TauEta = (TH1F*) HistoFile->Get("ggH_htt125_TauEta");
  TH1F* qqH_htt125_TauEta = (TH1F*) HistoFile->Get("qqH_htt125_TauEta");  
  TH1F* WplusH125_TauEta = (TH1F*) HistoFile->Get("WplusH125_TauEta");
  TH1F* WminusH125_TauEta = (TH1F*) HistoFile->Get("WminusH125_TauEta");
  TH1F* ZH125_TauEta = (TH1F*) HistoFile->Get("ZH125_TauEta");
  TH1F* EWKZLL_TauEta = (TH1F*) HistoFile->Get("EWKZLL_TauEta");
  TH1F* EWKZNuNu_TauEta = (TH1F*) HistoFile->Get("EWKZNuNu_TauEta");

  TH1F* DYFinal_TauEta = (TH1F*) DY_TauEta->Clone();
  DYFinal_TauEta->Add(DYlow_TauEta);
  
  TH1F* TTFinal_TauEta = (TH1F*) TTToHadronic_TauEta->Clone();
  TTFinal_TauEta->Add(TTTo2L2Nu_TauEta);
  TTFinal_TauEta->Add(TTToSemiLeptonic_TauEta);
  
  TH1F* VVFinal_TauEta = (TH1F*) WW4Q_TauEta->Clone();
  VVFinal_TauEta->Add(WWLNuQQ_TauEta);
  VVFinal_TauEta->Add(WZ2L2Q_TauEta);
  VVFinal_TauEta->Add(WZ1L3Nu_TauEta);
  VVFinal_TauEta->Add(WZ3LNu_TauEta);
  VVFinal_TauEta->Add(WZ1L1Nu2Q_TauEta);
  VVFinal_TauEta->Add(ZZ4L_TauEta);
  VVFinal_TauEta->Add(ZZ2L2Nu_TauEta);
  VVFinal_TauEta->Add(ZZ2L2Q_TauEta);
  
  TH1F* STFinal_TauEta = (TH1F*) ST_t_antitop_TauEta->Clone();
  STFinal_TauEta->Add(ST_t_top_TauEta);
  STFinal_TauEta->Add(ST_tW_antitop_TauEta);
  STFinal_TauEta->Add(ST_tW_top_TauEta);

  TH1F* VHFinal_TauEta = (TH1F*) WplusH125_TauEta->Clone();
  VHFinal_TauEta->Add(WminusH125_TauEta);
  VHFinal_TauEta->Add(ZH125_TauEta);

  TH1F* EWKFinal_TauEta = (TH1F*) EWKZLL_TauEta->Clone();
  EWKFinal_TauEta->Add(EWKZNuNu_TauEta);

  data_obs_TauEta->SetMarkerStyle(20);
  data_obs_TauEta->Sumw2();
  
  data_obs_Fake_TauEta->SetFillColor(kRed);
  data_obs_Fake_TauEta->SetLineColor(kBlack);

  embedded_TauEta->SetFillColor(kYellow);
  embedded_TauEta->SetLineColor(kBlack);

  DYFinal_TauEta->SetFillColor(kBlue);
  DYFinal_TauEta->SetLineColor(kBlack);

  TTFinal_TauEta->SetFillColor(kViolet-3);
  TTFinal_TauEta->SetLineColor(kBlack);

  VVFinal_TauEta->SetFillColor(kPink-3);
  VVFinal_TauEta->SetLineColor(kBlack);

  STFinal_TauEta->SetFillColor(kGreen);
  STFinal_TauEta->SetLineColor(kBlack);

  qqH_htt125_TauEta->SetFillColor(kCyan);
  qqH_htt125_TauEta->SetLineColor(kBlack);

  ggH_htt125_TauEta->SetFillColor(kCyan);
  ggH_htt125_TauEta->SetLineColor(kBlack);

  VHFinal_TauEta->SetFillColor(kOrange);
  VHFinal_TauEta->SetLineColor(kBlack);

  EWKFinal_TauEta->SetFillColor(kBlue-2);
  EWKFinal_TauEta->SetLineColor(kBlack);
  
  THStack* BackgroundStack_TauEta = new THStack("BackgroundStack_TauEta","BackgroundStack_TauEta");
  BackgroundStack_TauEta->Add(data_obs_Fake_TauEta,"hist");
  BackgroundStack_TauEta->Add(DYFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(embedded_TauEta,"hist");
  BackgroundStack_TauEta->Add(TTFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(VVFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(STFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(qqH_htt125_TauEta,"hist");
  BackgroundStack_TauEta->Add(ggH_htt125_TauEta,"hist");
  BackgroundStack_TauEta->Add(VHFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(EWKFinal_TauEta,"hist");

  TH1F* BackgroundStack_TauEta_Errors = MakeStackErrors(BackgroundStack_TauEta);

  TPad* PlotPad_TauEta = MakeRatioPlot(CanvasFour, BackgroundStack_TauEta, data_obs_TauEta,"#tau Eta");

  BackgroundStack_TauEta->SetMaximum(max(BackgroundStack_TauEta->GetMaximum(),data_obs_TauEta->GetMaximum()));

  BackgroundStack_TauEta->Draw();
  BackgroundStack_TauEta_Errors->Draw("SAME e2");
  BackgroundStack_TauEta->SetTitle("#tau Eta");
  data_obs_TauEta->Draw("SAME e1");
  BackgroundStack_TauEta->GetYaxis()->SetTitle("Events");
  BackgroundStack_TauEta->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_TauEta,0,33);

  TLegend* Legend_TauEta = new TLegend(0.1,0.7,0.3,0.9);
  Legend_TauEta->AddEntry(embedded_TauEta,"embedded","f");
  Legend_TauEta->AddEntry(DYFinal_TauEta, "Other DY","f");
  Legend_TauEta->AddEntry(TTFinal_TauEta,"t#bar{t}","f");
  Legend_TauEta->AddEntry(VVFinal_TauEta,"Dibsoson","f");
  Legend_TauEta->AddEntry(STFinal_TauEta,"Single Top","f");
  Legend_TauEta->AddEntry(qqH_htt125_TauEta,"qqh","f");
  Legend_TauEta->AddEntry(ggH_htt125_TauEta,"ggH","f");
  Legend_TauEta->AddEntry(VHFinal_TauEta,"VH","f");
  Legend_TauEta->AddEntry(EWKFinal_TauEta,"EWK","f");
  Legend_TauEta->AddEntry(data_obs_Fake_TauEta,"Fakes","f");

  Legend_TauEta->Draw();

  //Mu Phi

  TCanvas* CanvasFive = new TCanvas("CanvasFive","MuPhi",550,550);
  CanvasFive->SetTickx();
  CanvasFive->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_MuPhi = (TH1F*) HistoFile->Get("data_obs_MuPhi");
  TH1F* data_obs_Fake_MuPhi = (TH1F*) HistoFile->Get("data_obs_Fake_MuPhi");
  TH1F* embedded_MuPhi = (TH1F*) HistoFile->Get("embedded_MuPhi");
  TH1F* DY_MuPhi = (TH1F*) HistoFile->Get("DY_MuPhi");
  TH1F* DYlow_MuPhi = (TH1F*) HistoFile->Get("DYlow_MuPhi");
  TH1F* TTToHadronic_MuPhi = (TH1F*) HistoFile->Get("TTToHadronic_MuPhi");
  TH1F* TTTo2L2Nu_MuPhi = (TH1F*) HistoFile->Get("TTTo2L2Nu_MuPhi");
  TH1F* TTToSemiLeptonic_MuPhi = (TH1F*) HistoFile->Get("TTToSemiLeptonic_MuPhi");
  TH1F* WW4Q_MuPhi = (TH1F*) HistoFile->Get("WW4Q_MuPhi");
  TH1F* WWLNuQQ_MuPhi = (TH1F*) HistoFile->Get("WWLNuQQ_MuPhi");
  TH1F* WZ2L2Q_MuPhi = (TH1F*) HistoFile->Get("WZ2L2Q_MuPhi");
  TH1F* WZ1L3Nu_MuPhi = (TH1F*) HistoFile->Get("WZ1L3Nu_MuPhi");
  TH1F* WZ3LNu_MuPhi = (TH1F*) HistoFile->Get("WZ3LNu_MuPhi");
  TH1F* WZ1L1Nu2Q_MuPhi = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_MuPhi");
  TH1F* ZZ4L_MuPhi = (TH1F*) HistoFile->Get("ZZ4L_MuPhi");
  TH1F* ZZ2L2Nu_MuPhi = (TH1F*) HistoFile->Get("ZZ2L2Nu_MuPhi");
  TH1F* ZZ2L2Q_MuPhi = (TH1F*) HistoFile->Get("ZZ2L2Q_MuPhi");
  TH1F* ST_t_antitop_MuPhi = (TH1F*) HistoFile->Get("ST_t_antitop_MuPhi");
  TH1F* ST_t_top_MuPhi = (TH1F*) HistoFile->Get("ST_t_top_MuPhi");
  TH1F* ST_tW_antitop_MuPhi = (TH1F*) HistoFile->Get("ST_tW_antitop_MuPhi");
  TH1F* ST_tW_top_MuPhi = (TH1F*) HistoFile->Get("ST_tW_top_MuPhi");
  TH1F* ggH_htt125_MuPhi = (TH1F*) HistoFile->Get("ggH_htt125_MuPhi");
  TH1F* qqH_htt125_MuPhi = (TH1F*) HistoFile->Get("qqH_htt125_MuPhi");  
  TH1F* WplusH125_MuPhi = (TH1F*) HistoFile->Get("WplusH125_MuPhi");
  TH1F* WminusH125_MuPhi = (TH1F*) HistoFile->Get("WminusH125_MuPhi");
  TH1F* ZH125_MuPhi = (TH1F*) HistoFile->Get("ZH125_MuPhi");
  TH1F* EWKZLL_MuPhi = (TH1F*) HistoFile->Get("EWKZLL_MuPhi");
  TH1F* EWKZNuNu_MuPhi = (TH1F*) HistoFile->Get("EWKZNuNu_MuPhi");

  TH1F* DYFinal_MuPhi = (TH1F*) DY_MuPhi->Clone();
  DYFinal_MuPhi->Add(DYlow_MuPhi);
  
  TH1F* TTFinal_MuPhi = (TH1F*) TTToHadronic_MuPhi->Clone();
  TTFinal_MuPhi->Add(TTTo2L2Nu_MuPhi);
  TTFinal_MuPhi->Add(TTToSemiLeptonic_MuPhi);
  
  TH1F* VVFinal_MuPhi = (TH1F*) WW4Q_MuPhi->Clone();
  VVFinal_MuPhi->Add(WWLNuQQ_MuPhi);
  VVFinal_MuPhi->Add(WZ2L2Q_MuPhi);
  VVFinal_MuPhi->Add(WZ1L3Nu_MuPhi);
  VVFinal_MuPhi->Add(WZ3LNu_MuPhi);
  VVFinal_MuPhi->Add(WZ1L1Nu2Q_MuPhi);
  VVFinal_MuPhi->Add(ZZ4L_MuPhi);
  VVFinal_MuPhi->Add(ZZ2L2Nu_MuPhi);
  VVFinal_MuPhi->Add(ZZ2L2Q_MuPhi);
  
  TH1F* STFinal_MuPhi = (TH1F*) ST_t_antitop_MuPhi->Clone();
  STFinal_MuPhi->Add(ST_t_top_MuPhi);
  STFinal_MuPhi->Add(ST_tW_antitop_MuPhi);
  STFinal_MuPhi->Add(ST_tW_top_MuPhi);

  TH1F* VHFinal_MuPhi = (TH1F*) WplusH125_MuPhi->Clone();
  VHFinal_MuPhi->Add(WminusH125_MuPhi);
  VHFinal_MuPhi->Add(ZH125_MuPhi);

  TH1F* EWKFinal_MuPhi = (TH1F*) EWKZLL_MuPhi->Clone();
  EWKFinal_MuPhi->Add(EWKZNuNu_MuPhi);

  data_obs_MuPhi->SetMarkerStyle(20);
  data_obs_MuPhi->Sumw2();
  
  data_obs_Fake_MuPhi->SetFillColor(kRed);
  data_obs_Fake_MuPhi->SetLineColor(kBlack);

  embedded_MuPhi->SetFillColor(kYellow);
  embedded_MuPhi->SetLineColor(kBlack);

  DYFinal_MuPhi->SetFillColor(kBlue);
  DYFinal_MuPhi->SetLineColor(kBlack);

  TTFinal_MuPhi->SetFillColor(kViolet-3);
  TTFinal_MuPhi->SetLineColor(kBlack);

  VVFinal_MuPhi->SetFillColor(kPink-3);
  VVFinal_MuPhi->SetLineColor(kBlack);

  STFinal_MuPhi->SetFillColor(kGreen);
  STFinal_MuPhi->SetLineColor(kBlack);

  qqH_htt125_MuPhi->SetFillColor(kCyan);
  qqH_htt125_MuPhi->SetLineColor(kBlack);

  ggH_htt125_MuPhi->SetFillColor(kCyan);
  ggH_htt125_MuPhi->SetLineColor(kBlack);

  VHFinal_MuPhi->SetFillColor(kOrange);
  VHFinal_MuPhi->SetLineColor(kBlack);

  EWKFinal_MuPhi->SetFillColor(kBlue-2);
  EWKFinal_MuPhi->SetLineColor(kBlack);
  
  THStack* BackgroundStack_MuPhi = new THStack("BackgroundStack_MuPhi","BackgroundStack_MuPhi");
  BackgroundStack_MuPhi->Add(data_obs_Fake_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(DYFinal_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(embedded_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(TTFinal_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(VVFinal_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(STFinal_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(qqH_htt125_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(ggH_htt125_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(VHFinal_MuPhi,"hist");
  BackgroundStack_MuPhi->Add(EWKFinal_MuPhi,"hist");

  TH1F* BackgroundStack_MuPhi_Errors = MakeStackErrors(BackgroundStack_MuPhi);

  TPad* PlotPad_MuPhi = MakeRatioPlot(CanvasFive, BackgroundStack_MuPhi, data_obs_MuPhi,"#tau #phi");

  BackgroundStack_MuPhi->SetMaximum(max(BackgroundStack_MuPhi->GetMaximum(),data_obs_MuPhi->GetMaximum()));

  BackgroundStack_MuPhi->Draw();
  BackgroundStack_MuPhi_Errors->Draw("SAME e2");
  BackgroundStack_MuPhi->SetTitle("#mu #phi");
  data_obs_MuPhi->Draw("SAME e1");
  BackgroundStack_MuPhi->GetYaxis()->SetTitle("Events");
  BackgroundStack_MuPhi->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_MuPhi,0,33);

  TLegend* Legend_MuPhi = new TLegend(0.61,0.41,0.88,0.68);
  Legend_MuPhi->AddEntry(embedded_MuPhi,"embedded","f");
  Legend_MuPhi->AddEntry(DYFinal_MuPhi, "Other DY","f");
  Legend_MuPhi->AddEntry(TTFinal_MuPhi,"t#bar{t}","f");
  Legend_MuPhi->AddEntry(VVFinal_MuPhi,"Dibsoson","f");
  Legend_MuPhi->AddEntry(STFinal_MuPhi,"Single Top","f");
  Legend_MuPhi->AddEntry(qqH_htt125_MuPhi,"qqh","f");
  Legend_MuPhi->AddEntry(ggH_htt125_MuPhi,"ggH","f");
  Legend_MuPhi->AddEntry(VHFinal_MuPhi,"VH","f");
  Legend_MuPhi->AddEntry(EWKFinal_MuPhi,"EWK","f");
  Legend_MuPhi->AddEntry(data_obs_Fake_MuPhi,"Fakes","f");

  Legend_MuPhi->Draw();

  //Tau Phi
  
  TCanvas* CanvasSix = new TCanvas("CanvasSix","TauPhi",550,550);
  CanvasSix->SetTickx();
  CanvasSix->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_TauPhi = (TH1F*) HistoFile->Get("data_obs_TauPhi");
  TH1F* data_obs_Fake_TauPhi = (TH1F*) HistoFile->Get("data_obs_Fake_TauPhi");
  TH1F* embedded_TauPhi = (TH1F*) HistoFile->Get("embedded_TauPhi");
  TH1F* DY_TauPhi = (TH1F*) HistoFile->Get("DY_TauPhi");
  TH1F* DYlow_TauPhi = (TH1F*) HistoFile->Get("DYlow_TauPhi");
  TH1F* TTToHadronic_TauPhi = (TH1F*) HistoFile->Get("TTToHadronic_TauPhi");
  TH1F* TTTo2L2Nu_TauPhi = (TH1F*) HistoFile->Get("TTTo2L2Nu_TauPhi");
  TH1F* TTToSemiLeptonic_TauPhi = (TH1F*) HistoFile->Get("TTToSemiLeptonic_TauPhi");
  TH1F* WW4Q_TauPhi = (TH1F*) HistoFile->Get("WW4Q_TauPhi");
  TH1F* WWLNuQQ_TauPhi = (TH1F*) HistoFile->Get("WWLNuQQ_TauPhi");
  TH1F* WZ2L2Q_TauPhi = (TH1F*) HistoFile->Get("WZ2L2Q_TauPhi");
  TH1F* WZ1L3Nu_TauPhi = (TH1F*) HistoFile->Get("WZ1L3Nu_TauPhi");
  TH1F* WZ3LNu_TauPhi = (TH1F*) HistoFile->Get("WZ3LNu_TauPhi");
  TH1F* WZ1L1Nu2Q_TauPhi = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_TauPhi");
  TH1F* ZZ4L_TauPhi = (TH1F*) HistoFile->Get("ZZ4L_TauPhi");
  TH1F* ZZ2L2Nu_TauPhi = (TH1F*) HistoFile->Get("ZZ2L2Nu_TauPhi");
  TH1F* ZZ2L2Q_TauPhi = (TH1F*) HistoFile->Get("ZZ2L2Q_TauPhi");
  TH1F* ST_t_antitop_TauPhi = (TH1F*) HistoFile->Get("ST_t_antitop_TauPhi");
  TH1F* ST_t_top_TauPhi = (TH1F*) HistoFile->Get("ST_t_top_TauPhi");
  TH1F* ST_tW_antitop_TauPhi = (TH1F*) HistoFile->Get("ST_tW_antitop_TauPhi");
  TH1F* ST_tW_top_TauPhi = (TH1F*) HistoFile->Get("ST_tW_top_TauPhi");
  TH1F* ggH_htt125_TauPhi = (TH1F*) HistoFile->Get("ggH_htt125_TauPhi");
  TH1F* qqH_htt125_TauPhi = (TH1F*) HistoFile->Get("qqH_htt125_TauPhi");  
  TH1F* WplusH125_TauPhi = (TH1F*) HistoFile->Get("WplusH125_TauPhi");
  TH1F* WminusH125_TauPhi = (TH1F*) HistoFile->Get("WminusH125_TauPhi");
  TH1F* ZH125_TauPhi = (TH1F*) HistoFile->Get("ZH125_TauPhi");
  TH1F* EWKZLL_TauPhi = (TH1F*) HistoFile->Get("EWKZLL_TauPhi");
  TH1F* EWKZNuNu_TauPhi = (TH1F*) HistoFile->Get("EWKZNuNu_TauPhi");

  TH1F* DYFinal_TauPhi = (TH1F*) DY_TauPhi->Clone();
  DYFinal_TauPhi->Add(DYlow_TauPhi);
  
  TH1F* TTFinal_TauPhi = (TH1F*) TTToHadronic_TauPhi->Clone();
  TTFinal_TauPhi->Add(TTTo2L2Nu_TauPhi);
  TTFinal_TauPhi->Add(TTToSemiLeptonic_TauPhi);
  
  TH1F* VVFinal_TauPhi = (TH1F*) WW4Q_TauPhi->Clone();
  VVFinal_TauPhi->Add(WWLNuQQ_TauPhi);
  VVFinal_TauPhi->Add(WZ2L2Q_TauPhi);
  VVFinal_TauPhi->Add(WZ1L3Nu_TauPhi);
  VVFinal_TauPhi->Add(WZ3LNu_TauPhi);
  VVFinal_TauPhi->Add(WZ1L1Nu2Q_TauPhi);
  VVFinal_TauPhi->Add(ZZ4L_TauPhi);
  VVFinal_TauPhi->Add(ZZ2L2Nu_TauPhi);
  VVFinal_TauPhi->Add(ZZ2L2Q_TauPhi);
  
  TH1F* STFinal_TauPhi = (TH1F*) ST_t_antitop_TauPhi->Clone();
  STFinal_TauPhi->Add(ST_t_top_TauPhi);
  STFinal_TauPhi->Add(ST_tW_antitop_TauPhi);
  STFinal_TauPhi->Add(ST_tW_top_TauPhi);

  TH1F* VHFinal_TauPhi = (TH1F*) WplusH125_TauPhi->Clone();
  VHFinal_TauPhi->Add(WminusH125_TauPhi);
  VHFinal_TauPhi->Add(ZH125_TauPhi);

  TH1F* EWKFinal_TauPhi = (TH1F*) EWKZLL_TauPhi->Clone();
  EWKFinal_TauPhi->Add(EWKZNuNu_TauPhi);

  data_obs_TauPhi->SetMarkerStyle(20);
  data_obs_TauPhi->Sumw2();
  
  data_obs_Fake_TauPhi->SetFillColor(kRed);
  data_obs_Fake_TauPhi->SetLineColor(kBlack);

  embedded_TauPhi->SetFillColor(kYellow);
  embedded_TauPhi->SetLineColor(kBlack);

  DYFinal_TauPhi->SetFillColor(kBlue);
  DYFinal_TauPhi->SetLineColor(kBlack);

  TTFinal_TauPhi->SetFillColor(kViolet-3);
  TTFinal_TauPhi->SetLineColor(kBlack);

  VVFinal_TauPhi->SetFillColor(kPink-3);
  VVFinal_TauPhi->SetLineColor(kBlack);

  STFinal_TauPhi->SetFillColor(kGreen);
  STFinal_TauPhi->SetLineColor(kBlack);

  qqH_htt125_TauPhi->SetFillColor(kCyan);
  qqH_htt125_TauPhi->SetLineColor(kBlack);

  ggH_htt125_TauPhi->SetFillColor(kCyan);
  ggH_htt125_TauPhi->SetLineColor(kBlack);

  VHFinal_TauPhi->SetFillColor(kOrange);
  VHFinal_TauPhi->SetLineColor(kBlack);

  EWKFinal_TauPhi->SetFillColor(kBlue-2);
  EWKFinal_TauPhi->SetLineColor(kBlack);
  
  THStack* BackgroundStack_TauPhi = new THStack("BackgroundStack_TauPhi","BackgroundStack_TauPhi");
  BackgroundStack_TauPhi->Add(data_obs_Fake_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(DYFinal_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(embedded_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(TTFinal_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(VVFinal_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(STFinal_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(qqH_htt125_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(ggH_htt125_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(VHFinal_TauPhi,"hist");
  BackgroundStack_TauPhi->Add(EWKFinal_TauPhi,"hist");

  TH1F* BackgroundStack_TauPhi_Errors = MakeStackErrors(BackgroundStack_TauPhi);

  TPad* PlotPad_TauPhi = MakeRatioPlot(CanvasSix, BackgroundStack_TauPhi, data_obs_TauPhi,"#tau #phi");

  BackgroundStack_TauPhi->SetMaximum(max(BackgroundStack_TauPhi->GetMaximum(),data_obs_TauPhi->GetMaximum()));

  BackgroundStack_TauPhi->Draw();
  BackgroundStack_TauPhi_Errors->Draw("SAME e2");
  BackgroundStack_TauPhi->SetTitle("#tau #phi");
  data_obs_TauPhi->Draw("SAME e1");
  BackgroundStack_TauPhi->GetYaxis()->SetTitle("Events");
  BackgroundStack_TauPhi->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_TauPhi,0,33);

  TLegend* Legend_TauPhi = new TLegend(0.61,0.41,0.88,0.68);
  Legend_TauPhi->AddEntry(embedded_TauPhi,"embedded","f");
  Legend_TauPhi->AddEntry(DYFinal_TauPhi, "Other DY","f");
  Legend_TauPhi->AddEntry(TTFinal_TauPhi,"t#bar{t}","f");
  Legend_TauPhi->AddEntry(VVFinal_TauPhi,"Dibsoson","f");
  Legend_TauPhi->AddEntry(STFinal_TauPhi,"Single Top","f");
  Legend_TauPhi->AddEntry(qqH_htt125_TauPhi,"qqh","f");
  Legend_TauPhi->AddEntry(ggH_htt125_TauPhi,"ggH","f");
  Legend_TauPhi->AddEntry(VHFinal_TauPhi,"VH","f");
  Legend_TauPhi->AddEntry(EWKFinal_TauPhi,"EWK","f");
  Legend_TauPhi->AddEntry(data_obs_Fake_TauPhi,"Fakes","f");

  Legend_TauPhi->Draw();

  //N Jets

  TCanvas* CanvasSeven = new TCanvas("CanvasSeven","NJets",550,550);
  CanvasSeven->SetTickx();
  CanvasSeven->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_NJets = (TH1F*) HistoFile->Get("data_obs_NJets");
  TH1F* data_obs_Fake_NJets = (TH1F*) HistoFile->Get("data_obs_Fake_NJets");
  TH1F* embedded_NJets = (TH1F*) HistoFile->Get("embedded_NJets");
  TH1F* DY_NJets = (TH1F*) HistoFile->Get("DY_NJets");
  TH1F* DYlow_NJets = (TH1F*) HistoFile->Get("DYlow_NJets");
  TH1F* TTToHadronic_NJets = (TH1F*) HistoFile->Get("TTToHadronic_NJets");
  TH1F* TTTo2L2Nu_NJets = (TH1F*) HistoFile->Get("TTTo2L2Nu_NJets");
  TH1F* TTToSemiLeptonic_NJets = (TH1F*) HistoFile->Get("TTToSemiLeptonic_NJets");
  TH1F* WW4Q_NJets = (TH1F*) HistoFile->Get("WW4Q_NJets");
  TH1F* WWLNuQQ_NJets = (TH1F*) HistoFile->Get("WWLNuQQ_NJets");
  TH1F* WZ2L2Q_NJets = (TH1F*) HistoFile->Get("WZ2L2Q_NJets");
  TH1F* WZ1L3Nu_NJets = (TH1F*) HistoFile->Get("WZ1L3Nu_NJets");
  TH1F* WZ3LNu_NJets = (TH1F*) HistoFile->Get("WZ3LNu_NJets");
  TH1F* WZ1L1Nu2Q_NJets = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_NJets");
  TH1F* ZZ4L_NJets = (TH1F*) HistoFile->Get("ZZ4L_NJets");
  TH1F* ZZ2L2Nu_NJets = (TH1F*) HistoFile->Get("ZZ2L2Nu_NJets");
  TH1F* ZZ2L2Q_NJets = (TH1F*) HistoFile->Get("ZZ2L2Q_NJets");
  TH1F* ST_t_antitop_NJets = (TH1F*) HistoFile->Get("ST_t_antitop_NJets");
  TH1F* ST_t_top_NJets = (TH1F*) HistoFile->Get("ST_t_top_NJets");
  TH1F* ST_tW_antitop_NJets = (TH1F*) HistoFile->Get("ST_tW_antitop_NJets");
  TH1F* ST_tW_top_NJets = (TH1F*) HistoFile->Get("ST_tW_top_NJets");
  TH1F* ggH_htt125_NJets = (TH1F*) HistoFile->Get("ggH_htt125_NJets");
  TH1F* qqH_htt125_NJets = (TH1F*) HistoFile->Get("qqH_htt125_NJets");  
  TH1F* WplusH125_NJets = (TH1F*) HistoFile->Get("WplusH125_NJets");
  TH1F* WminusH125_NJets = (TH1F*) HistoFile->Get("WminusH125_NJets");
  TH1F* ZH125_NJets = (TH1F*) HistoFile->Get("ZH125_NJets");
  TH1F* EWKZLL_NJets = (TH1F*) HistoFile->Get("EWKZLL_NJets");
  TH1F* EWKZNuNu_NJets = (TH1F*) HistoFile->Get("EWKZNuNu_NJets");

  TH1F* DYFinal_NJets = (TH1F*) DY_NJets->Clone();
  DYFinal_NJets->Add(DYlow_NJets);
  
  TH1F* TTFinal_NJets = (TH1F*) TTToHadronic_NJets->Clone();
  TTFinal_NJets->Add(TTTo2L2Nu_NJets);
  TTFinal_NJets->Add(TTToSemiLeptonic_NJets);
  
  TH1F* VVFinal_NJets = (TH1F*) WW4Q_NJets->Clone();
  VVFinal_NJets->Add(WWLNuQQ_NJets);
  VVFinal_NJets->Add(WZ2L2Q_NJets);
  VVFinal_NJets->Add(WZ1L3Nu_NJets);
  VVFinal_NJets->Add(WZ3LNu_NJets);
  VVFinal_NJets->Add(WZ1L1Nu2Q_NJets);
  VVFinal_NJets->Add(ZZ4L_NJets);
  VVFinal_NJets->Add(ZZ2L2Nu_NJets);
  VVFinal_NJets->Add(ZZ2L2Q_NJets);
  
  TH1F* STFinal_NJets = (TH1F*) ST_t_antitop_NJets->Clone();
  STFinal_NJets->Add(ST_t_top_NJets);
  STFinal_NJets->Add(ST_tW_antitop_NJets);
  STFinal_NJets->Add(ST_tW_top_NJets);

  TH1F* VHFinal_NJets = (TH1F*) WplusH125_NJets->Clone();
  VHFinal_NJets->Add(WminusH125_NJets);
  VHFinal_NJets->Add(ZH125_NJets);

  TH1F* EWKFinal_NJets = (TH1F*) EWKZLL_NJets->Clone();
  EWKFinal_NJets->Add(EWKZNuNu_NJets);

  data_obs_NJets->SetMarkerStyle(20);
  data_obs_NJets->Sumw2();
  
  data_obs_Fake_NJets->SetFillColor(kRed);
  data_obs_Fake_NJets->SetLineColor(kBlack);

  embedded_NJets->SetFillColor(kYellow);
  embedded_NJets->SetLineColor(kBlack);

  DYFinal_NJets->SetFillColor(kBlue);
  DYFinal_NJets->SetLineColor(kBlack);

  TTFinal_NJets->SetFillColor(kViolet-3);
  TTFinal_NJets->SetLineColor(kBlack);

  VVFinal_NJets->SetFillColor(kPink-3);
  VVFinal_NJets->SetLineColor(kBlack);

  STFinal_NJets->SetFillColor(kGreen);
  STFinal_NJets->SetLineColor(kBlack);

  qqH_htt125_NJets->SetFillColor(kCyan);
  qqH_htt125_NJets->SetLineColor(kBlack);

  ggH_htt125_NJets->SetFillColor(kCyan);
  ggH_htt125_NJets->SetLineColor(kBlack);

  VHFinal_NJets->SetFillColor(kOrange);
  VHFinal_NJets->SetLineColor(kBlack);

  EWKFinal_NJets->SetFillColor(kBlue-2);
  EWKFinal_NJets->SetLineColor(kBlack);
  
  THStack* BackgroundStack_NJets = new THStack("BackgroundStack_NJets","BackgroundStack_NJets");
  BackgroundStack_NJets->Add(data_obs_Fake_NJets,"hist");
  BackgroundStack_NJets->Add(DYFinal_NJets,"hist");
  BackgroundStack_NJets->Add(embedded_NJets,"hist");
  BackgroundStack_NJets->Add(TTFinal_NJets,"hist");
  BackgroundStack_NJets->Add(VVFinal_NJets,"hist");
  BackgroundStack_NJets->Add(STFinal_NJets,"hist");
  BackgroundStack_NJets->Add(qqH_htt125_NJets,"hist");
  BackgroundStack_NJets->Add(ggH_htt125_NJets,"hist");
  BackgroundStack_NJets->Add(VHFinal_NJets,"hist");
  BackgroundStack_NJets->Add(EWKFinal_NJets,"hist");

  TH1F* BackgroundStack_NJets_Errors = MakeStackErrors(BackgroundStack_NJets);

  TPad* PlotPad_NJets = MakeRatioPlot(CanvasSeven, BackgroundStack_NJets, data_obs_NJets,"NJets");

  BackgroundStack_NJets->SetMaximum(max(BackgroundStack_NJets->GetMaximum(),data_obs_NJets->GetMaximum()));

  BackgroundStack_NJets->Draw();
  BackgroundStack_NJets_Errors->Draw("SAME e2");
  BackgroundStack_NJets->SetTitle("NJets");
  data_obs_NJets->Draw("SAME e1");
  BackgroundStack_NJets->GetYaxis()->SetTitle("Events");
  BackgroundStack_NJets->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_NJets,0,33);

  TLegend* Legend_NJets = new TLegend(0.61,0.41,0.88,0.68);
  Legend_NJets->AddEntry(embedded_NJets,"embedded","f");
  Legend_NJets->AddEntry(DYFinal_NJets, "Other DY","f");
  Legend_NJets->AddEntry(TTFinal_NJets,"t#bar{t}","f");
  Legend_NJets->AddEntry(VVFinal_NJets,"Dibsoson","f");
  Legend_NJets->AddEntry(STFinal_NJets,"Single Top","f");
  Legend_NJets->AddEntry(qqH_htt125_NJets,"qqh","f");
  Legend_NJets->AddEntry(ggH_htt125_NJets,"ggH","f");
  Legend_NJets->AddEntry(VHFinal_NJets,"VH","f");
  Legend_NJets->AddEntry(EWKFinal_NJets,"EWK","f");
  Legend_NJets->AddEntry(data_obs_Fake_NJets,"Fakes","f");

  Legend_NJets->Draw();
  */
  //iso_1

  TCanvas* CanvasEight = new TCanvas("CanvasEight","iso_1",550,550);
  CanvasEight->SetTickx();
  CanvasEight->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_iso_1 = (TH1F*) HistoFile->Get("data_obs_iso_1");
  TH1F* data_obs_Fake_iso_1 = (TH1F*) HistoFile->Get("data_obs_Fake_iso_1");
  TH1F* embedded_iso_1 = (TH1F*) HistoFile->Get("embedded_iso_1");
  TH1F* DY_iso_1 = (TH1F*) HistoFile->Get("DY_iso_1");
  TH1F* DYlow_iso_1 = (TH1F*) HistoFile->Get("DYlow_iso_1");
  TH1F* TTToHadronic_iso_1 = (TH1F*) HistoFile->Get("TTToHadronic_iso_1");
  TH1F* TTTo2L2Nu_iso_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_iso_1");
  TH1F* TTToSemiLeptonic_iso_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_iso_1");
  TH1F* WW4Q_iso_1 = (TH1F*) HistoFile->Get("WW4Q_iso_1");
  TH1F* WWLNuQQ_iso_1 = (TH1F*) HistoFile->Get("WWLNuQQ_iso_1");
  TH1F* WZ2L2Q_iso_1 = (TH1F*) HistoFile->Get("WZ2L2Q_iso_1");
  TH1F* WZ1L3Nu_iso_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_iso_1");
  TH1F* WZ3LNu_iso_1 = (TH1F*) HistoFile->Get("WZ3LNu_iso_1");
  TH1F* WZ1L1Nu2Q_iso_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_iso_1");
  TH1F* ZZ4L_iso_1 = (TH1F*) HistoFile->Get("ZZ4L_iso_1");
  TH1F* ZZ2L2Nu_iso_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_iso_1");
  TH1F* ZZ2L2Q_iso_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_iso_1");
  TH1F* ST_t_antitop_iso_1 = (TH1F*) HistoFile->Get("ST_t_antitop_iso_1");
  TH1F* ST_t_top_iso_1 = (TH1F*) HistoFile->Get("ST_t_top_iso_1");
  TH1F* ST_tW_antitop_iso_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_iso_1");
  TH1F* ST_tW_top_iso_1 = (TH1F*) HistoFile->Get("ST_tW_top_iso_1");
  TH1F* ggH_htt125_iso_1 = (TH1F*) HistoFile->Get("ggH_htt125_iso_1");
  TH1F* qqH_htt125_iso_1 = (TH1F*) HistoFile->Get("qqH_htt125_iso_1");  
  TH1F* WplusH125_iso_1 = (TH1F*) HistoFile->Get("WplusH125_iso_1");
  TH1F* WminusH125_iso_1 = (TH1F*) HistoFile->Get("WminusH125_iso_1");
  TH1F* ZH125_iso_1 = (TH1F*) HistoFile->Get("ZH125_iso_1");
  TH1F* EWKZLL_iso_1 = (TH1F*) HistoFile->Get("EWKZLL_iso_1");
  TH1F* EWKZNuNu_iso_1 = (TH1F*) HistoFile->Get("EWKZNuNu_iso_1");

  TH1F* DYFinal_iso_1 = (TH1F*) DY_iso_1->Clone();
  DYFinal_iso_1->Add(DYlow_iso_1);
  
  TH1F* TTFinal_iso_1 = (TH1F*) TTToHadronic_iso_1->Clone();
  TTFinal_iso_1->Add(TTTo2L2Nu_iso_1);
  TTFinal_iso_1->Add(TTToSemiLeptonic_iso_1);
  
  TH1F* VVFinal_iso_1 = (TH1F*) WW4Q_iso_1->Clone();
  VVFinal_iso_1->Add(WWLNuQQ_iso_1);
  VVFinal_iso_1->Add(WZ2L2Q_iso_1);
  VVFinal_iso_1->Add(WZ1L3Nu_iso_1);
  VVFinal_iso_1->Add(WZ3LNu_iso_1);
  VVFinal_iso_1->Add(WZ1L1Nu2Q_iso_1);
  VVFinal_iso_1->Add(ZZ4L_iso_1);
  VVFinal_iso_1->Add(ZZ2L2Nu_iso_1);
  VVFinal_iso_1->Add(ZZ2L2Q_iso_1);
  
  TH1F* STFinal_iso_1 = (TH1F*) ST_t_antitop_iso_1->Clone();
  STFinal_iso_1->Add(ST_t_top_iso_1);
  STFinal_iso_1->Add(ST_tW_antitop_iso_1);
  STFinal_iso_1->Add(ST_tW_top_iso_1);

  TH1F* VHFinal_iso_1 = (TH1F*) WplusH125_iso_1->Clone();
  VHFinal_iso_1->Add(WminusH125_iso_1);
  VHFinal_iso_1->Add(ZH125_iso_1);

  TH1F* EWKFinal_iso_1 = (TH1F*) EWKZLL_iso_1->Clone();
  EWKFinal_iso_1->Add(EWKZNuNu_iso_1);

  data_obs_iso_1->SetMarkerStyle(20);
  data_obs_iso_1->Sumw2();
  
  data_obs_Fake_iso_1->SetFillColor(kRed);
  data_obs_Fake_iso_1->SetLineColor(kBlack);

  embedded_iso_1->SetFillColor(kYellow);
  embedded_iso_1->SetLineColor(kBlack);

  DYFinal_iso_1->SetFillColor(kBlue);
  DYFinal_iso_1->SetLineColor(kBlack);

  TTFinal_iso_1->SetFillColor(kViolet-3);
  TTFinal_iso_1->SetLineColor(kBlack);

  VVFinal_iso_1->SetFillColor(kPink-3);
  VVFinal_iso_1->SetLineColor(kBlack);

  STFinal_iso_1->SetFillColor(kGreen);
  STFinal_iso_1->SetLineColor(kBlack);

  qqH_htt125_iso_1->SetFillColor(kCyan);
  qqH_htt125_iso_1->SetLineColor(kBlack);

  ggH_htt125_iso_1->SetFillColor(kCyan);
  ggH_htt125_iso_1->SetLineColor(kBlack);

  VHFinal_iso_1->SetFillColor(kOrange);
  VHFinal_iso_1->SetLineColor(kBlack);

  EWKFinal_iso_1->SetFillColor(kBlue-2);
  EWKFinal_iso_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_iso_1 = new THStack("BackgroundStack_iso_1","BackgroundStack_iso_1");
  BackgroundStack_iso_1->Add(data_obs_Fake_iso_1,"hist");
  BackgroundStack_iso_1->Add(DYFinal_iso_1,"hist");
  BackgroundStack_iso_1->Add(embedded_iso_1,"hist");
  BackgroundStack_iso_1->Add(TTFinal_iso_1,"hist");
  BackgroundStack_iso_1->Add(VVFinal_iso_1,"hist");
  BackgroundStack_iso_1->Add(STFinal_iso_1,"hist");
  BackgroundStack_iso_1->Add(qqH_htt125_iso_1,"hist");
  BackgroundStack_iso_1->Add(ggH_htt125_iso_1,"hist");
  BackgroundStack_iso_1->Add(VHFinal_iso_1,"hist");
  BackgroundStack_iso_1->Add(EWKFinal_iso_1,"hist");

  TH1F* BackgroundStack_iso_1_Errors = MakeStackErrors(BackgroundStack_iso_1);

  TPad* PlotPad_iso_1 = MakeRatioPlot(CanvasEight, BackgroundStack_iso_1, data_obs_iso_1,"iso_1");

  BackgroundStack_iso_1->SetMaximum(max(BackgroundStack_iso_1->GetMaximum(),data_obs_iso_1->GetMaximum()));

  BackgroundStack_iso_1->Draw();
  BackgroundStack_iso_1_Errors->Draw("SAME e2");
  BackgroundStack_iso_1->SetTitle("iso_1");
  data_obs_iso_1->Draw("SAME e1");
  BackgroundStack_iso_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_iso_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_iso_1,0,33);

  TLegend* Legend_iso_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_iso_1->AddEntry(embedded_iso_1,"embedded","f");
  Legend_iso_1->AddEntry(DYFinal_iso_1, "Other DY","f");
  Legend_iso_1->AddEntry(TTFinal_iso_1,"t#bar{t}","f");
  Legend_iso_1->AddEntry(VVFinal_iso_1,"Dibsoson","f");
  Legend_iso_1->AddEntry(STFinal_iso_1,"Single Top","f");
  Legend_iso_1->AddEntry(qqH_htt125_iso_1,"qqh","f");
  Legend_iso_1->AddEntry(ggH_htt125_iso_1,"ggH","f");
  Legend_iso_1->AddEntry(VHFinal_iso_1,"VH","f");
  Legend_iso_1->AddEntry(EWKFinal_iso_1,"EWK","f");
  Legend_iso_1->AddEntry(data_obs_Fake_iso_1,"Fakes","f");

  Legend_iso_1->Draw();

  //jpt_1
  TCanvas* CanvasNine = new TCanvas("CanvasNine","jpt_1",550,550);
  CanvasNine->SetTickx();
  CanvasNine->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jpt_1 = (TH1F*) HistoFile->Get("data_obs_jpt_1");
  TH1F* data_obs_Fake_jpt_1 = (TH1F*) HistoFile->Get("data_obs_Fake_jpt_1");
  TH1F* embedded_jpt_1 = (TH1F*) HistoFile->Get("embedded_jpt_1");
  TH1F* DY_jpt_1 = (TH1F*) HistoFile->Get("DY_jpt_1");
  TH1F* DYlow_jpt_1 = (TH1F*) HistoFile->Get("DYlow_jpt_1");
  TH1F* TTToHadronic_jpt_1 = (TH1F*) HistoFile->Get("TTToHadronic_jpt_1");
  TH1F* TTTo2L2Nu_jpt_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jpt_1");
  TH1F* TTToSemiLeptonic_jpt_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jpt_1");
  TH1F* WW4Q_jpt_1 = (TH1F*) HistoFile->Get("WW4Q_jpt_1");
  TH1F* WWLNuQQ_jpt_1 = (TH1F*) HistoFile->Get("WWLNuQQ_jpt_1");
  TH1F* WZ2L2Q_jpt_1 = (TH1F*) HistoFile->Get("WZ2L2Q_jpt_1");
  TH1F* WZ1L3Nu_jpt_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_jpt_1");
  TH1F* WZ3LNu_jpt_1 = (TH1F*) HistoFile->Get("WZ3LNu_jpt_1");
  TH1F* WZ1L1Nu2Q_jpt_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jpt_1");
  TH1F* ZZ4L_jpt_1 = (TH1F*) HistoFile->Get("ZZ4L_jpt_1");
  TH1F* ZZ2L2Nu_jpt_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jpt_1");
  TH1F* ZZ2L2Q_jpt_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_jpt_1");
  TH1F* ST_t_antitop_jpt_1 = (TH1F*) HistoFile->Get("ST_t_antitop_jpt_1");
  TH1F* ST_t_top_jpt_1 = (TH1F*) HistoFile->Get("ST_t_top_jpt_1");
  TH1F* ST_tW_antitop_jpt_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_jpt_1");
  TH1F* ST_tW_top_jpt_1 = (TH1F*) HistoFile->Get("ST_tW_top_jpt_1");
  TH1F* ggH_htt125_jpt_1 = (TH1F*) HistoFile->Get("ggH_htt125_jpt_1");
  TH1F* qqH_htt125_jpt_1 = (TH1F*) HistoFile->Get("qqH_htt125_jpt_1");  
  TH1F* WplusH125_jpt_1 = (TH1F*) HistoFile->Get("WplusH125_jpt_1");
  TH1F* WminusH125_jpt_1 = (TH1F*) HistoFile->Get("WminusH125_jpt_1");
  TH1F* ZH125_jpt_1 = (TH1F*) HistoFile->Get("ZH125_jpt_1");
  TH1F* EWKZLL_jpt_1 = (TH1F*) HistoFile->Get("EWKZLL_jpt_1");
  TH1F* EWKZNuNu_jpt_1 = (TH1F*) HistoFile->Get("EWKZNuNu_jpt_1");

  TH1F* DYFinal_jpt_1 = (TH1F*) DY_jpt_1->Clone();
  DYFinal_jpt_1->Add(DYlow_jpt_1);
  
  TH1F* TTFinal_jpt_1 = (TH1F*) TTToHadronic_jpt_1->Clone();
  TTFinal_jpt_1->Add(TTTo2L2Nu_jpt_1);
  TTFinal_jpt_1->Add(TTToSemiLeptonic_jpt_1);
  
  TH1F* VVFinal_jpt_1 = (TH1F*) WW4Q_jpt_1->Clone();
  VVFinal_jpt_1->Add(WWLNuQQ_jpt_1);
  VVFinal_jpt_1->Add(WZ2L2Q_jpt_1);
  VVFinal_jpt_1->Add(WZ1L3Nu_jpt_1);
  VVFinal_jpt_1->Add(WZ3LNu_jpt_1);
  VVFinal_jpt_1->Add(WZ1L1Nu2Q_jpt_1);
  VVFinal_jpt_1->Add(ZZ4L_jpt_1);
  VVFinal_jpt_1->Add(ZZ2L2Nu_jpt_1);
  VVFinal_jpt_1->Add(ZZ2L2Q_jpt_1);
  
  TH1F* STFinal_jpt_1 = (TH1F*) ST_t_antitop_jpt_1->Clone();
  STFinal_jpt_1->Add(ST_t_top_jpt_1);
  STFinal_jpt_1->Add(ST_tW_antitop_jpt_1);
  STFinal_jpt_1->Add(ST_tW_top_jpt_1);

  TH1F* VHFinal_jpt_1 = (TH1F*) WplusH125_jpt_1->Clone();
  VHFinal_jpt_1->Add(WminusH125_jpt_1);
  VHFinal_jpt_1->Add(ZH125_jpt_1);

  TH1F* EWKFinal_jpt_1 = (TH1F*) EWKZLL_jpt_1->Clone();
  EWKFinal_jpt_1->Add(EWKZNuNu_jpt_1);

  data_obs_jpt_1->SetMarkerStyle(20);
  data_obs_jpt_1->Sumw2();
  
  data_obs_Fake_jpt_1->SetFillColor(kRed);
  data_obs_Fake_jpt_1->SetLineColor(kBlack);

  embedded_jpt_1->SetFillColor(kYellow);
  embedded_jpt_1->SetLineColor(kBlack);

  DYFinal_jpt_1->SetFillColor(kBlue);
  DYFinal_jpt_1->SetLineColor(kBlack);

  TTFinal_jpt_1->SetFillColor(kViolet-3);
  TTFinal_jpt_1->SetLineColor(kBlack);

  VVFinal_jpt_1->SetFillColor(kPink-3);
  VVFinal_jpt_1->SetLineColor(kBlack);

  STFinal_jpt_1->SetFillColor(kGreen);
  STFinal_jpt_1->SetLineColor(kBlack);

  qqH_htt125_jpt_1->SetFillColor(kCyan);
  qqH_htt125_jpt_1->SetLineColor(kBlack);

  ggH_htt125_jpt_1->SetFillColor(kCyan);
  ggH_htt125_jpt_1->SetLineColor(kBlack);

  VHFinal_jpt_1->SetFillColor(kOrange);
  VHFinal_jpt_1->SetLineColor(kBlack);

  EWKFinal_jpt_1->SetFillColor(kBlue-2);
  EWKFinal_jpt_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jpt_1 = new THStack("BackgroundStack_jpt_1","BackgroundStack_jpt_1");
  BackgroundStack_jpt_1->Add(data_obs_Fake_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(DYFinal_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(embedded_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(TTFinal_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(VVFinal_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(STFinal_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(qqH_htt125_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(ggH_htt125_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(VHFinal_jpt_1,"hist");
  BackgroundStack_jpt_1->Add(EWKFinal_jpt_1,"hist");

  TH1F* BackgroundStack_jpt_1_Errors = MakeStackErrors(BackgroundStack_jpt_1);

  TPad* PlotPad_jpt_1 = MakeRatioPlot(CanvasNine, BackgroundStack_jpt_1, data_obs_jpt_1,"jpt_1");

  BackgroundStack_jpt_1->SetMaximum(max(BackgroundStack_jpt_1->GetMaximum(),data_obs_jpt_1->GetMaximum()));

  BackgroundStack_jpt_1->Draw();
  BackgroundStack_jpt_1_Errors->Draw("SAME e2");
  BackgroundStack_jpt_1->SetTitle("jpt_1");
  data_obs_jpt_1->Draw("SAME e1");
  BackgroundStack_jpt_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_jpt_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jpt_1,0,33);

  TLegend* Legend_jpt_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jpt_1->AddEntry(embedded_jpt_1,"embedded","f");
  Legend_jpt_1->AddEntry(DYFinal_jpt_1, "Other DY","f");
  Legend_jpt_1->AddEntry(TTFinal_jpt_1,"t#bar{t}","f");
  Legend_jpt_1->AddEntry(VVFinal_jpt_1,"Dibsoson","f");
  Legend_jpt_1->AddEntry(STFinal_jpt_1,"Single Top","f");
  Legend_jpt_1->AddEntry(qqH_htt125_jpt_1,"qqh","f");
  Legend_jpt_1->AddEntry(ggH_htt125_jpt_1,"ggH","f");
  Legend_jpt_1->AddEntry(VHFinal_jpt_1,"VH","f");
  Legend_jpt_1->AddEntry(EWKFinal_jpt_1,"EWK","f");
  Legend_jpt_1->AddEntry(data_obs_Fake_jpt_1,"Fakes","f");

  Legend_jpt_1->Draw();
  
  //jpt_2  
  TCanvas* CanvasTen = new TCanvas("CanvasTen","jpt_2",550,550);
  CanvasTen->SetTickx();
  CanvasTen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jpt_2 = (TH1F*) HistoFile->Get("data_obs_jpt_2");
  TH1F* data_obs_Fake_jpt_2 = (TH1F*) HistoFile->Get("data_obs_Fake_jpt_2");
  TH1F* embedded_jpt_2 = (TH1F*) HistoFile->Get("embedded_jpt_2");
  TH1F* DY_jpt_2 = (TH1F*) HistoFile->Get("DY_jpt_2");
  TH1F* DYlow_jpt_2 = (TH1F*) HistoFile->Get("DYlow_jpt_2");
  TH1F* TTToHadronic_jpt_2 = (TH1F*) HistoFile->Get("TTToHadronic_jpt_2");
  TH1F* TTTo2L2Nu_jpt_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jpt_2");
  TH1F* TTToSemiLeptonic_jpt_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jpt_2");
  TH1F* WW4Q_jpt_2 = (TH1F*) HistoFile->Get("WW4Q_jpt_2");
  TH1F* WWLNuQQ_jpt_2 = (TH1F*) HistoFile->Get("WWLNuQQ_jpt_2");
  TH1F* WZ2L2Q_jpt_2 = (TH1F*) HistoFile->Get("WZ2L2Q_jpt_2");
  TH1F* WZ1L3Nu_jpt_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_jpt_2");
  TH1F* WZ3LNu_jpt_2 = (TH1F*) HistoFile->Get("WZ3LNu_jpt_2");
  TH1F* WZ1L1Nu2Q_jpt_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jpt_2");
  TH1F* ZZ4L_jpt_2 = (TH1F*) HistoFile->Get("ZZ4L_jpt_2");
  TH1F* ZZ2L2Nu_jpt_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jpt_2");
  TH1F* ZZ2L2Q_jpt_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_jpt_2");
  TH1F* ST_t_antitop_jpt_2 = (TH1F*) HistoFile->Get("ST_t_antitop_jpt_2");
  TH1F* ST_t_top_jpt_2 = (TH1F*) HistoFile->Get("ST_t_top_jpt_2");
  TH1F* ST_tW_antitop_jpt_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_jpt_2");
  TH1F* ST_tW_top_jpt_2 = (TH1F*) HistoFile->Get("ST_tW_top_jpt_2");
  TH1F* ggH_htt125_jpt_2 = (TH1F*) HistoFile->Get("ggH_htt125_jpt_2");
  TH1F* qqH_htt125_jpt_2 = (TH1F*) HistoFile->Get("qqH_htt125_jpt_2");  
  TH1F* WplusH125_jpt_2 = (TH1F*) HistoFile->Get("WplusH125_jpt_2");
  TH1F* WminusH125_jpt_2 = (TH1F*) HistoFile->Get("WminusH125_jpt_2");
  TH1F* ZH125_jpt_2 = (TH1F*) HistoFile->Get("ZH125_jpt_2");
  TH1F* EWKZLL_jpt_2 = (TH1F*) HistoFile->Get("EWKZLL_jpt_2");
  TH1F* EWKZNuNu_jpt_2 = (TH1F*) HistoFile->Get("EWKZNuNu_jpt_2");

  TH1F* DYFinal_jpt_2 = (TH1F*) DY_jpt_2->Clone();
  DYFinal_jpt_2->Add(DYlow_jpt_2);
  
  TH1F* TTFinal_jpt_2 = (TH1F*) TTToHadronic_jpt_2->Clone();
  TTFinal_jpt_2->Add(TTTo2L2Nu_jpt_2);
  TTFinal_jpt_2->Add(TTToSemiLeptonic_jpt_2);
  
  TH1F* VVFinal_jpt_2 = (TH1F*) WW4Q_jpt_2->Clone();
  VVFinal_jpt_2->Add(WWLNuQQ_jpt_2);
  VVFinal_jpt_2->Add(WZ2L2Q_jpt_2);
  VVFinal_jpt_2->Add(WZ1L3Nu_jpt_2);
  VVFinal_jpt_2->Add(WZ3LNu_jpt_2);
  VVFinal_jpt_2->Add(WZ1L1Nu2Q_jpt_2);
  VVFinal_jpt_2->Add(ZZ4L_jpt_2);
  VVFinal_jpt_2->Add(ZZ2L2Nu_jpt_2);
  VVFinal_jpt_2->Add(ZZ2L2Q_jpt_2);
  
  TH1F* STFinal_jpt_2 = (TH1F*) ST_t_antitop_jpt_2->Clone();
  STFinal_jpt_2->Add(ST_t_top_jpt_2);
  STFinal_jpt_2->Add(ST_tW_antitop_jpt_2);
  STFinal_jpt_2->Add(ST_tW_top_jpt_2);

  TH1F* VHFinal_jpt_2 = (TH1F*) WplusH125_jpt_2->Clone();
  VHFinal_jpt_2->Add(WminusH125_jpt_2);
  VHFinal_jpt_2->Add(ZH125_jpt_2);

  TH1F* EWKFinal_jpt_2 = (TH1F*) EWKZLL_jpt_2->Clone();
  EWKFinal_jpt_2->Add(EWKZNuNu_jpt_2);

  data_obs_jpt_2->SetMarkerStyle(20);
  data_obs_jpt_2->Sumw2();
  
  data_obs_Fake_jpt_2->SetFillColor(kRed);
  data_obs_Fake_jpt_2->SetLineColor(kBlack);

  embedded_jpt_2->SetFillColor(kYellow);
  embedded_jpt_2->SetLineColor(kBlack);

  DYFinal_jpt_2->SetFillColor(kBlue);
  DYFinal_jpt_2->SetLineColor(kBlack);

  TTFinal_jpt_2->SetFillColor(kViolet-3);
  TTFinal_jpt_2->SetLineColor(kBlack);

  VVFinal_jpt_2->SetFillColor(kPink-3);
  VVFinal_jpt_2->SetLineColor(kBlack);

  STFinal_jpt_2->SetFillColor(kGreen);
  STFinal_jpt_2->SetLineColor(kBlack);

  qqH_htt125_jpt_2->SetFillColor(kCyan);
  qqH_htt125_jpt_2->SetLineColor(kBlack);

  ggH_htt125_jpt_2->SetFillColor(kCyan);
  ggH_htt125_jpt_2->SetLineColor(kBlack);

  VHFinal_jpt_2->SetFillColor(kOrange);
  VHFinal_jpt_2->SetLineColor(kBlack);

  EWKFinal_jpt_2->SetFillColor(kBlue-2);
  EWKFinal_jpt_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jpt_2 = new THStack("BackgroundStack_jpt_2","BackgroundStack_jpt_2");
  BackgroundStack_jpt_2->Add(data_obs_Fake_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(DYFinal_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(embedded_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(TTFinal_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(VVFinal_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(STFinal_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(qqH_htt125_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(ggH_htt125_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(VHFinal_jpt_2,"hist");
  BackgroundStack_jpt_2->Add(EWKFinal_jpt_2,"hist");

  TH1F* BackgroundStack_jpt_2_Errors = MakeStackErrors(BackgroundStack_jpt_2);

  TPad* PlotPad_jpt_2 = MakeRatioPlot(CanvasTen, BackgroundStack_jpt_2, data_obs_jpt_2,"jpt_2");

  BackgroundStack_jpt_2->SetMaximum(max(BackgroundStack_jpt_2->GetMaximum(),data_obs_jpt_2->GetMaximum()));

  BackgroundStack_jpt_2->Draw();
  BackgroundStack_jpt_2_Errors->Draw("SAME e2");
  BackgroundStack_jpt_2->SetTitle("jpt_2");
  data_obs_jpt_2->Draw("SAME e1");
  BackgroundStack_jpt_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_jpt_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jpt_2,0,33);

  TLegend* Legend_jpt_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jpt_2->AddEntry(embedded_jpt_2,"embedded","f");
  Legend_jpt_2->AddEntry(DYFinal_jpt_2, "Other DY","f");
  Legend_jpt_2->AddEntry(TTFinal_jpt_2,"t#bar{t}","f");
  Legend_jpt_2->AddEntry(VVFinal_jpt_2,"Dibsoson","f");
  Legend_jpt_2->AddEntry(STFinal_jpt_2,"Single Top","f");
  Legend_jpt_2->AddEntry(qqH_htt125_jpt_2,"qqh","f");
  Legend_jpt_2->AddEntry(ggH_htt125_jpt_2,"ggH","f");
  Legend_jpt_2->AddEntry(VHFinal_jpt_2,"VH","f");
  Legend_jpt_2->AddEntry(EWKFinal_jpt_2,"EWK","f");
  Legend_jpt_2->AddEntry(data_obs_Fake_jpt_2,"Fakes","f");

  Legend_jpt_2->Draw();

  //jeta_1
  TCanvas* CanvasEleven = new TCanvas("CanvasEleven","jeta_1",550,550);
  CanvasEleven->SetTickx();
  CanvasEleven->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jeta_1 = (TH1F*) HistoFile->Get("data_obs_jeta_1");
  TH1F* data_obs_Fake_jeta_1 = (TH1F*) HistoFile->Get("data_obs_Fake_jeta_1");
  TH1F* embedded_jeta_1 = (TH1F*) HistoFile->Get("embedded_jeta_1");
  TH1F* DY_jeta_1 = (TH1F*) HistoFile->Get("DY_jeta_1");
  TH1F* DYlow_jeta_1 = (TH1F*) HistoFile->Get("DYlow_jeta_1");
  TH1F* TTToHadronic_jeta_1 = (TH1F*) HistoFile->Get("TTToHadronic_jeta_1");
  TH1F* TTTo2L2Nu_jeta_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jeta_1");
  TH1F* TTToSemiLeptonic_jeta_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jeta_1");
  TH1F* WW4Q_jeta_1 = (TH1F*) HistoFile->Get("WW4Q_jeta_1");
  TH1F* WWLNuQQ_jeta_1 = (TH1F*) HistoFile->Get("WWLNuQQ_jeta_1");
  TH1F* WZ2L2Q_jeta_1 = (TH1F*) HistoFile->Get("WZ2L2Q_jeta_1");
  TH1F* WZ1L3Nu_jeta_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_jeta_1");
  TH1F* WZ3LNu_jeta_1 = (TH1F*) HistoFile->Get("WZ3LNu_jeta_1");
  TH1F* WZ1L1Nu2Q_jeta_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jeta_1");
  TH1F* ZZ4L_jeta_1 = (TH1F*) HistoFile->Get("ZZ4L_jeta_1");
  TH1F* ZZ2L2Nu_jeta_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jeta_1");
  TH1F* ZZ2L2Q_jeta_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_jeta_1");
  TH1F* ST_t_antitop_jeta_1 = (TH1F*) HistoFile->Get("ST_t_antitop_jeta_1");
  TH1F* ST_t_top_jeta_1 = (TH1F*) HistoFile->Get("ST_t_top_jeta_1");
  TH1F* ST_tW_antitop_jeta_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_jeta_1");
  TH1F* ST_tW_top_jeta_1 = (TH1F*) HistoFile->Get("ST_tW_top_jeta_1");
  TH1F* ggH_htt125_jeta_1 = (TH1F*) HistoFile->Get("ggH_htt125_jeta_1");
  TH1F* qqH_htt125_jeta_1 = (TH1F*) HistoFile->Get("qqH_htt125_jeta_1");  
  TH1F* WplusH125_jeta_1 = (TH1F*) HistoFile->Get("WplusH125_jeta_1");
  TH1F* WminusH125_jeta_1 = (TH1F*) HistoFile->Get("WminusH125_jeta_1");
  TH1F* ZH125_jeta_1 = (TH1F*) HistoFile->Get("ZH125_jeta_1");
  TH1F* EWKZLL_jeta_1 = (TH1F*) HistoFile->Get("EWKZLL_jeta_1");
  TH1F* EWKZNuNu_jeta_1 = (TH1F*) HistoFile->Get("EWKZNuNu_jeta_1");

  TH1F* DYFinal_jeta_1 = (TH1F*) DY_jeta_1->Clone();
  DYFinal_jeta_1->Add(DYlow_jeta_1);
  
  TH1F* TTFinal_jeta_1 = (TH1F*) TTToHadronic_jeta_1->Clone();
  TTFinal_jeta_1->Add(TTTo2L2Nu_jeta_1);
  TTFinal_jeta_1->Add(TTToSemiLeptonic_jeta_1);
  
  TH1F* VVFinal_jeta_1 = (TH1F*) WW4Q_jeta_1->Clone();
  VVFinal_jeta_1->Add(WWLNuQQ_jeta_1);
  VVFinal_jeta_1->Add(WZ2L2Q_jeta_1);
  VVFinal_jeta_1->Add(WZ1L3Nu_jeta_1);
  VVFinal_jeta_1->Add(WZ3LNu_jeta_1);
  VVFinal_jeta_1->Add(WZ1L1Nu2Q_jeta_1);
  VVFinal_jeta_1->Add(ZZ4L_jeta_1);
  VVFinal_jeta_1->Add(ZZ2L2Nu_jeta_1);
  VVFinal_jeta_1->Add(ZZ2L2Q_jeta_1);
  
  TH1F* STFinal_jeta_1 = (TH1F*) ST_t_antitop_jeta_1->Clone();
  STFinal_jeta_1->Add(ST_t_top_jeta_1);
  STFinal_jeta_1->Add(ST_tW_antitop_jeta_1);
  STFinal_jeta_1->Add(ST_tW_top_jeta_1);

  TH1F* VHFinal_jeta_1 = (TH1F*) WplusH125_jeta_1->Clone();
  VHFinal_jeta_1->Add(WminusH125_jeta_1);
  VHFinal_jeta_1->Add(ZH125_jeta_1);

  TH1F* EWKFinal_jeta_1 = (TH1F*) EWKZLL_jeta_1->Clone();
  EWKFinal_jeta_1->Add(EWKZNuNu_jeta_1);

  data_obs_jeta_1->SetMarkerStyle(20);
  data_obs_jeta_1->Sumw2();
  
  data_obs_Fake_jeta_1->SetFillColor(kRed);
  data_obs_Fake_jeta_1->SetLineColor(kBlack);

  embedded_jeta_1->SetFillColor(kYellow);
  embedded_jeta_1->SetLineColor(kBlack);

  DYFinal_jeta_1->SetFillColor(kBlue);
  DYFinal_jeta_1->SetLineColor(kBlack);

  TTFinal_jeta_1->SetFillColor(kViolet-3);
  TTFinal_jeta_1->SetLineColor(kBlack);

  VVFinal_jeta_1->SetFillColor(kPink-3);
  VVFinal_jeta_1->SetLineColor(kBlack);

  STFinal_jeta_1->SetFillColor(kGreen);
  STFinal_jeta_1->SetLineColor(kBlack);

  qqH_htt125_jeta_1->SetFillColor(kCyan);
  qqH_htt125_jeta_1->SetLineColor(kBlack);

  ggH_htt125_jeta_1->SetFillColor(kCyan);
  ggH_htt125_jeta_1->SetLineColor(kBlack);

  VHFinal_jeta_1->SetFillColor(kOrange);
  VHFinal_jeta_1->SetLineColor(kBlack);

  EWKFinal_jeta_1->SetFillColor(kBlue-2);
  EWKFinal_jeta_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jeta_1 = new THStack("BackgroundStack_jeta_1","BackgroundStack_jeta_1");
  BackgroundStack_jeta_1->Add(data_obs_Fake_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(DYFinal_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(embedded_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(TTFinal_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(VVFinal_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(STFinal_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(qqH_htt125_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(ggH_htt125_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(VHFinal_jeta_1,"hist");
  BackgroundStack_jeta_1->Add(EWKFinal_jeta_1,"hist");

  TH1F* BackgroundStack_jeta_1_Errors = MakeStackErrors(BackgroundStack_jeta_1);

  TPad* PlotPad_jeta_1 = MakeRatioPlot(CanvasEleven, BackgroundStack_jeta_1, data_obs_jeta_1,"jeta_1");

  BackgroundStack_jeta_1->SetMaximum(max(BackgroundStack_jeta_1->GetMaximum(),data_obs_jeta_1->GetMaximum()));

  BackgroundStack_jeta_1->Draw();
  BackgroundStack_jeta_1_Errors->Draw("SAME e2");
  BackgroundStack_jeta_1->SetTitle("jeta_1");
  data_obs_jeta_1->Draw("SAME e1");
  BackgroundStack_jeta_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_jeta_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jeta_1,0,33);

  TLegend* Legend_jeta_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jeta_1->AddEntry(embedded_jeta_1,"embedded","f");
  Legend_jeta_1->AddEntry(DYFinal_jeta_1, "Other DY","f");
  Legend_jeta_1->AddEntry(TTFinal_jeta_1,"t#bar{t}","f");
  Legend_jeta_1->AddEntry(VVFinal_jeta_1,"Dibsoson","f");
  Legend_jeta_1->AddEntry(STFinal_jeta_1,"Single Top","f");
  Legend_jeta_1->AddEntry(qqH_htt125_jeta_1,"qqh","f");
  Legend_jeta_1->AddEntry(ggH_htt125_jeta_1,"ggH","f");
  Legend_jeta_1->AddEntry(VHFinal_jeta_1,"VH","f");
  Legend_jeta_1->AddEntry(EWKFinal_jeta_1,"EWK","f");
  Legend_jeta_1->AddEntry(data_obs_Fake_jeta_1,"Fakes","f");

  Legend_jeta_1->Draw();

  //jeta_2
  TCanvas* CanvasTwelve = new TCanvas("CanvasTwelve","jeta_2",550,550);
  CanvasTwelve->SetTickx();
  CanvasTwelve->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jeta_2 = (TH1F*) HistoFile->Get("data_obs_jeta_2");
  TH1F* data_obs_Fake_jeta_2 = (TH1F*) HistoFile->Get("data_obs_Fake_jeta_2");
  TH1F* embedded_jeta_2 = (TH1F*) HistoFile->Get("embedded_jeta_2");
  TH1F* DY_jeta_2 = (TH1F*) HistoFile->Get("DY_jeta_2");
  TH1F* DYlow_jeta_2 = (TH1F*) HistoFile->Get("DYlow_jeta_2");
  TH1F* TTToHadronic_jeta_2 = (TH1F*) HistoFile->Get("TTToHadronic_jeta_2");
  TH1F* TTTo2L2Nu_jeta_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jeta_2");
  TH1F* TTToSemiLeptonic_jeta_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jeta_2");
  TH1F* WW4Q_jeta_2 = (TH1F*) HistoFile->Get("WW4Q_jeta_2");
  TH1F* WWLNuQQ_jeta_2 = (TH1F*) HistoFile->Get("WWLNuQQ_jeta_2");
  TH1F* WZ2L2Q_jeta_2 = (TH1F*) HistoFile->Get("WZ2L2Q_jeta_2");
  TH1F* WZ1L3Nu_jeta_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_jeta_2");
  TH1F* WZ3LNu_jeta_2 = (TH1F*) HistoFile->Get("WZ3LNu_jeta_2");
  TH1F* WZ1L1Nu2Q_jeta_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jeta_2");
  TH1F* ZZ4L_jeta_2 = (TH1F*) HistoFile->Get("ZZ4L_jeta_2");
  TH1F* ZZ2L2Nu_jeta_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jeta_2");
  TH1F* ZZ2L2Q_jeta_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_jeta_2");
  TH1F* ST_t_antitop_jeta_2 = (TH1F*) HistoFile->Get("ST_t_antitop_jeta_2");
  TH1F* ST_t_top_jeta_2 = (TH1F*) HistoFile->Get("ST_t_top_jeta_2");
  TH1F* ST_tW_antitop_jeta_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_jeta_2");
  TH1F* ST_tW_top_jeta_2 = (TH1F*) HistoFile->Get("ST_tW_top_jeta_2");
  TH1F* ggH_htt125_jeta_2 = (TH1F*) HistoFile->Get("ggH_htt125_jeta_2");
  TH1F* qqH_htt125_jeta_2 = (TH1F*) HistoFile->Get("qqH_htt125_jeta_2");  
  TH1F* WplusH125_jeta_2 = (TH1F*) HistoFile->Get("WplusH125_jeta_2");
  TH1F* WminusH125_jeta_2 = (TH1F*) HistoFile->Get("WminusH125_jeta_2");
  TH1F* ZH125_jeta_2 = (TH1F*) HistoFile->Get("ZH125_jeta_2");
  TH1F* EWKZLL_jeta_2 = (TH1F*) HistoFile->Get("EWKZLL_jeta_2");
  TH1F* EWKZNuNu_jeta_2 = (TH1F*) HistoFile->Get("EWKZNuNu_jeta_2");

  TH1F* DYFinal_jeta_2 = (TH1F*) DY_jeta_2->Clone();
  DYFinal_jeta_2->Add(DYlow_jeta_2);
  
  TH1F* TTFinal_jeta_2 = (TH1F*) TTToHadronic_jeta_2->Clone();
  TTFinal_jeta_2->Add(TTTo2L2Nu_jeta_2);
  TTFinal_jeta_2->Add(TTToSemiLeptonic_jeta_2);
  
  TH1F* VVFinal_jeta_2 = (TH1F*) WW4Q_jeta_2->Clone();
  VVFinal_jeta_2->Add(WWLNuQQ_jeta_2);
  VVFinal_jeta_2->Add(WZ2L2Q_jeta_2);
  VVFinal_jeta_2->Add(WZ1L3Nu_jeta_2);
  VVFinal_jeta_2->Add(WZ3LNu_jeta_2);
  VVFinal_jeta_2->Add(WZ1L1Nu2Q_jeta_2);
  VVFinal_jeta_2->Add(ZZ4L_jeta_2);
  VVFinal_jeta_2->Add(ZZ2L2Nu_jeta_2);
  VVFinal_jeta_2->Add(ZZ2L2Q_jeta_2);
  
  TH1F* STFinal_jeta_2 = (TH1F*) ST_t_antitop_jeta_2->Clone();
  STFinal_jeta_2->Add(ST_t_top_jeta_2);
  STFinal_jeta_2->Add(ST_tW_antitop_jeta_2);
  STFinal_jeta_2->Add(ST_tW_top_jeta_2);

  TH1F* VHFinal_jeta_2 = (TH1F*) WplusH125_jeta_2->Clone();
  VHFinal_jeta_2->Add(WminusH125_jeta_2);
  VHFinal_jeta_2->Add(ZH125_jeta_2);

  TH1F* EWKFinal_jeta_2 = (TH1F*) EWKZLL_jeta_2->Clone();
  EWKFinal_jeta_2->Add(EWKZNuNu_jeta_2);

  data_obs_jeta_2->SetMarkerStyle(20);
  data_obs_jeta_2->Sumw2();
  
  data_obs_Fake_jeta_2->SetFillColor(kRed);
  data_obs_Fake_jeta_2->SetLineColor(kBlack);

  embedded_jeta_2->SetFillColor(kYellow);
  embedded_jeta_2->SetLineColor(kBlack);

  DYFinal_jeta_2->SetFillColor(kBlue);
  DYFinal_jeta_2->SetLineColor(kBlack);

  TTFinal_jeta_2->SetFillColor(kViolet-3);
  TTFinal_jeta_2->SetLineColor(kBlack);

  VVFinal_jeta_2->SetFillColor(kPink-3);
  VVFinal_jeta_2->SetLineColor(kBlack);

  STFinal_jeta_2->SetFillColor(kGreen);
  STFinal_jeta_2->SetLineColor(kBlack);

  qqH_htt125_jeta_2->SetFillColor(kCyan);
  qqH_htt125_jeta_2->SetLineColor(kBlack);

  ggH_htt125_jeta_2->SetFillColor(kCyan);
  ggH_htt125_jeta_2->SetLineColor(kBlack);

  VHFinal_jeta_2->SetFillColor(kOrange);
  VHFinal_jeta_2->SetLineColor(kBlack);

  EWKFinal_jeta_2->SetFillColor(kBlue-2);
  EWKFinal_jeta_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jeta_2 = new THStack("BackgroundStack_jeta_2","BackgroundStack_jeta_2");
  BackgroundStack_jeta_2->Add(data_obs_Fake_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(DYFinal_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(embedded_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(TTFinal_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(VVFinal_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(STFinal_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(qqH_htt125_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(ggH_htt125_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(VHFinal_jeta_2,"hist");
  BackgroundStack_jeta_2->Add(EWKFinal_jeta_2,"hist");

  TH1F* BackgroundStack_jeta_2_Errors = MakeStackErrors(BackgroundStack_jeta_2);

  TPad* PlotPad_jeta_2 = MakeRatioPlot(CanvasTwelve, BackgroundStack_jeta_2, data_obs_jeta_2,"jeta_2");

  BackgroundStack_jeta_2->SetMaximum(max(BackgroundStack_jeta_2->GetMaximum(),data_obs_jeta_2->GetMaximum()));

  BackgroundStack_jeta_2->Draw();
  BackgroundStack_jeta_2_Errors->Draw("SAME e2");
  BackgroundStack_jeta_2->SetTitle("jeta_2");
  data_obs_jeta_2->Draw("SAME e1");
  BackgroundStack_jeta_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_jeta_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jeta_2,0,33);

  TLegend* Legend_jeta_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jeta_2->AddEntry(embedded_jeta_2,"embedded","f");
  Legend_jeta_2->AddEntry(DYFinal_jeta_2, "Other DY","f");
  Legend_jeta_2->AddEntry(TTFinal_jeta_2,"t#bar{t}","f");
  Legend_jeta_2->AddEntry(VVFinal_jeta_2,"Dibsoson","f");
  Legend_jeta_2->AddEntry(STFinal_jeta_2,"Single Top","f");
  Legend_jeta_2->AddEntry(qqH_htt125_jeta_2,"qqh","f");
  Legend_jeta_2->AddEntry(ggH_htt125_jeta_2,"ggH","f");
  Legend_jeta_2->AddEntry(VHFinal_jeta_2,"VH","f");
  Legend_jeta_2->AddEntry(EWKFinal_jeta_2,"EWK","f");
  Legend_jeta_2->AddEntry(data_obs_Fake_jeta_2,"Fakes","f");

  Legend_jeta_2->Draw();

  //jphi_1
  TCanvas* CanvasThirteen = new TCanvas("CanvasThirteen","jphi_1",550,550);
  CanvasThirteen->SetTickx();
  CanvasThirteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jphi_1 = (TH1F*) HistoFile->Get("data_obs_jphi_1");
  TH1F* data_obs_Fake_jphi_1 = (TH1F*) HistoFile->Get("data_obs_Fake_jphi_1");
  TH1F* embedded_jphi_1 = (TH1F*) HistoFile->Get("embedded_jphi_1");
  TH1F* DY_jphi_1 = (TH1F*) HistoFile->Get("DY_jphi_1");
  TH1F* DYlow_jphi_1 = (TH1F*) HistoFile->Get("DYlow_jphi_1");
  TH1F* TTToHadronic_jphi_1 = (TH1F*) HistoFile->Get("TTToHadronic_jphi_1");
  TH1F* TTTo2L2Nu_jphi_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jphi_1");
  TH1F* TTToSemiLeptonic_jphi_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jphi_1");
  TH1F* WW4Q_jphi_1 = (TH1F*) HistoFile->Get("WW4Q_jphi_1");
  TH1F* WWLNuQQ_jphi_1 = (TH1F*) HistoFile->Get("WWLNuQQ_jphi_1");
  TH1F* WZ2L2Q_jphi_1 = (TH1F*) HistoFile->Get("WZ2L2Q_jphi_1");
  TH1F* WZ1L3Nu_jphi_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_jphi_1");
  TH1F* WZ3LNu_jphi_1 = (TH1F*) HistoFile->Get("WZ3LNu_jphi_1");
  TH1F* WZ1L1Nu2Q_jphi_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jphi_1");
  TH1F* ZZ4L_jphi_1 = (TH1F*) HistoFile->Get("ZZ4L_jphi_1");
  TH1F* ZZ2L2Nu_jphi_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jphi_1");
  TH1F* ZZ2L2Q_jphi_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_jphi_1");
  TH1F* ST_t_antitop_jphi_1 = (TH1F*) HistoFile->Get("ST_t_antitop_jphi_1");
  TH1F* ST_t_top_jphi_1 = (TH1F*) HistoFile->Get("ST_t_top_jphi_1");
  TH1F* ST_tW_antitop_jphi_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_jphi_1");
  TH1F* ST_tW_top_jphi_1 = (TH1F*) HistoFile->Get("ST_tW_top_jphi_1");
  TH1F* ggH_htt125_jphi_1 = (TH1F*) HistoFile->Get("ggH_htt125_jphi_1");
  TH1F* qqH_htt125_jphi_1 = (TH1F*) HistoFile->Get("qqH_htt125_jphi_1");  
  TH1F* WplusH125_jphi_1 = (TH1F*) HistoFile->Get("WplusH125_jphi_1");
  TH1F* WminusH125_jphi_1 = (TH1F*) HistoFile->Get("WminusH125_jphi_1");
  TH1F* ZH125_jphi_1 = (TH1F*) HistoFile->Get("ZH125_jphi_1");
  TH1F* EWKZLL_jphi_1 = (TH1F*) HistoFile->Get("EWKZLL_jphi_1");
  TH1F* EWKZNuNu_jphi_1 = (TH1F*) HistoFile->Get("EWKZNuNu_jphi_1");

  TH1F* DYFinal_jphi_1 = (TH1F*) DY_jphi_1->Clone();
  DYFinal_jphi_1->Add(DYlow_jphi_1);
  
  TH1F* TTFinal_jphi_1 = (TH1F*) TTToHadronic_jphi_1->Clone();
  TTFinal_jphi_1->Add(TTTo2L2Nu_jphi_1);
  TTFinal_jphi_1->Add(TTToSemiLeptonic_jphi_1);
  
  TH1F* VVFinal_jphi_1 = (TH1F*) WW4Q_jphi_1->Clone();
  VVFinal_jphi_1->Add(WWLNuQQ_jphi_1);
  VVFinal_jphi_1->Add(WZ2L2Q_jphi_1);
  VVFinal_jphi_1->Add(WZ1L3Nu_jphi_1);
  VVFinal_jphi_1->Add(WZ3LNu_jphi_1);
  VVFinal_jphi_1->Add(WZ1L1Nu2Q_jphi_1);
  VVFinal_jphi_1->Add(ZZ4L_jphi_1);
  VVFinal_jphi_1->Add(ZZ2L2Nu_jphi_1);
  VVFinal_jphi_1->Add(ZZ2L2Q_jphi_1);
  
  TH1F* STFinal_jphi_1 = (TH1F*) ST_t_antitop_jphi_1->Clone();
  STFinal_jphi_1->Add(ST_t_top_jphi_1);
  STFinal_jphi_1->Add(ST_tW_antitop_jphi_1);
  STFinal_jphi_1->Add(ST_tW_top_jphi_1);

  TH1F* VHFinal_jphi_1 = (TH1F*) WplusH125_jphi_1->Clone();
  VHFinal_jphi_1->Add(WminusH125_jphi_1);
  VHFinal_jphi_1->Add(ZH125_jphi_1);

  TH1F* EWKFinal_jphi_1 = (TH1F*) EWKZLL_jphi_1->Clone();
  EWKFinal_jphi_1->Add(EWKZNuNu_jphi_1);

  data_obs_jphi_1->SetMarkerStyle(20);
  data_obs_jphi_1->Sumw2();
  
  data_obs_Fake_jphi_1->SetFillColor(kRed);
  data_obs_Fake_jphi_1->SetLineColor(kBlack);

  embedded_jphi_1->SetFillColor(kYellow);
  embedded_jphi_1->SetLineColor(kBlack);

  DYFinal_jphi_1->SetFillColor(kBlue);
  DYFinal_jphi_1->SetLineColor(kBlack);

  TTFinal_jphi_1->SetFillColor(kViolet-3);
  TTFinal_jphi_1->SetLineColor(kBlack);

  VVFinal_jphi_1->SetFillColor(kPink-3);
  VVFinal_jphi_1->SetLineColor(kBlack);

  STFinal_jphi_1->SetFillColor(kGreen);
  STFinal_jphi_1->SetLineColor(kBlack);

  qqH_htt125_jphi_1->SetFillColor(kCyan);
  qqH_htt125_jphi_1->SetLineColor(kBlack);

  ggH_htt125_jphi_1->SetFillColor(kCyan);
  ggH_htt125_jphi_1->SetLineColor(kBlack);

  VHFinal_jphi_1->SetFillColor(kOrange);
  VHFinal_jphi_1->SetLineColor(kBlack);

  EWKFinal_jphi_1->SetFillColor(kBlue-2);
  EWKFinal_jphi_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jphi_1 = new THStack("BackgroundStack_jphi_1","BackgroundStack_jphi_1");
  BackgroundStack_jphi_1->Add(data_obs_Fake_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(DYFinal_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(embedded_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(TTFinal_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(VVFinal_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(STFinal_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(qqH_htt125_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(ggH_htt125_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(VHFinal_jphi_1,"hist");
  BackgroundStack_jphi_1->Add(EWKFinal_jphi_1,"hist");

  TH1F* BackgroundStack_jphi_1_Errors = MakeStackErrors(BackgroundStack_jphi_1);

  TPad* PlotPad_jphi_1 = MakeRatioPlot(CanvasThirteen, BackgroundStack_jphi_1, data_obs_jphi_1,"jphi_1");

  BackgroundStack_jphi_1->SetMaximum(max(BackgroundStack_jphi_1->GetMaximum(),data_obs_jphi_1->GetMaximum()));

  BackgroundStack_jphi_1->Draw();
  BackgroundStack_jphi_1_Errors->Draw("SAME e2");
  BackgroundStack_jphi_1->SetTitle("jphi_1");
  data_obs_jphi_1->Draw("SAME e1");
  BackgroundStack_jphi_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_jphi_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jphi_1,0,33);

  TLegend* Legend_jphi_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jphi_1->AddEntry(embedded_jphi_1,"embedded","f");
  Legend_jphi_1->AddEntry(DYFinal_jphi_1, "Other DY","f");
  Legend_jphi_1->AddEntry(TTFinal_jphi_1,"t#bar{t}","f");
  Legend_jphi_1->AddEntry(VVFinal_jphi_1,"Dibsoson","f");
  Legend_jphi_1->AddEntry(STFinal_jphi_1,"Single Top","f");
  Legend_jphi_1->AddEntry(qqH_htt125_jphi_1,"qqh","f");
  Legend_jphi_1->AddEntry(ggH_htt125_jphi_1,"ggH","f");
  Legend_jphi_1->AddEntry(VHFinal_jphi_1,"VH","f");
  Legend_jphi_1->AddEntry(EWKFinal_jphi_1,"EWK","f");
  Legend_jphi_1->AddEntry(data_obs_Fake_jphi_1,"Fakes","f");

  Legend_jphi_1->Draw();

  //jphi_2
  TCanvas* CanvasFourteen = new TCanvas("CanvasFourteen","jphi_2",550,550);
  CanvasFourteen->SetTickx();
  CanvasFourteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_jphi_2 = (TH1F*) HistoFile->Get("data_obs_jphi_2");
  TH1F* data_obs_Fake_jphi_2 = (TH1F*) HistoFile->Get("data_obs_Fake_jphi_2");
  TH1F* embedded_jphi_2 = (TH1F*) HistoFile->Get("embedded_jphi_2");
  TH1F* DY_jphi_2 = (TH1F*) HistoFile->Get("DY_jphi_2");
  TH1F* DYlow_jphi_2 = (TH1F*) HistoFile->Get("DYlow_jphi_2");
  TH1F* TTToHadronic_jphi_2 = (TH1F*) HistoFile->Get("TTToHadronic_jphi_2");
  TH1F* TTTo2L2Nu_jphi_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_jphi_2");
  TH1F* TTToSemiLeptonic_jphi_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_jphi_2");
  TH1F* WW4Q_jphi_2 = (TH1F*) HistoFile->Get("WW4Q_jphi_2");
  TH1F* WWLNuQQ_jphi_2 = (TH1F*) HistoFile->Get("WWLNuQQ_jphi_2");
  TH1F* WZ2L2Q_jphi_2 = (TH1F*) HistoFile->Get("WZ2L2Q_jphi_2");
  TH1F* WZ1L3Nu_jphi_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_jphi_2");
  TH1F* WZ3LNu_jphi_2 = (TH1F*) HistoFile->Get("WZ3LNu_jphi_2");
  TH1F* WZ1L1Nu2Q_jphi_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_jphi_2");
  TH1F* ZZ4L_jphi_2 = (TH1F*) HistoFile->Get("ZZ4L_jphi_2");
  TH1F* ZZ2L2Nu_jphi_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_jphi_2");
  TH1F* ZZ2L2Q_jphi_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_jphi_2");
  TH1F* ST_t_antitop_jphi_2 = (TH1F*) HistoFile->Get("ST_t_antitop_jphi_2");
  TH1F* ST_t_top_jphi_2 = (TH1F*) HistoFile->Get("ST_t_top_jphi_2");
  TH1F* ST_tW_antitop_jphi_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_jphi_2");
  TH1F* ST_tW_top_jphi_2 = (TH1F*) HistoFile->Get("ST_tW_top_jphi_2");
  TH1F* ggH_htt125_jphi_2 = (TH1F*) HistoFile->Get("ggH_htt125_jphi_2");
  TH1F* qqH_htt125_jphi_2 = (TH1F*) HistoFile->Get("qqH_htt125_jphi_2");  
  TH1F* WplusH125_jphi_2 = (TH1F*) HistoFile->Get("WplusH125_jphi_2");
  TH1F* WminusH125_jphi_2 = (TH1F*) HistoFile->Get("WminusH125_jphi_2");
  TH1F* ZH125_jphi_2 = (TH1F*) HistoFile->Get("ZH125_jphi_2");
  TH1F* EWKZLL_jphi_2 = (TH1F*) HistoFile->Get("EWKZLL_jphi_2");
  TH1F* EWKZNuNu_jphi_2 = (TH1F*) HistoFile->Get("EWKZNuNu_jphi_2");

  TH1F* DYFinal_jphi_2 = (TH1F*) DY_jphi_2->Clone();
  DYFinal_jphi_2->Add(DYlow_jphi_2);
  
  TH1F* TTFinal_jphi_2 = (TH1F*) TTToHadronic_jphi_2->Clone();
  TTFinal_jphi_2->Add(TTTo2L2Nu_jphi_2);
  TTFinal_jphi_2->Add(TTToSemiLeptonic_jphi_2);
  
  TH1F* VVFinal_jphi_2 = (TH1F*) WW4Q_jphi_2->Clone();
  VVFinal_jphi_2->Add(WWLNuQQ_jphi_2);
  VVFinal_jphi_2->Add(WZ2L2Q_jphi_2);
  VVFinal_jphi_2->Add(WZ1L3Nu_jphi_2);
  VVFinal_jphi_2->Add(WZ3LNu_jphi_2);
  VVFinal_jphi_2->Add(WZ1L1Nu2Q_jphi_2);
  VVFinal_jphi_2->Add(ZZ4L_jphi_2);
  VVFinal_jphi_2->Add(ZZ2L2Nu_jphi_2);
  VVFinal_jphi_2->Add(ZZ2L2Q_jphi_2);
  
  TH1F* STFinal_jphi_2 = (TH1F*) ST_t_antitop_jphi_2->Clone();
  STFinal_jphi_2->Add(ST_t_top_jphi_2);
  STFinal_jphi_2->Add(ST_tW_antitop_jphi_2);
  STFinal_jphi_2->Add(ST_tW_top_jphi_2);

  TH1F* VHFinal_jphi_2 = (TH1F*) WplusH125_jphi_2->Clone();
  VHFinal_jphi_2->Add(WminusH125_jphi_2);
  VHFinal_jphi_2->Add(ZH125_jphi_2);

  TH1F* EWKFinal_jphi_2 = (TH1F*) EWKZLL_jphi_2->Clone();
  EWKFinal_jphi_2->Add(EWKZNuNu_jphi_2);

  data_obs_jphi_2->SetMarkerStyle(20);
  data_obs_jphi_2->Sumw2();
  
  data_obs_Fake_jphi_2->SetFillColor(kRed);
  data_obs_Fake_jphi_2->SetLineColor(kBlack);

  embedded_jphi_2->SetFillColor(kYellow);
  embedded_jphi_2->SetLineColor(kBlack);

  DYFinal_jphi_2->SetFillColor(kBlue);
  DYFinal_jphi_2->SetLineColor(kBlack);

  TTFinal_jphi_2->SetFillColor(kViolet-3);
  TTFinal_jphi_2->SetLineColor(kBlack);

  VVFinal_jphi_2->SetFillColor(kPink-3);
  VVFinal_jphi_2->SetLineColor(kBlack);

  STFinal_jphi_2->SetFillColor(kGreen);
  STFinal_jphi_2->SetLineColor(kBlack);

  qqH_htt125_jphi_2->SetFillColor(kCyan);
  qqH_htt125_jphi_2->SetLineColor(kBlack);

  ggH_htt125_jphi_2->SetFillColor(kCyan);
  ggH_htt125_jphi_2->SetLineColor(kBlack);

  VHFinal_jphi_2->SetFillColor(kOrange);
  VHFinal_jphi_2->SetLineColor(kBlack);

  EWKFinal_jphi_2->SetFillColor(kBlue-2);
  EWKFinal_jphi_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_jphi_2 = new THStack("BackgroundStack_jphi_2","BackgroundStack_jphi_2");
  BackgroundStack_jphi_2->Add(data_obs_Fake_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(DYFinal_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(embedded_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(TTFinal_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(VVFinal_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(STFinal_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(qqH_htt125_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(ggH_htt125_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(VHFinal_jphi_2,"hist");
  BackgroundStack_jphi_2->Add(EWKFinal_jphi_2,"hist");

  TH1F* BackgroundStack_jphi_2_Errors = MakeStackErrors(BackgroundStack_jphi_2);

  TPad* PlotPad_jphi_2 = MakeRatioPlot(CanvasFourteen, BackgroundStack_jphi_2, data_obs_jphi_2,"jphi_2");

  BackgroundStack_jphi_2->SetMaximum(max(BackgroundStack_jphi_2->GetMaximum(),data_obs_jphi_2->GetMaximum()));

  BackgroundStack_jphi_2->Draw();
  BackgroundStack_jphi_2_Errors->Draw("SAME e2");
  BackgroundStack_jphi_2->SetTitle("jphi_2");
  data_obs_jphi_2->Draw("SAME e1");
  BackgroundStack_jphi_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_jphi_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_jphi_2,0,33);

  TLegend* Legend_jphi_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_jphi_2->AddEntry(embedded_jphi_2,"embedded","f");
  Legend_jphi_2->AddEntry(DYFinal_jphi_2, "Other DY","f");
  Legend_jphi_2->AddEntry(TTFinal_jphi_2,"t#bar{t}","f");
  Legend_jphi_2->AddEntry(VVFinal_jphi_2,"Dibsoson","f");
  Legend_jphi_2->AddEntry(STFinal_jphi_2,"Single Top","f");
  Legend_jphi_2->AddEntry(qqH_htt125_jphi_2,"qqh","f");
  Legend_jphi_2->AddEntry(ggH_htt125_jphi_2,"ggH","f");
  Legend_jphi_2->AddEntry(VHFinal_jphi_2,"VH","f");
  Legend_jphi_2->AddEntry(EWKFinal_jphi_2,"EWK","f");
  Legend_jphi_2->AddEntry(data_obs_Fake_jphi_2,"Fakes","f");

  Legend_jphi_2->Draw();

  //bpt_1
  TCanvas* CanvasFifteen = new TCanvas("CanvasFifteen","bpt_1",550,550);
  CanvasFifteen->SetTickx();
  CanvasFifteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_bpt_1 = (TH1F*) HistoFile->Get("data_obs_bpt_1");
  TH1F* data_obs_Fake_bpt_1 = (TH1F*) HistoFile->Get("data_obs_Fake_bpt_1");
  TH1F* embedded_bpt_1 = (TH1F*) HistoFile->Get("embedded_bpt_1");
  TH1F* DY_bpt_1 = (TH1F*) HistoFile->Get("DY_bpt_1");
  TH1F* DYlow_bpt_1 = (TH1F*) HistoFile->Get("DYlow_bpt_1");
  TH1F* TTToHadronic_bpt_1 = (TH1F*) HistoFile->Get("TTToHadronic_bpt_1");
  TH1F* TTTo2L2Nu_bpt_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_bpt_1");
  TH1F* TTToSemiLeptonic_bpt_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_bpt_1");
  TH1F* WW4Q_bpt_1 = (TH1F*) HistoFile->Get("WW4Q_bpt_1");
  TH1F* WWLNuQQ_bpt_1 = (TH1F*) HistoFile->Get("WWLNuQQ_bpt_1");
  TH1F* WZ2L2Q_bpt_1 = (TH1F*) HistoFile->Get("WZ2L2Q_bpt_1");
  TH1F* WZ1L3Nu_bpt_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_bpt_1");
  TH1F* WZ3LNu_bpt_1 = (TH1F*) HistoFile->Get("WZ3LNu_bpt_1");
  TH1F* WZ1L1Nu2Q_bpt_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_bpt_1");
  TH1F* ZZ4L_bpt_1 = (TH1F*) HistoFile->Get("ZZ4L_bpt_1");
  TH1F* ZZ2L2Nu_bpt_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_bpt_1");
  TH1F* ZZ2L2Q_bpt_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_bpt_1");
  TH1F* ST_t_antitop_bpt_1 = (TH1F*) HistoFile->Get("ST_t_antitop_bpt_1");
  TH1F* ST_t_top_bpt_1 = (TH1F*) HistoFile->Get("ST_t_top_bpt_1");
  TH1F* ST_tW_antitop_bpt_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_bpt_1");
  TH1F* ST_tW_top_bpt_1 = (TH1F*) HistoFile->Get("ST_tW_top_bpt_1");
  TH1F* ggH_htt125_bpt_1 = (TH1F*) HistoFile->Get("ggH_htt125_bpt_1");
  TH1F* qqH_htt125_bpt_1 = (TH1F*) HistoFile->Get("qqH_htt125_bpt_1");  
  TH1F* WplusH125_bpt_1 = (TH1F*) HistoFile->Get("WplusH125_bpt_1");
  TH1F* WminusH125_bpt_1 = (TH1F*) HistoFile->Get("WminusH125_bpt_1");
  TH1F* ZH125_bpt_1 = (TH1F*) HistoFile->Get("ZH125_bpt_1");
  TH1F* EWKZLL_bpt_1 = (TH1F*) HistoFile->Get("EWKZLL_bpt_1");
  TH1F* EWKZNuNu_bpt_1 = (TH1F*) HistoFile->Get("EWKZNuNu_bpt_1");

  TH1F* DYFinal_bpt_1 = (TH1F*) DY_bpt_1->Clone();
  DYFinal_bpt_1->Add(DYlow_bpt_1);
  
  TH1F* TTFinal_bpt_1 = (TH1F*) TTToHadronic_bpt_1->Clone();
  TTFinal_bpt_1->Add(TTTo2L2Nu_bpt_1);
  TTFinal_bpt_1->Add(TTToSemiLeptonic_bpt_1);
  
  TH1F* VVFinal_bpt_1 = (TH1F*) WW4Q_bpt_1->Clone();
  VVFinal_bpt_1->Add(WWLNuQQ_bpt_1);
  VVFinal_bpt_1->Add(WZ2L2Q_bpt_1);
  VVFinal_bpt_1->Add(WZ1L3Nu_bpt_1);
  VVFinal_bpt_1->Add(WZ3LNu_bpt_1);
  VVFinal_bpt_1->Add(WZ1L1Nu2Q_bpt_1);
  VVFinal_bpt_1->Add(ZZ4L_bpt_1);
  VVFinal_bpt_1->Add(ZZ2L2Nu_bpt_1);
  VVFinal_bpt_1->Add(ZZ2L2Q_bpt_1);
  
  TH1F* STFinal_bpt_1 = (TH1F*) ST_t_antitop_bpt_1->Clone();
  STFinal_bpt_1->Add(ST_t_top_bpt_1);
  STFinal_bpt_1->Add(ST_tW_antitop_bpt_1);
  STFinal_bpt_1->Add(ST_tW_top_bpt_1);

  TH1F* VHFinal_bpt_1 = (TH1F*) WplusH125_bpt_1->Clone();
  VHFinal_bpt_1->Add(WminusH125_bpt_1);
  VHFinal_bpt_1->Add(ZH125_bpt_1);

  TH1F* EWKFinal_bpt_1 = (TH1F*) EWKZLL_bpt_1->Clone();
  EWKFinal_bpt_1->Add(EWKZNuNu_bpt_1);

  data_obs_bpt_1->SetMarkerStyle(20);
  data_obs_bpt_1->Sumw2();
  
  data_obs_Fake_bpt_1->SetFillColor(kRed);
  data_obs_Fake_bpt_1->SetLineColor(kBlack);

  embedded_bpt_1->SetFillColor(kYellow);
  embedded_bpt_1->SetLineColor(kBlack);

  DYFinal_bpt_1->SetFillColor(kBlue);
  DYFinal_bpt_1->SetLineColor(kBlack);

  TTFinal_bpt_1->SetFillColor(kViolet-3);
  TTFinal_bpt_1->SetLineColor(kBlack);

  VVFinal_bpt_1->SetFillColor(kPink-3);
  VVFinal_bpt_1->SetLineColor(kBlack);

  STFinal_bpt_1->SetFillColor(kGreen);
  STFinal_bpt_1->SetLineColor(kBlack);

  qqH_htt125_bpt_1->SetFillColor(kCyan);
  qqH_htt125_bpt_1->SetLineColor(kBlack);

  ggH_htt125_bpt_1->SetFillColor(kCyan);
  ggH_htt125_bpt_1->SetLineColor(kBlack);

  VHFinal_bpt_1->SetFillColor(kOrange);
  VHFinal_bpt_1->SetLineColor(kBlack);

  EWKFinal_bpt_1->SetFillColor(kBlue-2);
  EWKFinal_bpt_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_bpt_1 = new THStack("BackgroundStack_bpt_1","BackgroundStack_bpt_1");
  BackgroundStack_bpt_1->Add(data_obs_Fake_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(DYFinal_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(embedded_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(TTFinal_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(VVFinal_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(STFinal_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(qqH_htt125_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(ggH_htt125_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(VHFinal_bpt_1,"hist");
  BackgroundStack_bpt_1->Add(EWKFinal_bpt_1,"hist");

  TH1F* BackgroundStack_bpt_1_Errors = MakeStackErrors(BackgroundStack_bpt_1);

  TPad* PlotPad_bpt_1 = MakeRatioPlot(CanvasFifteen, BackgroundStack_bpt_1, data_obs_bpt_1,"bpt_1");

  BackgroundStack_bpt_1->SetMaximum(max(BackgroundStack_bpt_1->GetMaximum(),data_obs_bpt_1->GetMaximum()));

  BackgroundStack_bpt_1->Draw();
  BackgroundStack_bpt_1_Errors->Draw("SAME e2");
  BackgroundStack_bpt_1->SetTitle("bpt_1");
  data_obs_bpt_1->Draw("SAME e1");
  BackgroundStack_bpt_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_bpt_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_bpt_1,0,33);

  TLegend* Legend_bpt_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_bpt_1->AddEntry(embedded_bpt_1,"embedded","f");
  Legend_bpt_1->AddEntry(DYFinal_bpt_1, "Other DY","f");
  Legend_bpt_1->AddEntry(TTFinal_bpt_1,"t#bar{t}","f");
  Legend_bpt_1->AddEntry(VVFinal_bpt_1,"Dibsoson","f");
  Legend_bpt_1->AddEntry(STFinal_bpt_1,"Single Top","f");
  Legend_bpt_1->AddEntry(qqH_htt125_bpt_1,"qqh","f");
  Legend_bpt_1->AddEntry(ggH_htt125_bpt_1,"ggH","f");
  Legend_bpt_1->AddEntry(VHFinal_bpt_1,"VH","f");
  Legend_bpt_1->AddEntry(EWKFinal_bpt_1,"EWK","f");
  Legend_bpt_1->AddEntry(data_obs_Fake_bpt_1,"Fakes","f");

  Legend_bpt_1->Draw();

  //bpt_2 
  TCanvas* CanvasSixteen = new TCanvas("CanvasSixteen","bpt_2",550,550);
  CanvasSixteen->SetTickx();
  CanvasSixteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_bpt_2 = (TH1F*) HistoFile->Get("data_obs_bpt_2");
  TH1F* data_obs_Fake_bpt_2 = (TH1F*) HistoFile->Get("data_obs_Fake_bpt_2");
  TH1F* embedded_bpt_2 = (TH1F*) HistoFile->Get("embedded_bpt_2");
  TH1F* DY_bpt_2 = (TH1F*) HistoFile->Get("DY_bpt_2");
  TH1F* DYlow_bpt_2 = (TH1F*) HistoFile->Get("DYlow_bpt_2");
  TH1F* TTToHadronic_bpt_2 = (TH1F*) HistoFile->Get("TTToHadronic_bpt_2");
  TH1F* TTTo2L2Nu_bpt_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_bpt_2");
  TH1F* TTToSemiLeptonic_bpt_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_bpt_2");
  TH1F* WW4Q_bpt_2 = (TH1F*) HistoFile->Get("WW4Q_bpt_2");
  TH1F* WWLNuQQ_bpt_2 = (TH1F*) HistoFile->Get("WWLNuQQ_bpt_2");
  TH1F* WZ2L2Q_bpt_2 = (TH1F*) HistoFile->Get("WZ2L2Q_bpt_2");
  TH1F* WZ1L3Nu_bpt_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_bpt_2");
  TH1F* WZ3LNu_bpt_2 = (TH1F*) HistoFile->Get("WZ3LNu_bpt_2");
  TH1F* WZ1L1Nu2Q_bpt_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_bpt_2");
  TH1F* ZZ4L_bpt_2 = (TH1F*) HistoFile->Get("ZZ4L_bpt_2");
  TH1F* ZZ2L2Nu_bpt_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_bpt_2");
  TH1F* ZZ2L2Q_bpt_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_bpt_2");
  TH1F* ST_t_antitop_bpt_2 = (TH1F*) HistoFile->Get("ST_t_antitop_bpt_2");
  TH1F* ST_t_top_bpt_2 = (TH1F*) HistoFile->Get("ST_t_top_bpt_2");
  TH1F* ST_tW_antitop_bpt_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_bpt_2");
  TH1F* ST_tW_top_bpt_2 = (TH1F*) HistoFile->Get("ST_tW_top_bpt_2");
  TH1F* ggH_htt125_bpt_2 = (TH1F*) HistoFile->Get("ggH_htt125_bpt_2");
  TH1F* qqH_htt125_bpt_2 = (TH1F*) HistoFile->Get("qqH_htt125_bpt_2");  
  TH1F* WplusH125_bpt_2 = (TH1F*) HistoFile->Get("WplusH125_bpt_2");
  TH1F* WminusH125_bpt_2 = (TH1F*) HistoFile->Get("WminusH125_bpt_2");
  TH1F* ZH125_bpt_2 = (TH1F*) HistoFile->Get("ZH125_bpt_2");
  TH1F* EWKZLL_bpt_2 = (TH1F*) HistoFile->Get("EWKZLL_bpt_2");
  TH1F* EWKZNuNu_bpt_2 = (TH1F*) HistoFile->Get("EWKZNuNu_bpt_2");

  TH1F* DYFinal_bpt_2 = (TH1F*) DY_bpt_2->Clone();
  DYFinal_bpt_2->Add(DYlow_bpt_2);
  
  TH1F* TTFinal_bpt_2 = (TH1F*) TTToHadronic_bpt_2->Clone();
  TTFinal_bpt_2->Add(TTTo2L2Nu_bpt_2);
  TTFinal_bpt_2->Add(TTToSemiLeptonic_bpt_2);
  
  TH1F* VVFinal_bpt_2 = (TH1F*) WW4Q_bpt_2->Clone();
  VVFinal_bpt_2->Add(WWLNuQQ_bpt_2);
  VVFinal_bpt_2->Add(WZ2L2Q_bpt_2);
  VVFinal_bpt_2->Add(WZ1L3Nu_bpt_2);
  VVFinal_bpt_2->Add(WZ3LNu_bpt_2);
  VVFinal_bpt_2->Add(WZ1L1Nu2Q_bpt_2);
  VVFinal_bpt_2->Add(ZZ4L_bpt_2);
  VVFinal_bpt_2->Add(ZZ2L2Nu_bpt_2);
  VVFinal_bpt_2->Add(ZZ2L2Q_bpt_2);
  
  TH1F* STFinal_bpt_2 = (TH1F*) ST_t_antitop_bpt_2->Clone();
  STFinal_bpt_2->Add(ST_t_top_bpt_2);
  STFinal_bpt_2->Add(ST_tW_antitop_bpt_2);
  STFinal_bpt_2->Add(ST_tW_top_bpt_2);

  TH1F* VHFinal_bpt_2 = (TH1F*) WplusH125_bpt_2->Clone();
  VHFinal_bpt_2->Add(WminusH125_bpt_2);
  VHFinal_bpt_2->Add(ZH125_bpt_2);

  TH1F* EWKFinal_bpt_2 = (TH1F*) EWKZLL_bpt_2->Clone();
  EWKFinal_bpt_2->Add(EWKZNuNu_bpt_2);

  data_obs_bpt_2->SetMarkerStyle(20);
  data_obs_bpt_2->Sumw2();
  
  data_obs_Fake_bpt_2->SetFillColor(kRed);
  data_obs_Fake_bpt_2->SetLineColor(kBlack);

  embedded_bpt_2->SetFillColor(kYellow);
  embedded_bpt_2->SetLineColor(kBlack);

  DYFinal_bpt_2->SetFillColor(kBlue);
  DYFinal_bpt_2->SetLineColor(kBlack);

  TTFinal_bpt_2->SetFillColor(kViolet-3);
  TTFinal_bpt_2->SetLineColor(kBlack);

  VVFinal_bpt_2->SetFillColor(kPink-3);
  VVFinal_bpt_2->SetLineColor(kBlack);

  STFinal_bpt_2->SetFillColor(kGreen);
  STFinal_bpt_2->SetLineColor(kBlack);

  qqH_htt125_bpt_2->SetFillColor(kCyan);
  qqH_htt125_bpt_2->SetLineColor(kBlack);

  ggH_htt125_bpt_2->SetFillColor(kCyan);
  ggH_htt125_bpt_2->SetLineColor(kBlack);

  VHFinal_bpt_2->SetFillColor(kOrange);
  VHFinal_bpt_2->SetLineColor(kBlack);

  EWKFinal_bpt_2->SetFillColor(kBlue-2);
  EWKFinal_bpt_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_bpt_2 = new THStack("BackgroundStack_bpt_2","BackgroundStack_bpt_2");
  BackgroundStack_bpt_2->Add(data_obs_Fake_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(DYFinal_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(embedded_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(TTFinal_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(VVFinal_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(STFinal_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(qqH_htt125_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(ggH_htt125_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(VHFinal_bpt_2,"hist");
  BackgroundStack_bpt_2->Add(EWKFinal_bpt_2,"hist");

  TH1F* BackgroundStack_bpt_2_Errors = MakeStackErrors(BackgroundStack_bpt_2);

  TPad* PlotPad_bpt_2 = MakeRatioPlot(CanvasSixteen, BackgroundStack_bpt_2, data_obs_bpt_2,"bpt_2");

  BackgroundStack_bpt_2->SetMaximum(max(BackgroundStack_bpt_2->GetMaximum(),data_obs_bpt_2->GetMaximum()));

  BackgroundStack_bpt_2->Draw();
  BackgroundStack_bpt_2_Errors->Draw("SAME e2");
  BackgroundStack_bpt_2->SetTitle("bpt_2");
  data_obs_bpt_2->Draw("SAME e1");
  BackgroundStack_bpt_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_bpt_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_bpt_2,0,33);

  TLegend* Legend_bpt_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_bpt_2->AddEntry(embedded_bpt_2,"embedded","f");
  Legend_bpt_2->AddEntry(DYFinal_bpt_2, "Other DY","f");
  Legend_bpt_2->AddEntry(TTFinal_bpt_2,"t#bar{t}","f");
  Legend_bpt_2->AddEntry(VVFinal_bpt_2,"Dibsoson","f");
  Legend_bpt_2->AddEntry(STFinal_bpt_2,"Single Top","f");
  Legend_bpt_2->AddEntry(qqH_htt125_bpt_2,"qqh","f");
  Legend_bpt_2->AddEntry(ggH_htt125_bpt_2,"ggH","f");
  Legend_bpt_2->AddEntry(VHFinal_bpt_2,"VH","f");
  Legend_bpt_2->AddEntry(EWKFinal_bpt_2,"EWK","f");
  Legend_bpt_2->AddEntry(data_obs_Fake_bpt_2,"Fakes","f");

  Legend_bpt_2->Draw();

  //beta_1 
  TCanvas* CanvasSeventeen = new TCanvas("CanvasSeventeen","beta_1",550,550);
  CanvasSeventeen->SetTickx();
  CanvasSeventeen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_beta_1 = (TH1F*) HistoFile->Get("data_obs_beta_1");
  TH1F* data_obs_Fake_beta_1 = (TH1F*) HistoFile->Get("data_obs_Fake_beta_1");
  TH1F* embedded_beta_1 = (TH1F*) HistoFile->Get("embedded_beta_1");
  TH1F* DY_beta_1 = (TH1F*) HistoFile->Get("DY_beta_1");
  TH1F* DYlow_beta_1 = (TH1F*) HistoFile->Get("DYlow_beta_1");
  TH1F* TTToHadronic_beta_1 = (TH1F*) HistoFile->Get("TTToHadronic_beta_1");
  TH1F* TTTo2L2Nu_beta_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_beta_1");
  TH1F* TTToSemiLeptonic_beta_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_beta_1");
  TH1F* WW4Q_beta_1 = (TH1F*) HistoFile->Get("WW4Q_beta_1");
  TH1F* WWLNuQQ_beta_1 = (TH1F*) HistoFile->Get("WWLNuQQ_beta_1");
  TH1F* WZ2L2Q_beta_1 = (TH1F*) HistoFile->Get("WZ2L2Q_beta_1");
  TH1F* WZ1L3Nu_beta_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_beta_1");
  TH1F* WZ3LNu_beta_1 = (TH1F*) HistoFile->Get("WZ3LNu_beta_1");
  TH1F* WZ1L1Nu2Q_beta_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_beta_1");
  TH1F* ZZ4L_beta_1 = (TH1F*) HistoFile->Get("ZZ4L_beta_1");
  TH1F* ZZ2L2Nu_beta_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_beta_1");
  TH1F* ZZ2L2Q_beta_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_beta_1");
  TH1F* ST_t_antitop_beta_1 = (TH1F*) HistoFile->Get("ST_t_antitop_beta_1");
  TH1F* ST_t_top_beta_1 = (TH1F*) HistoFile->Get("ST_t_top_beta_1");
  TH1F* ST_tW_antitop_beta_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_beta_1");
  TH1F* ST_tW_top_beta_1 = (TH1F*) HistoFile->Get("ST_tW_top_beta_1");
  TH1F* ggH_htt125_beta_1 = (TH1F*) HistoFile->Get("ggH_htt125_beta_1");
  TH1F* qqH_htt125_beta_1 = (TH1F*) HistoFile->Get("qqH_htt125_beta_1");  
  TH1F* WplusH125_beta_1 = (TH1F*) HistoFile->Get("WplusH125_beta_1");
  TH1F* WminusH125_beta_1 = (TH1F*) HistoFile->Get("WminusH125_beta_1");
  TH1F* ZH125_beta_1 = (TH1F*) HistoFile->Get("ZH125_beta_1");
  TH1F* EWKZLL_beta_1 = (TH1F*) HistoFile->Get("EWKZLL_beta_1");
  TH1F* EWKZNuNu_beta_1 = (TH1F*) HistoFile->Get("EWKZNuNu_beta_1");

  TH1F* DYFinal_beta_1 = (TH1F*) DY_beta_1->Clone();
  DYFinal_beta_1->Add(DYlow_beta_1);
  
  TH1F* TTFinal_beta_1 = (TH1F*) TTToHadronic_beta_1->Clone();
  TTFinal_beta_1->Add(TTTo2L2Nu_beta_1);
  TTFinal_beta_1->Add(TTToSemiLeptonic_beta_1);
  
  TH1F* VVFinal_beta_1 = (TH1F*) WW4Q_beta_1->Clone();
  VVFinal_beta_1->Add(WWLNuQQ_beta_1);
  VVFinal_beta_1->Add(WZ2L2Q_beta_1);
  VVFinal_beta_1->Add(WZ1L3Nu_beta_1);
  VVFinal_beta_1->Add(WZ3LNu_beta_1);
  VVFinal_beta_1->Add(WZ1L1Nu2Q_beta_1);
  VVFinal_beta_1->Add(ZZ4L_beta_1);
  VVFinal_beta_1->Add(ZZ2L2Nu_beta_1);
  VVFinal_beta_1->Add(ZZ2L2Q_beta_1);
  
  TH1F* STFinal_beta_1 = (TH1F*) ST_t_antitop_beta_1->Clone();
  STFinal_beta_1->Add(ST_t_top_beta_1);
  STFinal_beta_1->Add(ST_tW_antitop_beta_1);
  STFinal_beta_1->Add(ST_tW_top_beta_1);

  TH1F* VHFinal_beta_1 = (TH1F*) WplusH125_beta_1->Clone();
  VHFinal_beta_1->Add(WminusH125_beta_1);
  VHFinal_beta_1->Add(ZH125_beta_1);

  TH1F* EWKFinal_beta_1 = (TH1F*) EWKZLL_beta_1->Clone();
  EWKFinal_beta_1->Add(EWKZNuNu_beta_1);

  data_obs_beta_1->SetMarkerStyle(20);
  data_obs_beta_1->Sumw2();
  
  data_obs_Fake_beta_1->SetFillColor(kRed);
  data_obs_Fake_beta_1->SetLineColor(kBlack);

  embedded_beta_1->SetFillColor(kYellow);
  embedded_beta_1->SetLineColor(kBlack);

  DYFinal_beta_1->SetFillColor(kBlue);
  DYFinal_beta_1->SetLineColor(kBlack);

  TTFinal_beta_1->SetFillColor(kViolet-3);
  TTFinal_beta_1->SetLineColor(kBlack);

  VVFinal_beta_1->SetFillColor(kPink-3);
  VVFinal_beta_1->SetLineColor(kBlack);

  STFinal_beta_1->SetFillColor(kGreen);
  STFinal_beta_1->SetLineColor(kBlack);

  qqH_htt125_beta_1->SetFillColor(kCyan);
  qqH_htt125_beta_1->SetLineColor(kBlack);

  ggH_htt125_beta_1->SetFillColor(kCyan);
  ggH_htt125_beta_1->SetLineColor(kBlack);

  VHFinal_beta_1->SetFillColor(kOrange);
  VHFinal_beta_1->SetLineColor(kBlack);

  EWKFinal_beta_1->SetFillColor(kBlue-2);
  EWKFinal_beta_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_beta_1 = new THStack("BackgroundStack_beta_1","BackgroundStack_beta_1");
  BackgroundStack_beta_1->Add(data_obs_Fake_beta_1,"hist");
  BackgroundStack_beta_1->Add(DYFinal_beta_1,"hist");
  BackgroundStack_beta_1->Add(embedded_beta_1,"hist");
  BackgroundStack_beta_1->Add(TTFinal_beta_1,"hist");
  BackgroundStack_beta_1->Add(VVFinal_beta_1,"hist");
  BackgroundStack_beta_1->Add(STFinal_beta_1,"hist");
  BackgroundStack_beta_1->Add(qqH_htt125_beta_1,"hist");
  BackgroundStack_beta_1->Add(ggH_htt125_beta_1,"hist");
  BackgroundStack_beta_1->Add(VHFinal_beta_1,"hist");
  BackgroundStack_beta_1->Add(EWKFinal_beta_1,"hist");

  TH1F* BackgroundStack_beta_1_Errors = MakeStackErrors(BackgroundStack_beta_1);

  TPad* PlotPad_beta_1 = MakeRatioPlot(CanvasSeventeen, BackgroundStack_beta_1, data_obs_beta_1,"beta_1");

  BackgroundStack_beta_1->SetMaximum(max(BackgroundStack_beta_1->GetMaximum(),data_obs_beta_1->GetMaximum()));

  BackgroundStack_beta_1->Draw();
  BackgroundStack_beta_1_Errors->Draw("SAME e2");
  BackgroundStack_beta_1->SetTitle("beta_1");
  data_obs_beta_1->Draw("SAME e1");
  BackgroundStack_beta_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_beta_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_beta_1,0,33);

  TLegend* Legend_beta_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_beta_1->AddEntry(embedded_beta_1,"embedded","f");
  Legend_beta_1->AddEntry(DYFinal_beta_1, "Other DY","f");
  Legend_beta_1->AddEntry(TTFinal_beta_1,"t#bar{t}","f");
  Legend_beta_1->AddEntry(VVFinal_beta_1,"Dibsoson","f");
  Legend_beta_1->AddEntry(STFinal_beta_1,"Single Top","f");
  Legend_beta_1->AddEntry(qqH_htt125_beta_1,"qqh","f");
  Legend_beta_1->AddEntry(ggH_htt125_beta_1,"ggH","f");
  Legend_beta_1->AddEntry(VHFinal_beta_1,"VH","f");
  Legend_beta_1->AddEntry(EWKFinal_beta_1,"EWK","f");
  Legend_beta_1->AddEntry(data_obs_Fake_beta_1,"Fakes","f");

  Legend_beta_1->Draw();

  //beta_2
  TCanvas* CanvasEighteen = new TCanvas("CanvasEighteen","beta_2",550,550);
  CanvasEighteen->SetTickx();
  CanvasEighteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_beta_2 = (TH1F*) HistoFile->Get("data_obs_beta_2");
  TH1F* data_obs_Fake_beta_2 = (TH1F*) HistoFile->Get("data_obs_Fake_beta_2");
  TH1F* embedded_beta_2 = (TH1F*) HistoFile->Get("embedded_beta_2");
  TH1F* DY_beta_2 = (TH1F*) HistoFile->Get("DY_beta_2");
  TH1F* DYlow_beta_2 = (TH1F*) HistoFile->Get("DYlow_beta_2");
  TH1F* TTToHadronic_beta_2 = (TH1F*) HistoFile->Get("TTToHadronic_beta_2");
  TH1F* TTTo2L2Nu_beta_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_beta_2");
  TH1F* TTToSemiLeptonic_beta_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_beta_2");
  TH1F* WW4Q_beta_2 = (TH1F*) HistoFile->Get("WW4Q_beta_2");
  TH1F* WWLNuQQ_beta_2 = (TH1F*) HistoFile->Get("WWLNuQQ_beta_2");
  TH1F* WZ2L2Q_beta_2 = (TH1F*) HistoFile->Get("WZ2L2Q_beta_2");
  TH1F* WZ1L3Nu_beta_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_beta_2");
  TH1F* WZ3LNu_beta_2 = (TH1F*) HistoFile->Get("WZ3LNu_beta_2");
  TH1F* WZ1L1Nu2Q_beta_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_beta_2");
  TH1F* ZZ4L_beta_2 = (TH1F*) HistoFile->Get("ZZ4L_beta_2");
  TH1F* ZZ2L2Nu_beta_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_beta_2");
  TH1F* ZZ2L2Q_beta_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_beta_2");
  TH1F* ST_t_antitop_beta_2 = (TH1F*) HistoFile->Get("ST_t_antitop_beta_2");
  TH1F* ST_t_top_beta_2 = (TH1F*) HistoFile->Get("ST_t_top_beta_2");
  TH1F* ST_tW_antitop_beta_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_beta_2");
  TH1F* ST_tW_top_beta_2 = (TH1F*) HistoFile->Get("ST_tW_top_beta_2");
  TH1F* ggH_htt125_beta_2 = (TH1F*) HistoFile->Get("ggH_htt125_beta_2");
  TH1F* qqH_htt125_beta_2 = (TH1F*) HistoFile->Get("qqH_htt125_beta_2");  
  TH1F* WplusH125_beta_2 = (TH1F*) HistoFile->Get("WplusH125_beta_2");
  TH1F* WminusH125_beta_2 = (TH1F*) HistoFile->Get("WminusH125_beta_2");
  TH1F* ZH125_beta_2 = (TH1F*) HistoFile->Get("ZH125_beta_2");
  TH1F* EWKZLL_beta_2 = (TH1F*) HistoFile->Get("EWKZLL_beta_2");
  TH1F* EWKZNuNu_beta_2 = (TH1F*) HistoFile->Get("EWKZNuNu_beta_2");

  TH1F* DYFinal_beta_2 = (TH1F*) DY_beta_2->Clone();
  DYFinal_beta_2->Add(DYlow_beta_2);
  
  TH1F* TTFinal_beta_2 = (TH1F*) TTToHadronic_beta_2->Clone();
  TTFinal_beta_2->Add(TTTo2L2Nu_beta_2);
  TTFinal_beta_2->Add(TTToSemiLeptonic_beta_2);
  
  TH1F* VVFinal_beta_2 = (TH1F*) WW4Q_beta_2->Clone();
  VVFinal_beta_2->Add(WWLNuQQ_beta_2);
  VVFinal_beta_2->Add(WZ2L2Q_beta_2);
  VVFinal_beta_2->Add(WZ1L3Nu_beta_2);
  VVFinal_beta_2->Add(WZ3LNu_beta_2);
  VVFinal_beta_2->Add(WZ1L1Nu2Q_beta_2);
  VVFinal_beta_2->Add(ZZ4L_beta_2);
  VVFinal_beta_2->Add(ZZ2L2Nu_beta_2);
  VVFinal_beta_2->Add(ZZ2L2Q_beta_2);
  
  TH1F* STFinal_beta_2 = (TH1F*) ST_t_antitop_beta_2->Clone();
  STFinal_beta_2->Add(ST_t_top_beta_2);
  STFinal_beta_2->Add(ST_tW_antitop_beta_2);
  STFinal_beta_2->Add(ST_tW_top_beta_2);

  TH1F* VHFinal_beta_2 = (TH1F*) WplusH125_beta_2->Clone();
  VHFinal_beta_2->Add(WminusH125_beta_2);
  VHFinal_beta_2->Add(ZH125_beta_2);

  TH1F* EWKFinal_beta_2 = (TH1F*) EWKZLL_beta_2->Clone();
  EWKFinal_beta_2->Add(EWKZNuNu_beta_2);

  data_obs_beta_2->SetMarkerStyle(20);
  data_obs_beta_2->Sumw2();
  
  data_obs_Fake_beta_2->SetFillColor(kRed);
  data_obs_Fake_beta_2->SetLineColor(kBlack);

  embedded_beta_2->SetFillColor(kYellow);
  embedded_beta_2->SetLineColor(kBlack);

  DYFinal_beta_2->SetFillColor(kBlue);
  DYFinal_beta_2->SetLineColor(kBlack);

  TTFinal_beta_2->SetFillColor(kViolet-3);
  TTFinal_beta_2->SetLineColor(kBlack);

  VVFinal_beta_2->SetFillColor(kPink-3);
  VVFinal_beta_2->SetLineColor(kBlack);

  STFinal_beta_2->SetFillColor(kGreen);
  STFinal_beta_2->SetLineColor(kBlack);

  qqH_htt125_beta_2->SetFillColor(kCyan);
  qqH_htt125_beta_2->SetLineColor(kBlack);

  ggH_htt125_beta_2->SetFillColor(kCyan);
  ggH_htt125_beta_2->SetLineColor(kBlack);

  VHFinal_beta_2->SetFillColor(kOrange);
  VHFinal_beta_2->SetLineColor(kBlack);

  EWKFinal_beta_2->SetFillColor(kBlue-2);
  EWKFinal_beta_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_beta_2 = new THStack("BackgroundStack_beta_2","BackgroundStack_beta_2");
  BackgroundStack_beta_2->Add(data_obs_Fake_beta_2,"hist");
  BackgroundStack_beta_2->Add(DYFinal_beta_2,"hist");
  BackgroundStack_beta_2->Add(embedded_beta_2,"hist");
  BackgroundStack_beta_2->Add(TTFinal_beta_2,"hist");
  BackgroundStack_beta_2->Add(VVFinal_beta_2,"hist");
  BackgroundStack_beta_2->Add(STFinal_beta_2,"hist");
  BackgroundStack_beta_2->Add(qqH_htt125_beta_2,"hist");
  BackgroundStack_beta_2->Add(ggH_htt125_beta_2,"hist");
  BackgroundStack_beta_2->Add(VHFinal_beta_2,"hist");
  BackgroundStack_beta_2->Add(EWKFinal_beta_2,"hist");

  TH1F* BackgroundStack_beta_2_Errors = MakeStackErrors(BackgroundStack_beta_2);

  TPad* PlotPad_beta_2 = MakeRatioPlot(CanvasEighteen, BackgroundStack_beta_2, data_obs_beta_2,"beta_2");

  BackgroundStack_beta_2->SetMaximum(max(BackgroundStack_beta_2->GetMaximum(),data_obs_beta_2->GetMaximum()));

  BackgroundStack_beta_2->Draw();
  BackgroundStack_beta_2_Errors->Draw("SAME e2");
  BackgroundStack_beta_2->SetTitle("beta_2");
  data_obs_beta_2->Draw("SAME e1");
  BackgroundStack_beta_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_beta_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_beta_2,0,33);

  TLegend* Legend_beta_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_beta_2->AddEntry(embedded_beta_2,"embedded","f");
  Legend_beta_2->AddEntry(DYFinal_beta_2, "Other DY","f");
  Legend_beta_2->AddEntry(TTFinal_beta_2,"t#bar{t}","f");
  Legend_beta_2->AddEntry(VVFinal_beta_2,"Dibsoson","f");
  Legend_beta_2->AddEntry(STFinal_beta_2,"Single Top","f");
  Legend_beta_2->AddEntry(qqH_htt125_beta_2,"qqh","f");
  Legend_beta_2->AddEntry(ggH_htt125_beta_2,"ggH","f");
  Legend_beta_2->AddEntry(VHFinal_beta_2,"VH","f");
  Legend_beta_2->AddEntry(EWKFinal_beta_2,"EWK","f");
  Legend_beta_2->AddEntry(data_obs_Fake_beta_2,"Fakes","f");

  Legend_beta_2->Draw();

  //bphi_1
  TCanvas* CanvasNineteen = new TCanvas("CanvasNineteen","bphi_1",550,550);
  CanvasNineteen->SetTickx();
  CanvasNineteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_bphi_1 = (TH1F*) HistoFile->Get("data_obs_bphi_1");
  TH1F* data_obs_Fake_bphi_1 = (TH1F*) HistoFile->Get("data_obs_Fake_bphi_1");
  TH1F* embedded_bphi_1 = (TH1F*) HistoFile->Get("embedded_bphi_1");
  TH1F* DY_bphi_1 = (TH1F*) HistoFile->Get("DY_bphi_1");
  TH1F* DYlow_bphi_1 = (TH1F*) HistoFile->Get("DYlow_bphi_1");
  TH1F* TTToHadronic_bphi_1 = (TH1F*) HistoFile->Get("TTToHadronic_bphi_1");
  TH1F* TTTo2L2Nu_bphi_1 = (TH1F*) HistoFile->Get("TTTo2L2Nu_bphi_1");
  TH1F* TTToSemiLeptonic_bphi_1 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_bphi_1");
  TH1F* WW4Q_bphi_1 = (TH1F*) HistoFile->Get("WW4Q_bphi_1");
  TH1F* WWLNuQQ_bphi_1 = (TH1F*) HistoFile->Get("WWLNuQQ_bphi_1");
  TH1F* WZ2L2Q_bphi_1 = (TH1F*) HistoFile->Get("WZ2L2Q_bphi_1");
  TH1F* WZ1L3Nu_bphi_1 = (TH1F*) HistoFile->Get("WZ1L3Nu_bphi_1");
  TH1F* WZ3LNu_bphi_1 = (TH1F*) HistoFile->Get("WZ3LNu_bphi_1");
  TH1F* WZ1L1Nu2Q_bphi_1 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_bphi_1");
  TH1F* ZZ4L_bphi_1 = (TH1F*) HistoFile->Get("ZZ4L_bphi_1");
  TH1F* ZZ2L2Nu_bphi_1 = (TH1F*) HistoFile->Get("ZZ2L2Nu_bphi_1");
  TH1F* ZZ2L2Q_bphi_1 = (TH1F*) HistoFile->Get("ZZ2L2Q_bphi_1");
  TH1F* ST_t_antitop_bphi_1 = (TH1F*) HistoFile->Get("ST_t_antitop_bphi_1");
  TH1F* ST_t_top_bphi_1 = (TH1F*) HistoFile->Get("ST_t_top_bphi_1");
  TH1F* ST_tW_antitop_bphi_1 = (TH1F*) HistoFile->Get("ST_tW_antitop_bphi_1");
  TH1F* ST_tW_top_bphi_1 = (TH1F*) HistoFile->Get("ST_tW_top_bphi_1");
  TH1F* ggH_htt125_bphi_1 = (TH1F*) HistoFile->Get("ggH_htt125_bphi_1");
  TH1F* qqH_htt125_bphi_1 = (TH1F*) HistoFile->Get("qqH_htt125_bphi_1");  
  TH1F* WplusH125_bphi_1 = (TH1F*) HistoFile->Get("WplusH125_bphi_1");
  TH1F* WminusH125_bphi_1 = (TH1F*) HistoFile->Get("WminusH125_bphi_1");
  TH1F* ZH125_bphi_1 = (TH1F*) HistoFile->Get("ZH125_bphi_1");
  TH1F* EWKZLL_bphi_1 = (TH1F*) HistoFile->Get("EWKZLL_bphi_1");
  TH1F* EWKZNuNu_bphi_1 = (TH1F*) HistoFile->Get("EWKZNuNu_bphi_1");

  TH1F* DYFinal_bphi_1 = (TH1F*) DY_bphi_1->Clone();
  DYFinal_bphi_1->Add(DYlow_bphi_1);
  
  TH1F* TTFinal_bphi_1 = (TH1F*) TTToHadronic_bphi_1->Clone();
  TTFinal_bphi_1->Add(TTTo2L2Nu_bphi_1);
  TTFinal_bphi_1->Add(TTToSemiLeptonic_bphi_1);
  
  TH1F* VVFinal_bphi_1 = (TH1F*) WW4Q_bphi_1->Clone();
  VVFinal_bphi_1->Add(WWLNuQQ_bphi_1);
  VVFinal_bphi_1->Add(WZ2L2Q_bphi_1);
  VVFinal_bphi_1->Add(WZ1L3Nu_bphi_1);
  VVFinal_bphi_1->Add(WZ3LNu_bphi_1);
  VVFinal_bphi_1->Add(WZ1L1Nu2Q_bphi_1);
  VVFinal_bphi_1->Add(ZZ4L_bphi_1);
  VVFinal_bphi_1->Add(ZZ2L2Nu_bphi_1);
  VVFinal_bphi_1->Add(ZZ2L2Q_bphi_1);
  
  TH1F* STFinal_bphi_1 = (TH1F*) ST_t_antitop_bphi_1->Clone();
  STFinal_bphi_1->Add(ST_t_top_bphi_1);
  STFinal_bphi_1->Add(ST_tW_antitop_bphi_1);
  STFinal_bphi_1->Add(ST_tW_top_bphi_1);

  TH1F* VHFinal_bphi_1 = (TH1F*) WplusH125_bphi_1->Clone();
  VHFinal_bphi_1->Add(WminusH125_bphi_1);
  VHFinal_bphi_1->Add(ZH125_bphi_1);

  TH1F* EWKFinal_bphi_1 = (TH1F*) EWKZLL_bphi_1->Clone();
  EWKFinal_bphi_1->Add(EWKZNuNu_bphi_1);

  data_obs_bphi_1->SetMarkerStyle(20);
  data_obs_bphi_1->Sumw2();
  
  data_obs_Fake_bphi_1->SetFillColor(kRed);
  data_obs_Fake_bphi_1->SetLineColor(kBlack);

  embedded_bphi_1->SetFillColor(kYellow);
  embedded_bphi_1->SetLineColor(kBlack);

  DYFinal_bphi_1->SetFillColor(kBlue);
  DYFinal_bphi_1->SetLineColor(kBlack);

  TTFinal_bphi_1->SetFillColor(kViolet-3);
  TTFinal_bphi_1->SetLineColor(kBlack);

  VVFinal_bphi_1->SetFillColor(kPink-3);
  VVFinal_bphi_1->SetLineColor(kBlack);

  STFinal_bphi_1->SetFillColor(kGreen);
  STFinal_bphi_1->SetLineColor(kBlack);

  qqH_htt125_bphi_1->SetFillColor(kCyan);
  qqH_htt125_bphi_1->SetLineColor(kBlack);

  ggH_htt125_bphi_1->SetFillColor(kCyan);
  ggH_htt125_bphi_1->SetLineColor(kBlack);

  VHFinal_bphi_1->SetFillColor(kOrange);
  VHFinal_bphi_1->SetLineColor(kBlack);

  EWKFinal_bphi_1->SetFillColor(kBlue-2);
  EWKFinal_bphi_1->SetLineColor(kBlack);
  
  THStack* BackgroundStack_bphi_1 = new THStack("BackgroundStack_bphi_1","BackgroundStack_bphi_1");
  BackgroundStack_bphi_1->Add(data_obs_Fake_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(DYFinal_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(embedded_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(TTFinal_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(VVFinal_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(STFinal_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(qqH_htt125_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(ggH_htt125_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(VHFinal_bphi_1,"hist");
  BackgroundStack_bphi_1->Add(EWKFinal_bphi_1,"hist");

  TH1F* BackgroundStack_bphi_1_Errors = MakeStackErrors(BackgroundStack_bphi_1);

  TPad* PlotPad_bphi_1 = MakeRatioPlot(CanvasNineteen, BackgroundStack_bphi_1, data_obs_bphi_1,"bphi_1");

  BackgroundStack_bphi_1->SetMaximum(max(BackgroundStack_bphi_1->GetMaximum(),data_obs_bphi_1->GetMaximum()));

  BackgroundStack_bphi_1->Draw();
  BackgroundStack_bphi_1_Errors->Draw("SAME e2");
  BackgroundStack_bphi_1->SetTitle("bphi_1");
  data_obs_bphi_1->Draw("SAME e1");
  BackgroundStack_bphi_1->GetYaxis()->SetTitle("Events");
  BackgroundStack_bphi_1->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_bphi_1,0,33);

  TLegend* Legend_bphi_1 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_bphi_1->AddEntry(embedded_bphi_1,"embedded","f");
  Legend_bphi_1->AddEntry(DYFinal_bphi_1, "Other DY","f");
  Legend_bphi_1->AddEntry(TTFinal_bphi_1,"t#bar{t}","f");
  Legend_bphi_1->AddEntry(VVFinal_bphi_1,"Dibsoson","f");
  Legend_bphi_1->AddEntry(STFinal_bphi_1,"Single Top","f");
  Legend_bphi_1->AddEntry(qqH_htt125_bphi_1,"qqh","f");
  Legend_bphi_1->AddEntry(ggH_htt125_bphi_1,"ggH","f");
  Legend_bphi_1->AddEntry(VHFinal_bphi_1,"VH","f");
  Legend_bphi_1->AddEntry(EWKFinal_bphi_1,"EWK","f");
  Legend_bphi_1->AddEntry(data_obs_Fake_bphi_1,"Fakes","f");

  Legend_bphi_1->Draw();

  //bphi_2
  TCanvas* CanvasTwenty = new TCanvas("CanvasTwenty","bphi_2",550,550);
  CanvasTwenty->SetTickx();
  CanvasTwenty->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_bphi_2 = (TH1F*) HistoFile->Get("data_obs_bphi_2");
  TH1F* data_obs_Fake_bphi_2 = (TH1F*) HistoFile->Get("data_obs_Fake_bphi_2");
  TH1F* embedded_bphi_2 = (TH1F*) HistoFile->Get("embedded_bphi_2");
  TH1F* DY_bphi_2 = (TH1F*) HistoFile->Get("DY_bphi_2");
  TH1F* DYlow_bphi_2 = (TH1F*) HistoFile->Get("DYlow_bphi_2");
  TH1F* TTToHadronic_bphi_2 = (TH1F*) HistoFile->Get("TTToHadronic_bphi_2");
  TH1F* TTTo2L2Nu_bphi_2 = (TH1F*) HistoFile->Get("TTTo2L2Nu_bphi_2");
  TH1F* TTToSemiLeptonic_bphi_2 = (TH1F*) HistoFile->Get("TTToSemiLeptonic_bphi_2");
  TH1F* WW4Q_bphi_2 = (TH1F*) HistoFile->Get("WW4Q_bphi_2");
  TH1F* WWLNuQQ_bphi_2 = (TH1F*) HistoFile->Get("WWLNuQQ_bphi_2");
  TH1F* WZ2L2Q_bphi_2 = (TH1F*) HistoFile->Get("WZ2L2Q_bphi_2");
  TH1F* WZ1L3Nu_bphi_2 = (TH1F*) HistoFile->Get("WZ1L3Nu_bphi_2");
  TH1F* WZ3LNu_bphi_2 = (TH1F*) HistoFile->Get("WZ3LNu_bphi_2");
  TH1F* WZ1L1Nu2Q_bphi_2 = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_bphi_2");
  TH1F* ZZ4L_bphi_2 = (TH1F*) HistoFile->Get("ZZ4L_bphi_2");
  TH1F* ZZ2L2Nu_bphi_2 = (TH1F*) HistoFile->Get("ZZ2L2Nu_bphi_2");
  TH1F* ZZ2L2Q_bphi_2 = (TH1F*) HistoFile->Get("ZZ2L2Q_bphi_2");
  TH1F* ST_t_antitop_bphi_2 = (TH1F*) HistoFile->Get("ST_t_antitop_bphi_2");
  TH1F* ST_t_top_bphi_2 = (TH1F*) HistoFile->Get("ST_t_top_bphi_2");
  TH1F* ST_tW_antitop_bphi_2 = (TH1F*) HistoFile->Get("ST_tW_antitop_bphi_2");
  TH1F* ST_tW_top_bphi_2 = (TH1F*) HistoFile->Get("ST_tW_top_bphi_2");
  TH1F* ggH_htt125_bphi_2 = (TH1F*) HistoFile->Get("ggH_htt125_bphi_2");
  TH1F* qqH_htt125_bphi_2 = (TH1F*) HistoFile->Get("qqH_htt125_bphi_2");  
  TH1F* WplusH125_bphi_2 = (TH1F*) HistoFile->Get("WplusH125_bphi_2");
  TH1F* WminusH125_bphi_2 = (TH1F*) HistoFile->Get("WminusH125_bphi_2");
  TH1F* ZH125_bphi_2 = (TH1F*) HistoFile->Get("ZH125_bphi_2");
  TH1F* EWKZLL_bphi_2 = (TH1F*) HistoFile->Get("EWKZLL_bphi_2");
  TH1F* EWKZNuNu_bphi_2 = (TH1F*) HistoFile->Get("EWKZNuNu_bphi_2");

  TH1F* DYFinal_bphi_2 = (TH1F*) DY_bphi_2->Clone();
  DYFinal_bphi_2->Add(DYlow_bphi_2);
  
  TH1F* TTFinal_bphi_2 = (TH1F*) TTToHadronic_bphi_2->Clone();
  TTFinal_bphi_2->Add(TTTo2L2Nu_bphi_2);
  TTFinal_bphi_2->Add(TTToSemiLeptonic_bphi_2);
  
  TH1F* VVFinal_bphi_2 = (TH1F*) WW4Q_bphi_2->Clone();
  VVFinal_bphi_2->Add(WWLNuQQ_bphi_2);
  VVFinal_bphi_2->Add(WZ2L2Q_bphi_2);
  VVFinal_bphi_2->Add(WZ1L3Nu_bphi_2);
  VVFinal_bphi_2->Add(WZ3LNu_bphi_2);
  VVFinal_bphi_2->Add(WZ1L1Nu2Q_bphi_2);
  VVFinal_bphi_2->Add(ZZ4L_bphi_2);
  VVFinal_bphi_2->Add(ZZ2L2Nu_bphi_2);
  VVFinal_bphi_2->Add(ZZ2L2Q_bphi_2);
  
  TH1F* STFinal_bphi_2 = (TH1F*) ST_t_antitop_bphi_2->Clone();
  STFinal_bphi_2->Add(ST_t_top_bphi_2);
  STFinal_bphi_2->Add(ST_tW_antitop_bphi_2);
  STFinal_bphi_2->Add(ST_tW_top_bphi_2);

  TH1F* VHFinal_bphi_2 = (TH1F*) WplusH125_bphi_2->Clone();
  VHFinal_bphi_2->Add(WminusH125_bphi_2);
  VHFinal_bphi_2->Add(ZH125_bphi_2);

  TH1F* EWKFinal_bphi_2 = (TH1F*) EWKZLL_bphi_2->Clone();
  EWKFinal_bphi_2->Add(EWKZNuNu_bphi_2);

  data_obs_bphi_2->SetMarkerStyle(20);
  data_obs_bphi_2->Sumw2();
  
  data_obs_Fake_bphi_2->SetFillColor(kRed);
  data_obs_Fake_bphi_2->SetLineColor(kBlack);

  embedded_bphi_2->SetFillColor(kYellow);
  embedded_bphi_2->SetLineColor(kBlack);

  DYFinal_bphi_2->SetFillColor(kBlue);
  DYFinal_bphi_2->SetLineColor(kBlack);

  TTFinal_bphi_2->SetFillColor(kViolet-3);
  TTFinal_bphi_2->SetLineColor(kBlack);

  VVFinal_bphi_2->SetFillColor(kPink-3);
  VVFinal_bphi_2->SetLineColor(kBlack);

  STFinal_bphi_2->SetFillColor(kGreen);
  STFinal_bphi_2->SetLineColor(kBlack);

  qqH_htt125_bphi_2->SetFillColor(kCyan);
  qqH_htt125_bphi_2->SetLineColor(kBlack);

  ggH_htt125_bphi_2->SetFillColor(kCyan);
  ggH_htt125_bphi_2->SetLineColor(kBlack);

  VHFinal_bphi_2->SetFillColor(kOrange);
  VHFinal_bphi_2->SetLineColor(kBlack);

  EWKFinal_bphi_2->SetFillColor(kBlue-2);
  EWKFinal_bphi_2->SetLineColor(kBlack);
  
  THStack* BackgroundStack_bphi_2 = new THStack("BackgroundStack_bphi_2","BackgroundStack_bphi_2");
  BackgroundStack_bphi_2->Add(data_obs_Fake_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(DYFinal_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(embedded_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(TTFinal_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(VVFinal_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(STFinal_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(qqH_htt125_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(ggH_htt125_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(VHFinal_bphi_2,"hist");
  BackgroundStack_bphi_2->Add(EWKFinal_bphi_2,"hist");

  TH1F* BackgroundStack_bphi_2_Errors = MakeStackErrors(BackgroundStack_bphi_2);

  TPad* PlotPad_bphi_2 = MakeRatioPlot(CanvasTwenty, BackgroundStack_bphi_2, data_obs_bphi_2,"bphi_2");

  BackgroundStack_bphi_2->SetMaximum(max(BackgroundStack_bphi_2->GetMaximum(),data_obs_bphi_2->GetMaximum()));

  BackgroundStack_bphi_2->Draw();
  BackgroundStack_bphi_2_Errors->Draw("SAME e2");
  BackgroundStack_bphi_2->SetTitle("bphi_2");
  data_obs_bphi_2->Draw("SAME e1");
  BackgroundStack_bphi_2->GetYaxis()->SetTitle("Events");
  BackgroundStack_bphi_2->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_bphi_2,0,33);

  TLegend* Legend_bphi_2 = new TLegend(0.61,0.41,0.88,0.68);
  Legend_bphi_2->AddEntry(embedded_bphi_2,"embedded","f");
  Legend_bphi_2->AddEntry(DYFinal_bphi_2, "Other DY","f");
  Legend_bphi_2->AddEntry(TTFinal_bphi_2,"t#bar{t}","f");
  Legend_bphi_2->AddEntry(VVFinal_bphi_2,"Dibsoson","f");
  Legend_bphi_2->AddEntry(STFinal_bphi_2,"Single Top","f");
  Legend_bphi_2->AddEntry(qqH_htt125_bphi_2,"qqh","f");
  Legend_bphi_2->AddEntry(ggH_htt125_bphi_2,"ggH","f");
  Legend_bphi_2->AddEntry(VHFinal_bphi_2,"VH","f");
  Legend_bphi_2->AddEntry(EWKFinal_bphi_2,"EWK","f");
  Legend_bphi_2->AddEntry(data_obs_Fake_bphi_2,"Fakes","f");

  Legend_bphi_2->Draw();

  //npv
  TCanvas* CanvasTwentyOne = new TCanvas("CanvasTwentyOne","npv",550,550);
  CanvasTwentyOne->SetTickx();
  CanvasTwentyOne->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_npv = (TH1F*) HistoFile->Get("data_obs_npv");
  TH1F* data_obs_Fake_npv = (TH1F*) HistoFile->Get("data_obs_Fake_npv");
  TH1F* embedded_npv = (TH1F*) HistoFile->Get("embedded_npv");
  TH1F* DY_npv = (TH1F*) HistoFile->Get("DY_npv");
  TH1F* DYlow_npv = (TH1F*) HistoFile->Get("DYlow_npv");
  TH1F* TTToHadronic_npv = (TH1F*) HistoFile->Get("TTToHadronic_npv");
  TH1F* TTTo2L2Nu_npv = (TH1F*) HistoFile->Get("TTTo2L2Nu_npv");
  TH1F* TTToSemiLeptonic_npv = (TH1F*) HistoFile->Get("TTToSemiLeptonic_npv");
  TH1F* WW4Q_npv = (TH1F*) HistoFile->Get("WW4Q_npv");
  TH1F* WWLNuQQ_npv = (TH1F*) HistoFile->Get("WWLNuQQ_npv");
  TH1F* WZ2L2Q_npv = (TH1F*) HistoFile->Get("WZ2L2Q_npv");
  TH1F* WZ1L3Nu_npv = (TH1F*) HistoFile->Get("WZ1L3Nu_npv");
  TH1F* WZ3LNu_npv = (TH1F*) HistoFile->Get("WZ3LNu_npv");
  TH1F* WZ1L1Nu2Q_npv = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_npv");
  TH1F* ZZ4L_npv = (TH1F*) HistoFile->Get("ZZ4L_npv");
  TH1F* ZZ2L2Nu_npv = (TH1F*) HistoFile->Get("ZZ2L2Nu_npv");
  TH1F* ZZ2L2Q_npv = (TH1F*) HistoFile->Get("ZZ2L2Q_npv");
  TH1F* ST_t_antitop_npv = (TH1F*) HistoFile->Get("ST_t_antitop_npv");
  TH1F* ST_t_top_npv = (TH1F*) HistoFile->Get("ST_t_top_npv");
  TH1F* ST_tW_antitop_npv = (TH1F*) HistoFile->Get("ST_tW_antitop_npv");
  TH1F* ST_tW_top_npv = (TH1F*) HistoFile->Get("ST_tW_top_npv");
  TH1F* ggH_htt125_npv = (TH1F*) HistoFile->Get("ggH_htt125_npv");
  TH1F* qqH_htt125_npv = (TH1F*) HistoFile->Get("qqH_htt125_npv");  
  TH1F* WplusH125_npv = (TH1F*) HistoFile->Get("WplusH125_npv");
  TH1F* WminusH125_npv = (TH1F*) HistoFile->Get("WminusH125_npv");
  TH1F* ZH125_npv = (TH1F*) HistoFile->Get("ZH125_npv");
  TH1F* EWKZLL_npv = (TH1F*) HistoFile->Get("EWKZLL_npv");
  TH1F* EWKZNuNu_npv = (TH1F*) HistoFile->Get("EWKZNuNu_npv");

  TH1F* DYFinal_npv = (TH1F*) DY_npv->Clone();
  DYFinal_npv->Add(DYlow_npv);
  
  TH1F* TTFinal_npv = (TH1F*) TTToHadronic_npv->Clone();
  TTFinal_npv->Add(TTTo2L2Nu_npv);
  TTFinal_npv->Add(TTToSemiLeptonic_npv);
  
  TH1F* VVFinal_npv = (TH1F*) WW4Q_npv->Clone();
  VVFinal_npv->Add(WWLNuQQ_npv);
  VVFinal_npv->Add(WZ2L2Q_npv);
  VVFinal_npv->Add(WZ1L3Nu_npv);
  VVFinal_npv->Add(WZ3LNu_npv);
  VVFinal_npv->Add(WZ1L1Nu2Q_npv);
  VVFinal_npv->Add(ZZ4L_npv);
  VVFinal_npv->Add(ZZ2L2Nu_npv);
  VVFinal_npv->Add(ZZ2L2Q_npv);
  
  TH1F* STFinal_npv = (TH1F*) ST_t_antitop_npv->Clone();
  STFinal_npv->Add(ST_t_top_npv);
  STFinal_npv->Add(ST_tW_antitop_npv);
  STFinal_npv->Add(ST_tW_top_npv);

  TH1F* VHFinal_npv = (TH1F*) WplusH125_npv->Clone();
  VHFinal_npv->Add(WminusH125_npv);
  VHFinal_npv->Add(ZH125_npv);

  TH1F* EWKFinal_npv = (TH1F*) EWKZLL_npv->Clone();
  EWKFinal_npv->Add(EWKZNuNu_npv);

  data_obs_npv->SetMarkerStyle(20);
  data_obs_npv->Sumw2();
  
  data_obs_Fake_npv->SetFillColor(kRed);
  data_obs_Fake_npv->SetLineColor(kBlack);

  embedded_npv->SetFillColor(kYellow);
  embedded_npv->SetLineColor(kBlack);

  DYFinal_npv->SetFillColor(kBlue);
  DYFinal_npv->SetLineColor(kBlack);

  TTFinal_npv->SetFillColor(kViolet-3);
  TTFinal_npv->SetLineColor(kBlack);

  VVFinal_npv->SetFillColor(kPink-3);
  VVFinal_npv->SetLineColor(kBlack);

  STFinal_npv->SetFillColor(kGreen);
  STFinal_npv->SetLineColor(kBlack);

  qqH_htt125_npv->SetFillColor(kCyan);
  qqH_htt125_npv->SetLineColor(kBlack);

  ggH_htt125_npv->SetFillColor(kCyan);
  ggH_htt125_npv->SetLineColor(kBlack);

  VHFinal_npv->SetFillColor(kOrange);
  VHFinal_npv->SetLineColor(kBlack);

  EWKFinal_npv->SetFillColor(kBlue-2);
  EWKFinal_npv->SetLineColor(kBlack);
  
  THStack* BackgroundStack_npv = new THStack("BackgroundStack_npv","BackgroundStack_npv");
  BackgroundStack_npv->Add(data_obs_Fake_npv,"hist");
  BackgroundStack_npv->Add(DYFinal_npv,"hist");
  BackgroundStack_npv->Add(embedded_npv,"hist");
  BackgroundStack_npv->Add(TTFinal_npv,"hist");
  BackgroundStack_npv->Add(VVFinal_npv,"hist");
  BackgroundStack_npv->Add(STFinal_npv,"hist");
  BackgroundStack_npv->Add(qqH_htt125_npv,"hist");
  BackgroundStack_npv->Add(ggH_htt125_npv,"hist");
  BackgroundStack_npv->Add(VHFinal_npv,"hist");
  BackgroundStack_npv->Add(EWKFinal_npv,"hist");

  TH1F* BackgroundStack_npv_Errors = MakeStackErrors(BackgroundStack_npv);

  TPad* PlotPad_npv = MakeRatioPlot(CanvasTwentyOne, BackgroundStack_npv, data_obs_npv,"npv");

  BackgroundStack_npv->SetMaximum(max(BackgroundStack_npv->GetMaximum(),data_obs_npv->GetMaximum()));

  BackgroundStack_npv->Draw();
  BackgroundStack_npv_Errors->Draw("SAME e2");
  BackgroundStack_npv->SetTitle("npv");
  data_obs_npv->Draw("SAME e1");
  BackgroundStack_npv->GetYaxis()->SetTitle("Events");
  BackgroundStack_npv->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_npv,0,33);

  TLegend* Legend_npv = new TLegend(0.61,0.41,0.88,0.68);
  Legend_npv->AddEntry(embedded_npv,"embedded","f");
  Legend_npv->AddEntry(DYFinal_npv, "Other DY","f");
  Legend_npv->AddEntry(TTFinal_npv,"t#bar{t}","f");
  Legend_npv->AddEntry(VVFinal_npv,"Dibsoson","f");
  Legend_npv->AddEntry(STFinal_npv,"Single Top","f");
  Legend_npv->AddEntry(qqH_htt125_npv,"qqh","f");
  Legend_npv->AddEntry(ggH_htt125_npv,"ggH","f");
  Legend_npv->AddEntry(VHFinal_npv,"VH","f");
  Legend_npv->AddEntry(EWKFinal_npv,"EWK","f");
  Legend_npv->AddEntry(data_obs_Fake_npv,"Fakes","f");

  Legend_npv->Draw();

  //nbtag
  TCanvas* CanvasTwentyTwo = new TCanvas("CanvasTwentyTwo","nbtag",550,550);
  CanvasTwentyTwo->SetTickx();
  CanvasTwentyTwo->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_nbtag = (TH1F*) HistoFile->Get("data_obs_nbtag");
  TH1F* data_obs_Fake_nbtag = (TH1F*) HistoFile->Get("data_obs_Fake_nbtag");
  TH1F* embedded_nbtag = (TH1F*) HistoFile->Get("embedded_nbtag");
  TH1F* DY_nbtag = (TH1F*) HistoFile->Get("DY_nbtag");
  TH1F* DYlow_nbtag = (TH1F*) HistoFile->Get("DYlow_nbtag");
  TH1F* TTToHadronic_nbtag = (TH1F*) HistoFile->Get("TTToHadronic_nbtag");
  TH1F* TTTo2L2Nu_nbtag = (TH1F*) HistoFile->Get("TTTo2L2Nu_nbtag");
  TH1F* TTToSemiLeptonic_nbtag = (TH1F*) HistoFile->Get("TTToSemiLeptonic_nbtag");
  TH1F* WW4Q_nbtag = (TH1F*) HistoFile->Get("WW4Q_nbtag");
  TH1F* WWLNuQQ_nbtag = (TH1F*) HistoFile->Get("WWLNuQQ_nbtag");
  TH1F* WZ2L2Q_nbtag = (TH1F*) HistoFile->Get("WZ2L2Q_nbtag");
  TH1F* WZ1L3Nu_nbtag = (TH1F*) HistoFile->Get("WZ1L3Nu_nbtag");
  TH1F* WZ3LNu_nbtag = (TH1F*) HistoFile->Get("WZ3LNu_nbtag");
  TH1F* WZ1L1Nu2Q_nbtag = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_nbtag");
  TH1F* ZZ4L_nbtag = (TH1F*) HistoFile->Get("ZZ4L_nbtag");
  TH1F* ZZ2L2Nu_nbtag = (TH1F*) HistoFile->Get("ZZ2L2Nu_nbtag");
  TH1F* ZZ2L2Q_nbtag = (TH1F*) HistoFile->Get("ZZ2L2Q_nbtag");
  TH1F* ST_t_antitop_nbtag = (TH1F*) HistoFile->Get("ST_t_antitop_nbtag");
  TH1F* ST_t_top_nbtag = (TH1F*) HistoFile->Get("ST_t_top_nbtag");
  TH1F* ST_tW_antitop_nbtag = (TH1F*) HistoFile->Get("ST_tW_antitop_nbtag");
  TH1F* ST_tW_top_nbtag = (TH1F*) HistoFile->Get("ST_tW_top_nbtag");
  TH1F* ggH_htt125_nbtag = (TH1F*) HistoFile->Get("ggH_htt125_nbtag");
  TH1F* qqH_htt125_nbtag = (TH1F*) HistoFile->Get("qqH_htt125_nbtag");  
  TH1F* WplusH125_nbtag = (TH1F*) HistoFile->Get("WplusH125_nbtag");
  TH1F* WminusH125_nbtag = (TH1F*) HistoFile->Get("WminusH125_nbtag");
  TH1F* ZH125_nbtag = (TH1F*) HistoFile->Get("ZH125_nbtag");
  TH1F* EWKZLL_nbtag = (TH1F*) HistoFile->Get("EWKZLL_nbtag");
  TH1F* EWKZNuNu_nbtag = (TH1F*) HistoFile->Get("EWKZNuNu_nbtag");

  TH1F* DYFinal_nbtag = (TH1F*) DY_nbtag->Clone();
  DYFinal_nbtag->Add(DYlow_nbtag);
  
  TH1F* TTFinal_nbtag = (TH1F*) TTToHadronic_nbtag->Clone();
  TTFinal_nbtag->Add(TTTo2L2Nu_nbtag);
  TTFinal_nbtag->Add(TTToSemiLeptonic_nbtag);
  
  TH1F* VVFinal_nbtag = (TH1F*) WW4Q_nbtag->Clone();
  VVFinal_nbtag->Add(WWLNuQQ_nbtag);
  VVFinal_nbtag->Add(WZ2L2Q_nbtag);
  VVFinal_nbtag->Add(WZ1L3Nu_nbtag);
  VVFinal_nbtag->Add(WZ3LNu_nbtag);
  VVFinal_nbtag->Add(WZ1L1Nu2Q_nbtag);
  VVFinal_nbtag->Add(ZZ4L_nbtag);
  VVFinal_nbtag->Add(ZZ2L2Nu_nbtag);
  VVFinal_nbtag->Add(ZZ2L2Q_nbtag);
  
  TH1F* STFinal_nbtag = (TH1F*) ST_t_antitop_nbtag->Clone();
  STFinal_nbtag->Add(ST_t_top_nbtag);
  STFinal_nbtag->Add(ST_tW_antitop_nbtag);
  STFinal_nbtag->Add(ST_tW_top_nbtag);

  TH1F* VHFinal_nbtag = (TH1F*) WplusH125_nbtag->Clone();
  VHFinal_nbtag->Add(WminusH125_nbtag);
  VHFinal_nbtag->Add(ZH125_nbtag);

  TH1F* EWKFinal_nbtag = (TH1F*) EWKZLL_nbtag->Clone();
  EWKFinal_nbtag->Add(EWKZNuNu_nbtag);

  data_obs_nbtag->SetMarkerStyle(20);
  data_obs_nbtag->Sumw2();
  
  data_obs_Fake_nbtag->SetFillColor(kRed);
  data_obs_Fake_nbtag->SetLineColor(kBlack);

  embedded_nbtag->SetFillColor(kYellow);
  embedded_nbtag->SetLineColor(kBlack);

  DYFinal_nbtag->SetFillColor(kBlue);
  DYFinal_nbtag->SetLineColor(kBlack);

  TTFinal_nbtag->SetFillColor(kViolet-3);
  TTFinal_nbtag->SetLineColor(kBlack);

  VVFinal_nbtag->SetFillColor(kPink-3);
  VVFinal_nbtag->SetLineColor(kBlack);

  STFinal_nbtag->SetFillColor(kGreen);
  STFinal_nbtag->SetLineColor(kBlack);

  qqH_htt125_nbtag->SetFillColor(kCyan);
  qqH_htt125_nbtag->SetLineColor(kBlack);

  ggH_htt125_nbtag->SetFillColor(kCyan);
  ggH_htt125_nbtag->SetLineColor(kBlack);

  VHFinal_nbtag->SetFillColor(kOrange);
  VHFinal_nbtag->SetLineColor(kBlack);

  EWKFinal_nbtag->SetFillColor(kBlue-2);
  EWKFinal_nbtag->SetLineColor(kBlack);
  
  THStack* BackgroundStack_nbtag = new THStack("BackgroundStack_nbtag","BackgroundStack_nbtag");
  BackgroundStack_nbtag->Add(data_obs_Fake_nbtag,"hist");
  BackgroundStack_nbtag->Add(DYFinal_nbtag,"hist");
  BackgroundStack_nbtag->Add(embedded_nbtag,"hist");
  BackgroundStack_nbtag->Add(TTFinal_nbtag,"hist");
  BackgroundStack_nbtag->Add(VVFinal_nbtag,"hist");
  BackgroundStack_nbtag->Add(STFinal_nbtag,"hist");
  BackgroundStack_nbtag->Add(qqH_htt125_nbtag,"hist");
  BackgroundStack_nbtag->Add(ggH_htt125_nbtag,"hist");
  BackgroundStack_nbtag->Add(VHFinal_nbtag,"hist");
  BackgroundStack_nbtag->Add(EWKFinal_nbtag,"hist");

  TH1F* BackgroundStack_nbtag_Errors = MakeStackErrors(BackgroundStack_nbtag);

  TPad* PlotPad_nbtag = MakeRatioPlot(CanvasTwentyTwo, BackgroundStack_nbtag, data_obs_nbtag,"nbtag");

  BackgroundStack_nbtag->SetMaximum(max(BackgroundStack_nbtag->GetMaximum(),data_obs_nbtag->GetMaximum()));

  BackgroundStack_nbtag->Draw();
  BackgroundStack_nbtag_Errors->Draw("SAME e2");
  BackgroundStack_nbtag->SetTitle("nbtag");
  data_obs_nbtag->Draw("SAME e1");
  BackgroundStack_nbtag->GetYaxis()->SetTitle("Events");
  BackgroundStack_nbtag->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_nbtag,0,33);

  TLegend* Legend_nbtag = new TLegend(0.61,0.41,0.88,0.68);
  Legend_nbtag->AddEntry(embedded_nbtag,"embedded","f");
  Legend_nbtag->AddEntry(DYFinal_nbtag, "Other DY","f");
  Legend_nbtag->AddEntry(TTFinal_nbtag,"t#bar{t}","f");
  Legend_nbtag->AddEntry(VVFinal_nbtag,"Dibsoson","f");
  Legend_nbtag->AddEntry(STFinal_nbtag,"Single Top","f");
  Legend_nbtag->AddEntry(qqH_htt125_nbtag,"qqh","f");
  Legend_nbtag->AddEntry(ggH_htt125_nbtag,"ggH","f");
  Legend_nbtag->AddEntry(VHFinal_nbtag,"VH","f");
  Legend_nbtag->AddEntry(EWKFinal_nbtag,"EWK","f");
  Legend_nbtag->AddEntry(data_obs_Fake_nbtag,"Fakes","f");

  Legend_nbtag->Draw();

  //vismass
  TCanvas* CanvasTwentyThree = new TCanvas("CanvasTwentyThree","vismass",550,550);
  CanvasTwentyThree->SetTickx();
  CanvasTwentyThree->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_vismass = (TH1F*) HistoFile->Get("data_obs_vismass");
  TH1F* data_obs_Fake_vismass = (TH1F*) HistoFile->Get("data_obs_Fake_vismass");
  TH1F* embedded_vismass = (TH1F*) HistoFile->Get("embedded_vismass");
  TH1F* DY_vismass = (TH1F*) HistoFile->Get("DY_vismass");
  TH1F* DYlow_vismass = (TH1F*) HistoFile->Get("DYlow_vismass");
  TH1F* TTToHadronic_vismass = (TH1F*) HistoFile->Get("TTToHadronic_vismass");
  TH1F* TTTo2L2Nu_vismass = (TH1F*) HistoFile->Get("TTTo2L2Nu_vismass");
  TH1F* TTToSemiLeptonic_vismass = (TH1F*) HistoFile->Get("TTToSemiLeptonic_vismass");
  TH1F* WW4Q_vismass = (TH1F*) HistoFile->Get("WW4Q_vismass");
  TH1F* WWLNuQQ_vismass = (TH1F*) HistoFile->Get("WWLNuQQ_vismass");
  TH1F* WZ2L2Q_vismass = (TH1F*) HistoFile->Get("WZ2L2Q_vismass");
  TH1F* WZ1L3Nu_vismass = (TH1F*) HistoFile->Get("WZ1L3Nu_vismass");
  TH1F* WZ3LNu_vismass = (TH1F*) HistoFile->Get("WZ3LNu_vismass");
  TH1F* WZ1L1Nu2Q_vismass = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_vismass");
  TH1F* ZZ4L_vismass = (TH1F*) HistoFile->Get("ZZ4L_vismass");
  TH1F* ZZ2L2Nu_vismass = (TH1F*) HistoFile->Get("ZZ2L2Nu_vismass");
  TH1F* ZZ2L2Q_vismass = (TH1F*) HistoFile->Get("ZZ2L2Q_vismass");
  TH1F* ST_t_antitop_vismass = (TH1F*) HistoFile->Get("ST_t_antitop_vismass");
  TH1F* ST_t_top_vismass = (TH1F*) HistoFile->Get("ST_t_top_vismass");
  TH1F* ST_tW_antitop_vismass = (TH1F*) HistoFile->Get("ST_tW_antitop_vismass");
  TH1F* ST_tW_top_vismass = (TH1F*) HistoFile->Get("ST_tW_top_vismass");
  TH1F* ggH_htt125_vismass = (TH1F*) HistoFile->Get("ggH_htt125_vismass");
  TH1F* qqH_htt125_vismass = (TH1F*) HistoFile->Get("qqH_htt125_vismass");  
  TH1F* WplusH125_vismass = (TH1F*) HistoFile->Get("WplusH125_vismass");
  TH1F* WminusH125_vismass = (TH1F*) HistoFile->Get("WminusH125_vismass");
  TH1F* ZH125_vismass = (TH1F*) HistoFile->Get("ZH125_vismass");
  TH1F* EWKZLL_vismass = (TH1F*) HistoFile->Get("EWKZLL_vismass");
  TH1F* EWKZNuNu_vismass = (TH1F*) HistoFile->Get("EWKZNuNu_vismass");

  TH1F* DYFinal_vismass = (TH1F*) DY_vismass->Clone();
  DYFinal_vismass->Add(DYlow_vismass);
  
  TH1F* TTFinal_vismass = (TH1F*) TTToHadronic_vismass->Clone();
  TTFinal_vismass->Add(TTTo2L2Nu_vismass);
  TTFinal_vismass->Add(TTToSemiLeptonic_vismass);
  
  TH1F* VVFinal_vismass = (TH1F*) WW4Q_vismass->Clone();
  VVFinal_vismass->Add(WWLNuQQ_vismass);
  VVFinal_vismass->Add(WZ2L2Q_vismass);
  VVFinal_vismass->Add(WZ1L3Nu_vismass);
  VVFinal_vismass->Add(WZ3LNu_vismass);
  VVFinal_vismass->Add(WZ1L1Nu2Q_vismass);
  VVFinal_vismass->Add(ZZ4L_vismass);
  VVFinal_vismass->Add(ZZ2L2Nu_vismass);
  VVFinal_vismass->Add(ZZ2L2Q_vismass);
  
  TH1F* STFinal_vismass = (TH1F*) ST_t_antitop_vismass->Clone();
  STFinal_vismass->Add(ST_t_top_vismass);
  STFinal_vismass->Add(ST_tW_antitop_vismass);
  STFinal_vismass->Add(ST_tW_top_vismass);

  TH1F* VHFinal_vismass = (TH1F*) WplusH125_vismass->Clone();
  VHFinal_vismass->Add(WminusH125_vismass);
  VHFinal_vismass->Add(ZH125_vismass);

  TH1F* EWKFinal_vismass = (TH1F*) EWKZLL_vismass->Clone();
  EWKFinal_vismass->Add(EWKZNuNu_vismass);

  data_obs_vismass->SetMarkerStyle(20);
  data_obs_vismass->Sumw2();
  
  data_obs_Fake_vismass->SetFillColor(kRed);
  data_obs_Fake_vismass->SetLineColor(kBlack);

  embedded_vismass->SetFillColor(kYellow);
  embedded_vismass->SetLineColor(kBlack);

  DYFinal_vismass->SetFillColor(kBlue);
  DYFinal_vismass->SetLineColor(kBlack);

  TTFinal_vismass->SetFillColor(kViolet-3);
  TTFinal_vismass->SetLineColor(kBlack);

  VVFinal_vismass->SetFillColor(kPink-3);
  VVFinal_vismass->SetLineColor(kBlack);

  STFinal_vismass->SetFillColor(kGreen);
  STFinal_vismass->SetLineColor(kBlack);

  qqH_htt125_vismass->SetFillColor(kCyan);
  qqH_htt125_vismass->SetLineColor(kBlack);

  ggH_htt125_vismass->SetFillColor(kCyan);
  ggH_htt125_vismass->SetLineColor(kBlack);

  VHFinal_vismass->SetFillColor(kOrange);
  VHFinal_vismass->SetLineColor(kBlack);

  EWKFinal_vismass->SetFillColor(kBlue-2);
  EWKFinal_vismass->SetLineColor(kBlack);
  
  THStack* BackgroundStack_vismass = new THStack("BackgroundStack_vismass","BackgroundStack_vismass");
  BackgroundStack_vismass->Add(data_obs_Fake_vismass,"hist");
  BackgroundStack_vismass->Add(DYFinal_vismass,"hist");
  BackgroundStack_vismass->Add(embedded_vismass,"hist");
  BackgroundStack_vismass->Add(TTFinal_vismass,"hist");
  BackgroundStack_vismass->Add(VVFinal_vismass,"hist");
  BackgroundStack_vismass->Add(STFinal_vismass,"hist");
  BackgroundStack_vismass->Add(qqH_htt125_vismass,"hist");
  BackgroundStack_vismass->Add(ggH_htt125_vismass,"hist");
  BackgroundStack_vismass->Add(VHFinal_vismass,"hist");
  BackgroundStack_vismass->Add(EWKFinal_vismass,"hist");

  TH1F* BackgroundStack_vismass_Errors = MakeStackErrors(BackgroundStack_vismass);

  TPad* PlotPad_vismass = MakeRatioPlot(CanvasTwentyThree, BackgroundStack_vismass, data_obs_vismass,"m_{vis}");

  BackgroundStack_vismass->SetMaximum(max(BackgroundStack_vismass->GetMaximum(),data_obs_vismass->GetMaximum()));

  BackgroundStack_vismass->Draw();
  BackgroundStack_vismass_Errors->Draw("SAME e2");
  BackgroundStack_vismass->SetTitle("m_{vis}");
  data_obs_vismass->Draw("SAME e1");
  BackgroundStack_vismass->GetYaxis()->SetTitle("Events");
  BackgroundStack_vismass->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_vismass,0,33);

  TLegend* Legend_vismass = new TLegend(0.61,0.41,0.88,0.68);
  Legend_vismass->AddEntry(embedded_vismass,"embedded","f");
  Legend_vismass->AddEntry(DYFinal_vismass, "Other DY","f");
  Legend_vismass->AddEntry(TTFinal_vismass,"t#bar{t}","f");
  Legend_vismass->AddEntry(VVFinal_vismass,"Dibsoson","f");
  Legend_vismass->AddEntry(STFinal_vismass,"Single Top","f");
  Legend_vismass->AddEntry(qqH_htt125_vismass,"qqh","f");
  Legend_vismass->AddEntry(ggH_htt125_vismass,"ggH","f");
  Legend_vismass->AddEntry(VHFinal_vismass,"VH","f");
  Legend_vismass->AddEntry(EWKFinal_vismass,"EWK","f");
  Legend_vismass->AddEntry(data_obs_Fake_vismass,"Fakes","f");

  Legend_vismass->Draw();

  //met
  TCanvas* CanvasTwentyFour = new TCanvas("CanvasTwentyFour","met",550,550);
  CanvasTwentyFour->SetTickx();
  CanvasTwentyFour->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_met = (TH1F*) HistoFile->Get("data_obs_met");
  TH1F* data_obs_Fake_met = (TH1F*) HistoFile->Get("data_obs_Fake_met");
  TH1F* embedded_met = (TH1F*) HistoFile->Get("embedded_met");
  TH1F* DY_met = (TH1F*) HistoFile->Get("DY_met");
  TH1F* DYlow_met = (TH1F*) HistoFile->Get("DYlow_met");
  TH1F* TTToHadronic_met = (TH1F*) HistoFile->Get("TTToHadronic_met");
  TH1F* TTTo2L2Nu_met = (TH1F*) HistoFile->Get("TTTo2L2Nu_met");
  TH1F* TTToSemiLeptonic_met = (TH1F*) HistoFile->Get("TTToSemiLeptonic_met");
  TH1F* WW4Q_met = (TH1F*) HistoFile->Get("WW4Q_met");
  TH1F* WWLNuQQ_met = (TH1F*) HistoFile->Get("WWLNuQQ_met");
  TH1F* WZ2L2Q_met = (TH1F*) HistoFile->Get("WZ2L2Q_met");
  TH1F* WZ1L3Nu_met = (TH1F*) HistoFile->Get("WZ1L3Nu_met");
  TH1F* WZ3LNu_met = (TH1F*) HistoFile->Get("WZ3LNu_met");
  TH1F* WZ1L1Nu2Q_met = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_met");
  TH1F* ZZ4L_met = (TH1F*) HistoFile->Get("ZZ4L_met");
  TH1F* ZZ2L2Nu_met = (TH1F*) HistoFile->Get("ZZ2L2Nu_met");
  TH1F* ZZ2L2Q_met = (TH1F*) HistoFile->Get("ZZ2L2Q_met");
  TH1F* ST_t_antitop_met = (TH1F*) HistoFile->Get("ST_t_antitop_met");
  TH1F* ST_t_top_met = (TH1F*) HistoFile->Get("ST_t_top_met");
  TH1F* ST_tW_antitop_met = (TH1F*) HistoFile->Get("ST_tW_antitop_met");
  TH1F* ST_tW_top_met = (TH1F*) HistoFile->Get("ST_tW_top_met");
  TH1F* ggH_htt125_met = (TH1F*) HistoFile->Get("ggH_htt125_met");
  TH1F* qqH_htt125_met = (TH1F*) HistoFile->Get("qqH_htt125_met");  
  TH1F* WplusH125_met = (TH1F*) HistoFile->Get("WplusH125_met");
  TH1F* WminusH125_met = (TH1F*) HistoFile->Get("WminusH125_met");
  TH1F* ZH125_met = (TH1F*) HistoFile->Get("ZH125_met");
  TH1F* EWKZLL_met = (TH1F*) HistoFile->Get("EWKZLL_met");
  TH1F* EWKZNuNu_met = (TH1F*) HistoFile->Get("EWKZNuNu_met");

  TH1F* DYFinal_met = (TH1F*) DY_met->Clone();
  DYFinal_met->Add(DYlow_met);
  
  TH1F* TTFinal_met = (TH1F*) TTToHadronic_met->Clone();
  TTFinal_met->Add(TTTo2L2Nu_met);
  TTFinal_met->Add(TTToSemiLeptonic_met);
  
  TH1F* VVFinal_met = (TH1F*) WW4Q_met->Clone();
  VVFinal_met->Add(WWLNuQQ_met);
  VVFinal_met->Add(WZ2L2Q_met);
  VVFinal_met->Add(WZ1L3Nu_met);
  VVFinal_met->Add(WZ3LNu_met);
  VVFinal_met->Add(WZ1L1Nu2Q_met);
  VVFinal_met->Add(ZZ4L_met);
  VVFinal_met->Add(ZZ2L2Nu_met);
  VVFinal_met->Add(ZZ2L2Q_met);
  
  TH1F* STFinal_met = (TH1F*) ST_t_antitop_met->Clone();
  STFinal_met->Add(ST_t_top_met);
  STFinal_met->Add(ST_tW_antitop_met);
  STFinal_met->Add(ST_tW_top_met);

  TH1F* VHFinal_met = (TH1F*) WplusH125_met->Clone();
  VHFinal_met->Add(WminusH125_met);
  VHFinal_met->Add(ZH125_met);

  TH1F* EWKFinal_met = (TH1F*) EWKZLL_met->Clone();
  EWKFinal_met->Add(EWKZNuNu_met);

  data_obs_met->SetMarkerStyle(20);
  data_obs_met->Sumw2();
  
  data_obs_Fake_met->SetFillColor(kRed);
  data_obs_Fake_met->SetLineColor(kBlack);

  embedded_met->SetFillColor(kYellow);
  embedded_met->SetLineColor(kBlack);

  DYFinal_met->SetFillColor(kBlue);
  DYFinal_met->SetLineColor(kBlack);

  TTFinal_met->SetFillColor(kViolet-3);
  TTFinal_met->SetLineColor(kBlack);

  VVFinal_met->SetFillColor(kPink-3);
  VVFinal_met->SetLineColor(kBlack);

  STFinal_met->SetFillColor(kGreen);
  STFinal_met->SetLineColor(kBlack);

  qqH_htt125_met->SetFillColor(kCyan);
  qqH_htt125_met->SetLineColor(kBlack);

  ggH_htt125_met->SetFillColor(kCyan);
  ggH_htt125_met->SetLineColor(kBlack);

  VHFinal_met->SetFillColor(kOrange);
  VHFinal_met->SetLineColor(kBlack);

  EWKFinal_met->SetFillColor(kBlue-2);
  EWKFinal_met->SetLineColor(kBlack);
  
  THStack* BackgroundStack_met = new THStack("BackgroundStack_met","BackgroundStack_met");
  BackgroundStack_met->Add(data_obs_Fake_met,"hist");
  BackgroundStack_met->Add(DYFinal_met,"hist");
  BackgroundStack_met->Add(embedded_met,"hist");
  BackgroundStack_met->Add(TTFinal_met,"hist");
  BackgroundStack_met->Add(VVFinal_met,"hist");
  BackgroundStack_met->Add(STFinal_met,"hist");
  BackgroundStack_met->Add(qqH_htt125_met,"hist");
  BackgroundStack_met->Add(ggH_htt125_met,"hist");
  BackgroundStack_met->Add(VHFinal_met,"hist");
  BackgroundStack_met->Add(EWKFinal_met,"hist");

  TH1F* BackgroundStack_met_Errors = MakeStackErrors(BackgroundStack_met);

  TPad* PlotPad_met = MakeRatioPlot(CanvasTwentyFour, BackgroundStack_met, data_obs_met,"met");

  BackgroundStack_met->SetMaximum(max(BackgroundStack_met->GetMaximum(),data_obs_met->GetMaximum()));

  BackgroundStack_met->Draw();
  BackgroundStack_met_Errors->Draw("SAME e2");
  BackgroundStack_met->SetTitle("met");
  data_obs_met->Draw("SAME e1");
  BackgroundStack_met->GetYaxis()->SetTitle("Events");
  BackgroundStack_met->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_met,0,33);

  TLegend* Legend_met = new TLegend(0.61,0.41,0.88,0.68);
  Legend_met->AddEntry(embedded_met,"embedded","f");
  Legend_met->AddEntry(DYFinal_met, "Other DY","f");
  Legend_met->AddEntry(TTFinal_met,"t#bar{t}","f");
  Legend_met->AddEntry(VVFinal_met,"Dibsoson","f");
  Legend_met->AddEntry(STFinal_met,"Single Top","f");
  Legend_met->AddEntry(qqH_htt125_met,"qqh","f");
  Legend_met->AddEntry(ggH_htt125_met,"ggH","f");
  Legend_met->AddEntry(VHFinal_met,"VH","f");
  Legend_met->AddEntry(EWKFinal_met,"EWK","f");
  Legend_met->AddEntry(data_obs_Fake_met,"Fakes","f");

  Legend_met->Draw();

  //metphi
  TCanvas* CanvasTwentyFive = new TCanvas("CanvasTwentyFive","metphi",550,550);
  CanvasTwentyFive->SetTickx();
  CanvasTwentyFive->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_metphi = (TH1F*) HistoFile->Get("data_obs_metphi");
  TH1F* data_obs_Fake_metphi = (TH1F*) HistoFile->Get("data_obs_Fake_metphi");
  TH1F* embedded_metphi = (TH1F*) HistoFile->Get("embedded_metphi");
  TH1F* DY_metphi = (TH1F*) HistoFile->Get("DY_metphi");
  TH1F* DYlow_metphi = (TH1F*) HistoFile->Get("DYlow_metphi");
  TH1F* TTToHadronic_metphi = (TH1F*) HistoFile->Get("TTToHadronic_metphi");
  TH1F* TTTo2L2Nu_metphi = (TH1F*) HistoFile->Get("TTTo2L2Nu_metphi");
  TH1F* TTToSemiLeptonic_metphi = (TH1F*) HistoFile->Get("TTToSemiLeptonic_metphi");
  TH1F* WW4Q_metphi = (TH1F*) HistoFile->Get("WW4Q_metphi");
  TH1F* WWLNuQQ_metphi = (TH1F*) HistoFile->Get("WWLNuQQ_metphi");
  TH1F* WZ2L2Q_metphi = (TH1F*) HistoFile->Get("WZ2L2Q_metphi");
  TH1F* WZ1L3Nu_metphi = (TH1F*) HistoFile->Get("WZ1L3Nu_metphi");
  TH1F* WZ3LNu_metphi = (TH1F*) HistoFile->Get("WZ3LNu_metphi");
  TH1F* WZ1L1Nu2Q_metphi = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_metphi");
  TH1F* ZZ4L_metphi = (TH1F*) HistoFile->Get("ZZ4L_metphi");
  TH1F* ZZ2L2Nu_metphi = (TH1F*) HistoFile->Get("ZZ2L2Nu_metphi");
  TH1F* ZZ2L2Q_metphi = (TH1F*) HistoFile->Get("ZZ2L2Q_metphi");
  TH1F* ST_t_antitop_metphi = (TH1F*) HistoFile->Get("ST_t_antitop_metphi");
  TH1F* ST_t_top_metphi = (TH1F*) HistoFile->Get("ST_t_top_metphi");
  TH1F* ST_tW_antitop_metphi = (TH1F*) HistoFile->Get("ST_tW_antitop_metphi");
  TH1F* ST_tW_top_metphi = (TH1F*) HistoFile->Get("ST_tW_top_metphi");
  TH1F* ggH_htt125_metphi = (TH1F*) HistoFile->Get("ggH_htt125_metphi");
  TH1F* qqH_htt125_metphi = (TH1F*) HistoFile->Get("qqH_htt125_metphi");  
  TH1F* WplusH125_metphi = (TH1F*) HistoFile->Get("WplusH125_metphi");
  TH1F* WminusH125_metphi = (TH1F*) HistoFile->Get("WminusH125_metphi");
  TH1F* ZH125_metphi = (TH1F*) HistoFile->Get("ZH125_metphi");
  TH1F* EWKZLL_metphi = (TH1F*) HistoFile->Get("EWKZLL_metphi");
  TH1F* EWKZNuNu_metphi = (TH1F*) HistoFile->Get("EWKZNuNu_metphi");

  TH1F* DYFinal_metphi = (TH1F*) DY_metphi->Clone();
  DYFinal_metphi->Add(DYlow_metphi);
  
  TH1F* TTFinal_metphi = (TH1F*) TTToHadronic_metphi->Clone();
  TTFinal_metphi->Add(TTTo2L2Nu_metphi);
  TTFinal_metphi->Add(TTToSemiLeptonic_metphi);
  
  TH1F* VVFinal_metphi = (TH1F*) WW4Q_metphi->Clone();
  VVFinal_metphi->Add(WWLNuQQ_metphi);
  VVFinal_metphi->Add(WZ2L2Q_metphi);
  VVFinal_metphi->Add(WZ1L3Nu_metphi);
  VVFinal_metphi->Add(WZ3LNu_metphi);
  VVFinal_metphi->Add(WZ1L1Nu2Q_metphi);
  VVFinal_metphi->Add(ZZ4L_metphi);
  VVFinal_metphi->Add(ZZ2L2Nu_metphi);
  VVFinal_metphi->Add(ZZ2L2Q_metphi);
  
  TH1F* STFinal_metphi = (TH1F*) ST_t_antitop_metphi->Clone();
  STFinal_metphi->Add(ST_t_top_metphi);
  STFinal_metphi->Add(ST_tW_antitop_metphi);
  STFinal_metphi->Add(ST_tW_top_metphi);

  TH1F* VHFinal_metphi = (TH1F*) WplusH125_metphi->Clone();
  VHFinal_metphi->Add(WminusH125_metphi);
  VHFinal_metphi->Add(ZH125_metphi);

  TH1F* EWKFinal_metphi = (TH1F*) EWKZLL_metphi->Clone();
  EWKFinal_metphi->Add(EWKZNuNu_metphi);

  data_obs_metphi->SetMarkerStyle(20);
  data_obs_metphi->Sumw2();
  
  data_obs_Fake_metphi->SetFillColor(kRed);
  data_obs_Fake_metphi->SetLineColor(kBlack);

  embedded_metphi->SetFillColor(kYellow);
  embedded_metphi->SetLineColor(kBlack);

  DYFinal_metphi->SetFillColor(kBlue);
  DYFinal_metphi->SetLineColor(kBlack);

  TTFinal_metphi->SetFillColor(kViolet-3);
  TTFinal_metphi->SetLineColor(kBlack);

  VVFinal_metphi->SetFillColor(kPink-3);
  VVFinal_metphi->SetLineColor(kBlack);

  STFinal_metphi->SetFillColor(kGreen);
  STFinal_metphi->SetLineColor(kBlack);

  qqH_htt125_metphi->SetFillColor(kCyan);
  qqH_htt125_metphi->SetLineColor(kBlack);

  ggH_htt125_metphi->SetFillColor(kCyan);
  ggH_htt125_metphi->SetLineColor(kBlack);

  VHFinal_metphi->SetFillColor(kOrange);
  VHFinal_metphi->SetLineColor(kBlack);

  EWKFinal_metphi->SetFillColor(kBlue-2);
  EWKFinal_metphi->SetLineColor(kBlack);
  
  THStack* BackgroundStack_metphi = new THStack("BackgroundStack_metphi","BackgroundStack_metphi");
  BackgroundStack_metphi->Add(data_obs_Fake_metphi,"hist");
  BackgroundStack_metphi->Add(DYFinal_metphi,"hist");
  BackgroundStack_metphi->Add(embedded_metphi,"hist");
  BackgroundStack_metphi->Add(TTFinal_metphi,"hist");
  BackgroundStack_metphi->Add(VVFinal_metphi,"hist");
  BackgroundStack_metphi->Add(STFinal_metphi,"hist");
  BackgroundStack_metphi->Add(qqH_htt125_metphi,"hist");
  BackgroundStack_metphi->Add(ggH_htt125_metphi,"hist");
  BackgroundStack_metphi->Add(VHFinal_metphi,"hist");
  BackgroundStack_metphi->Add(EWKFinal_metphi,"hist");

  TH1F* BackgroundStack_metphi_Errors = MakeStackErrors(BackgroundStack_metphi);

  TPad* PlotPad_metphi = MakeRatioPlot(CanvasTwentyFive, BackgroundStack_metphi, data_obs_metphi,"metphi");

  BackgroundStack_metphi->SetMaximum(max(BackgroundStack_metphi->GetMaximum(),data_obs_metphi->GetMaximum()));

  BackgroundStack_metphi->Draw();
  BackgroundStack_metphi_Errors->Draw("SAME e2");
  BackgroundStack_metphi->SetTitle("metphi");
  data_obs_metphi->Draw("SAME e1");
  BackgroundStack_metphi->GetYaxis()->SetTitle("Events");
  BackgroundStack_metphi->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_metphi,0,33);

  TLegend* Legend_metphi = new TLegend(0.61,0.41,0.88,0.68);
  Legend_metphi->AddEntry(embedded_metphi,"embedded","f");
  Legend_metphi->AddEntry(DYFinal_metphi, "Other DY","f");
  Legend_metphi->AddEntry(TTFinal_metphi,"t#bar{t}","f");
  Legend_metphi->AddEntry(VVFinal_metphi,"Dibsoson","f");
  Legend_metphi->AddEntry(STFinal_metphi,"Single Top","f");
  Legend_metphi->AddEntry(qqH_htt125_metphi,"qqh","f");
  Legend_metphi->AddEntry(ggH_htt125_metphi,"ggH","f");
  Legend_metphi->AddEntry(VHFinal_metphi,"VH","f");
  Legend_metphi->AddEntry(EWKFinal_metphi,"EWK","f");
  Legend_metphi->AddEntry(data_obs_Fake_metphi,"Fakes","f");

  Legend_metphi->Draw();
  
  //Vis Mass?
}
