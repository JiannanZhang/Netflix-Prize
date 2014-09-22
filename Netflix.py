import jason
# get prediction given mvId, userID
# mvID and userID are strs
def getPredictRating(mvID,userID):
    #cacheList = os.listdir(/u/prat0318/netflix-tests/)
    # caches are dics
    movieCache = open(os.listdir(/u/prat0318/netflix-tests/mjh3664movie.txt))
    movieCacheDic = json.load(open('cacheMovie','r'))

    cacheUser = open(os.listdir(/u/prat0318/netflix-tests/savant-cacheUsers.txt))
    userCacheFile = open('os.listdir(/u/prat0318/netflix-tests/savant-cacheUsers.txt)','r')
    userCacheDic = {}
    for line in inFile:
        line = line.split()
        userCacheDic[line[0]] = line[1]

    AveAllUsers = getAveAllUsers(userCacheFile)
    # movieOff and userOff
    movieOff = movieCacheDic[mvID] - AveAllUsers
    userOff = userCacheDic[userID] - AveAllUsers

    predictRat = AveAllUsers + movieOff + userOff



#plan 1
def netflixEval(r,w):
    for line in r:
        # first check it is not : in order to go to else clasue to record the id
        if (line[-1] != ':'):
            predictRat = getPredictRating(mvID,line)
            w.write(predictRat)
        # record id and then loop each user
        else:
            mvID = line[:-1]
            w.write(line)



# plan2 find the offsets for movies and users
# two offsets one is for movie the other is for user
# for the movie
# movieOff = aveMovieRat - aveAllUserating

# first find the averating for all users
def getAveAllUsers(cacheUserFile):
    sumRating = 0
    times = 0
    for line in cacheUserFile:
        stList = line.split()
        times += 1
        sumRating += stList[1]
    return sumRating / times





































