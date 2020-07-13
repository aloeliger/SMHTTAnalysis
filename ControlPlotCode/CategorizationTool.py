import ROOT
from tqdm import tqdm
import argparse
import math

parser = argparse.ArgumentParser(description="Generate percentage based categorization plot.")
parser.add_argument('--yAxisVar',nargs='?',help='variable to put on the y-axis')
parser.add_argument('--nYAxisBins',nargs='?',help='# of bins to use on the y-axis',type=int,default=20)
parser.add_argument('--yAxisLowBound',nargs='?',type=float)
parser.add_argument('--yAxisUpperBound',nargs='?',type=float)

parser.add_argument('--xAxisVar',nargs='?',help='variable to put on the x-axis',required=True)
parser.add_argument('--nXAxisBins',nargs='?',help='# of bins to use on the x-axis',type=int,default=20)
parser.add_argument('--xAxisLowBound',nargs='?',type=float,required=True)
parser.add_argument('--xAxisUpperBound',nargs='?',type=float,required=True)

parser.add_argument('--signalBinDefinition',nargs='?',help='Define the bin in signal to use')
parser.add_argument('--signalStrength',help='Test an estimated S/S+B instead',action='store_true')
parser.add_argument('--additionalDefinition',nargs='?',help='any additional definitions for all ntuples')
parser.add_argument('--additionalSignalDefinitions',nargs='+',help='Additional signal distributions to be drawn on the ')

args=parser.parse_args()

if args.yAxisVar != None and (args.yAxisLowBound == None or args.yAxisUpperBound == None):
    raise RuntimeError("Tried to make a 2D plot without specifying bounds for the y var")

#let's find the ggH ntuples we need.
fileName2016 = '/data/aloeliger/SMHTT_Selected_2016_Deep/ggH.root'
fileName2017 = '/data/aloeliger/SMHTT_Selected_2017_Deep/ggH.root'
fileName2018 = '/data/aloeliger/SMHTT_Selected_2018_Deep/ggH.root'

#large background ntuples
if args.signalStrength:
    embeddedFileName2016 = '/data/aloeliger/SMHTT_Selected_2016_Deep/Embedded.root'
    embeddedFileName2017 = '/data/aloeliger/SMHTT_Selected_2017_Deep/Embedded.root'
    embeddedFileName2018 = '/data/aloeliger/SMHTT_Selected_2018_Deep/Embedded.root'
    fakeFileName2016 = '/data/aloeliger/SMHTT_Selected_2016_Deep/Fake.root'
    fakeFileName2017 = '/data/aloeliger/SMHTT_Selected_2017_Deep/Fake.root'
    fakeFileName2018 = '/data/aloeliger/SMHTT_Selected_2018_Deep/Fake.root'
    ZLFileName2016 = '/data/aloeliger/SMHTT_Selected_2016_Deep/DY.root'
    ZLFileName2017 = '/data/aloeliger/SMHTT_Selected_2017_Deep/DY.root'
    ZLFileName2018 = '/data/aloeliger/SMHTT_Selected_2018_Deep/DY.root'

print 'Creating the chain...'
theChain = ROOT.TChain('mt_Selected')
theChain.Add(fileName2016)
theChain.Add(fileName2017)
theChain.Add(fileName2018)
print theChain.GetEntries()

if args.signalStrength:
    print 'Preparing background chains for s/s+b estimate...'
    print 'Embedded...'
    embeddedChain = ROOT.TChain('mt_Selected')
    embeddedChain.Add(embeddedFileName2016)
    embeddedChain.Add(embeddedFileName2017)
    embeddedChain.Add(embeddedFileName2018)
    print embeddedChain.GetEntries()
    print 'Fake...'
    fakeChain = ROOT.TChain('mt_Selected')
    fakeChain.Add(fakeFileName2016)
    fakeChain.Add(fakeFileName2017)
    fakeChain.Add(fakeFileName2018)
    print fakeChain.GetEntries()
    print 'ZL...'
    ZLChain=ROOT.TChain('mt_Selected')
    ZLChain.Add(ZLFileName2016)
    ZLChain.Add(ZLFileName2017)
    ZLChain.Add(ZLFileName2018)
    print ZLChain.GetEntries()
    ZLChain=ZLChain.CopyTree('gen_match_2 < 5 && !(numGenJets == 0 && njets >1)')

#if args.additionalDefinition != None:
#    print 'Applying additional defintions...'
#    theChain = theChain.CopyTree(args.additionalDefinition)
#    if args.signalStrength:
#        embeddedChain = embeddedChain.CopyTree(args.additionalDefinition)
#        fakeChain = fakeChain.CopyTree(args.additionalDefinition)
#        ZLChain = fakeChain.CopyTree(args.additionalDefinition)
#okay, theoretically, we now have an ntuple with all the proper bin conditions
#now it should be a matter as simple as just drawing from the tree, and 
#retrieving whatever histogram we made, and tuning it up.
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat('0.2f')
ROOT.gStyle.SetPalette(ROOT.kLightTemperature)
#ROOT.TColor.InvertPalette()
variableDeclaration = ''
histogramName = '>>h'
histogramSetup = ''
if args.yAxisVar != None:
    variableDeclaration+=args.yAxisVar+':'
