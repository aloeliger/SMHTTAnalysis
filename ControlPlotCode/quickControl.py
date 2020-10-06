#!/usr/bin/env python
#generate control plots quicker and without the need to go through explicit tqdm/for loop combinations
#Instead we'll use in place ROOT/TTree Draw components

import ROOT
import argparse

variableSettingDictionary = {
    'pt_2':'25,30.0,80.0',
    'eta_2':'45,-2.5,2.5',
    'pt_1':'30,20.0,80.0',
    'eta_1':'48,-2.4,2.4',
    'm_vis':'30,50.0,200.0',
    'm_sv':'25,50.0,300.0',
    'njets':'6,0.0,6.0',
    'HiggsPt':'40,0.0,400.0',
    'met':'40,0.0,400.0',
    'DeltaR':'40,0.0,6.0',
    'mjj':'20,0.0,500.0',
    'abs(eta_1-eta_2)':'45,0.0,2.5',
    'jpt_1':'50,0.0,200.0',
    'jeta_1':'50,-5.0,5.0',
    'jpt_2':'50,0.0,200.0',
    'jeta_2':'50,-5.0,5.0',
    'MT':'20,0.0,200.0',
}

variableAxisTitleDictionary = {
    'pt_2':'#tau p_{t}',
    'eta_2':'#tau #eta',
    'pt_1':'#mu p_{t}',
    'eta_1':'#mu #eta',
    'm_vis':'m_{vis}',
    'm_sv':'m_{#tau#tau}',
    'njets':'N_{jets}',
    'HiggsPt':'Higgs p_{t}',
    'met':'MET',
    'DeltaR':'#Delta r_{#mu,#tau}',
    'mjj':'m_{jj}',
    'abs(eta_1-eta_2)':'#Delta#eta_{jj}',
    'jpt_1':'p_{t} j_{1}',
    'jeta_1':'#eta j_{1}',
    'jpt_2':'p_{t} j_{2}',
    'jeta_2':'#eta j_{2}',    
    'MT':'Transverse Mass',
    }

#just compile our standard cutting and weighting string for ttree.draw()
def CreateCutString(standardCutString,
                    otherCuts,
                    weighting='FinalWeighting'):
    cutString = weighting+'*('+standardCutString+' && '
    for cut in otherCuts:
        cutString += cut+' && '
    cutString = cutString[:len(cutString)-3]
    cutString+=')'
    return cutString

#quick macro to cut 3 repeated lines of code down into one.
def StandardDraw(theFile,
                 variable,
                 standardCutString,
                 additionalSelections,
                 histogramName='h',
                 theWeight = 'FinalWeighting'):
    theFile.mt_Selected.Draw(variable+'>>'+histogramName+'('+variableSettingDictionary[variable]+')',
                             CreateCutString(standardCutString,
                                             additionalSelections,
                                             weighting=theWeight))
    #so, if the tree has no entries, root doesn't even hand back an empty histogram
    # and therefore this ends up trying to get clone a none type
    #pass the None forward, and we can let the Add handle this
    try:
        theHisto = ROOT.gDirectory.Get(histogramName).Clone()
    except ReferenceError:
        theHisto = None
    return theHisto

#make the statistical errors on the prediction stack
def MakeStackErrors(theStack):
    denominatorHistos = theStack.GetHists().At(0).Clone()
    denominatorHistos.Reset()

    for i in range(0,theStack.GetNhists()):
        denominatorHistos.Add(theStack.GetHists().At(i))
    
    theErrorHisto = denominatorHistos.Clone()
    theErrorHisto.Reset()
    
    for i in range(0,denominatorHistos.GetNbinsX()+1):
        theErrorHisto.SetBinContent(i,denominatorHistos.GetBinContent(i))
        theErrorHisto.SetBinError(i,denominatorHistos.GetBinError(i))
    theErrorHisto.SetLineColor(0)
    theErrorHisto.SetLineWidth(0)
    theErrorHisto.SetMarkerStyle(0)
    theErrorHisto.SetFillStyle(3001)
    theErrorHisto.SetFillColor(15)
    return theErrorHisto

