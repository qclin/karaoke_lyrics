import sys

# Step 1: find and count word pair
pairs = list()
for line in sys.stdin:
    # strip line, break into words
    line = line.strip()
    words = line.split(" ")

    if len(words) < 2:
        continue
    ## iterate to end of list
    for i in range(len(words) - 1):
        pair = words[i: i+2]
        pairs.append(pair)

for pair in pairs:
    print ' '.join(pair)
