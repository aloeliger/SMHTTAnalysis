#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include <string>

void DrawControlPlot(string var, bool UseEmbedded,string axisLabel)
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "137.1 fb^{-1}, 13 TeV";
  
  TFile* HistoFile_2018;
  TFile* HistoFile_2017;
  TFile* HistoFile_2016;
  if(!UseEmbedded)
    {
      HistoFile_2018 = new TFile("TemporaryFiles/ControlRegion_2018_MC.root","READ");
      HistoFile_2017 = new TFile("TemporaryFiles/ControlRegion_2017_MC.root","READ");
      HistoFile_2016 = new TFile("TemporaryFiles/ControlRegion_2016_MC.root","READ");
    }
  else
    {
      HistoFile_2018 = new TFile("TemporaryFiles/ControlRegion_2018.root","READ");
      HistoFile_2017 = new TFile("TemporaryFiles/ControlRegion_2017.root","READ");
      HistoFile_2016 = new TFile("TemporaryFiles/ControlRegion_2016.root","READ");
    }

  TCanvas* Canvas = new TCanvas("Canvas",var.c_str(),550,550);
  Canvas->SetTickx();
  Canvas->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data = (TH1F*) HistoFile_2018->Get(("Data_2018_"+var).c_str());
  Data->Add((TH1F*)HistoFile_2017->Get(("Data_2017_"+var).c_str()));
  Data->Add((TH1F*)HistoFile_2016->Get(("Data_2016_"+var).c_str()));

  TH1F* Data_Fake = (TH1F*) HistoFile_2018->Get(("Fake_2018_"+var).c_str());
  Data_Fake->Add((TH1F*)HistoFile_2017->Get(("Fake_2017_"+var).c_str()));
  Data_Fake->Add((TH1F*)HistoFile_2016->Get(("Fake_2016_"+var).c_str()));

  TH1F* DYTT;
  if (UseEmbedded) 
    {
      DYTT = (TH1F*) HistoFile_2018->Get(("Embedded_2018_genmatch_tt_"+var).c_str());
      DYTT->Add((TH1F*)HistoFile_2017->Get(("Embedded_2017_genmatch_tt_"+var).c_str()));
      DYTT->Add((TH1F*)HistoFile_2016->Get(("Embedded_2016_genmatch_tt_"+var).c_str()));
    }
  else 
    {
      DYTT = (TH1F*) HistoFile_2018->Get(("DY_2018_genmatch_tt_"+var).c_str());
      DYTT->Add((TH1F*)HistoFile_2017->Get(("DY_2017_genmatch_tt_"+var).c_str()));
      DYTT->Add((TH1F*)HistoFile_2016->Get(("DY_2016_genmatch_tt_"+var).c_str()));
    }
  TH1F* DYMM = (TH1F*) HistoFile_2018->Get(("DY_2018_genmatch_low_"+var).c_str());
  DYMM->Add((TH1F*)HistoFile_2017->Get(("DY_2017_genmatch_low_"+var).c_str()));
  DYMM->Add((TH1F*)HistoFile_2016->Get(("DY_2016_genmatch_low_"+var).c_str()));

  TH1F* TTToHadronic = (TH1F*) HistoFile_2018->Get(("TTToHadronic_2018_"+var).c_str());
  TTToHadronic->Add((TH1F*)HistoFile_2017->Get(("TTToHadronic_2017_"+var).c_str()));
  TTToHadronic->Add((TH1F*)HistoFile_2016->Get(("TT_2016_"+var).c_str()));

  TH1F* TTTo2L2Nu = (TH1F*) HistoFile_2018->Get(("TTTo2L2Nu_2018_"+var).c_str());
  TTTo2L2Nu->Add((TH1F*)HistoFile_2017->Get(("TTTo2L2Nu_2017_"+var).c_str()));
  //TTTo2L2Nu->Add((TH1F*)HistoFile_2016->Get(("TTTo2L2Nu_2016_"+var).c_str()));

  TH1F* TTToSemiLeptonic = (TH1F*) HistoFile_2018->Get(("TTToSemiLeptonic_2018_"+var).c_str());  
  TTToSemiLeptonic->Add((TH1F*)HistoFile_2017->Get(("TTToSemiLeptonic_2017_"+var).c_str()));
  //TTToSemiLeptonic->Add((TH1F*)HistoFile_2016->Get(("TTToSemiLeptonic_2016_"+var).c_str()));

  TH1F* WW1L1Nu2Q = (TH1F*) HistoFile_2018->Get(("WW1L1Nu2Q_2018_"+var).c_str());
  WW1L1Nu2Q->Add((TH1F*)HistoFile_2017->Get(("WW1L1Nu2Q_2017_"+var).c_str()));
  WW1L1Nu2Q->Add((TH1F*)HistoFile_2016->Get(("WW1L1Nu2Q_2016_"+var).c_str()));

  TH1F* WZ1L1Nu2Q = (TH1F*) HistoFile_2018->Get(("WZ1L1Nu2Q_2018_"+var).c_str());
  WZ1L1Nu2Q->Add((TH1F*)HistoFile_2017->Get(("WZ1L1Nu2Q_2017_"+var).c_str()));
  WZ1L1Nu2Q->Add((TH1F*)HistoFile_2016->Get(("WZ1L1Nu2Q_2016_"+var).c_str()));

  TH1F* WZ2L2Q = (TH1F*) HistoFile_2018->Get(("WZ2L2Q_2018_"+var).c_str());
  WZ2L2Q->Add((TH1F*)HistoFile_2017->Get(("WZ2L2Q_2017_"+var).c_str()));
  WZ2L2Q->Add((TH1F*)HistoFile_2016->Get(("WZ2L2Q_2016_"+var).c_str()));

  TH1F* WZ3L1Nu = (TH1F*) HistoFile_2018->Get(("WZ3L1Nu_2018_"+var).c_str());
  WZ3L1Nu->Add((TH1F*)HistoFile_2017->Get(("WZ3L1Nu_2017_"+var).c_str()));
  WZ3L1Nu->Add((TH1F*)HistoFile_2016->Get(("WZ3L1Nu_2016_"+var).c_str()));

  TH1F* ZZ2L2Q = (TH1F*) HistoFile_2018->Get(("ZZ2L2Q_2018_"+var).c_str());
  ZZ2L2Q->Add((TH1F*)HistoFile_2017->Get(("ZZ2L2Q_2017_"+var).c_str()));
  ZZ2L2Q->Add((TH1F*)HistoFile_2016->Get(("ZZ2L2Q_2016_"+var).c_str()));

  TH1F* ZZ4L = (TH1F*) HistoFile_2018->Get(("ZZ4L_2018_"+var).c_str());
  ZZ4L->Add((TH1F*)HistoFile_2017->Get(("ZZ4L_2017_"+var).c_str()));
  ZZ4L->Add((TH1F*)HistoFile_2016->Get(("ZZ4L_2016_"+var).c_str()));

  TH1F* VV2L2Nu = (TH1F*) HistoFile_2018->Get(("VV2L2Nu_2018_"+var).c_str());
  VV2L2Nu->Add((TH1F*)HistoFile_2017->Get(("VV2L2Nu_2017_"+var).c_str()));
  VV2L2Nu->Add((TH1F*)HistoFile_2016->Get(("VV2L2Nu_2016_"+var).c_str()));

  TH1F* ST_tW_top = (TH1F*) HistoFile_2018->Get(("ST_tW_top_2018_"+var).c_str());
  ST_tW_top->Add((TH1F*)HistoFile_2017->Get(("ST_tW_top_2017_"+var).c_str()));
  ST_tW_top->Add((TH1F*)HistoFile_2016->Get(("ST_tW_top_2016_"+var).c_str()));

  TH1F* ggH = (TH1F*) HistoFile_2018->Get(("ggH_2018_"+var).c_str());
  ggH->Add((TH1F*)HistoFile_2017->Get(("ggH_2017_"+var).c_str()));
  ggH->Add((TH1F*)HistoFile_2016->Get(("ggH_2016_"+var).c_str()));

  TH1F* VBF = (TH1F*) HistoFile_2018->Get(("VBF_2018_"+var).c_str());
  VBF->Add((TH1F*)HistoFile_2017->Get(("VBF_2017_"+var).c_str()));
  VBF->Add((TH1F*)HistoFile_2016->Get(("VBF_2016_"+var).c_str()));

  TH1F* WHPlus = (TH1F*) HistoFile_2018->Get(("WHPlus_2018_"+var).c_str());
  WHPlus->Add((TH1F*)HistoFile_2017->Get(("WHPlus_2017_"+var).c_str()));
  WHPlus->Add((TH1F*)HistoFile_2016->Get(("WHPlus_2016_"+var).c_str()));

  TH1F* WHMinus = (TH1F*) HistoFile_2018->Get(("WHMinus_2018_"+var).c_str());
  WHMinus->Add((TH1F*)HistoFile_2017->Get(("WHMinus_2017_"+var).c_str()));
  WHMinus->Add((TH1F*)HistoFile_2016->Get(("WHMinus_2016_"+var).c_str()));

  TH1F* ZH = (TH1F*) HistoFile_2018->Get(("ZH_2018_"+var).c_str());
  ZH->Add((TH1F*)HistoFile_2017->Get(("ZH_2017_"+var).c_str()));
  ZH->Add((TH1F*)HistoFile_2016->Get(("ZH_2016_"+var).c_str()));

  TH1F* GGHWW = (TH1F*) HistoFile_2018->Get(("GGHWW_2018_"+var).c_str());
  GGHWW->Add((TH1F*)HistoFile_2017->Get(("GGHWW_2017_"+var).c_str()));
  GGHWW->Add((TH1F*)HistoFile_2016->Get(("GGHWW_2016_"+var).c_str()));

  TH1F* VBFHWW = (TH1F*) HistoFile_2018->Get(("VBFHWW_2018_"+var).c_str());
  VBFHWW->Add((TH1F*)HistoFile_2017->Get(("VBFHWW_2017_"+var).c_str()));
  VBFHWW->Add((TH1F*)HistoFile_2016->Get(("VBFHWW_2016_"+var).c_str()));

  TH1F* WHWW = (TH1F*) HistoFile_2018->Get(("WminusHWW_2018_"+var).c_str());
  WHWW->Add((TH1F*)HistoFile_2017->Get(("WminusHWW_2017_"+var).c_str()));
  WHWW->Add((TH1F*)HistoFile_2016->Get(("WminusHWW_2016_"+var).c_str()));
  WHWW->Add((TH1F*)HistoFile_2018->Get(("WplusHWW_2018_"+var).c_str()));
  WHWW->Add((TH1F*)HistoFile_2017->Get(("WplusHWW_2017_"+var).c_str()));
  WHWW->Add((TH1F*)HistoFile_2016->Get(("WplusHWW_2016_"+var).c_str()));

  TH1F* ZHWW = (TH1F*) HistoFile_2018->Get(("ZHWW_2018_"+var).c_str());
  ZHWW->Add((TH1F*)HistoFile_2017->Get(("ZHWW_2017_"+var).c_str()));
  ZHWW->Add((TH1F*)HistoFile_2016->Get(("ZHWW_2016_"+var).c_str()));

  TH1F* GGZHWW = (TH1F*) HistoFile_2018->Get(("GGZHWW_2018_"+var).c_str());
  GGZHWW->Add((TH1F*)HistoFile_2017->Get(("GGZHWW_2017_"+var).c_str()));
  GGZHWW->Add((TH1F*)HistoFile_2016->Get(("GGZHWW_2016_"+var).c_str()));
    

  TH1F* TTFinal = (TH1F*) TTToHadronic->Clone();
  TTFinal->Add(TTTo2L2Nu);
  TTFinal->Add(TTToSemiLeptonic);

  TH1F* VVFinal = (TH1F*) VV2L2Nu->Clone();
  VVFinal->Add(WZ1L1Nu2Q);
  VVFinal->Add(WZ2L2Q);
  VVFinal->Add(WZ3L1Nu);
  VVFinal->Add(ZZ2L2Q);
  VVFinal->Add(ZZ4L);  
  VVFinal->Add(WW1L1Nu2Q);
  
  TH1F* VHFinal = (TH1F*) WHPlus->Clone();
  VHFinal->Add(WHMinus);
  VHFinal->Add(ZH);

  TH1F* Other = (TH1F*) VHFinal->Clone();
  Other->Add(ggH);
  Other->Add(VBF);
  Other->Add(VHFinal);
  Other->Add(VVFinal);
  Other->Add(GGHWW);
  Other->Add(VBFHWW);
  Other->Add(WHWW);
  Other->Add(ZHWW);

  TH1F* AllHiggs = (TH1F*) VHFinal->Clone();
  AllHiggs->Add(ggH);
  AllHiggs->Add(VBF);

  Data->SetMarkerStyle(20);
  Data->Sumw2();
  
  Data_Fake->SetLineColor(kBlack);
  Data_Fake->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    
  DYTT->SetLineColor(kBlack);
  DYTT->SetFillColor(TColor::GetColor("#ffcc66"));

  DYMM->SetLineColor(kBlack);
  DYMM->SetFillColor(TColor::GetColor("#4496c8"));
  
  TTFinal->SetLineColor(kBlack);
  TTFinal->SetFillColor(TColor::GetColor("#9999cc"));

  Other->SetLineColor(kBlack);
  Other->SetFillColor(TColor::GetColor("#12cadd"));
  
  AllHiggs->SetLineColor(kRed);
  AllHiggs->Scale(30);

  std::cout<<"Fake Background Integral: "<<Data_Fake->Integral()<<std::endl;

  THStack* BackgroundStack = new THStack("BackgroundStack","BackgroundStack");  
  BackgroundStack->Add(Data_Fake,"hist");  
  BackgroundStack->Add(TTFinal,"hist");
  BackgroundStack->Add(DYMM,"hist");
  BackgroundStack->Add(Other,"hist");
  BackgroundStack->Add(DYTT,"hist");  

  TH1F* BackgroundStack_Errors = MakeStackErrors(BackgroundStack);

  TPad* PlotPad = MakeRatioPlot(Canvas,BackgroundStack, Data, axisLabel,0.5,1.5);
  PlotPad->SetTickx();
  PlotPad->SetTicky();

  BackgroundStack->SetMaximum(max(BackgroundStack->GetMaximum(),Data->GetMaximum()));
  
  BackgroundStack->Draw();
  BackgroundStack_Errors->Draw("SAME e2");
  BackgroundStack->SetTitle(axisLabel.c_str());
  Data->Draw("SAME e1");
  AllHiggs->Draw("SAME HIST");
  BackgroundStack->GetYaxis()->SetTitle("Events");
  BackgroundStack->GetYaxis()->SetTitleOffset(1.58);
  BackgroundStack->GetXaxis()->SetLabelSize(0.0);

  CMS_lumi(PlotPad,0,33);

  TLegend* Legend = new TLegend(0.61,0.41,0.88,0.68);        
  Legend->AddEntry(Data,"Observed","pe");
  Legend->AddEntry(DYTT,"Embedded","f");
  Legend->AddEntry(Other,"Other","f");  
  Legend->AddEntry(DYMM,"DY #rightarrow ll","f");  
  Legend->AddEntry(TTFinal,"t#bar{t}","f");  
  Legend->AddEntry(Data_Fake,"Fakes","f");
  Legend->AddEntry(AllHiggs,"All Higgs (#times 30)","l");

  Legend->Draw();
  if(UseEmbedded)
    {
      Canvas->SaveAs(("FinalPlots/"+var+"_Run2_Embedded.png").c_str());
      Canvas->SaveAs(("FinalPlots/"+var+"_Run2_Embedded.pdf").c_str());
    }
  else
    {
      Canvas->SaveAs(("FinalPlots/"+var+"_Run2_MC.png").c_str());
      Canvas->SaveAs(("FinalPlots/"+var+"_Run2_MC.pdf").c_str());
    }
  
  //HistoFile->Close();
}

