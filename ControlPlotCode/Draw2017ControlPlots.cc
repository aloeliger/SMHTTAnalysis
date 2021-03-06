#include "TROOT.h"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/CMS_lumi.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/tdrstyle.C"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeRatioPlot.cc"
#include "/afs/cern.ch/user/a/aloelige/private/ScriptsAndMacros/MakeStackErrors.cc"
#include <string>

void DrawControlPlot(string var, bool UseEmbedded,string axisLabel, bool isAntiIso)
{
  setTDRStyle();

  writeExtraText = true;
  extraText = "Preliminary";
  lumi_sqrtS = "41.5 fb^{-1}, 13 TeV";

  TFile* HistoFile;
  if(!UseEmbedded)
    {
      HistoFile = new TFile("TemporaryFiles/ControlRegion_2017_MC.root","READ");
    }
  else
    {
      HistoFile = new TFile("TemporaryFiles/ControlRegion_2017.root","READ");
    }

  TCanvas* Canvas = new TCanvas(("Canvas_"+var).c_str(),var.c_str(),550,550);
  Canvas->SetTickx();
  Canvas->SetTicky();

  gStyle->SetOptStat(0);
  TH1F* Data = (TH1F*) HistoFile->Get(("Data_2017_"+var).c_str());
  TH1F* Data_Fake;
  if (not isAntiIso) Data_Fake  = (TH1F*) HistoFile->Get(("Fake_2017_"+var).c_str());
  //TH1F* DYTT_MuPt = (TH1F*) HistoFile->Get("Embedded_2017_genmatch_tt_MuPt");
  TH1F* DYTT; 
  if(UseEmbedded) DYTT = (TH1F*) HistoFile->Get(("Embedded_2017_genmatch_tt_"+var).c_str());
  else DYTT = (TH1F*) HistoFile->Get(("DY_2017_genmatch_tt_"+var).c_str());
  TH1F* DYMM = (TH1F*) HistoFile->Get(("DY_2017_genmatch_low_"+var).c_str());
  TH1F* TTToHadronic = (TH1F*) HistoFile->Get(("TTToHadronic_2017_"+var).c_str());
  TH1F* TTTo2L2Nu = (TH1F*) HistoFile->Get(("TTTo2L2Nu_2017_"+var).c_str());
  TH1F* TTToSemiLeptonic = (TH1F*) HistoFile->Get(("TTToSemiLeptonic_2017_"+var).c_str());  
  TH1F* WW1L1Nu2Q = (TH1F*) HistoFile->Get(("WW1L1Nu2Q_2017_"+var).c_str());
  TH1F* WZ1L1Nu2Q = (TH1F*) HistoFile->Get(("WZ1L1Nu2Q_2017_"+var).c_str());
  TH1F* WZ2L2Q = (TH1F*) HistoFile->Get(("WZ2L2Q_2017_"+var).c_str());
  TH1F* WZ3L1Nu = (TH1F*) HistoFile->Get(("WZ3L1Nu_2017_"+var).c_str());
  TH1F* ZZ2L2Q = (TH1F*) HistoFile->Get(("ZZ2L2Q_2017_"+var).c_str());
  TH1F* ZZ4L = (TH1F*) HistoFile->Get(("ZZ4L_2017_"+var).c_str());
  TH1F* VV2L2Nu = (TH1F*) HistoFile->Get(("VV2L2Nu_2017_"+var).c_str());
  TH1F* ST_tW_top = (TH1F*) HistoFile->Get(("ST_tW_top_2017_"+var).c_str());
  TH1F* ggH = (TH1F*) HistoFile->Get(("ggH_2017_"+var).c_str());
  TH1F* VBF = (TH1F*) HistoFile->Get(("VBF_2017_"+var).c_str());
  TH1F* WHPlus = (TH1F*) HistoFile->Get(("WHPlus_2017_"+var).c_str());
  TH1F* WHMinus = (TH1F*) HistoFile->Get(("WHMinus_2017_"+var).c_str());
  TH1F* ZH = (TH1F*) HistoFile->Get(("ZH_2017_"+var).c_str());
  TH1F* GGHWW;
  TH1F* VBFHWW;
  TH1F* WHWW;
  TH1F* ZHWW;
  TH1F* GGZHWW;
  if (not isAntiIso)
    {
      GGHWW = (TH1F*) HistoFile->Get(("GGHWW_2017_"+var).c_str());
      VBFHWW = (TH1F*) HistoFile->Get(("VBFHWW_2017_"+var).c_str());
      WHWW = (TH1F*) HistoFile->Get(("WHWW_2017_"+var).c_str());
      ZHWW = (TH1F*) HistoFile->Get(("ZHWW_2017_"+var).c_str());
      GGZHWW = (TH1F*) HistoFile->Get(("GGZHWW_2017_"+var).c_str());
    }
  TH1F* W;
  if (isAntiIso) W  = (TH1F*) HistoFile->Get(("W_2017_"+var).c_str());

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
  if (not isAntiIso)
    {
      Other->Add(GGHWW);
      Other->Add(VBFHWW);
      Other->Add(WHWW);
      Other->Add(ZHWW);
    }

  TH1F* AllHiggs = (TH1F*) VHFinal->Clone();
  AllHiggs->Add(ggH);
  AllHiggs->Add(VBF);

  Data->SetMarkerStyle(20);
  Data->Sumw2();
  
  if(not isAntiIso)
    {
      Data_Fake->SetLineColor(kBlack);
      Data_Fake->SetFillColor(TColor::GetColor("#ffccff"));//FakesColor->GetNumber());
    }
  if (isAntiIso)
    {
      W->SetLineColor(kBlack);
      W->SetFillColor(TColor::GetColor("#ffccff"));
    }
    
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

  //std::cout<<"Fake Background Integral: "<<Data_Fake->Integral()<<std::endl;

  THStack* BackgroundStack = new THStack(("BackgroundStack_"+var).c_str(),("BackgroundStack_"+var).c_str());  
  if (not isAntiIso)
    {
      BackgroundStack->Add(Data_Fake,"hist");  
    }
  if (isAntiIso)
    {
      BackgroundStack->Add(W,"hist");
    }
  BackgroundStack->Add(TTFinal,"hist");
  BackgroundStack->Add(DYMM,"hist");
  BackgroundStack->Add(Other,"hist");
  BackgroundStack->Add(DYTT,"hist");  

  TH1F* BackgroundStack_Errors = MakeStackErrors(BackgroundStack);

  TPad* PlotPad = MakeRatioPlot(Canvas,BackgroundStack, Data, axisLabel.c_str(),0.5,1.5);
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

  TLegend* Legend = new TLegend(0.85,0.35,0.99,0.7);        
  Legend->AddEntry(Data,"Observed","pe");
  if (UseEmbedded) Legend->AddEntry(DYTT,"Embedded","f");
  else Legend->AddEntry(DYTT,"DY #rightarrow #tau#tau (MC)");
  Legend->AddEntry(Other,"Other","f");  
  Legend->AddEntry(DYMM,"DY #rightarrow ll","f");  
  Legend->AddEntry(TTFinal,"t#bar{t}","f");  
  if (not isAntiIso)
    {
      Legend->AddEntry(Data_Fake,"Fakes","f");
    }
  if (isAntiIso)
    {
      Legend->AddEntry(W,"W+Jets","f");
    }
  Legend->AddEntry(AllHiggs,"All Higgs (#times 30)","l");

  Legend->Draw();
  if(UseEmbedded)
    {
      Canvas->SaveAs(("FinalPlots/"+var+"_2017_Embedded.png").c_str());
      Canvas->SaveAs(("FinalPlots/"+var+"_2017_Embedded.pdf").c_str());
    }
  else
    {
      Canvas->SaveAs(("FinalPlots/"+var+"_2017_MC.png").c_str());
      Canvas->SaveAs(("FinalPlots/"+var+"_2017_MC.pdf").c_str());
    }

  //HistoFile->Close();
}

