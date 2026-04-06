import random

#남은 할 일,, 
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
            suit = int(input("Which Suit Do you Choose? 0:♡ 1:♠ 2:◇ 3:3"))


        self.top = (suit,11)
        print("Wild Card Setted")
        
        return
    
    @staticmethod
    def autoChoice(player:Player) -> int:
        suits = [card[0] for card in player.hand]
        count = [0,0,0,0]
        for i in suits:
            count[i] += 1
        maxSuit = max(suits)
        idx = suits.index(maxSuit)
        
        candidates = [idx]

        for k in range(len(count)):
            if count[k] == maxSuit:
                candidates.append(k)        
  
        return random.choice(candidates)
    
    
    def draw(self):
        
        return self.Deck.pop()
    

                


def make_deck():
    deck = []
    for suit in range(4):
        for value in range(12):
            deck.append((suit,value))

    random.shuffle(deck)
    
    return deck

def make_initial_card(deck:list,player:Player):
    for i in range(6):
        player.getCard(deck.pop())

    return None


def show_game_state(game:Game) -> None:
    print("")
    print(f"Top Card: {suitFormater(game.top)}")
    print("")
    print(f"Number of cards in deck: {len(game.Deck)}")
    print("")
    
    return 

def suitFormater(card:tuple) -> str:
    if card[0] == 0:
        return f"♡ {card[1]}"
    elif card[0] == 1:
        return f"♠ {card[1]}"
    elif card[0] == 2:
        return f"◇ {card[1]}"
    elif card[0] == 3:
        return f"♣ {card[1]}"
    return 

def show_player_hand(player:Player):

    for i in player.hand:
        print(f"{player.hand.index(i)}: {suitFormater(i)}")
        
    
    return

def is_playable_card(card:tuple,reference:tuple):
    if card[0] == reference[0] or card[1] == reference[1] or card[1] == 11:
        return True
    return False

def is_valid_card_index(player:Player,input):
    if len(player.hand) < input:
        return False
    return True

#main에 있는 알고리즘 복붙하기
def play_user_turn(game:Game,user:Player):
    print("User playing. ")
    show_game_state(game)
    show_player_hand(user)
    if len(user.hand) == 0:
        win(0)
        quit()
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
        if not command.isdigit():
            print("Invalid input...")
            return
        
        if command == "q":
            quit()

        elif not is_valid_card_index(user,command):
            print("Not Valid Index. Try again. ")
            return

        elif not is_playable_card(user.hand[int(command)],game.top):
            print("이카드안됨")
        
        else:
            if user.hand[command][1] == 10:
                game.top = user.hand.pop(int(command))
            elif user.hand[command][1] == 11:
                user.hand.pop(int(command))
                game.wild(False,user)
                game.turn = not game.turn
            else:
                game.top = user.hand.pop(int(command))
                game.turn = not game.turn
    print("")
    return

def play_computer_turn(game:Game,computer:Player) -> None:
    print("Computer Playing. ")
    # Debug mode인 경우
    if game.mode:
        show_game_state(game)
        show_player_hand(computer)
    # 덱에 카드가 없으면 이긴다. 
    if len(computer.hand) == 0:
        win(2)
        quit()
    #낼 카드가 없으면
    if computer.checkIdx(game.top) == 1000:
        computer.hand.append(game.draw()) #덱에서 하나 뽑고
        show_game_state(game)
        show_player_hand(computer)
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
            computer.hand.pop(int(command))
            game.wild(True,computer)
            game.turn = not game.turn
        else:
            game.top = computer.hand.pop(int(command))
            game.turn = not game.turn
        
    print("")
    return

def win(result:int) -> None:
    if result == 0:
        display_winner("User")
        quit()
        pass
    elif result == 1:
        display_winner("Computer")
        quit()
        pass

    elif result == 2:
        print("Draw. ")
        quit()
        pass
    

def display_winner(name:str) -> None:

    trophy_art = r"""
        ___________
       '._==_==_=_.'
       .-\:      /-.
      | (|:.     |) |
       '-|:.     |-'
         \::.    /
          '::. .'
            ) (
          _.' '._
         `"""""""`
    """

    banner = f"🎉 {name} WINS! 🎉"

    print(trophy_art)
    print(banner)
    print("=" * len(banner))


    return

def noCardInDeck(user:Player,computer:Player) -> None:
    userCard = len(user.hand)
    computerCard = len(computer.hand)

    if userCard > computerCard:
        win(0)
    elif userCard < computerCard:
        win(1)
    else:
        win(2)
    
    return
    
def main() -> None:   

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
        if len(game.Deck) == 0:
            noCardInDeck(user,computer)
            
        print(f"game mode is {game.mode}")
    
        #User 차례일 때
        if game.turn:
            play_user_turn(game,user)


        #Computer 차례일 때
        elif not game.turn:
            play_computer_turn(game,computer)




        


if __name__ == "__main__":
    main()
            
                
        
            


        

        
        


    
        

        