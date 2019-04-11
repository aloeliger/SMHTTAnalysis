import ROOT
import argparse
import math
from tqdm import tqdm

def CalculateMT(MuonVector,METVector):
    return math.sqrt(2.0*MuonVector.Pt()*METVector.Pt()*(1.0-math.cos(MuonVector.DeltaPhi(METVector))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="measure a lnN uncertainty on embedded")
    parser.add_argument('File',nargs='?',help="File to measure the uncertainty on")

    args = parser.parse_args()

    TheFile = ROOT.TFile(args.File)

    FirstScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_v17_5.root")
    FirstWorkSpace = FirstScaleFactorFile.w

    SecondScaleFactorFile = ROOT.TFile("/data/aloeliger/CMSSW_9_4_0/src/SMHTTAnalysis/NtuplePolishing/Weightings/htt_scalefactors_2017_v2.root")
    SecondWorkSpace = SecondScaleFactorFile.w    

    TheNominalHisto = ROOT.TH1F("NominalHisto","NominalHisto",1,0.0,9000.0)
    TheOneProngUpHisto = ROOT.TH1F("OneProngUpHisto","OneProngUpHisto",1,0.0,9000.0)
    TheOneProngDownHisto = ROOT.TH1F("OneProngDownHisto","OneProngDownHisto",1,0.0,9000.0)
    TheThreeProngUpHisto = ROOT.TH1F("ThreeProngUpHisto","ThreeProngUpHisto",1,0.0,9000.0)
    TheThreeProngDownHisto = ROOT.TH1F("ThreeProngDownHisto","ThreeProngDownHisto",1,0.0,9000.0)
    
    for i in tqdm(range(TheFile.mt_Selected.GetEntries())):
        TheFile.mt_Selected.GetEntry(i)
        
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheFile.mt_Selected.pt_1,TheFile.mt_Selected.eta_1,TheFile.mt_Selected.phi_1,TheFile.mt_Selected.m_1)
        TauVector.SetPtEtaPhiM(TheFile.mt_Selected.pt_2,TheFile.mt_Selected.eta_2,TheFile.mt_Selected.phi_2,TheFile.mt_Selected.m_2)
        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(TheFile.mt_Selected.met,0.0,TheFile.mt_Selected.metphi,0.0)

        MT = CalculateMT(MuVector,MetVector)
        
        if(TauVector.Pt() < 30 or MuVector.Pt() < 26 or MT > 50.0):
            continue

        Weight = TheFile.mt_Selected.CrossSectionWeighting
        Weight = Weight * 0.97
                
        if(TheFile.mt_Selected.gen_match_2 == 2
           or TheFile.mt_Selected.gen_match_2 == 4):
            if(abs(TauVector.Eta())<0.4):
                Weight = Weight * 1.17
            elif(abs(TauVector.Eta())<0.8):
                Weight = Weight * 1.29
            elif(abs(TauVector.Eta())<1.2):
                Weight = Weight*1.14
            elif(abs(TauVector.Eta())<1.7):
                Weight = Weight*0.93      
            elif(abs(TauVector.Eta())<2.3):
                Weight = Weight*1.61

        Trigger24 = (TheFile.mt_Selected.passMu24 and TheFile.mt_Selected.matchMu24_1 
                     and TheFile.mt_Selected.filterMu24_1 and TheFile.mt_Selected.pt_1 > 25.0)
        Trigger27 = (TheFile.mt_Selected.passMu27 and TheFile.mt_Selected.matchMu27_1 
                     and TheFile.mt_Selected.filterMu27_1 and TheFile.mt_Selected.pt_1 > 28.0)
    #no tau trigger matching in embedded        
        Trigger2027 = (TheFile.mt_Selected.passMu20Tau27 and TheFile.mt_Selected.matchMu20Tau27_1 
                       and TheFile.mt_Selected.filterMu20Tau27_1
                       and TheFile.mt_Selected.pt_1 > 21 and TheFile.mt_Selected.pt_2 > 31 
                       and TheFile.mt_Selected.pt_1 < 25
                       and abs(TheFile.mt_Selected.eta_2 < 2.1))

            #Embedded trigger whatever            
        if TheFile.mt_Selected.l2_decayMode == 0:
            Weight = Weight * 0.975
        elif TheFile.mt_Selected.l2_decayMode == 1:
            Weight = Weight * 0.975 * 1.051
        elif TheFile.mt_Selected.l2_decayMode == 10:
            Weight = Weight * 0.975 * 0.975 * 0.975
        FirstWorkSpace.var("m_pt").setVal(MuVector.Pt())
        FirstWorkSpace.var("m_eta").setVal(MuVector.Eta())
        FirstWorkSpace.var("gt_pt").setVal(MuVector.Pt())
        FirstWorkSpace.var("gt_eta").setVal(MuVector.Eta())
        Weight = Weight * FirstWorkSpace.function("m_sel_idEmb_ratio").getVal()
        FirstWorkSpace.var("gt_pt").setVal(TauVector.Pt())
        FirstWorkSpace.var("gt_eta").setVal(TauVector.Eta())
        Weight = Weight * FirstWorkSpace.function("m_sel_idEmb_ratio").getVal()
        FirstWorkSpace.var("gt1_pt").setVal(MuVector.Pt())
        FirstWorkSpace.var("gt1_eta").setVal(MuVector.Eta())
        FirstWorkSpace.var("gt2_pt").setVal(TauVector.Pt())
        FirstWorkSpace.var("gt2_eta").setVal(TauVector.Eta())
        Weight=Weight*FirstWorkSpace.function("m_sel_trg_ratio").getVal()
        Weight=Weight*FirstWorkSpace.function("m_iso_binned_embed_kit_ratio").getVal()
        Weight = Weight*FirstWorkSpace.function("m_id_embed_kit_ratio").getVal()
        if(Trigger24 or Trigger27):
            Weight = Weight*FirstWorkSpace.function("m_trg24_27_embed_kit_ratio").getVal()
        
        Weight = Weight * TheFile.mt_Selected.ZPTWeighting
        
        #now we do the interesting stuff
        OneProngUpWeight = Weight
        ThreeProngUpWeight = Weight
        OneProngDownWeight = Weight
        ThreeProngDownWeight = Weight        
        if TheFile.mt_Selected.l2_decayMode == 0:            
            OneProngPpWeight  = OneProngUpWeight * (0.975 + 0.008)
            ThreeProngUpWeight = ThreeProngUpWeight * 0.975
            OneProngDownWeight = OneProngDownWeight * (0.975 - 0.008)
            ThreeProngDownWeight = ThreeProngDownWeight * 0.975
            Weight = Weight * 0.975
        elif TheFile.mt_Selected.l2_decayMode == 1:            
            OneProngUpWeight = OneProngUpWeight * (0.975 + 0.008) * 1.051
            ThreeProngUpWeight = ThreeProngUpWeight * 0.975 * 1.051
            OneProngDownWeight = OneProngDownWeight * (0.975 - 0.008) * 1.051
            ThreeProngDownWeight = ThreeProngDownWeight * 0.975
            Weight = Weight * 0.975 * 1.051
        elif TheFile.mt_Selected.l2_decayMode == 10:           
            OneProngUpWeight = OneProngUpWeight * 0.975 * 0.975 * 0.975
            ThreeProngUpWeight = ThreeProngUpWeight * (0.975 + 0.008) * (0.975 + 0.008) * (0.975 + 0.008)
            OneProngDownWeight = OneProngDownWeight * 0.975 * 0.975 * 0.975
            ThreeProngDownWeight = ThreeProngDownWeight * (0.975 - 0.008) * (0.975 - 0.008) *(0.975 - 0.008)
            Weight = Weight * 0.975 * 0.975 * 0.975            
        #now we fill            
        TheNominalHisto.Fill(TauVector.Pt(),Weight)        
        TheOneProngUpHisto.Fill(TauVector.Pt(),OneProngUpWeight)
        TheOneProngDownHisto.Fill(TauVector.Pt(),OneProngDownWeight)
        TheThreeProngUpHisto.Fill(TauVector.Pt(),ThreeProngUpWeight)
        TheThreeProngDownHisto.Fill(TauVector.Pt(),ThreeProngDownWeight)
    print("OneProngUp/Nominal: "+str(TheOneProngUpHisto.Integral()/TheNominalHisto.Integral()))
    print("OneProngDown/Nominal: "+str(TheOneProngDownHisto.Integral()/TheNominalHisto.Integral()))
    print("ThreeProngUp/Nominal: "+str(TheThreeProngUpHisto.Integral()/TheNominalHisto.Integral()))
    print("ThreeProngDown/Nominal: "+str(TheThreeProngDownHisto.Integral()/TheNominalHisto.Integral()))
