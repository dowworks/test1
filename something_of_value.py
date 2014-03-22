prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

totalcost = 0
for i in stock and prices:
    totalcost = totalcost + (prices[i]*stock[i])
    
print totalcost

# push to gerrithub
# test with gerrit
# after mirror
