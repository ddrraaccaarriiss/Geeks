t = []
n = int(input('Введите количество круга: '))
for i in range(n):
    m = input('Введите час, минуту и секунду  через пробел: ')
    t.append(m)
print(sorted(t,reverse=True))



