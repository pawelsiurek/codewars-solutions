def count(s):
    if len(s) == 0:
        return {}
    
    frequencies = {} # linear solution
    for ch in s:
        if ch not in frequencies:
            frequencies[ch] = 1
        else:
            frequencies[ch] += 1
    return frequencies

print(count("sadpigjsiafgadsasfdsa"))