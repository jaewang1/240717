# 문제 메세지 길이 판별 함수
# 문자 메세지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오.
# 메세지의 길이가 20 이하이면 50원, 20원을 초과하면 100원이다.
# 사용자로부터 문자메세지를 입력 받아서 문자 요금을 반환하는 코드 작성
text = input("길이를 입력하세요:")
def aa_1(a):
    if len(a) <= 20:
        print("50원")
    else:
        print("100원")
    result = a
    return result
aa_1(text)

