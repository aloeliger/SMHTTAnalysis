import ROOT
import sys
from tqdm import tqdm
from array import array
import argparse

def getEfficiency(pt,eta,phi,effHist,etaPhi,etaPhiAvg,central_or_shift = 0):
    effHist_xAxis = effHist.GetXaxis()
    ptMin = effHist_xAxis.GetXmin() + 0.1
    ptMax = effHist_xAxis.GetXmax() - 0.1
    pt_checked = pt
    if(pt_checked > ptMax):
        pt_checked = ptMax
    if(pt_checked < ptMin):
        pt_checked = ptMin
    effHist_idxBin = effHist.FindBin(pt_checked)
    assert(effHist_idxBin >= 1 and effHist_idxBin <= effHist.GetNbinsX())
    eff = effHist.GetBinContent(effHist_idxBin)

    effErr = effHist.GetBinError(effHist_idxBin)
    if(central_or_shift==1):
        eff += effErr
    if(central_or_shift==-1):
        eff -= effErr

    #Adjust SF based on (eta, phi) location
    #keep eta barrel boundaries within SF region
    #but, for taus outside eta limits or with unralistic
    #phi values, return zero SF
    etaPhiAvg_xAxis = etaPhiAvg.GetXaxis()
    etaMin = etaPhiAvg_xAxis.GetXmin() + 0.01
    etaMax = etaPhiAvg_xAxis.GetXmax() - 0.01
    eta_checked = eta
    if(eta_checked > etaMax):
        eta_checked = etaMax
    if(eta_checked < etaMin):
        eta_checked = etaMin
    etaPhiAvg_idxBinX = etaPhiAvg_xAxis.FindBin(eta_checked)
    assert(etaPhiAvg_idxBinX >= 1 and etaPhiAvg_idxBinX <= etaPhiAvg_xAxis.GetNbins())
    etaPhiAvg_yAxis = etaPhiAvg.GetYaxis()
    etaPhiAvg_idxBinY = etaPhiAvg_yAxis.FindBin(phi)
    assert(etaPhiAvg_idxBinY >= 1 and etaPhiAvg_idxBinY <= etaPhiAvg_yAxis.GetNbins())
    effCorr_etaPhi = etaPhi.GetBinContent(etaPhi.FindBin(eta_checked,phi))
    effCorr_etaPhiAvg = etaPhiAvg.GetBinContent(etaPhiAvg.FindBin(eta_checked,phi))
    if(effCorr_etaPhiAvg <= 0.):
        #print("One of the provided tau (eta, phi) values (%3.3f, %3.3f) is outside the boundary of triggering taus" %(eta,phi))
        #print("Returning efficiency = 0.0")
        return 0.
    eff = eff * (effCorr_etaPhi/effCorr_etaPhiAvg)
    if (eff > 1.):
        eff = 1.0
    return eff

def getDiTauEfficiencyData(pt,eta,phi,central_or_shift, diTauData_, diTauEtaPhiData_, diTauEtaPhiAvgData_):
    return getEfficiency(pt,eta,phi,diTauData_,diTauEtaPhiData_,diTauEtaPhiAvgData_,central_or_shift)

def getDiTauEfficiencyMC(pt,eta,phi,central_or_shift,diTauMC_,diTauEtaPhiMC_,diTauEtaPhiAvgMC_):
    return getEfficiency(pt, eta, phi, diTauMC_, diTauEtaPhiMC_, diTauEtaPhiAvgMC_, central_or_shift)

def getDiTauScaleFactor(pt,eta,phi,central_or_shift,diTauMC_,diTauEtaPhiMC_,diTauEtaPhiAvgMC_,diTauData_,diTauEtaPhiData_,diTauEtaPhiAvgData_):
    effData = getDiTauEfficiencyData(pt,eta,phi,central_or_shift,diTauData_,diTauEtaPhiData_,diTauEtaPhiAvgData_)
    effMC = getDiTauEfficiencyMC(pt,eta,phi,central_or_shift,diTauMC_,diTauEtaPhiMC_,diTauEtaPhiAvgMC_)
    if(effMC < 1e-5):
        #print("Eff MC is suspiciously low. Please contact Tau POG.")
        #print(" - DiTau Trigger SF for Tau MVA:   pT: %3.3f   eta: %3.3f   phi: %3.3f" %(pt,eta,phi))
        #print(" - MC Efficiency = %3.3f" %effMC)
        return 0.
    sf = (effData/effMC)
    return sf

def AddDiTauTriggerFactor(File,args):
    print("Setting up file and tree...")
    TheFile = ROOT.TFile(File,"UPDATE")
    TheTree = TheFile.mt_Selected
    
    fTylerN = ROOT.TFile("Weightings/tauTriggerEfficiencies2017_New.root")
    fTyler = ROOT.TFile("Weightings/tauTriggerEfficiencies2017.root")
    mTauData_ = fTylerN.Get("hist_MuTauTriggerEfficiency_tightTauMVA_DATA")
    mTauMC_ = fTylerN.Get("hist_MuTauTriggerEfficiency_tightTauMVA_MC")
    mTauEtaPhiData_ = fTyler.Get("muTau_tight_DATA")
    mTauEtaPhiMC_ = fTyler.Get("muTau_tight_MC")
    mTauEtaPhiAvgData_ = fTyler.Get("muTau_tight_AVG_DATA")
    mTauEtaPhiAvgMC_ = fTyler.Get("muTau_tight_AVG_MC")

    print("Branching...")
    DiTauTriggerWeight = array("f",[0.])
    DiTauTriggerBranch = TheTree.Branch("DiTauTriggerWeight", DiTauTriggerWeight,"DiTauTriggerWeight/F")

    print("Adding Scale Factors...")
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)
        DiTauTriggerWeight[0] = getDiTauScaleFactor(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,0,mTauMC_,mTauEtaPhiMC_,mTauEtaPhiAvgMC_,mTauData_,mTauEtaPhiData_,mTauEtaPhiAvgData_)        
        DiTauTriggerBranch.Fill()
    TheFile.cd()
    TheTree.Write()
    TheFile.Write()
    TheFile.Close()

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Generate and attach di tau trigger scale factor branches")
    parser.add_argument('year',choices=["2016","2017","2018"],help="Select which year's cross sections are to be used")
    parser.add_argument('Files',nargs="+",help="List of files to run the tool on")

    args = parser.parse_args()

    for File in args.Files:
        AddDiTauTriggerFactor(File,args)
