import ROOT
import sys

ROOT.gStyle.SetOptStat(0)

TheNewHistoFile = ROOT.TFile("JetFile.root")
TheNewJetHisto = TheNewHistoFile.TightJetDistribution

TheOldHistoFile = ROOT.TFile("FakeRateDeterminedDistributions.root")
TheOldJetHisto = TheOldHistoFile.TightPTFRJetDistribution

TheCanvas = ROOT.TCanvas("c1")

TheNewJetHisto.SetLineColor(ROOT.kRed)
TheOldJetHisto.SetLineColor(ROOT.kBlue)

TheLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
TheLegend.AddEntry(TheNewJetHisto,"Fake Factor Method", "l")
TheLegend.AddEntry(TheOldJetHisto, "Tau ID Fake Rate Method", "l")

TheNewJetHisto.GetXaxis().SetTitle("m_{vis}")
TheNewJetHisto.SetMaximum(max(TheNewJetHisto.GetMaximum(),TheOldJetHisto.GetMaximum())*1.10)

TheNewJetHisto.Draw()
TheOldJetHisto.Draw("SAME")

TheLegend.Draw()
raw_input("Press Enter To Continue...")
