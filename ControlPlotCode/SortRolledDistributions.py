import ROOT
import UnrollDistributions

TheFile = ROOT.TFile("CecileCode/Results.root")
OutFile = ROOT.TFile("CombineWorkSpaceFile-2D.root","RECREATE")

#collect and name the 0jet 1D Category
ZeroJet_data_obs_Rolled = TheFile.mt_0jet.Get("data_obs_0jet_Results_Rolled")

ZeroJet_Fakes_Rolled = TheFile.mt_0jet.Get("data_obs_0jet_Fake_Results_Rolled")

ZeroJet_ZTauTau_Rolled = TheFile.mt_0jet.Get("embedded_0jet_Results_Rolled")

ZeroJet_ZToLeptons_Rolled = TheFile.mt_0jet.Get("DY_0jet_Results_Rolled")
ZeroJet_ZToLeptons_Rolled.Add(TheFile.mt_0jet.Get("DYlow_0jet_Results_Rolled"))

ZeroJet_TT_Rolled = TheFile.mt_0jet.Get("TTToHadronic_0jet_Results_Rolled")
ZeroJet_TT_Rolled.Add(TheFile.mt_0jet.Get("TTTo2L2Nu_0jet_Results_Rolled"))
ZeroJet_TT_Rolled.Add(TheFile.mt_0jet.Get("TTToSemiLeptonic_0jet_Results_Rolled"))

