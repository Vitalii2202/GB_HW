# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

var_1 = 54
var_2 = 'kiev'
var_3 = [1, 2, 6, 7, 18]
var_4 = (1, 564, 'total')

print(var_1)
print(var_2)
print(var_3)
print(var_4)

vvod = int(input('Vvedite chislo: '))
print(vvod)

vvod_2 = input('Vvedite stroky: ')
print(vvod_2)


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

vvod_chislo = int(input('Vvedite chislo: '))
print(vvod_chislo)
ch = 0
mm = 0
cc = 0

if vvod_chislo < 60:
    print('{}:{}:{}'.format(ch, mm, vvod_chislo))

elif vvod_chislo >= 60 and vvod_chislo < 3600:
    mm = vvod_chislo // 60
    cc = vvod_chislo % 60
    print('{}:{}:{}'.format(ch, mm, cc))

else:
    ch = vvod_chislo // 3600
    cc_1 = int(vvod_chislo / ch - 3600)
    if cc_1 > 60:
        mm = cc_1 // 60
        cc_1 = vvod_chislo % 60
    print('{}:{}:{}'.format(ch, mm, cc_1))



# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Vvedite chislo: ')
#print(n)
#print(type(n))

nn = n+n
nnn = n+n+n

sum = int(n) + int(nn) + int(nnn)
print(sum)


#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


n = input('Vvedite chislo: ')
vuv = 0
m = 0
i = 0

while len(n) > m:
    if vuv < int(n[i]):
        vuv = int(n[i])
    m += 1
    i += 1

print(vuv)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.


virychka = int(input('Vvedite virychky: '))
izderjka = int(input('Vvedite izderjky: '))

if virychka < izderjka:
    print('Vu rabotaete v minus!!!')
else:
    print('Vu rabotaete v plus!!!')
    pribul = virychka - izderjka
    roi = int((pribul / izderjka) * 100)
    print('Vash ROI:', roi, '%')
    sotrudniki = int(input('Vvedite kolichestvo sotrudnikov: '))
    prib_sotr = int(pribul / sotrudniki)
    print('Pribul na odnogo sotrudnika:', prib_sotr)

# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров
# a и b и выводить одно натуральное число — номер дня.

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

a = 2
b = 3
d = 1
print('1-й день:', a)

while a < b:
    a = a + a*0.1
    d = d + 1
    print(d, '-й день: ', round(a, 2), sep='')

print('Ответ: на ', d, '-й день: ', 'спортсмен достиг результата - не менее ', d, ' км', sep='')
