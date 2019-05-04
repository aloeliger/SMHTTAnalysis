import ROOT
import configparser
from array import array

class AnalysisCategory():
    def __init__(self,ConfigurationFileName):
        self.Configuration = configparser.ConfigParser()
        self.Configuration.optionxform = str
        self.Configuration.read(ConfigurationFileName)
        self.Name = ''
        self.DefinitionDictionary = {}
        self.ReconstructionVar = ''
        self.ReconstructionBins = []
        self.nReconstructionBins = 0.0
        self.RollingVar = ''
        self.RollingBins = []
        self.nRollingBins = 0.0
        for Token in self.Configuration:
            for Element in self.Configuration[Token]:
                #start setting things up?
                if Token == 'META':
                    if Element == 'name':
                        self.Name = self.Configuration[Token][Element]
                    if Element == 'reconstruction':
                        self.ReconstructionVar = self.Configuration[Token][Element]                        
                    if Element == 'recobins':
                        recobinstring = self.Configuration[Token][Element]
                        stringList = recobinstring.split(",")
                        for x in stringList:
                            self.ReconstructionBins.append(float(x))
                            self.nReconstructionBins = len(self.ReconstructionBins)-1
                    if Element == 'rolling':
                        self.RollingVar = self.Configuration[Token][Element]
                    if Element == 'rollbins':
                        rollbinstring = self.Configuration[Token][Element]
                        stringList = rollbinstring.split(",")
                        for x in stringList:
                            self.RollingBins.append(float(x))
                            self.nRollingBins = len(self.RollingBins)-1
                if Token == 'DEF':
                    self.DefinitionDictionary[Element] = self.Configuration[Token][Element]      
        assert self.Name != '', "No category name!"
        assert self.ReconstructionVar != '', "No reconstruction variable for category "+self.Name
        assert self.ReconstructionBins != [], "No reconstruction bins for category "+self.Name
        assert self.RollingVar != '', "No rolling variable for category "+self.Name
        assert self.RollingBins != [], "No rolling bins for category "+self.Name
                    
    def CheckEventInCategory(self,EventDictionary):
        FallsIntoCategory = True        
        for Key in self.DefinitionDictionary:
            DefinitionTokens = self.DefinitionDictionary[Key].split()
            try:
                DefinitionTokens[0],DefinitionTokens[1],DefinitionTokens[2]
            except:
                print("Was expecting at least 3 tokens to create a valid definition:")
                print(DefinitionDictionary[Key])
                raise RuntimeError()            
            
            if not self.ParseTokens(DefinitionTokens,EventDictionary):                
                FallsIntoCategory = False                                            
        return FallsIntoCategory

    def ParseTokens(self,DefinitionTokens,EventDictionary):        
        try:
            DefinitionTokens[0],DefinitionTokens[1],DefinitionTokens[2]
        except:
            print("Was expecting at least 3 tokens to create a valid definition:")
            print(DefinitionDictionary[Key])
            raise RuntimeError()                              

        if not self.CheckForSubTokens(DefinitionTokens):
            if DefinitionTokens[1] == '<':
                if float(EventDictionary[DefinitionTokens[0]]) >= float(DefinitionTokens[2]):                    
                    return False                
                return True
            elif DefinitionTokens[1] == '>':
                if float(EventDictionary[DefinitionTokens[0]]) <= float(DefinitionTokens[2]):
                    return False
                return True
            elif DefinitionTokens[1] == '=':
                if float(EventDictionary[DefinitionTokens[0]]) != float(DefinitionTokens[2]):
                    return False
                return True
            elif DefinitionTokens[1] == '<=':
                if float(EventDictionary[DefinitionTokens[0]]) > float(DefinitionTokens[2]):
                    return False
                return True
            elif DefinitionTokens[1] == '>=':
                if float(EventDictionary[DefinitionTokens[0]]) < float(DefinitionTokens[2]):
                    return False
                return True
        else:
            SubClauseLocation = self.FindFirstSubClause(DefinitionTokens)
            if DefinitionTokens[SubClauseLocation] == '!':
                assert DefinitionTokens[SubClauseLocation+1] == '(',"No parenthesized statement for \'not\' to act on!"
                #now we just return the not of the parenthesized clause to the right
                CloseParenLocation = self.FindClosingParen(DefinitionTokens[SubClauseLocation+2:])
                return not self.ParseTokens(DefinitionTokens[SubClauseLocation+2:SubClauseLocation+1+CloseParenLocation])

            elif DefinitionTokens[SubClauseLocation] == '(':
                #okay, first thing we do, is have to look for it's closing paren.
                CloseParenLocation = self.FindClosingParen(DefinitionTokens[SubClauseLocation+1:])
                return self.ParseTokens(DefinitionTokens[SubClauseLocation+1:SubClauseLocation+CloseParenLocation+1],EventDictionary)

            elif DefinitionTokens[SubClauseLocation] == 'and':
                return (self.ParseTokens(DefinitionTokens[:SubClauseLocation],EventDictionary) and self.ParseTokens(DefinitionTokens[SubClauseLocation+1:],EventDictionary))
            elif DefinitionTokens[SubClauseLocation] == 'or':
                return (self.ParseTokens(DefinitionTokens[:SubClauseLocation],EventDictionary) or self.ParseTokens(DefinitionTokens[SubClauseLocation+1:],EventDictionary))
            elif DefinitionTokens[SubClauseLocation] == ')':
                raise RuntimeError("Unmatched closing paren in category definition!")

    def CheckForSubTokens(self,DefinitionTokens):
        Subtokens = ['!','(',')','and','or']
        for Token in Subtokens:
            if Token in DefinitionTokens:
                return True
        return False
    
    def FindFirstSubClause(self,DefinitionTokens):
        Subtokens = ['!','(',')','and','or']
        for i in range(len(DefinitionTokens)):
            if DefinitionTokens[i] in Subtokens:
                return i
        raise RunTimeError('Failed to find denoted subclause where there should be one!')

    def FindClosingParen(self,DefinitionTokens):
        #assume we just got everything to the right of the opening paren
        #we just march down the tokens looking for a closing paren, and the instant we find it, let's return its location
        OpenParens = 1
        for i in range(len(DefinitionTokens)):
            if DefinitionTokens[i] == '(':
                OpenParens += 1
            elif DefinitionTokens[i] == ')':
                OpenParens -= 1
            if OpenParens == 0:
                return i
        raise RunTimeError('No closing paren in category definition clause!')
            
            
        
