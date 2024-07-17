# 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 리스트로 반환하는 함수 작성

numbers = [100, 200, 300]
def jw_1(a):
    result = []
    for a in numbers:
        b = int(a * 1.1)
        result.append(b)
    return result
print(jw_1(numbers))


# var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def jw_2(a):
#     result = 0
#     for i in a:
#         result = result + i
#     avr = result / len(a)
#     return avr
# var = list(range(2, 99999))
# print(jw_2(var))