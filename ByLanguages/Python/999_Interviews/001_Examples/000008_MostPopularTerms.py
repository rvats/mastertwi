"""
You are working on finding the most popular terms from a given list in your feedback. You have been given 5 parameters
numberOfTerms, topTerms, requestedTerms, numberOfFeedback, feedbackList
6, 2, ["slim","battery","storage","test","light","solar"], 8, ["Slim battery with more storage test is awesome", "powerfull battery with light", "Strong BATTERY", "SOLAR BATTERY", "Slim battery with more storage test is awesome", "powerfull battery with light", "TEST BATTERY", "SOLAR BATTERY"]
0,0,None,0,[" "]
"""


def mostPopularTerm(numberOfTerms,topTerms,requestedTerms,numberOfFeedback,feedbackList):
    dictionaryTermCount = {}
    
    if not requestedTerms:
        return ["No Requested Terms"]
    if not feedbackList:
        return ["No Feedback List"]
        
    requestedTerms=[x.lower() for x in requestedTerms]
    feedbackList=[x.lower() for x in feedbackList]
    
    for Term in requestedTerms:
        dictionaryTermCount[Term]=0
    
    for feedback in feedbackList:
        for term in requestedTerms:
            if term in feedback:
                dictionaryTermCount[term]+=1
    
    temp = sorted(dictionaryTermCount.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for i in range(topTerms):
        result.append(temp[i][0])
    
    return result

result = mostPopularTerm(6,4,["slim","battery","storage","test","light","solar"],8,["Slim battery with more storage test is awesome", "powerfull battery with light", "Strong BATTERY", "SOLAR BATTERY", "Slim battery with more storage test is awesome", "powerfull battery with light", "TEST BATTERY", "SOLAR BATTERY"])
print (result)
result = mostPopularTerm(0,0,None,0,[" "])
print (result)
result = mostPopularTerm(0,1,[" "],0,None)
print (result)