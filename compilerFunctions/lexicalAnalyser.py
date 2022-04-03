from ast import operator

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
    
]

BINOP = [
    "+"     ,"-"    ,"*"    ,"/"    ,"%"
    ,"^"    ,"#"    ,"=="   ,"~="   ,"<="
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
    def __repr__(self) -> str:
        return "\t" + str(self.line) + "\t" + str(self.startingPosition) + "\t" + str(self.inputSpecification) + "\t" + "||||"+str(self.innerText) +"||||"+"\n"
        
def lexicalAnalysis(allLines:list[str])->list[Token]:
    tokenList:list[Token] = []    
    for index,line in enumerate(allLines):
        word:str = ''
        for i in range(len(line)):
            if (line[i] in OPERATORS or line[i] in BINOP or line[i] == ' '):
                tokenList.append(Token(index,i-len(word),findTokenSpecification(word),word))
                word = line[i]
                continue
            word = word + line[i]
    return tokenList

def findTokenSpecification(tokenToBeFound:str)->str:
    if(tokenToBeFound in KEYWORDS):
        return KEYWORDS[tokenToBeFound]
    return "Identifier"