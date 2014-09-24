import timeit
import rmse
start = timeit.timeit()
import sys
from Netflix import netflixEval
if __name__ == '__main__':
    rmse.main()
netflixEval(sys.stdin,sys.stdout)
end = timeit.timeit()
print (str(start - end))