variableDeclaration+=args.xAxisVar
histogramSetup+='('+str(args.nXAxisBins)+','+str(args.xAxisLowBound)+','+str(args.xAxisUpperBound)
if args.yAxisVar != None:
    histogramSetup+=','+str(args.nYAxisBins)+','+str(args.yAxisLowBound)+','+str(args.yAxisUpperBound)
histogramSetup+=')'
print variableDeclaration+histogramName+histogramSetup

if args.yAxisVar != None:
    drawOptions = 'TEXT COLZ'
else:
    drawOptions = 'HIST'

weightSelection = 'FinalWeighting*(pt_2>30&&MT<50'
if args.additionalDefinition != None:
    weightSelection+='&&'+args.additionalDefinition
signalWeightSelection = weightSelection
if args.signalBinDefinition != None:
    signalWeightSelection+='&&'+args.signalBinDefinition

additionalWeightSelections = []
if args.additionalSignalDefinitions != None:
    for additionalDefinition in args.additionalSignalDefinitions:
        additionalWeightSelections.append(weightSelection+'&&'+additionalDefinition+')')
        
signalWeightSelection+=')'
weightSelection+=')'

fakeWeightSelection = 'FinalWeighting*Event_Fake_Factor*(pt_2>30&&MT<50'
if args.additionalDefinition != None:
    fakeWeightSelection+='&&'+args.additionalDefinition
fakeWeightSelection+=')'

#let's figure out to retrieve our histogrammy-do
if args.signalStrength:
    theChain.Draw(variableDeclaration+'>>h'+histogramSetup,signalWeightSelection,'')
    signalHisto = ROOT.gDirectory.Get('h').Clone()
    sPlusBHisto = ROOT.gDirectory.Get('h').Clone()
    embeddedChain.Draw(variableDeclaration+'>>embedded'+histogramSetup,weightSelection,'')
    sPlusBHisto.Add(ROOT.gDirectory.Get('embedded').Clone())
    fakeChain.Draw(variableDeclaration+'>>fake'+histogramSetup,fakeWeightSelection,'')
    sPlusBHisto.Add(ROOT.gDirectory.Get('fake').Clone())
    ZLChain.Draw(variableDeclaration+'>>ZL'+histogramSetup,weightSelection,'')
    sPlusBHisto.Add(ROOT.gDirectory.Get('ZL').Clone())
    signalHisto.Divide(sPlusBHisto)
    signalHisto.Draw(drawOptions)

    signalHisto.SetTitle("ggH S/S+B Estimate")
    signalHisto.GetXaxis().SetTitle(args.xAxisVar)
    if args.yAxisVar != None:
        signalHisto.GetYaxis().SetTitle(args.yAxisVar)
    else:
        signalHisto.GetYaxis().SetTitle("S/S+B")
    
else:
    theChain.Draw(variableDeclaration+'>>h'+histogramSetup,signalWeightSelection,'')
    #ROOT.gPad.ls()
    theHisto = ROOT.gDirectory.Get('h').Clone()
    additionalHistos = []
    if args.additionalSignalDefinitions != None:
        for i in range(len(args.additionalSignalDefinitions)):
            theChain.Draw(variableDeclaration+'>>h'+str(i)+histogramSetup,additionalWeightSelections[i],'')
            additionalHistos.append(ROOT.gDirectory.Get('h'+str(i)).Clone())
            additionalHistos[i].SetLineColor(i+2)
    theHisto.SetLineColor(1)
    theHisto.Scale(1.0/theHisto.Integral())
    theHisto.Draw(drawOptions)
    theHisto.GetXaxis().SetTitle(args.xAxisVar)
    theHisto.SetTitle("ggH Signal Fraction Estimate")
    if args.yAxisVar != None:
        theHisto.GetYaxis().SetTitle(args.yAxisVar)
    else:
        theHisto.GetYaxis().SetTitle("Fraction")
    if args.additionalSignalDefinitions != None:
        for i in range(len(args.additionalSignalDefinitions)):
            additionalHistos[i].Scale(1.0/additionalHistos[i].Integral())
            additionalHistos[i].Draw('HIST SAME')
        theLegend = ROOT.TLegend(0.8,0.5,1.0,0.9)
        if args.signalBinDefinition != 'None':
            theLegend.AddEntry(theHisto,args.signalBinDefinition,'l')
        else:
            theLegend.AddEntry(theHist,'ggH','l')
        for i in range(len(args.additionalSignalDefinitions)):
            theLegend.AddEntry(additionalHistos[i],args.additionalSignalDefinitions[i],'l')
        theLegend.Draw()
ROOT.gPad.SaveAs("Test.png")
