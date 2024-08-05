first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
a = first
b = second
c = third
if a == b == c:
    print('3')
elif a == b or b == c or a == c:
    print ('2')
else: # a != b != c:
    print(0)
