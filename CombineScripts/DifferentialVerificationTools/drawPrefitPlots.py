#!/usr/bin/env python

import ROOT
import argparse
import utilities

def main():
    parser = argparse.ArgumentParser(description="Generate plots for all the directories inside of a given htt combine space")
    parser.add_argument('fileName',help='Specify the file to draw the plots from')
    parser.add_argument('--year',nargs='?',help='Specify the year',default='2016')

    args = parser.parse_args()

    theFile = ROOT.TFile(args.fileName)

    ROOT.gStyle.SetOptStat(0)
        
    for directoryName in theFile.GetListOfKeys():
        theDirectory = theFile.Get(directoryName.GetName())
        theCanvas = ROOT.TCanvas("theCanvas","theCanvas")

        data_obs = theDirectory.Get('data_obs')
        embedded = theDirectory.Get('embedded')
        jetFakes = theDirectory.Get('jetFakes')
        ZL = theDirectory.Get('ZL')

        TT = theDirectory.Get('TTL')
        TT.Add(theDirectory.Get('TTT'))

        Other = theDirectory.Get('VVL')
        Other.Add(theDirectory.Get('VVT'))
        Other.Add(theDirectory.Get('STL'))
        Other.Add(theDirectory.Get('STT'))
        Other.Add(theDirectory.Get('ggH_htt125'))
        Other.Add(theDirectory.Get('qqH_htt125'))
        Other.Add(theDirectory.Get('WH_htt125'))
        Other.Add(theDirectory.Get('ZH_htt125'))       
        
        higgsUpscale = theDirectory.Get('ggH_htt125')
        higgsUpscale.Add(theDirectory.Get('qqH_htt125'))
        higgsUpscale.Add(theDirectory.Get('WH_htt125'))
        higgsUpscale.Add(theDirectory.Get('ZH_htt125'))
        
        higgsUpscale.Scale(30)

        data_obs.SetMarkerStyle(20)
        jetFakes.SetFillColor(ROOT.TColor.GetColor('#ffccff'))
        embedded.SetFillColor(ROOT.TColor.GetColor('#ffcc66'))
        ZL.SetFillColor(ROOT.TColor.GetColor('#4496c8'))
        TT.SetFillColor(ROOT.TColor.GetColor('#9999cc'))
        Other.SetFillColor(ROOT.TColor.GetColor('#12cadd'))
        higgsUpscale.SetLineColor(ROOT.kRed)
        higgsUpscale.SetLineWidth(2)

        backgroundStack = ROOT.THStack('backgroundStack','backgroundStack')
        backgroundStack.Add(jetFakes,'HIST')
        backgroundStack.Add(TT,'HIST')
        backgroundStack.Add(Other,'HIST')
        backgroundStack.Add(embedded,'HIST')
        backgroundStack.Add(ZL,'HIST')

        backgroundStackErrors = utilities.MakeStackErrors(backgroundStack)
        
        thePlotPad,theRatioPad,theRatioHist,theRatioErrors = utilities.MakeRatioPlot(theCanvas,backgroundStack,data_obs,'mass bin',0.7,1.3)

        theRatioPad.cd()
        theRatioHist.Draw('ex0')
        theRatioErrors.Draw('SAME e2')
        theRatioHist.Draw('SAME ex0')
        theRatioPad.Draw()

        thePlotPad.cd()
        thePlotPad.SetTickx()
        thePlotPad.SetTicky()
        thePlotPad.SetLogy()
        
        backgroundStack.SetMaximum(max(backgroundStack.GetMaximum(),data_obs.GetMaximum())*1.1)
        backgroundStack.SetMinimum(1.0)

        backgroundStack.Draw()
        backgroundStackErrors.Draw('SAME e2')
        backgroundStack.SetTitle(theDirectory.GetName())
        data_obs.Draw('SAME e1')
        higgsUpscale.Draw('SAME HIST')
        backgroundStack.GetYaxis().SetTitle('Events')
        backgroundStack.GetYaxis().SetTitleOffset(1.58)
        backgroundStack.GetXaxis().SetLabelSize(0.0)

        theLegend = ROOT.TLegend(0.9,0.6,1.0,0.9)
        theLegend.AddEntry(data_obs,'Observed','pe')
        theLegend.AddEntry(embedded,'Embedded','f')
        theLegend.AddEntry(Other,'Other','f')
        theLegend.AddEntry(ZL,'DY #rightarrow ll','f')
        theLegend.AddEntry(TT,'t#bar{t}','f')
        theLegend.AddEntry(jetFakes,'Fakes','f')
        theLegend.AddEntry(higgsUpscale,'All Higgs (#times 30)','l')
        theLegend.Draw()

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
        latex.SetTextSize(0.6*thePlotPad.GetTopMargin())
        latex.DrawLatex(1.0-thePlotPad.GetRightMargin(),1.01-thePlotPad.GetTopMargin(),lumiText)

        latex.SetTextFont(61)
        latex.SetTextSize(0.75*thePlotPad.GetTopMargin())
        latex.DrawLatex(0.18,1.01-thePlotPad.GetTopMargin(),"CMS")

        latex.SetTextFont(52)
        latex.SetTextSize(0.76*0.75*thePlotPad.GetTopMargin())
        latex.DrawLatex(0.33,1.01-thePlotPad.GetTopMargin(),"Preliminary")

        thePlotPad.Draw()

        theCanvas.SaveAs(theDirectory.GetName()+'.png')

        #raw_input("Press Enter to Continue...")
        
if __name__ == '__main__':
    main()
