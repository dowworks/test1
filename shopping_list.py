shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

food = shopping_list;
# function fruit sales
def compute_bill(food): 
    total = 0
    for x in food:
        if stock[x] > 0:
            total += prices[x] 
            stock[x] -= 1
    return total


    result = compute_bill(shopping_list)
    print 'the result of compute_bill(shopping_list) is', result
