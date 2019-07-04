import ROOT
import configparser
from array import array
import math
import UnrollDistributions

def CalculatePZeta(MuVector,TauVector,METVector):
    leg1x = math.cos(MuVector.Phi())
    leg1y = math.sin(MuVector.Phi())
    leg2x = math.cos(TauVector.Phi())
    leg2y = math.sin(TauVector.Phi())
    zetaX = leg1x+leg2x
    zetaY = leg1y+leg2y
    zetaR = math.sqrt(zetaX*zetaX+zetaY*zetaY)
    if(zetaR > 0.0):
        zetaX = zetaX/zetaR
        zetaY = zetaY/zetaR
    visPx = MuVector.Px()
    visPy = MuVector.Py()
    PZetaVis = visPx*zetaX+visPy*zetaY
        
    px = visPx+METVector.Px()
    py = visPy+METVector.Py()
    PZetaAll = px*zetaX+py*zetaY
    return PZetaAll-1.85*PZetaVis
    

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
                elif Shape == "UES":
                    self.InitializeUESShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "TTbarContamination":
                    self.InitializeTTbarContaminationShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "TTbarShape":
                    self.InitializeTTbarShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "muonES":
                    self.InitializeMuonESShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
                elif Shape == "JtoT":
                    self.InitializeJtoTShapes(Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins)
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
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEC2Up_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEC2Up_"+Cat,self.Name+"_CMS_JetEC2Up_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JetEC2Down_"+Cat] = ROOT.TH2F(self.Name+"_CMS_JetEC2Down_"+Cat,self.Name+"_CMS_JetEC2Down_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
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
        self.MasterCategoryDictionary[Cat][self.Name+"_THU_ggH_Mig01Down"+"_"+Cat] = ROOT.TH2F(self.Name+"_THU_ggH_Mig01Down"+"_"+Cat,self.Name+"_THU_ggH_Mig01Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
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
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_0jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_0jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_0jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_0jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_0jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_0jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_0jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_0jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_0jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_0jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_0jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_0jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_1jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_1jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_1jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_1jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_1jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_1jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_1jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_1jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_1jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_1jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_1jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_1jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_2jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_2jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_2jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_reso_met_2jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_reso_met_2jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_reso_met_2jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_2jetUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_2jetUp"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_2jetUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_boson_scale_met_2jetDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_boson_scale_met_2jetDown"+"_"+Cat,self.Name+"_CMS_htt_boson_scale_met_2jetDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        
    def InitializeUESShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):        
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_met_unclusteredUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_scale_met_unclusteredUp"+"_"+Cat,self.Name+"_CMS_scale_met_unclusteredUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_met_unclusteredDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_scale_met_unclusteredDown"+"_"+Cat,self.Name+"_CMS_scale_met_unclusteredDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        
    #oh geez, oh geez. How are we going to handle this?
    def InitializeTTbarContaminationShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_emb_ttbar"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_emb_ttbar"+"_"+Cat,self.Name+"_CMS_htt_emb_ttbar"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        

    def InitializeTTbarShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_ttbarShapeUp"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_ttbarShapeUp"+"_"+Cat,self.Name+"_CMS_htt_ttbarShapeUp"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_htt_ttbarShapeDown"+"_"+Cat] = ROOT.TH2F(self.Name+"_CMS_htt_ttbarShapeDown"+"_"+Cat,self.Name+"_CMS_htt_ttbarShapeDown"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)        

    def InitializeMuonESShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam2p4tom2p1Up"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam2p4tom2p1Up"+"_"+Cat,self.Name+"_CMS_scale_m_etam2p4tom2p1Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam2p4tom2p1Down"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam2p4tom2p1Down"+"_"+Cat,self.Name+"_CMS_scale_m_etam2p4tom2p1Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam2p1tom1p2Up"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam2p1tom1p2Up"+"_"+Cat,self.Name+"_CMS_scale_m_etam2p1tom1p2Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam2p1tom1p2Down"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam2p1tom1p2Down"+"_"+Cat,self.Name+"_CMS_scale_m_etam2p1tom1p2Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam1p2to1p2Up"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam1p2to1p2Up"+"_"+Cat,self.Name+"_CMS_scale_m_etam1p2to1p2Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_etam1p2to1p2Down"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_etam1p2to1p2Down"+"_"+Cat,self.Name+"_CMS_scale_m_etam1p2to1p2Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_eta1p2to2p1Up"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_eta1p2to2p1Up"+"_"+Cat,self.Name+"_CMS_scale_m_eta1p2to2p1Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_eta1p2to2p1Down"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_eta1p2to2p1Down"+"_"+Cat,self.Name+"_CMS_scale_m_eta1p2to2p1Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_eta2p1to2p4Up"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_eta2p1to2p4Up"+"_"+Cat,self.Name+"_CMS_scale_m_eta2p1to2p4Up"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_scale_m_eta2p1to2p4Down"+"_"+Cat]=ROOT.TH2F(self.Name+"_CMS_scale_m_eta2p1to2p4Down"+"_"+Cat,self.Name+"_CMS_scale_m_eta2p1to2p4Down"+"_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)

    def InitializeJtoTShapes(self,Cat,RollingBinsArray,nRollingBins,RecoBinsArray,nRecoBins):
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JtoTUp_"+Cat]=ROOT.TH2F(self.Name+"_CMS_JtoTUp_"+Cat,self.Name+"_CMS_JtoTUp_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)
        self.MasterCategoryDictionary[Cat][self.Name+"_CMS_JtoTDown_"+Cat]=ROOT.TH2F(self.Name+"_CMS_JtoTDown_"+Cat,self.Name+"_CMS_JtoTDown_"+Cat,nRecoBins,RecoBinsArray,nRollingBins,RollingBinsArray)

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
        TheEventDump['njets'] = TheEvent.njets
        TheEventDump['mjj'] = TheEvent.mjj
        #reco variables
        TheEventDump['m_vis'] = (TauVector+MuVector).M()
        TheEventDump['m_sv'] = TheEvent.m_sv
        #rolling variables
        TheEventDump['HiggsPt'] = HiggsPt        
        #STXS variables.
        TheEventDump['Higgs_jjPt'] = Higgs_jjPt
        #jet variables
        TheEventDump['LeadingJetPt'] = JetOneVector.Pt()
        TheEventDump['PZeta']=CalculatePZeta(MuVector,TauVector,METVector)
        
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
            elif Shape == "UES":
                self.ProcessMETUESUncertainties(AnalysisCategories,args)
            elif Shape == "TTbarShape":
                self.ProcessTTbarShapeUncertainties(AnalysisCategories,args)
            elif Shape == "muonES":
                self.ProcessMuonESUncertainties(AnalysisCategories,args)
            elif Shape == "JtoT":
                self.ProcessJtoTUncertainties(AnalysisCategories,args)
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
            NewDump = NominalDump.copy()
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

        #we're missing m_sv varriations on this, 
        #is this m_sv_UP and DOWN? Assume it is,
        #and then ask cecile.

        DM0_UP_Dump = NominalDump.copy()
        DM1_UP_Dump = NominalDump.copy()
        DM10_UP_Dump = NominalDump.copy()
        DM0_DOWN_Dump = NominalDump.copy()
        DM1_DOWN_Dump = NominalDump.copy()
        DM10_DOWN_Dump = NominalDump.copy()
        if self.EventChain.l2_decayMode == 0:            
            DM0_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM0_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM0_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM0_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM0_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM0_UP_Dump['m_sv'] = self.EventChain.m_sv_UP
            DM0_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM0_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM0_UP_Dump['MT'] = CorrectedMT_UP
            DM0_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM0_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM0_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM0_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM0_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM0_DOWN_Dump['m_sv'] = self.EventChain.m_sv_DOWN
            DM0_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM0_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
            DM0_DOWN_Dump['MT']=CorrectedMT_DOWN
        elif self.EventChain.l2_decayMode == 1:
            DM1_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM1_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM1_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM1_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM1_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM1_UP_Dump['m_sv'] = self.EventChain.m_sv_UP
            DM1_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM1_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM1_UP_Dump['MT'] = CorrectedMT_UP
            DM1_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM1_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM1_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM1_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM1_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM1_DOWN_Dump['m_sv'] = self.EventChain.m_sv_DOWN
            DM1_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM1_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
            DM1_DOWN_Dump['MT'] = CorrectedMT_DOWN
        elif self.EventChain.l2_decayMode == 10:
            DM10_UP_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
            DM10_UP_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
            DM10_UP_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
            DM10_UP_Dump['TauM'] = CorrectedTauVector_UP.M()
            DM10_UP_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
            DM10_UP_Dump['m_sv'] = self.EventChain.m_sv_UP
            DM10_UP_Dump['HiggsPt'] = (CorrectedTauVector_UP + CorrectedMetVector_UP + MuVector).Pt()
            DM10_UP_Dump['Higgs_jjPt'] = (CorrectedTauVector_UP+MuVector+CorrectedMetVector_UP + JetOneVector+JetTwoVector).Pt()
            DM10_UP_Dump['MT'] = CorrectedMT_UP
            DM10_DOWN_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
            DM10_DOWN_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
            DM10_DOWN_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
            DM10_DOWN_Dump['TauM'] = CorrectedTauVector_DOWN.M()
            DM10_DOWN_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
            DM10_DOWN_Dump['m_sv'] = self.EventChain.m_sv_DOWN
            DM10_DOWN_Dump['HiggsPt'] = (CorrectedTauVector_DOWN + CorrectedMetVector_DOWN + MuVector).Pt()
            DM10_DOWN_Dump['Higgs_jjPt'] = (CorrectedTauVector_DOWN+MuVector+CorrectedMetVector_DOWN + JetOneVector+JetTwoVector).Pt()
            DM10_DOWN_Dump['MT'] = CorrectedMT_DOWN
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
        MetVector_JetEC2_UP = ROOT.TLorentzVector()
        MetVector_JetEC2_DOWN = ROOT.TLorentzVector()

        MetVector_JetEta0to3_UP.SetPtEtaPhiM(self.EventChain.met_JetEta0to3Up,0.0,self.EventChain.metphi_JetEta0to3Up,0.0)
        MetVector_JetEta0to3_DOWN.SetPtEtaPhiM(self.EventChain.met_JetEta0to3Down,0.0,self.EventChain.metphi_JetEta0to3Down,0.0)
        MetVector_JetRelativeBal_UP.SetPtEtaPhiM(self.EventChain.met_JetRelativeBalUp,0.0,self.EventChain.metphi_JetRelativeBalUp,0.0)
        MetVector_JetRelativeBal_DOWN.SetPtEtaPhiM(self.EventChain.met_JetRelativeBalDown,0.0,self.EventChain.metphi_JetRelativeBalDown,0.0)
        MetVector_JetRelativeSample_UP.SetPtEtaPhiM(self.EventChain.met_JetRelativeSampleUp,0.0,self.EventChain.metphi_JetRelativeSampleUp,0.0)
        MetVector_JetRelativeSample_DOWN.SetPtEtaPhiM(self.EventChain.met_JetRelativeSampleDown,0.0,self.EventChain.metphi_JetRelativeSampleDown,0.0)
        MetVector_JetEta3to5_UP.SetPtEtaPhiM(self.EventChain.met_JetEta3to5Up,0.0,self.EventChain.metphi_JetEta3to5Up,0.0)
        MetVector_JetEta3to5_DOWN.SetPtEtaPhiM(self.EventChain.met_JetEta3to5Down,0.0,self.EventChain.metphi_JetEta3to5Down,0.0)
        MetVector_JetEta0to5_UP.SetPtEtaPhiM(self.EventChain.met_JetEta0to5Up,0.0,self.EventChain.metphi_JetEta0to5Up,0.0)
        MetVector_JetEta0to5_DOWN.SetPtEtaPhiM(self.EventChain.met_JetEta0to5Down,0.0,self.EventChain.metphi_JetEta0to5Down,0.0)
        MetVector_JetEC2_UP.SetPtEtaPhiM(self.EventChain.met_JetEC2Up,0.0,self.EventChain.metphi_JetEC2Up,0.0)
        MetVector_JetEC2_DOWN.SetPtEtaPhiM(self.EventChain.met_JetEC2Down,0.0,self.EventChain.metphi_JetEC2Down,0.0)

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
        JetOneVector_JetEC2_UP = ROOT.TLorentzVector()
        JetOneVector_JetEC2_DOWN = ROOT.TLorentzVector()
        
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
        #ask cecile to include these corrections in the ntuple
        JetOneVector_JetEC2_UP.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetOneVector_JetEC2_DOWN.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)

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
        JetTwoVector_JetEC2_UP = ROOT.TLorentzVector()
        JetTwoVector_JetEC2_DOWN = ROOT.TLorentzVector()

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
        #ask cecile to include these corrections in the ntuples
        JetTwoVector_JetEC2_UP.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)
        JetTwoVector_JetEC2_DOWN.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)

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
        MT_JetEC2_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEC2_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEC2_UP))))
        MT_JetEC2_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_JetEC2_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_JetEC2_DOWN))))

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
            'JetEC2Up': MT_JetEC2_UP,
            'JetEC2Down': MT_JetEC2_DOWN,
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
            'JetEta0to5Down': (TauVector+MuVector+MetVector_JetEta0to5_DOWN).Pt(),
            'JetEC2Up': (TauVector+MuVector+MetVector_JetEC2_UP).Pt(),
            'JetEC2Down': (TauVector+MuVector+MetVector_JetEC2_DOWN).Pt(),
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
            'JetEC2Up': (TauVector+MuVector+MetVector_JetEC2_UP+JetOneVector_JetEC2_UP+JetTwoVector_JetEC2_UP).Pt(),
            'JetEC2Down': (TauVector+MuVector+MetVector_JetEC2_DOWN+JetOneVector_JetEC2_DOWN+JetTwoVector_JetEC2_DOWN).Pt(),
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
            'JetEta0to5Down': JetOneVector_JetEta0to5_DOWN.Pt(),
            'JetEC2Up': JetOneVector_JetEC2_UP.Pt(),
            'JetEC2Down': JetOneVector_JetEC2_DOWN.Pt()
            }            
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
            'JetEC2Up': self.EventChain.njets_JetEC2Up,
            'JetEC2Down': self.EventChain.njets_JetEC2Down,
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
            'JetEC2Up': self.EventChain.mjj_JetEC2Up,
            'JetEC2Down': self.EventChain.mjj_JetEC2Down,
        }        
        m_svDictionary = {
            'JetEta0to3Up': self.EventChain.m_sv_JetEta0to3Up,
            'JetEta0to3Down': self.EventChain.m_sv_JetEta0to3Down,
            'JetRelativeBalUp': self.EventChain.m_sv_JetRelativeBalUp,
            'JetRelativeBalDown': self.EventChain.m_sv_JetRelativeBalDown,
            'JetRelativeSampleUp': self.EventChain.m_sv_JetRelativeSampleUp,
            'JetRelativeSampleDown': self.EventChain.m_sv_JetRelativeSampleDown,
            'JetEta3to5Up': self.EventChain.m_sv_JetEta3to5Down,
            'JetEta3to5Down': self.EventChain.m_sv_JetEta3to5Down,
            'JetEta0to5Up': self.EventChain.m_sv_JetEta0to5Up,
            'JetEta0to5Down': self.EventChain.m_sv_JetEta0to5Down,
            'JetEC2Up': self.EventChain.m_sv_JetEC2Up,
            'JetEC2Down': self.EventChain.m_sv_JetEC2Down,
            }

        for Shape in MTDictionary:
            JESDump = NominalDump.copy()
            JESDump['MT'] = MTDictionary[Shape]
            JESDump['njets'] = njetsDictionary[Shape]
            JESDump['mjj'] = mjjDictionary[Shape]
            JESDump['HiggsPt'] = HiggsPtDictionary[Shape]
            JESDump['Higgs_jjPt'] = HiggsjjPtDictionary[Shape]
            JESDump['LeadingJetPt'] = LeadingJetPtDictionary[Shape]
            JESDump['m_sv'] = m_svDictionary[Shape]

            JESCategories = self.ClassifyEvent(JESDump,AnalysisCategories)

            for Category in JESCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_CMS_"+Shape+"_"+Category].Fill(JESDump[AnalysisCategories[Category].ReconstructionVar],JESDump[AnalysisCategories[Category].RollingVar],JESDump['Weight'])
    def ProcessDYShapeUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        ZPT_Up_Dump = NominalDump.copy()
        ZPT_Up_Dump['Weight'] = self.EventChain.FinalWeighting_ZPT_UP
        ZPT_Down_Dump = NominalDump.copy()
        ZPT_Down_Dump['Weight'] = self.EventChain.FinalWeighting_ZPT_DOWN   

        UP_Categories = self.ClassifyEvent(ZPT_Up_Dump,AnalysisCategories)
        DOWN_Categories = self.ClassifyEvent(ZPT_Down_Dump,AnalysisCategories)
        for Category in UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_dyShapeUp_"+Category].Fill(ZPT_Up_Dump[AnalysisCategories[Category].ReconstructionVar],ZPT_Up_Dump[AnalysisCategories[Category].RollingVar],ZPT_Up_Dump['Weight'])
        for Category in DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_dyShapeDown_"+Category].Fill(ZPT_Down_Dump[AnalysisCategories[Category].ReconstructionVar],ZPT_Down_Dump[AnalysisCategories[Category].RollingVar],ZPT_Down_Dump['Weight'])

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
        #no m_sv for this correction?
        ZLDumpUp = NominalDump.copy()
        ZLDumpDown = NominalDump.copy()

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
            ggHDump = NominalDump.copy()
            ggHDump['Weight'] = ggHDictionary[Shape]
            
            ggHCategories = self.ClassifyEvent(ggHDump,AnalysisCategories)
            for Category in ggHCategories:
                self.MasterCategoryDictionary[Category][self.Name+"_"+Shape+"_"+Category].Fill(ggHDump[AnalysisCategories[Category].ReconstructionVar],ggHDump[AnalysisCategories[Category].RollingVar],ggHDump['Weight'])
        
    def ProcessRecoilUncertainties(self,AnalysisCategories,args):
        #print("Processing recoil")
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

        #print("Resolution MT")
        #print("self.EventChain.met_resolutionUp: "+str(self.EventChain.met_resolutionUp))
        #print("self.EventChain.metphi_resolutionUp: "+str(self.EventChain.metphi_resolutionUp))
        #print("self.EventChain.met: "+str(self.EventChain.met))
        #print("MuVector.Pt(): "+str(MuVector.Pt()))
        
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
        
        Resolution_0jetUpDump = NominalDump.copy()
        Resolution_0jetDownDump = NominalDump.copy()
        Response_0jetUpDump = NominalDump.copy()
        Response_0jetDownDump = NominalDump.copy()
        Resolution_1jetUpDump = NominalDump.copy()
        Resolution_1jetDownDump = NominalDump.copy()
        Response_1jetUpDump = NominalDump.copy()
        Response_1jetDownDump = NominalDump.copy()
        Resolution_2jetUpDump = NominalDump.copy()
        Resolution_2jetDownDump = NominalDump.copy()
        Response_2jetUpDump = NominalDump.copy()
        Response_2jetDownDump = NominalDump.copy()

        if self.EventChain.njets == 0:
            Resolution_0jetUpDump['m_sv'] = self.EventChain.m_sv_ResolutionUp
            Resolution_0jetUpDump['MT'] = ResolutionCorrectedMT_UP
            Resolution_0jetUpDump['HiggsPt'] = ResolutionCorrectedHiggsPt_UP
            Resolution_0jetUpDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_UP
            Resolution_0jetDownDump['m_sv'] = self.EventChain.m_sv_ResolutionDown
            Resolution_0jetDownDump['MT'] = ResolutionCorrectedMT_DOWN
            Resolution_0jetDownDump['HiggsPt'] = ResolutionCorrectedHiggsPt_DOWN
            Resolution_0jetDownDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_DOWN
            Response_0jetUpDump['m_sv'] = self.EventChain.m_sv_ResponseUp
            Response_0jetUpDump['MT'] = ResponseCorrectedMT_UP
            Response_0jetUpDump['HiggsPt'] = ResponseCorrectedHiggsPt_UP
            Response_0jetUpDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_UP
            Response_0jetDownDump['m_sv'] = self.EventChain.m_sv_ResponseDown
            Response_0jetDownDump['MT'] = ResponseCorrectedMT_DOWN
            Response_0jetDownDump['HiggsPt'] = ResponseCorrectedHiggsPt_DOWN
            Response_0jetDownDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_DOWN
        if self.EventChain.njets == 1:
            Resolution_1jetUpDump['m_sv'] = self.EventChain.m_sv_ResolutionUp
            Resolution_1jetUpDump['MT'] = ResolutionCorrectedMT_UP
            Resolution_1jetUpDump['HiggsPt'] = ResolutionCorrectedHiggsPt_UP
            Resolution_1jetUpDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_UP
            Resolution_1jetDownDump['m_sv'] = self.EventChain.m_sv_ResolutionDown
            Resolution_1jetDownDump['MT'] = ResolutionCorrectedMT_DOWN
            Resolution_1jetDownDump['HiggsPt'] = ResolutionCorrectedHiggsPt_DOWN
            Resolution_1jetDownDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_DOWN
            Response_1jetUpDump['m_sv'] = self.EventChain.m_sv_ResponseUp
            Response_1jetUpDump['MT'] = ResponseCorrectedMT_UP
            Response_1jetUpDump['HiggsPt'] = ResponseCorrectedHiggsPt_UP
            Response_1jetUpDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_UP
            Response_1jetDownDump['m_sv'] = self.EventChain.m_sv_ResponseDown
            Response_1jetDownDump['MT'] = ResponseCorrectedMT_DOWN
            Response_1jetDownDump['HiggsPt'] = ResponseCorrectedHiggsPt_DOWN
            Response_1jetDownDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_DOWN
        if self.EventChain.njets >= 2:
            Resolution_2jetUpDump['m_sv'] = self.EventChain.m_sv_ResolutionUp
            Resolution_2jetUpDump['MT'] = ResolutionCorrectedMT_UP
            Resolution_2jetUpDump['HiggsPt'] = ResolutionCorrectedHiggsPt_UP
            Resolution_2jetUpDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_UP
            Resolution_2jetDownDump['m_sv'] = self.EventChain.m_sv_ResolutionDown
            Resolution_2jetDownDump['MT'] = ResolutionCorrectedMT_DOWN
            Resolution_2jetDownDump['HiggsPt'] = ResolutionCorrectedHiggsPt_DOWN
            Resolution_2jetDownDump['Higgs_jjPt'] = ResolutionCorrectedHiggsjjPt_DOWN
            Response_2jetUpDump['m_sv'] = self.EventChain.m_sv_ResponseUp
            Response_2jetUpDump['MT'] = ResponseCorrectedMT_UP
            Response_2jetUpDump['HiggsPt'] = ResponseCorrectedHiggsPt_UP
            Response_2jetUpDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_UP
            Response_2jetDownDump['m_sv'] = self.EventChain.m_sv_ResponseDown
            Response_2jetDownDump['MT'] = ResponseCorrectedMT_DOWN
            Response_2jetDownDump['HiggsPt'] = ResponseCorrectedHiggsPt_DOWN
            Response_2jetDownDump['Higgs_jjPt'] = ResponseCorrectedHiggsjjPt_DOWN
        
        Resolution_0jetUpCategories = self.ClassifyEvent(Resolution_0jetUpDump,AnalysisCategories)
        Resolution_0jetDownCategories = self.ClassifyEvent(Resolution_0jetDownDump,AnalysisCategories)
        Response_0jetUpCategories = self.ClassifyEvent(Response_0jetUpDump,AnalysisCategories)
        Response_0jetDownCategories = self.ClassifyEvent(Response_0jetDownDump,AnalysisCategories)
        Resolution_1jetUpCategories = self.ClassifyEvent(Resolution_1jetUpDump,AnalysisCategories)
        Resolution_1jetDownCategories = self.ClassifyEvent(Resolution_1jetDownDump,AnalysisCategories)
        Response_1jetUpCategories = self.ClassifyEvent(Response_1jetUpDump,AnalysisCategories)
        Response_1jetDownCategories = self.ClassifyEvent(Response_1jetDownDump,AnalysisCategories)
        Resolution_2jetUpCategories = self.ClassifyEvent(Resolution_2jetUpDump,AnalysisCategories)
        Resolution_2jetDownCategories = self.ClassifyEvent(Resolution_2jetDownDump,AnalysisCategories)
        Response_2jetUpCategories = self.ClassifyEvent(Response_2jetUpDump,AnalysisCategories)
        Response_2jetDownCategories = self.ClassifyEvent(Response_2jetDownDump,AnalysisCategories)

        for Category in Resolution_0jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_0jetUp_"+Category].Fill(Resolution_0jetUpDump[AnalysisCategories[Category].ReconstructionVar],Resolution_0jetUpDump[AnalysisCategories[Category].RollingVar],Resolution_0jetUpDump['Weight'])
        for Category in Resolution_0jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_0jetDown_"+Category].Fill(Resolution_0jetDownDump[AnalysisCategories[Category].ReconstructionVar],Resolution_0jetDownDump[AnalysisCategories[Category].RollingVar],Resolution_0jetDownDump['Weight'])
        for Category in Response_0jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_0jetUp_"+Category].Fill(Response_0jetUpDump[AnalysisCategories[Category].ReconstructionVar],Response_0jetUpDump[AnalysisCategories[Category].RollingVar],Response_0jetUpDump['Weight'])
        for Category in Response_0jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_0jetDown_"+Category].Fill(Response_0jetDownDump[AnalysisCategories[Category].ReconstructionVar],Response_0jetDownDump[AnalysisCategories[Category].RollingVar],Response_0jetDownDump['Weight'])
        for Category in Resolution_1jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_1jetUp_"+Category].Fill(Resolution_1jetUpDump[AnalysisCategories[Category].ReconstructionVar],Resolution_1jetUpDump[AnalysisCategories[Category].RollingVar],Resolution_1jetUpDump['Weight'])
        for Category in Resolution_1jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_1jetDown_"+Category].Fill(Resolution_1jetDownDump[AnalysisCategories[Category].ReconstructionVar],Resolution_1jetDownDump[AnalysisCategories[Category].RollingVar],Resolution_1jetDownDump['Weight'])
        for Category in Response_1jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_1jetUp_"+Category].Fill(Response_1jetUpDump[AnalysisCategories[Category].ReconstructionVar],Response_1jetUpDump[AnalysisCategories[Category].RollingVar],Response_1jetUpDump['Weight'])
        for Category in Response_1jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_1jetDown_"+Category].Fill(Response_1jetDownDump[AnalysisCategories[Category].ReconstructionVar],Response_1jetDownDump[AnalysisCategories[Category].RollingVar],Response_1jetDownDump['Weight'])
        for Category in Resolution_2jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_2jetUp_"+Category].Fill(Resolution_2jetUpDump[AnalysisCategories[Category].ReconstructionVar],Resolution_2jetUpDump[AnalysisCategories[Category].RollingVar],Resolution_2jetUpDump['Weight'])
        for Category in Resolution_2jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_reso_met_2jetDown_"+Category].Fill(Resolution_2jetDownDump[AnalysisCategories[Category].ReconstructionVar],Resolution_2jetDownDump[AnalysisCategories[Category].RollingVar],Resolution_2jetDownDump['Weight'])
        for Category in Response_2jetUpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_2jetUp_"+Category].Fill(Response_2jetUpDump[AnalysisCategories[Category].ReconstructionVar],Response_2jetUpDump[AnalysisCategories[Category].RollingVar],Response_2jetUpDump['Weight'])
        for Category in Response_2jetDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_boson_scale_met_2jetDown_"+Category].Fill(Response_2jetDownDump[AnalysisCategories[Category].ReconstructionVar],Response_2jetDownDump[AnalysisCategories[Category].RollingVar],Response_2jetDownDump['Weight'])

    def ProcessTTbarContaminationUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)

        TTBarContaminationCats = self.ClassifyEvent(NominalDump,AnalysisCategories)
        
        for Category in TTBarContaminationCats:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_emb_ttbar_"+Category].Fill(NominalDump[AnalysisCategories[Category].ReconstructionVar],NominalDump[AnalysisCategories[Category].RollingVar],NominalDump['Weight'])

    def ProcessMETUESUncertainties(self,AnalysisCategories,args):
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

        MetVector_UES_UP = ROOT.TLorentzVector()
        MetVector_UES_DOWN = ROOT.TLorentzVector()

        MetVector_UES_UP.SetPtEtaPhiM(self.EventChain.met_UESUp,0.0,self.EventChain.metphi_UESUp,0.0)
        MetVector_UES_DOWN.SetPtEtaPhiM(self.EventChain.met_UESDown,0.0,self.EventChain.metphi_UESDown,0.0)

        MT_UES_UP = math.sqrt(2.0*MuVector.Pt()*MetVector_UES_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_UES_UP))))
        MT_UES_DOWN = math.sqrt(2.0*MuVector.Pt()*MetVector_UES_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector_UES_DOWN))))

        HiggsPt_UES_UP = (TauVector+MuVector+MetVector_UES_UP).Pt()
        HiggsPt_UES_DOWN = (TauVector+MuVector+MetVector_UES_DOWN).Pt()

        HiggsjjPt_UP = (TauVector+MuVector+MetVector_UES_UP+JetOneVector+JetTwoVector).Pt()
        HiggsjjPt_DOWN = (TauVector+MuVector+MetVector_UES_DOWN+JetOneVector+JetTwoVector).Pt()

        UESUpDump = NominalDump.copy()
        UESDownDump = NominalDump.copy()

        UESUpDump['MT'] = MT_UES_UP
        UESUpDump['HiggsPt'] = HiggsPt_UES_UP
        UESUpDump['Higgs_jjPt'] = HiggsjjPt_UP
        UESUpDump['m_sv'] = self.EventChain.m_sv_UESUp

        UESDownDump['MT'] = MT_UES_DOWN
        UESDownDump['HiggsPt'] = HiggsPt_UES_DOWN
        UESDownDump['Higgs_jjPt'] = HiggsjjPt_DOWN
        UESDownDump['m_sv'] = self.EventChain.m_sv_UESDown

        UESUpCategories = self.ClassifyEvent(UESUpDump,AnalysisCategories)
        UESDownCategories = self.ClassifyEvent(UESDownDump,AnalysisCategories)

        for Category in UESUpCategories:            
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_met_unclusteredUp_"+Category].Fill(UESUpDump[AnalysisCategories[Category].ReconstructionVar],UESUpDump[AnalysisCategories[Category].RollingVar],UESUpDump['Weight'])
        for Category in UESDownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_met_unclusteredDown_"+Category].Fill(UESDownDump[AnalysisCategories[Category].ReconstructionVar],UESDownDump[AnalysisCategories[Category].RollingVar],UESDownDump['Weight'])

    def ProcessTTbarShapeUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)
        TTbar_Up_Dump = NominalDump.copy()
        TTbar_Up_Dump['Weight'] = self.EventChain.FinalWeighting_TOP_UP
        TTbar_Down_Dump = NominalDump.copy()
        TTbar_Down_Dump['Weight'] = self.EventChain.FinalWeighting_TOP_DOWN

        UpCategories = self.ClassifyEvent(TTbar_Up_Dump,AnalysisCategories)
        DownCategories = self.ClassifyEvent(TTbar_Down_Dump,AnalysisCategories)
        for Category in UpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_ttbarShapeUp_"+Category].Fill(TTbar_Up_Dump[AnalysisCategories[Category].ReconstructionVar],TTbar_Up_Dump[AnalysisCategories[Category].RollingVar],TTbar_Up_Dump['Weight'])
        for Category in DownCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_htt_ttbarShapeDown_"+Category].Fill(TTbar_Down_Dump[AnalysisCategories[Category].ReconstructionVar],TTbar_Down_Dump[AnalysisCategories[Category].RollingVar],TTbar_Down_Dump['Weight'])

    def ProcessMuonESUncertainties(self,AnalysisCategories,args):
        NominalDump = self.GetEventDump(self.EventChain,args)

        MuVector=ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)

        CorrectedMuVector_UP = ROOT.TLorentzVector()
        CorrectedMuVector_DOWN = ROOT.TLorentzVector()
        CorrectedMuVector_UP.SetPtEtaPhiE(self.EventChain.muonES_Pt_UP,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.muonES_E_UP)
        CorrectedMuVector_DOWN.SetPtEtaPhiE(self.EventChain.muonES_Pt_DOWN,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.muonES_E_DOWN)

        JetOneVector = ROOT.TLorentzVector()
        JetTwoVector = ROOT.TLorentzVector()
        JetOneVector.SetPtEtaPhiM(self.EventChain.jpt_1,self.EventChain.jeta_1,self.EventChain.jphi_1,0.0)
        JetTwoVector.SetPtEtaPhiM(self.EventChain.jpt_2,self.EventChain.jeta_2,self.EventChain.jphi_2,0.0)

        TauVector = ROOT.TLorentzVector()
        TauVector.SetPtEtaPhiE(self.EventChain.pt_2,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.e_2)

        MetVector = ROOT.TLorentzVector()
        MetVector.SetPtEtaPhiM(self.EventChain.met,0.0,self.EventChain.metphi,0.0)
        
        CorrectedMetVector_UP = ROOT.TLorentzVector()
        CorrectedMetVector_DOWN = ROOT.TLorentzVector()
        CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.muonES_MET_UP,0.0,self.EventChain.muonES_METPhi_UP,0.0)
        CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.muonES_MET_DOWN,0.0,self.EventChain.muonES_METPhi_DOWN,0.0)

        MT = math.sqrt(2.0*MuVector.Pt()*MetVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(MetVector))))

        CorrectedMT_UP = math.sqrt(2.0*CorrectedMuVector_UP.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(CorrectedMuVector_UP.DeltaPhi(CorrectedMetVector_UP))))
        CorrectedMT_DOWN = math.sqrt(2.0*CorrectedMuVector_DOWN.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(CorrectedMuVector_DOWN.DeltaPhi(CorrectedMetVector_DOWN))))

        #five uncertainties * Up+Down = 10 new dumps
        etam2p4tom2p1_UP_Dump = NominalDump.copy()
        etam2p1tom1p2_UP_Dump = NominalDump.copy()
        etam1p2to1p2_UP_Dump = NominalDump.copy()
        eta1p2to2p1_UP_Dump = NominalDump.copy()
        eta2p1to2p4_UP_Dump = NominalDump.copy()
        etam2p4tom2p1_DOWN_Dump = NominalDump.copy()
        etam2p1tom1p2_DOWN_Dump = NominalDump.copy()
        etam1p2to1p2_DOWN_Dump = NominalDump.copy()
        eta1p2to2p1_DOWN_Dump = NominalDump.copy()
        eta2p1to2p4_DOWN_Dump = NominalDump.copy()
        if self.EventChain.eta_1 > -2.4 and self.EventChain.eta_1 < -2.1:
            etam2p4tom2p1_UP_Dump['MuPt'] = CorrectedMuVector_UP.Pt()
            etam2p4tom2p1_UP_Dump['MuEta'] = CorrectedMuVector_UP.Eta()
            etam2p4tom2p1_UP_Dump['MuPhi'] = CorrectedMuVector_UP.Phi()
            etam2p4tom2p1_UP_Dump['MuM'] = CorrectedMuVector_UP.M()
            etam2p4tom2p1_UP_Dump['MT'] = CorrectedMT_UP
            etam2p4tom2p1_UP_Dump['m_vis'] = (CorrectedMuVector_UP+TauVector).M()
            etam2p4tom2p1_UP_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam2p4tom2p1_UP_Dump['HiggsPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP).Pt()
            etam2p4tom2p1_UP_Dump['Higgs_jjPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
            etam2p4tom2p1_DOWN_Dump['MuPt'] = CorrectedMuVector_DOWN.Pt()
            etam2p4tom2p1_DOWN_Dump['MuEta'] = CorrectedMuVector_DOWN.Eta()
            etam2p4tom2p1_DOWN_Dump['MuPhi'] = CorrectedMuVector_DOWN.Phi()
            etam2p4tom2p1_DOWN_Dump['MuM'] = CorrectedMuVector_DOWN.M()
            etam2p4tom2p1_DOWN_Dump['MT'] = CorrectedMT_DOWN
            etam2p4tom2p1_DOWN_Dump['m_vis'] = (CorrectedMuVector_DOWN+TauVector).M()
            etam2p4tom2p1_DOWN_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam2p4tom2p1_DOWN_Dump['HiggsPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN).Pt()
            etam2p4tom2p1_DOWN_Dump['Higgs_jjPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.eta_1 > -2.1 and self.EventChain.eta_1 < -1.2:
            etam2p1tom1p2_UP_Dump['MuPt'] = CorrectedMuVector_UP.Pt()
            etam2p1tom1p2_UP_Dump['MuEta'] = CorrectedMuVector_UP.Eta()
            etam2p1tom1p2_UP_Dump['MuPhi'] = CorrectedMuVector_UP.Phi()
            etam2p1tom1p2_UP_Dump['MuM'] = CorrectedMuVector_UP.M()
            etam2p1tom1p2_UP_Dump['MT'] = CorrectedMT_UP
            etam2p1tom1p2_UP_Dump['m_vis'] = (CorrectedMuVector_UP+TauVector).M()
            etam2p1tom1p2_UP_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam2p1tom1p2_UP_Dump['HiggsPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP).Pt()
            etam2p1tom1p2_UP_Dump['Higgs_jjPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
            etam2p1tom1p2_DOWN_Dump['MuPt'] = CorrectedMuVector_DOWN.Pt()
            etam2p1tom1p2_DOWN_Dump['MuEta'] = CorrectedMuVector_DOWN.Eta()
            etam2p1tom1p2_DOWN_Dump['MuPhi'] = CorrectedMuVector_DOWN.Phi()
            etam2p1tom1p2_DOWN_Dump['MuM'] = CorrectedMuVector_DOWN.M()
            etam2p1tom1p2_DOWN_Dump['MT'] = CorrectedMT_DOWN
            etam2p1tom1p2_DOWN_Dump['m_vis'] = (CorrectedMuVector_DOWN+TauVector).M()
            etam2p1tom1p2_DOWN_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam2p1tom1p2_DOWN_Dump['HiggsPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN).Pt()
            etam2p1tom1p2_DOWN_Dump['Higgs_jjPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.eta_1 > -1.2 and self.EventChain.eta_1 < 1.2:
            etam1p2to1p2_UP_Dump['MuPt'] = CorrectedMuVector_UP.Pt()
            etam1p2to1p2_UP_Dump['MuEta'] = CorrectedMuVector_UP.Eta()
            etam1p2to1p2_UP_Dump['MuPhi'] = CorrectedMuVector_UP.Phi()
            etam1p2to1p2_UP_Dump['MuM'] = CorrectedMuVector_UP.M()
            etam1p2to1p2_UP_Dump['MT'] = CorrectedMT_UP
            etam1p2to1p2_UP_Dump['m_vis'] = (CorrectedMuVector_UP+TauVector).M()
            etam1p2to1p2_UP_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam1p2to1p2_UP_Dump['HiggsPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP).Pt()
            etam1p2to1p2_UP_Dump['Higgs_jjPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
            etam1p2to1p2_DOWN_Dump['MuPt'] = CorrectedMuVector_DOWN.Pt()
            etam1p2to1p2_DOWN_Dump['MuEta'] = CorrectedMuVector_DOWN.Eta()
            etam1p2to1p2_DOWN_Dump['MuPhi'] = CorrectedMuVector_DOWN.Phi()
            etam1p2to1p2_DOWN_Dump['MuM'] = CorrectedMuVector_DOWN.M()
            etam1p2to1p2_DOWN_Dump['MT'] = CorrectedMT_DOWN
            etam1p2to1p2_DOWN_Dump['m_vis'] = (CorrectedMuVector_DOWN+TauVector).M()
            etam1p2to1p2_DOWN_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            etam1p2to1p2_DOWN_Dump['HiggsPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN).Pt()
            etam1p2to1p2_DOWN_Dump['Higgs_jjPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.eta_1 > 1.2 and self.EventChain.eta_1 < 2.1:
            eta1p2to2p1_UP_Dump['MuPt'] = CorrectedMuVector_UP.Pt()
            eta1p2to2p1_UP_Dump['MuEta'] = CorrectedMuVector_UP.Eta()
            eta1p2to2p1_UP_Dump['MuPhi'] = CorrectedMuVector_UP.Phi()
            eta1p2to2p1_UP_Dump['MuM'] = CorrectedMuVector_UP.M()
            eta1p2to2p1_UP_Dump['MT'] = CorrectedMT_UP
            eta1p2to2p1_UP_Dump['m_vis'] = (CorrectedMuVector_UP+TauVector).M()
            eta1p2to2p1_UP_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            eta1p2to2p1_UP_Dump['HiggsPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP).Pt()
            eta1p2to2p1_UP_Dump['Higgs_jjPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
            eta1p2to2p1_DOWN_Dump['MuPt'] = CorrectedMuVector_DOWN.Pt()
            eta1p2to2p1_DOWN_Dump['MuEta'] = CorrectedMuVector_DOWN.Eta()
            eta1p2to2p1_DOWN_Dump['MuPhi'] = CorrectedMuVector_DOWN.Phi()
            eta1p2to2p1_DOWN_Dump['MuM'] = CorrectedMuVector_DOWN.M()
            eta1p2to2p1_DOWN_Dump['MT'] = CorrectedMT_DOWN
            eta1p2to2p1_DOWN_Dump['m_vis'] = (CorrectedMuVector_DOWN+TauVector).M()
            eta1p2to2p1_DOWN_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            eta1p2to2p1_DOWN_Dump['HiggsPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN).Pt()
            eta1p2to2p1_DOWN_Dump['Higgs_jjPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        elif self.EventChain.eta_1 > 2.1 and self.EventChain.eta_1 < 2.4:
            eta2p1to2p4_UP_Dump['MuPt'] = CorrectedMuVector_UP.Pt()
            eta2p1to2p4_UP_Dump['MuEta'] = CorrectedMuVector_UP.Eta()
            eta2p1to2p4_UP_Dump['MuPhi'] = CorrectedMuVector_UP.Phi()
            eta2p1to2p4_UP_Dump['MuM'] = CorrectedMuVector_UP.M()
            eta2p1to2p4_UP_Dump['MT'] = CorrectedMT_UP
            eta2p1to2p4_UP_Dump['m_vis'] = (CorrectedMuVector_UP+TauVector).M()
            eta2p1to2p4_UP_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            eta2p1to2p4_UP_Dump['HiggsPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP).Pt()
            eta2p1to2p4_UP_Dump['Higgs_jjPt'] = (CorrectedMuVector_UP+TauVector+CorrectedMetVector_UP+JetOneVector+JetTwoVector).Pt()
            eta2p1to2p4_DOWN_Dump['MuPt'] = CorrectedMuVector_DOWN.Pt()
            eta2p1to2p4_DOWN_Dump['MuEta'] = CorrectedMuVector_DOWN.Eta()
            eta2p1to2p4_DOWN_Dump['MuPhi'] = CorrectedMuVector_DOWN.Phi()
            eta2p1to2p4_DOWN_Dump['MuM'] = CorrectedMuVector_DOWN.M()
            eta2p1to2p4_DOWN_Dump['MT'] = CorrectedMT_DOWN
            eta2p1to2p4_DOWN_Dump['m_vis'] = (CorrectedMuVector_DOWN+TauVector).M()
            eta2p1to2p4_DOWN_Dump['m_sv'] = self.EventChain.m_sv_muonESUp
            eta2p1to2p4_DOWN_Dump['HiggsPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN).Pt()
            eta2p1to2p4_DOWN_Dump['Higgs_jjPt'] = (CorrectedMuVector_DOWN+TauVector+CorrectedMetVector_DOWN+JetOneVector+JetTwoVector).Pt()
        etam2p4tom2p1_UP_Categories = self.ClassifyEvent(etam2p4tom2p1_UP_Dump,AnalysisCategories)
        etam2p4tom2p1_DOWN_Categories = self.ClassifyEvent(etam2p4tom2p1_DOWN_Dump,AnalysisCategories)
        etam2p1tom1p2_UP_Categories = self.ClassifyEvent(etam2p1tom1p2_UP_Dump,AnalysisCategories)
        etam2p1tom1p2_DOWN_Categories = self.ClassifyEvent(etam2p1tom1p2_DOWN_Dump,AnalysisCategories)
        etam1p2to1p2_UP_Categories = self.ClassifyEvent(etam1p2to1p2_UP_Dump,AnalysisCategories)
        etam1p2to1p2_DOWN_Categories = self.ClassifyEvent(etam1p2to1p2_DOWN_Dump,AnalysisCategories)
        eta1p2to2p1_UP_Categories = self.ClassifyEvent(eta1p2to2p1_UP_Dump,AnalysisCategories)
        eta1p2to2p1_DOWN_Categories = self.ClassifyEvent(eta1p2to2p1_DOWN_Dump,AnalysisCategories)
        eta2p1to2p4_UP_Categories = self.ClassifyEvent(eta2p1to2p4_UP_Dump,AnalysisCategories)
        eta2p1to2p4_DOWN_Categories = self.ClassifyEvent(eta2p1to2p4_DOWN_Dump,AnalysisCategories)

        for Category in etam2p4tom2p1_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam2p4tom2p1Up_"+Category].Fill(etam2p4tom2p1_UP_Dump[AnalysisCategories[Category].ReconstructionVar],etam2p4tom2p1_UP_Dump[AnalysisCategories[Category].RollingVar],etam2p4tom2p1_UP_Dump['Weight'])
        for Category in etam2p4tom2p1_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam2p4tom2p1Down_"+Category].Fill(etam2p4tom2p1_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],etam2p4tom2p1_DOWN_Dump[AnalysisCategories[Category].RollingVar],etam2p4tom2p1_DOWN_Dump['Weight'])

        for Category in etam2p1tom1p2_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam2p1tom1p2Up_"+Category].Fill(etam2p1tom1p2_UP_Dump[AnalysisCategories[Category].ReconstructionVar],etam2p1tom1p2_UP_Dump[AnalysisCategories[Category].RollingVar],etam2p1tom1p2_UP_Dump['Weight'])
        for Category in etam2p1tom1p2_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam2p1tom1p2Down_"+Category].Fill(etam2p1tom1p2_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],etam2p1tom1p2_DOWN_Dump[AnalysisCategories[Category].RollingVar],etam2p1tom1p2_DOWN_Dump['Weight'])

        for Category in etam1p2to1p2_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam1p2to1p2Up_"+Category].Fill(etam1p2to1p2_UP_Dump[AnalysisCategories[Category].ReconstructionVar],etam1p2to1p2_UP_Dump[AnalysisCategories[Category].RollingVar],etam1p2to1p2_UP_Dump['Weight'])
        for Category in etam1p2to1p2_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_etam1p2to1p2Down_"+Category].Fill(etam1p2to1p2_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],etam1p2to1p2_DOWN_Dump[AnalysisCategories[Category].RollingVar],etam1p2to1p2_DOWN_Dump['Weight'])

        for Category in eta1p2to2p1_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_eta1p2to2p1Up_"+Category].Fill(eta1p2to2p1_UP_Dump[AnalysisCategories[Category].ReconstructionVar],eta1p2to2p1_UP_Dump[AnalysisCategories[Category].RollingVar],eta1p2to2p1_UP_Dump['Weight'])
        for Category in eta1p2to2p1_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_eta1p2to2p1Down_"+Category].Fill(eta1p2to2p1_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],eta1p2to2p1_DOWN_Dump[AnalysisCategories[Category].RollingVar],eta1p2to2p1_DOWN_Dump['Weight'])

        for Category in eta2p1to2p4_UP_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_eta2p1to2p4Up_"+Category].Fill(eta2p1to2p4_UP_Dump[AnalysisCategories[Category].ReconstructionVar],eta2p1to2p4_UP_Dump[AnalysisCategories[Category].RollingVar],eta2p1to2p4_UP_Dump['Weight'])
        for Category in eta2p1to2p4_DOWN_Categories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_scale_m_eta2p1to2p4Down_"+Category].Fill(eta2p1to2p4_DOWN_Dump[AnalysisCategories[Category].ReconstructionVar],eta2p1to2p4_DOWN_Dump[AnalysisCategories[Category].RollingVar],eta2p1to2p4_DOWN_Dump['Weight'])
    
    def ProcessJtoTUncertainties(self,AnalysisCategories,args):
        MuVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(self.EventChain.pt_1,self.EventChain.eta_1,self.EventChain.phi_1,self.EventChain.m_1)
        
        CorrectedTauVector_UP = ROOT.TLorentzVector()
        CorrectedTauVector_DOWN = ROOT.TLorentzVector()

        CorrectedMetVector_UP = ROOT.TLorentzVector()
        CorrectedMetVector_DOWN = ROOT.TLorentzVector()
        
        CorrectedTauVector_UP.SetPtEtaPhiE(self.EventChain.JtoT_Pt_UP,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.JtoT_E_UP)
        CorrectedTauVector_DOWN.SetPtEtaPhiE(self.EventChain.JtoT_Pt_DOWN,self.EventChain.eta_2,self.EventChain.phi_2,self.EventChain.JtoT_E_DOWN)

        CorrectedMetVector_UP.SetPtEtaPhiM(self.EventChain.JtoT_MET_UP,0.0,self.EventChain.JtoT_METPhi_UP,0.0)
        CorrectedMetVector_DOWN.SetPtEtaPhiM(self.EventChain.JtoT_MET_DOWN,0.0,self.EventChain.JtoT_METPhi_DOWN,0.0)

        CorrectedMT_UP = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_UP.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_UP))))
        CorrectedMT_DOWN = math.sqrt(2.0*MuVector.Pt()*CorrectedMetVector_DOWN.Pt()*(1.0-math.cos(MuVector.DeltaPhi(CorrectedMetVector_DOWN))))        

        NominalDump = self.GetEventDump(self.EventChain,args)
        Up_Dump = NominalDump.copy()
        Down_Dump = NominalDump.copy()
        Up_Dump['TauPt'] = CorrectedTauVector_UP.Pt()
        Up_Dump['TauEta'] = CorrectedTauVector_UP.Eta()
        Up_Dump['TauPhi'] = CorrectedTauVector_UP.Phi()
        Up_Dump['TauM'] = CorrectedTauVector_UP.M()
        Up_Dump['m_vis'] = (CorrectedTauVector_UP + MuVector).M()
        Up_Dump['MT'] = CorrectedMT_UP
        Down_Dump['TauPt'] = CorrectedTauVector_DOWN.Pt()
        Down_Dump['TauEta'] = CorrectedTauVector_DOWN.Eta()
        Down_Dump['TauPhi'] = CorrectedTauVector_DOWN.Phi()
        Down_Dump['TauM'] = CorrectedTauVector_DOWN.M()
        Down_Dump['m_vis'] = (CorrectedTauVector_DOWN + MuVector).M()
        Down_Dump['MT'] = CorrectedMT_DOWN

        UpCategories = self.ClassifyEvent(Up_Dump,AnalysisCategories)
        DownCategories = self.ClassifyEvent(Down_Dump,AnalysisCategories)
        for Category in UpCategories:
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_JtoTUp_"+Category].Fill(Up_Dump[AnalysisCategories[Category].ReconstructionVar],Up_Dump[AnalysisCategories[Category].RollingVar],Up_Dump['Weight'])
            self.MasterCategoryDictionary[Category][self.Name+"_CMS_JtoTDown_"+Category].Fill(Down_Dump[AnalysisCategories[Category].ReconstructionVar],Down_Dump[AnalysisCategories[Category].RollingVar],Down_Dump['Weight'])

    #go trhough the master dictionary,
    # and replace all histogram entries with their unrolled counterparts
    def UnrollAllDistributions(self):
        for Cat in self.MasterCategoryDictionary:
            for HistoName in self.MasterCategoryDictionary[Cat]:
                self.MasterCategoryDictionary[Cat][HistoName] = UnrollDistributions.Unroll(self.MasterCategoryDictionary[Cat][HistoName])
