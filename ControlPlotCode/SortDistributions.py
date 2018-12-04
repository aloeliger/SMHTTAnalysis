import ROOT

TheFile = ROOT.TFile("CecileCode/Results.root")
OutFile = ROOT.TFile("CombineWorkSpaceFile.root", "RECREATE")

data_obs = TheFile.data_obs_mvis
data_obs.SetNameTitle("data_obs","data_obs")

Fakes = TheFile.data_obs_Fake_mvis
Fakes.SetNameTitle("jetFakes","jetFakes")

ZTauTau = TheFile.embedded_mvis
ZTauTau.SetNameTitle("ZTT","ZTT")

ZToLeptons = TheFile.DY_mvis
ZToLeptonsLow = TheFile.DYlow_mvis
ZToLeptons.Add(ZToLeptonsLow)
ZToLeptons.SetNameTitle("ZL","ZL")

TT = TheFile.TTToHadronic_mvis
TT.Add(TheFile.TTTo2L2Nu_mvis)
TT.Add(TheFile.TTToSemiLeptonic_mvis)
TT.SetNameTitle("TTT","TTT")

Diboson = TheFile.WW4Q_mvis
Diboson.Add(TheFile.WWLNuQQ_mvis)
Diboson.Add(TheFile.WZ2L2Q_mvis)
Diboson.Add(TheFile.WZ1L3Nu_mvis)
Diboson.Add(TheFile.WZ3LNu_mvis)
Diboson.Add(TheFile.WZ1L1Nu2Q_mvis)
Diboson.Add(TheFile.ZZ4L_mvis)
Diboson.Add(TheFile.ZZ4L_mvis)
Diboson.Add(TheFile.ZZ2L2Nu_mvis)
Diboson.Add(TheFile.ZZ2L2Q_mvis)
Diboson.SetNameTitle("VVT","VVT")

SingleTop = TheFile.ST_t_antitop_mvis
SingleTop.Add(TheFile.ST_t_top_mvis)
SingleTop.Add(TheFile.ST_tW_antitop_mvis)
SingleTop.Add(TheFile.ST_tW_top_mvis)
#Temporary?
Diboson.Add(SingleTop)

ggH_htt = TheFile.ggH_htt125_mvis
ggH_htt.SetNameTitle("ggH_htt125","ggH_htt")

qqH_htt = TheFile.qqH_htt125_mvis
qqH_htt.SetNameTitle("qqH_htt125","qqH_htt")

WH_htt = TheFile.WplusH125_mvis
WH_htt.Add(TheFile.WminusH125_mvis)
WH_htt.SetNameTitle("WH_htt125","WH_htt")

ZH_htt = TheFile.ZH125_mvis
ZH_htt.SetNameTitle("ZH_htt125","ZH_htt")

EWK = TheFile.EWKZLL_mvis
EWK.Add(TheFile.EWKZNuNu_mvis)
EWK.SetNameTitle("EWKZ","EWKZ")

OutFile.cd()
ZeroJetDir = OutFile.mkdir("mt_0jet")
ZeroJetDir.cd()
data_obs.Write()
Fakes.Write()
ZTauTau.Write()
ZToLeptons.Write()
TT.Write()
Diboson.Write()
ggH_htt.Write()
qqH_htt.Write()
WH_htt.Write()
ZH_htt.Write()
EWK.Write()
OutFile.Write()
OutFile.Close()
