def main():
    inFile = open('/u/downing/cs/netflix/probe.txt','r')
    outFile = open('RunNetflix.in.txt','w')
    for i in range (1000):
        line = inFile.readline()
        print(line,file = outFile,end = '')

main()
