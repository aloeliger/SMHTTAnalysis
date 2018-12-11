import ROOT

TheFile = ROOT.TFile("CecileCode/Results.root")
OneDOutFile = ROOT.TFile("CombineWorkSpaceFile-1D.root", "RECREATE")

#Collect and name the 0 jet 1D Category
ZeroJet_data_obs = TheFile.mt_0jet.data_obs_mvis
ZeroJet_data_obs.SetNameTitle("data_obs","data_obs")

ZeroJet_Fakes = TheFile.mt_0jet.data_obs_Fake_mvis
ZeroJet_Fakes.SetNameTitle("jetFakes","jetFakes")

ZeroJet_ZTauTau = TheFile.mt_0jet.embedded_mvis
ZeroJet_ZTauTau.SetNameTitle("ZTT","ZTT")

ZeroJet_ZToLeptons = TheFile.mt_0jet.DY_mvis
ZeroJet_ZToLeptons.Add(TheFile.mt_0jet.DYlow_mvis)
ZeroJet_ZToLeptons.SetNameTitle("ZL","ZL")

ZeroJet_TT = TheFile.mt_0jet.TTToHadronic_mvis
ZeroJet_TT.Add(TheFile.mt_0jet.TTTo2L2Nu_mvis)
ZeroJet_TT.Add(TheFile.mt_0jet.TTToSemiLeptonic_mvis)
ZeroJet_TT.SetNameTitle("TTT","TTT")

ZeroJet_Diboson = TheFile.WW4Q_mvis
ZeroJet_Diboson.Add(TheFile.mt_0jet.WWLNuQQ_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.WZ2L2Q_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.WZ1L3Nu_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.WZ3LNu_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.WZ1L1Nu2Q_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.ZZ4L_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.ZZ2L2Nu_mvis)
ZeroJet_Diboson.Add(TheFile.mt_0jet.ZZ2L2Q_mvis)
ZeroJet_Diboson.SetNameTitle("VVT","VVT")

ZeroJet_SingleTop = TheFile.mt_0jet.ST_t_antitop_mvis
ZeroJet_SingleTop.Add(TheFile.mt_0jet.ST_t_top_mvis)
ZeroJet_SingleTop.Add(TheFile.mt_0jet.ST_tW_antitop_mvis)
ZeroJet_SingleTop.Add(TheFile.mt_0jet.ST_tW_top_mvis)
#Temporary?
ZeroJet_Diboson.Add(SingleTop)

ZeroJet_ggH_htt = TheFile.mt_0jet.ggH_htt125_mvis
ZeroJet_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")

ZeroJet_qqH_htt = TheFile.mt_0jet.qqH_htt125_mvis
ZeroJet_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")

ZeroJet_WH_htt = TheFile.mt_0jet.WplusH125_mvis
ZeroJet_WH_htt.Add(TheFile.mt_0jet.WminusH125_mvis)
ZeroJet_WH_htt.SetNameTitle("WH_htt125","WH_htt")

ZeroJet_ZH_htt = TheFile.mt_0jet.ZH125_mvis
ZeroJet_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")

ZeroJet_EWK = TheFile.mt_0jet.EWKZLL_mvis
ZeroJet_EWK.Add(TheFile.mt_0jet.EWKZNuNu_mvis)
ZeroJet_EWK.SetNameTitle("EWKZ","EWKZ")

#Boosted
Boosted_data_obs = TheFile.mt_boosted.data_obs_mvis
Boosted_data_obs.SetNameTitle("data_obs","data_obs")

Boosted_Fakes = TheFile.mt_boosted.data_obs_Fake_mvis
Boosted_Fakes.SetNameTitle("jetFakes","jetFakes")

Boosted_ZTauTau = TheFile.mt_boosted.embedded_mvis
Boosted_ZTauTau.SetNameTitle("ZTT","ZTT")

Boosted_ZToLeptons = TheFile.mt_boosted.DY_mvis
Boosted_ZToLeptons.Add(TheFile.mt_boosted.DYlow_mvis)
Boosted_ZToLeptons.SetNameTitle("ZL","ZL")

Boosted_TT = TheFile.mt_boosted.TTToHadronic_mvis
Boosted_TT.Add(TheFile.mt_boosted.TTTo2L2Nu_mvis)
Boosted_TT.Add(TheFile.mt_boosted.TTToSemiLeptonic_mvis)
Boosted_TT.SetNameTitle("TTT","TTT")

Boosted_Diboson = TheFile.WW4Q_mvis
Boosted_Diboson.Add(TheFile.mt_boosted.WWLNuQQ_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.WZ2L2Q_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.WZ1L3Nu_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.WZ3LNu_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.WZ1L1Nu2Q_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.ZZ4L_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.ZZ2L2Nu_mvis)
Boosted_Diboson.Add(TheFile.mt_boosted.ZZ2L2Q_mvis)
Boosted_Diboson.SetNameTitle("VVT","VVT")

