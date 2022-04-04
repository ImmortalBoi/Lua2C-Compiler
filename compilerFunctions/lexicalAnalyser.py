from ast import operator
from externalFunctions.usefulFunctions import removeEmptyLines
from externalFunctions.usefulFunctions import checkEmptyLine


KEYWORDS = {   
    "do":"STAT"    ,"end":"STAT"      ,"while":"STAT"    ,"repeat":"STAT"   ,"until":"STAT"
    ,"if":"STAT"   ,"then":"STAT"     ,"elseif":"STAT"   ,"else":"STAT"     ,"for":"STAT"
    ,"in":"STAT"   ,"function":"STAT" ,"local":"STAT",
    
    "return":"LASTSTAT"     ,"break":"LASTSTAT",
    
    "nil":"EXP"   ,"false":"EXP"    ,"true":"EXP",
    
    ":":"FIELDSEP"    ,",":"FIELDSEP",
    
    "(":"OPERATORS"     ,")":"OPERATORS"     ,"{":"OPERATORS"     ,"}":"OPERATORS"    ,"[":"OPERATORS"    
    ,"]":"OPERATORS"    ,";":"OPERATORS"    ,".":"OPERATORS"    ,"..":"OPERATORS"   ,"...":"OPERATORS",

    
    "+":"BINOP"     ,"*":"BINOP"    ,"/":"BINOP"    ,"%":"BINOP"    ,"^":"BINOP"
    ,"==":"BINOP"   ,"~=":"BINOP"   ,"<=":"BINOP"   ,">=":"BINOP"   ,"<":"BINOP"
    ,">":"BINOP"    ,"=":"BINOP"    ,"and":"BINOP"  ,"or":"BINOP",
    
    '-':"UNOP"     ,'#':"UNOP"    ,"not":"UNOP"
}
STAT = [
    "do"    ,"end"      ,"while"    ,"repeat"   ,"until"
    ,"if"   ,"then"     ,"elseif"   ,"else"     ,"for"
    ,"in"   ,"function" ,"local"
]

LASTSTAT = [
    "return","break"
]

EXP = [
    "nil"   ,"false"    ,"true"
]

FIELDSEP = [
    ":"     ,","
]

OPERATORS = [
    "("     ,")"    ,"{"    ,"}"    ,"["    
    ,"]"    ,";"    ,"."    ,".."   ,"..."
    ,'"'    ,"'"
    
]

BINOP = [
    "+"     ,"*"    ,"/"    ,"%"
    ,"^"    ,"=="   ,"~="   ,"<="
    ,">="   ,"<"    ,">"    ,"="    ,"and"
    ,"or"
]

UNOP = [
    '-'     ,'#'    ,"not"
]

class Token:
    def __init__(self, line:int, startingPosition:int, inputSpecification:str, innerText:str) -> None:
        self.line = line
        self.startingPosition = startingPosition
        self.inputSpecification = inputSpecification
        self.innerText = innerText
    def clearText(self):                             #this helps clear the words from tabs and whitespaces -- done
        if(' ' in self.innerText):
            self.innerText = self.innerText.replace(' ','')
        if('\t' in self.innerText):
            self.innerText = self.innerText.replace('\t','')
    def __repr__(self) -> str:
        return "\t" + str(self.line) + "\t" + str(self.startingPosition) + "\t" + str(self.inputSpecification) + "\t" + "||||"+str(self.innerText) +"||||"+"\n"
        
def lexicalAnalysis(allLines:list[str])->list[Token]:
    tokenList:list[Token] = []
    testObject:Token
    for index,line in enumerate(allLines):
        word:str = ''
        for i in range(len(line)):
            if (line[i] in OPERATORS or line[i] in BINOP or line[i] in FIELDSEP or line[i] == ' ' or word in OPERATORS or word in BINOP):
                testObject = Token(index+1, i - len(word), findTokenSpecification(word), word)
                testObject.clearText()
                if(testObject.innerText != ''):                 #stops creating empty objects -- Done
                    tokenList.append(testObject)
                word = line[i]
            word = word + line[i]
    return tokenList

def findTokenSpecification(tokenToBeFound:str)->str:            #this needs to be fixed (does not work) -- Done
    if (' ' in tokenToBeFound):
       tokenToBeFound = tokenToBeFound.replace(' ', '')
    if ('\t' in tokenToBeFound):
        tokenToBeFound = tokenToBeFound.replace('\t', '')
    if(tokenToBeFound in KEYWORDS):
        return KEYWORDS[tokenToBeFound]
    return "Identifier"
