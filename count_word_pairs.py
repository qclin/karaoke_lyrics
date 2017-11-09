import sys

# as dict w/ tuples as keys, integers as value
pairs = dict()

for line in sys.stdin:
    # strip line, break into words
    line = line.strip()
    words = line.split(" ")

    if len(words) < 2:
        continue
    ## iterate to end of list
    for i in range(len(words) - 1):
        pair = tuple(words[i: i+2])
        if pair in pairs:
            pairs[pair] +=1
        else:
            pairs[pair] = 1

for pair in pairs.keys():
    count = pairs[pair]
    if count > 4: # only print pairs that occur frequent
        print ' '.join(pair) + ': ' + str(count)