void DrawRun2ControlPlots()
{  

  bool UsingEmbedded = true;

  DrawControlPlot("msv", UsingEmbedded, "m_{#tau#tau}");

  DrawControlPlot("MuPt",UsingEmbedded,"#mu p_{t}");
  DrawControlPlot("MuEta",UsingEmbedded,"#mu #eta");
  DrawControlPlot("TauPt",UsingEmbedded, "#tau p_{t}");
  DrawControlPlot("TauEta",UsingEmbedded,"#tau #eta");
  DrawControlPlot("MT",UsingEmbedded,"Transverse Mass");

  DrawControlPlot("mvis",UsingEmbedded,"m_{vis}");
  DrawControlPlot("Njets",UsingEmbedded,"N_{jets}");
  DrawControlPlot("HiggsPt",UsingEmbedded,"Higgs p_{t}");
  DrawControlPlot("MET",UsingEmbedded,"MET");
  DrawControlPlot("DR",UsingEmbedded,"#Delta r_{#mu,#tau}");

  DrawControlPlot("mjj",UsingEmbedded,"m_{jj}");
  DrawControlPlot("detajj",UsingEmbedded,"#Delta#eta_{jj}");
  DrawControlPlot("j1pt",UsingEmbedded,"p_{t} j_{1}");
  DrawControlPlot("j1eta",UsingEmbedded,"#eta j_{1}");
  DrawControlPlot("j2pt",UsingEmbedded,"p_{t} j_{2}");
  DrawControlPlot("j2eta",UsingEmbedded,"#eta j_{2}");

  DrawControlPlot("METPhi",UsingEmbedded,"MET_{#phi}");      
  //DrawControlPlot("trigger",UsingEmbedded,"trigger");  
}
