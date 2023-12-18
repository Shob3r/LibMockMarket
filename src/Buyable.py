class Buyable:
    def __init__(self, price, name, category):
        self.price = price
        self.name = name
        self.category = category


class BuyableClothing(Buyable):
    def __init__(self, price, name, size):
        super().__init__(price, name, "Clothing")
        self.size = size


class BuyableFood(Buyable):
    def __init__(self, price, name, weight):
        super().__init__(price, name, "Food")
        self.weight = weight


class BuyableGame(Buyable):
    def __init__(self, price, name, numPlayers, genre):
        super().__init__(price, name, "Clothing")
        self.numPlayers = numPlayers
        self.genre = genre
