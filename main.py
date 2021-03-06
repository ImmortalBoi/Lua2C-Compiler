from externalFunctions.usefulFunctions import commentRemover
from externalFunctions.usefulFunctions import removeEmptyLines
from compilerFunctions.lexicalAnalyser import lexicalAnalysis
from compilerFunctions.syntaxAnalyser import syntaxAnalysis,terminal

#Some string manipulation to remove unnecessary chars
allLines:list[str] = []
with(open("./IOfiles/input.lua",'r')) as f:
    allLines = f.readlines()    
allLines = removeEmptyLines(commentRemover(allLines))
print(lexicalAnalysis(allLines))
syntaxAnalysis(terminal)