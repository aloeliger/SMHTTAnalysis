import ROOT
from array import array

def Unroll(histogram):
    nBinsX = histogram.GetNbinsX()
    nBinsY = histogram.GetNbinsY()
    nBins = nBinsX*nBinsY

    binArray = array('d',[i for i in range(nBins+1)])
    NewHisto = ROOT.TH1F(histogram.GetName().replace("_Rolled",""),
                         histogram.GetTitle().replace("_Rolled",""),
                         nBins,
                         binArray)
    for i in range(1,nBinsY+1):
        for j in range(1,nBinsX+1):
            NewHisto.SetBinContent(j+(i-1)*nBinsX,histogram.GetBinContent(j,i))
            NewHisto.SetBinError(j+(i-1)*nBinsX,histogram.GetBinError(j,i))
    return NewHisto
