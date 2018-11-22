import os
if __name__ == "__main__":

    place="/hdfs/store/user/caillol/SMHTT_2017_7nov/"
    sample=["DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v2/","DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14_ext1-v1/","DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v3_94X_mc2017_realistic/","DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14_ext1-v1/","DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14_ext1-v1/","DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2_94X_mc2017_realistic/","DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v14_ext1-v1/","GluGluHToTauTau_M125_13TeV_powheg_pythia8_v14-v1/","GluGluHToTauTau_M125_13TeV_powheg_pythia8_v14_ext1-v1/","ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v14-v2/","ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v14-v1/","ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v14-v2/","ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v14-v2/","TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_v14-v1/","TTToHadronic_TuneCP5_13TeV-powheg-pythia8_v14-v2/","TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_v14-v2/","VBFHToTauTau_M125_13TeV_powheg_pythia8_v14-v1/","VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_v14-v1/","W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v3/","W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v4/","W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v1/","WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14-v2/","WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v14_ext1-v2/","WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_v14-v1/","WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_v14-v1/","WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_v14-v1/","WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_v14_ext1-v1/","WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_v14-v1/","WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_v14-v2/","WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2_v2/","WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v14-v1/","WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_v14-v1/","WminusHToTauTau_M125_13TeV_powheg_pythia8_v14-v1/","WplusHToTauTau_M125_13TeV_powheg_pythia8_v14-v1/","ZHToTauTau_M125_13TeV_powheg_pythia8_v14-v1/","ZZTo2L2Nu_13TeV_powheg_pythia8_v14-v1/","ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v14-v1/","ZZTo4L_13TeV_powheg_pythia8_v14-v1/","ZZTo4L_13TeV_powheg_pythia8_v14-v2/","ZZTo4L_13TeV_powheg_pythia8_v14_ext1-v1/","EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v14-v1/","EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8_v14-v1/","EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8_v14-v1/","EWKZ2Jets_ZToNuNu_TuneCP5_13TeV-madgraph-pythia8_v14-v1/"]
    name=["DY1_1","DY1_2","DY1_3","DY1_4","DY2_1","DY2_2","DY3_1","DY3_2","DY4_1","DY4_2","DY10to50","DY_1","DY_2","ggH125_1","ggH125_2","ST_t_antitop","ST_t_top","ST_tW_antitop","ST_tW_top","TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic","VBF125","VV2L2Nu","W1","W2","W3","W4","W_1","W_2","WWTo1L1Nu2Q","WWTo4Q","WWToLNuQQ_1","WWToLNuQQ_2","WZTo1L1Nu2Q_1","WZTo1L1Nu2Q_2","WZTo1L3Nu","WZTo2L2Q","WZTo3LNu","WminusH125","WplusH125","ZH125","ZZTo2L2Nu","ZZTo2L2Q","ZZTo4L_1","ZZTo4L_2","ZZ4L_2","EWKWMinus","EWKWPlus","EWKZLL","EWKZNuNu"]
    recoil=["Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","0","0","0","0","0","0","0","Z","0","W","W","W","W","W","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","Z","Z","Z","Z"]

    #place="/hdfs/store/user/caillol/SMHTT2017_embedded_8nov/"
    #sample=["embedded_EmbeddingRun2017B_MuTauFinalState/","embedded_EmbeddingRun2017C_MuTauFinalState/","embedded_EmbeddingRun2017D_MuTauFinalState/","embedded_EmbeddingRun2017E_MuTauFinalState/","embedded_EmbeddingRun2017F_MuTauFinalState/"]
    #name=["embeddedB","embeddedC","embeddedD","embeddedE","embeddedF"]
    #recoil=["0","0","0","0","0"]

    #place="/hdfs/store/user/caillol/SMHTT2017_data_8nov/"
    #sample=["data_SingleMuon_Run2017B-31Mar2018/","data_SingleMuon_Run2017C-31Mar2018/","data_SingleMuon_Run2017D-31Mar2018/","data_SingleMuon_Run2017E-31Mar2018/","data_SingleMuon_Run2017F-31Mar2018/"]
    #name=["DataB","DataC","DataD","DataE","DataF"]
    #recoil=["0","0","0","0","0"]
    
    datadir="/nfs_scratch/caillol/smhmt_15nov/"
    all_File = open("do_submit_mt.sh" , 'w')
    line=""
    for j in range(0,len(name)):
       print name[j],sample[j],recoil[j]
       submit_File = open("Submit_"+name[j]+"_mt.sh" , 'w')
       line+="mkdir -p "+datadir+"Out_"+name[j]+"\n"
       line+="sh Submit_"+name[j]+"_mt.sh" +"\n"
       f=os.popen("ls -t " + place+sample[j] + "make* | sort")
       command1=""
       ligne=0
       for i in f.readlines():
	   command1=command1+"./skim_mt.exe mc "+datadir+"Out_"+name[j]+"/"+name[j]+str(ligne)+".root " + i[0:-1] + " " + recoil[j] +"\n"
           ligne=ligne+1
       submit_File.write(command1)
       submit_File.close()
    all_File.write(line)
    all_File.close()
