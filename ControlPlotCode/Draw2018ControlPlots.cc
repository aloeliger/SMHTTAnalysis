#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"

void Draw2018ControlPlots()
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "60 fb^{-1}, 13 TeV";
  
  TFile* HistoFile = new TFile("TemporaryFiles/ControlRegion_2018.root","READ");

  TCanvas* CanvasOne = new TCanvas("CanvasOne","MuPt",550,550);
  CanvasOne->SetTickx();
  CanvasOne->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_MuPt = (TH1F*) HistoFile->Get("Data_2018_MuPt");
  TH1F* Data_Fake_MuPt = (TH1F*) HistoFile->Get("Fake_2018_MuPt");
  TH1F* DYTT_MuPt = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_MuPt");
  TH1F* DYMM_MuPt = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_MuPt");
  TH1F* TTToHadronic_MuPt = (TH1F*) HistoFile->Get("TTToHadronic_2018_MuPt");
  TH1F* TTTo2L2Nu_MuPt = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_MuPt");
  TH1F* TTToSemiLeptonic_MuPt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_MuPt");  
  TH1F* WW_MuPt = (TH1F*) HistoFile->Get("WW_2018_MuPt");
  TH1F* WZ_MuPt = (TH1F*) HistoFile->Get("WZ_2018_MuPt");
  TH1F* ZZ_MuPt = (TH1F*) HistoFile->Get("ZZ_2018_MuPt");
  TH1F* ST_tW_top_MuPt = (TH1F*) HistoFile->Get("ST_tW_top_2018_MuPt");
  TH1F* ggH_MuPt = (TH1F*) HistoFile->Get("ggH_2018_MuPt");
  TH1F* VBF_MuPt = (TH1F*) HistoFile->Get("VBF_2018_MuPt");
  TH1F* WHPlus_MuPt = (TH1F*) HistoFile->Get("WHPlus_2018_MuPt");
  TH1F* WHMinus_MuPt = (TH1F*) HistoFile->Get("WHMinus_2018_MuPt");
  TH1F* ZH_MuPt = (TH1F*) HistoFile->Get("ZH_2018_MuPt");

  TH1F* TTFinal_MuPt = (TH1F*) TTToHadronic_MuPt->Clone();
  TTFinal_MuPt->Add(TTTo2L2Nu_MuPt);
  TTFinal_MuPt->Add(TTToSemiLeptonic_MuPt);

  TH1F* VVFinal_MuPt = (TH1F*) WW_MuPt->Clone();
  VVFinal_MuPt->Add(WZ_MuPt);
  VVFinal_MuPt->Add(ZZ_MuPt);
  VVFinal_MuPt->Add(ST_tW_top_MuPt);
  
  TH1F* VHFinal_MuPt = (TH1F*) WHPlus_MuPt->Clone();
  VHFinal_MuPt->Add(WHMinus_MuPt);
  VHFinal_MuPt->Add(ZH_MuPt);

  TH1F* Other_MuPt = (TH1F*) VHFinal_MuPt->Clone();
  Other_MuPt->Add(ggH_MuPt);
  Other_MuPt->Add(VBF_MuPt);
  Other_MuPt->Add(VVFinal_MuPt);

  TH1F* AllHiggs_MuPt = (TH1F*) VHFinal_MuPt->Clone();
  AllHiggs_MuPt->Add(ggH_MuPt);
  AllHiggs_MuPt->Add(VBF_MuPt);

  Data_MuPt->SetMarkerStyle(20);
  Data_MuPt->Sumw2();
  
  Data_Fake_MuPt->SetLineColor(kBlack);
  Data_Fake_MuPt->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_MuPt->SetLineColor(kBlack);
  DYTT_MuPt->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_MuPt->SetLineColor(kBlack);
  DYMM_MuPt->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_MuPt->SetLineColor(kBlack);
  TTFinal_MuPt->SetFillColor(TColor::GetColor("#9999cc"));

  Other_MuPt->SetLineColor(kBlack);
  Other_MuPt->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_MuPt->SetLineColor(kRed);
  AllHiggs_MuPt->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_MuPt->Integral()<<std::endl;

  THStack* BackgroundStack_MuPt = new THStack("BackgroundStack_MuPt","BackgroundStack_MuPt");  
  BackgroundStack_MuPt->Add(Data_Fake_MuPt,"hist");  
  BackgroundStack_MuPt->Add(TTFinal_MuPt,"hist");
  BackgroundStack_MuPt->Add(DYMM_MuPt,"hist");
  BackgroundStack_MuPt->Add(Other_MuPt,"hist");
  BackgroundStack_MuPt->Add(DYTT_MuPt,"hist");  

  TH1F* BackgroundStack_MuPt_Errors = MakeStackErrors(BackgroundStack_MuPt);

  TPad* PlotPad_MuPt = MakeRatioPlot(CanvasOne,BackgroundStack_MuPt, Data_MuPt, "#mu p_{t}",0.7,1.3);
  PlotPad_MuPt->SetTickx();
  PlotPad_MuPt->SetTicky();

  BackgroundStack_MuPt->SetMaximum(max(BackgroundStack_MuPt->GetMaximum(),Data_MuPt->GetMaximum()));
  
  BackgroundStack_MuPt->Draw();
  BackgroundStack_MuPt_Errors->Draw("SAME e2");
  BackgroundStack_MuPt->SetTitle("#mu p_{t}");
  Data_MuPt->Draw("SAME e1");
  AllHiggs_MuPt->Draw("SAME HIST");
  BackgroundStack_MuPt->GetYaxis()->SetTitle("Events");
  BackgroundStack_MuPt->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_MuPt->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_MuPt,0,33);

  TLegend* Legend_MuPt = new TLegend(0.61,0.41,0.88,0.68);        
  Legend_MuPt->AddEntry(Data_MuPt,"Observed","pe");
  Legend_MuPt->AddEntry(DYTT_MuPt,"Embedded","f");
  Legend_MuPt->AddEntry(Other_MuPt,"Other","f");  
  Legend_MuPt->AddEntry(DYMM_MuPt,"DY #rightarrow ll","f");  
  Legend_MuPt->AddEntry(TTFinal_MuPt,"t#bar{t}","f");  
  Legend_MuPt->AddEntry(Data_Fake_MuPt,"Fakes","f");
  Legend_MuPt->AddEntry(AllHiggs_MuPt,"All Higgs (#times 30)","l");

  Legend_MuPt->Draw();
  CanvasOne->SaveAs("FinalPlots/MuPt.png");
  CanvasOne->SaveAs("FinalPlots/MuPt.pdf");

  //MuEta
  TCanvas* CanvasTwo = new TCanvas("CanvasTwo","MuEta",550,550);
  CanvasTwo->SetTickx();
  CanvasTwo->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_MuEta = (TH1F*) HistoFile->Get("Data_2018_MuEta");
  TH1F* Data_Fake_MuEta = (TH1F*) HistoFile->Get("Fake_2018_MuEta");
  TH1F* DYTT_MuEta = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_MuEta");
  TH1F* DYMM_MuEta = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_MuEta");
  TH1F* TTToHadronic_MuEta = (TH1F*) HistoFile->Get("TTToHadronic_2018_MuEta");
  TH1F* TTTo2L2Nu_MuEta = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_MuEta");
  TH1F* TTToSemiLeptonic_MuEta = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_MuEta");  
  TH1F* WW_MuEta = (TH1F*) HistoFile->Get("WW_2018_MuEta");
  TH1F* WZ_MuEta = (TH1F*) HistoFile->Get("WZ_2018_MuEta");
  TH1F* ZZ_MuEta = (TH1F*) HistoFile->Get("ZZ_2018_MuEta");
  TH1F* ST_tW_top_MuEta = (TH1F*) HistoFile->Get("ST_tW_top_2018_MuEta");
  TH1F* ggH_MuEta = (TH1F*) HistoFile->Get("ggH_2018_MuEta");
  TH1F* VBF_MuEta = (TH1F*) HistoFile->Get("VBF_2018_MuEta");
  TH1F* WHPlus_MuEta = (TH1F*) HistoFile->Get("WHPlus_2018_MuEta");
  TH1F* WHMinus_MuEta = (TH1F*) HistoFile->Get("WHMinus_2018_MuEta");
  TH1F* ZH_MuEta = (TH1F*) HistoFile->Get("ZH_2018_MuEta");

  TH1F* TTFinal_MuEta = (TH1F*) TTToHadronic_MuEta->Clone();
  TTFinal_MuEta->Add(TTTo2L2Nu_MuEta);
  TTFinal_MuEta->Add(TTToSemiLeptonic_MuEta);

  TH1F* VVFinal_MuEta = (TH1F*) WW_MuEta->Clone();
  VVFinal_MuEta->Add(WZ_MuEta);
  VVFinal_MuEta->Add(ZZ_MuEta);
  VVFinal_MuEta->Add(ST_tW_top_MuEta);
  
  TH1F* VHFinal_MuEta = (TH1F*) WHPlus_MuEta->Clone();
  VHFinal_MuEta->Add(WHMinus_MuEta);
  VHFinal_MuEta->Add(ZH_MuEta);

  TH1F* Other_MuEta = (TH1F*) VHFinal_MuEta->Clone();
  Other_MuEta->Add(ggH_MuEta);
  Other_MuEta->Add(VBF_MuEta);
  Other_MuEta->Add(VVFinal_MuEta);

  TH1F* AllHiggs_MuEta = (TH1F*) VHFinal_MuEta->Clone();
  AllHiggs_MuEta->Add(ggH_MuEta);
  AllHiggs_MuEta->Add(VBF_MuEta);

  Data_MuEta->SetMarkerStyle(20);
  Data_MuEta->Sumw2();
  
  Data_Fake_MuEta->SetLineColor(kBlack);
  Data_Fake_MuEta->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_MuEta->SetLineColor(kBlack);
  DYTT_MuEta->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_MuEta->SetLineColor(kBlack);
  DYMM_MuEta->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_MuEta->SetLineColor(kBlack);
  TTFinal_MuEta->SetFillColor(TColor::GetColor("#9999cc"));

  Other_MuEta->SetLineColor(kBlack);
  Other_MuEta->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_MuEta->SetLineColor(kRed);
  AllHiggs_MuEta->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_MuEta->Integral()<<std::endl;

  THStack* BackgroundStack_MuEta = new THStack("BackgroundStack_MuEta","BackgroundStack_MuEta");  
  BackgroundStack_MuEta->Add(Data_Fake_MuEta,"hist");    
  BackgroundStack_MuEta->Add(TTFinal_MuEta,"hist");
  BackgroundStack_MuEta->Add(DYMM_MuEta,"hist");
  BackgroundStack_MuEta->Add(Other_MuEta,"hist");
  BackgroundStack_MuEta->Add(DYTT_MuEta,"hist");

  TH1F* BackgroundStack_MuEta_Errors = MakeStackErrors(BackgroundStack_MuEta);

  TPad* PlotPad_MuEta = MakeRatioPlot(CanvasTwo,BackgroundStack_MuEta, Data_MuEta, "#mu #eta",0.7,1.3);
  PlotPad_MuEta->SetTickx();
  PlotPad_MuEta->SetTicky();

  BackgroundStack_MuEta->SetMaximum(max(BackgroundStack_MuEta->GetMaximum(),Data_MuEta->GetMaximum()));
  
  BackgroundStack_MuEta->Draw();
  BackgroundStack_MuEta_Errors->Draw("SAME e2");
  BackgroundStack_MuEta->SetTitle("#mu #eta");
  Data_MuEta->Draw("SAME e1");
  AllHiggs_MuEta->Draw("SAME HIST");
  BackgroundStack_MuEta->GetYaxis()->SetTitle("Events");
  BackgroundStack_MuEta->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_MuEta->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_MuEta,0,33);

  TLegend* Legend_MuEta = new TLegend(0.1,0.70,0.30,0.9);      
  Legend_MuEta->AddEntry(Data_MuEta,"Observed","pe");
  Legend_MuEta->AddEntry(DYTT_MuEta,"Embedded","f");
  Legend_MuEta->AddEntry(Other_MuEta,"Other","f");
  Legend_MuEta->AddEntry(DYMM_MuEta,"DY #rightarrow ll","f");
  Legend_MuEta->AddEntry(TTFinal_MuEta,"t#bar{t}","f");
  Legend_MuEta->AddEntry(Data_Fake_MuEta,"Fakes","f");
  Legend_MuEta->AddEntry(AllHiggs_MuEta,"All Higgs (#times 30)","l");

  Legend_MuEta->Draw();
  CanvasTwo->SaveAs("FinalPlots/MuEta.png");
  CanvasTwo->SaveAs("FinalPlots/MuEta.pdf");

  //TauPt  
  TCanvas* CanvasThree = new TCanvas("CanvasThree","TauPt",550,550);
  CanvasThree->SetTickx();
  CanvasThree->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_TauPt = (TH1F*) HistoFile->Get("Data_2018_TauPt");
  TH1F* Data_Fake_TauPt = (TH1F*) HistoFile->Get("Fake_2018_TauPt");
  TH1F* DYTT_TauPt = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_TauPt");
  TH1F* DYMM_TauPt = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_TauPt");
  TH1F* TTToHadronic_TauPt = (TH1F*) HistoFile->Get("TTToHadronic_2018_TauPt");
  TH1F* TTTo2L2Nu_TauPt = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_TauPt");
  TH1F* TTToSemiLeptonic_TauPt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_TauPt");  
  TH1F* WW_TauPt = (TH1F*) HistoFile->Get("WW_2018_TauPt");
  TH1F* WZ_TauPt = (TH1F*) HistoFile->Get("WZ_2018_TauPt");
  TH1F* ZZ_TauPt = (TH1F*) HistoFile->Get("ZZ_2018_TauPt");
  TH1F* ST_tW_top_TauPt = (TH1F*) HistoFile->Get("ST_tW_top_2018_TauPt");
  TH1F* ggH_TauPt = (TH1F*) HistoFile->Get("ggH_2018_TauPt");
  TH1F* VBF_TauPt = (TH1F*) HistoFile->Get("VBF_2018_TauPt");
  TH1F* WHPlus_TauPt = (TH1F*) HistoFile->Get("WHPlus_2018_TauPt");
  TH1F* WHMinus_TauPt = (TH1F*) HistoFile->Get("WHMinus_2018_TauPt");
  TH1F* ZH_TauPt = (TH1F*) HistoFile->Get("ZH_2018_TauPt");

  TH1F* TTFinal_TauPt = (TH1F*) TTToHadronic_TauPt->Clone();
  TTFinal_TauPt->Add(TTTo2L2Nu_TauPt);
  TTFinal_TauPt->Add(TTToSemiLeptonic_TauPt);

  TH1F* VVFinal_TauPt = (TH1F*) WW_TauPt->Clone();
  VVFinal_TauPt->Add(WZ_TauPt);
  VVFinal_TauPt->Add(ZZ_TauPt);
  VVFinal_TauPt->Add(ST_tW_top_TauPt);
  
  TH1F* VHFinal_TauPt = (TH1F*) WHPlus_TauPt->Clone();
  VHFinal_TauPt->Add(WHMinus_TauPt);
  VHFinal_TauPt->Add(ZH_TauPt);

  TH1F* Other_TauPt = (TH1F*) VHFinal_TauPt->Clone();
  Other_TauPt->Add(ggH_TauPt);
  Other_TauPt->Add(VBF_TauPt);
  Other_TauPt->Add(VVFinal_TauPt);

  TH1F* AllHiggs_TauPt = (TH1F*) VHFinal_TauPt->Clone();
  AllHiggs_TauPt->Add(ggH_TauPt);
  AllHiggs_TauPt->Add(VBF_TauPt);

  Data_TauPt->SetMarkerStyle(20);
  Data_TauPt->Sumw2();
  
  Data_Fake_TauPt->SetLineColor(kBlack);
  Data_Fake_TauPt->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_TauPt->SetLineColor(kBlack);
  DYTT_TauPt->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_TauPt->SetLineColor(kBlack);
  DYMM_TauPt->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_TauPt->SetLineColor(kBlack);
  TTFinal_TauPt->SetFillColor(TColor::GetColor("#9999cc"));

  Other_TauPt->SetLineColor(kBlack);
  Other_TauPt->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_TauPt->SetLineColor(kRed);
  AllHiggs_TauPt->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_TauPt->Integral()<<std::endl;

  THStack* BackgroundStack_TauPt = new THStack("BackgroundStack_TauPt","BackgroundStack_TauPt");  
  BackgroundStack_TauPt->Add(Data_Fake_TauPt,"hist");  
  BackgroundStack_TauPt->Add(TTFinal_TauPt,"hist");
  BackgroundStack_TauPt->Add(DYMM_TauPt,"hist");  
  BackgroundStack_TauPt->Add(Other_TauPt,"hist");
  BackgroundStack_TauPt->Add(DYTT_TauPt,"hist");

  TH1F* BackgroundStack_TauPt_Errors = MakeStackErrors(BackgroundStack_TauPt);

  TPad* PlotPad_TauPt = MakeRatioPlot(CanvasThree,BackgroundStack_TauPt, Data_TauPt, "#tau p_{t}",0.7,1.3);
  PlotPad_TauPt->SetTickx();
  PlotPad_TauPt->SetTicky();

  BackgroundStack_TauPt->SetMaximum(max(BackgroundStack_TauPt->GetMaximum(),Data_TauPt->GetMaximum()));
  
  BackgroundStack_TauPt->Draw();
  BackgroundStack_TauPt_Errors->Draw("SAME e2");
  BackgroundStack_TauPt->SetTitle("#tau p_{t}");
  Data_TauPt->Draw("SAME e1");
  AllHiggs_TauPt->Draw("SAME HIST");
  BackgroundStack_TauPt->GetYaxis()->SetTitle("Events");
  BackgroundStack_TauPt->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_TauPt->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_TauPt,0,33);

  TLegend* Legend_TauPt = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_TauPt->AddEntry(Data_TauPt,"Observed","pe");
  Legend_TauPt->AddEntry(DYTT_TauPt,"Embedded","f");
  Legend_TauPt->AddEntry(Other_TauPt,"Other","f");
  Legend_TauPt->AddEntry(DYMM_TauPt,"DY #rightarrow ll","f");
  Legend_TauPt->AddEntry(TTFinal_TauPt,"t#bar{t}","f");
  Legend_TauPt->AddEntry(Data_Fake_TauPt,"Fakes","f");
  Legend_TauPt->AddEntry(AllHiggs_TauPt,"All Higgs (#times 30)","l");

  Legend_TauPt->Draw();
  CanvasThree->SaveAs("FinalPlots/TauPt.png");
  CanvasThree->SaveAs("FinalPlots/TauPt.pdf");

  //TauEta  
  TCanvas* CanvasFour = new TCanvas("CanvasFour","TauEta",550,550);
  CanvasFour->SetTickx();
  CanvasFour->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_TauEta = (TH1F*) HistoFile->Get("Data_2018_TauEta");
  TH1F* Data_Fake_TauEta = (TH1F*) HistoFile->Get("Fake_2018_TauEta");
  TH1F* DYTT_TauEta = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_TauEta");
  TH1F* DYMM_TauEta = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_TauEta");
  TH1F* TTToHadronic_TauEta = (TH1F*) HistoFile->Get("TTToHadronic_2018_TauEta");
  TH1F* TTTo2L2Nu_TauEta = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_TauEta");
  TH1F* TTToSemiLeptonic_TauEta = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_TauEta");  
  TH1F* WW_TauEta = (TH1F*) HistoFile->Get("WW_2018_TauEta");
  TH1F* WZ_TauEta = (TH1F*) HistoFile->Get("WZ_2018_TauEta");
  TH1F* ZZ_TauEta = (TH1F*) HistoFile->Get("ZZ_2018_TauEta");
  TH1F* ST_tW_top_TauEta = (TH1F*) HistoFile->Get("ST_tW_top_2018_TauEta");
  TH1F* ggH_TauEta = (TH1F*) HistoFile->Get("ggH_2018_TauEta");
  TH1F* VBF_TauEta = (TH1F*) HistoFile->Get("VBF_2018_TauEta");
  TH1F* WHPlus_TauEta = (TH1F*) HistoFile->Get("WHPlus_2018_TauEta");
  TH1F* WHMinus_TauEta = (TH1F*) HistoFile->Get("WHMinus_2018_TauEta");
  TH1F* ZH_TauEta = (TH1F*) HistoFile->Get("ZH_2018_TauEta");

  TH1F* TTFinal_TauEta = (TH1F*) TTToHadronic_TauEta->Clone();
  TTFinal_TauEta->Add(TTTo2L2Nu_TauEta);
  TTFinal_TauEta->Add(TTToSemiLeptonic_TauEta);

  TH1F* VVFinal_TauEta = (TH1F*) WW_TauEta->Clone();
  VVFinal_TauEta->Add(WZ_TauEta);
  VVFinal_TauEta->Add(ZZ_TauEta);
  VVFinal_TauEta->Add(ST_tW_top_TauEta);
  
  TH1F* VHFinal_TauEta = (TH1F*) WHPlus_TauEta->Clone();
  VHFinal_TauEta->Add(WHMinus_TauEta);
  VHFinal_TauEta->Add(ZH_TauEta);

  TH1F* Other_TauEta = (TH1F*) VHFinal_TauEta->Clone();
  Other_TauEta->Add(ggH_TauEta);
  Other_TauEta->Add(VBF_TauEta);
  Other_TauEta->Add(VVFinal_TauEta);

  TH1F* AllHiggs_TauEta = (TH1F*) VHFinal_TauEta->Clone();
  AllHiggs_TauEta->Add(ggH_TauEta);
  AllHiggs_TauEta->Add(VBF_TauEta);

  Data_TauEta->SetMarkerStyle(20);
  Data_TauEta->Sumw2();
  
  Data_Fake_TauEta->SetLineColor(kBlack);
  Data_Fake_TauEta->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_TauEta->SetLineColor(kBlack);
  DYTT_TauEta->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_TauEta->SetLineColor(kBlack);
  DYMM_TauEta->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_TauEta->SetLineColor(kBlack);
  TTFinal_TauEta->SetFillColor(TColor::GetColor("#9999cc"));

  Other_TauEta->SetLineColor(kBlack);
  Other_TauEta->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_TauEta->SetLineColor(kRed);
  AllHiggs_TauEta->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_TauEta->Integral()<<std::endl;

  THStack* BackgroundStack_TauEta = new THStack("BackgroundStack_TauEta","BackgroundStack_TauEta");  
  BackgroundStack_TauEta->Add(Data_Fake_TauEta,"hist");  
  BackgroundStack_TauEta->Add(TTFinal_TauEta,"hist");
  BackgroundStack_TauEta->Add(DYMM_TauEta,"hist");
  BackgroundStack_TauEta->Add(Other_TauEta,"hist");
  BackgroundStack_TauEta->Add(DYTT_TauEta,"hist");

  TH1F* BackgroundStack_TauEta_Errors = MakeStackErrors(BackgroundStack_TauEta);

  TPad* PlotPad_TauEta = MakeRatioPlot(CanvasFour,BackgroundStack_TauEta, Data_TauEta, "#tau #eta",0.7,1.3);
  PlotPad_TauEta->SetTickx();
  PlotPad_TauEta->SetTicky();

  BackgroundStack_TauEta->SetMaximum(max(BackgroundStack_TauEta->GetMaximum(),Data_TauEta->GetMaximum()));
  
  BackgroundStack_TauEta->Draw();
  BackgroundStack_TauEta_Errors->Draw("SAME e2");
  BackgroundStack_TauEta->SetTitle("#tau #eta");
  Data_TauEta->Draw("SAME e1");
  AllHiggs_TauEta->Draw("SAME HIST");
  BackgroundStack_TauEta->GetYaxis()->SetTitle("Events");
  BackgroundStack_TauEta->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_TauEta->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_TauEta,0,33);

  TLegend* Legend_TauEta = new TLegend(0.1,0.7,0.3,0.9);
  Legend_TauEta->AddEntry(Data_TauEta,"Observed","pe");
  Legend_TauEta->AddEntry(DYTT_TauEta,"Embedded","f");
  Legend_TauEta->AddEntry(Other_TauEta,"Other","f");
  Legend_TauEta->AddEntry(DYMM_TauEta,"DY #rightarrow ll","f");
    Legend_TauEta->AddEntry(TTFinal_TauEta,"t#bar{t}","f");
  Legend_TauEta->AddEntry(Data_Fake_TauEta,"Fakes","f");
  Legend_TauEta->AddEntry(AllHiggs_TauEta,"All Higgs (#times 30)","l");

  Legend_TauEta->Draw();
  CanvasFour->SaveAs("FinalPlots/TauEta.png");
  CanvasFour->SaveAs("FinalPlots/TauEta.pdf");

  //MET  
  TCanvas* CanvasFive = new TCanvas("CanvasFive","MET",550,550);
  CanvasFive->SetTickx();
  CanvasFive->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_MET = (TH1F*) HistoFile->Get("Data_2018_MET");
  TH1F* Data_Fake_MET = (TH1F*) HistoFile->Get("Fake_2018_MET");
  TH1F* DYTT_MET = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_MET");
  TH1F* DYMM_MET = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_MET");
  TH1F* TTToHadronic_MET = (TH1F*) HistoFile->Get("TTToHadronic_2018_MET");
  TH1F* TTTo2L2Nu_MET = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_MET");
  TH1F* TTToSemiLeptonic_MET = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_MET");  
  TH1F* WW_MET = (TH1F*) HistoFile->Get("WW_2018_MET");
  TH1F* WZ_MET = (TH1F*) HistoFile->Get("WZ_2018_MET");
  TH1F* ZZ_MET = (TH1F*) HistoFile->Get("ZZ_2018_MET");
  TH1F* ST_tW_top_MET = (TH1F*) HistoFile->Get("ST_tW_top_2018_MET");
  TH1F* ggH_MET = (TH1F*) HistoFile->Get("ggH_2018_MET");
  TH1F* VBF_MET = (TH1F*) HistoFile->Get("VBF_2018_MET");
  TH1F* WHPlus_MET = (TH1F*) HistoFile->Get("WHPlus_2018_MET");
  TH1F* WHMinus_MET = (TH1F*) HistoFile->Get("WHMinus_2018_MET");
  TH1F* ZH_MET = (TH1F*) HistoFile->Get("ZH_2018_MET");

  TH1F* TTFinal_MET = (TH1F*) TTToHadronic_MET->Clone();
  TTFinal_MET->Add(TTTo2L2Nu_MET);
  TTFinal_MET->Add(TTToSemiLeptonic_MET);

  TH1F* VVFinal_MET = (TH1F*) WW_MET->Clone();
  VVFinal_MET->Add(WZ_MET);
  VVFinal_MET->Add(ZZ_MET);
  VVFinal_MET->Add(ST_tW_top_MET);
  
  TH1F* VHFinal_MET = (TH1F*) WHPlus_MET->Clone();
  VHFinal_MET->Add(WHMinus_MET);
  VHFinal_MET->Add(ZH_MET);

  TH1F* Other_MET = (TH1F*) VHFinal_MET->Clone();
  Other_MET->Add(ggH_MET);
  Other_MET->Add(VBF_MET);
  Other_MET->Add(VVFinal_MET);

  TH1F* AllHiggs_MET = (TH1F*) VHFinal_MET->Clone();
  AllHiggs_MET->Add(ggH_MET);
  AllHiggs_MET->Add(VBF_MET);

  Data_MET->SetMarkerStyle(20);
  Data_MET->Sumw2();
  
  Data_Fake_MET->SetLineColor(kBlack);
  Data_Fake_MET->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_MET->SetLineColor(kBlack);
  DYTT_MET->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_MET->SetLineColor(kBlack);
  DYMM_MET->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_MET->SetLineColor(kBlack);
  TTFinal_MET->SetFillColor(TColor::GetColor("#9999cc"));

  Other_MET->SetLineColor(kBlack);
  Other_MET->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_MET->SetLineColor(kRed);
  AllHiggs_MET->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_MET->Integral()<<std::endl;

  THStack* BackgroundStack_MET = new THStack("BackgroundStack_MET","BackgroundStack_MET");  
  BackgroundStack_MET->Add(Data_Fake_MET,"hist");
  BackgroundStack_MET->Add(TTFinal_MET,"hist");
  BackgroundStack_MET->Add(DYMM_MET,"hist");
  BackgroundStack_MET->Add(Other_MET,"hist");
  BackgroundStack_MET->Add(DYTT_MET,"hist");

  TH1F* BackgroundStack_MET_Errors = MakeStackErrors(BackgroundStack_MET);

  TPad* PlotPad_MET = MakeRatioPlot(CanvasFive,BackgroundStack_MET, Data_MET, "MET",0.7,1.3);
  PlotPad_MET->SetTickx();
  PlotPad_MET->SetTicky();

  BackgroundStack_MET->SetMaximum(max(BackgroundStack_MET->GetMaximum(),Data_MET->GetMaximum()));
  
  BackgroundStack_MET->Draw();
  BackgroundStack_MET_Errors->Draw("SAME e2");
  BackgroundStack_MET->SetTitle("MET");
  Data_MET->Draw("SAME e1");
  AllHiggs_MET->Draw("SAME HIST");
  BackgroundStack_MET->GetYaxis()->SetTitle("Events");
  BackgroundStack_MET->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_MET->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_MET,0,33);

  TLegend* Legend_MET = new TLegend(0.61,0.41,0.88,0.68);
  Legend_MET->AddEntry(Data_MET,"Observed","pe");
  Legend_MET->AddEntry(DYTT_MET,"Embedded","f");
  Legend_MET->AddEntry(Other_MET,"Other","f");
  Legend_MET->AddEntry(TTFinal_MET,"t#bar{t}","f");
  Legend_MET->AddEntry(DYMM_MET,"DY #rightarrow ll","f");
  Legend_MET->AddEntry(Data_Fake_MET,"Fakes","f");
  Legend_MET->AddEntry(AllHiggs_MET,"All Higgs (#times 30)","l");

  Legend_MET->Draw();
  CanvasFive->SaveAs("FinalPlots/MET.png");
  CanvasFive->SaveAs("FinalPlots/MET.pdf");

  //METPHI
  TCanvas* CanvasSix = new TCanvas("CanvasSix","METPhi",550,550);
  CanvasSix->SetTickx();
  CanvasSix->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_METPhi = (TH1F*) HistoFile->Get("Data_2018_METPhi");
  TH1F* Data_Fake_METPhi = (TH1F*) HistoFile->Get("Fake_2018_METPhi");
  TH1F* DYTT_METPhi = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_METPhi");
  TH1F* DYMM_METPhi = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_METPhi");
  TH1F* TTToHadronic_METPhi = (TH1F*) HistoFile->Get("TTToHadronic_2018_METPhi");
  TH1F* TTTo2L2Nu_METPhi = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_METPhi");
  TH1F* TTToSemiLeptonic_METPhi = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_METPhi");  
  TH1F* WW_METPhi = (TH1F*) HistoFile->Get("WW_2018_METPhi");
  TH1F* WZ_METPhi = (TH1F*) HistoFile->Get("WZ_2018_METPhi");
  TH1F* ZZ_METPhi = (TH1F*) HistoFile->Get("ZZ_2018_METPhi");
  TH1F* ST_tW_top_METPhi = (TH1F*) HistoFile->Get("ST_tW_top_2018_METPhi");
  TH1F* ggH_METPhi = (TH1F*) HistoFile->Get("ggH_2018_METPhi");
  TH1F* VBF_METPhi = (TH1F*) HistoFile->Get("VBF_2018_METPhi");
  TH1F* WHPlus_METPhi = (TH1F*) HistoFile->Get("WHPlus_2018_METPhi");
  TH1F* WHMinus_METPhi = (TH1F*) HistoFile->Get("WHMinus_2018_METPhi");
  TH1F* ZH_METPhi = (TH1F*) HistoFile->Get("ZH_2018_METPhi");

  TH1F* TTFinal_METPhi = (TH1F*) TTToHadronic_METPhi->Clone();
  TTFinal_METPhi->Add(TTTo2L2Nu_METPhi);
  TTFinal_METPhi->Add(TTToSemiLeptonic_METPhi);

  TH1F* VVFinal_METPhi = (TH1F*) WW_METPhi->Clone();
  VVFinal_METPhi->Add(WZ_METPhi);
  VVFinal_METPhi->Add(ZZ_METPhi);
  VVFinal_METPhi->Add(ST_tW_top_METPhi);
  
  TH1F* VHFinal_METPhi = (TH1F*) WHPlus_METPhi->Clone();
  VHFinal_METPhi->Add(WHMinus_METPhi);
  VHFinal_METPhi->Add(ZH_METPhi);

  TH1F* Other_METPhi = (TH1F*) VHFinal_METPhi->Clone();
  Other_METPhi->Add(ggH_METPhi);
  Other_METPhi->Add(VBF_METPhi);
  Other_METPhi->Add(VVFinal_METPhi);

  TH1F* AllHiggs_METPhi = (TH1F*) VHFinal_METPhi->Clone();
  AllHiggs_METPhi->Add(ggH_METPhi);
  AllHiggs_METPhi->Add(VBF_METPhi);

  Data_METPhi->SetMarkerStyle(20);
  Data_METPhi->Sumw2();
  
  Data_Fake_METPhi->SetLineColor(kBlack);
  Data_Fake_METPhi->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_METPhi->SetLineColor(kBlack);
  DYTT_METPhi->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_METPhi->SetLineColor(kBlack);
  DYMM_METPhi->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_METPhi->SetLineColor(kBlack);
  TTFinal_METPhi->SetFillColor(TColor::GetColor("#9999cc"));

  Other_METPhi->SetLineColor(kBlack);
  Other_METPhi->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_METPhi->SetLineColor(kRed);
  AllHiggs_METPhi->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_METPhi->Integral()<<std::endl;

  THStack* BackgroundStack_METPhi = new THStack("BackgroundStack_METPhi","BackgroundStack_METPhi");  
  BackgroundStack_METPhi->Add(Data_Fake_METPhi,"hist");
  BackgroundStack_METPhi->Add(TTFinal_METPhi,"hist");
  BackgroundStack_METPhi->Add(DYMM_METPhi,"hist");
  BackgroundStack_METPhi->Add(Other_METPhi,"hist");
  BackgroundStack_METPhi->Add(DYTT_METPhi,"hist");

  TH1F* BackgroundStack_METPhi_Errors = MakeStackErrors(BackgroundStack_METPhi);

  TPad* PlotPad_METPhi = MakeRatioPlot(CanvasSix,BackgroundStack_METPhi, Data_METPhi, "MET_{#phi}",0.7,1.3);
  PlotPad_METPhi->SetTickx();
  PlotPad_METPhi->SetTicky();

  BackgroundStack_METPhi->SetMaximum(max(BackgroundStack_METPhi->GetMaximum(),Data_METPhi->GetMaximum()));
  
  BackgroundStack_METPhi->Draw();
  BackgroundStack_METPhi_Errors->Draw("SAME e2");
  BackgroundStack_METPhi->SetTitle("MET_{#phi}");
  Data_METPhi->Draw("SAME e1");
  AllHiggs_METPhi->Draw("SAME HIST");
  BackgroundStack_METPhi->GetYaxis()->SetTitle("Events");
  BackgroundStack_METPhi->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_METPhi->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_METPhi,0,33);

  TLegend* Legend_METPhi = new TLegend(0.1,0.7,0.3,0.9);
  Legend_METPhi->AddEntry(Data_METPhi,"Observed","pe");
  Legend_METPhi->AddEntry(DYTT_METPhi,"Embedded","f");
  Legend_METPhi->AddEntry(Other_METPhi,"Other","f");
  Legend_METPhi->AddEntry(DYMM_METPhi,"DY #rightarrow ll","f");
  Legend_METPhi->AddEntry(TTFinal_METPhi,"t#bar{t}","f");
  Legend_METPhi->AddEntry(Data_Fake_METPhi,"Fakes","f");
  Legend_METPhi->AddEntry(AllHiggs_METPhi,"All Higgs (#times 30)","l");

  Legend_METPhi->Draw();
  CanvasSix->SaveAs("FinalPlots/METPhi.png");
  CanvasSix->SaveAs("FinalPlots/METPhi.pdf");

  //mvis histo
  TCanvas* CanvasSeven = new TCanvas("CanvasSeven","mvis",550,550);
  CanvasSeven->SetTickx();
  CanvasSeven->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_mvis = (TH1F*) HistoFile->Get("Data_2018_mvis");
  TH1F* Data_Fake_mvis = (TH1F*) HistoFile->Get("Fake_2018_mvis");
  TH1F* DYTT_mvis = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_mvis");
  TH1F* DYMM_mvis = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_mvis");
  TH1F* TTToHadronic_mvis = (TH1F*) HistoFile->Get("TTToHadronic_2018_mvis");
  TH1F* TTTo2L2Nu_mvis = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_mvis");
  TH1F* TTToSemiLeptonic_mvis = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_mvis");  
  TH1F* WW_mvis = (TH1F*) HistoFile->Get("WW_2018_mvis");
  TH1F* WZ_mvis = (TH1F*) HistoFile->Get("WZ_2018_mvis");
  TH1F* ZZ_mvis = (TH1F*) HistoFile->Get("ZZ_2018_mvis");
  TH1F* ST_tW_top_mvis = (TH1F*) HistoFile->Get("ST_tW_top_2018_mvis");
  TH1F* ggH_mvis = (TH1F*) HistoFile->Get("ggH_2018_mvis");
  TH1F* VBF_mvis = (TH1F*) HistoFile->Get("VBF_2018_mvis");
  TH1F* WHPlus_mvis = (TH1F*) HistoFile->Get("WHPlus_2018_mvis");
  TH1F* WHMinus_mvis = (TH1F*) HistoFile->Get("WHMinus_2018_mvis");
  TH1F* ZH_mvis = (TH1F*) HistoFile->Get("ZH_2018_mvis");

  TH1F* TTFinal_mvis = (TH1F*) TTToHadronic_mvis->Clone();
  TTFinal_mvis->Add(TTTo2L2Nu_mvis);
  TTFinal_mvis->Add(TTToSemiLeptonic_mvis);

  TH1F* VVFinal_mvis = (TH1F*) WW_mvis->Clone();
  VVFinal_mvis->Add(WZ_mvis);
  VVFinal_mvis->Add(ZZ_mvis);
  VVFinal_mvis->Add(ST_tW_top_mvis);
  
  TH1F* VHFinal_mvis = (TH1F*) WHPlus_mvis->Clone();
  VHFinal_mvis->Add(WHMinus_mvis);
  VHFinal_mvis->Add(ZH_mvis);

  TH1F* Other_mvis = (TH1F*) VHFinal_mvis->Clone();
  Other_mvis->Add(ggH_mvis);
  Other_mvis->Add(VBF_mvis);
  Other_mvis->Add(VVFinal_mvis);

  TH1F* AllHiggs_mvis = (TH1F*) VHFinal_mvis->Clone();
  AllHiggs_mvis->Add(ggH_mvis);
  AllHiggs_mvis->Add(VBF_mvis);

  Data_mvis->SetMarkerStyle(20);
  Data_mvis->Sumw2();
  
  Data_Fake_mvis->SetLineColor(kBlack);
  Data_Fake_mvis->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_mvis->SetLineColor(kBlack);
  DYTT_mvis->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_mvis->SetLineColor(kBlack);
  DYMM_mvis->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_mvis->SetLineColor(kBlack);
  TTFinal_mvis->SetFillColor(TColor::GetColor("#9999cc"));

  Other_mvis->SetLineColor(kBlack);
  Other_mvis->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_mvis->SetLineColor(kRed);
  AllHiggs_mvis->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_mvis->Integral()<<std::endl;

  THStack* BackgroundStack_mvis = new THStack("BackgroundStack_mvis","BackgroundStack_mvis");  
  BackgroundStack_mvis->Add(Data_Fake_mvis,"hist");    
  BackgroundStack_mvis->Add(TTFinal_mvis,"hist");
  BackgroundStack_mvis->Add(DYMM_mvis,"hist");
  BackgroundStack_mvis->Add(Other_mvis,"hist");
  BackgroundStack_mvis->Add(DYTT_mvis,"hist");

  TH1F* BackgroundStack_mvis_Errors = MakeStackErrors(BackgroundStack_mvis);

  TPad* PlotPad_mvis = MakeRatioPlot(CanvasSeven,BackgroundStack_mvis, Data_mvis, "m_{vis}",0.7,1.3);
  PlotPad_mvis->SetTickx();
  PlotPad_mvis->SetTicky();

  BackgroundStack_mvis->SetMaximum(max(BackgroundStack_mvis->GetMaximum(),Data_mvis->GetMaximum()));
  
  BackgroundStack_mvis->Draw();
  BackgroundStack_mvis_Errors->Draw("SAME e2");
  BackgroundStack_mvis->SetTitle("m_{vis}");
  Data_mvis->Draw("SAME e1");
  AllHiggs_mvis->Draw("SAME HIST");
  BackgroundStack_mvis->GetYaxis()->SetTitle("Events");
  BackgroundStack_mvis->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_mvis->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_mvis,0,33);

  TLegend* Legend_mvis = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_mvis->AddEntry(Data_mvis,"Observed","pe");
  Legend_mvis->AddEntry(DYTT_mvis,"Embedded","f");
  Legend_mvis->AddEntry(Other_mvis,"Other","f");
  Legend_mvis->AddEntry(DYMM_mvis,"DY #rightarrow ll","f");
  Legend_mvis->AddEntry(TTFinal_mvis,"t#bar{t}","f");
  Legend_mvis->AddEntry(Data_Fake_mvis,"Fakes","f");
  Legend_mvis->AddEntry(AllHiggs_mvis,"All Higgs (#times 30)","l");

  Legend_mvis->Draw();
  CanvasSeven->SaveAs("FinalPlots/mvis.png");
  CanvasSeven->SaveAs("FinalPlots/mvis.pdf");

  //NJets Histo
  TCanvas* CanvasEight = new TCanvas("CanvasEight","Njets",550,550);
  CanvasEight->SetTickx();
  CanvasEight->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_Njets = (TH1F*) HistoFile->Get("Data_2018_Njets");
  TH1F* Data_Fake_Njets = (TH1F*) HistoFile->Get("Fake_2018_Njets");
  TH1F* DYTT_Njets = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_Njets");
  TH1F* DYMM_Njets = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_Njets");
  TH1F* TTToHadronic_Njets = (TH1F*) HistoFile->Get("TTToHadronic_2018_Njets");
  TH1F* TTTo2L2Nu_Njets = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_Njets");
  TH1F* TTToSemiLeptonic_Njets = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_Njets");  
  TH1F* WW_Njets = (TH1F*) HistoFile->Get("WW_2018_Njets");
  TH1F* WZ_Njets = (TH1F*) HistoFile->Get("WZ_2018_Njets");
  TH1F* ZZ_Njets = (TH1F*) HistoFile->Get("ZZ_2018_Njets");
  TH1F* ST_tW_top_Njets = (TH1F*) HistoFile->Get("ST_tW_top_2018_Njets");
  TH1F* ggH_Njets = (TH1F*) HistoFile->Get("ggH_2018_Njets");
  TH1F* VBF_Njets = (TH1F*) HistoFile->Get("VBF_2018_Njets");
  TH1F* WHPlus_Njets = (TH1F*) HistoFile->Get("WHPlus_2018_Njets");
  TH1F* WHMinus_Njets = (TH1F*) HistoFile->Get("WHMinus_2018_Njets");
  TH1F* ZH_Njets = (TH1F*) HistoFile->Get("ZH_2018_Njets");

  TH1F* TTFinal_Njets = (TH1F*) TTToHadronic_Njets->Clone();
  TTFinal_Njets->Add(TTTo2L2Nu_Njets);
  TTFinal_Njets->Add(TTToSemiLeptonic_Njets);

  TH1F* VVFinal_Njets = (TH1F*) WW_Njets->Clone();
  VVFinal_Njets->Add(WZ_Njets);
  VVFinal_Njets->Add(ZZ_Njets);
  VVFinal_Njets->Add(ST_tW_top_Njets);
  
  TH1F* VHFinal_Njets = (TH1F*) WHPlus_Njets->Clone();
  VHFinal_Njets->Add(WHMinus_Njets);
  VHFinal_Njets->Add(ZH_Njets);

  TH1F* Other_Njets = (TH1F*) VHFinal_Njets->Clone();
  Other_Njets->Add(ggH_Njets);
  Other_Njets->Add(VBF_Njets);
  Other_Njets->Add(VVFinal_Njets);

  TH1F* AllHiggs_Njets = (TH1F*) VHFinal_Njets->Clone();
  AllHiggs_Njets->Add(ggH_Njets);
  AllHiggs_Njets->Add(VBF_Njets);

  Data_Njets->SetMarkerStyle(20);
  Data_Njets->Sumw2();
  
  Data_Fake_Njets->SetLineColor(kBlack);
  Data_Fake_Njets->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_Njets->SetLineColor(kBlack);
  DYTT_Njets->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_Njets->SetLineColor(kBlack);
  DYMM_Njets->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_Njets->SetLineColor(kBlack);
  TTFinal_Njets->SetFillColor(TColor::GetColor("#9999cc"));

  Other_Njets->SetLineColor(kBlack);
  Other_Njets->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_Njets->SetLineColor(kRed);
  AllHiggs_Njets->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_Njets->Integral()<<std::endl;

  THStack* BackgroundStack_Njets = new THStack("BackgroundStack_Njets","BackgroundStack_Njets");  
  BackgroundStack_Njets->Add(Data_Fake_Njets,"hist");
  BackgroundStack_Njets->Add(TTFinal_Njets,"hist");
  BackgroundStack_Njets->Add(DYMM_Njets,"hist");
  BackgroundStack_Njets->Add(Other_Njets,"hist");
  BackgroundStack_Njets->Add(DYTT_Njets,"hist");

  TH1F* BackgroundStack_Njets_Errors = MakeStackErrors(BackgroundStack_Njets);

  TPad* PlotPad_Njets = MakeRatioPlot(CanvasEight,BackgroundStack_Njets, Data_Njets, "N_{jets}",0.7,1.3);
  PlotPad_Njets->SetTickx();
  PlotPad_Njets->SetTicky();

  BackgroundStack_Njets->SetMaximum(max(BackgroundStack_Njets->GetMaximum(),Data_Njets->GetMaximum()));
  
  BackgroundStack_Njets->Draw();
  BackgroundStack_Njets_Errors->Draw("SAME e2");
  BackgroundStack_Njets->SetTitle("N_{jets}");
  Data_Njets->Draw("SAME e1");
  AllHiggs_Njets->Draw("SAME HIST");
  BackgroundStack_Njets->GetYaxis()->SetTitle("Events");
  BackgroundStack_Njets->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_Njets->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_Njets,0,33);

  TLegend* Legend_Njets = new TLegend(0.61,0.41,0.88,0.68);
  Legend_Njets->AddEntry(Data_Njets,"Observed","pe");
  Legend_Njets->AddEntry(DYTT_Njets,"Embedded","f");
  Legend_Njets->AddEntry(Other_Njets,"Other","f");
  Legend_Njets->AddEntry(DYMM_Njets,"DY #rightarrow ll","f");
  Legend_Njets->AddEntry(TTFinal_Njets,"t#bar{t}","f");
  Legend_Njets->AddEntry(Data_Fake_Njets,"Fakes","f");
  Legend_Njets->AddEntry(AllHiggs_Njets,"All Higgs (#times 30)","l");

  Legend_Njets->Draw();
  CanvasEight->SaveAs("FinalPlots/Njets.png");
  CanvasEight->SaveAs("FinalPlots/Njets.pdf");

  //Higgs Pt Histo
  TCanvas* CanvasNine = new TCanvas("CanvasNine","HiggsPt",550,550);
  CanvasNine->SetTickx();
  CanvasNine->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_HiggsPt = (TH1F*) HistoFile->Get("Data_2018_HiggsPt");
  TH1F* Data_Fake_HiggsPt = (TH1F*) HistoFile->Get("Fake_2018_HiggsPt");
  TH1F* DYTT_HiggsPt = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_HiggsPt");
  TH1F* DYMM_HiggsPt = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_HiggsPt");
  TH1F* TTToHadronic_HiggsPt = (TH1F*) HistoFile->Get("TTToHadronic_2018_HiggsPt");
  TH1F* TTTo2L2Nu_HiggsPt = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_HiggsPt");
  TH1F* TTToSemiLeptonic_HiggsPt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_HiggsPt");  
  TH1F* WW_HiggsPt = (TH1F*) HistoFile->Get("WW_2018_HiggsPt");
  TH1F* WZ_HiggsPt = (TH1F*) HistoFile->Get("WZ_2018_HiggsPt");
  TH1F* ZZ_HiggsPt = (TH1F*) HistoFile->Get("ZZ_2018_HiggsPt");
  TH1F* ST_tW_top_HiggsPt = (TH1F*) HistoFile->Get("ST_tW_top_2018_HiggsPt");
  TH1F* ggH_HiggsPt = (TH1F*) HistoFile->Get("ggH_2018_HiggsPt");
  TH1F* VBF_HiggsPt = (TH1F*) HistoFile->Get("VBF_2018_HiggsPt");
  TH1F* WHPlus_HiggsPt = (TH1F*) HistoFile->Get("WHPlus_2018_HiggsPt");
  TH1F* WHMinus_HiggsPt = (TH1F*) HistoFile->Get("WHMinus_2018_HiggsPt");
  TH1F* ZH_HiggsPt = (TH1F*) HistoFile->Get("ZH_2018_HiggsPt");

  TH1F* TTFinal_HiggsPt = (TH1F*) TTToHadronic_HiggsPt->Clone();
  TTFinal_HiggsPt->Add(TTTo2L2Nu_HiggsPt);
  TTFinal_HiggsPt->Add(TTToSemiLeptonic_HiggsPt);

  TH1F* VVFinal_HiggsPt = (TH1F*) WW_HiggsPt->Clone();
  VVFinal_HiggsPt->Add(WZ_HiggsPt);
  VVFinal_HiggsPt->Add(ZZ_HiggsPt);
  VVFinal_HiggsPt->Add(ST_tW_top_HiggsPt);
  
  TH1F* VHFinal_HiggsPt = (TH1F*) WHPlus_HiggsPt->Clone();
  VHFinal_HiggsPt->Add(WHMinus_HiggsPt);
  VHFinal_HiggsPt->Add(ZH_HiggsPt);

  TH1F* Other_HiggsPt = (TH1F*) VHFinal_HiggsPt->Clone();
  Other_HiggsPt->Add(ggH_HiggsPt);
  Other_HiggsPt->Add(VBF_HiggsPt);
  Other_HiggsPt->Add(VVFinal_HiggsPt);

  TH1F* AllHiggs_HiggsPt = (TH1F*) VHFinal_HiggsPt->Clone();
  AllHiggs_HiggsPt->Add(ggH_HiggsPt);
  AllHiggs_HiggsPt->Add(VBF_HiggsPt);

  Data_HiggsPt->SetMarkerStyle(20);
  Data_HiggsPt->Sumw2();
  
  Data_Fake_HiggsPt->SetLineColor(kBlack);
  Data_Fake_HiggsPt->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_HiggsPt->SetLineColor(kBlack);
  DYTT_HiggsPt->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_HiggsPt->SetLineColor(kBlack);
  DYMM_HiggsPt->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_HiggsPt->SetLineColor(kBlack);
  TTFinal_HiggsPt->SetFillColor(TColor::GetColor("#9999cc"));

  Other_HiggsPt->SetLineColor(kBlack);
  Other_HiggsPt->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_HiggsPt->SetLineColor(kRed);
  AllHiggs_HiggsPt->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_HiggsPt->Integral()<<std::endl;

  THStack* BackgroundStack_HiggsPt = new THStack("BackgroundStack_HiggsPt","BackgroundStack_HiggsPt");  
  BackgroundStack_HiggsPt->Add(Data_Fake_HiggsPt,"hist");
  BackgroundStack_HiggsPt->Add(TTFinal_HiggsPt,"hist");
  BackgroundStack_HiggsPt->Add(DYMM_HiggsPt,"hist");
  BackgroundStack_HiggsPt->Add(Other_HiggsPt,"hist");
  BackgroundStack_HiggsPt->Add(DYTT_HiggsPt,"hist");

  TH1F* BackgroundStack_HiggsPt_Errors = MakeStackErrors(BackgroundStack_HiggsPt);

  TPad* PlotPad_HiggsPt = MakeRatioPlot(CanvasNine,BackgroundStack_HiggsPt, Data_HiggsPt, "Higgs p_{t}",0.7,1.3);
  PlotPad_HiggsPt->SetTickx();
  PlotPad_HiggsPt->SetTicky();

  BackgroundStack_HiggsPt->SetMaximum(max(BackgroundStack_HiggsPt->GetMaximum(),Data_HiggsPt->GetMaximum()));
  
  BackgroundStack_HiggsPt->Draw();
  BackgroundStack_HiggsPt_Errors->Draw("SAME e2");
  BackgroundStack_HiggsPt->SetTitle("Higgs p_{t}");
  Data_HiggsPt->Draw("SAME e1");
  AllHiggs_HiggsPt->Draw("SAME HIST");
  BackgroundStack_HiggsPt->GetYaxis()->SetTitle("Events");
  BackgroundStack_HiggsPt->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_HiggsPt->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_HiggsPt,0,33);

  TLegend* Legend_HiggsPt = new TLegend(0.61,0.41,0.88,0.68);
  Legend_HiggsPt->AddEntry(Data_HiggsPt,"Observed","pe");
  Legend_HiggsPt->AddEntry(DYTT_HiggsPt,"Embedded","f");
  Legend_HiggsPt->AddEntry(Other_HiggsPt,"Other","f");
  Legend_HiggsPt->AddEntry(DYMM_HiggsPt,"DY #rightarrow ll","f");
  Legend_HiggsPt->AddEntry(TTFinal_HiggsPt,"t#bar{t}","f");
  Legend_HiggsPt->AddEntry(Data_Fake_HiggsPt,"Fakes","f");
  Legend_HiggsPt->AddEntry(AllHiggs_HiggsPt,"All Higgs (#times 30)","l");

  Legend_HiggsPt->Draw();
  CanvasNine->SaveAs("FinalPlots/HiggsPt.png");
  CanvasNine->SaveAs("FinalPlots/HiggsPt.pdf");

  //mjj Histo
  TCanvas* CanvasTen = new TCanvas("CanvasTen","mjj",550,550);
  CanvasTen->SetTickx();
  CanvasTen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_mjj = (TH1F*) HistoFile->Get("Data_2018_mjj");
  TH1F* Data_Fake_mjj = (TH1F*) HistoFile->Get("Fake_2018_mjj");
  TH1F* DYTT_mjj = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_mjj");
  TH1F* DYMM_mjj = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_mjj");
  TH1F* TTToHadronic_mjj = (TH1F*) HistoFile->Get("TTToHadronic_2018_mjj");
  TH1F* TTTo2L2Nu_mjj = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_mjj");
  TH1F* TTToSemiLeptonic_mjj = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_mjj");  
  TH1F* WW_mjj = (TH1F*) HistoFile->Get("WW_2018_mjj");
  TH1F* WZ_mjj = (TH1F*) HistoFile->Get("WZ_2018_mjj");
  TH1F* ZZ_mjj = (TH1F*) HistoFile->Get("ZZ_2018_mjj");
  TH1F* ST_tW_top_mjj = (TH1F*) HistoFile->Get("ST_tW_top_2018_mjj");
  TH1F* ggH_mjj = (TH1F*) HistoFile->Get("ggH_2018_mjj");
  TH1F* VBF_mjj = (TH1F*) HistoFile->Get("VBF_2018_mjj");
  TH1F* WHPlus_mjj = (TH1F*) HistoFile->Get("WHPlus_2018_mjj");
  TH1F* WHMinus_mjj = (TH1F*) HistoFile->Get("WHMinus_2018_mjj");
  TH1F* ZH_mjj = (TH1F*) HistoFile->Get("ZH_2018_mjj");

  TH1F* TTFinal_mjj = (TH1F*) TTToHadronic_mjj->Clone();
  TTFinal_mjj->Add(TTTo2L2Nu_mjj);
  TTFinal_mjj->Add(TTToSemiLeptonic_mjj);

  TH1F* VVFinal_mjj = (TH1F*) WW_mjj->Clone();
  VVFinal_mjj->Add(WZ_mjj);
  VVFinal_mjj->Add(ZZ_mjj);
  VVFinal_mjj->Add(ST_tW_top_mjj);
  
  TH1F* VHFinal_mjj = (TH1F*) WHPlus_mjj->Clone();
  VHFinal_mjj->Add(WHMinus_mjj);
  VHFinal_mjj->Add(ZH_mjj);

  TH1F* Other_mjj = (TH1F*) VHFinal_mjj->Clone();
  Other_mjj->Add(ggH_mjj);
  Other_mjj->Add(VBF_mjj);
  Other_mjj->Add(VVFinal_mjj);

  TH1F* AllHiggs_mjj = (TH1F*) VHFinal_mjj->Clone();
  AllHiggs_mjj->Add(ggH_mjj);
  AllHiggs_mjj->Add(VBF_mjj);

  Data_mjj->SetMarkerStyle(20);
  Data_mjj->Sumw2();
  
  Data_Fake_mjj->SetLineColor(kBlack);
  Data_Fake_mjj->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_mjj->SetLineColor(kBlack);
  DYTT_mjj->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_mjj->SetLineColor(kBlack);
  DYMM_mjj->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_mjj->SetLineColor(kBlack);
  TTFinal_mjj->SetFillColor(TColor::GetColor("#9999cc"));

  Other_mjj->SetLineColor(kBlack);
  Other_mjj->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_mjj->SetLineColor(kRed);
  AllHiggs_mjj->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_mjj->Integral()<<std::endl;

  THStack* BackgroundStack_mjj = new THStack("BackgroundStack_mjj","BackgroundStack_mjj");  
  BackgroundStack_mjj->Add(Data_Fake_mjj,"hist");
  BackgroundStack_mjj->Add(TTFinal_mjj,"hist");
  BackgroundStack_mjj->Add(Other_mjj,"hist");
  BackgroundStack_mjj->Add(DYMM_mjj,"hist");
  BackgroundStack_mjj->Add(DYTT_mjj,"hist");

  TH1F* BackgroundStack_mjj_Errors = MakeStackErrors(BackgroundStack_mjj);

  TPad* PlotPad_mjj = MakeRatioPlot(CanvasTen,BackgroundStack_mjj, Data_mjj, "m_{jj}",0.7,1.3);
  PlotPad_mjj->SetTickx();
  PlotPad_mjj->SetTicky();

  BackgroundStack_mjj->SetMaximum(max(BackgroundStack_mjj->GetMaximum(),Data_mjj->GetMaximum()));
  
  BackgroundStack_mjj->Draw();
  BackgroundStack_mjj_Errors->Draw("SAME e2");
  BackgroundStack_mjj->SetTitle("m_{jj}");
  Data_mjj->Draw("SAME e1");
  AllHiggs_mjj->Draw("SAME HIST");
  BackgroundStack_mjj->GetYaxis()->SetTitle("Events");
  BackgroundStack_mjj->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_mjj->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_mjj,0,33);

  TLegend* Legend_mjj = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_mjj->AddEntry(Data_mjj,"Observed","pe");
  Legend_mjj->AddEntry(DYTT_mjj,"Embedded","f");
  Legend_mjj->AddEntry(Other_mjj,"Other","f");
  Legend_mjj->AddEntry(DYMM_mjj,"DY #rightarrow ll","f");
  Legend_mjj->AddEntry(TTFinal_mjj,"t#bar{t}","f");
  Legend_mjj->AddEntry(Data_Fake_mjj,"Fakes","f");
  Legend_mjj->AddEntry(AllHiggs_mjj,"All Higgs (#times 30)","l");

  Legend_mjj->Draw();
  CanvasTen->SaveAs("FinalPlots/mjj.png");
  CanvasTen->SaveAs("FinalPlots/mjj.pdf");

  //jeta_1 histo
  TCanvas* CanvasEleven = new TCanvas("CanvasEleven","j1eta",550,550);
  CanvasEleven->SetTickx();
  CanvasEleven->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_j1eta = (TH1F*) HistoFile->Get("Data_2018_j1eta");
  TH1F* Data_Fake_j1eta = (TH1F*) HistoFile->Get("Fake_2018_j1eta");
  TH1F* DYTT_j1eta = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_j1eta");
  TH1F* DYMM_j1eta = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_j1eta");
  TH1F* TTToHadronic_j1eta = (TH1F*) HistoFile->Get("TTToHadronic_2018_j1eta");
  TH1F* TTTo2L2Nu_j1eta = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_j1eta");
  TH1F* TTToSemiLeptonic_j1eta = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_j1eta");  
  TH1F* WW_j1eta = (TH1F*) HistoFile->Get("WW_2018_j1eta");
  TH1F* WZ_j1eta = (TH1F*) HistoFile->Get("WZ_2018_j1eta");
  TH1F* ZZ_j1eta = (TH1F*) HistoFile->Get("ZZ_2018_j1eta");
  TH1F* ST_tW_top_j1eta = (TH1F*) HistoFile->Get("ST_tW_top_2018_j1eta");
  TH1F* ggH_j1eta = (TH1F*) HistoFile->Get("ggH_2018_j1eta");
  TH1F* VBF_j1eta = (TH1F*) HistoFile->Get("VBF_2018_j1eta");
  TH1F* WHPlus_j1eta = (TH1F*) HistoFile->Get("WHPlus_2018_j1eta");
  TH1F* WHMinus_j1eta = (TH1F*) HistoFile->Get("WHMinus_2018_j1eta");
  TH1F* ZH_j1eta = (TH1F*) HistoFile->Get("ZH_2018_j1eta");

  TH1F* TTFinal_j1eta = (TH1F*) TTToHadronic_j1eta->Clone();
  TTFinal_j1eta->Add(TTTo2L2Nu_j1eta);
  TTFinal_j1eta->Add(TTToSemiLeptonic_j1eta);

  TH1F* VVFinal_j1eta = (TH1F*) WW_j1eta->Clone();
  VVFinal_j1eta->Add(WZ_j1eta);
  VVFinal_j1eta->Add(ZZ_j1eta);
  VVFinal_j1eta->Add(ST_tW_top_j1eta);
  
  TH1F* VHFinal_j1eta = (TH1F*) WHPlus_j1eta->Clone();
  VHFinal_j1eta->Add(WHMinus_j1eta);
  VHFinal_j1eta->Add(ZH_j1eta);

  TH1F* Other_j1eta = (TH1F*) VHFinal_j1eta->Clone();
  Other_j1eta->Add(ggH_j1eta);
  Other_j1eta->Add(VBF_j1eta);
  Other_j1eta->Add(VVFinal_j1eta);

  TH1F* AllHiggs_j1eta = (TH1F*) VHFinal_j1eta->Clone();
  AllHiggs_j1eta->Add(ggH_j1eta);
  AllHiggs_j1eta->Add(VBF_j1eta);

  Data_j1eta->SetMarkerStyle(20);
  Data_j1eta->Sumw2();
  
  Data_Fake_j1eta->SetLineColor(kBlack);
  Data_Fake_j1eta->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_j1eta->SetLineColor(kBlack);
  DYTT_j1eta->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_j1eta->SetLineColor(kBlack);
  DYMM_j1eta->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_j1eta->SetLineColor(kBlack);
  TTFinal_j1eta->SetFillColor(TColor::GetColor("#9999cc"));

  Other_j1eta->SetLineColor(kBlack);
  Other_j1eta->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_j1eta->SetLineColor(kRed);
  AllHiggs_j1eta->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_j1eta->Integral()<<std::endl;

  THStack* BackgroundStack_j1eta = new THStack("BackgroundStack_j1eta","BackgroundStack_j1eta");  
  BackgroundStack_j1eta->Add(Data_Fake_j1eta,"hist");
  BackgroundStack_j1eta->Add(TTFinal_j1eta,"hist");
  BackgroundStack_j1eta->Add(Other_j1eta,"hist");
  BackgroundStack_j1eta->Add(DYMM_j1eta,"hist");
  BackgroundStack_j1eta->Add(DYTT_j1eta,"hist");

  TH1F* BackgroundStack_j1eta_Errors = MakeStackErrors(BackgroundStack_j1eta);

  TPad* PlotPad_j1eta = MakeRatioPlot(CanvasEleven,BackgroundStack_j1eta, Data_j1eta, "#eta_{j_{1}}",0.7,1.3);
  PlotPad_j1eta->SetTickx();
  PlotPad_j1eta->SetTicky();

  BackgroundStack_j1eta->SetMaximum(max(BackgroundStack_j1eta->GetMaximum(),Data_j1eta->GetMaximum()));
  
  BackgroundStack_j1eta->Draw();
  BackgroundStack_j1eta_Errors->Draw("SAME e2");
  BackgroundStack_j1eta->SetTitle("#eta_{j_{1}}");
  Data_j1eta->Draw("SAME e1");
  AllHiggs_j1eta->Draw("SAME HIST");
  BackgroundStack_j1eta->GetYaxis()->SetTitle("Events");
  BackgroundStack_j1eta->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_j1eta->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_j1eta,0,33);

  TLegend* Legend_j1eta = new TLegend(0.78,0.41,0.98,0.68);  
  Legend_j1eta->AddEntry(Data_j1eta,"Observed","pe");
  Legend_j1eta->AddEntry(DYTT_j1eta,"Embedded","f");
  Legend_j1eta->AddEntry(Other_j1eta,"Other","f");
  Legend_j1eta->AddEntry(DYMM_j1eta,"DY #rightarrow ll","f");
  Legend_j1eta->AddEntry(TTFinal_j1eta,"t#bar{t}","f");
  Legend_j1eta->AddEntry(Data_Fake_j1eta,"Fakes","f");
  Legend_j1eta->AddEntry(AllHiggs_j1eta,"All Higgs (#times 30)","l");

  Legend_j1eta->Draw();
  CanvasEleven->SaveAs("FinalPlots/j1eta.png");
  CanvasEleven->SaveAs("FinalPlots/j1eta.pdf");
  
  //trigger histo
  TCanvas* CanvasTwelve = new TCanvas("CanvasTwelve","trigger",550,550);
  CanvasTwelve->SetTickx();
  CanvasTwelve->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_trigger = (TH1F*) HistoFile->Get("Data_2018_trigger");
  TH1F* Data_Fake_trigger = (TH1F*) HistoFile->Get("Fake_2018_trigger");
  TH1F* DYTT_trigger = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_trigger");
  TH1F* DYMM_trigger = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_trigger");
  TH1F* TTToHadronic_trigger = (TH1F*) HistoFile->Get("TTToHadronic_2018_trigger");
  TH1F* TTTo2L2Nu_trigger = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_trigger");
  TH1F* TTToSemiLeptonic_trigger = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_trigger");  
  TH1F* WW_trigger = (TH1F*) HistoFile->Get("WW_2018_trigger");
  TH1F* WZ_trigger = (TH1F*) HistoFile->Get("WZ_2018_trigger");
  TH1F* ZZ_trigger = (TH1F*) HistoFile->Get("ZZ_2018_trigger");
  TH1F* ST_tW_top_trigger = (TH1F*) HistoFile->Get("ST_tW_top_2018_trigger");
  TH1F* ggH_trigger = (TH1F*) HistoFile->Get("ggH_2018_trigger");
  TH1F* VBF_trigger = (TH1F*) HistoFile->Get("VBF_2018_trigger");
  TH1F* WHPlus_trigger = (TH1F*) HistoFile->Get("WHPlus_2018_trigger");
  TH1F* WHMinus_trigger = (TH1F*) HistoFile->Get("WHMinus_2018_trigger");
  TH1F* ZH_trigger = (TH1F*) HistoFile->Get("ZH_2018_trigger");

  TH1F* TTFinal_trigger = (TH1F*) TTToHadronic_trigger->Clone();
  TTFinal_trigger->Add(TTTo2L2Nu_trigger);
  TTFinal_trigger->Add(TTToSemiLeptonic_trigger);

  TH1F* VVFinal_trigger = (TH1F*) WW_trigger->Clone();
  VVFinal_trigger->Add(WZ_trigger);
  VVFinal_trigger->Add(ZZ_trigger);
  VVFinal_trigger->Add(ST_tW_top_trigger);
  
  TH1F* VHFinal_trigger = (TH1F*) WHPlus_trigger->Clone();
  VHFinal_trigger->Add(WHMinus_trigger);
  VHFinal_trigger->Add(ZH_trigger);

  TH1F* Other_trigger = (TH1F*) VHFinal_trigger->Clone();
  Other_trigger->Add(ggH_trigger);
  Other_trigger->Add(VBF_trigger);
  Other_trigger->Add(VVFinal_trigger);

  TH1F* AllHiggs_trigger = (TH1F*) VHFinal_trigger->Clone();
  AllHiggs_trigger->Add(ggH_trigger);
  AllHiggs_trigger->Add(VBF_trigger);

  Data_trigger->SetMarkerStyle(20);
  Data_trigger->Sumw2();
  
  Data_Fake_trigger->SetLineColor(kBlack);
  Data_Fake_trigger->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_trigger->SetLineColor(kBlack);
  DYTT_trigger->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_trigger->SetLineColor(kBlack);
  DYMM_trigger->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_trigger->SetLineColor(kBlack);
  TTFinal_trigger->SetFillColor(TColor::GetColor("#9999cc"));

  Other_trigger->SetLineColor(kBlack);
  Other_trigger->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_trigger->SetLineColor(kRed);
  AllHiggs_trigger->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_trigger->Integral()<<std::endl;

  THStack* BackgroundStack_trigger = new THStack("BackgroundStack_trigger","BackgroundStack_trigger");  
  BackgroundStack_trigger->Add(Data_Fake_trigger,"hist");
  BackgroundStack_trigger->Add(TTFinal_trigger,"hist");
  BackgroundStack_trigger->Add(Other_trigger,"hist");
  BackgroundStack_trigger->Add(DYMM_trigger,"hist");
  BackgroundStack_trigger->Add(DYTT_trigger,"hist");

  TH1F* BackgroundStack_trigger_Errors = MakeStackErrors(BackgroundStack_trigger);

  TPad* PlotPad_trigger = MakeRatioPlot(CanvasTwelve,BackgroundStack_trigger, Data_trigger, "trigger",0.7,1.3);
  PlotPad_trigger->SetTickx();
  PlotPad_trigger->SetTicky();

  BackgroundStack_trigger->SetMaximum(max(BackgroundStack_trigger->GetMaximum(),Data_trigger->GetMaximum()));
  
  BackgroundStack_trigger->Draw();
  BackgroundStack_trigger_Errors->Draw("SAME e2");
  BackgroundStack_trigger->SetTitle("trigger");
  Data_trigger->Draw("SAME e1");
  AllHiggs_trigger->Draw("SAME HIST");
  BackgroundStack_trigger->GetYaxis()->SetTitle("Events");
  BackgroundStack_trigger->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_trigger->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_trigger,0,33);

  TLegend* Legend_trigger = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_trigger->AddEntry(Data_trigger,"Observed","pe");
  Legend_trigger->AddEntry(DYTT_trigger,"Embedded","f");
  Legend_trigger->AddEntry(Other_trigger,"Other","f");
  Legend_trigger->AddEntry(DYMM_trigger,"DY #rightarrow ll","f");
  Legend_trigger->AddEntry(TTFinal_trigger,"t#bar{t}","f");
  Legend_trigger->AddEntry(Data_Fake_trigger,"Fakes","f");
  Legend_trigger->AddEntry(AllHiggs_trigger,"All Higgs (#times 30)","l");

  Legend_trigger->Draw();
  CanvasTwelve->SaveAs("FinalPlots/trigger.png");
  CanvasTwelve->SaveAs("FinalPlots/trigger.pdf");

  //leading jet pt
  TCanvas* CanvasThirteen = new TCanvas("CanvasThirteen","j1pt",550,550);
  CanvasThirteen->SetTickx();
  CanvasThirteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_j1pt = (TH1F*) HistoFile->Get("Data_2018_j1pt");
  TH1F* Data_Fake_j1pt = (TH1F*) HistoFile->Get("Fake_2018_j1pt");
  TH1F* DYTT_j1pt = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_j1pt");
  TH1F* DYMM_j1pt = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_j1pt");
  TH1F* TTToHadronic_j1pt = (TH1F*) HistoFile->Get("TTToHadronic_2018_j1pt");
  TH1F* TTTo2L2Nu_j1pt = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_j1pt");
  TH1F* TTToSemiLeptonic_j1pt = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_j1pt");  
  TH1F* WW_j1pt = (TH1F*) HistoFile->Get("WW_2018_j1pt");
  TH1F* WZ_j1pt = (TH1F*) HistoFile->Get("WZ_2018_j1pt");
  TH1F* ZZ_j1pt = (TH1F*) HistoFile->Get("ZZ_2018_j1pt");
  TH1F* ST_tW_top_j1pt = (TH1F*) HistoFile->Get("ST_tW_top_2018_j1pt");
  TH1F* ggH_j1pt = (TH1F*) HistoFile->Get("ggH_2018_j1pt");
  TH1F* VBF_j1pt = (TH1F*) HistoFile->Get("VBF_2018_j1pt");
  TH1F* WHPlus_j1pt = (TH1F*) HistoFile->Get("WHPlus_2018_j1pt");
  TH1F* WHMinus_j1pt = (TH1F*) HistoFile->Get("WHMinus_2018_j1pt");
  TH1F* ZH_j1pt = (TH1F*) HistoFile->Get("ZH_2018_j1pt");

  TH1F* TTFinal_j1pt = (TH1F*) TTToHadronic_j1pt->Clone();
  TTFinal_j1pt->Add(TTTo2L2Nu_j1pt);
  TTFinal_j1pt->Add(TTToSemiLeptonic_j1pt);

  TH1F* VVFinal_j1pt = (TH1F*) WW_j1pt->Clone();
  VVFinal_j1pt->Add(WZ_j1pt);
  VVFinal_j1pt->Add(ZZ_j1pt);
  VVFinal_j1pt->Add(ST_tW_top_j1pt);
  
  TH1F* VHFinal_j1pt = (TH1F*) WHPlus_j1pt->Clone();
  VHFinal_j1pt->Add(WHMinus_j1pt);
  VHFinal_j1pt->Add(ZH_j1pt);

  TH1F* Other_j1pt = (TH1F*) VHFinal_j1pt->Clone();
  Other_j1pt->Add(ggH_j1pt);
  Other_j1pt->Add(VBF_j1pt);
  Other_j1pt->Add(VVFinal_j1pt);

  TH1F* AllHiggs_j1pt = (TH1F*) VHFinal_j1pt->Clone();
  AllHiggs_j1pt->Add(ggH_j1pt);
  AllHiggs_j1pt->Add(VBF_j1pt);

  Data_j1pt->SetMarkerStyle(20);
  Data_j1pt->Sumw2();
  
  Data_Fake_j1pt->SetLineColor(kBlack);
  Data_Fake_j1pt->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_j1pt->SetLineColor(kBlack);
  DYTT_j1pt->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_j1pt->SetLineColor(kBlack);
  DYMM_j1pt->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_j1pt->SetLineColor(kBlack);
  TTFinal_j1pt->SetFillColor(TColor::GetColor("#9999cc"));

  Other_j1pt->SetLineColor(kBlack);
  Other_j1pt->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_j1pt->SetLineColor(kRed);
  AllHiggs_j1pt->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_j1pt->Integral()<<std::endl;

  THStack* BackgroundStack_j1pt = new THStack("BackgroundStack_j1pt","BackgroundStack_j1pt");  
  BackgroundStack_j1pt->Add(Data_Fake_j1pt,"hist");
  BackgroundStack_j1pt->Add(TTFinal_j1pt,"hist");
  BackgroundStack_j1pt->Add(Other_j1pt,"hist");
  BackgroundStack_j1pt->Add(DYMM_j1pt,"hist");
  BackgroundStack_j1pt->Add(DYTT_j1pt,"hist");

  TH1F* BackgroundStack_j1pt_Errors = MakeStackErrors(BackgroundStack_j1pt);

  TPad* PlotPad_j1pt = MakeRatioPlot(CanvasThirteen,BackgroundStack_j1pt, Data_j1pt, "j1pt",0.7,1.3);
  PlotPad_j1pt->SetTickx();
  PlotPad_j1pt->SetTicky();

  BackgroundStack_j1pt->SetMaximum(max(BackgroundStack_j1pt->GetMaximum(),Data_j1pt->GetMaximum()));
  
  BackgroundStack_j1pt->Draw();
  BackgroundStack_j1pt_Errors->Draw("SAME e2");
  BackgroundStack_j1pt->SetTitle("j1pt");
  Data_j1pt->Draw("SAME e1");
  AllHiggs_j1pt->Draw("SAME HIST");
  BackgroundStack_j1pt->GetYaxis()->SetTitle("Events");
  BackgroundStack_j1pt->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_j1pt->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_j1pt,0,33);

  TLegend* Legend_j1pt = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_j1pt->AddEntry(Data_j1pt,"Observed","pe");
  Legend_j1pt->AddEntry(DYTT_j1pt,"Embedded","f");
  Legend_j1pt->AddEntry(Other_j1pt,"Other","f");
  Legend_j1pt->AddEntry(DYMM_j1pt,"DY #rightarrow ll","f");
  Legend_j1pt->AddEntry(TTFinal_j1pt,"t#bar{t}","f");
  Legend_j1pt->AddEntry(Data_Fake_j1pt,"Fakes","f");
  Legend_j1pt->AddEntry(AllHiggs_j1pt,"All Higgs (#times 30)","l");

  Legend_j1pt->Draw();
  CanvasThirteen->SaveAs("FinalPlots/j1pt.png");
  CanvasThirteen->SaveAs("FinalPlots/j1pt.pdf");

  //msv
  TCanvas* CanvasFourteen = new TCanvas("CanvasFourteen","msv",550,550);
  CanvasFourteen->SetTickx();
  CanvasFourteen->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data_msv = (TH1F*) HistoFile->Get("Data_2018_msv");
  TH1F* Data_Fake_msv = (TH1F*) HistoFile->Get("Fake_2018_msv");
  TH1F* DYTT_msv = (TH1F*) HistoFile->Get("Embedded_2018_genmatch_tt_msv");
  TH1F* DYMM_msv = (TH1F*) HistoFile->Get("DY_2018_genmatch_low_msv");
  TH1F* TTToHadronic_msv = (TH1F*) HistoFile->Get("TTToHadronic_2018_msv");
  TH1F* TTTo2L2Nu_msv = (TH1F*) HistoFile->Get("TTTo2L2Nu_2018_msv");
  TH1F* TTToSemiLeptonic_msv = (TH1F*) HistoFile->Get("TTToSemiLeptonic_2018_msv");  
  TH1F* WW_msv = (TH1F*) HistoFile->Get("WW_2018_msv");
  TH1F* WZ_msv = (TH1F*) HistoFile->Get("WZ_2018_msv");
  TH1F* ZZ_msv = (TH1F*) HistoFile->Get("ZZ_2018_msv");
  TH1F* ST_tW_top_msv = (TH1F*) HistoFile->Get("ST_tW_top_2018_msv");
  TH1F* ggH_msv = (TH1F*) HistoFile->Get("ggH_2018_msv");
  TH1F* VBF_msv = (TH1F*) HistoFile->Get("VBF_2018_msv");
  TH1F* WHPlus_msv = (TH1F*) HistoFile->Get("WHPlus_2018_msv");
  TH1F* WHMinus_msv = (TH1F*) HistoFile->Get("WHMinus_2018_msv");
  TH1F* ZH_msv = (TH1F*) HistoFile->Get("ZH_2018_msv");

  TH1F* TTFinal_msv = (TH1F*) TTToHadronic_msv->Clone();
  TTFinal_msv->Add(TTTo2L2Nu_msv);
  TTFinal_msv->Add(TTToSemiLeptonic_msv);

  TH1F* VVFinal_msv = (TH1F*) WW_msv->Clone();
  VVFinal_msv->Add(WZ_msv);
  VVFinal_msv->Add(ZZ_msv);
  VVFinal_msv->Add(ST_tW_top_msv);
  
  TH1F* VHFinal_msv = (TH1F*) WHPlus_msv->Clone();
  VHFinal_msv->Add(WHMinus_msv);
  VHFinal_msv->Add(ZH_msv);

  TH1F* Other_msv = (TH1F*) VHFinal_msv->Clone();
  Other_msv->Add(ggH_msv);
  Other_msv->Add(VBF_msv);
  Other_msv->Add(VVFinal_msv);

  TH1F* AllHiggs_msv = (TH1F*) VHFinal_msv->Clone();
  AllHiggs_msv->Add(ggH_msv);
  AllHiggs_msv->Add(VBF_msv);

  Data_msv->SetMarkerStyle(20);
  Data_msv->Sumw2();
  
  Data_Fake_msv->SetLineColor(kBlack);
  Data_Fake_msv->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT_msv->SetLineColor(kBlack);
  DYTT_msv->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM_msv->SetLineColor(kBlack);
  DYMM_msv->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal_msv->SetLineColor(kBlack);
  TTFinal_msv->SetFillColor(TColor::GetColor("#9999cc"));

  Other_msv->SetLineColor(kBlack);
  Other_msv->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs_msv->SetLineColor(kRed);
  AllHiggs_msv->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake_msv->Integral()<<std::endl;

  THStack* BackgroundStack_msv = new THStack("BackgroundStack_msv","BackgroundStack_msv");  
  BackgroundStack_msv->Add(Data_Fake_msv,"hist");
  BackgroundStack_msv->Add(TTFinal_msv,"hist");
  BackgroundStack_msv->Add(Other_msv,"hist");
  BackgroundStack_msv->Add(DYMM_msv,"hist");
  BackgroundStack_msv->Add(DYTT_msv,"hist");

  TH1F* BackgroundStack_msv_Errors = MakeStackErrors(BackgroundStack_msv);

  TPad* PlotPad_msv = MakeRatioPlot(CanvasFourteen,BackgroundStack_msv, Data_msv, "m_{tt}",0.7,1.3);
  PlotPad_msv->SetTickx();
  PlotPad_msv->SetTicky();

  BackgroundStack_msv->SetMaximum(max(BackgroundStack_msv->GetMaximum(),Data_msv->GetMaximum()));
  
  BackgroundStack_msv->Draw();
  BackgroundStack_msv_Errors->Draw("SAME e2");
  BackgroundStack_msv->SetTitle("m_{tt}");
  Data_msv->Draw("SAME e1");
  AllHiggs_msv->Draw("SAME HIST");
  BackgroundStack_msv->GetYaxis()->SetTitle("Events");
  BackgroundStack_msv->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack_msv->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad_msv,0,33);

  TLegend* Legend_msv = new TLegend(0.61,0.41,0.88,0.68);  
  Legend_msv->AddEntry(Data_msv,"Observed","pe");
  Legend_msv->AddEntry(DYTT_msv,"Embedded","f");
  Legend_msv->AddEntry(Other_msv,"Other","f");
  Legend_msv->AddEntry(DYMM_msv,"DY #rightarrow ll","f");
  Legend_msv->AddEntry(TTFinal_msv,"t#bar{t}","f");
  Legend_msv->AddEntry(Data_Fake_msv,"Fakes","f");
  Legend_msv->AddEntry(AllHiggs_msv,"All Higgs (#times 30)","l");

  Legend_msv->Draw();
  CanvasFourteen->SaveAs("FinalPlots/msv.png");
  CanvasFourteen->SaveAs("FinalPlots/msv.pdf");
}
