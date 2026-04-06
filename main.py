import random
import time

#남은 할 일,, wildcard 알고리즘 for user and computer, when deck is empty.. 
# 디버그하기, 

class Player:
    def __init__(self) -> None:
        self.hand = []
        
        pass
    
    def getCard(self,card:tuple) -> None:
        self.hand.append(card)

        pass

    def checkIdx(self,reference:tuple) -> int:
        for idx in range(len(self.hand)):
            if self.hand[idx][0] == reference[0] or self.hand[idx][1] == reference[1] or self.hand[idx][1] == 11:
                return idx
        
        return 1000
    
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
                self.top = top
                return
            
    def wild(self,isBot:bool,player:Player):
        if isBot: 
            suit = self.autoChoice(player)
        
        else: 
            suit = input("Which Suit Do you Choose?")


        self.top = (suit,11)
        print("Wild Card Setted")
        
        return
    
    @staticmethod
    def autoChoice(player:Player) -> int:
        values = [card[1] for card in player.hand]
        count = [0,0,0,0]
        for i in values:
            count[i] += 1
        max = max(values)
        idx = values.index(max)
        
        candidates = [idx]

        for k in range(count):
            if count[k] == max:
                candidates.append(k)        
  
        return random.choice(candidates)
    
    
    def draw(self):
        
        return self.Deck.pop()
    

                


def make_deck():
    deck = []
    for suit in range(4):
        for value in range(11):
            deck.append((suit,value))

    random.shuffle(deck)
    
    return deck

def make_initial_card(deck:list,player:Player):
    for i in range(6):
        player.getCard(deck.pop())

    return None


def show_game_state(game:Game,player:Player) -> None:
    print("")
    print(f"Top Card: {game.top}")
    print(f"Deck: {player.hand}")
    print(f"Number of cards in deck: {len(game.Deck)}")
    print("")
    
    return (game.top,len(game.Deck),player.hand)

def show_player_hand():
    return

def is_playable_card(card:tuple,reference:tuple):
    if card[0] == reference[0] or card[1] == reference[1] or card[1] == 11:
        return True
    return False

def is_valid_card_index():
    return

#main에 있는 알고리즘 복붙하기
def play_user_turn(game:Game,user:Player):
    return
def play_computer_turn(game:Game,computer:Player):
    return

def win(result:int) -> None:
    if result == 0:
        display_winner("User")
        pass
    elif result == 1:
        display_winner("Computer")
        pass

    elif result == 3:
        print("Draw. ")
        pass
    

def display_winner(name:str) -> None:

    return

def main():   
    user = Player()
    computer = Player()
    game = Game()
    game.updateDeck(make_deck())
    make_initial_card(game.Deck,user)
    make_initial_card(game.Deck,computer)
    game.makeTopCard()
    print("Welcome to One card Game! Select Game Mode. (Play Mode:0 Debug Mode:1)")
    game.mode = int(input("Enter GameMode:")) == 1

    while True:
        print(f"game mode is {game.mode}")
    
        #User 차례일 때
        if game.turn:
            print("User playing. ")
            show_game_state(game,user)
            if len(user.hand) == 0:
                win(0)
                break
            if user.checkIdx(game.top) == 1000:
                user.hand.append(game.draw())
                print("")
                if user.checkIdx(game.top) != 1000:
                    print(user.checkIdx(game.top))
                    game.top = user.hand.pop(int(user.checkIdx(game.top)))
                    
                    print("유저가 자동으로 뽑은 카드 내기")
                game.turn = not game.turn
            
            
            
            else:   
                command = int(input(f"Enter card index (0–{len(user.hand)}) or q (quit):"))
                if command == "q":
                    quit()
                if not is_playable_card(user.hand[int(command)],game.top):
                    print("이카드안됨")
                
                else:
                    if user.hand[command][1] == 10:
                        game.top = user.hand.pop(int(command))
                    elif user.hand[command][1] == 11:
                        game.wild()
                    else:
                        game.top = user.hand.pop(int(command))
                        game.turn = not game.turn
            print("")


        #Computer 차례일 때
        elif not game.turn:
            print("Computer Playing. ")
            ## Debug mode인 경우
            if game.mode:
                print("computer status")
                show_game_state(game,computer)
            # 덱에 카드가 없으면 이긴다. 
            if len(computer.hand) == 0:
                win(2)
                break
            #낼 카드가 없으면
            if computer.checkIdx(game.top) == 1000:
                computer.hand.append(game.draw()) #덱에서 하나 뽑고
                show_game_state(game,computer)
                print("No card playable, Getting one card from the Deck. ")
                if computer.checkIdx(game.top) != 1000: #다시 체크했을 때 낼 카드가 있으면
                    print(computer.checkIdx(game.top))
                    game.top = computer.hand.pop(int(computer.checkIdx(game.top))) #그걸 자동으로 낸다. 
                    
                    print("The card is automatically Played. ")
                game.turn = not game.turn # 차례 바꾸기
                
                    
                print("자동으로 순서 넘어감\n")

            else: #낼 카드가 있다면
                command = computer.checkIdx(game.top) #컴퓨터가 알아서 골라서 낸다. 

                if computer.hand[command][1] == 10:
                    game.top = computer.hand.pop(int(command))
                if computer.hand[command][1] == 11: #낸 카드가 wildcard면
                    game.wild()
                else:
                    game.top = computer.hand.pop(int(command))
                    game.turn = not game.turn
                
            print("")


    




        


if __name__ == "__main__":
    main()
            
                
        
            


        

        
        


    
        

        