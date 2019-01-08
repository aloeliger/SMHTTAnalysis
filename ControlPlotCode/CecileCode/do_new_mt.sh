./Make.sh FinalSelection_mt.cc
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/Data.root files_nominal_mt/Data.root data_obs data_obs 0
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/Embedded.root files_nominal_mt/Embedded.root embedded embedded 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/DYall.root files_nominal_mt/DY.root DY DY 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/DYlow.root files_nominal_mt/DYlow.root DYlow DYlow 0
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/Wall.root files_nominal_mt/W.root W W 0
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/TTToHadronic.root files_nominal_mt/TTToHadronic.root TTToHadronic TT 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/TTTo2L2Nu.root files_nominal_mt/TTTo2L2Nu.root TTTo2L2Nu TT 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/TTToSemiLeptonic.root files_nominal_mt/TTToSemiLeptonic.root TTToSemiLeptonic TT 0

hadd -f files_nominal_mt/TT.root files_nominal_mt/TTToHadronic.root files_nominal_mt/TTTo2L2Nu.root files_nominal_mt/TTToSemiLeptonic.root
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/WW.root files_nominal_mt/WW.root WW VV 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/WZ.root files_nominal_mt/WZ.root WZ VV 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ZZ.root files_nominal_mt/ZZ.root ZZ VV 0

./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ST_t_antitop.root files_nominal_mt/ST_t_antitop.root ST_t_antitop VV 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ST_t_top.root files_nominal_mt/ST_t_top.root ST_t_top VV 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ST_tW_antitop.root files_nominal_mt/ST_tW_antitop.root ST_tW_antitop VV 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ST_tW_top.root files_nominal_mt/ST_tW_top.root ST_tW_top VV 0

hadd -f files_nominal_mt/VV.root files_nominal_mt/ST_t_antitop.root files_nominal_mt/ST_t_top.root files_nominal_mt/ST_tW_antitop.root files_nominal_mt/ST_tW_top.root files_nominal_mt/WW.root files_nominal_mt/WZ.root files_nominal_mt/ZZ.root
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ggH125.root files_nominal_mt/ggH_htt125.root ggH_htt125 ggH_htt125 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/VBF125.root files_nominal_mt/qqH_htt125.root qqH_htt125 qqH_htt125 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/WplusH125.root files_nominal_mt/Wplus125.root WplusH125 WH_htt125 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/WminusH125.root files_nominal_mt/WminusH125.root WminusH125 WH_htt125 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/ZH125.root files_nominal_mt/ZH125.root ZH125 ZH_htt125 0
hadd -f files_nominal_mt/signal.root files_nominal_mt/ggH_htt125.root files_nominal_mt/qqH_htt125.root files_nominal_mt/Wplus125.root files_nominal_mt/WminusH125.root files_nominal_mt/ZH125.root
#
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/EWKZLL.root files_nominal_mt/EWKZLL.root EWKZLL EWKZ 0
./FinalSelection_mt.exe /data/ccaillol/smhmt_3jan_svfit/EWKZNuNu.root files_nominal_mt/EWKZNuNu.root EWKZNuNu EWKZ 0