import ROOT
import sys

TheHistoFile = ROOT.TFile("JetFile.root","UPDATE")

TheFinalJetDistribution = ROOT.TH1F("FinalJetDistribution","FinalJetDistribution",
                                    20, 50.0, 150.0)

TheFinalJetDistribution.Add(TheHistoFile.TightJetDistribution,1.0)
TheFinalJetDistribution.Add(TheHistoFile.DYJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.DY1JetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.DY2JetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.DY3JetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.DY4JetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.TTTo2L2NuJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.TTToSemiLeptonicJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.TTToHadronicJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.WWJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.ZZJetDistribution,-1.0)
TheFinalJetDistribution.Add(TheHistoFile.WZJetDistribution,-1.0)

print("TightJetHisto: "+str(TheHistoFile.TightJetDistribution.Integral()))
print("DYJetDistribution: "+str(TheHistoFile.DYJetDistribution.Integral()))
print("DY1JetDistribution: "+str(TheHistoFile.DY1JetDistribution.Integral()))
print("DY2JetDistribution: "+str(TheHistoFile.DY2JetDistribution.Integral()))
print("DY3JetDistribution: "+str(TheHistoFile.DY3JetDistribution.Integral()))
print("DY4JetDistribution: "+str(TheHistoFile.DY4JetDistribution.Integral()))
print("TTTo2L2LNuJetDistribution: "+str(TheHistoFile.TTTo2L2NuJetDistribution.Integral()))
print("TTToSemiLeptonicJetDistribution: "+str(TheHistoFile.TTToSemiLeptonicJetDistribution.Integral()))
print("TTToHadronicJetDistribution: "+str(TheHistoFile.TTToHadronicJetDistribution.Integral()))
print("WWJetDistribution: "+str(TheHistoFile.WWJetDistribution.Integral()))
print("ZZJetDistribution: "+str(TheHistoFile.ZZJetDistribution.Integral()))
print("WZJetDistribution: "+str(TheHistoFile.WZJetDistribution.Integral()))
#print("Data - MC: "+str())

TheFinalJetDistribution.Write()
TheHistoFile.Close()
