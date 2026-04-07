import random

class Player:
    def __init__(self) -> None:
        self.hand = [] #유저가 가지고 있는 카드
        
        pass
    
    #유저가 가지고 있는 카드의 모음에 새로운 카드를 추가한다. 
    def getCard(self,card:tuple) -> None:
        self.hand.append(card)

        pass

    def checkIdx(self,reference:tuple) -> int:
        for idx in range(len(self.hand)):
            #value, suit가 같거나 낸 카드가 WildCard라면
            if self.hand[idx][0] == reference[0] or self.hand[idx][1] == reference[1] or self.hand[idx][1] == 11: 
                return idx
        
        return -1
    
class Game:
    def __init__(self):
        self.Deck = []
        self.top = None
        self.mode = False #Debug mode 여부
        self.turn = True #User 차례가 True

        pass
    
    #받은 덱(리스트)를 게임의 덱으로 사용한다. 
    def updateDeck(self,deck):
        self.Deck = deck

        pass
    
    #일반 카드가 뽑힐 때 까지 Top card 뽑기
    def makeTopCard(self) -> tuple:
        while True:
            top = self.Deck.pop()
            if top[1] <= 9:
                self.top = top
                return
            
    def wild(self,isBot:bool,player:Player):
        #컴퓨터용 wildCard 절차 진입
        if isBot: 
            suit = self.autoChoice(player)
        
        #유저인 경우 유저가 직접 카드 고르기. 
        else: 
            while True:
                suit = input("Which Suit Do you Choose? 0:♡ 1:♠ 2:◇ 3:3")
                if not suit.isdigit():
                    print("Not Valid Input. ")
                suit = int(suit)
                
                break
                


        self.top = (suit,11)
        print("Wild Card Setted")
        
        return
    
    @staticmethod #컴퓨터가 WildCard를 사용했을 때 자동으로 suit를 고르는 알고리즘. 
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
    

                

#초기 덱 만들어서 리스트로 반환
def make_deck():
    deck = []
    for suit in range(4):
        for value in range(12):
            deck.append((suit,value))

    random.shuffle(deck)
    
    return deck

#인자로 받은 Player에게 카드를 6장씩 덱에서 빼서 나눠준다. 
def make_initial_card(deck:list,player:Player):
    for i in range(6):
        player.getCard(deck.pop())

    return None

#게임의 상태를 보여준다. 
def show_game_state(game:Game) -> None:
    print("")
    print(f"Top Card: {suitFormater(game.top)}")
    print("")
    print(f"Number of cards in deck: {len(game.Deck)}")
    print("")
    
    return 

def suitFormater(card:tuple) -> str:
    #카드 데이터(튜플)을 사람이 알아보기 쉬운 형식의 데이터로 바꿔서 보여준다. 
    if card[1] == 10:
        value = "S"
    elif card[1] ==11:
        value = "W"
    else:
        value = card[1]
    if card[0] == 0:
        return f"♡ {value}"
    elif card[0] == 1:
        return f"♠ {value}"
    elif card[0] == 2:
        return f"◇ {value}"
    elif card[0] == 3:
        return f"♣ {value}"
    
    return 

def show_player_hand(player:Player):
    #카드 데이터를 포매팅해서 보여준다. 
    for i in player.hand:
        print(f"{player.hand.index(i)}: {suitFormater(i)}")
        
    
    return

def is_playable_card(card:tuple,reference:tuple):
    if card[0] == reference[0] or card[1] == reference[1] or card[1] == 11:
        return True
    return False

