# 리스트 변수의 평균 값을 구하는 함수 작성
# 리스트의 길이는 매번 달리질 수 있음에 유의하고, sum() 함수를 사용할 수 없다.
# var = []
# var_1 = []
# def jw_1(var, var_1):
#     result = ((var * var_1)/2)
#     print(result)
#     return result
# jw_1(10, 20)

var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def jw_2(a):
    result = 0
    for i in a:
        result = result + i
    avr = result / len(a)
    return avr
var = list(range(2, 99999))
print(jw_2(var))



