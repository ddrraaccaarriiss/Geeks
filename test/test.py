
def area(x1, y1, x2, y2, x3, y3):
    s = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    if s == s:
        with open('area.txt', 'w', encoding='UTF-8') as file:
            file.write(str(s))


def truefalse(x1, y1, x2, y2, x3, y3):
    kv_a, kv_b, kv_c = (x2 - x1) ** 2 + (y2 - y1) ** 2, (x3 - x2) ** 2 + (y3 - y2) ** 2, (x1 - x3) ** 2 + (y1 - y3) ** 2

    if kv_a > kv_c:
        kv_a, kv_c = kv_c, kv_a

    if kv_b > kv_c:
        kv_b, kv_c = kv_c, kv_b

    if kv_a + kv_b == kv_c:
        with open('truefalse.txt', 'w', encoding='UTF-8') as file:
            file.write("True")

    else:
        with open('truefalse.txt', 'w', encoding='UTF-8') as file:
            file.write("Fasle")

test1 = truefalse(1, 7, 7,7,1, 1)#  является прямо угольным треугольником
test2 = area(1, 7, 7,7,1, 1)# 18
print("1 задание")
