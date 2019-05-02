#!/usr/bin/bash
python SeperateIntoSTXSBins.py 2017 ../SelectedNtuples/2017/!(W.root) ../SelectedNtuples/2017AntiIso/Data.root \
--ggHSignalFiles ../SelectedNtuples/2017/ggH.root \
--ggHBackgroundFiles ../SelectedNtuples/2017/WHPlus.root ../SelectedNtuples/2017/WHMinus.root ../SelectedNtuples/2017/WHMinus.root ../SelectedNtuples/2017/ZH.root ../SelectedNtuples/2017/VBF.root \
--qqHSignalFiles ../SelectedNtuples/2017/VBF.root \
--qqHBackgroundFiles ../SelectedNtuples/2017/ggH.root ../SelectedNtuples/2017/WHMinus.root ../SelectedNtuples/2017/WHPlus.root ../SelectedNtuples/2017/ZH.root \
--VHSignalFiles ../SelectedNtuples/2017/WHMinus.root ../SelectedNtuples/2017/WHPlus.root ../SelectedNtuples/2017/ZH.root \
--VHBackgroundFiles ../SelectedNtuples/2017/ggH.root ../SelectedNtuples/2017/VBF.root \
--NonHiggsBackgroundFiles ../SelectedNtuples/2017/DY.root ../SelectedNtuples/2017/EWKZLL.root ../SelectedNtuples/2017/EWKZNuNu.root ../SelectedNtuples/2017/Embedded.root ../SelectedNtuples/2017/ST_tW_antitop.root ../SelectedNtuples/2017/ST_tW_top.root ../SelectedNtuples/2017/ST_t_antitop.root ../SelectedNtuples/2017/ST_t_top.root ../SelectedNtuples/2017/TTTo2L2Nu.root ../SelectedNtuples/2017/TTToHadronic.root ../SelectedNtuples/2017/TTToSemiLeptonic.root ../SelectedNtuples/2017/WW.root ../SelectedNtuples/2017/WZ.root ../SelectedNtuples/2017/ZZ.root ../SelectedNtuples/2017AntiIso/Data.root \
--UseFakeFactorOnFiles ../SelectedNtuples/2017AntiIso/Data.root \
--DataFiles ../SelectedNtuples/2017/Data.root 