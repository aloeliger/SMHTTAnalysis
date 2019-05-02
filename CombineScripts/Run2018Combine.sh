#!/usr/bin/bash
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/Data.root

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY_T.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/DY_L.root --MakeDYShape --UseTES --UseJES --MakeZLShape --MakeRecoilUncertainties

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/Embedded.root --UseTES 

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTTo2L2Nu.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTTo2L2Nu_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTTo2L2Nu_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToHadronic.root --UseTES --UseJES 
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToHadronic_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToHadronic_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToSemiLeptonic.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToSemiLeptonic_L.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/TTToSemiLeptonic_T.root  --UseTES --UseJES

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WW.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WW_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WW_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZZ.root --UseTES --UseJES 
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZZ_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZZ_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WZ.root --UseTES --UseJES 
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WZ_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WZ_T.root --UseTES --UseJES

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZLL.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZLL_L.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZLL_T.root  --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZNuNu.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZNuNu_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/EWKZNuNu_T.root --UseTES --UseJES

#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_top.root --UseTES --UseJES 
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_top_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_top_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_antitop.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_antitop_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_t_antitop_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_top.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_top_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_top_T.root --UseTES --UseJES
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_antitop.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_antitop_L.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ST_tW_antitop_T.root --UseTES --UseJES

python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ZH.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/VBF.root --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WHPlus.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/WHMinus.root  --UseTES --UseJES
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018/ggH.root --UseTES --UseJES --MakeggHTheoryShape

#Create the rolled up fake shapes
python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018AntiIso/Data.root --UseFakeFactor

#Create the TTBarContamination shapes needed
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTTo2L2Nu.root --MakeTTbarContamination
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTToSemiLeptonic.root --MakeTTbarContamination
#python GenerateRolledPlots.py 2018 ../SelectedNtuples/2018TTContamination/TTToHadronic.root --MakeTTbarContamination

python SortRolledDistributions.py 2018