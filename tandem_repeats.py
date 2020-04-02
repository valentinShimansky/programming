import sys
path = sys.stdin

with open(path, 'r') as inf:
    for s in inf:
        if '#' not in s:
            s = s.strip().split()
            if (len(s[3]) >= 4 or len(s[4]) >= 4) and (s[3] != s[4]):
                print (s[0], '\t', s[3], '\t', s[4])