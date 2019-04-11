import ROOT
import argparse
from tqdm import tqdm
from array import array

#taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingLegacyRun2#ggH_theory_uncertainties

g_sig0=30.117
g_sig1=12.989
g_sig_ge2=5.475
g_sig_ge1=g_sig1+g_sig_ge2
g_sig_tot=g_sig0+g_sig_ge1
g_sig_vbfTopo = 0.630
g_sig_ge2noVBF=g_sig_ge2-g_sig_vbfTopo
g_sig_ge1noVBF=g_sig_ge1-g_sig_vbfTopo

def blptw(njets):
    sig = [g_sig0,g_sig1,g_sig_ge2noVBF]

    yieldUnc = [1.12, 0.66, 0.42]
    resUnc = [0.03, 0.57, 0.42]
    cut01Unc = [-1.22, 1.00, 0.21]
    cut12Unc = [0, -0.86, 0.86]

    sf = 48.52/47.4
    jetBin = 2 if njets > 1 else int(njets)
    normFact = sf/sig[jetBin]

    retVector = [yieldUnc[jetBin]*normFact, resUnc[jetBin]*normFact,
                 cut01Unc[jetBin]*normFact, cut12Unc[jetBin]*normFact]

    return retVector

def vbf_2j(STXS):
    if(STXS==101 or STXS == 102):
        return 0.200 # 20.0%
    return 0.0 #event with no vbf topology have no vbf uncertainty

def vbf_3j(STXS):
    if (STXS==101):
        return -0.320 #GG2H_VBFTOPO_JET3VETO, tot unc 38%
    if(STXS == 102):
        return 0.235 #GG2H_VBFTOPO_JET3 tot unc 30.4%
    return 0.0 #events with no VBF topology have no VBF uncertainty

def jetBinUnc(njets, STXS):
    result = blptw(njets)
    result.append(vbf_2j(STXS))
    result.append(vbf_3j(STXS))
    #set jet bin uncertainties to zero if we are in the vbf phase-space
    if result[len(result)-1] != 0.0:
        result[0]=result[1]=result[2]=result[3] = 0.0
    return result

def interpol(x,x1,y1,x2,y2):
    if(x<x1):
        return y1
    if(x>x2):
        return y2
    return y1+(y2-y1)*(x-x1)/(x2-x1)

def pT60 (pT, njets):
    if(njets==0):
        return 0
    if(njets == 1):
        return interpol(pT,20,-0.1,100,0.2)
    return interpol(pT,0,-0.1,180,0.10) # >= 2 jets

def pT120(pT, njets):
    if(njets==0):
        return 0
    return interpol(pT,90,-0.16,160,0.14)

def qm_t(pT):
    return interpol(pT,160,0.0,500,0.37)

def qcd_ggF_uncert_2017(njets, pT, STXS):
    result = jetBinUnc(njets,STXS)
    result.append(pT60(pT,njets))
    result.append(pT120(pT,njets))
    result.append(qm_t(pT))
    return result

def AddggHBranch(File,args):
    ReweightFile = ROOT.TFile(File,"UPDATE")
    TheTree=ReweightFile.mt_Selected
    
    THU_ggH_Mu_13TeV = array('f',[0])
    THU_ggH_Res_13TeV = array('f',[0])
    THU_ggH_Mig01_13TeV = array('f',[0])
    THU_ggH_Mig12_13TeV = array('f',[0])
    THU_ggH_VBF2j_13TeV = array('f',[0])
    THU_ggH_VBF3j_13TeV = array('f',[0])
    THU_ggH_PT60_13TeV = array('f',[0])
    THU_ggH_PT120_13TeV = array('f',[0])
    THU_ggH_qmtop_13TeV = array('f',[0])
    
    THU_ggH_Mu_13TeV_Branch = TheTree.Branch('THU_ggH_Mu_13TeV',THU_ggH_Mu_13TeV,'THU_ggH_Mu_13TeV/F')
    THU_ggH_Res_13TeV_Branch = TheTree.Branch('THU_ggH_Res_13TeV',THU_ggH_Res_13TeV,'THU_ggH_Res_13TeV/F')
    THU_ggH_Mig01_13TeV_Branch = TheTree.Branch('THU_ggH_Mig01_13TeV',THU_ggH_Mig01_13TeV,'THU_ggH_Mig01_13TeV/F')
    THU_ggH_Mig12_13TeV_Branch = TheTree.Branch('THU_ggH_Mig12_13TeV',THU_ggH_Mig12_13TeV,'THU_ggH_Mig12_13TeV/F')
    THU_ggH_VBF2j_13TeV_Branch = TheTree.Branch('THU_ggH_VBF2j_13TeV',THU_ggH_VBF2j_13TeV,'THU_ggH_VBF2j_13TeV/F')
    THU_ggH_VBF3j_13TeV_Branch = TheTree.Branch('THU_ggH_VBF3j_13TeV',THU_ggH_VBF3j_13TeV,'THU_ggH_VBF3j_13TeV/F')
    THU_ggH_PT60_13TeV_Branch = TheTree.Branch('THU_ggH_PT60_13TeV',THU_ggH_PT60_13TeV,'THU_ggH_PT60_13TeV/F')
    THU_ggH_PT120_13TeV_Branch = TheTree.Branch('THU_ggH_PT120_13TeV',THU_ggH_PT120_13TeV,'THU_ggH_PT120_13TeV/F')
    THU_ggH_qmtop_13TeV_Branch = TheTree.Branch('THU_ggH_qmtop_13TeV',THU_ggH_qmtop_13TeV,'THU_ggH_qmtop_13TeV/F')
    
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)

        result = qcd_ggF_uncert_2017(TheTree.Rivet_nJets30,
                                     TheTree.Rivet_higgsPt,
                                     TheTree.Rivet_stage1_cat_pTjet30GeV)

        THU_ggH_Mu_13TeV[0] = result[0]
        THU_ggH_Res_13TeV[0] = result[1]
        THU_ggH_Mig01_13TeV[0] = result[2]
        THU_ggH_Mig12_13TeV[0] = result[3]
        THU_ggH_VBF2j_13TeV[0] = result[4]
        THU_ggH_VBF3j_13TeV[0] = result[5]
        THU_ggH_PT60_13TeV[0] = result[6]
        THU_ggH_PT120_13TeV[0] = result[7]
        THU_ggH_qmtop_13TeV[0] = result[8]
        
        THU_ggH_Mu_13TeV_Branch.Fill()
        THU_ggH_Res_13TeV_Branch.Fill()
        THU_ggH_Mig01_13TeV_Branch.Fill()
        THU_ggH_Mig12_13TeV_Branch.Fill()
        THU_ggH_VBF2j_13TeV_Branch.Fill()
        THU_ggH_VBF3j_13TeV_Branch.Fill()
        THU_ggH_PT60_13TeV_Branch.Fill()
        THU_ggH_PT120_13TeV_Branch.Fill()
        THU_ggH_qmtop_13TeV_Branch.Fill()
    ReweightFile.cd()
    TheTree.Write('',ROOT.TObject.kOverwrite)
    ReweightFile.Write()
    ReweightFile.Close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and attach the ggH Theory Uncertainty branches")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's branches should be used")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")

    args = parser.parse_args()

    for File in args.Files:
        print("Processing the ggH theory uncertainty for "+File)
        AddggHBranch(File,args)