#make the ratio histograms and associated errors
def MakeRatioHistograms(dataHisto,backgroundStack,variable):
    ratioHist = dataHisto.Clone()

    denominatorHistos = dataHisto.Clone()
    denominatorHistos.Reset()
    for i in range(0,backgroundStack.GetNhists()):
        denominatorHistos.Add(backgroundStack.GetHists().At(i))
    ratioHist.Divide(denominatorHistos)
    finalRatioHist = ratioHist.Clone()
    for i in range(1,finalRatioHist.GetNbinsX()+1):
        try:
            finalRatioHist.SetBinError(i,dataHisto.GetBinError(i)/dataHisto.GetBinContent(i)*ratioHist.GetBinContent(i))
        except ZeroDivisionError:
            finalRatioHist.SetBinError(i,0)

    finalRatioHist.SetMarkerStyle(20)
    finalRatioHist.SetTitle("")
    finalRatioHist.GetYaxis().SetTitle("Data/Predicted")
    finalRatioHist.GetYaxis().SetTitleSize(0.1)
    finalRatioHist.GetYaxis().SetTitleOffset(0.32)
    finalRatioHist.GetYaxis().CenterTitle()
    finalRatioHist.GetYaxis().SetLabelSize(0.1)
    finalRatioHist.GetYaxis().SetNdivisions(6,0,0)
    #finalRatioHist.GetYaxis().SetRangeUser(1.3*1.05,0.7*0.95) #this doesn't seem to take effect here?    
    finalRatioHist.GetXaxis().SetTitleOffset(0.75)
    finalRatioHist.SetMaximum(1.3)
    finalRatioHist.SetMinimum(0.7)

    finalRatioHist.GetXaxis().SetLabelSize(0.1)

    finalRatioHist.GetXaxis().SetTitle(variableAxisTitleDictionary[variable])
    finalRatioHist.GetXaxis().SetTitleSize(0.14)

    MCErrors = ratioHist.Clone()
    MCErrors.Reset()
    for i in range(1,MCErrors.GetNbinsX()+1):
        MCErrors.SetBinContent(i,1.0)
        try:
            MCErrors.SetBinError(i,denominatorHistos.GetBinError(i)/denominatorHistos.GetBinContent(i))
        except ZeroDivisionError:
            MCErrors.SetBinError(i,0)
    MCErrors.SetFillStyle(3001)
    MCErrors.SetFillColor(15)
    MCErrors.SetMarkerStyle(0)

    return finalRatioHist,MCErrors

