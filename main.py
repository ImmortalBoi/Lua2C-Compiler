from externalFunctions.usefulFunctions import commentRemover
from externalFunctions.usefulFunctions import removeEmptyLines

#Some string manipulation to remove unnecessary chars
allLines:list[str] = []
with(open("./IOfiles/input.lua",'r')) as f:
    allLines = f.readlines()    
allLines = removeEmptyLines(commentRemover(allLines))
for i in allLines:
    print(i)
