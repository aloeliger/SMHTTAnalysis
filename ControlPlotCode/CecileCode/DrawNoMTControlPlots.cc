#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"

void DrawNoMTControlPlots()
{
  setTDRStyle();

  writeExtraText=true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* HistoFile = new TFile("ControlFile.root","READ");  

  //Met phi
  TCanvas* CanvasOne = new TCanvas("CanvasOne","MetPhi_BeforeMt",550,550);
  CanvasOne->SetTickx();
  CanvasOne->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("data_obs_MetPhi_BeforeMt");
  TH1F* data_obs_Fake_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("data_obs_Fake_MetPhi_BeforeMt");
  TH1F* embedded_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("embedded_MetPhi_BeforeMt");
  TH1F* DY_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("DY_MetPhi_BeforeMt");
  TH1F* DYlow_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("DYlow_MetPhi_BeforeMt");
  TH1F* TTToHadronic_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("TTToHadronic_MetPhi_BeforeMt");
  TH1F* TTTo2L2Nu_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("TTTo2L2Nu_MetPhi_BeforeMt");
  TH1F* TTToSemiLeptonic_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_MetPhi_BeforeMt");
  TH1F* WW4Q_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WW4Q_MetPhi_BeforeMt");
  TH1F* WWLNuQQ_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WWLNuQQ_MetPhi_BeforeMt");
  TH1F* WZ2L2Q_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WZ2L2Q_MetPhi_BeforeMt");
  TH1F* WZ1L3Nu_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WZ1L3Nu_MetPhi_BeforeMt");
  TH1F* WZ3LNu_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WZ3LNu_MetPhi_BeforeMt");
  TH1F* WZ1L1Nu2Q_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_MetPhi_BeforeMt");
  TH1F* ZZ4L_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ZZ4L_MetPhi_BeforeMt");
  TH1F* ZZ2L2Nu_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Nu_MetPhi_BeforeMt");
  TH1F* ZZ2L2Q_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Q_MetPhi_BeforeMt");
  TH1F* ST_t_antitop_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ST_t_antitop_MetPhi_BeforeMt");
  TH1F* ST_t_top_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ST_t_top_MetPhi_BeforeMt");
  TH1F* ST_tW_antitop_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_antitop_MetPhi_BeforeMt");
  TH1F* ST_tW_top_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_top_MetPhi_BeforeMt");
  TH1F* ggH_htt125_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ggH_htt125_MetPhi_BeforeMt");
  TH1F* qqH_htt125_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("qqH_htt125_MetPhi_BeforeMt");  
  TH1F* WplusH125_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WplusH125_MetPhi_BeforeMt");
  TH1F* WminusH125_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("WminusH125_MetPhi_BeforeMt");
  TH1F* ZH125_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("ZH125_MetPhi_BeforeMt");
  TH1F* EWKZLL_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("EWKZLL_MetPhi_BeforeMt");
  TH1F* EWKZNuNu_MetPhi_BeforeMt = (TH1F*) HistoFile->Get("EWKZNuNu_MetPhi_BeforeMt");

  TH1F* DYFinal_MetPhi_BeforeMt = (TH1F*) DY_MetPhi_BeforeMt->Clone();
  DYFinal_MetPhi_BeforeMt->Add(DYlow_MetPhi_BeforeMt);
  
  TH1F* TTFinal_MetPhi_BeforeMt = (TH1F*) TTToHadronic_MetPhi_BeforeMt->Clone();
  TTFinal_MetPhi_BeforeMt->Add(TTTo2L2Nu_MetPhi_BeforeMt);
  TTFinal_MetPhi_BeforeMt->Add(TTToSemiLeptonic_MetPhi_BeforeMt);
  
  TH1F* VVFinal_MetPhi_BeforeMt = (TH1F*) WW4Q_MetPhi_BeforeMt->Clone();
  VVFinal_MetPhi_BeforeMt->Add(WWLNuQQ_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(WZ2L2Q_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(WZ1L3Nu_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(WZ3LNu_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(WZ1L1Nu2Q_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(ZZ4L_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(ZZ2L2Nu_MetPhi_BeforeMt);
  VVFinal_MetPhi_BeforeMt->Add(ZZ2L2Q_MetPhi_BeforeMt);
  
  TH1F* STFinal_MetPhi_BeforeMt = (TH1F*) ST_t_antitop_MetPhi_BeforeMt->Clone();
  STFinal_MetPhi_BeforeMt->Add(ST_t_top_MetPhi_BeforeMt);
  STFinal_MetPhi_BeforeMt->Add(ST_tW_antitop_MetPhi_BeforeMt);
  STFinal_MetPhi_BeforeMt->Add(ST_tW_top_MetPhi_BeforeMt);

  TH1F* VHFinal_MetPhi_BeforeMt = (TH1F*) WplusH125_MetPhi_BeforeMt->Clone();
  VHFinal_MetPhi_BeforeMt->Add(WminusH125_MetPhi_BeforeMt);
  VHFinal_MetPhi_BeforeMt->Add(ZH125_MetPhi_BeforeMt);

  TH1F* EWKFinal_MetPhi_BeforeMt = (TH1F*) EWKZLL_MetPhi_BeforeMt->Clone();
  EWKFinal_MetPhi_BeforeMt->Add(EWKZNuNu_MetPhi_BeforeMt);

  data_obs_MetPhi_BeforeMt->SetMarkerStyle(20);
  data_obs_MetPhi_BeforeMt->Sumw2();
  
  data_obs_Fake_MetPhi_BeforeMt->SetFillColor(kRed);
  data_obs_Fake_MetPhi_BeforeMt->SetLineColor(kBlack);

  embedded_MetPhi_BeforeMt->SetFillColor(kYellow);
  embedded_MetPhi_BeforeMt->SetLineColor(kBlack);

  DYFinal_MetPhi_BeforeMt->SetFillColor(kBlue);
  DYFinal_MetPhi_BeforeMt->SetLineColor(kBlack);

  TTFinal_MetPhi_BeforeMt->SetFillColor(kViolet-3);
  TTFinal_MetPhi_BeforeMt->SetLineColor(kBlack);

  VVFinal_MetPhi_BeforeMt->SetFillColor(kPink-3);
  VVFinal_MetPhi_BeforeMt->SetLineColor(kBlack);

  STFinal_MetPhi_BeforeMt->SetFillColor(kGreen);
  STFinal_MetPhi_BeforeMt->SetLineColor(kBlack);

  qqH_htt125_MetPhi_BeforeMt->SetFillColor(kCyan);
  qqH_htt125_MetPhi_BeforeMt->SetLineColor(kBlack);

  ggH_htt125_MetPhi_BeforeMt->SetFillColor(kCyan);
  ggH_htt125_MetPhi_BeforeMt->SetLineColor(kBlack);

  VHFinal_MetPhi_BeforeMt->SetFillColor(kOrange);
  VHFinal_MetPhi_BeforeMt->SetLineColor(kBlack);

  EWKFinal_MetPhi_BeforeMt->SetFillColor(kBlue-2);
  EWKFinal_MetPhi_BeforeMt->SetLineColor(kBlack);
  
  THStack* BackgroundStack_MetPhi_BeforeMt = new THStack("BackgroundStack_MetPhi_BeforeMt","BackgroundStack_MetPhi_BeforeMt");
  BackgroundStack_MetPhi_BeforeMt->Add(data_obs_Fake_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(DYFinal_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(embedded_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(TTFinal_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(VVFinal_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(STFinal_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(qqH_htt125_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(ggH_htt125_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(VHFinal_MetPhi_BeforeMt,"hist");
  BackgroundStack_MetPhi_BeforeMt->Add(EWKFinal_MetPhi_BeforeMt,"hist");

  TH1F* BackgroundStack_MetPhi_BeforeMt_Errors = MakeStackErrors(BackgroundStack_MetPhi_BeforeMt);

  TPad* PlotPad_MetPhi_BeforeMt = MakeRatioPlot(CanvasOne, BackgroundStack_MetPhi_BeforeMt, data_obs_MetPhi_BeforeMt,"metphi");

  BackgroundStack_MetPhi_BeforeMt->SetMaximum(max(BackgroundStack_MetPhi_BeforeMt->GetMaximum(),data_obs_MetPhi_BeforeMt->GetMaximum()));

  BackgroundStack_MetPhi_BeforeMt->Draw();
  BackgroundStack_MetPhi_BeforeMt_Errors->Draw("SAME e2");
  BackgroundStack_MetPhi_BeforeMt->SetTitle("metphi (no m_{t} cut)");
  data_obs_MetPhi_BeforeMt->Draw("SAME e1");
  BackgroundStack_MetPhi_BeforeMt->GetYaxis()->SetTitle("Events");
  BackgroundStack_MetPhi_BeforeMt->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_MetPhi_BeforeMt,0,33);

  TLegend* Legend_MetPhi_BeforeMt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_MetPhi_BeforeMt->AddEntry(embedded_MetPhi_BeforeMt,"embedded","f");
  Legend_MetPhi_BeforeMt->AddEntry(DYFinal_MetPhi_BeforeMt, "Other DY","f");
  Legend_MetPhi_BeforeMt->AddEntry(TTFinal_MetPhi_BeforeMt,"t#bar{t}","f");
  Legend_MetPhi_BeforeMt->AddEntry(VVFinal_MetPhi_BeforeMt,"Dibsoson","f");
  Legend_MetPhi_BeforeMt->AddEntry(STFinal_MetPhi_BeforeMt,"Single Top","f");
  Legend_MetPhi_BeforeMt->AddEntry(qqH_htt125_MetPhi_BeforeMt,"qqh","f");
  Legend_MetPhi_BeforeMt->AddEntry(ggH_htt125_MetPhi_BeforeMt,"ggH","f");
  Legend_MetPhi_BeforeMt->AddEntry(VHFinal_MetPhi_BeforeMt,"VH","f");
  Legend_MetPhi_BeforeMt->AddEntry(EWKFinal_MetPhi_BeforeMt,"EWK","f");
  Legend_MetPhi_BeforeMt->AddEntry(data_obs_Fake_MetPhi_BeforeMt,"Fakes","f");

  Legend_MetPhi_BeforeMt->Draw();

  CanvasOne->SaveAs("metphi.png");

  //phi 1
  TCanvas* CanvasTwo = new TCanvas("CanvasTwo","Phi_1_BeforeMt",550,550);
  CanvasTwo->SetTickx();
  CanvasTwo->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("data_obs_Phi_1_BeforeMt");
  TH1F* data_obs_Fake_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("data_obs_Fake_Phi_1_BeforeMt");
  TH1F* embedded_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("embedded_Phi_1_BeforeMt");
  TH1F* DY_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("DY_Phi_1_BeforeMt");
  TH1F* DYlow_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("DYlow_Phi_1_BeforeMt");
  TH1F* TTToHadronic_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("TTToHadronic_Phi_1_BeforeMt");
  TH1F* TTTo2L2Nu_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("TTTo2L2Nu_Phi_1_BeforeMt");
  TH1F* TTToSemiLeptonic_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_Phi_1_BeforeMt");
  TH1F* WW4Q_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WW4Q_Phi_1_BeforeMt");
  TH1F* WWLNuQQ_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WWLNuQQ_Phi_1_BeforeMt");
  TH1F* WZ2L2Q_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WZ2L2Q_Phi_1_BeforeMt");
  TH1F* WZ1L3Nu_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WZ1L3Nu_Phi_1_BeforeMt");
  TH1F* WZ3LNu_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WZ3LNu_Phi_1_BeforeMt");
  TH1F* WZ1L1Nu2Q_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_Phi_1_BeforeMt");
  TH1F* ZZ4L_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ZZ4L_Phi_1_BeforeMt");
  TH1F* ZZ2L2Nu_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Nu_Phi_1_BeforeMt");
  TH1F* ZZ2L2Q_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Q_Phi_1_BeforeMt");
  TH1F* ST_t_antitop_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ST_t_antitop_Phi_1_BeforeMt");
  TH1F* ST_t_top_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ST_t_top_Phi_1_BeforeMt");
  TH1F* ST_tW_antitop_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_antitop_Phi_1_BeforeMt");
  TH1F* ST_tW_top_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_top_Phi_1_BeforeMt");
  TH1F* ggH_htt125_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ggH_htt125_Phi_1_BeforeMt");
  TH1F* qqH_htt125_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("qqH_htt125_Phi_1_BeforeMt");  
  TH1F* WplusH125_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WplusH125_Phi_1_BeforeMt");
  TH1F* WminusH125_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("WminusH125_Phi_1_BeforeMt");
  TH1F* ZH125_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("ZH125_Phi_1_BeforeMt");
  TH1F* EWKZLL_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("EWKZLL_Phi_1_BeforeMt");
  TH1F* EWKZNuNu_Phi_1_BeforeMt = (TH1F*) HistoFile->Get("EWKZNuNu_Phi_1_BeforeMt");

  TH1F* DYFinal_Phi_1_BeforeMt = (TH1F*) DY_Phi_1_BeforeMt->Clone();
  DYFinal_Phi_1_BeforeMt->Add(DYlow_Phi_1_BeforeMt);
  
  TH1F* TTFinal_Phi_1_BeforeMt = (TH1F*) TTToHadronic_Phi_1_BeforeMt->Clone();
  TTFinal_Phi_1_BeforeMt->Add(TTTo2L2Nu_Phi_1_BeforeMt);
  TTFinal_Phi_1_BeforeMt->Add(TTToSemiLeptonic_Phi_1_BeforeMt);
  
  TH1F* VVFinal_Phi_1_BeforeMt = (TH1F*) WW4Q_Phi_1_BeforeMt->Clone();
  VVFinal_Phi_1_BeforeMt->Add(WWLNuQQ_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(WZ2L2Q_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(WZ1L3Nu_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(WZ3LNu_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(WZ1L1Nu2Q_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(ZZ4L_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(ZZ2L2Nu_Phi_1_BeforeMt);
  VVFinal_Phi_1_BeforeMt->Add(ZZ2L2Q_Phi_1_BeforeMt);
  
  TH1F* STFinal_Phi_1_BeforeMt = (TH1F*) ST_t_antitop_Phi_1_BeforeMt->Clone();
  STFinal_Phi_1_BeforeMt->Add(ST_t_top_Phi_1_BeforeMt);
  STFinal_Phi_1_BeforeMt->Add(ST_tW_antitop_Phi_1_BeforeMt);
  STFinal_Phi_1_BeforeMt->Add(ST_tW_top_Phi_1_BeforeMt);

  TH1F* VHFinal_Phi_1_BeforeMt = (TH1F*) WplusH125_Phi_1_BeforeMt->Clone();
  VHFinal_Phi_1_BeforeMt->Add(WminusH125_Phi_1_BeforeMt);
  VHFinal_Phi_1_BeforeMt->Add(ZH125_Phi_1_BeforeMt);

  TH1F* EWKFinal_Phi_1_BeforeMt = (TH1F*) EWKZLL_Phi_1_BeforeMt->Clone();
  EWKFinal_Phi_1_BeforeMt->Add(EWKZNuNu_Phi_1_BeforeMt);

  data_obs_Phi_1_BeforeMt->SetMarkerStyle(20);
  data_obs_Phi_1_BeforeMt->Sumw2();
  
  data_obs_Fake_Phi_1_BeforeMt->SetFillColor(kRed);
  data_obs_Fake_Phi_1_BeforeMt->SetLineColor(kBlack);

  embedded_Phi_1_BeforeMt->SetFillColor(kYellow);
  embedded_Phi_1_BeforeMt->SetLineColor(kBlack);

  DYFinal_Phi_1_BeforeMt->SetFillColor(kBlue);
  DYFinal_Phi_1_BeforeMt->SetLineColor(kBlack);

  TTFinal_Phi_1_BeforeMt->SetFillColor(kViolet-3);
  TTFinal_Phi_1_BeforeMt->SetLineColor(kBlack);

  VVFinal_Phi_1_BeforeMt->SetFillColor(kPink-3);
  VVFinal_Phi_1_BeforeMt->SetLineColor(kBlack);

  STFinal_Phi_1_BeforeMt->SetFillColor(kGreen);
  STFinal_Phi_1_BeforeMt->SetLineColor(kBlack);

  qqH_htt125_Phi_1_BeforeMt->SetFillColor(kCyan);
  qqH_htt125_Phi_1_BeforeMt->SetLineColor(kBlack);

  ggH_htt125_Phi_1_BeforeMt->SetFillColor(kCyan);
  ggH_htt125_Phi_1_BeforeMt->SetLineColor(kBlack);

  VHFinal_Phi_1_BeforeMt->SetFillColor(kOrange);
  VHFinal_Phi_1_BeforeMt->SetLineColor(kBlack);

  EWKFinal_Phi_1_BeforeMt->SetFillColor(kBlue-2);
  EWKFinal_Phi_1_BeforeMt->SetLineColor(kBlack);
  
  THStack* BackgroundStack_Phi_1_BeforeMt = new THStack("BackgroundStack_Phi_1_BeforeMt","BackgroundStack_Phi_1_BeforeMt");
  BackgroundStack_Phi_1_BeforeMt->Add(data_obs_Fake_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(DYFinal_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(embedded_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(TTFinal_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(VVFinal_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(STFinal_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(qqH_htt125_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(ggH_htt125_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(VHFinal_Phi_1_BeforeMt,"hist");
  BackgroundStack_Phi_1_BeforeMt->Add(EWKFinal_Phi_1_BeforeMt,"hist");

  TH1F* BackgroundStack_Phi_1_BeforeMt_Errors = MakeStackErrors(BackgroundStack_Phi_1_BeforeMt);

  TPad* PlotPad_Phi_1_BeforeMt = MakeRatioPlot(CanvasTwo, BackgroundStack_Phi_1_BeforeMt, data_obs_Phi_1_BeforeMt,"#phi_{1}");

  BackgroundStack_Phi_1_BeforeMt->SetMaximum(max(BackgroundStack_Phi_1_BeforeMt->GetMaximum(),data_obs_Phi_1_BeforeMt->GetMaximum()));

  BackgroundStack_Phi_1_BeforeMt->Draw();
  BackgroundStack_Phi_1_BeforeMt_Errors->Draw("SAME e2");
  BackgroundStack_Phi_1_BeforeMt->SetTitle("#phi_{1} (no m_{t} cut)");
  data_obs_Phi_1_BeforeMt->Draw("SAME e1");
  BackgroundStack_Phi_1_BeforeMt->GetYaxis()->SetTitle("Events");
  BackgroundStack_Phi_1_BeforeMt->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_Phi_1_BeforeMt,0,33);

  TLegend* Legend_Phi_1_BeforeMt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_Phi_1_BeforeMt->AddEntry(embedded_Phi_1_BeforeMt,"embedded","f");
  Legend_Phi_1_BeforeMt->AddEntry(DYFinal_Phi_1_BeforeMt, "Other DY","f");
  Legend_Phi_1_BeforeMt->AddEntry(TTFinal_Phi_1_BeforeMt,"t#bar{t}","f");
  Legend_Phi_1_BeforeMt->AddEntry(VVFinal_Phi_1_BeforeMt,"Dibsoson","f");
  Legend_Phi_1_BeforeMt->AddEntry(STFinal_Phi_1_BeforeMt,"Single Top","f");
  Legend_Phi_1_BeforeMt->AddEntry(qqH_htt125_Phi_1_BeforeMt,"qqh","f");
  Legend_Phi_1_BeforeMt->AddEntry(ggH_htt125_Phi_1_BeforeMt,"ggH","f");
  Legend_Phi_1_BeforeMt->AddEntry(VHFinal_Phi_1_BeforeMt,"VH","f");
  Legend_Phi_1_BeforeMt->AddEntry(EWKFinal_Phi_1_BeforeMt,"EWK","f");
  Legend_Phi_1_BeforeMt->AddEntry(data_obs_Fake_Phi_1_BeforeMt,"Fakes","f");

  Legend_Phi_1_BeforeMt->Draw();

  CanvasTwo->SaveAs("phione.png");

  //phi 2
  TCanvas* CanvasThree = new TCanvas("CanvasThree","Phi_2_BeforeMt",550,550);
  CanvasThree->SetTickx();
  CanvasThree->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* data_obs_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("data_obs_Phi_2_BeforeMt");
  TH1F* data_obs_Fake_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("data_obs_Fake_Phi_2_BeforeMt");
  TH1F* embedded_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("embedded_Phi_2_BeforeMt");
  TH1F* DY_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("DY_Phi_2_BeforeMt");
  TH1F* DYlow_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("DYlow_Phi_2_BeforeMt");
  TH1F* TTToHadronic_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("TTToHadronic_Phi_2_BeforeMt");
  TH1F* TTTo2L2Nu_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("TTTo2L2Nu_Phi_2_BeforeMt");
  TH1F* TTToSemiLeptonic_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_Phi_2_BeforeMt");
  TH1F* WW4Q_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WW4Q_Phi_2_BeforeMt");
  TH1F* WWLNuQQ_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WWLNuQQ_Phi_2_BeforeMt");
  TH1F* WZ2L2Q_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WZ2L2Q_Phi_2_BeforeMt");
  TH1F* WZ1L3Nu_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WZ1L3Nu_Phi_2_BeforeMt");
  TH1F* WZ3LNu_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WZ3LNu_Phi_2_BeforeMt");
  TH1F* WZ1L1Nu2Q_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WZ1L1Nu2Q_Phi_2_BeforeMt");
  TH1F* ZZ4L_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ZZ4L_Phi_2_BeforeMt");
  TH1F* ZZ2L2Nu_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Nu_Phi_2_BeforeMt");
  TH1F* ZZ2L2Q_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ZZ2L2Q_Phi_2_BeforeMt");
  TH1F* ST_t_antitop_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ST_t_antitop_Phi_2_BeforeMt");
  TH1F* ST_t_top_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ST_t_top_Phi_2_BeforeMt");
  TH1F* ST_tW_antitop_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_antitop_Phi_2_BeforeMt");
  TH1F* ST_tW_top_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ST_tW_top_Phi_2_BeforeMt");
  TH1F* ggH_htt125_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ggH_htt125_Phi_2_BeforeMt");
  TH1F* qqH_htt125_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("qqH_htt125_Phi_2_BeforeMt");  
  TH1F* WplusH125_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WplusH125_Phi_2_BeforeMt");
  TH1F* WminusH125_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("WminusH125_Phi_2_BeforeMt");
  TH1F* ZH125_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("ZH125_Phi_2_BeforeMt");
  TH1F* EWKZLL_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("EWKZLL_Phi_2_BeforeMt");
  TH1F* EWKZNuNu_Phi_2_BeforeMt = (TH1F*) HistoFile->Get("EWKZNuNu_Phi_2_BeforeMt");

  TH1F* DYFinal_Phi_2_BeforeMt = (TH1F*) DY_Phi_2_BeforeMt->Clone();
  DYFinal_Phi_2_BeforeMt->Add(DYlow_Phi_2_BeforeMt);
  
  TH1F* TTFinal_Phi_2_BeforeMt = (TH1F*) TTToHadronic_Phi_2_BeforeMt->Clone();
  TTFinal_Phi_2_BeforeMt->Add(TTTo2L2Nu_Phi_2_BeforeMt);
  TTFinal_Phi_2_BeforeMt->Add(TTToSemiLeptonic_Phi_2_BeforeMt);
  
  TH1F* VVFinal_Phi_2_BeforeMt = (TH1F*) WW4Q_Phi_2_BeforeMt->Clone();
  VVFinal_Phi_2_BeforeMt->Add(WWLNuQQ_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(WZ2L2Q_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(WZ1L3Nu_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(WZ3LNu_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(WZ1L1Nu2Q_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(ZZ4L_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(ZZ2L2Nu_Phi_2_BeforeMt);
  VVFinal_Phi_2_BeforeMt->Add(ZZ2L2Q_Phi_2_BeforeMt);
  
  TH1F* STFinal_Phi_2_BeforeMt = (TH1F*) ST_t_antitop_Phi_2_BeforeMt->Clone();
  STFinal_Phi_2_BeforeMt->Add(ST_t_top_Phi_2_BeforeMt);
  STFinal_Phi_2_BeforeMt->Add(ST_tW_antitop_Phi_2_BeforeMt);
  STFinal_Phi_2_BeforeMt->Add(ST_tW_top_Phi_2_BeforeMt);

  TH1F* VHFinal_Phi_2_BeforeMt = (TH1F*) WplusH125_Phi_2_BeforeMt->Clone();
  VHFinal_Phi_2_BeforeMt->Add(WminusH125_Phi_2_BeforeMt);
  VHFinal_Phi_2_BeforeMt->Add(ZH125_Phi_2_BeforeMt);

  TH1F* EWKFinal_Phi_2_BeforeMt = (TH1F*) EWKZLL_Phi_2_BeforeMt->Clone();
  EWKFinal_Phi_2_BeforeMt->Add(EWKZNuNu_Phi_2_BeforeMt);

  data_obs_Phi_2_BeforeMt->SetMarkerStyle(20);
  data_obs_Phi_2_BeforeMt->Sumw2();
  
  data_obs_Fake_Phi_2_BeforeMt->SetFillColor(kRed);
  data_obs_Fake_Phi_2_BeforeMt->SetLineColor(kBlack);

  embedded_Phi_2_BeforeMt->SetFillColor(kYellow);
  embedded_Phi_2_BeforeMt->SetLineColor(kBlack);

  DYFinal_Phi_2_BeforeMt->SetFillColor(kBlue);
  DYFinal_Phi_2_BeforeMt->SetLineColor(kBlack);

  TTFinal_Phi_2_BeforeMt->SetFillColor(kViolet-3);
  TTFinal_Phi_2_BeforeMt->SetLineColor(kBlack);

  VVFinal_Phi_2_BeforeMt->SetFillColor(kPink-3);
  VVFinal_Phi_2_BeforeMt->SetLineColor(kBlack);

  STFinal_Phi_2_BeforeMt->SetFillColor(kGreen);
  STFinal_Phi_2_BeforeMt->SetLineColor(kBlack);

  qqH_htt125_Phi_2_BeforeMt->SetFillColor(kCyan);
  qqH_htt125_Phi_2_BeforeMt->SetLineColor(kBlack);

  ggH_htt125_Phi_2_BeforeMt->SetFillColor(kCyan);
  ggH_htt125_Phi_2_BeforeMt->SetLineColor(kBlack);

  VHFinal_Phi_2_BeforeMt->SetFillColor(kOrange);
  VHFinal_Phi_2_BeforeMt->SetLineColor(kBlack);

  EWKFinal_Phi_2_BeforeMt->SetFillColor(kBlue-2);
  EWKFinal_Phi_2_BeforeMt->SetLineColor(kBlack);
  
  THStack* BackgroundStack_Phi_2_BeforeMt = new THStack("BackgroundStack_Phi_2_BeforeMt","BackgroundStack_Phi_2_BeforeMt");
  BackgroundStack_Phi_2_BeforeMt->Add(data_obs_Fake_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(DYFinal_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(embedded_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(TTFinal_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(VVFinal_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(STFinal_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(qqH_htt125_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(ggH_htt125_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(VHFinal_Phi_2_BeforeMt,"hist");
  BackgroundStack_Phi_2_BeforeMt->Add(EWKFinal_Phi_2_BeforeMt,"hist");

  TH1F* BackgroundStack_Phi_2_BeforeMt_Errors = MakeStackErrors(BackgroundStack_Phi_2_BeforeMt);

  TPad* PlotPad_Phi_2_BeforeMt = MakeRatioPlot(CanvasThree, BackgroundStack_Phi_2_BeforeMt, data_obs_Phi_2_BeforeMt,"#phi_{2}");

  BackgroundStack_Phi_2_BeforeMt->SetMaximum(max(BackgroundStack_Phi_2_BeforeMt->GetMaximum(),data_obs_Phi_2_BeforeMt->GetMaximum()));

  BackgroundStack_Phi_2_BeforeMt->Draw();
  BackgroundStack_Phi_2_BeforeMt_Errors->Draw("SAME e2");
  BackgroundStack_Phi_2_BeforeMt->SetTitle("#phi_{2} (no m_{t} cut)");
  data_obs_Phi_2_BeforeMt->Draw("SAME e1");
  BackgroundStack_Phi_2_BeforeMt->GetYaxis()->SetTitle("Events");
  BackgroundStack_Phi_2_BeforeMt->GetYaxis()->SetTitleOffset(1.58);

  CMS_lumi(PlotPad_Phi_2_BeforeMt,0,33);

  TLegend* Legend_Phi_2_BeforeMt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_Phi_2_BeforeMt->AddEntry(embedded_Phi_2_BeforeMt,"embedded","f");
  Legend_Phi_2_BeforeMt->AddEntry(DYFinal_Phi_2_BeforeMt, "Other DY","f");
  Legend_Phi_2_BeforeMt->AddEntry(TTFinal_Phi_2_BeforeMt,"t#bar{t}","f");
  Legend_Phi_2_BeforeMt->AddEntry(VVFinal_Phi_2_BeforeMt,"Dibsoson","f");
  Legend_Phi_2_BeforeMt->AddEntry(STFinal_Phi_2_BeforeMt,"Single Top","f");
  Legend_Phi_2_BeforeMt->AddEntry(qqH_htt125_Phi_2_BeforeMt,"qqh","f");
  Legend_Phi_2_BeforeMt->AddEntry(ggH_htt125_Phi_2_BeforeMt,"ggH","f");
  Legend_Phi_2_BeforeMt->AddEntry(VHFinal_Phi_2_BeforeMt,"VH","f");
  Legend_Phi_2_BeforeMt->AddEntry(EWKFinal_Phi_2_BeforeMt,"EWK","f");
  Legend_Phi_2_BeforeMt->AddEntry(data_obs_Fake_Phi_2_BeforeMt,"Fakes","f");

  Legend_Phi_2_BeforeMt->Draw();
  CanvasThree->SaveAs("phitwo.png");
}
