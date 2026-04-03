import random

#남은 할 일,, wildcard 알고리즘 for user and computer, 

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
    print(f"Top Card: {game.top}")
    print(f"Deck: {player.hand}")
    print(f"Number of cards in deck: {len(game.Deck)}")
    
    return (game.top,len(game.Deck),player.hand)

def show_player_hand():
    return

def is_playable_card(card:tuple,reference:tuple):
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
    game.mode = input("Enter GameMode:") == 1

    while True:
        
        #User 차례일 때
        if game.turn:
            print("User playing. ")
            display_status("User",user.hand,game.top)
            if len(user.hand) == 0:
                win(0)
                break
            if user.checkIdx(game.top) == False:
                user.hand.append(game.draw())
                print("")
                if user.checkIdx(game.top) != False:
                    game.top = user.hand.pop(int(user.checkIdx(game.top)))
                    game.turn = not game.turn
                    print("")
                game.turn = not game.turn
                print("")
            
            else:   
                command = input(f"Enter card index (0–{len(user.hand)}) or q (quit):")
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

        #Computer 차례일 때
        elif not game.turn:
            print("Computer Playing. ")
            ## Debug mode인 경우 제어문
            if game.mode:
                show_game_state(game,computer)
            if len(computer.hand) == 0:
                win(2)
                break
            if user.checkIdx(game.top) == False:
                user.hand.append(game.draw())
                print("No card playable, Getting one card from the Deck. ")
                if user.checkIdx(game.top) != False:
                    game.top = user.hand.pop(int(user.checkIdx(game.top)))
                    game.turn = not game.turn
                    print("The card is automatically Played. ")
                game.turn = not game.turn
                print("자동으로 순서 넘어감")

            else:
                command = computer.checkIdx(game.top)
                if command == False:
                    print("lose") # 이 부분 추가 필요
                    
                if computer.hand[command][1] == 10:
                    game.top = computer.hand.pop(int(command))
                elif computer.hand[command][1] == 11:
                    game.wild()
                else:
                    game.top = computer.hand.pop(int(command))
                    game.turn = not game.turn



        


if __name__ == "__main__":
    main()
            
                
        
            


        

        
        


    
        

        