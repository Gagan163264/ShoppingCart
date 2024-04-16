import sys
prefix = r'D:\RandomBS\ShoppingCart\\'
path = prefix + 'cart.txt'

if len(sys.argv) > 1:
    path = prefix+sys.argv[1]

with open(path, 'r') as file:
    cart = file.read().splitlines()

whopay = {}

for item in cart:
    if item != '':
        pay, item, price = item.split('-')
        pay = list(pay)
        if price.isupper() or price.islower() or price.isspace() or price == '':
            print('Invalid price:', price)
            exit()
        cost = eval(price) / len(pay)

        for person in pay:
            if person not in whopay:
                whopay[person] = []
            whopay[person].append([item, cost, price])

print("Total amount:", sum([x[1] for person, cost in whopay.items() for x in cost]))

for person, cost in whopay.items():
    print(person, 'owes', sum([x[1] for x in cost]))

for person, cost in whopay.items():
    print(person)
    for item, cost, price in cost:
        print(f'  {item} - {cost:.2f} ({price})')    
