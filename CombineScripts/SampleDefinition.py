import ROOT
import configparser
from array import array
import math
import UnrollDistributions

class Sample():
    def __init__(self,Name,CatConfig,FileList):        
        self.Name = Name
        self.DefinitionList = []
        self.UncertaintyList = []
        self.FileList = FileList
        self.NominallyFake = False
        for Element in CatConfig:
            if Element == "Def":
                self.DefinitionList = CatConfig[Element]
                self.DefinitionList = self.DefinitionList.split('\n')        
            if Element == "Unc":
                self.UncertaintyList = CatConfig[Element]
                self.UncertaintyList = self.UncertaintyList.split('\n')                
            if Element == "NominallyFake":
                self.NominallyFake = True
        #master category dictionary.
        #this will be a dictionary of dictionaries.
        #first key will be categories.
        #This will return a dictionary of histograms
        #next key will be nominal histogram name
        self.MasterCategoryDictionary = {}
        #actual event chain that contains all the events we want present
        self.EventChain = ROOT.TChain("mt_Selected")
        for File in self.FileList:
            self.EventChain.Add(File)
        self.DefString = ''        
        for Definition in self.DefinitionList:
            self.DefString += '('+Definition+')&&'
        self.DefString = self.DefString.rstrip('&&')        
        self.EventChain = self.EventChain.CopyTree(self.DefString)
        
    #initializes one histogram and one set of uncertainty histograms for each
    #analysis category
    #input: list of analysis categories
    #output: none
    def InitializeHistograms(self,AnalysisCategories):
        for Cat in AnalysisCategories:
            self.MasterCategoryDictionary[Cat] = {}
            #create the nominal histogram            
            RollingBins = AnalysisCategories[Cat].RollingBins
            nRollingBins = AnalysisCategories[Cat].nRollingBins
            RecoBins = AnalysisCategories[Cat].ReconstructionBins
            nRecoBins = AnalysisCategories[Cat].nReconstructionBins
            RollingBinsArray = array('d',RollingBins)
            RecoBinsArray = array('d',RecoBins)
            self.MasterCategoryDictionary[Cat][self.Name] = ROOT.TH2F(self.Name+"_"+Cat,self.Name+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
            #okay, now we need to initialize all the shape uncertainties needed
            
            for Shape in self.UncertaintyList:
                if Shape == "FakeFactor":
                    self.InitializeFakeFactorShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "TES":
                    self.InitializeTESShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "JES":
                    self.InitializeJESShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "DYShape":
                    self.InitializeDYShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "ZLShape":
                    self.InitializeZLShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "ggHTheory":
                    self.InitializeggHTheoryShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "Recoil":
                    self.InitializeRecoilShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "TTbarContamination":
                    pass
                else:
                    raise RuntimeError("Undefined shape present: "+Shape)
    #the next few functions just break down and make a bunch of different shapes:
    #input: the category it is being created for, the binning arrays, and the number of bins
    #output: none
    def InitializeFakeFactorShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_mt_systUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_mt_systUp"+"_"+Cat,self.Name+"_CMS_ff_qcd_mt_systUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_mt_systDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_mt_systDown"+"_"+Cat,self.Name+"_CMS_ff_qcd_mt_systDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_njet0_mt_statUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_njet0_mt_statUp"+"_"+Cat,self.Name+"_CMS_ff_qcd_njet0_mt_statUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_njet0_mt_statDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_njet0_mt_statDown"+"_"+Cat,self.Name+"_CMS_ff_qcd_njet0_mt_statDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_njet1_mt_statUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_njet1_mt_statUp"+"_"+Cat,self.Name+"_CMS_ff_qcd_njet1_mt_statUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_qcd_njet1_mt_statDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_qcd_njet1_mt_statDown"+"_"+Cat,self.Name+"_CMS_ff_qcd_njet1_mt_statDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_tt_njet1_statUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_tt_njet1_statUp"+"_"+Cat,self.Name+"_CMS_ff_tt_njet1_statUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_tt_njet1_statDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_tt_njet1_statDown"+"_"+Cat,self.Name+"_CMS_ff_tt_njet1_statDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_tt_systUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_tt_systUp"+"_"+Cat,self.Name+"_CMS_ff_tt_systUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_tt_systDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_tt_systDown"+"_"+Cat,self.Name+"_CMS_ff_tt_systDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_njet0_mt_statUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_njet0_mt_statUp"+"_"+Cat,self.Name+"_CMS_ff_w_njet0_mt_statUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_njet0_mt_statDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_njet0_mt_statDown"+"_"+Cat,self.Name+"_CMS_ff_w_njet0_mt_statDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_njet1_mt_statUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_njet1_mt_statUp"+"_"+Cat,self.Name+"_CMS_ff_w_njet1_mt_statUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_njet1_mt_statDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_njet1_mt_statDown"+"_"+Cat,self.Name+"_CMS_ff_w_njet1_mt_statDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_systUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_systUp"+"_"+Cat,self.Name+"_CMS_ff_w_systUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ff_w_systDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ff_w_systDown"+"_"+Cat,self.Name+"_CMS_ff_w_systDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
    def InitializeTESShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        if self.Name == 'embedded':
            TESName = '_CMS_scale_emb_t'
        else:
            TESName = '_CMS_scale_t'
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_1prongUp'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_1prongUp'+"_"+Cat,self.Name+TESName+'_1prongUp'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_1prongDown'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_1prongDown'+"_"+Cat,self.Name+TESName+'_1prongDown'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_1prong1pizeroUp'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_1prong1pizeroUp'+"_"+Cat,self.Name+TESName+'_1prong1pizeroUp'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_1prong1pizeroDown'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_1prong1pizeroDown'+"_"+Cat,self.Name+TESName+'_1prong1pizeroDown'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_3prongUp'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_3prongUp'+"_"+Cat,self.Name+TESName+'_3prongUp'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+TESName+'_3prongDown'+"_"+Cat] = ROOT.TH2F(self.Name+TESName+'_3prongDown'+"_"+Cat,self.Name+TESName+'_3prongDown'+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
    def InitializeJESShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta0to3Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta0to3Up"+"_"+Cat,self.Name+"_CMS_JetEta0to3Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta0to3Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta0to3Down"+"_"+Cat,self.Name+"_CMS_JetEta0to3Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetRelativeBalUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetRelativeBalUp"+"_"+Cat,self.Name+"_CMS_JetRelativeBalUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetRelativeBalDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetRelativeBalDown"+"_"+Cat,self.Name+"_CMS_JetRelativeBalDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetRelativeSampleUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetRelativeSampleUp"+"_"+Cat,self.Name+"_CMS_JetRelativeSampleUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetRelativeSampleDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetRelativeSampleDown"+"_"+Cat,self.Name+"_CMS_JetRelativeSampleDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta3to5Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta3to5Up"+"_"+Cat,self.Name+"_CMS_JetEta3to5Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta3to5Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta3to5Down"+"_"+Cat,self.Name+"_CMS_JetEta3to5Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta0to5Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta0to5Up"+"_"+Cat,self.Name+"_CMS_JetEta0to5Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEta0to5Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEta0to5Down"+"_"+Cat,self.Name+"_CMS_JetEta0to5Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
    def InitializeDYShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_dyShapeUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_dyShapeUp"+"_"+Cat,self.Name+"_CMS_htt_dyShapeUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_dyShapeDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_dyShapeDown"+"_"+Cat,self.Name+"_CMS_htt_dyShapeDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
    def InitializeZLShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ZLShape_mt_1prongUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ZLShape_mt_1prongUp"+"_"+Cat,self.Name+"_CMS_ZLShape_mt_1prongUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ZLShape_mt_1prongDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ZLShape_mt_1prongDown"+"_"+Cat,self.Name+"_CMS_ZLShape_mt_1prongDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)  
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ZLShape_mt_1prong1pizeroUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ZLShape_mt_1prong1pizeroUp"+"_"+Cat,self.Name+"_CMS_ZLShape_mt_1prong1pizeroUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_ZLShape_mt_1prong1pizeroDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_ZLShape_mt_1prong1pizeroDown"+"_"+Cat,self.Name+"_CMS_ZLShape_mt_1prong1pizeroDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)  
    def InitializeggHTheoryShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_MuUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_MuUp"+"_"+Cat,self.Name+"_THU_ggH_MuUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_MuDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_MuDown"+"_"+Cat,self.Name+"_THU_ggH_MuDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_ResUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_ResUp"+"_"+Cat,self.Name+"_THU_ggH_ResUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_ResDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_ResDown"+"_"+Cat,self.Name+"_THU_ggH_ResDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_Mig01Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_Mig01Up"+"_"+Cat,self.Name+"_THU_ggH_Mig01Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_Mig01Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_Mig01Down+"+"_"+Cat,self.Name+"_THU_ggH_Mig01Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_Mig12Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_Mig12Up"+"_"+Cat,self.Name+"_THU_ggH_Mig12Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_Mig12Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_Mig12Down"+"_"+Cat,self.Name+"_THU_ggH_Mig12Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_VBF2jUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_VBF2jUp"+"_"+Cat,self.Name+"_THU_ggH_VBF2jUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_VBF2jDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_VBF2jDown"+"_"+Cat,self.Name+"_THU_ggH_VBF2jDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_VBF3jUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_VBF3jUp"+"_"+Cat,self.Name+"_THU_ggH_VBF3jUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_VBF3jDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_VBF3jDown"+"_"+Cat,self.Name+"_THU_ggH_VBF3jDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_PT60Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_PT60Up"+"_"+Cat,self.Name+"_THU_ggH_PT60Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_PT60Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_PT60Down"+"_"+Cat,self.Name+"_THU_ggH_PT60Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_PT120Up"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_PT120Up"+"_"+Cat,self.Name+"_THU_ggH_PT120Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_PT120Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_PT120Down"+"_"+Cat,self.Name+"_THU_ggH_PT120Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_qmtopUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_qmtopUp"+"_"+Cat,self.Name+"_THU_ggH_qmtopUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_qmtopDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_qmtopDown"+"_"+Cat,self.Name+"_THU_ggH_qmtopDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
    def InitializeRecoilShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_metUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_metUp"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_metUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_metDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_metDown"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_metDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_metUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_metUp"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_metUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_metDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_metDown"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_metDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        
    #oh geez, oh geez. How are we going to handle this?
    def InitializeTTbarContaminationErrors(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        pass

    #Okay, this will create the nominal event dump to a dictionary
    #from this dictionary, the analysis category can look 
    #input: loaded tree, arguments with year variable?
    #output: dictionary of variable names and values
    def GetEventDump(self,TheEvent,args):
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        JetOneVector = ROOT.TLorentzVector()
        JetTwoVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheEvent.pt_1,TheEvent.eta_1,TheEvent.phi_1,TheEvent.m_1)
        TauVector.SetPtEtaPhiM(TheEvent.pt_2,TheEvent.eta_2,TheEvent.phi_2,TheEvent.m_2)
        METVector.SetPtEtaPhiM(TheEvent.met,0.0,TheEvent.metphi,0.0)
        JetOneVector.SetPtEtaPhiM(TheEvent.jpt_1,TheEvent.jeta_1,TheEvent.jphi_1,0.0)
        JetTwoVector.SetPtEtaPhiM(TheEvent.jpt_2,TheEvent.jeta_2,TheEvent.jphi_2,0.0)

        MT = math.sqrt(2.0*MuVector.Pt()*METVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(METVector))))
        HiggsPt = (TauVector+MuVector+METVector).Pt()
        Higgs_jjPt = (TauVector+MuVector+METVector+JetOneVector+JetTwoVector).Pt()
        if args.year == "2017":
            njetsVariable = TheEvent.njetsWoNoisyJets
            mjjVariable = TheEvent.mjjWoNoisyJets
        elif args.year == "2018":
            njetsVariable = TheEvent.njets
            mjjVariable = TheEvent.mjj
        elif args.year == "2016":
            raise RuntimeError("2016 not implemented yet! Implement me!")
        
        TheEventDump = {}
        #lepton kinematics
        TheEventDump['MuPt'] = MuVector.Pt()
        TheEventDump['MuEta'] = MuVector.Eta()
        TheEventDump['MuPhi'] = MuVector.Phi()
        TheEventDump['MuM'] = MuVector.M()
        TheEventDump['TauPt'] = TauVector.Pt()
        TheEventDump['TauEta'] = TauVector.Eta()
        TheEventDump['TauPhi'] = TauVector.Phi()
        TheEventDump['TauM'] = TauVector.M()
        #category variables
        TheEventDump['MT'] = MT
        TheEventDump['njets'] = njetsVariable
        TheEventDump['mjj'] = mjjVariable
        #reco variables
        TheEventDump['m_vis'] = (TauVector+MuVector).M()
        TheEventDump['m_sv'] = TheEvent.m_sv
        #rolling variables
        TheEventDump['HiggsPt'] = HiggsPt        
        #STXS variables.
        TheEventDump['Higgs_jjPt'] = Higgs_jjPt
        #jet variables
        TheEventDump['LeadingJetPt'] = JetOneVector.Pt()
        
        #Create the weight
        if self.NominallyFake:
            TheEventDump['Weight'] = TheEvent.FinalWeighting*TheEvent.Event_Fake_Factor
        else:
            TheEventDump['Weight'] = TheEvent.FinalWeighting

        return TheEventDump
    
    #Classify the event into one of the available categories event
    #input: loaded event dump,list of categories to try and classify it into
    #output: list of categories that it meets the definition for?
    def ClassifyEvent(self,EventDump,AnalysisCategories):
        PossibleCategories = []
        for Cat in AnalysisCategories:
            if AnalysisCategories[Cat].CheckEventInCategory(EventDump):
                PossibleCategories.append(Cat)
        return PossibleCategories
    
    #take the current event, classify it, and fill the nominal histogram
    #input: AnalysisCategories arguments
    #output: none?
    def ProcessEvent(self,AnalysisCategories,args):
        EventDump = self.GetEventDump(self.EventChain,args)
        Categories = self.ClassifyEvent(EventDump,AnalysisCategories)

        #locate the histogram in the master dictionary,
        #then consult the appropriate category for rolling and reco variables
        #then use the event dump to get the approrpiate values
        for Category in Categories:            
            self.MasterCategoryDictionary[Category][self.Name].Fill(EventDump[AnalysisCategories[Category].ReconstructionVar],EventDump[AnalysisCategories[Category].RollingVar],EventDump['Weight'])
    
    #take the current event, loop over all the uncertainties,
    #process the uncertainties (get individual event dumps, modify as necessary
    #classify them, then find and fill the appropriate uncertainty histograms
    def ProcessAllUncertainties(self,AnalysisCategories,args):
        for Shape in self.UncertaintyList:
            if Shape == "FakeFactor":
                self.ProcessFakeFactorUncertainties(AnalysisCategories,args)                
            elif Shape == "TES":
                self.ProcessTESUncertainties(AnalysisCategories,args)
            elif Shape == "JES":
                self.ProcessJESUncertainties(AnalysisCategories,args)
            elif Shape == "DYShape":
                self.ProcessDYShapeUncertainties(AnalysisCategories,args)
            elif Shape == "ZLShape":
                self.ProcessZLShapeUncertainties(AnalysisCategories,args)
            elif Shape == "ggHTheory":
                self.ProcessggHTheoryUncertainties(AnalysisCategories,args)
            elif Shape == "Recoil":
                self.ProcessRecoilUncertainties(AnalysisCategories,args)
            elif Shape == "TTbarContamination":
                self.ProcessTTbarContaminationUncertainties(AnalysisCategories,args)
            else:
                raise RuntimeError("Undefined Shape attempted: "+Shape)
            
    def ProcessFakeFactorUncertainties(self,AnalysisCategories,args):
        #setup the nominal dump
        NominalDump = self.GetEventDump(self.EventChain,args)
        #setup the weights and names, and we'll loop over this to fill
        FFChangeDictionary = {'CMS_ff_qcd_mt_systUp':self.EventChain.ff_qcd_syst_up,
                              'CMS_ff_qcd_mt_systDown':self.EventChain.ff_qcd_syst_down,
                              'CMS_ff_qcd_njet0_mt_statUp':self.EventChain.ff_qcd_dm0_njet0_stat_up,
                              'CMS_ff_qcd_njet0_mt_statDown':self.EventChain.ff_qcd_dm0_njet0_stat_down,
                              'CMS_ff_qcd_njet1_mt_statUp':self.EventChain.ff_qcd_dm0_njet1_stat_up,
                              'CMS_ff_qcd_njet1_mt_statDown':self.EventChain.ff_qcd_dm0_njet1_stat_down,
                              'CMS_ff_tt_njet1_statUp':self.EventChain.ff_tt_dm0_njet1_stat_up,
                              'CMS_ff_tt_njet1_statDown':self.EventChain.ff_tt_dm0_njet1_stat_down,
                              'CMS_ff_tt_systUp':self.EventChain.ff_tt_syst_up,
                              'CMS_ff_tt_systDown':self.EventChain.ff_tt_syst_down,
                              'CMS_ff_w_njet0_mt_statUp':self.EventChain.ff_w_dm0_njet0_stat_up,
                              'CMS_ff_w_njet0_mt_statDown':self.EventChain.ff_w_dm0_njet0_stat_down,
                              'CMS_ff_w_njet1_mt_statUp':self.EventChain.ff_w_dm0_njet1_stat_up,
                              'CMS_ff_w_njet1_mt_statDown':self.EventChain.ff_w_dm0_njet1_stat_down,
                              'CMS_ff_w_systUp':self.EventChain.ff_w_syst_up,
                              'CMS_ff_w_systDown':self.EventChain.ff_w_syst_down}
        for Shape in FFChangeDictionary:
            NewDump = NominalDump
            NewDump['Weight'] = self.EventChain.FinalWeighting*FFChangeDictionary[Shape]
            NewCategories = self.ClassifyEvent(NewDump,AnalysisCategories)
            
            for Category in NewCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_"+Shape+"_"+Category].Fill(NewDump[AnalysisCategories[Category].ReconstructionVar],NewDump[AnalysisCategories[Category].RollingVar],NewDump['Weight'])
                
    def ProcessTESUncertainties(self,AnalysisCategories,args):
        if self.Name == 'embedded':
            TESName = 'CMS_scale_emb_t'
        else:
            TESName = 'CMS_scale_t'
        #create the nominal dump
        NominalDump = self.GetEventDump(self.EventChain,args)        

        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)
        
        JetOneVector = ROOT.TLorentzVector()
        JetTwoVector = ROOT.TLorentzVector()
        JetOneVector.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetTwoVector.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        
        CorrectedTauVector_UP = ROOT.TLorentzVector()
        CorrectedTauVector_DOWN = ROOT.TLorentzVector()
        CorrectedTauVector_UP.SetPtEtaPhiE(self.EventChain.TES_Pt_UP,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.TES_E_UP)
        CorrectedTauVector_DOWN.SetPtEtaPhiE(self.EventChain.TES_Pt_DOWN,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.TES_E_DOWN)

        CorrectedMetVector_UP = ROOT.TLorentzVector()
        CorrectedMetVector_DOWN = ROOT.TLorentzVector()
        CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.TES_MET_UP,0.0,self.EventChain.TES_METPhi_UP,0.0)
        CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.TES_MET_DOWN,0.0,self.EventChain.TES_METPhi_DOWN,0.0)

        CorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_UP))))
        CorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_DOWN))))        
        
        #create six dumps, one each for dms 0,1,10, and up and down
        # we classify each of them
        # and then use each to fill Corresponding histograms?        

        DM0_UP_Dump = NominalDump
        DM1_UP_Dump = NominalDump
        DM10_UP_Dump = NominalDump
        DM0_DOWN_Dump = NominalDump
        DM1_DOWN_Dump = NominalDump
        DM10_DOWN_Dump = NominalDump
        if self.EventChain.l2_decayMode == 0:
            DM0_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM0_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM0_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM0_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM0_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM0_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM0_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM0_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM0_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM0_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM0_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM0_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM0_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM0_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.l2_decayMode == 1:
            DM1_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM1_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM1_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM1_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM1_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM1_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM1_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM1_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM1_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM1_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM1_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM1_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM1_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM1_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.l2_decayMode == 10:
            DM10_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM10_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM10_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM10_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM10_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM10_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM10_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM10_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM10_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM10_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM10_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM10_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM10_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM10_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
        else:
            print("Warning! Non-Old DM found!")
        
        DM0_UP_Categories = self.ClassifyEvent(DM0_UP_Dump,AnalysisCategories)
        DM0_DOWN_Categories = self.ClassifyEvent(DM0_DOWN_Dump,AnalysisCategories)
        DM1_UP_Categories = self.ClassifyEvent(DM1_UP_Dump,AnalysisCategories)
        DM1_DOWN_Categories = self.ClassifyEvent(DM1_DOWN_Dump,AnalysisCategories)
        DM10_UP_Categories = self.ClassifyEvent(DM10_UP_Dump,AnalysisCategories)
        DM10_DOWN_Categories = self.ClassifyEvent(DM10_DOWN_Dump,AnalysisCategories)

        for Category in DM0_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_1prongUp_"+Category].Fill(DM0_UP_Dump[AnalysisCategories[Category].ReconstructionVar],DM0_UP_Dump[AnalysisCategories[Category].RollingVar],DM0_UP_Dump['Weight'])
        for Category in DM0_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_1prongDown_"+Category].Fill(DM0_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],DM0_DOWN_Dump[AnalysisCategories[Category].RollingVar],DM0_DOWN_Dump['Weight'])
        for Category in DM1_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_1prong1pizeroUp_"+Category].Fill(DM1_UP_Dump[AnalysisCategories[Category].ReconstructionVar],DM1_UP_Dump[AnalysisCategories[Category].RollingVar],DM1_UP_Dump['Weight'])
        for Category in DM1_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_1prong1pizeroDown_"+Category].Fill(DM1_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],DM1_DOWN_Dump[AnalysisCategories[Category].RollingVar],DM1_DOWN_Dump['Weight'])
        for Category in DM10_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_3prongUp_"+Category].Fill(DM10_UP_Dump[AnalysisCategories[Category].ReconstructionVar],DM10_UP_Dump[AnalysisCategories[Category].RollingVar],DM10_UP_Dump['Weight'])
        for Category in DM10_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_"+TESName+"_3prongDown_"+Category].Fill(DM10_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],DM10_DOWN_Dump[AnalysisCategories[Category].RollingVar],DM10_DOWN_Dump['Weight'])
    def ProcessJESUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)
        
        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiM(self.EventChain.pt_2,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.m_2)

        MetVector_JetEta0to3_UP = ROOT.TLorentzVector()
        MetVector_JetEta0to3_DOWN = ROOT.TLorentzVector()
        MetVector_JetRelativeBal_UP = ROOT.TLorentzVector()
        MetVector_JetRelativeBal_DOWN = ROOT.TLorentzVector()
        MetVector_JetRelativeSample_UP = ROOT.TLorentzVector()
        MetVector_JetRelativeSample_DOWN = ROOT.TLorentzVector()
        MetVector_JetEta3to5_UP = ROOT.TLorentzVector()
        MetVector_JetEta3to5_DOWN = ROOT.TLorentzVector()
        MetVector_JetEta0to5_UP = ROOT.TLorentzVector()
        MetVector_JetEta0to5_DOWN = ROOT.TLorentzVector()

        JetOneVector_JetEta0to3_UP = ROOT.TLorentzVector()
        JetOneVector_JetEta0to3_DOWN = ROOT.TLorentzVector()
        JetOneVector_JetRelativeBal_UP = ROOT.TLorentzVector()
        JetOneVector_JetRelativeBal_DOWN = ROOT.TLorentzVector()
        JetOneVector_JetRelativeSample_UP = ROOT.TLorentzVector()
        JetOneVector_JetRelativeSample_DOWN = ROOT.TLorentzVector()
        JetOneVector_JetEta3to5_UP = ROOT.TLorentzVector()
        JetOneVector_JetEta3to5_DOWN = ROOT.TLorentzVector()
        JetOneVector_JetEta0to5_UP = ROOT.TLorentzVector()
        JetOneVector_JetEta0to5_DOWN = ROOT.TLorentzVector()
        
        JetOneVector_JetEta0to3_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to3Up_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEta0to3_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to3Down_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetRelativeBal_UP.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeBalUp_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetRelativeBal_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeBalDown_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetRelativeSample_UP.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeSampleUp_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetRelativeSample_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeSampleDown_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEta3to5_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta3to5Up_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEta3to5_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta3to5Down_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEta0to5_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to5Up_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEta0to5_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to5Down_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)

        JetTwoVector_JetEta0to3_UP = ROOT.TLorentzVector()
        JetTwoVector_JetEta0to3_DOWN = ROOT.TLorentzVector()
        JetTwoVector_JetRelativeBal_UP = ROOT.TLorentzVector()
        JetTwoVector_JetRelativeBal_DOWN = ROOT.TLorentzVector()
        JetTwoVector_JetRelativeSample_UP = ROOT.TLorentzVector()
        JetTwoVector_JetRelativeSample_DOWN = ROOT.TLorentzVector()
        JetTwoVector_JetEta3to5_UP = ROOT.TLorentzVector()
        JetTwoVector_JetEta3to5_DOWN = ROOT.TLorentzVector()
        JetTwoVector_JetEta0to5_UP = ROOT.TLorentzVector()
        JetTwoVector_JetEta0to5_DOWN = ROOT.TLorentzVector()

        JetTwoVector_JetEta0to3_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to3Up_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEta0to3_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to3Down_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetRelativeBal_UP.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeBalUp_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetRelativeBal_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeBalDown_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetRelativeSample_UP.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeSampleUp_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetRelativeSample_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetRelativeSampleDown_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEta3to5_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta3to5Up_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEta3to5_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta3to5Down_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEta0to5_UP.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to5Up_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEta0to5_DOWN.SetPtEtaPhiM(self.EventChain.jpt_JetEta0to5Down_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)

        MT_JetEta0to3_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to3_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to3_UP))))
        MT_JetEta0to3_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to3_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to3_DOWN))))
        MT_JetRelativeBal_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeBal_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeBal_UP))))
        MT_JetRelativeBal_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeBal_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeBal_DOWN))))
        MT_JetRelativeSample_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeSample_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeSample_UP))))
        MT_JetRelativeSample_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetRelativeSample_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetRelativeSample_DOWN))))
        MT_JetEta3to5_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta3to5_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta3to5_UP))))
        MT_JetEta3to5_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta3to5_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta3to5_DOWN))))
        MT_JetEta0to5_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to5_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to5_UP))))
        MT_JetEta0to5_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEta0to5_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEta0to5_DOWN))))

        MTDictionary = {
            'JetEta0to3Up': MT_JetEta0to3_UP,
            'JetEta0to3Down': MT_JetEta0to3_DOWN,
            'JetRelativeBalUp': MT_JetRelativeBal_UP,
            'JetRelativeBalDown': MT_JetRelativeBal_DOWN,
            'JetRelativeSampleUp': MT_JetRelativeSample_UP,
            'JetRelativeSampleDown': MT_JetRelativeSample_DOWN,
            'JetEta3to5Up': MT_JetEta3to5_UP,
            'JetEta3to5Down': MT_JetEta3to5_DOWN,
            'JetEta0to5Up': MT_JetEta0to5_UP,
            'JetEta0to5Down': MT_JetEta0to5_DOWN,
            }

        HiggsPtDictionary = {
            'JetEta0to3Up': (TauVector+MuVector+MetVector_JetEta0to3_UP).Pt(),
            'JetEta0to3Down': (TauVector+MuVector+MetVector_JetEta0to3_DOWN).Pt(),
            'JetRelativeBalUp': (TauVector+MuVector+MetVector_JetRelativeBal_UP).Pt(),
            'JetRelativeBalDown': (TauVector+MuVector+MetVector_JetRelativeBal_DOWN).Pt(),
            'JetRelativeSampleUp': (TauVector+MuVector+MetVector_JetRelativeSample_UP).Pt(),
            'JetRelativeSampleDown': (TauVector+MuVector+MetVector_JetRelativeSample_DOWN).Pt(),
            'JetEta3to5Up': (TauVector+MuVector+MetVector_JetEta3to5_UP).Pt(),
            'JetEta3to5Down': (TauVector+MuVector+MetVector_JetEta3to5_DOWN).Pt(),
            'JetEta0to5Up': (TauVector+MuVector+MetVector_JetEta0to5_UP).Pt(),
            'JetEta0to5Down': (TauVector+MuVector+MetVector_JetEta3to5_DOWN).Pt(),
            }

        HiggsjjPtDictionary = {
            'JetEta0to3Up': (TauVector+MuVector+MetVector_JetEta0to3_UP+JetOneVector_JetEta0to3_UP+JetTwoVector_JetEta0to3_UP).Pt(),
            'JetEta0to3Down': (TauVector+MuVector+MetVector_JetEta0to3_DOWN+JetOneVector_JetEta0to3_DOWN+JetTwoVector_JetEta0to3_DOWN).Pt(),
            'JetRelativeBalUp': (TauVector+MuVector+MetVector_JetRelativeBal_UP+JetOneVector_JetRelativeBal_UP+JetTwoVector_JetRelativeBal_UP).Pt(),
            'JetRelativeBalDown': (TauVector+MuVector+MetVector_JetRelativeBal_DOWN+JetOneVector_JetRelativeBal_DOWN+JetTwoVector_JetRelativeBal_DOWN).Pt(),
            'JetRelativeSampleUp': (TauVector+MuVector+MetVector_JetRelativeSample_UP+JetOneVector_JetRelativeSample_UP+JetTwoVector_JetRelativeSample_UP).Pt(),
            'JetRelativeSampleDown': (TauVector+MuVector+MetVector_JetRelativeSample_DOWN+JetOneVector_JetRelativeSample_DOWN+JetTwoVector_JetRelativeSample_DOWN).Pt(),
            'JetEta3to5Up': (TauVector+MuVector+MetVector_JetEta3to5_UP+JetOneVector_JetEta3to5_UP+JetTwoVector_JetEta3to5_UP).Pt(),
            'JetEta3to5Down': (TauVector+MuVector+MetVector_JetEta3to5_DOWN+JetOneVector_JetEta3to5_DOWN+JetTwoVector_JetEta3to5_DOWN).Pt(),
            'JetEta0to5Up': (TauVector+MuVector+MetVector_JetEta0to5_UP+JetOneVector_JetEta0to5_UP+JetTwoVector_JetEta0to5_UP).Pt(),
            'JetEta0to5Down': (TauVector+MuVector+MetVector_JetEta0to5_DOWN+JetOneVector_JetEta0to5_DOWN+JetTwoVector_JetEta0to5_DOWN).Pt(),
            }
        LeadingJetPtDictionary = {
            'JetEta0to3Up': JetOneVector_JetEta0to3_UP.Pt(),
            'JetEta0to3Down': JetOneVector_JetEta0to3_DOWN.Pt(),
            'JetRelativeBalUp': JetOneVector_JetRelativeBal_UP.Pt(),
            'JetRelativeBalDown': JetOneVector_JetRelativeBal_DOWN.Pt(),
            'JetRelativeSampleUp': JetOneVector_JetRelativeSample_UP.Pt(),
            'JetRelativeSampleDown': JetOneVector_JetRelativeSample_DOWN.Pt(),
            'JetEta3to5Up': JetOneVector_JetEta3to5_UP.Pt(),
            'JetEta3to5Down': JetOneVector_JetEta3to5_DOWN.Pt(),
            'JetEta0to5Up': JetOneVector_JetEta0to5_UP.Pt(),
            'JetEta0to5Down': JetOneVector_JetEta0to5_DOWN.Pt()
            }

        if args.year == "2017":
            njetsDictionary = {
                'JetEta0to3Up': self.EventChain.njetsWoNoisyJets_JetEta0to3Up,
                'JetEta0to3Down': self.EventChain.njetsWoNoisyJets_JetEta0to3Down,
                'JetRelativeBalUp': self.EventChain.njetsWoNoisyJets_JetRelativeBalUp,
                'JetRelativeBalDown': self.EventChain.njetsWoNoisyJets_JetRelativeBalDown,
                'JetRelativeSampleUp': self.EventChain.njetsWoNoisyJets_JetRelativeSampleUp,
                'JetRelativeSampleDown': self.EventChain.njetsWoNoisyJets_JetRelativeSampleDown,
                'JetEta3to5Up': self.EventChain.njetsWoNoisyJets_JetEta3to5Down,
                'JetEta3to5Down': self.EventChain.njetsWoNoisyJets_JetEta3to5Down,
                'JetEta0to5Up': self.EventChain.njetsWoNoisyJets_JetEta0to5Up,
                'JetEta0to5Down': self.EventChain.njetsWoNoisyJets_JetEta0to5Down,
                }
            mjjDictionary  = {
                'JetEta0to3Up': self.EventChain.mjjWoNoisyJets_JetEta0to3Up,
                'JetEta0to3Down': self.EventChain.mjjWoNoisyJets_JetEta0to3Down,
                'JetRelativeBalUp': self.EventChain.mjjWoNoisyJets_JetRelativeBalUp,
                'JetRelativeBalDown': self.EventChain.mjjWoNoisyJets_JetRelativeBalDown,
                'JetRelativeSampleUp': self.EventChain.mjjWoNoisyJets_JetRelativeSampleUp,
                'JetRelativeSampleDown': self.EventChain.mjjWoNoisyJets_JetRelativeSampleDown,
                'JetEta3to5Up': self.EventChain.mjjWoNoisyJets_JetEta3to5Down,
                'JetEta3to5Down': self.EventChain.mjjWoNoisyJets_JetEta3to5Down,
                'JetEta0to5Up': self.EventChain.mjjWoNoisyJets_JetEta0to5Up,
                'JetEta0to5Down': self.EventChain.mjjWoNoisyJets_JetEta0to5Down,
                }
        elif args.year == "2018":
            njetsDictionary = {
                'JetEta0to3Up': self.EventChain.njets_JetEta0to3Up,
                'JetEta0to3Down': self.EventChain.njets_JetEta0to3Down,
                'JetRelativeBalUp': self.EventChain.njets_JetRelativeBalUp,
                'JetRelativeBalDown': self.EventChain.njets_JetRelativeBalDown,
                'JetRelativeSampleUp': self.EventChain.njets_JetRelativeSampleUp,
                'JetRelativeSampleDown': self.EventChain.njets_JetRelativeSampleDown,
                'JetEta3to5Up': self.EventChain.njets_JetEta3to5Down,
                'JetEta3to5Down': self.EventChain.njets_JetEta3to5Down,
                'JetEta0to5Up': self.EventChain.njets_JetEta0to5Up,
                'JetEta0to5Down': self.EventChain.njets_JetEta0to5Down,
                }
            mjjDictionary  = {
                'JetEta0to3Up': self.EventChain.mjj_JetEta0to3Up,
                'JetEta0to3Down': self.EventChain.mjj_JetEta0to3Down,
                'JetRelativeBalUp': self.EventChain.mjj_JetRelativeBalUp,
                'JetRelativeBalDown': self.EventChain.mjj_JetRelativeBalDown,
                'JetRelativeSampleUp': self.EventChain.mjj_JetRelativeSampleUp,
                'JetRelativeSampleDown': self.EventChain.mjj_JetRelativeSampleDown,
                'JetEta3to5Up': self.EventChain.mjj_JetEta3to5Down,
                'JetEta3to5Down': self.EventChain.mjj_JetEta3to5Down,
                'JetEta0to5Up': self.EventChain.mjj_JetEta0to5Up,
                'JetEta0to5Down': self.EventChain.mjj_JetEta0to5Down,
                }
        elif args.year == "2016":
            raise RuntimeError("2016 not implemented yet! Implement me")
        
        for Shape in MTDictionary:
            JESDump = NominalDump
            JESDump['MT'] = MTDictionary[Shape]
            JESDump['njets'] = njetsDictionary[Shape]
            JESDump['mjj'] = mjjDictionary[Shape]
            JESDump['HiggsPt'] = HiggsPtDictionary[Shape]
            JESDump['Higgs_jjPt'] = HiggsjjPtDictionary[Shape]
            JESDump['LeadingJetPt'] = LeadingJetPtDictionary[Shape]

            JESCategories = self.ClassifyEvent(JESDump,AnalysisCategories)

            for Category in JESCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_"+Shape+"_"+Category].Fill(JESDump[AnalysisCategories[Category].ReconstructionVar],JESDump[AnalysisCategories[Category].RollingVar],JESDump['Weight'])
    def ProcessDYShapeUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        ZPT_Up_Dump = NominalDump
        ZPT_Up_Dump['Weight'] = self.EventChain.FinalWeighting_ZPT_UP
        ZPT_Down_Dump = NominalDump
        ZPT_Down_Dump['Weight'] = self.EventChain.FinalWeighting_ZPT_DOWN

        UP_Categories = self.ClassifyEvent(ZPT_Up_Dump,AnalysisCategories)
        DOWN_Categories = self.ClassifyEvent(ZPT_Down_Dump,AnalysisCategories)
        for Category in UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_dyShapeUp_"+Category].Fill(ZPT_Up_Dump[AnalysisCategories[Category].ReconstructionVar],ZPT_Up_Dump[AnalysisCategories[Category].RollingVar],ZPT_Up_Dump['Weight'])
        for Category in DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_dyShapeUp_"+Category].Fill(ZPT_Down_Dump[AnalysisCategories[Category].ReconstructionVar],ZPT_Down_Dump[AnalysisCategories[Category].RollingVar],ZPT_Down_Dump['Weight'])

    def ProcessZLShapeUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)

        JetOneVector = ROOT.TLorentzVector()
        JetTwoVector = ROOT.TLorentzVector()
        JetOneVector.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetTwoVector.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        
        if(self.EventChain.gen_match_2 == 1 or self.EventChain.gen_match_2 == 3):
            CorrectedTauVector_UP = ROOT.TLorentzVector()
            CorrectedTauVector_DOWN = ROOT.TLorentzVector()
            CorrectedTauVector_UP.SetPtEtaPhiE(self.EventChain.EES_Pt_UP,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.EES_E_UP)
            CorrectedTauVector_DOWN.SetPtEtaPhiE(self.EventChain.EES_Pt_DOWN,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.EES_E_DOWN)

            CorrectedMetVector_UP = ROOT.TLorentzVector()
            CorrectedMetVector_DOWN = ROOT.TLorentzVector()
            CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.EES_MET_UP,0.0,self.EventChain.EES_METPhi_UP,0.0)
            CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.EES_MET_DOWN,0.0,self.EventChain.EES_METPhi_DOWN,0.0)

            CorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_UP))))
            CorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_DOWN))))
        
        elif(self.EventChain.gen_match_2 == 2 or self.EventChain.gen_match_2 == 4):
            CorrectedTauVector_UP = ROOT.TLorentzVector()
            CorrectedTauVector_DOWN = ROOT.TLorentzVector()
            CorrectedTauVector_UP.SetPtEtaPhiE(self.EventChain.MES_Pt_UP,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.MES_E_UP)
            CorrectedTauVector_DOWN.SetPtEtaPhiE(self.EventChain.MES_Pt_DOWN,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.MES_E_DOWN)

            CorrectedMetVector_UP = ROOT.TLorentzVector()
            CorrectedMetVector_DOWN = ROOT.TLorentzVector()
            CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.MES_MET_UP,0.0,self.EventChain.MES_METPhi_UP,0.0)
            CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.MES_MET_DOWN,0.0,self.EventChain.MES_METPhi_DOWN,0.0)

            CorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_UP))))
            CorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_DOWN))))
            
        else:
            CorrectedTauVector_UP = ROOT.TLorentzVector()
            CorrectedTauVector_DOWN = ROOT.TLorentzVector()
            CorrectedTauVector_UP.SetPtEtaPhiE(self.EventChain.pt_2,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.e_2)
            CorrectedTauVector_DOWN.SetPtEtaPhiE(self.EventChain.pt_2,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.e_2)

            CorrectedMetVector_UP = ROOT.TLorentzVector()
            CorrectedMetVector_DOWN = ROOT.TLorentzVector()
            CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.met,0.0,self.EventChain.metphi,0.0)
            CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.met,0.0,self.EventChain.metphi,0.0)

            CorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_UP))))
            CorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_DOWN))))

        #set up the dumps
        ZLDumpUp = NominalDump
        ZLDumpDown = NominalDump

        ZLDumpUp['TauPt'] = CorrectedTauVector_UP.Pt()
        ZLDumpUp['TauEta'] = CorrectedTauVector_UP.Eta()
        ZLDumpUp['TauPhi'] = CorrectedTauVector_UP.Phi()
        ZLDumpUp['TauM'] = CorrectedTauVector_UP.M()
        ZLDumpUp['MT'] = CorrectedMT_UP
        ZLDumpUp['m_vis'] = (CorrectedTauVector_UP+MuVector).M()
        ZLDumpUp['HiggsPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP).Pt()
        ZLDumpUp['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()

        ZLDumpDown['TauPt'] = CorrectedTauVector_DOWN.Pt()
        ZLDumpDown['TauEta'] = CorrectedTauVector_DOWN.Eta()
        ZLDumpDown['TauPhi'] = CorrectedTauVector_DOWN.Phi()
        ZLDumpDown['TauM'] = CorrectedTauVector_DOWN.M()
        ZLDumpDown['MT'] = CorrectedMT_DOWN
        ZLDumpDown['m_vis'] = (CorrectedTauVector_DOWN+MuVector).M()
        ZLDumpDown['HiggsPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN).M()
        ZLDumpUp['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()

        ZLCategoriesUp = self.ClassifyEvent(ZLDumpUp,AnalysisCategories)
        ZLCategoriesDown = self.ClassifyEvent(ZLDumpDown,AnalysisCategories)
        NominalCategories = self.ClassifyEvent(NominalDump,AnalysisCategories)

        # if tau decay mode 0, check for categories (corrected), otherwise, check for categories (nominal), and fill the DM 0 accordingly
        # similarly, if tau decay mode 1, check for categories (corrected), otherwise, check for categories(nominal) and fill the DM 1 accordingly
        if self.EventChain.l2_decayMode == 0:
            for Category in ZLCategoriesUp:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prongUp_"+Category].Fill(ZLDumpUp[AnalysisCategories[Category].ReconstructionVar],ZLDumpUp[AnalysisCategories[Category].RollingVar],ZLDumpUp['Weight'])
            for Category in ZLCategoriesDown:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prongDown_"+Category].Fill(ZLDumpDown[AnalysisCategories[Category].ReconstructionVar],ZLDumpDown[AnalysisCategories[Category].RollingVar],ZLDumpDown['Weight'])
        else:
            for Category in NominalCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prongUp_"+Category].Fill(NominalDump[AnalysisCategories[Category].ReconstructionVar],NominalDump[AnalysisCategories[Category].RollingVar],NominalDump['Weight'])
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prongDown_"+Category].Fill(NominalDump[AnalysisCategories[Category].ReconstructionVar],NominalDump[AnalysisCategories[Category].RollingVar],NominalDump['Weight'])
        
        if self.EventChain.l2_decayMode == 1:
            for Category in ZLCategoriesUp:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prong1pizeroUp_"+Category].Fill(ZLDumpUp[AnalysisCategories[Category].ReconstructionVar],ZLDumpUp[AnalysisCategories[Category].RollingVar],ZLDumpUp['Weight'])
            for Category in ZLCategoriesDown:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prong1pizeroDown_"+Category].Fill(ZLDumpDown[AnalysisCategories[Category].ReconstructionVar],ZLDumpDown[AnalysisCategories[Category].RollingVar],ZLDumpDown['Weight'])
        else:
            for Category in NominalCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prong1pizeroUp_"+Category].Fill(NominalDump[AnalysisCategories[Category].ReconstructionVar],NominalDump[AnalysisCategories[Category].RollingVar],NominalDump['Weight'])
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_ZLShape_mt_1prong1pizeroDown_"+Category].Fill(NominalDump[AnalysisCategories[Category].ReconstructionVar],NominalDump[AnalysisCategories[Category].RollingVar],NominalDump['Weight'])
        
    def ProcessggHTheoryUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        ggHDictionary = {
            'THU_ggH_MuUp':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_Mu_13TeV),
            'THU_ggH_MuDown':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_Mu_13TeV),
            'THU_ggH_ResUp':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_Res_13TeV),
            'THU_ggH_ResDown':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_Res_13TeV),
            'THU_ggH_Mig01Up':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_Mig01_13TeV),
            'THU_ggH_Mig01Down':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_Mig01_13TeV),
            'THU_ggH_Mig12Up':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_Mig12_13TeV),
            'THU_ggH_Mig12Down':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_Mig12_13TeV),
            'THU_ggH_VBF2jUp':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_VBF2j_13TeV),
            'THU_ggH_VBF2jDown':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_VBF2j_13TeV),
            'THU_ggH_VBF3jUp':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_VBF3j_13TeV),
            'THU_ggH_VBF3jDown':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_VBF3j_13TeV),
            'THU_ggH_PT60Up':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_PT60_13TeV),
            'THU_ggH_PT60Down':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_PT60_13TeV),
            'THU_ggH_PT120Up':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_PT120_13TeV),
            'THU_ggH_PT120Down':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_PT120_13TeV),
            'THU_ggH_qmtopUp':self.EventChain.FinalWeighting*(1.0+self.EventChain.THU_ggH_qmtop_13TeV),
            'THU_ggH_qmtopDown':self.EventChain.FinalWeighting*(1.0-self.EventChain.THU_ggH_qmtop_13TeV)
            }
        for Shape in ggHDictionary:
            ggHDump = NominalDump
            ggHDump['Weight'] = ggHDictionary[Shape]
            
            ggHCategories = self.ClassifyEvent(ggHDump,AnalysisCategories)
            for Category in ggHCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_"+Shape+"_"+Category].Fill(ggHDump[AnalysisCategories[Category].ReconstructionVar],ggHDump[AnalysisCategories[Category].RollingVar],ggHDump['Weight'])
        
    def ProcessRecoilUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        
        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        JetOneVector = ROOT.TLorentzVector()
        JetTwoVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)
        TauVector.SetPtEtaPhiM(self.EventChain.pt_2,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.m_2)
        METVector.SetPtEtaPhiM(self.EventChain.met,0.0,self.EventChain.metphi,0.0)
        JetOneVector.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetTwoVector.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)

        ResolutionCorrectedMetVector_UP = ROOT.TLorentzVector()
        ResolutionCorrectedMetVector_DOWN = ROOT.TLorentzVector()
        ResponseCorrectedMetVector_UP = ROOT.TLorentzVector()
        ResponseCorrectedMetVector_DOWN = ROOT.TLorentzVector()
        
        ResolutionCorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.met_resolutionUp,0.0,self.EventChain.metphi_resolutionUp,0.0)
        ResolutionCorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.met_resolutionDown,0.0,self.EventChain.metphi_resolutionDown,0.0)
        ResponseCorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.met_responseUp,0.0,self.EventChain.metphi_responseUp,0.0)
        ResponseCorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.met_responseDown,0.0,self.EventChain.metphi_responseDown,0.0)

        ResolutionCorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*ResolutionCorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(ResolutionCorrectedMetVector_UP))))
        ResolutionCorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*ResolutionCorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(ResolutionCorrectedMetVector_DOWN))))
        ResponseCorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*ResponseCorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(ResponseCorrectedMetVector_UP))))
        ResponseCorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*ResponseCorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(ResponseCorrectedMetVector_DOWN))))

        ResolutionCorrectedHiggsPt_UP = (TauVector+MuVector+ResolutionCorrectedMetVector_UP).Pt()
        ResolutionCorrectedHiggsPt_DOWN = (TauVector+MuVector+ResolutionCorrectedMetVector_DOWN).Pt()
        ResponseCorrectedHiggsPt_UP = (TauVector+MuVector+ResponseCorrectedMetVector_UP).Pt()
        ResponseCorrectedHiggsPt_DOWN = (TauVector+MuVector+ResponseCorrectedMetVector_DOWN).Pt()
        
        ResolutionCorrectedHiggsjjPt_UP = (TauVector+MuVector+ResolutionCorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
        ResolutionCorrectedHiggsjjPt_DOWN = (TauVector+MuVector+ResolutionCorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        ResponseCorrectedHiggsjjPt_UP = (TauVector+MuVector+ResponseCorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
        ResponseCorrectedHiggsjjPt_DOWN = (TauVector+MuVector+ResponseCorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()

        ResolutionUpDump = NominalDump
        ResolutionDownDump = NominalDump
        ResponseUpDump = NominalDump
        ResponseDownDump = NominalDump
        
        ResolutionUpDump['MT'] = ResolutionCorrectedMT_UP
        ResolutionUpDump['HiggsPt'] = ResolutionCorrectedHiggsPt_UP
        ResolutionUpDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_UP
        ResolutionDownDump['MT'] = ResolutionCorrectedMT_DOWN
        ResolutionDownDump['HiggsPt'] = ResolutionCorrectedHiggsPt_DOWN
        ResolutionDownDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_DOWN
        ResponseUpDump['MT'] = ResponseCorrectedMT_UP
        ResponseUpDump['HiggsPt'] = ResponseCorrectedHiggsPt_UP
        ResponseUpDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_UP
        ResponseDownDump['MT'] = ResponseCorrectedMT_DOWN
        ResponseDownDump['HiggsPt'] = ResponseCorrectedHiggsPt_DOWN
        ResponseDownDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_DOWN

        ResolutionUpCategories = self.ClassifyEvent(ResolutionUpDump,AnalysisCategories)
        ResolutionDownCategories = self.ClassifyEvent(ResolutionDownDump,AnalysisCategories)
        ResponseUpCategories = self.ClassifyEvent(ResponseUpDump,AnalysisCategories)
        ResponseDownCategories = self.ClassifyEvent(ResponseDownDump,AnalysisCategories)

        for Category in ResolutionUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_metUp_"+Category].Fill(ResolutionUpDump[AnalysisCategories[Category].ReconstructionVar],ResolutionUpDump[AnalysisCategories[Category].RollingVar],ResolutionUpDump['Weight'])
        for Category in ResolutionDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_metDown_"+Category].Fill(ResolutionDownDump[AnalysisCategories[Category].ReconstructionVar],ResolutionDownDump[AnalysisCategories[Category].RollingVar],ResolutionDownDump['Weight'])
        for Category in ResponseUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_metUp_"+Category].Fill(ResponseUpDump[AnalysisCategories[Category].ReconstructionVar],ResponseUpDump[AnalysisCategories[Category].RollingVar],ResponseUpDump['Weight'])
        for Category in ResponseDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_metDown_"+Category].Fill(ResponseDownDump[AnalysisCategories[Category].ReconstructionVar],ResponseDownDump[AnalysisCategories[Category].RollingVar],ResponseDownDump['Weight'])

    def ProcessTTbarContaminationUncertainties(self,AnalysisCategories,args):
        raise RuntimeError('TTBar contamination uncertainties not implemented yet! Implement me!')

    #go trhough the master dictionary,
    # and replace all histogram entries with their unrolled counterparts
    def UnrollAllDistributions(self):
        for Cat in self.MasterCategoryDictionary:
            for HistoName in self.MasterCategoryDictionary[Cat]:
                self.MasterCategoryDictionary[Cat][HistoName] = UnrollDistributions.Unroll(self.MasterCategoryDictionary[Cat][HistoName])
