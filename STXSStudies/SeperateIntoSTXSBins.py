import ROOT
import argparse
from tqdm import tqdm
import math

def DetermineggHBin(TheTree,args):
    MuVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    MuVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
    TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
    METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
    JetOneVector = ROOT.TLorentzVector()
    JetOneVector.SetPtEtaPhiM(TheTree.jpt_1,TheTree.jeta_1,TheTree.jphi_1,0.0)
    JetTwoVector = ROOT.TLorentzVector()
    JetTwoVector.SetPtEtaPhiM(TheTree.jpt_2,TheTree.jeta_2,TheTree.jphi_2,0.0)
    
    HiggsPt = (TauVector+MuVector+METVector).Pt()
    Higgs_jjPt = (TauVector+MuVector+METVector+JetOneVector+JetTwoVector).Pt()
    if args.year == "2017":
        njetsVariable = TheTree.njetsWoNoisyJets
        mjjVariable = TheTree.mjjWoNoisyJets
    elif args.year == "2018":
        njetsVariable = TheTree.njets
        mjjVariable = TheTree.mjj
    elif args.year == "2016":
        raise RuntimeError("2016 not implemented. Implement me!")

    if HiggsPt < 200.0:
        if njetsVariable == 0:
            if HiggsPt < 10.0 and HiggsPt > 0:
                return '2'
            elif HiggsPt >= 10.0:
                return '3'
        elif njetsVariable == 1:
            if HiggsPt < 60.0 and HiggsPt > 0.0:
                return '4'
            elif HiggsPt < 120.0 and HiggsPt >= 60.0:
                return '5'
            elif HiggsPt < 200.0 and HiggsPt >= 120.0:
                return '6'
        elif njetsVariable >= 2:
            if mjjVariable < 350.0 and mjjVariable >= 0.0:                
                if HiggsPt > 0.0 and HiggsPt <= 60.0:
                    return '7'
                elif HiggsPt > 60.0 and HiggsPt <= 120.0:
                    return '8'
                elif HiggsPt > 120.0 and HiggsPt <= 200.0:
                    return '9'                
            elif mjjVariable >=350.0:
                if Higgs_jjPt < 25.0 and Higgs_jjPt > 0.0:
                    if njetsVariable == 2 and mjjVariable < 700.0:
                        return '10'
                    elif njetsVariable == 2 and mjjVariable >= 700:
                        return '11'
                elif Higgs_jjPt > 25.0:
                    if njetsVariable == 3 and mjjVariable < 700.0:
                        return '12'
                    elif njetsVariable == 3 and mjjVariable >= 700:
                        return '13'
    else:
        return '1'
    return 'X'

def DetermineqqHBin(TheTree,args):
    MuVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    MuVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
    TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
    METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
    JetOneVector = ROOT.TLorentzVector()
    JetOneVector.SetPtEtaPhiM(TheTree.jpt_1,TheTree.jeta_1,TheTree.jphi_1,0.0)
    JetTwoVector = ROOT.TLorentzVector()
    JetTwoVector.SetPtEtaPhiM(TheTree.jpt_2,TheTree.jeta_2,TheTree.jphi_2,0.0)
    
    HiggsPt = (TauVector+MuVector+METVector).Pt()
    Higgs_jjPt = (TauVector+MuVector+METVector+JetOneVector+JetTwoVector).Pt()
    if args.year == "2017":
        njetsVariable = TheTree.njetsWoNoisyJets
        mjjVariable = TheTree.mjjWoNoisyJets
    elif args.year == "2018":
        njetsVariable = TheTree.njets
        mjjVariable = TheTree.mjj
    elif args.year == "2016":
        raise RuntimeError("2016 not implemented. Implement me!")

    if njetsVariable >= 2:
        if mjjVariable < 350.0 and mjjVariable >= 0:
            #I think the fact that the rest of the bins are whited out 
            #may mean they are not included as a part of the VBF
            if mjjVariable >= 60.0 and mjjVariable < 120:
                return '1'
        elif mjjVariable >= 350.0:
            if HiggsPt >= 0.0 and HiggsPt < 200.0:
                if Higgs_jjPt < 25.0 and Higgs_jjPt >= 0.0 and njetsVariable == 2:
                    if mjjVariable < 700.0:
                        return '2'
                    elif mjjVariable >= 700.0:
                        return '3'
                elif Higgs_jjPt >= 25.0 and njetsVariable >= 3:
                    if mjjVariable < 700:
                        return '4'
                    elif mjjVariable >= 700:
                        return '5'
            elif HiggsPt >= 200.0:
                return '6'
    #not considered to be part of the qqH STXS
    else:
        return 'X'
    return 'X'
    
