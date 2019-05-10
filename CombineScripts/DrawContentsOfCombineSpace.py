import ROOT
import argparse
from tqdm import tqdm
import math

def MakeRatioPlot(TheCanvas,TheStack,TheData,XAxisLabel,YBoundDown,YBoundUp):
    PlotPad = ROOT.TPad("pad1","plot",0.,0.20,1.,1.)
    PlotPad.Draw()
    RatioPad = ROOT.TPad("pad2","ratio",0.,0.,1.,0.25)
    RatioPad.Draw()

    PlotPad.cd()
    RatioPad.SetTopMargin(0.0)
    RatioPad.SetBottomMargin(0.08)
    RatioPad.SetGridy()

    RatioHist = ROOT.TH1F("Ratio","",
                          TheData.GetNbinsX(),
                          TheData.GetXaxis().GetXmin(),
                          TheData.GetXaxis().GetXmax())
    RatioHist.Sumw2()
    RatioHist.Add(TheData)

    DenominatorHistos = ROOT.TH1F("DenominatorHistos","DenominatorHistos",
                                  TheData.GetNbinsX(),
                                  TheData.GetXaxis().GetXmin(),
                                  TheData.GetXaxis().GetXmax())
    
    ListOfStackHistograms = TheStack.GetHists()
    for i in range(TheStack.GetNhists()):
        DenominatorHistos.Add(TheStack.GetHists().At(i))
    RatioHist.Divide(DenominatorHistos)
    FinalRatioHist = ROOT.TH1F("FinalRatio","",
                               RatioHist.GetNbinsX(),
                               RatioHist.GetXaxis().GetXmin(),
                               RatioHist.GetXaxis().GetXmax())

    for i in range(1,FinalRatioHist.GetNbinsX()+1):
        FinalRatioHist.SetBinContent(i,RatioHist.GetBinContent(i))
        try:
            FinalRatioHist.SetBinError(i,(TheData.GetBinError(i)/TheData.GetBinContent(i))*RatioHist.GetBinContent(i))
        except ZeroDivisionError:
            print("Division By zero in ratio bin errors.")
            print("Setting bin: "+str(i)+" to zero")
            FinalRatioHist.SetBinError(i,0)
    
    FinalRatioHist.SetMarkerStyle(20)
    
    FinalRatioHist.GetYaxis().SetTitle("Data/Predicted")
    FinalRatioHist.GetYaxis().SetTitleSize(0.1)
    FinalRatioHist.GetYaxis().SetTitleOffset(0.32)
    FinalRatioHist.GetYaxis().CenterTitle()
    FinalRatioHist.GetYaxis().SetLabelSize(0.10)
    FinalRatioHist.GetYaxis().SetNdivisions(6,0,0)
    FinalRatioHist.GetYaxis().SetRangeUser(YBoundDown*0.95,YBoundUp*1.05)

    FinalRatioHist.GetXaxis().SetLabelSize(0.10)
    
    FinalRatioHist.GetXaxis().SetTitle(XAxisLabel)
    FinalRatioHist.GetXaxis().SetTitleSize(0.14)

    MCErrors = ROOT.TH1F("MCErrors","MCErrors",
                         RatioHist.GetNbinsX(),
                         RatioHist.GetXaxis().GetXmin(),
                         RatioHist.GetXaxis().GetXmax())

    for i in range (1,MCErrors.GetNbinsX()+1):
        MCErrors.SetBinContent(i,1.0)
        try:
            MCErrors.SetBinError(i,DenominatorHistos.GetBinError(i)/DenominatorHistos.GetBinContent(i))
        except:
            print("No background predicted in ratio plot errors for bin: "+str(i))
            print("Setting it to zero")
            MCErrors.SetBinError(i,0)

    MCErrors.SetFillStyle(3001)
    MCErrors.SetFillColor(15)    

    #RatioPad.cd()
    #FinalRatioHist.Draw("ex0")
    #MCErrors.Draw("SAME e2")
    #FinalRatioHist.Draw("SAME ex0")    
    #RatioPad.Draw()
    #PlotPad.cd()

    #RatioPad.ls()
    #FinalRatioHist.Print()
    #MCErrors.Print()
    #raw_input("Done Drawing Ratio. Press Enter...")

    return PlotPad,RatioPad,FinalRatioHist,MCErrors

