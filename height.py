
def sortHeight(m):
    new_array = sorted([x for x in m if x != -1 ]) 
    j = 0
    for i in m: 
        if m[i] != -1:
            m[i] = new_array[j]
            j += 1
    return m