def DetermineVHBin(TheTree,args):
    #primary decision in this categroy is just based on the pt
    #of the vector boson. How do we reconstruct that?
    #Well working in a V(invisible)H(tt or lt or em) (Veto all extra leptons other than higgs)
    # I would guess that the V products are related to met. There does seem to be geninfo
    # avaialable under a rivet tag... For now I think just using the MET as a yardstick
    MuVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()
    MuVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
    TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
    METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
    JetOneVector = ROOT.TLorentzVector()
    JetOneVector.SetPtEtaPhiM(TheTree.jpt_1,TheTree.jeta_1,TheTree.jphi_1,0.0)
    JetTwoVector = ROOT.TLorentzVector()
    JetTwoVector.SetPtEtaPhiM(TheTree.jpt_2,TheTree.jeta_2,TheTree.jphi_2,0.0)
    
    HiggsPt = (TauVector+MuVector+METVector).Pt()
    Higgs_jjPt = (TauVector+MuVector+METVector+JetOneVector+JetTwoVector).Pt()
    if args.year == "2017":
        njetsVariable = TheTree.njetsWoNoisyJets
        mjjVariable = TheTree.mjjWoNoisyJets
    elif args.year == "2018":
        njetsVariable = TheTree.njets
        mjjVariable = TheTree.mjj
    elif args.year == "2016":
        raise RuntimeError("2016 not implemented. Implement me!")

    if TheTree.met >= 0 and TheTree.met < 75.0:
        return '1'
    elif TheTree.met >= 75.0 and TheTree.met < 150.0:
        return '2'
    elif TheTree.met >= 150.0 and TheTree.met < 250.0:
        if njetsVariable == 0:
            return '3'
        elif njetsVariable >= 1:
            return '4'
    elif TheTree.met >= 250.0:
        return '5'
    return 'X'
    
def CreateggHClassification(File,Tree,args):
    ggHBin = DetermineggHBin(Tree,args)
    if File in args.ggHSignalFiles:
        ggHBin += 'S'
    elif File in args.ggHBackgroundFiles:
        ggHBin += 'B'
    elif File in args.NonHiggsBackgroundFiles:
        ggHBin += 'N'
    elif File in args.DataFiles:
        ggHBin += 'D'
    return ggHBin

def CreateqqHClassification(File,Tree,args):
    qqHBin = DetermineqqHBin(Tree,args)
    if File in args.qqHSignalFiles:
        qqHBin += 'S'
    elif File in args.qqHBackgroundFiles:
        qqHBin += 'B'
    elif File in args.NonHiggsBackgroundFiles:
        qqHBin += 'N'
    elif File in args.DataFiles:
        qqHBin += 'D'
    return qqHBin

def CreateVHClassification(File,Tree,args):
    VHBin = DetermineVHBin(Tree,args)
    if File in args.VHSignalFiles:
        VHBin += 'S'
    elif File in args.VHBackgroundFiles:
        VHBin += 'B'
    elif File in args.NonHiggsBackgroundFiles:
        VHBin += 'N'
    elif File in args.DataFiles:
        VHBin += 'D'
    return VHBin

