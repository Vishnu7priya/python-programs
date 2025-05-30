def coinchange_greedy(amount):
    coins = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []
    
    for c in coins:
        while amount >= c:
            amount -= c
            result.append(c)
    return result

amount = 11
change = coinchange_greedy(amount)
print(len(change))
print(change)