ZeroJet_Diboson_Rolled = TheFile.mt_0jet.Get("WW4Q_0jet_Results_Rolled")
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("WWLNuQQ_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("WZ2L2Q_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("WZ1L3Nu_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("WZ3LNu_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("WZ1L1Nu2Q_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("ZZ4L_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("ZZ2L2Nu_0jet_Results_Rolled"))
ZeroJet_Diboson_Rolled.Add(TheFile.mt_0jet.Get("ZZ2L2Q_0jet_Results_Rolled"))

ZeroJet_SingleTop_Rolled = TheFile.mt_0jet.Get("ST_t_antitop_0jet_Results_Rolled")
ZeroJet_SingleTop_Rolled.Add(TheFile.mt_0jet.Get("ST_t_top_0jet_Results_Rolled"))
ZeroJet_SingleTop_Rolled.Add(TheFile.mt_0jet.Get("ST_tW_antitop_0jet_Results_Rolled"))
ZeroJet_SingleTop_Rolled.Add(TheFile.mt_0jet.Get("ST_tW_top_0jet_Results_Rolled"))
#Temporary?
ZeroJet_Diboson_Rolled.Add(ZeroJet_SingleTop_Rolled)

ZeroJet_EWK_Rolled = TheFile.mt_0jet.Get("EWKZLL_0jet_Results_Rolled")
ZeroJet_EWK_Rolled.Add(TheFile.mt_0jet.Get("EWKZNuNu_0jet_Results_Rolled"))

ZeroJet_ggH_htt_Rolled = TheFile.mt_0jet.Get("ggH_htt125_0jet_Results_Rolled")

ZeroJet_qqH_htt_Rolled = TheFile.mt_0jet.Get("qqH_htt125_0jet_Results_Rolled")

ZeroJet_WH_htt_Rolled = TheFile.mt_0jet.Get("WplusH125_0jet_Results_Rolled")
ZeroJet_WH_htt_Rolled.Add(TheFile.mt_0jet.Get("WminusH125_0jet_Results_Rolled"))

ZeroJet_ZH_htt_Rolled = TheFile.mt_0jet.Get("ZH125_0jet_Results_Rolled")

ZeroJet_Other_Rolled = ZeroJet_Diboson_Rolled.Clone()
ZeroJet_Other_Rolled.Add(ZeroJet_EWK_Rolled)
ZeroJet_Other_Rolled.Add(ZeroJet_ggH_htt_Rolled)
ZeroJet_Other_Rolled.Add(ZeroJet_qqH_htt_Rolled)
ZeroJet_Other_Rolled.Add(ZeroJet_WH_htt_Rolled)
ZeroJet_Other_Rolled.Add(ZeroJet_ZH_htt_Rolled)

#Boosted
Boosted_data_obs_Rolled = TheFile.mt_boosted.Get("data_obs_boosted_Results_Rolled")

Boosted_Fakes_Rolled = TheFile.mt_boosted.Get("data_obs_boosted_Fake_Results_Rolled")

Boosted_ZTauTau_Rolled = TheFile.mt_boosted.Get("embedded_boosted_Results_Rolled")

Boosted_ZToLeptons_Rolled = TheFile.mt_boosted.Get("DY_boosted_Results_Rolled")
Boosted_ZToLeptons_Rolled.Add(TheFile.mt_boosted.Get("DYlow_boosted_Results_Rolled"))

Boosted_TT_Rolled = TheFile.mt_boosted.Get("TTToHadronic_boosted_Results_Rolled")
Boosted_TT_Rolled.Add(TheFile.mt_boosted.Get("TTTo2L2Nu_boosted_Results_Rolled"))
Boosted_TT_Rolled.Add(TheFile.mt_boosted.Get("TTToSemiLeptonic_boosted_Results_Rolled"))

Boosted_Diboson_Rolled = TheFile.mt_boosted.Get("WW4Q_boosted_Results_Rolled")
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("WWLNuQQ_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("WZ2L2Q_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("WZ1L3Nu_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("WZ3LNu_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("WZ1L1Nu2Q_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("ZZ4L_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("ZZ2L2Nu_boosted_Results_Rolled"))
Boosted_Diboson_Rolled.Add(TheFile.mt_boosted.Get("ZZ2L2Q_boosted_Results_Rolled"))

Boosted_SingleTop_Rolled = TheFile.mt_boosted.Get("ST_t_antitop_boosted_Results_Rolled")
Boosted_SingleTop_Rolled.Add(TheFile.mt_boosted.Get("ST_t_top_boosted_Results_Rolled"))
Boosted_SingleTop_Rolled.Add(TheFile.mt_boosted.Get("ST_tW_antitop_boosted_Results_Rolled"))
Boosted_SingleTop_Rolled.Add(TheFile.mt_boosted.Get("ST_tW_top_boosted_Results_Rolled"))
#Temporary?
Boosted_Diboson_Rolled.Add(Boosted_SingleTop_Rolled)

Boosted_EWK_Rolled = TheFile.mt_boosted.Get("EWKZLL_boosted_Results_Rolled")
Boosted_EWK_Rolled.Add(TheFile.mt_boosted.Get("EWKZNuNu_boosted_Results_Rolled"))

Boosted_ggH_htt_Rolled = TheFile.mt_boosted.Get("ggH_htt125_boosted_Results_Rolled")

Boosted_qqH_htt_Rolled = TheFile.mt_boosted.Get("qqH_htt125_boosted_Results_Rolled")

Boosted_WH_htt_Rolled = TheFile.mt_boosted.Get("WplusH125_boosted_Results_Rolled")
Boosted_WH_htt_Rolled.Add(TheFile.mt_boosted.Get("WminusH125_boosted_Results_Rolled"))

Boosted_ZH_htt_Rolled = TheFile.mt_boosted.Get("ZH125_boosted_Results_Rolled")

Boosted_Other_Rolled = Boosted_Diboson_Rolled.Clone()
Boosted_Other_Rolled.Add(Boosted_EWK_Rolled)
Boosted_Other_Rolled.Add(Boosted_ggH_htt_Rolled)
Boosted_Other_Rolled.Add(Boosted_qqH_htt_Rolled)
Boosted_Other_Rolled.Add(Boosted_WH_htt_Rolled)
Boosted_Other_Rolled.Add(Boosted_ZH_htt_Rolled)

#VBF
VBF_data_obs_Rolled = TheFile.mt_vbf.Get("data_obs_vbf_Results_Rolled")

VBF_Fakes_Rolled = TheFile.mt_vbf.Get("data_obs_vbf_Fake_Results_Rolled")

VBF_ZTauTau_Rolled = TheFile.mt_vbf.Get("embedded_vbf_Results_Rolled")

VBF_ZToLeptons_Rolled = TheFile.mt_vbf.Get("DY_vbf_Results_Rolled")
VBF_ZToLeptons_Rolled.Add(TheFile.mt_vbf.Get("DYlow_vbf_Results_Rolled"))

VBF_TT_Rolled = TheFile.mt_vbf.Get("TTToHadronic_vbf_Results_Rolled")
VBF_TT_Rolled.Add(TheFile.mt_vbf.Get("TTTo2L2Nu_vbf_Results_Rolled"))
VBF_TT_Rolled.Add(TheFile.mt_vbf.Get("TTToSemiLeptonic_vbf_Results_Rolled"))

VBF_Diboson_Rolled = TheFile.mt_vbf.Get("WW4Q_vbf_Results_Rolled")
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("WWLNuQQ_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("WZ2L2Q_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("WZ1L3Nu_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("WZ3LNu_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("WZ1L1Nu2Q_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("ZZ4L_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("ZZ2L2Nu_vbf_Results_Rolled"))
VBF_Diboson_Rolled.Add(TheFile.mt_vbf.Get("ZZ2L2Q_vbf_Results_Rolled"))

VBF_SingleTop_Rolled = TheFile.mt_vbf.Get("ST_t_antitop_vbf_Results_Rolled")
VBF_SingleTop_Rolled.Add(TheFile.mt_vbf.Get("ST_t_top_vbf_Results_Rolled"))
VBF_SingleTop_Rolled.Add(TheFile.mt_vbf.Get("ST_tW_antitop_vbf_Results_Rolled"))
VBF_SingleTop_Rolled.Add(TheFile.mt_vbf.Get("ST_tW_top_vbf_Results_Rolled"))
#Temporary?
VBF_Diboson_Rolled.Add(VBF_SingleTop_Rolled)

VBF_EWK_Rolled = TheFile.mt_vbf.Get("EWKZLL_vbf_Results_Rolled")
VBF_EWK_Rolled.Add(TheFile.mt_vbf.Get("EWKZNuNu_vbf_Results_Rolled"))

VBF_ggH_htt_Rolled = TheFile.mt_vbf.Get("ggH_htt125_vbf_Results_Rolled")

VBF_qqH_htt_Rolled = TheFile.mt_vbf.Get("qqH_htt125_vbf_Results_Rolled")

VBF_WH_htt_Rolled = TheFile.mt_vbf.Get("WplusH125_vbf_Results_Rolled")
VBF_WH_htt_Rolled.Add(TheFile.mt_vbf.Get("WminusH125_vbf_Results_Rolled"))

VBF_ZH_htt_Rolled = TheFile.mt_vbf.Get("ZH125_vbf_Results_Rolled")

VBF_Other_Rolled = VBF_Diboson_Rolled.Clone()
VBF_Other_Rolled.Add(VBF_EWK_Rolled)
VBF_Other_Rolled.Add(VBF_ggH_htt_Rolled)
VBF_Other_Rolled.Add(VBF_qqH_htt_Rolled)
VBF_Other_Rolled.Add(VBF_WH_htt_Rolled)
VBF_Other_Rolled.Add(VBF_ZH_htt_Rolled)

#Create unrolled distributions
ZeroJet_data_obs = UnrollDistributions.Unroll(ZeroJet_data_obs_Rolled)
ZeroJet_Fakes = UnrollDistributions.Unroll(ZeroJet_Fakes_Rolled)
ZeroJet_ZTauTau = UnrollDistributions.Unroll(ZeroJet_ZTauTau_Rolled)
ZeroJet_ZToLeptons = UnrollDistributions.Unroll(ZeroJet_ZToLeptons_Rolled)
ZeroJet_TT = UnrollDistributions.Unroll(ZeroJet_TT_Rolled)
ZeroJet_Diboson = UnrollDistributions.Unroll(ZeroJet_Diboson_Rolled)
ZeroJet_ggH_htt = UnrollDistributions.Unroll(ZeroJet_ggH_htt_Rolled)
ZeroJet_qqH_htt = UnrollDistributions.Unroll(ZeroJet_qqH_htt_Rolled)
ZeroJet_WH_htt = UnrollDistributions.Unroll(ZeroJet_WH_htt_Rolled)
ZeroJet_ZH_htt = UnrollDistributions.Unroll(ZeroJet_ZH_htt_Rolled)
ZeroJet_EWK = UnrollDistributions.Unroll(ZeroJet_EWK_Rolled)
ZeroJet_Other = UnrollDistributions.Unroll(ZeroJet_Other_Rolled)

ZeroJet_Higgs_Upscale = ZeroJet_ggH_htt.Clone()
ZeroJet_Higgs_Upscale.Add(ZeroJet_qqH_htt)
ZeroJet_Higgs_Upscale.Add(ZeroJet_WH_htt)
ZeroJet_Higgs_Upscale.Add(ZeroJet_ZH_htt)
ZeroJet_Higgs_Upscale.SetNameTitle("Higgs_Upscale","Higgs_Upscale")
ZeroJet_Higgs_Upscale.SetLineColor(ROOT.kRed)
ZeroJet_Higgs_Upscale.SetLineWidth(2)
ZeroJet_Higgs_Upscale.Scale(30)

ZeroJet_data_obs.SetNameTitle("data_obs","data_obs")
ZeroJet_Fakes.SetNameTitle("jetFakes","jetFakes")
ZeroJet_ZTauTau.SetNameTitle("ZTT","ZTT")
ZeroJet_ZToLeptons.SetNameTitle("ZL","ZL")
ZeroJet_TT.SetNameTitle("TTT","TTT")
ZeroJet_Diboson.SetNameTitle("VVT","VVT")
ZeroJet_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")
ZeroJet_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")
ZeroJet_WH_htt.SetNameTitle("WH_htt125","WH_htt")
ZeroJet_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")
ZeroJet_EWK.SetNameTitle("EWKZ","EWKZ")
ZeroJet_Other.SetNameTitle("Other","Other")

Boosted_data_obs = UnrollDistributions.Unroll(Boosted_data_obs_Rolled)
Boosted_Fakes = UnrollDistributions.Unroll(Boosted_Fakes_Rolled)
Boosted_ZTauTau = UnrollDistributions.Unroll(Boosted_ZTauTau_Rolled)
Boosted_ZToLeptons = UnrollDistributions.Unroll(Boosted_ZToLeptons_Rolled)
Boosted_TT = UnrollDistributions.Unroll(Boosted_TT_Rolled)
Boosted_Diboson = UnrollDistributions.Unroll(Boosted_Diboson_Rolled)
Boosted_ggH_htt = UnrollDistributions.Unroll(Boosted_ggH_htt_Rolled)
Boosted_qqH_htt = UnrollDistributions.Unroll(Boosted_qqH_htt_Rolled)
Boosted_WH_htt = UnrollDistributions.Unroll(Boosted_WH_htt_Rolled)
Boosted_ZH_htt = UnrollDistributions.Unroll(Boosted_ZH_htt_Rolled)
Boosted_EWK = UnrollDistributions.Unroll(Boosted_EWK_Rolled)
Boosted_Other = UnrollDistributions.Unroll(Boosted_Other_Rolled)

Boosted_Higgs_Upscale = Boosted_ggH_htt.Clone()
Boosted_Higgs_Upscale.Add(Boosted_qqH_htt)
Boosted_Higgs_Upscale.Add(Boosted_WH_htt)
Boosted_Higgs_Upscale.Add(Boosted_ZH_htt)
Boosted_Higgs_Upscale.SetNameTitle("Higgs_Upscale","Higgs_Upscale")
Boosted_Higgs_Upscale.SetLineColor(ROOT.kRed)
Boosted_Higgs_Upscale.SetLineWidth(2)
Boosted_Higgs_Upscale.Scale(30)

Boosted_data_obs.SetNameTitle("data_obs","data_obs")
Boosted_Fakes.SetNameTitle("jetFakes","jetFakes")
Boosted_ZTauTau.SetNameTitle("ZTT","ZTT")
Boosted_ZToLeptons.SetNameTitle("ZL","ZL")
Boosted_TT.SetNameTitle("TTT","TTT")
Boosted_Diboson.SetNameTitle("VVT","VVT")
Boosted_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")
Boosted_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")
Boosted_WH_htt.SetNameTitle("WH_htt125","WH_htt")
Boosted_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")
Boosted_EWK.SetNameTitle("EWKZ","EWKZ")
Boosted_Other.SetNameTitle("Other","Other")

VBF_data_obs = UnrollDistributions.Unroll(VBF_data_obs_Rolled)
VBF_Fakes = UnrollDistributions.Unroll(VBF_Fakes_Rolled)
VBF_ZTauTau = UnrollDistributions.Unroll(VBF_ZTauTau_Rolled)
VBF_ZToLeptons = UnrollDistributions.Unroll(VBF_ZToLeptons_Rolled)
VBF_TT = UnrollDistributions.Unroll(VBF_TT_Rolled)
VBF_Diboson = UnrollDistributions.Unroll(VBF_Diboson_Rolled)
VBF_ggH_htt = UnrollDistributions.Unroll(VBF_ggH_htt_Rolled)
VBF_qqH_htt = UnrollDistributions.Unroll(VBF_qqH_htt_Rolled)
VBF_WH_htt = UnrollDistributions.Unroll(VBF_WH_htt_Rolled)
VBF_ZH_htt = UnrollDistributions.Unroll(VBF_ZH_htt_Rolled)
VBF_EWK = UnrollDistributions.Unroll(VBF_EWK_Rolled)
VBF_Other = UnrollDistributions.Unroll(VBF_Other_Rolled)

VBF_Higgs_Upscale = VBF_ggH_htt.Clone()
VBF_Higgs_Upscale.Add(VBF_qqH_htt)
VBF_Higgs_Upscale.Add(VBF_WH_htt)
VBF_Higgs_Upscale.Add(VBF_ZH_htt)
VBF_Higgs_Upscale.SetNameTitle("Higgs_Upscale","Higgs_Upscale")
VBF_Higgs_Upscale.SetLineColor(ROOT.kRed)
VBF_Higgs_Upscale.SetLineWidth(2)
VBF_Higgs_Upscale.Scale(30)

VBF_data_obs.SetNameTitle("data_obs","data_obs")
VBF_Fakes.SetNameTitle("jetFakes","jetFakes")
VBF_ZTauTau.SetNameTitle("ZTT","ZTT")
VBF_ZToLeptons.SetNameTitle("ZL","ZL")
VBF_TT.SetNameTitle("TTT","TTT")
VBF_Diboson.SetNameTitle("VVT","VVT")
VBF_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")
VBF_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")
VBF_WH_htt.SetNameTitle("WH_htt125","WH_htt")
VBF_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")
VBF_EWK.SetNameTitle("EWKZ","EWKZ")
VBF_Other.SetNameTitle("Other","Other")

#write the combine File
OutFile.cd()

ZeroJetDir = OutFile.mkdir("mt_0jet")
ZeroJetDir.cd()
ZeroJet_data_obs.Write()
ZeroJet_Fakes.Write()
ZeroJet_ZTauTau.Write()
ZeroJet_ZToLeptons.Write()
ZeroJet_TT.Write()
ZeroJet_Diboson.Write()
ZeroJet_ggH_htt.Write()
ZeroJet_qqH_htt.Write()
ZeroJet_WH_htt.Write()
ZeroJet_ZH_htt.Write()
ZeroJet_EWK.Write()

BoostedDir = OutFile.mkdir("mt_boosted")
BoostedDir.cd()
Boosted_data_obs.Write()
Boosted_Fakes.Write()
Boosted_ZTauTau.Write()
Boosted_ZToLeptons.Write()
Boosted_TT.Write()
Boosted_Diboson.Write()
Boosted_ggH_htt.Write()
Boosted_qqH_htt.Write()
Boosted_WH_htt.Write()
Boosted_ZH_htt.Write()
Boosted_EWK.Write()

VBFDir = OutFile.mkdir("mt_vbf")
VBFDir.cd()
VBF_data_obs.Write()
VBF_Fakes.Write()
VBF_ZTauTau.Write()
VBF_ZToLeptons.Write()
VBF_TT.Write()
VBF_Diboson.Write()
VBF_ggH_htt.Write()
VBF_qqH_htt.Write()
VBF_WH_htt.Write()
VBF_ZH_htt.Write()
VBF_EWK.Write()

OutFile.Write()

#Create a stack and toss all of our backgrounds into it
#zero jet
ZeroJetBackgroundStack = ROOT.THStack("ZeroJetBackgroundStack","ZeroJetBackgroundStack")
ZeroJet_data_obs.SetMarkerStyle(20)

ZeroJet_Fakes.SetLineColor(ROOT.kBlack)
ZeroJet_Fakes.SetFillColor(ROOT.TColor.GetColor("#ffccff"))

ZeroJet_ZTauTau.SetLineColor(ROOT.kBlack)
ZeroJet_ZTauTau.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))

ZeroJet_ZToLeptons.SetLineColor(ROOT.kBlack)
ZeroJet_ZToLeptons.SetFillColor(ROOT.TColor.GetColor("#4496c8"))

ZeroJet_TT.SetLineColor(ROOT.kBlack)
ZeroJet_TT.SetFillColor(ROOT.TColor.GetColor("#9999cc"))

ZeroJet_Diboson.SetLineColor(ROOT.kBlack)
ZeroJet_Diboson.SetFillColor(ROOT.kOrange)

ZeroJet_ggH_htt.SetLineColor(ROOT.kBlack)
ZeroJet_ggH_htt.SetFillColor(ROOT.kCyan)

ZeroJet_qqH_htt.SetLineColor(ROOT.kBlack)
ZeroJet_qqH_htt.SetFillColor(ROOT.kGreen)

ZeroJet_WH_htt.SetLineColor(ROOT.kBlack)
ZeroJet_WH_htt.SetFillColor(ROOT.kPink+6)

ZeroJet_ZH_htt.SetLineColor(ROOT.kBlack)
ZeroJet_ZH_htt.SetFillColor(ROOT.kGreen+3)

ZeroJet_EWK.SetLineColor(ROOT.kBlack)
ZeroJet_EWK.SetFillColor(ROOT.kBlue-2)

ZeroJet_Other.SetLineColor(ROOT.kBlack)
ZeroJet_Other.SetFillColor(ROOT.TColor.GetColor("#12cadd"))

ZeroJetBackgroundStack.Add(ZeroJet_Fakes,"hist")
ZeroJetBackgroundStack.Add(ZeroJet_ZTauTau,"hist")
ZeroJetBackgroundStack.Add(ZeroJet_ZToLeptons,"hist")
ZeroJetBackgroundStack.Add(ZeroJet_TT,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_Diboson,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_ggH_htt,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_qqH_htt,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_WH_htt,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_ZH_htt,"hist")
#ZeroJetBackgroundStack.Add(ZeroJet_EWK,"hist")
ZeroJetBackgroundStack.Add(ZeroJet_Other,"hist")

#Create the legend we're going to use
ZeroJetLegend = ROOT.TLegend(0.72,0.40,0.87,0.70)
#ZeroJetLegend.AddEntry(ZeroJet_EWK,"EWK","f")
#ZeroJetLegend.AddEntry(ZeroJet_ZH_htt,"ZH","f")
#ZeroJetLegend.AddEntry(ZeroJet_WH_htt,"WH","f")
#ZeroJetLegend.AddEntry(ZeroJet_qqH_htt,"qqH","f")
#ZeroJetLegend.AddEntry(ZeroJet_ggH_htt,"ggH","f")
#ZeroJetLegend.AddEntry(ZeroJet_Diboson,"VV+ST","f")
ZeroJetLegend.AddEntry(ZeroJet_Other,"Other","f")
ZeroJetLegend.AddEntry(ZeroJet_TT,"t#bar{t}","f")
ZeroJetLegend.AddEntry(ZeroJet_ZToLeptons,"Z#rightarrow ll","f")
ZeroJetLegend.AddEntry(ZeroJet_ZTauTau,"Z#rightarrow #tau#tau","f")
ZeroJetLegend.AddEntry(ZeroJet_Fakes,"Fakes","f")
ZeroJetLegend.AddEntry(ZeroJet_Higgs_Upscale,"All Higgs (#times 30)","l")

#Boosted
BoostedBackgroundStack = ROOT.THStack("BoostedBackgroundStack","BoostedBackgroundStack")
Boosted_data_obs.SetMarkerStyle(20)

Boosted_Fakes.SetLineColor(ROOT.kBlack)
Boosted_Fakes.SetFillColor(ROOT.TColor.GetColor("#ffccff"))

Boosted_ZTauTau.SetLineColor(ROOT.kBlack)
Boosted_ZTauTau.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))

Boosted_ZToLeptons.SetLineColor(ROOT.kBlack)
Boosted_ZToLeptons.SetFillColor(ROOT.TColor.GetColor("#4496c8"))

Boosted_TT.SetLineColor(ROOT.kBlack)
Boosted_TT.SetFillColor(ROOT.TColor.GetColor("#9999cc"))

Boosted_Diboson.SetLineColor(ROOT.kBlack)
Boosted_Diboson.SetFillColor(ROOT.kOrange)

Boosted_ggH_htt.SetLineColor(ROOT.kBlack)
Boosted_ggH_htt.SetFillColor(ROOT.kCyan)

Boosted_qqH_htt.SetLineColor(ROOT.kBlack)
Boosted_qqH_htt.SetFillColor(ROOT.kGreen)

Boosted_WH_htt.SetLineColor(ROOT.kBlack)
Boosted_WH_htt.SetFillColor(ROOT.kPink+6)

Boosted_ZH_htt.SetLineColor(ROOT.kBlack)
Boosted_ZH_htt.SetFillColor(ROOT.kGreen+3)

Boosted_EWK.SetLineColor(ROOT.kBlack)
Boosted_EWK.SetFillColor(ROOT.kBlue-2)

Boosted_Other.SetLineColor(ROOT.kBlack)
Boosted_Other.SetFillColor(ROOT.TColor.GetColor("#12cadd"))

BoostedBackgroundStack.Add(Boosted_Fakes,"hist")
BoostedBackgroundStack.Add(Boosted_ZTauTau,"hist")
BoostedBackgroundStack.Add(Boosted_ZToLeptons,"hist")
BoostedBackgroundStack.Add(Boosted_TT,"hist")
#BoostedBackgroundStack.Add(Boosted_Diboson,"hist")
#BoostedBackgroundStack.Add(Boosted_ggH_htt,"hist")
#BoostedBackgroundStack.Add(Boosted_qqH_htt,"hist")
#BoostedBackgroundStack.Add(Boosted_WH_htt,"hist")
#BoostedBackgroundStack.Add(Boosted_ZH_htt,"hist")
#BoostedBackgroundStack.Add(Boosted_EWK,"hist")
BoostedBackgroundStack.Add(Boosted_Other,"hist")

BoostedLegend = ROOT.TLegend(0.9,0.6,1.0,0.9)
#BoostedLegend.AddEntry(Boosted_EWK,"EWK","f")
#BoostedLegend.AddEntry(Boosted_ZH_htt,"ZH","f")
#BoostedLegend.AddEntry(Boosted_WH_htt,"WH","f")
#BoostedLegend.AddEntry(Boosted_qqH_htt,"qqH","f")
#BoostedLegend.AddEntry(Boosted_ggH_htt,"ggH","f")
#BoostedLegend.AddEntry(Boosted_Diboson,"VV+ST","f")
BoostedLegend.AddEntry(Boosted_Other,"Other","f")
BoostedLegend.AddEntry(Boosted_TT,"t#bar{t}","f")
BoostedLegend.AddEntry(Boosted_ZToLeptons,"Z#rightarrow ll","f")
BoostedLegend.AddEntry(Boosted_ZTauTau,"Z#rightarrow #tau#tau","f")
BoostedLegend.AddEntry(Boosted_Fakes,"Fakes","f")
BoostedLegend.AddEntry(Boosted_Higgs_Upscale,"All Higgs (#times 30)","l")

#VBF
VBFBackgroundStack = ROOT.THStack("VBFBackgroundStack","VBFBackgroundStack")
VBF_data_obs.SetMarkerStyle(20)

VBF_Fakes.SetLineColor(ROOT.kBlack)
VBF_Fakes.SetFillColor(ROOT.TColor.GetColor("#ffccff"))

VBF_ZTauTau.SetLineColor(ROOT.kBlack)
VBF_ZTauTau.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))

