from StoreInventory import StoreInventory
from BankAccount import BankAccount
from Buyable import Buyable, BuyableGame, BuyableFood, BuyableClothing
from ClampValue import ClampValue
from EmployeePanel import EmployeePanel

# Initialize inventories
storeInventory = StoreInventory()
myStuff = list()
myShoppingCart = list()

# Other Variables
allStoreItems = storeInventory.allItems
employeePanel = EmployeePanel()

# Placeholder bank account (Gets replaced on program start with an actual Bank Account)
myBankAccount = BankAccount(0, '')


def Startup():
    CreateBankAccount()
    MainMenu()


def BuyItem():
    userItem = input("Which item would you like to buy?").lower()
    storeItems: Buyable
    item = 0

    isItemFound = False

    for storeItems in storeInventory.ReturnAllItems():
        item += 1

        if storeItems.name.lower() == userItem:
            isItemFound = True

            print("Item found in our stock!")
            print("Would you like to:")
            print("1. BUY NOW")
            print("2. Add To cart")
            print("3. Cancel Purchase")

            try:
                itemFoundChoice = int(input("(1-3) "))
            except ValueError:
                print("Please choose a valid value!")
                break

            itemFoundChoice = ClampValue(itemFoundChoice, 1, 3)
            match itemFoundChoice:
                case 1:
                    print("Ok, buying now!")
                    MakePurchaseFromStore(storeInventory.allItems[item - 1])
                    break

                case 2:
                    print("Ok, adding to shopping cart!")
                    MoveItemToShoppingCart(storeInventory.allItems[item - 1])

                    break

                case 3:
                    print("Cancelling Purchase...")
                    break

    if not isItemFound:
        print("Item Not Found!")


def ReviewMyInventory():
    print('Here is a list of the items you now own: ')
    for item in myStuff:
        print(item.name)


def ReviewFinancials():
    print(f"Would you like to deposit money into the account?")

    print(f"1. Yes")
    print(f"2. No")
    try:
        depositCheck = int(input())
        if 1 <= depositCheck <= 2:
            match depositCheck:
                case 1:
                    try:
                        howMuchToDeposit = float(input(f"How much money would you like to deposit into your account?"))
                    except ValueError:
                        print("ERROR: value is not valid")
                        return

                    if howMuchToDeposit < 0:
                        print(f"ERROR: Cannot deposit a negative value into an account!")
                        return
                    myBankAccount.MakeDeposit(howMuchToDeposit)
                case 2:
                    print(f"Not making a deposit!")
                    return
        else:
            print("Pick a choice between 1 and 2!")

    except TypeError:
        print("Pick a valid number!")
        ReviewFinancials()
        return


def ReviewShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        for item in myShoppingCart:
            print(item.name)

        # Check to see if the user wants to purchase anything currently in their shopping cart

        print(f"Would you like to purchase any held items now?")
        print(f"1. Yes")
        print(f"2. No")

        try:
            checkoutChoice = int(input("(1-2) "))
            ClampValue(checkoutChoice, 1, 2)
            match checkoutChoice:
                case 1:
                    BuyItemInShoppingCart()
                    return
                case 2:
                    print(f"Leaving shopping cart as is and returning to the storefront...")
                    return

        except ValueError:
            print("Please enter a valid value!")
    else:  # If cart is empty
        print('Your shopping cart is empty! Nothing to see here... ')


def BuyItemInShoppingCart():
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match
    items: Buyable
    currentItem = 0
    if len(myShoppingCart) > 0:
        for items in myShoppingCart:
            if myShoppingCart[currentItem].lower() == userChoice.lower():
                MakePurchaseFromCart(myShoppingCart[currentItem])
                return
            currentItem += 1

        print('Item could not be found in shopping cart... ')
    else:
        print("Shopping cart is empty!")
        return


def RemoveItemFromCart(item):
    removeChoice = input('Which item would you like to remove from your shopping cart?')

    # Compare user requested name with cart entry names and remove item if found
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == removeChoice.lower():
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            MoveItemFromShoppingCartToInventory(itemInCart)
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')


def MoveItemToShoppingCart(item):
    myShoppingCart.append(item)
    storeInventory.allItems.remove(item)


def MoveItemFromShoppingCartToInventory(item):
    storeInventory.AddItemToInventory(item)
    myShoppingCart.remove(item)


def MakePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.IsItemAffordable(item.price):
        myBankAccount.MakePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
        myStuff.append(item)
        storeInventory.RemoveItemFromStoreInventory(item)
    else:
        print('You can\'t afford this item ... ')


def MakePurchaseFromCart(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.IsItemAffordable(item.price):

        if myBankAccount.VerifyPassword():  # Check for password
            myBankAccount.MakePurchase(item.price)
            print(f'Purchase complete! You now own {item.name}')
            myStuff.append(item)
            myShoppingCart.remove(item)
        else:
            print("Purchase cancelled due to inputting an incorrect password!")
            return
    else:
        print('You can\'t afford that item ... ')


# PROGRAM BEGINS HERE
print('Welcome to the cool people store B)')


def CreateBankAccount():
    # setup bank account
    print('To begin, please set up a bank account.')
    try:
        deposit = input('How much do you want to deposit into your account? ')
        depositCheck = float(deposit)

        if depositCheck <= 0:
            print("LOL! you are bankrupt!!")
        myBankAccount.MakeInitialDeposit(depositCheck)

    except ValueError:
        print("Please enter a valid integer!")
        CreateBankAccount()
        return

    myBankAccount.SetPassword()


def GetInventory():
    inventoryListChoice = None

    print("Which product type would you like to view?")
    print("1. Food")
    print("2. Clothes")
    print("3. Games")
    print("4. The entire inventory")
    print("5. Back")

    try:
        inventoryListChoice = int(input("(1-5) "))
        inventoryListChoice = ClampValue(inventoryListChoice, 1, 5)
    except ValueError:
        print("Please input a valid value!")

    match inventoryListChoice:
        case 1:
            storeInventory.GetFoodInventory()
            return
        case 2:
            storeInventory.GetClothesInventory()
            return
        case 3:
            storeInventory.GetGamesInventory()
            return
        case 4:
            storeInventory.GetFullInventory()
            return
        case 5:
            return


def MainMenu():
    stillShopping = True

    while stillShopping:
        print("\n------------------------------------------------------------ ")
        print("Please choose from one of the following menu options: ")
        print("1. View catalog of items to buy")
        print("2. Buy an item")
        print("3. View your cart of held items")
        print("4. Review the items you already own")
        print("5. View the status of your financials")
        print("6. Employee Login")
        print("7. Exit program")

        userChoice = int(input())
        userChoice = ClampValue(userChoice, 1, 7)

        match userChoice:
            case 1:
                GetInventory()
            case 2:
                BuyItem()
            case 3:
                ReviewShoppingCart()
            case 4:
                ReviewMyInventory()
            case 5:
                print(f"you currently have ${myBankAccount.BalanceReport()} in your bank account")
                ReviewFinancials()
            case 6:
                employeePanel.VerifyEmployeePassword()
            case 7:
                print('Thanks for shopping! Now exiting program ... ')
                stillShopping = False


Startup()