void Draw2017ControlPlots()
{
  bool UsingEmbedded = true;
  bool isAntiIso = false;

  DrawControlPlot("msv", UsingEmbedded, "m_{#tau#tau}",isAntiIso);

  DrawControlPlot("MuPt",UsingEmbedded,"#mu p_{t}",isAntiIso);
  DrawControlPlot("MuEta",UsingEmbedded,"#mu #eta",isAntiIso);
  DrawControlPlot("TauPt",UsingEmbedded, "#tau p_{t}",isAntiIso);
  DrawControlPlot("TauEta",UsingEmbedded,"#tau #eta",isAntiIso);
  DrawControlPlot("MT",UsingEmbedded,"Transverse Mass",isAntiIso);

  DrawControlPlot("mvis",UsingEmbedded,"m_{vis}",isAntiIso);
  DrawControlPlot("Njets",UsingEmbedded,"N_{jets}",isAntiIso);
  DrawControlPlot("HiggsPt",UsingEmbedded,"Higgs p_{t}",isAntiIso);
  DrawControlPlot("MET",UsingEmbedded,"MET",isAntiIso);
  DrawControlPlot("DR",UsingEmbedded,"#Delta r_{#mu,#tau}",isAntiIso);

  DrawControlPlot("mjj",UsingEmbedded,"m_{jj}",isAntiIso);
  DrawControlPlot("detajj",UsingEmbedded,"#Delta#eta_{jj}",isAntiIso);
  DrawControlPlot("j1pt",UsingEmbedded,"p_{t} j_{1}",isAntiIso);
  DrawControlPlot("j1eta",UsingEmbedded,"#eta j_{1}",isAntiIso);
  DrawControlPlot("j2pt",UsingEmbedded,"p_{t} j_{2}",isAntiIso);
  DrawControlPlot("j2eta",UsingEmbedded,"#eta j_{2}",isAntiIso);

  DrawControlPlot("METPhi",UsingEmbedded,"MET_{#phi}",isAntiIso);      
  DrawControlPlot("trigger",UsingEmbedded,"trigger",isAntiIso);  
}
