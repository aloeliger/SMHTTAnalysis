#!/usr/bin/bash
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/Data.root --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/DY.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/Embedded.root --UseTES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/TTTo2L2Nu.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/TTToHadronic.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/TTToSemiLeptonic.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/WW.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ZZ.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/WZ.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/EWKZLL.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/EWKZNuNu.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ST_t_top.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ST_t_antitop.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ST_tW_top.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ST_tW_antitop.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ZH.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/VBF.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/WHPlus.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/WHMinus.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017/ggH.root --UseTES --UseJES --MakeggHTheoryShape --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#Create the rolled up fake shapes
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017AntiIso/Data.root --UseFakeFactor --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#Create the TTBarContamination shapes needed
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017TTContamination/TTTo2L2Nu.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017TTContamination/TTToSemiLeptonic.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2017 ../SelectedNtuples/2017TTContamination/TTToHadronic.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python SortRolledDistributions.py 2017