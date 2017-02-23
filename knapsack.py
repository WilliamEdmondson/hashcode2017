try:
    xrange
except:
    xrange = range

def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)

# ("item", weight, value)
# video, videoSize, savedLatency
# savedLatency = numRequests * latencySavedPerServer

# list of videos
# how do we identify the savedLatency per video?
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10)
    )

itemslist = []
for item in items:
    itemslist.append(list(item))
print itemslist
items = itemslist

#items = list(items)
print "items should be list"
print "-------------"

print items

# items is list of vids
# limit is size limit per cache
def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result

# cacheservers
# sacks
# has a number, limit and a latency
#sacks = [{"sacknumber": 1, "limit": 20, "latency": 100},
#        {"sacknumber": 2, "limit": 100, "latency": 200},
#        {"sacknumber": 3, "limit": 50, "latency": 300} ]

# number, limit, latency
#sacks = [100], [2, 100, 200], [3, 50, 300]]

# --------------------
# IMPORTANT VARS
cacheSize = 100
numOfServers = 3
# --------------------


# will want to do a knapsack for each cache server
# items = videos
def multiSack(items, limit):
    result = []

    for i in range(numOfServers):
        #print sack.get("limit")
        print "Working on server " + str(i)
        print
        currentsackresult = knapsack01_dp(items, limit)
        for item in currentsackresult:
            print "Removing "+ str(item)
            items.remove(item)

        result += currentsackresult
        # for item in items:
        #     if item in result:
        #         print "removing " + str(item)
        #         items.remove(item)
        # #for item in result:

        #    items.remove(item)
        print "----------"




    return result

# will this have duplicate items?
bagged = multiSack(items, cacheSize)


#bagged = knapsack01_dp(items, 400)
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))


# [[[cacheId, latencyImprovement],[cacheId, latencyImprovement]], [[cacheId, latencyImprovement],[cacheId, latencyImprovement]]  ]
