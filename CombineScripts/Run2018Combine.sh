#!/usr/bin/bash
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/Data.root --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY_T.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY_L.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/Embedded.root --UseTES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTTo2L2Nu.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToHadronic.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToSemiLeptonic.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WW.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZZ.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WZ.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZLL.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZNuNu.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_top.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_antitop.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_top.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_antitop.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZH.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/VBF.root --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WHPlus.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WHMinus.root  --UseTES --UseJES --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ggH.root --UseTES --UseJES --MakeggHTheoryShape --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#Create the rolled up fake shapes
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018AntiIso/Data.root --UseFakeFactor --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

#Create the TTBarContamination shapes needed
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTTo2L2Nu.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTToSemiLeptonic.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTToHadronic.root --MakeTTbarContamination --numZeroJetBins 10 --numBoostedBins 10 --numVBFBins 10

python SortRolledDistributions.py 2018