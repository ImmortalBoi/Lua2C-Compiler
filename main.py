from externalFunctions.usefulFunctions import commentRemover
from externalFunctions.usefulFunctions import removeEmptyLines

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

#Some string manipulation to remove unnecessary chars
allLines:list[str] = []
with(open("./IOfiles/input.lua",'r')) as f:
    allLines = f.readlines()    
allLines = removeEmptyLines(commentRemover(allLines))
for i in allLines:
    print(i)
