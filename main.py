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
        self.mode = False #Debug mode 여부
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
    
    def play(self,card):

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

def win(result:int) -> None:
    if result == 0:
        pass
    elif result == 1:
        pass

    elif result == 3:
        pass
    
def display_status(name:str,hand:list) -> None:
    return     

def display_winner(name:str) -> None:

    return

def main():  
   
    user = Player()
    computer = Player()
    game = Game()
    game.updateDeck(make_deck())
    make_initial_card(game.Deck,user)
    make_initial_card(game.Deck,computer)
    print("Welcome to One card Game! Select Game Mode. (Play Mode:0 Debug Mode:1)")
    game.mode = input("Enter GameMode:") == 1

    while True:
        top = game.makeTopCard()

        if game.turn:
            if len(user.hand) == 0:
                win(2)
                break

            command = input(f"Enter card index (0–{len(user.hand)}) or q (quit):")
            if command == "q":
                quit()
            if not is_playable_card(user.hand[int(command)],game.top):
                print("이카드안됨")
            else:
                game.top = user.hand.pop(int(command))
                game.turn = not game.turn
        
        elif not game.turn:
            print("Computer Playing. ")
            ## Debug mode인 경우 제어문
            if game.mode:
                display_status("Computer",computer.hand)
            if len(computer.hand) == 0:
                win(2)
                break
            bestAns = computer.checkIdx()
            if bestAns == False:
                print("lose") # 이 부분 추가 필요
            game.top = computer.hand.pop(bestAns)
            game.turn = not game.turn


        



            
                
        
            


        

        
        


    
        

        