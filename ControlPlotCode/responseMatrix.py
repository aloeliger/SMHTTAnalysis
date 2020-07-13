import ROOT
import argparse
from array import array

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat('1.3f')

parser = argparse.ArgumentParser(description="Generate differential response matrices for all run 2 higgs2taus")
parser.add_argument('--recoVar',nargs = '?',help='Select the reconstruction variable',default='HiggsPt')
parser.add_argument('--genVar',nargs='?',help='Select the gen variable',default='Rivet_higgsPt')
parser.add_argument('--binning',nargs='+',help='Select the binning',type=float,default=[0,45,80,120,200,350,450,10000])
parser.add_argument('--xAxisLabel',nargs='?',help='Select the x axis label',default='Reco Higgs Pt')

#okay, let's compile a complete signal list.
signalFiles = ['/data/aloeliger/SMHTT_Selected_2016_Deep/ggH.root',
               '/data/aloeliger/SMHTT_Selected_2017_Deep/ggH.root',
               '/data/aloeliger/SMHTT_Selected_2018_Deep/ggH.root',
               '/data/aloeliger/SMHTT_Selected_2016_Deep/VBF.root',
               '/data/aloeliger/SMHTT_Selected_2017_Deep/VBF.root',
               '/data/aloeliger/SMHTT_Selected_2018_Deep/VBF.root',
               '/data/aloeliger/SMHTT_Selected_2016_Deep/WHPlus.root',
               '/data/aloeliger/SMHTT_Selected_2016_Deep/WHMinus.root',
               '/data/aloeliger/SMHTT_Selected_2017_Deep/WHPlus.root',
               '/data/aloeliger/SMHTT_Selected_2017_Deep/WHMinus.root',
               '/data/aloeliger/SMHTT_Selected_2018_Deep/WHPlus.root',
               '/data/aloeliger/SMHTT_Selected_2018_Deep/WHMinus.root',
               '/data/aloeliger/SMHTT_Selected_2016_Deep/ZH.root',
               '/data/aloeliger/SMHTT_Selected_2017_Deep/ZH.root',
               '/data/aloeliger/SMHTT_Selected_2018_Deep/ZH.root']

theChain = ROOT.TChain('mt_Selected')
for signalFile in signalFiles:
    theChain.Add(signalFile)
#Okay... Let's start drawing I guess?
higgsPtList = [0,45,80,120,200,350,450,10000]

higgsPtBinning = array('f',higgsPtList)
overallNormHisto = ROOT.TH2F('overallNormHisto','overallNormHisto',
                         len(higgsPtList)-1,higgsPtBinning,
                         len(higgsPtList)-1,higgsPtBinning)
theCanvas = ROOT.TCanvas()
print theChain.Draw('Rivet_higgsPt:HiggsPt>>overallNormHisto','FinalWeighting**(pt_2>30&MT<50)','TEXT')

#no option exists in root to create even visible areas on the axes for bin drawing,
#... so we just have to make a new histogram and fill that in a predictable way.
higgsPtHisto = ROOT.TH2F('higgsPtHisto','higgsPtHisto',
                         len(higgsPtList)-1,0,len(higgsPtList)-1,
                         len(higgsPtList)-1,0,len(higgsPtList)-1)

for xBin in range(1,len(higgsPtList)):
    #let's also make sure to label our axes while we're here
    higgsPtHisto.GetXaxis().SetBinLabel(xBin,'['+str(higgsPtList[xBin-1])+','+str(higgsPtList[xBin])+']')
    #we can get away with this since the axes are reflectively symmetric
    higgsPtHisto.GetYaxis().SetBinLabel(xBin,'['+str(higgsPtList[xBin-1])+','+str(higgsPtList[xBin])+']')
    for yBin in range(1,len(higgsPtList)):
        #print "Bin ("+str(xBin)+","+str(yBin)+"): "+str(overallNormHisto.GetBinContent(xBin,yBin))
        higgsPtHisto.SetBinContent(xBin,yBin,overallNormHisto.GetBinContent(xBin,yBin))
        higgsPtHisto.SetBinError(xBin,yBin,overallNormHisto.GetBinError(xBin,yBin))
