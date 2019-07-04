import ROOT
import argparse
import configparser
from tqdm import tqdm
import AnalysisCategory
import SampleDefinition
import sys

def CalculateAverageWeights(OutputSamples):
    AverageWeights={}
    for Sample in OutputSamples:        
        CategoryWeights={}
        for Cat in OutputSamples[Sample].MasterCategoryDictionary:                        
            if OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetEntries() > 0.0:
                TheWeight = OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].Integral()/OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetEntries()
                CategoryWeights[Cat]=TheWeight
            else: 
                print("No Entries! Defaulting Zero!")
                print(Sample)
                print(Cat)
                CategoryWeights[Cat]=0.0
        AverageWeights[Sample] = CategoryWeights
    return AverageWeights

def PerformFinalSteps(OutputSamples,AnalysisCategories,AverageWeights):    
    #create the ttbar contamination stuff
    try:
        TTbarContaminationSample = OutputSamples['TT_Contamination']
        try:
            embeddedSample = OutputSamples['embedded']
        except KeyError:
            print("Couldn't find embedded samples to make ttbar contamination shapes with!")
        for Category in embeddedSample.MasterCategoryDictionary:
            Emb_tt_UP = MasterCategoryDictionary[Category]['embedded'].Clone()
            Emb_tt_UP.SetNameTitle('embedded_CMS_htt_emb_ttbarUp_'+Category,'embedded_CMS_htt_emb_ttbarUp_'+Category)
            Emb_tt_DOWN = MasterCategoryDictionary[Category]['embedded'].Clone()
            Emb_tt_DoWN.SetNameTitle('embedded_CMS_htt_emb_ttbarDown_'+Category,'embedded_CMS_htt_emb_ttbarDown_'+Category)
            #get the actual TTContamination histogram
            TTContamination = TTbarContaminationSample.MasterCategoryDictionary[Category]['TT_Contamination_CMS_htt_emb_ttbar_'+Category]
            Emb_tt_UP.Add(TTContamination)
            Emb_tt_DOWN.Add(TTContamination,-1.0)
            OutputSamples['embedded'].MasterCategoryDictionary[Category]['embedded_Contamination_CMS_htt_emb_ttbarUp_'+Category] = Emb_tt_UP
            OutputSamples['embedded'].MasterCategoryDictionary[Category]['embedded_Contamination_CMS_htt_emb_ttbarDown_'+Category] = Emb_tt_DOWN
    except KeyError:
        print("Not Making ttbar contamination shapes.")
    except:
        print("Unexpected error while making ttbar contamination shapes!")
        print(sys.exc_info()[0])
        raise
    #rectify empty bins/negative bins
    for Sample in OutputSamples:
        #Nominal should now be OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].    
        for Cat in OutputSamples[Sample].MasterCategoryDictionary:            
            TheWeight=AverageWeights[Sample][Cat]            
            for i in range(1,OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetNbinsX()+1):
                if Sample == "data_obs":
                    continue
                if OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i) <= 0.0:
                    #First we need to check if we are in the overflow bin
                    #in which case we need only check the bin to our left
                    if i % AnalysisCategories[Cat].nReconstructionBins == 0:
                        if OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i-1) > 0:
                            #print("Bin #"+str(i)+" (Overflow bin)")
                            # now we just add the bin error
                            OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].SetBinError(i,1.8*TheWeight)
                            #print("Adding Error: "+str(1.8*TheWeight))
                            #check if we are in the first bin on 
                    elif (i-1 ) % AnalysisCategories[Cat].nReconstructionBins == 0:                        
                        if OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i+1) > 0:
                            #print("Bin #"+str(i)+" (First bin)")
                            OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].SetBinError(i,1.8*TheWeight)
                            #print("Adding Error: "+str(1.8*TheWeight))
                    else:
                        if (OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i-1) > 0) or (OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i+1) > 0):
                            #print("Bin #"+str(i))
                            OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].SetBinError(i,1.8*TheWeight)
                            #print("Adding Error: "+str(1.8*TheWeight))
                else:
                    continue                    
            #do the same thing, but now we adjust the MC up a bit everywhere it is zero            
            for i in range(1,OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetNbinsX()+1):
                if Sample == "data_obs":
                    continue
                elif OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].GetBinContent(i) <= 0.0:                    
                    OutputSamples[Sample].MasterCategoryDictionary[Cat][Sample].SetBinContent(i,1e-8)
                else:
                    continue                        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a combine file with the specified signal sample and analysis category")
    parser.add_argument('year',choices=['2016','2017','2018'],help="Specify the year to construct from")
    parser.add_argument('--AnalysisConfigFiles',nargs="+",help="Specify The analysis category configuration files",required=True)
    parser.add_argument('--SampleConfigFiles',nargs="+",help="Specify the sample configuration files",required=True)
    parser.add_argument('--RunShapeless',help='For speed, do not process any shape uncertainties (will still create the empty histograms)',action='store_true')
    parser.add_argument('--OutputFileName',nargs="?",help="Name the output file. Output file name will include the year at the end",default="CombineSpace")
    
    args = parser.parse_args()

    AnalysisCategories = {}
    print("Setting up analysis categories...")
    for File in args.AnalysisConfigFiles:
        NewCategory = AnalysisCategory.AnalysisCategory(File)
        print("\t"+NewCategory.Name+" complete...")
        AnalysisCategories[NewCategory.Name] = NewCategory

    #parsing the files for the sample categories is a little different
    OutputSamples = {}
    print("Prepping output samples...")
    for File in args.SampleConfigFiles:
        SampleFileParser = configparser.ConfigParser()
        SampleFileParser.optionxform = str
        SampleFileParser.read(File)
        for Token in SampleFileParser:            
            if Token == "META":
                for Element in SampleFileParser[Token]:                    
                    if Element == "Files":
                        FileList = SampleFileParser[Token][Element]
                        FileList = FileList.split()
            elif Token == "DEFAULT":
                continue
            else:
                print("\t"+Token+"...")                
                NewOutputSample = SampleDefinition.Sample(Token,SampleFileParser[Token],FileList)
                OutputSamples[NewOutputSample.Name] = NewOutputSample
    # initialize all the histograms we are going to need.
    print("Prepping all histograms...")
    for Sample in OutputSamples:
        print("\t"+Sample)
        OutputSamples[Sample].InitializeHistograms(AnalysisCategories)
    
    #okay now we simply start looping over samples and events
    print("Creating Histograms...")
    for Sample in OutputSamples:
        print("For "+Sample+"...")
        for i in tqdm(range(OutputSamples[Sample].EventChain.GetEntries())):
            OutputSamples[Sample].EventChain.GetEntry(i)
            #do the nominal things
            OutputSamples[Sample].ProcessEvent(AnalysisCategories,args)
            if not args.RunShapeless:
                OutputSamples[Sample].ProcessAllUncertainties(AnalysisCategories,args)    

    #Create the average weights
    AverageWeightDict = CalculateAverageWeights(OutputSamples)
    
    #now we unroll all of our distributions
    for Sample in OutputSamples:
        OutputSamples[Sample].UnrollAllDistributions()
    
    #perform any final miscellaneous operations we may need    
    PerformFinalSteps(OutputSamples,AnalysisCategories,AverageWeightDict)    

    #now we create a combine file, and write to it
    CombineFile = ROOT.TFile(str(args.OutputFileName)+"_"+str(args.year)+".root","RECREATE")
    for Cat in AnalysisCategories:
        CombineFile.mkdir(Cat)
    
    for Sample in OutputSamples:
        for Cat in OutputSamples[Sample].MasterCategoryDictionary:
            CombineFile.cd(Cat)
            for HistogramName in OutputSamples[Sample].MasterCategoryDictionary[Cat]:
                OutputSamples[Sample].MasterCategoryDictionary[Cat][HistogramName].SetNameTitle(OutputSamples[Sample].MasterCategoryDictionary[Cat][HistogramName].GetName()[:-1*len('_'+Cat)],
                                                                                                OutputSamples[Sample].MasterCategoryDictionary[Cat][HistogramName].GetTitle()[:-1*len('_'+Cat)])
                print("Writing "+Cat+"/"+OutputSamples[Sample].MasterCategoryDictionary[Cat][HistogramName].GetName())
                OutputSamples[Sample].MasterCategoryDictionary[Cat][HistogramName].Write()
    CombineFile.Write()
    CombineFile.Close()