VBF_ZToLeptons.SetLineColor(ROOT.kBlack)
VBF_ZToLeptons.SetFillColor(ROOT.TColor.GetColor("#4496c8"))

VBF_TT.SetLineColor(ROOT.kBlack)
VBF_TT.SetFillColor(ROOT.TColor.GetColor("#9999cc"))

VBF_Diboson.SetLineColor(ROOT.kBlack)
VBF_Diboson.SetFillColor(ROOT.kOrange)

VBF_ggH_htt.SetLineColor(ROOT.kBlack)
VBF_ggH_htt.SetFillColor(ROOT.kCyan)

VBF_qqH_htt.SetLineColor(ROOT.kBlack)
VBF_qqH_htt.SetFillColor(ROOT.kGreen)

VBF_WH_htt.SetLineColor(ROOT.kBlack)
VBF_WH_htt.SetFillColor(ROOT.kPink+6)

VBF_ZH_htt.SetLineColor(ROOT.kBlack)
VBF_ZH_htt.SetFillColor(ROOT.kGreen+3)

VBF_EWK.SetLineColor(ROOT.kBlack)
VBF_EWK.SetFillColor(ROOT.kBlue-2)

VBF_Other.SetLineColor(ROOT.kBlack)
VBF_Other.SetFillColor(ROOT.TColor.GetColor("#12cadd"))

