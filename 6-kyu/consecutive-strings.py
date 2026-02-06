def longest_consec(strarr, k):
    max_length = float('-inf')
    max_length_str = ""
    
    for i in range(len(strarr) - k + 1):
        current_str = ""
        for j in range(i, i + k):
            current_str += strarr[j]
        
        if len(current_str) > max_length:
            max_length = len(current_str)
            max_length_str = current_str
    
    return max_length_str

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
    
    