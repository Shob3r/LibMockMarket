from StoreInventory import StoreInventory
from BankAccount import BankAccount
from Buyable import Buyable, BuyableGame, BuyableFood, BuyableClothing
from clearScreen import clearScreen

# Initialize inventories
storeInventory = StoreInventory()

myStuff = list()
myShoppingCart = list()

# Other Variables
allStoreItems = storeInventory.allItems

# Placeholder bank account
myBankAccount = BankAccount(0, '')


# FUNCTIONS TO MANAGE MENUING SYSTEM IN MAIN SHOPPING PROGRAM

def clampValue(valueToClamp, minRange, maxRange):
    # Chatting up the GPT or whatever it's called
    return max(min(valueToClamp, maxRange), minRange)


def buyItem():
    userItem = input("Which item would you like to buy?").lower()
    storeItems: Buyable
    item = 0

    isItemFound = False

    for storeItems in storeInventory.returnFullInventory():
        item += 1

        if storeItems.name.lower() == userItem:
            isItemFound = True

            print("Item found in our stock!")
            print(f"Found at place ")
            print("Would you like to:")
            print("1. BUY NOW")
            print("2. Add To cart")
            print("3. Cancel Purchase")

            choosing = True

            while choosing:
                try:
                    itemFoundChoice = int(input("(1-3) "))
                except ValueError:
                    print("Please choose a valid value!")
                    break

                itemFoundChoice = clampValue(itemFoundChoice, 1, 3)
                match itemFoundChoice:
                    case 1:
                        print("Ok, buying now!")
                        moveItemToShoppingCart(storeInventory.allItems[item])
                        makePurchaseFromStore(storeInventory.allItems[item])
                        break
                    case 2:
                        print("Ok, Adding to cart!")
                        moveItemToShoppingCart(storeInventory.allItems[item])
                        break
                    case 3:
                        print("Cancelling Purchase...")
                        choosing = False
                        break

    if not isItemFound:
        print("Item Not Found!")


def reviewMyInventory():
    print('Here is a list of the items you now own: ')
    for item in myStuff:
        print(item.name)


def reviewFinancials():
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
                    myBankAccount.makeDeposit(howMuchToDeposit)
                case 2:
                    print(f"Not making a deposit!")
                    return
        else:
            print("Pick a choice between 1 and 2!")
    except TypeError:
        print("Pick a valid number!")
        reviewFinancials()
        return


def reviewMyShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        for item in myShoppingCart:
            print(item.name)

        # Check to see if the user wants to purchase anything currently in their shopping cart
        shoppingCartChoice = int(
            input('Would you like to purchase any held items now? 1 for YES or any other key for NO'))

        if shoppingCartChoice == 1:
            buyItemInShoppingCart()
        else:
            print('Leaving shopping cart as is and returning to the storefront... ')

    else:  # If cart is empty
        print('Your shopping cart is empty! Nothing to see here... ')


def buyItemInShoppingCart():
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match

    for i in myShoppingCart:
        if myShoppingCart[i].lower() == userChoice.lower():
            makePurchaseFromShoppingCart(myShoppingCart[i])
        else:
            print('Item could not be found in shopping cart ... ')


def removeItemFromShoppingCart(item):
    removeChoice = input('Which item would you like to remove from your shopping cart?')

    # Compare user requested name with cart entry names and remove item if found
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == removeChoice.lower():
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            moveItemFromShoppingCartToInventory(itemInCart)
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')


def moveItemToShoppingCart(item):
    myShoppingCart.append(item)
    storeInventory.allItems.remove(item)


def moveItemFromShoppingCartToInventory(item):
    storeInventory.restockItemToInventory(item)
    myShoppingCart.remove(item)


def makePurchaseFromStore(item):

    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):
        myBankAccount.makePurchase(item.price)
        print(f'Purchase complete! You now own {item.name}')
        myStuff.append(item)
        storeInventory.removeItemFromInventory(item)
    else:
        print('You can\'t afford this item ... ')


def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store
    if myBankAccount.canAfford(item.price):

        if myBankAccount.checkPassword():  # Check for password
            myBankAccount.makePurchase(item.price)
            print(f'Purchase complete! You now own {item.name}')
            myStuff.append(item)
            myShoppingCart.remove(item)
    else:
        print('You can\'t afford that item ... ')


# PROGRAM BEGINS HERE
print('Welcome to the cool people store B)')


def setupBankAccount():
    # setup bank account
    print('To begin, please set up a bank account.')
    try:
        deposit = input('How much do you want to deposit into your account? ')
        depositCheck = float(deposit)

        if depositCheck <= 0:
            print("LOL! you are bankrupt!!")
        myBankAccount.makeInitialDeposit(depositCheck)

    except ValueError:
        print("Please enter a valid integer!")
        setupBankAccount()
        return

    myBankAccount.setPassword()


def shoppingMenu():
    stillShopping = True

    while stillShopping:
        print("\n------------------------------------------------------------ ")
        print("Please choose from one of the following menu options: ")
        print("1. View catalog of items to buy")
        print("2. Buy an item")
        print("3. View your cart of held items")
        print("4. Review the items you already own")
        print("5. View the status of your financials")
        print("6. Launch Store GUI")
        print("7. Exit program")

        userChoice = int(input())
        userChoice = clampValue(userChoice, 1, 7)

        match userChoice:
            case 1:
                storeInventory.getFullInventory()
            case 2:
                buyItem()
            case 3:
                reviewMyShoppingCart()
            case 4:
                reviewMyInventory()
            case 5:
                print(f"you currently have ${myBankAccount.balanceReport()} in your bank account")
                reviewFinancials()
            case 6:
                print("YOUR CONTENT HERE!")
            case 7:
                print('Thanks for shopping! Now exiting program ... ')
                stillShopping = False


setupBankAccount()
shoppingMenu()