def main():
    parser = argparse.ArgumentParser(description='Generate control plots quick.')    
    parser.add_argument('--year',
                        nargs='?',
                        choices=['2016','2017','2018'],
                        help='Use the file\'s fake factor weightings when making plots for these files.',
                        required=True)
    parser.add_argument('--variables',
                        nargs='+',
                        help='Variables to draw the control plots for',
                        default=['pt_2',
                                 'eta_2',
                                 'pt_1',
                                 'eta_1',
                                 'm_vis',
                                 'm_sv',
                                 'njets',
                                 'HiggsPt',
                                 'met',
                                 'DeltaR',
                                 'mjj',
                                 'abs(eta_1-eta_2)',
                                 'jpt_1',
                                 'jeta_1',
                                 'jpt_2',
                                 'jeta_2',])
    parser.add_argument('--additionalSelections',
                        nargs='+',
                        help='additional region selections',
                        default=[])
    parser.add_argument('--pause',
                        help='pause after drawing each plot to make it easier to view',
                        action='store_true')
    parser.add_argument('--standardCutString',
                        nargs='?',
                        help='Change the standard cutting definition',
                        default='pt_2 > 30 && MT < 50')
    parser.add_argument('--changeHistogramBounds',
                        nargs = '?',
                        help = 'Change the standard histogram bounding (affects all histograms)')

    args = parser.parse_args()    

    ROOT.gStyle.SetOptStat(0)

    #change the standard cut definition if that's available

    #okay, let's grab some files and get to work
    if args.year == '2016':
        dataPath = '/data/aloeliger/SMHTT_Selected_2016_Deep/'
    elif args.year == '2017':
        dataPath = '/data/aloeliger/SMHTT_Selected_2017_Deep/'
    elif args.year == '2018':
        dataPath = '/data/aloeliger/SMHTT_Selected_2018_Deep/'

    ZLFile = ROOT.TFile(dataPath+'DY.root')
    dataFile = ROOT.TFile(dataPath+'Data.root')
    EWKZLLFile = ROOT.TFile(dataPath+'EWKZLL.root')
    EWKZNuNuFile = ROOT.TFile(dataPath+'EWKZNuNu.root')
    embeddedFile = ROOT.TFile(dataPath+'Embedded.root')
    fakesFile = ROOT.TFile(dataPath+'Fake.root')    
    GGHWWFile = ROOT.TFile(dataPath+'GGHWW.root')
    GGZHLLTTFile = ROOT.TFile(dataPath+'GGZHLLTT.root')
    GGZHNNTTFile = ROOT.TFile(dataPath+'GGZHNNTT.root')
    GGZHQQTTFile = ROOT.TFile(dataPath+'GGZHQQTT.root')
    GGZHWWFile = ROOT.TFile(dataPath+'GGZHWW.root')
    ST_tW_antitopFile = ROOT.TFile(dataPath+'ST_tW_antitop.root')
    ST_tW_topFile = ROOT.TFile(dataPath+'ST_tW_top.root')
    ST_t_antitopFile = ROOT.TFile(dataPath+'ST_t_antitop.root')
    ST_t_topFile = ROOT.TFile(dataPath+'ST_t_top.root')
    if args.year == '2016':
        TTFile = ROOT.TFile(dataPath+'TT.root')
    else:
        TTToHadronicFile = ROOT.TFile(dataPath+'TTToHadronic.root')
        TTToSemiLeptonicFile = ROOT.TFile(dataPath+'TTToSemiLeptonic.root')
        TTTo2L2NuFile = ROOT.TFile(dataPath+'TTTo2L2Nu.root')
    VBFFile = ROOT.TFile(dataPath+'VBF.root')
    VBFHWWFile = ROOT.TFile(dataPath+'VBFHWW.root')
    VV2L2NuFile = ROOT.TFile(dataPath+'VV2L2Nu.root')
    WHMinusFile = ROOT.TFile(dataPath+'WHMinus.root')
    WHPlusFile = ROOT.TFile(dataPath+'WHPlus.root')
    WW1L1Nu2QFile = ROOT.TFile(dataPath+'WW1L1Nu2Q.root')
    WZ1L1Nu2QFile = ROOT.TFile(dataPath+'WZ1L1Nu2Q.root')
    WZ1L3NuFile = ROOT.TFile(dataPath+'WZ1L3Nu.root')
    WZ2L2QFile = ROOT.TFile(dataPath+'WZ2L2Q.root')
    WZ3L1NuFile = ROOT.TFile(dataPath+'WZ3L1Nu.root')
    WminusHWWFile = ROOT.TFile(dataPath+'WminusHWW.root')
    WplusHWWFile = ROOT.TFile(dataPath+'WplusHWW.root')
    ZHFile = ROOT.TFile(dataPath+'ZH.root')
    ZHWWFile = ROOT.TFile(dataPath+'ZHWW.root')
    ZZ2L2QFile = ROOT.TFile(dataPath+'ZZ2L2Q.root')
    ZZ4LFile = ROOT.TFile(dataPath+'ZZ4L.root')
    ggHFile = ROOT.TFile(dataPath+'ggH.root')

    #okay, let's draw some histograms
    for variable in args.variables:
        try:
            variableSettingDictionary[variable] != None
        except KeyError:
            print("No defined histogram settings for variable: "+variable)
            continue
        try:
            variableAxisTitleDictionary[variable]
        except KeyError:
            print("No defined title information for variable: "+variable)
            continue

        if args.changeHistogramBounds != None:
            variableSettingDictionary[variable] = args.changeHistogramBounds
        ZLFile.mt_Selected.Draw(variable+'>>ZL('+variableSettingDictionary[variable]+')',
                                CreateCutString(args.standardCutString,
                                                args.additionalSelections+['gen_match_2 < 5']))
        dyHisto = ROOT.gDirectory.Get("ZL").Clone()
        dyHisto.Add(StandardDraw(EWKZLLFile,variable,args.standardCutString,args.additionalSelections,'ewkzll'))
        dyHisto.Add(StandardDraw(EWKZNuNuFile,variable,args.standardCutString,args.additionalSelections,'ewkznunu'))
        
        dataFile.mt_Selected.Draw(variable+'>>data('+variableSettingDictionary[variable]+')',
                                  CreateCutString(args.standardCutString,
                                                  args.additionalSelections,
                                                  weighting='1'))
        dataHisto = ROOT.gDirectory.Get('data').Clone()

        fakesFile.mt_Selected.Draw(variable+'>>fake('+variableSettingDictionary[variable]+')',
                                   CreateCutString(args.standardCutString,
                                                   args.additionalSelections,
                                                   weighting='FinalWeighting*Event_Fake_Factor'))
        fakeHisto = ROOT.gDirectory.Get("fake").Clone()

        embeddedHisto = StandardDraw(embeddedFile,variable,args.standardCutString,args.additionalSelections,'embedded')

        otherHisto = StandardDraw(GGHWWFile,variable,args.standardCutString,args.additionalSelections,'gghww')
        otherHisto.Add(StandardDraw(GGZHWWFile,variable,args.standardCutString,args.additionalSelections,'ggzhww'))
        otherHisto.Add(StandardDraw(ST_tW_antitopFile,variable,args.standardCutString,args.additionalSelections,'st_tw_antitop'))
        otherHisto.Add(StandardDraw(ST_tW_topFile,variable,args.standardCutString,args.additionalSelections,'st_tw_top'))
        otherHisto.Add(StandardDraw(ST_t_antitopFile,variable,args.standardCutString,args.additionalSelections,'st_t_antitop'))
        otherHisto.Add(StandardDraw(ST_t_topFile,variable,args.standardCutString,args.additionalSelections,'st_t_top'))
        otherHisto.Add(StandardDraw(VBFHWWFile,variable,args.standardCutString,args.additionalSelections,'vbfhww'))
        otherHisto.Add(StandardDraw(VV2L2NuFile,variable,args.standardCutString,args.additionalSelections,'vv2l2nu'))
        otherHisto.Add(StandardDraw(WW1L1Nu2QFile,variable,args.standardCutString,args.additionalSelections,'ww1l1nu2q'))
        otherHisto.Add(StandardDraw(WZ1L1Nu2QFile,variable,args.standardCutString,args.additionalSelections,'wz1l1nu2q'))
        otherHisto.Add(StandardDraw(WZ3L1NuFile,variable,args.standardCutString,args.additionalSelections,'wz3l1nu'))
        otherHisto.Add(StandardDraw(WZ2L2QFile,variable,args.standardCutString,args.additionalSelections,'wz2l2q'))
        otherHisto.Add(StandardDraw(WminusHWWFile,variable,args.standardCutString,args.additionalSelections,'wminushww'))
        otherHisto.Add(StandardDraw(WplusHWWFile,variable,args.standardCutString,args.additionalSelections,'wplushww'))
        otherHisto.Add(StandardDraw(ZHWWFile,variable,args.standardCutString,args.additionalSelections,'zhww'))
        otherHisto.Add(StandardDraw(ZZ2L2QFile,variable,args.standardCutString,args.additionalSelections,'zz2l2q'))
        otherHisto.Add(StandardDraw(ZZ4LFile,variable,args.standardCutString,args.additionalSelections,'zz4l'))

        if args.year == '2016':
            TTHisto = StandardDraw(TTFile,variable,args.standardCutString,args.additionalSelections,'tt')
        else:
            TTHisto = StandardDraw(TTToSemiLeptonicFile,variable,args.standardCutString,args.additionalSelections,'tttosemileptonic')            
            TTHisto.Add(StandardDraw(TTTo2L2NuFile,variable,args.standardCutString,args.additionalSelections,'ttto2l2nu'))
            TTHisto.Add(StandardDraw(TTToHadronicFile,variable,args.standardCutString,args.additionalSelections,'tttohadronic'))

        signalHisto = StandardDraw(GGZHLLTTFile,variable,args.standardCutString,args.additionalSelections,'ggzhlltt')
        signalHisto.Add(StandardDraw(GGZHNNTTFile,variable,args.standardCutString,args.additionalSelections,'ggzhnntt'))
        signalHisto.Add(StandardDraw(GGZHQQTTFile,variable,args.standardCutString,args.additionalSelections,'ggzhqqtt'))
        signalHisto.Add(StandardDraw(VBFFile,variable,args.standardCutString,args.additionalSelections,'vbf'))
        signalHisto.Add(StandardDraw(WHMinusFile,variable,args.standardCutString,args.additionalSelections,'wminush'))
        signalHisto.Add(StandardDraw(WHPlusFile,variable,args.standardCutString,args.additionalSelections,'wplush'))
        signalHisto.Add(StandardDraw(ZHFile,variable,args.standardCutString,args.additionalSelections,'zh'))
        signalHisto.Add(StandardDraw(ggHFile,variable,args.standardCutString,args.additionalSelections,'ggh'))        
        
        otherHisto.Add(signalHisto.Clone())

        dataHisto.SetMarkerStyle(20)
        dataHisto.Sumw2()
        
        fakeHisto.SetFillColor(ROOT.TColor.GetColor("#ffccff"))
        
        embeddedHisto.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))
        
        dyHisto.SetFillColor(ROOT.TColor.GetColor("#4496c8"))
        
        TTHisto.SetFillColor(ROOT.TColor.GetColor('#9999cc'))

        otherHisto.SetFillColor(ROOT.TColor.GetColor("#12cadd"))
        
        signalHisto.SetLineColor(ROOT.kRed)
        signalHisto.Scale(30)

        fakeHisto.SetLineWidth(0)
        TTHisto.SetLineWidth(0)
        dyHisto.SetLineWidth(0)
        otherHisto.SetLineWidth(0)
        embeddedHisto.SetLineWidth(0)

        dataHisto.SetLineColor(ROOT.kBlack)

        backgroundStack = ROOT.THStack('backgroundStack','backgroundstack')
        backgroundStack.Add(fakeHisto,'HIST')
        backgroundStack.Add(TTHisto,'HIST')
        backgroundStack.Add(dyHisto,'HIST')
        backgroundStack.Add(otherHisto,'HIST')
        backgroundStack.Add(embeddedHisto,'HIST')        
        
        backgroundStack_Errors = MakeStackErrors(backgroundStack)

        theCanvas = ROOT.TCanvas("theCanvas","theCanvas")
        theCanvas.Divide(1,2)
        
        plotPad = ROOT.gPad.GetPrimitive('theCanvas_1')
        ratioPad = ROOT.gPad.GetPrimitive('theCanvas_2')
        
        plotPad.SetPad("pad1","plot",0.0,0.20,1.0,1.0,0)
        ratioPad.SetPad("pad2","ratio",0.0,0.0,1.0,0.25,0)
        
        ratioPad.SetTopMargin(0.05)
        ratioPad.SetBottomMargin(0.27)
        plotPad.SetBottomMargin(0.08)
        ratioPad.SetGridy()

        ratioHist, ratioError = MakeRatioHistograms(dataHisto,backgroundStack,variable)
        ratioPad.cd()
        ratioHist.Draw('ex0')
        ratioError.Draw('SAME e2')
        ratioHist.Draw('SAME ex0')

        plotPad.cd()
        plotPad.SetTickx()
        plotPad.SetTicky()

        backgroundStack.SetMaximum(max(backgroundStack.GetMaximum(),dataHisto.GetMaximum()))
        
        backgroundStack.Draw()
        backgroundStack_Errors.Draw('SAME e2')
        backgroundStack.SetTitle(variableAxisTitleDictionary[variable])
        dataHisto.Draw('SAME e1')
        signalHisto.Draw('SAME HIST')
        backgroundStack.GetYaxis().SetTitle("Events")
        backgroundStack.GetYaxis().SetTitleOffset(1.58)
        backgroundStack.GetXaxis().SetLabelSize(0.0)

        theLegend = ROOT.TLegend(0.61,0.61,0.88,0.88)
        theLegend.AddEntry(dataHisto,'Observed','pe')
        theLegend.AddEntry(embeddedHisto,'Embedded','f')
        theLegend.AddEntry(otherHisto,'Other','f')
        theLegend.AddEntry(dyHisto,'DY #rightarrow ll','f')
        theLegend.AddEntry(TTHisto,'t#bar{t}','f')
        theLegend.AddEntry(fakeHisto,'Fakes','f')
        theLegend.AddEntry(signalHisto,'All Higgs (#times 30)','l')

        theLegend.Draw()

        #also draw the preliminary warnings
        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextFont(61)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92,"CMS")
        cmsLatex.SetTextFont(52)
        cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")
        
        cmsLatex.SetTextAlign(31)
        cmsLatex.SetTextFont(42)
        if args.year == '2016':
            lumiText = '35.9 fb^{-1}, 13TeV'
        elif args.year == '2017':
            lumiText = '41.5 fb^{-1}, 13TeV'
        elif args.year == '2018':
            lumiText = '59.7 fb^{-1}, 13TeV'
        cmsLatex.DrawLatex(0.9,0.92,lumiText)

        theCanvas.SaveAs('QuickControlPlots/'+variable+'_'+args.year+'.png')
        theCanvas.SaveAs('QuickControlPlots/'+variable+'_'+args.year+'.pdf')
        
        if args.pause:
            raw_input("Press Enter to Continue...")
        #this causes issues if you don't get rid of the canvas
        #I suspect it to be something to do with modifiying histograms that 
        # are alreayd referenced by the canvas in preparing the next one
        del theCanvas
    ZLFile.Close()
    dataFile.Close()
    EWKZLLFile.Close()
    EWKZNuNuFile.Close()
    embeddedFile.Close()
    fakesFile.Close()
    GGHWWFile.Close()
    GGZHLLTTFile.Close()
    GGZHNNTTFile.Close()
    GGZHQQTTFile.Close()
    GGZHWWFile.Close()
    ST_tW_antitopFile.Close()
    ST_tW_topFile.Close()
    ST_t_antitopFile.Close()
    ST_t_topFile.Close()
    if args.year == '2016':
        TTFile.Close()
    else:
        TTToHadronicFile.Close()
        TTToSemiLeptonicFile.Close()
        TTTo2L2NuFile.Close()
    VBFFile.Close()
    VBFHWWFile.Close()
    VV2L2NuFile.Close()
    WHMinusFile.Close()
    WHPlusFile.Close()
    WW1L1Nu2QFile.Close()
    WZ1L1Nu2QFile.Close()
    WZ1L3NuFile.Close()
    WZ2L2QFile.Close()
    WZ3L1NuFile.Close()
    WminusHWWFile.Close()
    WplusHWWFile.Close()
    ZHFile.Close()
    ZHWWFile.Close()
    ZZ2L2QFile.Close()
    ZZ4LFile.Close()
    ggHFile.Close()

if __name__ == '__main__':
    main()
