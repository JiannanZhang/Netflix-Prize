import sys
from Netflix import netflixEval
rmse = netflixEval(sys.stdin,sys.stdout)
print("RMSE: " + str('%.2f' % rmse))
