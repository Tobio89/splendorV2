red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'

emptyTokenWallet = {
    red:0,
    green:0,
    blue:0,
    white:0,
    black:0,
    yellow:0
}



class player():
    def __init__(self, name, nobles=[], cards=[], reservedCards=[], tokens=emptyTokenWallet.copy()):
        self.name = name
        self.nobles = nobles
        self.cards = cards
        self.tokens = tokens

        
    
    #Inventory Methods

    def addToken(self, color, quantity):
        self.tokens[color] += quantity

    def minusToken(self, color, quantity):
        self.tokens[color] -= quantity
    
    def addCard(self, selectedCard):
        self.cards.append(selectedCard)

    def addNoble(self, selectedNoble):
        self.nobles.append(selectedNoble)

    def getTotalTokens(self):
        totalTokens = 0
        for tokenQuant in self.tokens.values():
            totalTokens += tokenQuant
        return totalTokens

    def canPickUp(self):

        if self.getTotalTokens() >= 10:
            return False
        else:
            return True
    
    def getPickupQuant(self):
        if self.canPickUp:
            if self.getTotalTokens() < 8:
                return 3
            if self.getTotalTokens() == 8:
                return 2
            if self.getTotalTokens() == 9:
                return 1
            if self.getTotalTokens() > 10:
                return 0
        else:
            return 0
    
    def getCardCount(self):
        cardCount = emptyTokenWallet.copy()
        if self.cards:
            for card in self.cards:
                cardCount[card.color] += 1
        return cardCount
    
    def getCombinedWallet(self):
        combinedWallet = emptyTokenWallet.copy()
        for color in combinedWallet.keys():
            combinedWallet[color] = self.tokens[color] + self.getCardCount()[color]
        return combinedWallet

    def getPrestige(self):
        points = 0
        if self.cards:
            for card in self.cards:
                points += card.pointValue
        if self.nobles:
            for noble in self.nobles:
                points += noble.pointValue
        return points

player1 = player('Toby')

# print(player1.name)
# print(player1.tokens)
# player1.addToken(red, 5)
# print(player1.tokens)
# print(player1.tellScore())
# print(player1.tokens[red])
# print(player1.getTotalTokens())
