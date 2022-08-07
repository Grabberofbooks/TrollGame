import random



print("Выбери от кого-го числа угадывать")
ot = input()
print("Выбери до кого-го числа угадывать")
do = input()
randomnum = random.randint(int(ot), int(do))





user = input(f"Угадайте число от {ot} до {do}:")
choose = random.randint(1, 2)
scam = random.randint(1, 5)
if int(choose) == 1:
    randomnum = int(user) + int(scam)
    if int(randomnum) > int(do):
       minus = int(randomnum) - int(do) + 1
       randomnum = int(randomnum) - minus
if int(choose) == 2:
    randomnum = int(user) - int(scam)
    if int(randomnum) < int(ot):
        plus = int(ot) - int(randomnum) + 1
        randomnum = randomnum + int(plus)

if int(randomnum) == int(user):
    if int(randomnum) < 100:
        print("Ты угадал, молодец")
    else:
        print(f"Похоже ты обладаешь даром предвидинья, {name}")
else:
    print("Ты не угадал, попробуй еще раз")
    print(f"Число которре было загадано {randomnum}")
print(randomnum)

