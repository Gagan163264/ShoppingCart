import sys
prefix = r'D:\RandomBS\ShoppingCart\\'
path = prefix + 'cart.txt'

if len(sys.argv) > 1:
    path = prefix+sys.argv[1]

with open(path, 'r') as file:
    cart = file.read().splitlines()

try:
    person_count = int(cart[0])
except:
    print("Invalid number of people:", cart[0])
    exit()
cart = cart[1:]
print("Number of people:", person_count)

discount = ()
if cart[0].endswith('%'):
    conv_fee, discount_item = cart[0].split('-')
    discount = ('%', eval(discount_item[:-1])/100, eval(conv_fee))
    print('Percentage discount:', discount[1])
    cart = cart[1:]
elif cart[0].endswith('#') or cart[0].endswith('$'):
    discount = ("#", eval(cart[0][:-1]))
    print('Discount:', discount[1])
    print("Discount per person:", discount[1]/person_count)
    cart = cart[1:]

    

whopay = {}
for item in cart:
    if item != '':
        pay, item, price = item.split('-')
        pay = list(pay)
        if price.isupper() or price.islower() or price.isspace() or price == '':
            print('Invalid price:', price)
            exit()
        if pay == ['*']:
            cost = eval(price) / person_count
        else:
            cost = eval(price) / len(pay)

        for person in pay:
            if person not in whopay:
                whopay[person] = []
            whopay[person].append([item, cost, eval(price)])

total = 0
for person, cost in whopay.items():
    if person != "*":
        total += sum([x[1] for x in cost])
    else:
        total += sum([int(x[2]) for x in cost])
print("Total amount:", total)

common_cost = 0
if "*" in whopay.keys():
    common_cost = sum([x[1] for x in whopay["*"]])

discount_per_person = 0
conv_fee_per_person = 0
print('Common Cost per person:', sum([x[1] for x in whopay["*"]]))
if len(discount) > 0:
    if(discount[0]=="%"):
        total_discount = total*discount[1]
        discount_per_person = total_discount/person_count
        conv_fee_per_person = discount[2]/person_count
        print('Discount per person:', discount_per_person)
        print('Final Amount paid:', round(total-total_discount+discount[2]))
        print()
        print('After discount:')
    elif discount[0]=="#":
        discount_per_person = discount[1]/person_count
        print('Discount per person:', discount_per_person)
        print('Final Amount paid:', round(total-discount[1]))
        print()
        print('After discount:')
else:
    print()

for person, cost in whopay.items():
    if person != "*":
        print(person, 'owes', round(sum([x[1] for x in cost])+common_cost+conv_fee_per_person-discount_per_person))
print()

for person, cost in whopay.items():
    print(person if person != "*" else "Common Cost")
    if person != "*":
        for citem, ccost, cprice in whopay["*"]:
            print(f'  {citem} - {ccost:.2f} ({cprice})')
    for pitem, pcost, pprice in cost:
        print(f'  {pitem} - {pcost:.2f} ({pprice})')    
