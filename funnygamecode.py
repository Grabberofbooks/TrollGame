from random import randint


class Game:
    def game(self):
        ot = int(input("Выбери от кого-го числа угадывать:"))
        do = int(input("Выбери до кого-го числа угадывать:"))
        user = int(input(f"Угадайте число от {ot} до {do}:"))
        choose = randint(1, 2)
        scam = randint(1, 10000)
        randomnum = user + scam
        while ot > randomnum or randomnum > do or randomnum == user:
            if randomnum < ot:
                randomnum += 1
            elif randomnum > do:
                randomnum -= 1
    def __str__(self):
        return "Крутая игра сделанная за 5 минут"

Gamer = Game()

print(Gamer)
