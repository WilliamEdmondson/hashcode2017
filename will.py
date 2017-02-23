#
#
import numpy

# Read from test file
fname = "tests/me_at_the_zoo.txt"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

line0 = content[0].split()

numVids = line0[0]
numEndpts = line0[1]
numReqs = line0[2]
numCache = line0[3]
cacheSize = line0[4]

print ("V = ", numVids,", E = ",numEndpts,", R = ",numReqs,", #Caches = ",numCache,", CacheSize = ",cacheSize)

# Array of vid sizes
videoSizes = content[1].split()

#####

# line 2
lineIndex = 2
currEndpt = 0

# storage variables
# endptLatencyArr = [[DB,[C1,C2,C3]],[DB,[C1,C2,C3]]
endptLatencyArr = []

# loop endpts
numEndpts = int(numEndpts);
for j in range(0, numEndpts):
    endptContent = content[lineIndex].split()
    # datacenter latency
    endptLatencyArr.append([endptContent[0]])
    cacheLatTempArr = []
    endptContent[1] = int(endptContent[1])
    for i in range(lineIndex, lineIndex + endptContent[1]):
        lineIndex += 1
        cacheContent = content[lineIndex].split()
        cacheLatTempArr.append([cacheContent[0],cacheContent[1]])
    endptLatencyArr[currEndpt].append(cacheLatTempArr)
    currEndpt += 1
    lineIndex += 1
# print (endptLatencyArr)

####### Requests

requestsByEndpoint = []
for i in range(0, numEndpts):
    requestsByEndpoint.append([])
#print (requestsByEndpoint)


numReqs = int(numReqs)
for i in range(lineIndex, lineIndex + numReqs-1):
    lineIndex += 1
    reqContent = content[lineIndex].split()
    vidId = int(reqContent[0])
    numReq = int(reqContent[2])
    endptId = int(reqContent[1])
    size = int(videoSizes[vidId])
    reqArr = [vidId, numReq, size]
    requestsByEndpoint[endptId-1].append(reqArr)
# print (requestsByEndpoint)

# cache latencies

endptCachesLatencyArr = []
for i in range(0,numEndpts):
    cacheLatenciesArr = []
    databaseLat = endptLatencyArr[i][0]
    cacheLats = endptLatencyArr[i][1]
    for j in range(0, len(cacheLats)-1):
        temp = int(databaseLat) - int(cacheLats[j][1])
        cacheLatenciesArr.append([cacheLats[j][0],temp])
        endptCachesLatencyArr.append(cacheLatenciesArr)
print (endptCachesLatencyArr)
