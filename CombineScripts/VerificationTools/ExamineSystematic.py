import ROOT
import argparse
from tqdm import tqdm
import math
import re
import os

def ExamineSystematic(TheDirectory,NominalName,UncertaintyName,args,pause):
    ROOT.gStyle.SetOptStat(0)

    TheCanvas = ROOT.TCanvas("TheCanvas","TheCanvas")
    
    DistributionPad = ROOT.TPad("DistributionPad","DistributionPad",0.,0.2,1.,1.)
    RatioPad = ROOT.TPad("RatioPad","RatioPad",0.,0.,1.,0.25)

    DistributionPad.Draw()    
    RatioPad.Draw()

    Nominal = TheDirectory.Get(NominalName)
    UpUncert = TheDirectory.Get(UncertaintyName+"Up")
    DownUncert = TheDirectory.Get(UncertaintyName+"Down")    
    
    Nominal.SetLineColor(ROOT.kBlack)
    UpUncert.SetLineColor(ROOT.kRed)
    DownUncert.SetLineColor(ROOT.kBlue)
     
    Nominal.SetTitle(TheDirectory.GetName()+" "+UncertaintyName)
    Nominal.SetMaximum(max(Nominal.GetMaximum(),UpUncert.GetMaximum(),DownUncert.GetMaximum())*1.05)

    DistributionPad.cd()    
    Nominal.Draw("HIST E")    
    UpUncert.Draw("HIST E SAME")
    DownUncert.Draw("HIST E SAME")        

    TheLegend = ROOT.TLegend(0.7,0.6,0.98,0.9)
    TheLegend.AddEntry(Nominal,"Nominal","l")
    TheLegend.AddEntry(UpUncert,"Up","l")
    TheLegend.AddEntry(DownUncert,"Down","l")
    TheLegend.Draw()
    
    RatioPad.cd()
    RatioPad.SetTopMargin(0.0)
    RatioPad.SetBottomMargin(0.08)
    RatioPad.SetGridy()
    
    NominalWoErrors = Nominal.Clone()
    for i in range(1,NominalWoErrors.GetNbinsX()+1):
        NominalWoErrors.SetBinError(i,0.)

    UpRatio = UpUncert.Clone()
    #for i in range(1,UpRatio.GetNbinsX()+1):
    #    UpRatio.SetBinError(i,0.)
    #UpRatio.Divide(NominalWoErrors)
    UpRatio.Divide(Nominal)
    UpRatio.SetMarkerStyle(20)
    UpRatio.SetMarkerColor(ROOT.kRed)

    DownRatio = DownUncert.Clone()
    #for i in range(1,DownRatio.GetNbinsX()+1):
    #    DownRatio.SetBinError(i,0.)
    #DownRatio.Divide(NominalWoErrors)
    DownRatio.Divide(Nominal)
    DownRatio.SetMarkerStyle(20)
    DownRatio.SetMarkerColor(ROOT.kBlue)

    UpRatio.SetTitle("")
    UpRatio.GetYaxis().SetRangeUser(0.9,1.1)

    UpRatio.Draw("P E")
    UpRatio.GetYaxis().SetTitle("Uncertainty/Nominal")
    UpRatio.GetYaxis().SetTitleSize(0.1)
    UpRatio.GetYaxis().SetTitleOffset(0.32)
    UpRatio.GetYaxis().CenterTitle()
    UpRatio.GetYaxis().SetLabelSize(0.10)
    UpRatio.GetYaxis().SetNdivisions(5,0,0)    
    DownRatio.Draw("P E SAME")        

    #TheCanvas.SaveAs(os.environ.get('CMSSW_BASE')+"src/SMHTTAnalysis/CombineScripts/SystematicsScans/"+TheDirectory.GetName()+"/"+UncertaintyName+".png")
    TheCanvas.SaveAs(TheDirectory.GetName()+"_"+UncertaintyName+".png")

    if(pause):
        raw_input("Press Enter to Continue...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate comparison plots for the specified nominal plot and its specified uncertainty")
    #parser.add_argument('year',choices=['2016','2017','2018'],help="Specify the year of the files")
    parser.add_argument('CombineFile',help="Specify the file to draw the plots from")
    parser.add_argument('--Nominals',nargs='+',help="Specify the nominal distribution",required=True)
    parser.add_argument('--Pause',help="Pause after each histogram to ask to continue",action="store_true")
    UncertaintyGroup = parser.add_mutually_exclusive_group(required=True)
    UncertaintyGroup.add_argument('--Uncertainty',nargs='?',help="Specify the uncertainty to be drawn")
    UncertaintyGroup.add_argument('--Uncertainties',nargs='+',help='Specify the uncertainties to be drawn')
    UncertaintyGroup.add_argument('--AllUncerts',help="Draw all uncertainties for the given nominals",action="store_true")

    args = parser.parse_args()            
    
    TheFile = ROOT.TFile(args.CombineFile)
    for NominalName in args.Nominals:        
        for Directory in TheFile.GetListOfKeys():
            TheDirectory = TheFile.Get(Directory.GetName())
            Uncertainties = []
            if(args.Uncertainty != None):
                #print("Doing one Uncertainty: "+args.Uncertainty)
                Uncertainties.append(args.Uncertainty)
            elif(args.Uncertainties != None):
                for Uncertainty in args.Uncertainties:
                    Uncertainties.append(Uncertainty)
            elif(args.AllUncerts != None):
                #print("All Uncerts: "+str(args.AllUncerts))
                UncertExp = re.compile(NominalName+"_"+"(CMS|THU)_*")
                for Object in TheDirectory.GetListOfKeys():
                    if (UncertExp.match(Object.GetName())):
                        if Object.GetName()[len(Object.GetName())-2:]=="Up" and (Object.GetName()[:len(Object.GetName())-2] not in Uncertainties):
                            Uncertainties.append(Object.GetName()[:len(Object.GetName())-2])
                        if Object.GetName()[len(Object.GetName())-4:]=="Down" and (Object.GetName()[:len(Object.GetName())-4] not in Uncertainties):
                            Uncertainties.append(Object.GetName()[:len(Object.GetName())-4])
                #print("All Uncerts: "+str(Uncertainties))

            for UncertaintyName in Uncertainties:                                
                try:
                    ExamineSystematic(TheDirectory,NominalName,UncertaintyName,args,args.Pause)
                except Exception as Problem:
                    print("Failed NominalName/UncertaintyName: "+NominalName+"/"+UncertaintyName)
                    print("Reported issue:")
                    print(Problem)

