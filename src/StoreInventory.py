from Buyable import Buyable, BuyableClothing, BuyableFood, BuyableGame


class StoreInventory:

    def __init__(self):
        self.clothesForSale = []
        self.foodForSale = []
        self.gamesForSale = []
        self.allItems = []
        self.allSoldItems = []
        self.InitializeInitialInventory()
        self.AllItemsInit()

    def ReturnAllItems(self):
        return self.foodForSale + self.clothesForSale + self.gamesForSale

    def AllItemsInit(self):
        item: Buyable
        for item in self.ReturnAllItems():
            self.allItems.append(item)
    
    def GetSpecificSoldItems(self, count):
        for item in self.allSoldItems:
            item:Buyable
            x = 0

            if x > 0 and x >= count - 1:
                break
            else:
                print(f"Purchased {item.name} for ${item.price}")
                x += 1

    def AddToSoldItems(self, item):
        self.allSoldItems.append(item)

    def GetFullInventory(self):
        self.DisplayClothesInventory()
        self.DisplayFoodInventory()
        self.DisplayGamesInventory()

    def GetFoodInventory(self):
        self.DisplayFoodInventory()

    def GetClothesInventory(self):
        self.DisplayClothesInventory()

    def GetGamesInventory(self):
        self.DisplayGamesInventory()

    def DisplayClothesInventory(self):
        print("-*-*-*--Clothes--*-*-*-")
        item: BuyableClothing
        for item in self.clothesForSale:
            print(f"Size {item.size} {item.name}, Price: ${item.price}")

    def DisplayFoodInventory(self):
        print("-*-*-*--Food--*-*-*-")
        item: BuyableFood
        for item in self.foodForSale:
            print(f"{item.name}, Weight: {item.weight}g, Price: ${item.price}")

    def DisplayGamesInventory(self):
        print("-*-*-*--Games--*-*-*-")
        item: BuyableGame
        for item in self.gamesForSale:
            print(f"{item.name}, Genre: {item.genre}, {item.numPlayers} player game, Price: ${item.price}")

    def RemoveItemFromStoreInventory(self, item, isPurchase):
        if type(item) is BuyableClothing:
            self.clothesForSale.remove(item)
        elif type(item) is BuyableFood:
            self.foodForSale.remove(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.remove(item)

        # Reset All Items List
        self.allItems = []
        self.AllItemsInit()
        if isPurchase == True:
            self.allSoldItems.append(item)


    def AddItemToInventory(self, item):
        if type(item) is BuyableClothing:
            self.clothesForSale.append(item)
        elif type(item) is BuyableFood:
            self.foodForSale.append(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.append(item)

        # Reset All Items List
        self.allItems = []
        self.AllItemsInit()

    def AddMultipleItemsToInventory(self, item, num):
        if type(item) is BuyableClothing:
            for x in range(num):
                self.clothesForSale.append(item)
        elif type(item) is BuyableFood:
            for x in range(num):
                self.foodForSale.append(item)
        elif type(item) is BuyableGame:
            for x in range(num):
                self.gamesForSale.append(item)

    def InitializeInitialInventory(self):
        # Populate initial clothes list
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'medium'))
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'large'))

        # Shoes
        self.clothesForSale.append(BuyableClothing(99.99, 'Dress Shoes', '8'))
        self.clothesForSale.append(BuyableClothing(9.99, 'Sandals', '5'))

        # Gloves
        gloves = BuyableClothing(13.49, 'Gloves', 'Medium')
        self.AddMultipleItemsToInventory(gloves, 3)

        # Populate initial food list
        # Perishables
        self.foodForSale.append(BuyableFood(12.99, 'Pizza', 400))
        self.foodForSale.append(BuyableFood(24, 'Lasagna', 1000))
        self.foodForSale.append(BuyableFood(3.99, 'Spinach', 250))

        # Non-perishables
        self.foodForSale.append(BuyableFood(1.49, 'Beans', 300))
        self.foodForSale.append(BuyableFood(0.99, 'Noodles', 125))
        rice = BuyableFood(7.99, 'Rice', 2000)
        self.AddMultipleItemsToInventory(rice, 5)

        # Populate initial games list
        # Board Games
        self.gamesForSale.append(BuyableGame(19.99, 'Monopoly', 4, 'Board Game'))
        self.gamesForSale.append(BuyableGame(24.99, 'Scrabble', 2, 'Board Game'))

        # Computer Games
        self.gamesForSale.append(BuyableGame(79.99, 'Breath of the Wild', 2, 'Open-World'))
        self.gamesForSale.append(BuyableGame(59.99, 'Forza', 2, 'Racing/Open-World'))
