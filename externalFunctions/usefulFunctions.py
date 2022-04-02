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
            allLines[iterator] = allLines[iterator][isThereBlockCommentEnd:]
            commentBlockFlag = 0
            
        if(blockCommentFlag == 1):
            allLines[iterator] = ""            
            
        # Finding the quotations quotations
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