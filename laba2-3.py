#1
def z1():
a = input("vvedite chiclo")
b = input("vvedite chiclo")
if a == b:
    print("parol prinat")
else:
    print("parol neprinat")


def z2():
    number = str(input("ведите номер места"))
    A = []
    if number % 2 == 0:
        A = ("верхнее боковое")
    else:
        A = ("нижний боковок ")
    if number % 4 == 0:
        A = ("верхний купе")
    else:
         A = ("нижний купе")
    print("тип места")


def z3():
year = int(input("Введите номер года: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Год {year} - високосный")
else:
    print("Этот год не високосный")


def z4():
color1 = input("Введите осн цвет (красный, синий или желтый): ")
color2 = input("Введитеосн цвет (красный, синий или желтый): ")
if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("Фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    print("Оранжевый")
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    print("Зеленый")
else:
    print("Ошибка! Введите только основные цвета: красный, синий или желтый.")


def z2.1():
N = input("ведите колич слов")
a = 1
word = []
while a <= N:
    b = input("ведите словo: ")
    word.append(b)
    a += 1
    c = " ".join(word)
print(c)



def z2.2():
a = 10
b = 1
words = []
while b <= a:
    c = str(input("Введите слово: "))
    if c == "stop":
        break
        words.append(c)
d = ' '.join(words)
print(d)


def z2.3():
a = input("Введите слово: ")
if "ф" in word.lower():
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово")



def z2.4():
import random
c = 0
d = 0
print("математика для детей. Решите пример")
while c < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    e = a + b
    k = int(input("{}+{}=".format(a,b)))
    if k != e:
        print("oshibka")
        c +=1
    else:
        print("pravilno")
        d +=1
print("game over")




