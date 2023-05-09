import itertools

def get_strings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

# 0/1 bruteforce
def bruteForceKnapSack_01(p,w,m):
    assert len(p) == len(w), "p and w are of different length"
    n = len(p)
    bit_strings = get_strings(n)
    solution = []

    for s in bit_strings:
        profit = sum((int(s[i]) * p[i]) for i in range(n))
        weight = sum((int(s[i]) * w[i]) for i in range(n))
        if weight<=m:
            solution.append(profit)

    return max(solution)



# fractional bruteforce
def bruteForceKnapSack_Frac(p,w,m):
    assert len(p) == len(w), "p and w are of different length"
    n = len(p)
    max_profit = 0
    fractions = []

    # fraction of items with multiple 0.1
    for i in range(n):
        fractions.append([0] + [round(j / 10, 1) for j in range(1, 11)])
    
    # all possible combinations of fractions
    combinations = itertools.product(*fractions)
    for combination in combinations:
        total_profit = 0
        total_weight = 0
        for i in range(n):
            total_profit += combination[i] * p[i]
            total_weight += combination[i] * w[i]
        if total_weight <= m and total_profit > max_profit:
            max_profit = total_profit

    return max_profit



# fractional greedy
def greedyKnapSack_Frac(p,w,m):
    assert len(p) == len(w), "p and w are of different length"
    n = len(p)
    
    # sorting profit, weight and profit_by_weight list in descending order wrt profit_by_weight 
    pbyw = [p[i]/w[i] for i in range(n)]
    p = [x for _, x in sorted(zip(pbyw,p),reverse=True)]
    w = [x for _, x in sorted(zip(pbyw,w),reverse=True)]
    pbyw.sort(reverse = True)
    
    remaining_weight = m
    total_profit = 0
    
    for i in range(n):
        if (w[i] <= remaining_weight):
            total_profit += p[i]
            remaining_weight -= w[i]
        else: 
            total_profit += pbyw[i] * remaining_weight        

    return total_profit
    


