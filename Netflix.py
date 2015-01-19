import json
# get prediction given mvId, userID
# mvID and userID are strs
userCacheDic = json.load(open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt','r'))
movieCacheDic = json.load(open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt','r'))

def getAveAllUsers(userCacheDic):
    sumRating = 0
    length = len(userCacheDic)
    for key in userCacheDic:
        sumRating += float(userCacheDic[key])
    return sumRating / length
# get global aveRat for all users : 3.6741013034524457
AveAllUsers = getAveAllUsers(userCacheDic)

def getPredictRating(mvID,userID):
    # movieOff and userOff
    movieOff = float(movieCacheDic[mvID]) - AveAllUsers
    userOff = float(userCacheDic[userID]) - AveAllUsers

    predictRat = AveAllUsers + movieOff + userOff

    return predictRat


#plan 2
def netflixEval(r,w):
    mvIDEval = 0
    for line in r:
        line = line.strip('\n')
        # first check it is not : in order to go to else clasue to record the id
        if (line[-1] == ':'):
            mvIDEval = line[:-1]
            w.write(line + '\n')
        # record id and then loop each user
        else:
            userIDEval = line
            predictRat = getPredictRating(mvIDEval,userIDEval)
            w.write(str("%.1f" % predictRat) + '\n')

    # the code below is to find the rmse
    # 1 fist the realRatDic
    realRatDic = {}
    rrText = open("/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt","r") #contains the movies, and all the real ratings each user gave for the movies
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

    # creat two lists one is actural the other is predict
    # remember to open it again !!!!!!! otherwise list wil be empty
    rrText.close()
    rrText = open("/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt","r")
    aRList = []
    pRlist = []
    for line in rrText:
        lineList = line.split()
        aRList.append(lineList[2])  #gets actual rating
    #find specific movie and user to get specific predicted rating
        movieID = lineList[0]
        userID = lineList[1]
        pRlist.append(getPredictRating(movieID,userID))
    total = 0
    z = zip(aRList,pRlist)
    # calc rmse
    for x,y in z:
        total += (float(x)-float(y))**2
    rmse = (total / len(aRList))  ** 0.5
    return rmse













































































