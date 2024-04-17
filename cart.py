import sys
import os

def fileReader(path):
    """
    Reads the contents of a file and returns them as a list of strings.

    Args:
        path (str): The path to the file to be read.

    Returns:
        list: A list of strings representing the contents of the file.
    """
    with open(path, 'r') as file:
        cart = file.read().splitlines()
    return cart

def SplitEngine(cart):
    """
    Splits the cart items and calculates the cost for each person.

    Args:
        cart (list): A list of cart items in the format 'pay-item-price'.

    Returns:
        dict: A dictionary where the keys are the people who need to pay and the values are lists of [item, cost, price] for each person.
    """
    whopay = {}
    try:
        itemcount = 1
        for item in cart:
            if item != '':
                pay, item, price = item.split('-')
                pay = list(pay)
                if price.isupper() or price.islower() or price.isspace() or price == '':
                    print('Invalid price:', price, "at line", itemcount)
                    exit()
                cost = eval(price) / len(pay)

                for person in pay:
                    if person not in whopay:
                        whopay[person] = []
                    whopay[person].append([item, cost, price])
            itemcount += 1

    except Exception as e:
        print('Invalid input:', e)
        exit()
    return whopay

def ReportEngine(whopay):
    """
    Generates a report of the total amount, individual debts, and itemized costs for each person in the shopping cart.

    Args:
        whopay (dict): A dictionary containing the names of people as keys and their respective shopping costs as values.

    Returns:
        None
    """
    print("Total amount:", sum([x[1] for person, cost in whopay.items() for x in cost]))

    for person, cost in whopay.items():
        print(person, 'owes', sum([x[1] for x in cost]))

    for person, cost in whopay.items():
        print(person)
        for item, cost, price in cost:
            print(f'  {item} - {cost:.2f} ({price})')

prefix = os.getcwd()
path = os.path.join(prefix, 'Example', 'cart.txt')
if len(sys.argv) > 1:
    path = os.path.join(prefix, sys.argv[1])
    if not os.path.exists(path):
        print('File not found:', path)
        exit()

if __name__ == '__main__':
    cart = fileReader(path)
    whopay = SplitEngine(cart)
    ReportEngine(whopay)