VBFBackgroundStack.Add(VBF_Fakes,"hist")
VBFBackgroundStack.Add(VBF_ZTauTau,"hist")
VBFBackgroundStack.Add(VBF_ZToLeptons,"hist")
VBFBackgroundStack.Add(VBF_TT,"hist")
VBFBackgroundStack.Add(VBF_Diboson,"hist")
#VBFBackgroundStack.Add(VBF_ggH_htt,"hist")
#VBFBackgroundStack.Add(VBF_qqH_htt,"hist")
#VBFBackgroundStack.Add(VBF_WH_htt,"hist")
#VBFBackgroundStack.Add(VBF_ZH_htt,"hist")
#VBFBackgroundStack.Add(VBF_EWK,"hist")
VBFBackgroundStack.Add(VBF_Other,"hist")

VBFLegend = ROOT.TLegend(0.9,0.6,1.0,0.9)
#VBFLegend.AddEntry(VBF_EWK,"EWK","f")
#VBFLegend.AddEntry(VBF_ZH_htt,"ZH","f")
#VBFLegend.AddEntry(VBF_WH_htt,"WH","f")
#VBFLegend.AddEntry(VBF_qqH_htt,"qqH","f")
#VBFLegend.AddEntry(VBF_ggH_htt,"ggH","f")
#VBFLegend.AddEntry(VBF_Diboson,"VV+ST","f")
VBFLegend.AddEntry(VBF_Other,"Other", "f")
VBFLegend.AddEntry(VBF_TT,"t#bar{t}","f")
VBFLegend.AddEntry(VBF_ZToLeptons,"Z#rightarrow ll","f")
VBFLegend.AddEntry(VBF_ZTauTau,"Z#rightarrow #tau#tau","f")
VBFLegend.AddEntry(VBF_Fakes,"Fakes","f")
VBFLegend.AddEntry(VBF_Higgs_Upscale,"All Higgs (x30)","l")

#write it all and get out of here
HistoFile = ROOT.TFile("UnrolledHistograms.root","RECREATE")
ZeroJetHistoDir = HistoFile.mkdir("mt_0jet")
ZeroJetHistoDir.cd()
ZeroJetBackgroundStack.Write()
ZeroJet_Higgs_Upscale.Write()
ZeroJet_data_obs.Write()
ZeroJetLegend.Write()

BoostedHistoDir = HistoFile.mkdir("mt_boosted")
BoostedHistoDir.cd()
BoostedBackgroundStack.Write()
Boosted_Higgs_Upscale.Write()
Boosted_data_obs.Write()
BoostedLegend.Write()

VBFHistoDir = HistoFile.mkdir("mt_vbf")
VBFHistoDir.cd()
VBFBackgroundStack.Write()
VBF_Higgs_Upscale.Write()
VBF_data_obs.Write()
VBFLegend.Write()

HistoFile.Write()
HistoFile.Close()
OutFile.Close()