def is_valid_card_index(player:Player,input):
    if len(player.hand)-1 < input:
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
    if user.checkIdx(game.top) == -1: #낼 카드가 없다면
        user.hand.append(game.draw())
        print("")
        if user.checkIdx(game.top) != -1: #뽑은 카드를 낼 수 있다면
            game.top = user.hand.pop(int(user.checkIdx(game.top))) #그걸 낸다. 
            
            print("유저가 자동으로 뽑은 카드 내기")
        game.turn = not game.turn
    
    
    
    else:   
        command = (input(f"Enter card index (0–{len(user.hand)}) or q (quit):"))
        
        if command == "q":
            quit()
        
        if not command.isdigit(): 
            print("Invalid input...")
            return

        command = int(command)

        if not is_valid_card_index(user,command): #덱에 없는 카드 인덱스를 선택하면
            print("Not Valid Index. Try again. ")
            return

        if not is_playable_card(user.hand[int(command)],game.top): #낼 수 없는 카드를 선택하면
            print("This card is not playable.")
        
        else:
            if user.hand[command][1] == 10: #S카드이면 내기만 하고 순서는 안 바꾸기
                game.top = user.hand.pop(int(command))
            elif user.hand[command][1] == 11: #W 카드이면 W카드 절차 밟고 순서 바꾸기
                user.hand.pop(int(command))
                game.wild(False,user)
                game.turn = not game.turn
            else:
                game.top = user.hand.pop(int(command)) #일반 카드이면 내고 순서 바꾸기
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
    if computer.checkIdx(game.top) == -1:
        computer.hand.append(game.draw()) #덱에서 하나 뽑고
        show_game_state(game)
        show_player_hand(computer)
        print("No card playable, Getting one card from the Deck. ")
        if computer.checkIdx(game.top) != -1: #다시 체크했을 때 낼 카드가 있으면
            print(computer.checkIdx(game.top))
            game.top = computer.hand.pop(int(computer.checkIdx(game.top))) #그걸 자동으로 낸다. 
            
            print("The card is automatically Played. ")
        game.turn = not game.turn # 차례 바꾸기
        
            
        print("자동으로 순서 넘어감\n")

    else: #낼 카드가 있다면
        command = computer.checkIdx(game.top) #컴퓨터가 알아서 골라서 낸다. 

        
        if computer.hand[command][1] == 10: #낸 카드가 s카드라면
            game.top = computer.hand.pop(int(command)) #내기만 하고 순서는 안 바꾼다. 
        if computer.hand[command][1] == 11: #낸 카드가 wildcard면
            computer.hand.pop(int(command)) 
            game.wild(True,computer)
            game.turn = not game.turn
        else:
            game.top = computer.hand.pop(int(command))
            game.turn = not game.turn
        
    print("")
    return

#0이면 유저 승, 1이면 컴퓨터 승, 2이면 무승부. 
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
    
#승자를 축하하는 문구를 띄우는 함수
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

#덱에 카드가 더 이상 없을 떄 진행하는 절차, 유저 카드 개수와 컴퓨터 카드 개수를 비교하여 승자를 가린다. 
def noCardInDeck(user:Player,computer:Player) -> None:
    userCard = len(user.hand) #유저 카드 개수
    computerCard = len(computer.hand) #컴퓨터 카드 개수

    if userCard > computerCard:
        win(0) #유저가 많으면 유저 승
    elif userCard < computerCard:
        win(1) #컴퓨터가 많으면 컴퓨터 승
    else: #두 플레이어 카드 개수가 같다면
        win(2) #무승부
    
    return
    
def main() -> None:   

    user = Player()
    computer = Player()
    game = Game()
    game.updateDeck(make_deck()) #덱 만들기
    make_initial_card(game.Deck,user) #유저 6장 뽑기. 
    make_initial_card(game.Deck,computer) #컴퓨터 6장 뽑기
    game.makeTopCard() #Top Card 만들기
    print("Welcome to One card Game! Select Game Mode. (Play Mode:0 Debug Mode:1)")
    while True:
        modeIdx = input("Enter GameMode:")
        if not modeIdx.isdigit():
            print("Not Valid Input. ")
        else:
            game.mode = int(modeIdx) == 1
            break

    while True:
        #덱이 비었으면 대결 상대끼리 남은 카드 개수 비교하는 
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
            
                
        
            


        

        
        


    
        

        