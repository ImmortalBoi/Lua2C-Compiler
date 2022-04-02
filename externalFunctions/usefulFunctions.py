def findAllOccurenceChar(characterSearch:str,stringSearched:str):
    isThereChar = stringSearched.count(characterSearch)
    if(isThereChar == 0):
        return []
    
    stringLiteralPositions : list[int] = []
    previousOccurence = -1
    for i in range(isThereChar):
        stringLiteralPositions.append(stringSearched.find(characterSearch,previousOccurence+1))
        previousOccurence = stringLiteralPositions[i]
    return stringLiteralPositions

def commentRemover(allLines:list[str]) -> list[str]:
    
    stringLiteralFlag = 0
    inlineCommentFlag = 0
    blockCommentFlag = 0
    
    for iterator,line in enumerate(allLines):
        
        isThereBlockCommentEnd = line.find(']]')
        if(isThereBlockCommentEnd != -1):
            allLines[iterator] = allLines[iterator][isThereBlockCommentEnd+2:]
            blockCommentFlag = 0
            
        if(blockCommentFlag == 1):
            allLines[iterator] = ""            
            
        # Finding the quotations 
        allStringLiterals = findAllOccurenceChar('\"',line)
        
        isThereBlockComment = line.find('--[[')
        if(isThereBlockComment != -1):
            blockCommentFlag = 1
        
        
        # Finding if there is a comment or not
        isThereComment = line.find('--')
        if(isThereComment == -1):
            continue
        else:
            inlineCommentFlag = 1
        
        
        if(allStringLiterals != []):
            for i in range(0,len(allStringLiterals),2):
                if (isThereComment > allStringLiterals[i] and isThereComment < allStringLiterals[i+1]):
                    inlineCommentFlag = 0
                    continue
                elif (isThereBlockComment > allStringLiterals[i] and isThereBlockComment < allStringLiterals[i+1]):
                    blockCommentFlag = 0
        
        if(isThereBlockComment != -1):
            allLines[iterator] = allLines[iterator][:isThereBlockComment]
        
        allLines[iterator] = allLines[iterator][:isThereComment]
    
    return allLines

#Removing all the lines with no text in them
def removeEmptyLines(allLines:list[str])->list[str]:
    newAllLines = list(filter(checkEmptyLine,allLines))
    return newAllLines
#Function to filter out lines that only have certain characters
def checkEmptyLine(line:str)->bool:
    for i in range(len(line)):
        #A changeable filter if necessary
        if(line[i] != '\n' and line[i] != ' ' and line[i] !='\t'):
            return True
    return False