#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
'''
i=1
while i <= 5:
    print(i,0)
    i=i+1
'''
'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''


'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
'''
product = 1
for i in range(1,10):
    product*=i
    print (product)
'''
'''
Задача 5

Вывести цифры числа на каждой строчке.
'''
'''''
integer_number = 2129

print(integer_number%10,integer_number//10)

while integer_number>0:
    print (integer_number%10)
    integer_number = integer_number//10
''''''

''''''
Задача 6

Найти сумму цифр числа
'''
'''''
num = 102030
sum = 0
while num>0:
    sum += num%10
    num = num//10
print(sum)
'''
'''
Задача 7

Найти произведение цифр числа.
'''
'''
num = 112233
n = 1
for i in str(num):
    n *= int(i)
print(n)
'''

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?

integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''

#Задача 9

#Найти максимальную цифру в числе
'''
integer_number = 2129
num = 0
while integer_number>0:
    if integer_number%10 > num:
        num = integer_number%10
        integer_number = integer_number//10
print(num)
'''





#Задача 10

#Найти количество цифр 5 в числе
'''numer =5656
n = 1
for i in str(numer):
    if numer == 5:
        n+=str(i)
print(n)
'''