Boosted_SingleTop = TheFile.mt_boosted.ST_t_antitop_mvis
Boosted_SingleTop.Add(TheFile.mt_boosted.ST_t_top_mvis)
Boosted_SingleTop.Add(TheFile.mt_boosted.ST_tW_antitop_mvis)
Boosted_SingleTop.Add(TheFile.mt_boosted.ST_tW_top_mvis)
#Temporary?
Boosted_Diboson.Add(SingleTop)

Boosted_ggH_htt = TheFile.mt_boosted.ggH_htt125_mvis
Boosted_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")

Boosted_qqH_htt = TheFile.mt_boosted.qqH_htt125_mvis
Boosted_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")

Boosted_WH_htt = TheFile.mt_boosted.WplusH125_mvis
Boosted_WH_htt.Add(TheFile.mt_boosted.WminusH125_mvis)
Boosted_WH_htt.SetNameTitle("WH_htt125","WH_htt")

Boosted_ZH_htt = TheFile.mt_boosted.ZH125_mvis
Boosted_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")

Boosted_EWK = TheFile.mt_boosted.EWKZLL_mvis
Boosted_EWK.Add(TheFile.mt_boosted.EWKZNuNu_mvis)
Boosted_EWK.SetNameTitle("EWKZ","EWKZ")

#VBF
VBF_data_obs = TheFile.mt_vbf.data_obs_mvis
VBF_data_obs.SetNameTitle("data_obs","data_obs")

VBF_Fakes = TheFile.mt_vbf.data_obs_Fake_mvis
VBF_Fakes.SetNameTitle("jetFakes","jetFakes")

VBF_ZTauTau = TheFile.mt_vbf.embedded_mvis
VBF_ZTauTau.SetNameTitle("ZTT","ZTT")

VBF_ZToLeptons = TheFile.mt_vbf.DY_mvis
VBF_ZToLeptons.Add(TheFile.mt_vbf.DYlow_mvis)
VBF_ZToLeptons.SetNameTitle("ZL","ZL")

VBF_TT = TheFile.mt_vbf.TTToHadronic_mvis
VBF_TT.Add(TheFile.mt_vbf.TTTo2L2Nu_mvis)
VBF_TT.Add(TheFile.mt_vbf.TTToSemiLeptonic_mvis)
VBF_TT.SetNameTitle("TTT","TTT")

VBF_Diboson = TheFile.WW4Q_mvis
VBF_Diboson.Add(TheFile.mt_vbf.WWLNuQQ_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.WZ2L2Q_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.WZ1L3Nu_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.WZ3LNu_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.WZ1L1Nu2Q_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.ZZ4L_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.ZZ2L2Nu_mvis)
VBF_Diboson.Add(TheFile.mt_vbf.ZZ2L2Q_mvis)
VBF_Diboson.SetNameTitle("VVT","VVT")

VBF_SingleTop = TheFile.mt_vbf.ST_t_antitop_mvis
VBF_SingleTop.Add(TheFile.mt_vbf.ST_t_top_mvis)
VBF_SingleTop.Add(TheFile.mt_vbf.ST_tW_antitop_mvis)
VBF_SingleTop.Add(TheFile.mt_vbf.ST_tW_top_mvis)
#Temporary?
VBF_Diboson.Add(SingleTop)

VBF_ggH_htt = TheFile.mt_vbf.ggH_htt125_mvis
VBF_ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")

VBF_qqH_htt = TheFile.mt_vbf.qqH_htt125_mvis
VBF_qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")

VBF_WH_htt = TheFile.mt_vbf.WplusH125_mvis
VBF_WH_htt.Add(TheFile.mt_vbf.WminusH125_mvis)
VBF_WH_htt.SetNameTitle("WH_htt125","WH_htt")

VBF_ZH_htt = TheFile.mt_vbf.ZH125_mvis
VBF_ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")

VBF_EWK = TheFile.mt_vbf.EWKZLL_mvis
VBF_EWK.Add(TheFile.mt_vbf.EWKZNuNu_mvis)
VBF_EWK.SetNameTitle("EWKZ","EWKZ")

OneDOutFile.cd()

ZeroJetOneDDir = OneDOutFile.mkdir("mt_0jet")
ZeroJetOneDDir.cd()
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

BoostedOneDDir = OneDOutFile.mkdir("mt_boosted")
BoostedOneDDir.cd()
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

VBFOneDDir = OneDOutFile.mkdir("mt_vbf")
VBFOneDDir.cd()
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

OneDOutFile.Write()
OneDOutFile.Close()
