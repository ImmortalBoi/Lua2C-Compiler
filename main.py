from externalFunctions.usefulFunctions import commentRemover
KEYWORDS = [
    "and"       ,"break"     ,"do"        ,"else"      ,"elseif"
    "end"       ,"false"     ,"for"       ,"function"  ,"if"
    "in"        ,"local"     ,"nil"       ,"not"       ,"or"
    "repeat"    ,"return"    ,"then"      ,"true"      ,"until"     ,"while"
]

OPERATORS = [
    "+"     ,"-"     ,"*"     ,"/"     ,"%"     ,"^"     ,"#"
    "=="    ,"~="    ,"<="    ,">="    ,"<"     ,">"     ,"="
    "("     ,")"     ,"{"     ,"}"     ,"["     ,"]"
    ";"     ,":"     ,","     ,"."     ,".."    ,"..."  
]

allLines:list[str] = []
with(open("./IOfiles/input.lua",'r')) as f:
    allLines = f.readlines()
    
for i in commentRemover(allLines):
    print(i)