higgsPtHisto.SetTitle('Signal Response Matrix')
higgsPtHisto.GetXaxis().SetTitle('Reco Higgs Pt')
higgsPtHisto.GetYaxis().SetTitle('Rivet Higgs Pt')
higgsPtHisto.Draw("TEXT")

#let's make the overall norm one canvas
normOneCanvas = ROOT.TCanvas("normOneCanvas")
normOneCanvas.SetGrid()
normOneHisto = higgsPtHisto.Clone()
normOneHisto.SetNameTitle('normOneHisto',"Global Unity Normalization Response Matrix")
normOneHisto.Scale(1.0/normOneHisto.Integral())
normOneHisto.Draw("TEXT")

#okay, let's make the columnized normalization canvas
columnNormCanvas = ROOT.TCanvas("columnNormCanvas")
columnNormCanvas.SetGrid()
columnNormHisto = ROOT.TH2F('columNormHisto','Column Unity Normalization Response Matrix',
                            len(higgsPtList)-1,0,len(higgsPtList)-1,
                            len(higgsPtList)-1,0,len(higgsPtList)-1)
#ok let's pick a column, and get it's normalization
for xBin in range(1,len(higgsPtList)):
    columnNorm = 0
    columnNormHisto.GetXaxis().SetBinLabel(xBin,'['+str(higgsPtList[xBin-1])+','+str(higgsPtList[xBin])+']')
    columnNormHisto.GetYaxis().SetBinLabel(xBin,'['+str(higgsPtList[xBin-1])+','+str(higgsPtList[xBin])+']')
    for yBin in range(1,len(higgsPtList)):
        columnNorm+=higgsPtHisto.GetBinContent(xBin,yBin)
    #normalize it to unity
    columnNorm = 1.0/columnNorm
    #now let's go up the column in the new histogram filling it with the proper entries
    for yBin in range(1,len(higgsPtList)):
        columnNormHisto.SetBinContent(xBin,yBin,higgsPtHisto.GetBinContent(xBin,yBin)*columnNorm)
        columnNormHisto.SetBinError(xBin,yBin,higgsPtHisto.GetBinError(xBin,yBin)*columnNorm)
columnNormHisto.GetXaxis().SetTitle('Reco Higgs Pt')
columnNormHisto.GetYaxis().SetTitle('Rivet Higgs Pt')
columnNormHisto.Draw("TEXT")
    
#and we make the mirror image version of that with the row norm one canvas
rowNormCanvas = ROOT.TCanvas("rowNormCanvas")
rowNormCanvas.SetGrid()
rowNormHisto = ROOT.TH2F('rowNormHisto','Row Unity Normalization Response Matrix',
                         len(higgsPtList)-1,0,len(higgsPtList)-1,
                         len(higgsPtList)-1,0,len(higgsPtList)-1)
#now we do the same thing as before, but this time picking a row
for yBin in range(1,len(higgsPtList)):
    rowNorm = 0
    rowNormHisto.GetXaxis().SetBinLabel(yBin,'['+str(higgsPtList[yBin-1])+','+str(higgsPtList[yBin])+']')
    rowNormHisto.GetYaxis().SetBinLabel(yBin,'['+str(higgsPtList[yBin-1])+','+str(higgsPtList[yBin])+']')
    for xBin in range(1,len(higgsPtList)):
        rowNorm += higgsPtHisto.GetBinContent(xBin,yBin)
    #normalize it to unity
    rowNorm = 1.0/rowNorm
    #go up the rows filling in proper entries
    for xBin in range (1,len(higgsPtList)):
        rowNormHisto.SetBinContent(xBin,yBin,higgsPtHisto.GetBinContent(xBin,yBin)*rowNorm)
        rowNormHisto.SetBinError(xBin,yBin,higgsPtHisto.GetBinError(xBin,yBin)*rowNorm)
rowNormHisto.GetXaxis().SetTitle('Reco Higgs Pt')
rowNormHisto.GetYaxis().SetTitle('Rivet Higgs Pt')
rowNormHisto.Draw("TEXT")

normOneCanvas.SaveAs("globalResponseMatrix.png")
rowNormCanvas.SaveAs("rowResponseMatrix.png")
columnNormCanvas.SaveAs("columnResponseMatrix.png")

raw_input('Press Enter To Continue...')
