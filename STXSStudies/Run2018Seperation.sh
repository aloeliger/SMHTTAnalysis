#!/usr/bin/bash
python SeperateIntoSTXSBins.py 2018 ../SelectedNtuples/2018/!(W.root|*_L*|*_T*) ../SelectedNtuples/2018AntiIso/Data.root \
--ggHSignalFiles ../SelectedNtuples/2018/ggH.root \
--ggHBackgroundFiles ../SelectedNtuples/2018/WHPlus.root ../SelectedNtuples/2018/WHMinus.root ../SelectedNtuples/2018/WHMinus.root ../SelectedNtuples/2018/ZH.root ../SelectedNtuples/2018/VBF.root \
--qqHSignalFiles ../SelectedNtuples/2018/VBF.root \
--qqHBackgroundFiles ../SelectedNtuples/2018/ggH.root ../SelectedNtuples/2018/WHMinus.root ../SelectedNtuples/2018/WHPlus.root ../SelectedNtuples/2018/ZH.root \
--VHSignalFiles ../SelectedNtuples/2018/WHMinus.root ../SelectedNtuples/2018/WHPlus.root ../SelectedNtuples/2018/ZH.root \
--VHBackgroundFiles ../SelectedNtuples/2018/ggH.root ../SelectedNtuples/2018/VBF.root \
--NonHiggsBackgroundFiles ../SelectedNtuples/2018/DY.root ../SelectedNtuples/2018/EWKZLL.root ../SelectedNtuples/2018/EWKZNuNu.root ../SelectedNtuples/2018/ST_tW_antitop.root ../SelectedNtuples/2018/ST_tW_top.root ../SelectedNtuples/2018/ST_t_antitop.root ../SelectedNtuples/2018/ST_t_top.root ../SelectedNtuples/2018/TTTo2L2Nu.root ../SelectedNtuples/2018/TTToHadronic.root ../SelectedNtuples/2018/TTToSemiLeptonic.root ../SelectedNtuples/2018/WW.root ../SelectedNtuples/2018/WZ.root ../SelectedNtuples/2018/ZZ.root ../SelectedNtuples/2018AntiIso/Data.root \
--UseFakeFactorOnFiles ../SelectedNtuples/2018AntiIso/Data.root \
--DataFiles ../SelectedNtuples/2018/Data.root 