#!/usr/bin/bash
cd $CMSSW_BASE/src/
#first things first let's get the official tau POG ID and Trigger SF repos.
#tau ID:
git clone https://github.com/cms-tau-pog/TauIDSFs TauPOG/TauIDSFs
#Tau trigger SFs:
mkdir TauAnalysisTools
git clone -b run2_SFs https://github.com/cms-tau-pog/TauTriggerSFs $CMSSW_BASE/src/TauAnalysisTools/TauTriggerSFs
#Let's also get the master version of the fake factor computing repo
git clone https://github.com/CMS-HTT/LeptonEfficiencies.git
git clone https://github.com/cecilecaillol/ComputeFF2018.git

#build and return
scram b -j 8
cd SMHTTAnalysis
