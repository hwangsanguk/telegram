import random


def getLotto():
    winner = [1, 15, 19, 23, 28, 42]

    lotto = sorted(random.sample(range(1,46),6))

    set(lotto) #=> 집합이 됨 => 중복원소가 제거되고, 집합 연산자를 쓸 수 있음

    print(set(winner) & set(lotto))
    print(len(set(winner) & set(lotto)))

    cnt = len(set(winner) & set(lotto))

    if cnt==6:
        print(cnt , '1등입니다')    
    elif cnt==5:
        print(cnt , '3등입니다') 
    elif cnt==4:
        print(cnt,'4등입니다')  
    elif cnt==3:
        print(cnt ,'5등입니다')   
    else :
        print(cnt,'꽝 입니다')  



n = 0
while n < 1000:
    getLotto()
    n += 1