# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def vending_machine():
    # Predefined drinks available in the vending machine, key=name of drink, value=price of drink
    total = 0

    drinks = {
        "Coffee": 10,
        "Pepsi": 10,
        "Coca Cola": 10,
        "100 Plus": 10
    }

    bills_available = {
        50: 100,
        20: 100,
        10: 100,
        5: 100,
        1: 100,

    }

    # Get the drinks user wish to buy
    while True:
        for key, value in drinks.items():
            print("{0:<10} {1:>10}".format(key, f"RM: {value}"))
        # Input validation
        desired_drinks = input("Please enter the drinks you wish to buy:").lower().strip()


        for key, value in drinks.items():
            if key.lower().replace(" ", "") == desired_drinks:
                total = value
                break

        # if total is larger than 0 means user selected a valid drink
        if total > 0:
            break

        print("Please enter a valid drink form the list!")

    return_bills = {}

    # Get the bills user inserted
    while True:
        print(f"We only accept bills, no coins allowed! Total is {total}")
        inserted_amount = input("How many bills you wish to insert:")
        if inserted_amount.isnumeric():
            if int(inserted_amount) < total:
                print("Insufficient bill, please insert more bills")
            else:
                break

    return_bills = {}
    total = int(inserted_amount) - total

    while total > 0:
        for key in bills_available.keys():
            if total >= key and bills_available[key] > 0:
                total -= key
                bills_available[key] -= 1
                if key not in return_bills:
                    return_bills[key] = 1
                else:
                    return_bills[key] += 1
                break

    print("Returning: ")
    for key, value in return_bills.items():
        print(f"RM {key} - {value}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vending_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
