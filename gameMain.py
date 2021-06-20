
# 사용할 모듈을 임포트
import gameFunction

# gameFunction.을 사용하기 싫다면
from gameFunction import ret_inputCash, cash_multiply

print("게임 시작")
print("누구를 만났습니다...")
input()
print("과연 누구를 만났을까요?")
input()

# 입력 담당하는 기능
select = gameFunction.ret_input()

# 입력 값을 넣었을 때
gameFunction.if_show(select)


# 돈을 입력하는 함수 + 넣은 돈 출력
myCash = ret_inputCash()

# 그 돈을 넣으면, 3배로 뻥튀기 해주는 기능
print("수리수리 마수리 ~~ (엔터)")
input()
myCash = cash_multiply(myCash)
# 넣은 돈과 뻥튀기 된 돈 출력
print("복사된 내 돈 [ {0} ]" .format(myCash))