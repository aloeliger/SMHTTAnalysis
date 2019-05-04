import ROOT
import argparse
import configparser
from tqdm import tqdm
import AnalysisCategory
import SampleDefinition

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a combine file with the specified signal sample and analysis category")
    parser.add_argument('year',choices=['2016','2017','2018'],help="Specify the year to construct from")
    parser.add_argument('--AnalysisConfigFiles',nargs="+",help="Specify The analysis category configuration files",required=True)
    parser.add_argument('--SampleConfigFiles',nargs="+",help="Specify the sample configuration files",required=True)
    parser.add_argument('--RunShapeless',help='For speed, do not process any shape uncertainties (but still create the empty histograms)',action='store_true')
    
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
    #now we unroll all of our distributions
    for Sample in OutputSamples:
        OutputSamples[Sample].UnrollAllDistributions()

    #now we create a combine file, and write to it
    CombineFile = ROOT.TFile("CombineSpace_"+args.year+".root","RECREATE")
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
