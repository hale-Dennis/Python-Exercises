from collections import Counter

def commonCharacterSum(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    add = 0
    checked = set()
    for c in s1:
        if c in c2 and c not in checked: 
            add = c2[c] if c1[c] > c2[c] else c1[c]
            checked.add(c)
    return add
