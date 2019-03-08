#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"

void DrawCombinePlots()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  //Color Corrections
  TColor* DYColor = new TColor((4.0*16.0+4.0)/256.0,(9.0*16.0+6.0)/256.0,(12.0*16.0+8.0)/256.0);
  TColor* OtherColor = new TColor((16.0+2.0)/256.0,(12.0*16.0+10.0)/256.0,(13.0*16.0+13.0)/256.0);

  TLatex latex;
  int numCategories;

  TFile* HistoFile = new TFile("HistoFile.root","READ");

  //ZeroJet
  TCanvas* CanvasOne = new TCanvas("CanvasOne","ZeroJet",550,550);
  CanvasOne->SetTickx();
  CanvasOne->SetTicky();

  gStyle->SetOptStat(0);
  TDirectory* ZeroJetDir = (TDirectory*) HistoFile->Get("ZeroJet");
  TH1F* ZeroJet_Data = (TH1F*) ZeroJetDir->Get("data_obs");
  TH1F* ZeroJet_Fakes = (TH1F*) ZeroJetDir->Get("jetFakes");
  TH1F* ZeroJet_Embedded = (TH1F*) ZeroJetDir->Get("embedded");
  TH1F* ZeroJet_ZMM = (TH1F*) ZeroJetDir->Get("ZL");
  TH1F* ZeroJet_TT = (TH1F*) ZeroJetDir->Get("TTL");
  TH1F* ZeroJet_Other = (TH1F*) ZeroJetDir->Get("Other");
  TH1F* ZeroJet_Higgs_Upscale = (TH1F*) ZeroJetDir->Get("Higgs_Upscale");

  //Color Corections
  ZeroJet_ZMM->SetFillColor(DYColor->GetNumber());
  ZeroJet_Other->SetFillColor(OtherColor->GetNumber());

  THStack* ZeroJetStack = new THStack("ZeroJetStack","ZeroJetStack");
  ZeroJetStack->Add(ZeroJet_Fakes,"HIST");
  ZeroJetStack->Add(ZeroJet_TT,"HIST");
  ZeroJetStack->Add(ZeroJet_ZMM,"HIST");
  ZeroJetStack->Add(ZeroJet_Other,"HIST");
  ZeroJetStack->Add(ZeroJet_Embedded,"HIST");

  TH1F* ZeroJet_Errors = MakeStackErrors(ZeroJetStack);
  
  TPad* ZeroJet_PlotPad = MakeRatioPlot(CanvasOne,ZeroJetStack,ZeroJet_Data,"m_{vis}",0.7,1.3);
  ZeroJet_PlotPad->SetTickx();
  ZeroJet_PlotPad->SetTicky();
  ZeroJet_PlotPad->SetGridx();
  
  ZeroJetStack->SetMaximum(max(ZeroJetStack->GetMaximum(),ZeroJet_Data->GetMaximum())*1.1);
  
  ZeroJetStack->Draw();
  ZeroJet_Errors->Draw("SAME e2");
  ZeroJetStack->SetTitle("0 Jet");
  ZeroJet_Data->Draw("SAME e1");
  ZeroJet_Higgs_Upscale->Draw("SAME HIST");
  ZeroJetStack->GetYaxis()->SetTitle("Events");
  ZeroJetStack->GetYaxis()->SetTitleOffset(1.58);
  ZeroJetStack->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(ZeroJet_PlotPad,0,33);
  
  TLegend* ZeroJetLegend = new TLegend(0.9,0.6,1.0,0.9);
  ZeroJetLegend->AddEntry(ZeroJet_Data,"Observed","pe");
  ZeroJetLegend->AddEntry(ZeroJet_Embedded,"DY #rightarrow #tau#tau","f");
  ZeroJetLegend->AddEntry(ZeroJet_Other,"Other","f");
  ZeroJetLegend->AddEntry(ZeroJet_ZMM,"DY #rightarrow ll","f");
  ZeroJetLegend->AddEntry(ZeroJet_TT,"t#bar{t}","f");
  ZeroJetLegend->AddEntry(ZeroJet_Fakes,"Fakes","f");
  ZeroJetLegend->AddEntry(ZeroJet_Higgs_Upscale,"All Higgs (#times 30)","l");
  ZeroJetLegend->Draw();

  numCategories = 4;
  TH1F* ZeroJetGridDivision = new TH1F("ZeroJetGrid","ZeroJetGrid",
				 ZeroJet_Higgs_Upscale->GetNbinsX(),
				 ZeroJet_Higgs_Upscale->GetXaxis()->GetXmin(),
				 ZeroJet_Higgs_Upscale->GetXaxis()->GetXmax());
  ZeroJetStack->GetXaxis()->SetNdivisions(-500-numCategories);
  ZeroJetGridDivision->GetXaxis()->SetNdivisions(-500-numCategories);
  ZeroJetGridDivision->Draw("SAME");
  
  latex.SetTextSize(0.025);
  latex.SetTextAlign(13);
  latex.DrawLatex(2.0,13000.0,"30.0 #leq #tau_{p_{t}} #leq 35.0");
  latex.DrawLatex(22.0,13000.0,"35.0 #leq #tau_{p_{t}} #leq 40.0");
  latex.DrawLatex(42.0,13000.0,"40.0 #leq #tau_{p_{t}} #leq 50.0");
  latex.DrawLatex(62.0,10000.0,"50.0 #leq #tau_{p_{t}}");

  CanvasOne->Draw();

  //Boosted
  TCanvas* CanvasTwo = new TCanvas("CanvasTwo","Boosted",550,550);
  CanvasTwo->SetTickx();
  CanvasTwo->SetTicky();

  gStyle->SetOptStat(0);
  TDirectory* BoostedDir = (TDirectory*) HistoFile->Get("Boosted");
  TH1F* Boosted_Data = (TH1F*) BoostedDir->Get("data_obs");
  TH1F* Boosted_Fakes = (TH1F*) BoostedDir->Get("jetFakes");
  TH1F* Boosted_Embedded = (TH1F*) BoostedDir->Get("embedded");
  TH1F* Boosted_ZMM = (TH1F*) BoostedDir->Get("ZL");
  TH1F* Boosted_TT = (TH1F*) BoostedDir->Get("TTL");
  TH1F* Boosted_Other = (TH1F*) BoostedDir->Get("Other");
  TH1F* Boosted_Higgs_Upscale = (TH1F*) BoostedDir->Get("Higgs_Upscale");

  //Color Corections
  Boosted_ZMM->SetFillColor(DYColor->GetNumber());
  Boosted_Other->SetFillColor(OtherColor->GetNumber());

  THStack* BoostedStack = new THStack("BoostedStack","BoostedStack");
  BoostedStack->Add(Boosted_Fakes,"HIST");
  BoostedStack->Add(Boosted_TT,"HIST");
  BoostedStack->Add(Boosted_ZMM,"HIST");
  BoostedStack->Add(Boosted_Other,"HIST");
  BoostedStack->Add(Boosted_Embedded,"HIST");

  TH1F* Boosted_Errors = MakeStackErrors(BoostedStack);
  
  TPad* Boosted_PlotPad = MakeRatioPlot(CanvasTwo,BoostedStack,Boosted_Data,"m_{vis}",0.7,1.3);
  Boosted_PlotPad->SetTickx();
  Boosted_PlotPad->SetTicky();
  Boosted_PlotPad->SetGridx();
  
  BoostedStack->SetMaximum(max(BoostedStack->GetMaximum(),Boosted_Data->GetMaximum())*1.1);
  
  BoostedStack->Draw();
  Boosted_Errors->Draw("SAME e2");
  BoostedStack->SetTitle("Boosted");
  Boosted_Data->Draw("SAME e1");
  Boosted_Higgs_Upscale->Draw("SAME HIST");
  BoostedStack->GetYaxis()->SetTitle("Events");
  BoostedStack->GetYaxis()->SetTitleOffset(1.58);
  BoostedStack->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(Boosted_PlotPad,0,33);
  
  TLegend* BoostedLegend = new TLegend(0.9,0.6,1.0,0.9);
  BoostedLegend->AddEntry(Boosted_Data,"Observed","pe");
  BoostedLegend->AddEntry(Boosted_Embedded,"DY #rightarrow #tau#tau","f");
  BoostedLegend->AddEntry(Boosted_Other,"Other","f");
  BoostedLegend->AddEntry(Boosted_ZMM,"DY #rightarrow ll","f");
  BoostedLegend->AddEntry(Boosted_TT,"t#bar{t}","f");
  BoostedLegend->AddEntry(Boosted_Fakes,"Fakes","f");
  BoostedLegend->AddEntry(Boosted_Higgs_Upscale,"All Higgs (#times 30)","l");
  BoostedLegend->Draw();

  numCategories = 5;
  TH1F* BoostedGridDivision = new TH1F("BoostedGrid","BoostedGrid",
				 Boosted_Higgs_Upscale->GetNbinsX(),
				 Boosted_Higgs_Upscale->GetXaxis()->GetXmin(),
				 Boosted_Higgs_Upscale->GetXaxis()->GetXmax());
  BoostedStack->GetXaxis()->SetNdivisions(-500-numCategories);
  BoostedGridDivision->GetXaxis()->SetNdivisions(-500-numCategories);
  BoostedGridDivision->Draw("SAME");

  latex.SetTextSize(0.017);
  latex.SetTextAlign(13);
  latex.DrawLatex(2.0,4500.0,"0.0 #leq H_{p_{t}} #leq 30.0");
  latex.DrawLatex(22.0,4500.0,"30.0 #leq H_{p_{t}} #leq 60.0");
  latex.DrawLatex(42.0,4500.0,"60.0 #leq H_{p_{t}} #leq 100.0");
  latex.DrawLatex(62.0,4500.0,"100.0 #leq H_{p_{t}} #leq 150.0");
  //latex.DrawLatex(82.0,6000.0,"250.0 #leq H_{p_{t}} #leq 300.0");
  latex.DrawLatex(102.0,3200.0,"150.0 #leq H_{p_{t}}");

  CanvasTwo->Draw();
  
  //VBF
  
  TCanvas* CanvasThree = new TCanvas("CanvasThree","VBF",550,550);
  CanvasThree->SetTickx();
  CanvasThree->SetTicky();

  gStyle->SetOptStat(0);
  TDirectory* VBFDir = (TDirectory*) HistoFile->Get("VBF");
  TH1F* VBF_Data = (TH1F*) VBFDir->Get("data_obs");
  TH1F* VBF_Fakes = (TH1F*) VBFDir->Get("jetFakes");
  TH1F* VBF_Embedded = (TH1F*) VBFDir->Get("embedded");
  TH1F* VBF_ZMM = (TH1F*) VBFDir->Get("ZL");
  TH1F* VBF_TT = (TH1F*) VBFDir->Get("TTL");
  TH1F* VBF_Other = (TH1F*) VBFDir->Get("Other");
  TH1F* VBF_Higgs_Upscale = (TH1F*) VBFDir->Get("Higgs_Upscale");

  //Color Corections
  VBF_ZMM->SetFillColor(DYColor->GetNumber());
  VBF_Other->SetFillColor(OtherColor->GetNumber());

  THStack* VBFStack = new THStack("VBFStack","VBFStack");
  VBFStack->Add(VBF_Fakes,"HIST");
  VBFStack->Add(VBF_TT,"HIST");
  VBFStack->Add(VBF_ZMM,"HIST");
  VBFStack->Add(VBF_Other,"HIST");
  VBFStack->Add(VBF_Embedded,"HIST");

  TH1F* VBF_Errors = MakeStackErrors(VBFStack);
  
  TPad* VBF_PlotPad = MakeRatioPlot(CanvasThree,VBFStack,VBF_Data,"m_{vis}",0.7,1.3);
  VBF_PlotPad->SetTickx();
  VBF_PlotPad->SetTicky();
  VBF_PlotPad->SetGridx();
  
  VBFStack->SetMaximum(max(VBFStack->GetMaximum(),VBF_Data->GetMaximum())*1.1);
  
  VBFStack->Draw();
  VBF_Errors->Draw("SAME e2");
  VBFStack->SetTitle("VBF");
  VBF_Data->Draw("SAME e1");
  VBF_Higgs_Upscale->Draw("SAME HIST");
  VBFStack->GetYaxis()->SetTitle("Events");
  VBFStack->GetYaxis()->SetTitleOffset(1.58);
  VBFStack->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(VBF_PlotPad,0,33);
  
  TLegend* VBFLegend = new TLegend(0.9,0.6,1.0,0.9);
  VBFLegend->AddEntry(VBF_Data,"Observed","pe");
  VBFLegend->AddEntry(VBF_Embedded,"DY #rightarrow #tau#tau","f");
  VBFLegend->AddEntry(VBF_Other,"Other","f");
  VBFLegend->AddEntry(VBF_ZMM,"DY #rightarrow ll","f");
  VBFLegend->AddEntry(VBF_TT,"t#bar{t}","f");
  VBFLegend->AddEntry(VBF_Fakes,"Fakes","f");
  VBFLegend->AddEntry(VBF_Higgs_Upscale,"All Higgs (#times 30)","l");
  VBFLegend->Draw();

  numCategories = 4;
  TH1F* VBFGridDivision = new TH1F("VBFGrid","VBFGrid",
				 VBF_Higgs_Upscale->GetNbinsX(),
				 VBF_Higgs_Upscale->GetXaxis()->GetXmin(),
				 VBF_Higgs_Upscale->GetXaxis()->GetXmax());
  VBFStack->GetXaxis()->SetNdivisions(-500-numCategories);
  VBFGridDivision->GetXaxis()->SetNdivisions(-500-numCategories);
  VBFGridDivision->Draw("SAME");

  latex.SetTextSize(0.017);
  latex.SetTextAlign(13);
  latex.DrawLatex(2.0,900.0,"0.0 #leq m_{jj} #leq 100.0");
  latex.DrawLatex(22.0,900.0,"100.0 #leq m_{jj} #leq 200.0");
  latex.DrawLatex(42.0,900.0,"200.0 #leq m_{jj} #leq 300.0");
  //latex.DrawLatex(62.0,1800.0,"1100.0 #leq m_{jj} #leq 1500.0");
  latex.DrawLatex(82.0,700.0,"300.0 #leq m_{jj}");

  CanvasThree->Draw();
  
}
