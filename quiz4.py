# 학점 변환기 함수. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 사용자로부터 score를 입력 받아 학점으로 환산하여 반환하는 함수를 작성
# text = input("점수를 입력하세요:")
# def gkrwja_1(a):
#     if int(a) <= 20:
#         print("E")
#     elif int(a) <= 40:
#         print("D")
#     elif int(a) <= 60:
#         print("C")
#     elif int(a) <= 80:
#         print("B")
#     elif int(a) <= 100:
#         print("A")
#     result = a
#     return result
#
# print(gkrwja_1(text))


def gkrwja_1(a):
    result = ""
    if 81 <= a <=100:
        result = "A"
    elif 61 <= a <= 80:
        result = "B"
    elif 41 <= a <= 60:
        result = "C"
    elif 21 <= a <= 40:
        result = "D"
    elif 0 <= a <= 21:
        result = "E"
    return result
text = int(input("점수를 입력하세요: "))
res = gkrwja_1(text)


