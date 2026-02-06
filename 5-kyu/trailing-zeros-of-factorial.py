import math

def zeros(n):
    if n == 0:
        return 0
    
    # per Wolfram: https://mathworld.wolfram.com/Factorial.html
    k_max = math.floor(math.log(n, 5))
    Z_sum = 0
    
    for k in range(1, k_max + 1):
        Z_sum += math.floor(n / (5 ** k))
    return Z_sum

print(zeros(12))
    
    