def SeperateIntoSTXSBins(File,args):
    TheFile = ROOT.TFile(File)
    TheTree = TheFile.mt_Selected

    #Create the dictionaries of histograms that we will fill
    ggHDictionary = {}
    qqHDictionary = {}
    VHDictionary = {}
    print("Creating the dictionaries...")
    for tag in ['S','B','N','D']:
        #ggH: 13 bins
        for BinNum in range(1,14):
            ggHDictionary[str(BinNum)+tag] = ROOT.TH1F("ggH"+str(BinNum)+tag,str(BinNum)+tag,
                                                       1,50.0,150.0)
            ggHDictionary[str(BinNum)+tag].SetDirectory(0)
        ggHDictionary['X'+tag] = ROOT.TH1F("ggH"+'X'+tag,'X'+tag,
                                                   1,50.0,150.0)
        ggHDictionary['X'+tag].SetDirectory(0)
        #qqH: 6 bins, and the outsides
        for BinNum in range(1,7):
            qqHDictionary[str(BinNum)+tag] = ROOT.TH1F("qqH"+str(BinNum)+tag,str(BinNum)+tag,
                                                       1,50.0,150.0)
            qqHDictionary[str(BinNum)+tag].SetDirectory(0)
        qqHDictionary['X'+tag] = ROOT.TH1F("qqH"+'X'+tag,'X'+tag,
                                           1,50.0,150.0)
        qqHDictionary['X'+tag].SetDirectory(0)
        #VH: 5 bins
        for BinNum in range(1,6):
            VHDictionary[str(BinNum)+tag] = ROOT.TH1F("VH"+str(BinNum)+tag,str(BinNum)+tag,
                                                      1,50.0,150.0)
            VHDictionary[str(BinNum)+tag].SetDirectory(0)
        VHDictionary['X'+tag] = ROOT.TH1F("VH"+'X'+tag,'X'+tag,
                                          1,50.0,150.0)
        VHDictionary['X'+tag].SetDirectory(0)

    print("Running the tree...")
    for i in tqdm(range(TheTree.GetEntries())):
        TheTree.GetEntry(i)

        ggHClassification = CreateggHClassification(File,TheTree,args)
        qqHClassification = CreateqqHClassification(File,TheTree,args)
        VHClassification = CreateVHClassification(File,TheTree,args)

        MuVector = ROOT.TLorentzVector()
        TauVector = ROOT.TLorentzVector()
        METVector = ROOT.TLorentzVector()
        MuVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_1,TheTree.phi_1,TheTree.m_1)
        TauVector.SetPtEtaPhiM(TheTree.pt_2,TheTree.eta_2,TheTree.phi_2,TheTree.m_2)
        METVector.SetPtEtaPhiM(TheTree.met,0.0,TheTree.metphi,0.0)
        MT = math.sqrt(2.0*MuVector.Pt()*METVector.Pt()*(1.0-math.cos(MuVector.DeltaPhi(METVector))))

        #perform the final Selection?
        if(MT > 50.0):
            continue

        TheWeight = TheTree.FinalWeighting
        if File in args.UseFakeFactorOnFiles:
            TheWeight = TheWeight * TheTree.Event_Fake_Factor

        ggHDictionary[ggHClassification].Fill((MuVector+TauVector).M(),TheWeight)
        qqHDictionary[qqHClassification].Fill((MuVector+TauVector).M(),TheWeight)
        VHDictionary[VHClassification].Fill((MuVector+TauVector).M(),TheWeight)
    return ggHDictionary,qqHDictionary,VHDictionary
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate plots seperating distributions into reconstructed STXS categories")
    parser.add_argument('year',nargs='?',choices=["2016","2017","2018"],help="Choose which year's data is to be processed")
    parser.add_argument('Files',nargs="+",help="List of files to run seperate into the STXS bins")
    parser.add_argument('--ggHSignalFiles',nargs="+",help="Treat the ntuple as a part of the higgs signal in the ggH category")
    parser.add_argument('--ggHBackgroundFiles',nargs="+",help="Treat the ntuple as higgs, but as background in the ggH category")
    parser.add_argument('--qqHSignalFiles',nargs="+",help="Treat the ntuple as part of the higgs signal in the qqH category")
    parser.add_argument('--qqHBackgroundFiles',nargs="+",help="Treat the ntuple as higgs, but as background in the qqH category")
    parser.add_argument('--VHSignalFiles',nargs="+",help="Treat the ntuple as part of the higgs signal in the VH category")
    parser.add_argument('--VHBackgroundFiles',nargs="+",help="Treat the ntuple as higgs, but as background in the VH category")
    parser.add_argument('--NonHiggsBackgroundFiles',nargs="+",help="Treat the ntuple as a non higgs background in any/all categories")
    parser.add_argument('--UseFakeFactorOnFiles',nargs='+',help="Use the fake factor weightings")
    parser.add_argument('--DataFiles',nargs="+",help="The ntuple here is to be treated as Data")

    args = parser.parse_args()
    
    isFirstFile = True
    
    for File in args.Files:
        print("Seperating the bins for "+File+"...")
        NewggHDictionary,NewqqHDictionary,NewVHDictionary = SeperateIntoSTXSBins(File,args)
        if isFirstFile:
            print("Is first file")
            ggHDictionary=NewggHDictionary
            qqHDictionary=NewqqHDictionary
            VHDictionary=NewVHDictionary            
            isFirstFile = False
        else:
            print("Adding these results to previous")
            for key in ggHDictionary.keys():                
                ggHDictionary[key].Add(NewggHDictionary[key])
            for key in qqHDictionary.keys():
                qqHDictionary[key].Add(NewqqHDictionary[key])
            for key in VHDictionary.keys():
                VHDictionary[key].Add(NewVHDictionary[key])
    #We should have a set of dictionaries now with completed stuff
    #let's just dump them to screen, and work out a more convenient way of
    #talking about this later.
    print("ggH bins:")
    ggHKeys = ggHDictionary.keys()
    ggHKeys.sort()
    qqHKeys = qqHDictionary.keys()
    qqHKeys.sort()
    VHKeys = VHDictionary.keys()
    VHKeys.sort()
    for key in ggHKeys:
        print(key+":")
        print ggHDictionary[key].Integral()
        print ''
    print("qqH bins:")
    for key in qqHKeys:
        print(key+":")
        print qqHDictionary[key].Integral()
        print ''
    print("VH bins:")
    for key in VHKeys:
        print(key+":")
        print VHDictionary[key].Integral()
        print ''
    
