
# 모듈 (Module)

# 입력을 받는 기능을 하는 함수
def ret_input():
    print("1. 만난다 / 2. 안만난다")
    inp = int(input("입력 : "))
    return inp

# 선택에 대한 분기하는 함수
def if_show(inp):
    if inp == 1:
        print("해피 엔딩")
    elif inp == 2:
        print("새드 엔딩")
    else:
        print("게임 오버")

# 돈 복사 함수
def ret_inputCash():
    cash = int(input("돈 입력 >> "))
    print("현재 소지중인 금액 [ {0} ]" .format(cash))
    return cash

def cash_multiply(cash):
    cash = cash * 3
    return cash