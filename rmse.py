from Netflix import getPredictRating
#import timeit
rrText = open("/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt","r") #contains the movies, and all the real ratings each user gave for the movies

def createCache():
    realRatDic = {}
    for line in rrText:
        lineList = line.split() #[4447,121331,2]
        valueList = []
        sublist = []    #will contain the userID and the rating (convert to interger) given
        sublist.append(lineList[1])
        sublist.append(int(lineList[2]))
        if lineList[0] not in realRatDic:   #movie not yet in cache, so add the movieID as a new key and append the user and rating
            valueList.append(sublist)
            realRatDic[lineList[0]] = valueList
        else:
            realRatDic[lineList[0]].append(sublist) #movie key already exists in cache, just add another user and rating
    return realRatDic



def getRealRating(movieID,userID): #returns the rating when given a specific user and movie ID. Reach into the cache
    #userAndRating =  realRatDic[movieID]
    realRatDic = createCache
    movieSublist = realRatDic.get(movieID, default = None) #this variable is the 2D list containing one movie, and all the users and each of their ratings
    for i in movieSublist:     #Go through each sublist
        if (movieSublist[i][0] == userID):    #find the sublist that contains the specific user
            return movieSublist[i][1]      #return that user's rating
            
            
            
            
#get a from the rmse.py file where you can get a user's movie real rating.
#get p from the netflixEval function above where you made a file with all the predicted ratings (  STILL NOT SURE ABOUT THISSS?!?!?!?!)

def rmse(a,p):  #when running the code, will import this file / function and input values a and p for the final output to be printed somewhere else. Need to direct
    total = 0
    z = zip(a,p)
    for x,y in z:
        total += (float(x)-float(y))**2
    rmse = (total / len(a))  ** 0.5
    return rmse

def main():
    #start = timeit.timeit()
    aRList = []
    pRlist = []
    for line in rrText:
        lineList = line.split()
        aRList.append(lineList[2])  #gets actual rating
    #find specific movie and user to get specific predicted rating
        movieID = lineList[0]
        userID = lineList[1]
        pRlist.append(getPredictRating(movieID,userID))
    RMSE = rmse(aRList,pRlist)
    #end = timeit.timeit()
    print(RMSE)

if __name__ == '__main__':        
    main()
        


    
