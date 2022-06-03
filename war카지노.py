import random
from secrets import choice

#기본금액 1만원, 카드종류
user_money = 10000
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
print("카드게임을 시작합니다.")
print()

def game() :
    global user_money
    #카드 랜덤으로 선택
    pc_card = random.choice(card)
    user_card = random.choice(card)
    
    #카드비교를 위해 인덱스를 비교
    #인덱스가 높을수록 큰 숫자
    pc_card_index = card.index(pc_card)
    user_card_index = card.index(user_card)

    #보유금액 0원일 때 종료
    if(user_money == 0):
        print("돈이 없습니다.")
        return
    
    print("{0} 카드를 받았습니다".format(user_card))
    print("현재 {0} 원을 보유하고 있습니다.".format(user_money))
    bat = int(input("얼마를 배팅하실 껀가요? : "))
    print()
    
    #비기고 Go to war 일때 다시 경기를 해야하기 때문에 while 이용하여 continue로 재경기
    while True:
        #승, 무, 패 결정
        if(pc_card_index < user_card_index):
            user_money += bat
            print("이겼습니다! \n")
        elif(pc_card_index > user_card_index):
            user_money -= bat
            print("졌습니다. \n")
        else:
            print("비겼습니다. 어떻게 하실껀가요? \n")
            while True:
                # 숫자 1, 2를 입력하지 않으면 무한루프, 입력하면 탈출
                try:
                    answer = int(input("1. Go to War, 2. Surrender (숫자입력): "))
                    print()
                    if answer != 1 and answer != 2 :
                        print("1 또는 2 를 입력하세요.")
                        continue
                except:
                    print("숫자를 입력하세요.")
                    continue
                break
            #배팅 금액 그대로 새로 카드 받아 경기
            if(answer == 1):
                pc_card = random.choice(card)
                user_card = random.choice(card)

                pc_card_index = card.index(pc_card)
                user_card_index = card.index(user_card)
                print("재경기 \n")
                print("{0} 카드를 받았습니다".format(user_card))
                continue
            #경기 포기
            elif(answer == 2):
                print("경기를 포기하여 졌습니다. \n")
                user_money -= bat
        break

    #새 게임 시작
    game()

#게임시작
game()
