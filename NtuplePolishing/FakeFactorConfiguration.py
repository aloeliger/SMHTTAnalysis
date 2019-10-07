#configuration for fake factors
import os

#ntuple_path_2016 = os.environ["CMSSW_BASE"]+"/src/SMHTTAnalysis/SelectedNtuples/2016AntiIso/"
#ntuple_path_2017 = os.environ["CMSSW_BASE"]+"/src/SMHTTAnalysis/SelectedNtuples/2017AntiIso/"
#ntuple_path_2018 = os.environ["CMSSW_BASE"]+"/src/SMHTTAnalysis/SelectedNtuples/2018AntiIso/"

ntuple_path_2016 = "/data/aloeliger/SMHTT_Selected_2016_AntiIso/"
ntuple_path_2017 = "/data/aloeliger/SMHTT_Selected_2017_AntiIso/"
#ntuple_path_2018 = "/data/aloeliger/SMHTT_Selected_2018_AntiIso/"
ntuple_path_2018 = "/data/aloeliger/SMHTT_Selected_2018_MCOnly_AntiIso_Deep/"

Data_Files_2016 = {'data':'Data.root'}
Data_Files_2017 = {'data':'Data.root'}
Data_Files_2018 = {'data':'Data.root'}

W_Files_2016 = {'DY':'DY.root',
                'ST_t_antitop':'ST_t_antitop.root',
                'ST_t_top':'ST_t_top.root',
                'ST_tW_antitop':'ST_tW_antitop.root',
                'ST_tW_top':'ST_tW_top.root',
                #'WW1L1Nu2Q':'WW1L1Nu2Q.root',
                #'WZ1L1Nu2Q':'WZ1L1Nu2Q.root',
                #'WZ1L3Nu':'WZ1L3Nu.root',
                #'WZ2L2Q':'WZ2L2Q.root',
                #'WZJLLLNu':'WZJLLLNu.root',
                #'ZZ4L':'ZZ4L.root',
                #'ZZ2L2Q':'ZZ2L2Q.root',
                'WW':'WW.root',
                'WZ':'WZ.root',                
                'ZZ':'ZZ.root',                
                'W':'W.root'}
W_Files_2017 = {'DY':'DY.root',
                'ST_t_antitop':'ST_t_antitop.root',
                'ST_t_top':'ST_t_top.root',
                'ST_tW_antitop':'ST_tW_antitop.root',
                'ST_tW_top':'ST_tW_top.root',
                'WW':'WW.root',
                'WZ':'WZ.root',                
                'ZZ':'ZZ.root',                
                'W':'W.root'}
W_Files_2018 = {'DY':'DY.root',
                'ST_t_antitop':'ST_t_antitop.root',
                'ST_t_top':'ST_t_top.root',
                'ST_tW_antitop':'ST_tW_antitop.root',
                'ST_tW_top':'ST_tW_top.root',
                'WW':'WW.root',
                'WZ':'WZ.root',                
                'ZZ':'ZZ.root',                
                'W':'W.root'}

TT_Files_2016 = {'TT':'TT.root'}
TT_Files_2017 = {'TTTo2L2Nu':'TTTo2L2Nu.root',
                 'TTToHadronic':'TTToHadronic.root',
                 'TTToSemiLeptonic':'TTToSemiLeptonic.root'}
TT_Files_2018 = {'TTTo2L2Nu':'TTTo2L2Nu.root',
                 'TTToHadronic':'TTToHadronic.root',
                 'TTToSemiLeptonic':'TTToSemiLeptonic.root'}

Embedded_Files_2017 = {'Embedded':'Embedded.root'}
Embedded_Files_2018 = {'Embedded':'Embedded.root'}
