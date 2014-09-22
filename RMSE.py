# get prediction given mvId, userID
# mvID and userID are strs
def getPredictRating(mvID,userID):
    cacheList = os.listdir(/u/prat0318/netflix-tests/)
    cacheMovie = cacheList[...]
    cacheUser = cacheList[...]
    # find the movie ID
    for line in cacheMovie:
        stList = line.split()
        if (stList[0] == mvID):
            mvRating = int(stList[1]) # make it to be int
            break
    for line in cacheUser:
        stList = line.split()
        if (stList[0] == userID):
            userRating = int(stList[1]) # make it to be int
            break
    #take ave as the prediction
    aveRating = (mvRating + userRating) / 2
    return aveRating

# get realRating given mvID,userID from the training set
def getRealRating(targetMVID,targetUserID):
    listOfFiles = os.listdir(/u/downing/cs/netflix/training_set/)
    for i in listOfFiles:
        found = False
        if (found):
            break
        inFile = open('/u/downing/cs/netflix/training_set/' + i,'r')
        firstLine = inFile.readline()
        mvID = firstLine[:-1] # return a str
        
        if (mvID == targetMVID):
            listOfUserRating = inFile.readlines() # each entry is a string
            for item in listOfUserRating:
                listOfEachUser = item.split(',')
                userID = listOfEachUser[0]
                if (userID == targetUserID):
                    realRating = listOfEachUser[1]
                    found = True
                    break

# get realRating given mvID,userID from the cache
#def getRealRating(targetMVID,targetUserID):




