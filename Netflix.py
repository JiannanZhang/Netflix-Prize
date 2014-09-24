import json

# get prediction given mvId, userID
# mvID and userID are strs
def getPredictRating(mvID,userID):
    #cacheList = os.listdir(/u/prat0318/netflix-tests/)
    # caches are dics
    #movieCache = open(os.listdir(/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt))
    movieCacheDic = json.load(open('/u/prat0318/netflix-tests/ctd446-movieAverageRating.txt','r'))

    userCacheDic = json.load(open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt','r'))

    AveAllUsers = getAveAllUsers(userCacheDic)
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
            w.write(line)
        # record id and then loop each user
        else:
            userIDEval = line
            predictRat = getPredictRating(mvIDEval,userIDEval)
            w.write(str(predictRat))



# plan2 find the offsets for movies and users
# two offsets one is for movie the other is for user
# for the movie
# movieOff = aveMovieRat - aveAllUserating

# first find the averating for all users
def getAveAllUsers(userCacheDic):
    sumRating = 0
    length = len(userCacheDic)
    for key in userCacheDic:
        sumRating += float(userCacheDic[key])
    return sumRating / length
    '''
    times = 0
    for line in cacheUserFile:
        stList = line.split()
        times += 1
        sumRating += stList[1]
    return sumRating / times
    '''






































