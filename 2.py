#Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
N = int(input('Введите число '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f

    print(f, end=" ")
