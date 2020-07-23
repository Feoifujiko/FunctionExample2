def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("-----iShop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1 :
        print(vatCalculate())
        return userSelected
    elif userSelected == 2 :
        print(priceCalculate())
        return userSelected
def vatCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    vat = 7
    result = totalPrice - (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


if login() == True :
    showMenu()
    menuSelect()
else:
    print("ERROR")