def MakeStackErrors(TheStack):
    DenominatorHistos = ROOT.TH1F("DenominatorHistos","DenominatorHistos",
                                  TheStack.GetHists().At(0).GetNbinsX(),
                                  TheStack.GetHists().At(0).GetXaxis().GetXmin(),
                                  TheStack.GetHists().At(0).GetXaxis().GetXmax())
    for i in range(TheStack.GetNhists()):
        DenominatorHistos.Add(TheStack.GetHists().At(i))
    TheErrorHisto = ROOT.TH1F("TheErrorHisto","",
                              DenominatorHistos.GetNbinsX(),
                              DenominatorHistos.GetXaxis().GetXmin(),
                              DenominatorHistos.GetXaxis().GetXmax())

    for i in range(1,DenominatorHistos.GetNbinsX()+1):
        TheErrorHisto.SetBinContent(i,DenominatorHistos.GetBinContent(i))
        TheErrorHisto.SetBinError(i,DenominatorHistos.GetBinError(i))
    TheErrorHisto.SetLineColor(0)
    TheErrorHisto.SetLineWidth(0)
    TheErrorHisto.SetMarkerSize(0)
    TheErrorHisto.SetFillStyle(3001)
    TheErrorHisto.SetFillColor(15)
    return TheErrorHisto

