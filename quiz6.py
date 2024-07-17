# 홀수/짝수 판별기 함수
# 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수 작성
# 반환되는 값은 '홀수' 또는 '짝수'이다.

def jw_1(a):
    result = ""
    if a % 2 == 1:
        result = "홀수"
    else:
        result = "짝수"
    return result
num = int(input("숫자를 입력하세요: "))
print(jw_1(num))

