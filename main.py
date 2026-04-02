import random

class Player:
    def __init__(self) -> None:
        self.hand = []
        
        pass
    
    def getCard(self,card:tuple) -> None:
        self.hand.append(card)

        pass

    def checkIdx(self,reference:tuple) -> int | bool:
        for idx in range(len(self.hand)):
            if self.hand[idx][0] == reference[0] or self.hand[idx][1] == reference[1] or self.hand[idx][1] == 11:
                return idx
        
        return False
    
class Game:
    def __init__(self):
        self.Deck = []
        self.top = None
        self.mode = 0
        self.turn = True #User 차례가 True

        pass

    def updateDeck(self,deck):
        self.Deck = deck

        pass

    def makeTopCard(self) -> tuple:
        while True:
            top = self.Deck.pop()
            if top[1] <= 9:
                return top
            
    def wild(self,suit,value):
        self.top = (suit,value) #이때 value는 사용자로부터 입력 받은거
        
        return

                


def make_deck():
    deck = []
    for suit in range(4):
        for value in range(11):
            deck.append((suit,value))

    random.shuffle(deck)
    
    return deck

def make_initial_card(deck,player):
    for i in range(6):
        player.getCard(deck.pop())

    return None


def show_game_state(game:Game,player:Player) -> tuple:
    return (game.top,len(game.Deck),player.hand)

def show_player_hand():
    return

def is_playable_card(card,reference):
    if card[0] == reference[0] or card[1] == reference[1] or card[1] == 11:
        return True
    return False

def is_valid_card_index():
    return

def play_user_turn():
    return

def play_computer_turn():
    return

def main():  
   
    user = Player()
    computer = Player()
    game = Game()
    game.updateDeck(make_deck())
    make_initial_card(game.Deck,user)
    make_initial_card(game.Deck,computer)
    print("Welcome to One card Game! Select Game Mode. (Play Mode:0 Debug Mode:1)")
    game.mode = input("Enter GameMode:")

    while True:
        top = game.makeTopCard()


        

        game.turn = not game.turn
        


    
        

        