def DrawDirectoryContents(TheDirectory,args):
    ROOT.gStyle.SetOptStat(0)

    TheCanvas = ROOT.TCanvas("TheCanvas","TheCanvas")

    data_obs = TheDirectory.Get("data_obs")
    jetFakes = TheDirectory.Get("jetFakes")
    if args.year=='2018':
        ZT = TheDirectory.Get("ZT")
    elif args.year == '2017':
        ZT.year = TheDirectory.Get("embedded")
    ZL = TheDirectory.Get("ZL")
    TT = TheDirectory.Get("TTL")
    if args.year=='2018':
        TT.Add(TheDirectory.Get("TTT"))
    #create the other category
    Other = TheDirectory.Get("VVL")
    Other.Add(TheDirectory.Get("qqH_htt125"))
    Other.Add(TheDirectory.Get("ggH_htt125"))
    Other.Add(TheDirectory.Get("WH_htt125"))
    Other.Add(TheDirectory.Get("ZH_htt125"))
    if args.year == '2018':
        Other.Add(TheDirectory.Get("VVT"))    
    HiggsUpscale = TheDirectory.Get("qqH_htt125") #create the upscale
    HiggsUpscale.Add(TheDirectory.Get("ggH_htt125"))
    HiggsUpscale.Add(TheDirectory.Get("WH_htt125"))
    HiggsUpscale.Add(TheDirectory.Get("ZH_htt125"))
    HiggsUpscale.Scale(30.0)

    #verify STXS bin integrals
    ggH = TheDirectory.Get("ggH_htt125")
    qqH = TheDirectory.Get("qqH_htt125")
    
    ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125")
    ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125")
    ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125")
    ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125")
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125")
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125")
    ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125 = TheDirectory.Get("ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125")
    ggH_PTH_0_200_1J_PTH_120_200_htt125 = TheDirectory.Get("ggH_PTH_0_200_1J_PTH_120_200_htt125")
    ggH_PTH_0_200_1J_PTH_60_120_htt125 = TheDirectory.Get("ggH_PTH_0_200_1J_PTH_60_120_htt125")
    ggH_PTH_0_200_1J_PTH_0_60_htt125 = TheDirectory.Get("ggH_PTH_0_200_1J_PTH_0_60_htt125")
    ggH_PTH_0_200_0J_PTH_10_200_htt125 = TheDirectory.Get("ggH_PTH_0_200_0J_PTH_10_200_htt125")
    ggH_PTH_0_200_0J_PTH_0_10_htt125 = TheDirectory.Get("ggH_PTH_0_200_0J_PTH_0_10_htt125")
    ggH_PTH_GE200_htt125 = TheDirectory.Get("ggH_PTH_GE200_htt125")
    
    ggHIntegral = ggH.Integral()
    ggH_STXS_Integral = ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_0_25_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_GE25_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_GE700_PTHJJ_GE25_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_350_700_PTHJJ_0_25_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_120_200_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_60_120_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_GE2J_MJJ_0_350_PTH_0_60_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_1J_PTH_120_200_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_1J_PTH_60_120_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_1J_PTH_0_60_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_0J_PTH_10_200_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_0_200_0J_PTH_0_10_htt125.Integral()
    ggH_STXS_Integral += ggH_PTH_GE200_htt125.Integral()
    
    print("ggH Integral: "+str(ggHIntegral)+" STXS bins: "+str(ggH_STXS_Integral))

    qqH_htt125 = TheDirectory.Get("qqH_htt125")
    qqH_0J_htt125 = TheDirectory.Get("qqH_0J_htt125")
    qqH_1J_htt125 = TheDirectory.Get("qqH_1J_htt125")
    qqH_GE2J_MJJ_0_60_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_0_60_htt125")
    qqH_GE2J_MJJ_60_120_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_60_120_htt125")
    qqH_GE2J_MJJ_120_350_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_120_350_htt125")
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125")
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125")
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125")
    qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125")
    qqH_GE2J_MJJ_GE350_PTH_GE200_htt125 = TheDirectory.Get("qqH_GE2J_MJJ_GE350_PTH_GE200_htt125")

    qqHIntegral = qqH_htt125.Integral()
    qqH_STXS_Integral = qqH_0J_htt125.Integral()
    qqH_STXS_Integral += qqH_1J_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_0_60_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_60_120_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_120_350_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_0_25_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_350_700_PTHJJ_GE25_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_0_25_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_GE350_PTH_0_200_MJJ_GE700_PTHJJ_GE25_htt125.Integral()
    qqH_STXS_Integral += qqH_GE2J_MJJ_GE350_PTH_GE200_htt125.Integral()

    print("qqH Integral: "+str(qqHIntegral)+" STXS Bins: "+str(qqH_STXS_Integral))

    #Color Corrections
    data_obs.SetMarkerStyle(20)
    jetFakes.SetFillColor(ROOT.TColor.GetColor("#ffccff"))
    ZT.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))
    ZL.SetFillColor(ROOT.TColor.GetColor("#4496c8"))
    TT.SetFillColor(ROOT.TColor.GetColor("#9999cc"))
    Other.SetFillColor(ROOT.TColor.GetColor("#12cadd"))
    HiggsUpscale.SetLineColor(ROOT.kRed)
    HiggsUpscale.SetLineWidth(2)

    #Signal blinding
    for i in range(1,data_obs.GetNbinsX()+1):
        SignalContribution = HiggsUpscale.GetBinContent(i) / 30.0
        NonHiggsOtherContribution = Other.GetBinContent(i) - SignalContribution
        TotalBackgroundContribution = NonHiggsOtherContribution + jetFakes.GetBinContent(i) + ZT.GetBinContent(i)+ZL.GetBinContent(i)+TT.GetBinContent(i)
        try:
            if SignalContribution/math.sqrt(TotalBackgroundContribution) > 0.5:
                data_obs.SetBinContent(i,-1.0)
        except ZeroDivisionError:
            print("No background contribution predicted in bin: "+str(i))
            print("Not blinding this bin???")
        except ValueError:
            print("Negative Background in this bin.")
            print("Not blinding this bin.")
    BackgroundStack = ROOT.THStack("BackgroundStack","BackgroundStack")
    BackgroundStack.Add(Other,"HIST")
    BackgroundStack.Add(TT,"HIST")
    BackgroundStack.Add(ZL,"HIST")
    BackgroundStack.Add(jetFakes,"HIST")
    BackgroundStack.Add(ZT,"HIST")

    TheErrors = MakeStackErrors(BackgroundStack)

    ThePlotPad,TheRatioPad,TheRatioHist,TheRatioErrors = MakeRatioPlot(TheCanvas,BackgroundStack,data_obs,"mass bin",0.7,1.3)

    TheRatioPad.cd()
    TheRatioHist.Draw("ex0")
    TheRatioErrors.Draw("SAME e2")
    TheRatioHist.Draw("SAME ex0")
    TheRatioPad.Draw()

    ThePlotPad.cd()
    ThePlotPad.SetTickx()
    ThePlotPad.SetTicky()
    ThePlotPad.SetGridx()
    ThePlotPad.SetLogy()
    
    #RatioPad = TheCanvas.FindObject("pad2")
    #RatioPad.ls()
    #RatioHist = RatioPad.FindObject("FinalRatio")
    #RatioHist.Print()

    BackgroundStack.SetMaximum(max(BackgroundStack.GetMaximum(),data_obs.GetMaximum())*1.1)

    BackgroundStack.Draw()
    TheErrors.Draw("SAME e2")
    BackgroundStack.SetTitle(TheDirectory.GetName())
    data_obs.Draw("SAME e1")
    HiggsUpscale.Draw("SAME HIST")
    BackgroundStack.GetYaxis().SetTitle("Events")
    BackgroundStack.GetYaxis().SetTitleOffset(1.58)
    BackgroundStack.GetXaxis().SetLabelSize(0.0)

    TheLegend = ROOT.TLegend(0.9,0.6,1.0,0.9)
    TheLegend.AddEntry(data_obs,"Observed","pe")
    TheLegend.AddEntry(ZT,"DY #rightarrow #tau#tau","f")
    TheLegend.AddEntry(Other,"Other","f")
    TheLegend.AddEntry(ZL,"DY #rightarrow ll","f")
    TheLegend.AddEntry(TT,"t#bar{t}","f")
    TheLegend.AddEntry(jetFakes,"Fakes","f")
    TheLegend.AddEntry(HiggsUpscale,"All Higgs (#times 30)","l")
    TheLegend.Draw()

    TheCanvas.Draw()
    #TheCanvas.SaveAs("PrefitCheck/"+TheDirectory.GetName()+".png")
    
    #ROOT.gSystem.ProcessEvents()
    #Image = ROOT.TImage.Create()
    #Image.FromPad(TheCanvas)
    #Image.WriteImage("PrefitCheck/"+TheDirectory.GetName()+".png")

    #Create Grid Divisions
    numCategories = (BackgroundStack.GetHistogram().GetNbinsX())/11
    print("Number of unrolled bins: "+str(numCategories))
    TheGridDivisions = ROOT.TH1F("GridDivisions","GridDivisions",
                                 HiggsUpscale.GetNbinsX(),
                                 HiggsUpscale.GetXaxis().GetXmin(),
                                 HiggsUpscale.GetXaxis().GetXmax())    
    BackgroundStack.GetXaxis().SetNdivisions(-500-numCategories)
    TheGridDivisions.GetXaxis().SetNdivisions(-500-numCategories)
    #TheGridDivisions.Draw("SAME")

    if args.year == "2018":
        lumiText = "13 TeV, 59.7 fb^{-1}"
    elif args.year == "2017":
        lumiText = "13 TeV, 41.5 fb^{-1}"
    elif args.year == "2016":
        lumiText = "13 TeV, 35.9 fb^{-1}"

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)
    latex.SetTextFont(42)
    latex.SetTextAlign(31)
    latex.SetTextSize(0.6*ThePlotPad.GetTopMargin())
    latex.DrawLatex(1.0-ThePlotPad.GetRightMargin(),1.01-ThePlotPad.GetTopMargin(),lumiText)

    latex.SetTextFont(61)
    latex.SetTextSize(0.75*ThePlotPad.GetTopMargin())
    latex.DrawLatex(0.18,1.01-ThePlotPad.GetTopMargin(),"CMS")

    latex.SetTextFont(52)
    latex.SetTextSize(0.76*0.75*ThePlotPad.GetTopMargin())
    latex.DrawLatex(0.33,1.01-ThePlotPad.GetTopMargin(),"Preliminary")

    ThePlotPad.Draw()

    raw_input("Press Enter to Continue...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate plots for all the directories inside of a given htt combine space (provided all the names are familiar)")
    parser.add_argument('year',choices=['2016','2017','2018'],help="Specify the year of the files")
    parser.add_argument('CombineFile',help="Specify the file to draw the plots from")

    args = parser.parse_args()

    TheFile = ROOT.TFile(args.CombineFile)
    
    for Directory in TheFile.GetListOfKeys():
        TheDirectory = TheFile.Get(Directory.GetName())
        DrawDirectoryContents(TheDirectory,args)
