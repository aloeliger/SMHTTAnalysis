import ROOT
from tqdm import tqdm
TempFile = ROOT.TFile("/nfs_scratch/aloeliger/SMHTT2017Sync/VBF.root")
MetUpHisto = ROOT.TH1F("MetUp","MetUp",20,0.0,200.0)
MetDownHisto = ROOT.TH1F("MetDown","MetDown",20,0.0,200.0)
MetHisto = ROOT.TH1F("Met","Met",20,0.0,200.0)
MetUESUpHisto = ROOT.TH1F("MetUESUp","MetUESUp",20,0.0,200.0)
MetUESDownHisto = ROOT.TH1F("MetUESDown","MetUESDown",20,0.0,200.0)

for i in tqdm(range(TempFile.mutau_tree.GetEntries())):
    TempFile.mutau_tree.GetEntry(i)
    MetVector = ROOT.TLorentzVector()    
    MetVector.SetPtEtaPhiM(TempFile.mutau_tree.met,0,TempFile.mutau_tree.metphi,0)

    MetUpVector = ROOT.TLorentzVector()    
    MetUpVector.SetXYZM(TempFile.mutau_tree.met_RecUnc_X_UP,
                        TempFile.mutau_tree.met_RecUnc_Y_UP,
                        0,
                        0)        

    MetDownVector = ROOT.TLorentzVector()
    MetDownVector.SetXYZM(TempFile.mutau_tree.met_RecUnc_X_DOWN,
                          TempFile.mutau_tree.met_RecUnc_Y_DOWN,
                          0,
                          0)
    
    MetUESUpHisto.Fill(TempFile.mutau_tree.met_UESUp)
    MetUESDownHisto.Fill(TempFile.mutau_tree.met_UESDown)
    MetHisto.Fill(MetVector.E())
    MetUpHisto.Fill(MetUpVector.E())
    MetDownHisto.Fill(MetDownVector.E())

CanvasOne = ROOT.TCanvas("CanvasOne","CanvasOne")
MetUpHisto.SetLineColor(ROOT.kRed)
MetDownHisto.SetLineColor(ROOT.kBlue)
MetHisto.SetLineColor(ROOT.kBlack)
MetUESUpHisto.SetLineColor(ROOT.kGreen)
MetUESDownHisto.SetLineColor(ROOT.kOrange)

MetHisto.Draw()
MetUpHisto.Draw("SAME")
MetDownHisto.Draw("SAME")
MetUESUpHisto.Draw("SAME")
MetUESDownHisto.Draw("SAME")

CanvasOne.SaveAs("MetPlot.png")
    
