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

def lexicalAnalysis():
    return