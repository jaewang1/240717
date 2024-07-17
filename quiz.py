# 구구단 2-9단을 출력하라. 출력할 때, 2 * 3 = 6과 같이 어떤 값을 곱하였는지도 출력

# data = 0
# while data < 9:
#     data = data + 1
#     data1 = data * 3
#     print("3 x", data, "=", data1)

# print(list(range(1, 10)))
for index in range(2, 10):
    for k in range(1, 10):
        print(index,"x", k, "=", k*index)

