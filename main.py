# import statistics
#
#
# print("sveiki")
#
# #print(list(range(1,10)))
# numbersSequence = range(100, 110)
# print(list(numbersSequence))
# for i in numbersSequence:
#     print("spausdiname ")
#     print(" dar")
#     print("kart")
# print("po visko")
#
# for i in numbersSequence:
#     print(i)
#
#
# #           0           1       2
# fruits = ["apple", "banana", "cherry","pineapple","plum","kiwi"]
# print(fruits)
# for fruit in fruits:
#   print(fruit.upper())
# print("----------------------")
# skaiciai = [100, 101, 102, 4, 5, 6, 7, 8, 9]
# for number in skaiciai:
#     if number % 2 == 0:
#         print(number)
# print("po ciklo")
#
# print("----------------------")
# for number in skaiciai:
#     if number < 100:
#         break
#     print(number)
# print(";)")
#
# print("----------------------")
# for number in skaiciai:
#     if number % 2 == 0:
#         continue
#     print(number)
# print(";)")
# print("----------------------")
# fruits = ["apple", "banana", "cherry","pineapple","plum","kiwi"]
#
# for fruit in fruits:
#     if fruit == "pineapple":
#         continue
#     print(fruit)
# print("----------------------")
#
# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)
# print("----------------------")
# # inputStr = input("select a fruit:")
# # hasFruit = False
# # for fruit in fruits:
# #     if fruit == inputStr:
# #         print("there you are, one",fruit)
# #         hasFruit = True
# #         break
#
#
# # if not hasFruit:
# #     print("sorry, we dont have such fruit")
#
# for i in reversed(range(0, 10)):
#     print(i)
# print("----------------------")
#
# for i in reversed("labas"):
#     print(i)
#
# # counter = 0
# # while True:
# #     counter +=1
# #     if counter % 1000000 == 0:
# #         print(counter / 1000000)
# #     if counter > 14565316:
# #         break
# #
# # prekiu_kiekis = 24
# # while prekiu_kiekis > 0:
# #     print(f'turimas prekiu kiekis: {prekiu_kiekis}')
# #     nupirkta = int(input("Kiek norite nupirkti?"))
# #     if nupirkta > prekiu_kiekis:
# #         print("deje tiek prekiu neturime")
# #         continue
# #     print(f'nupirkote: {nupirkta}\n')
# #     prekiu_kiekis -= nupirkta
# #
# # print("prekes isparduotoss")
#
# ct = 0
# while True:
#     ct += 1
#     if ct == 5:
#         break
#     print("labas",ct)
# print("------")
# ct = 0
# shouldGo = True
# while shouldGo:
#     ct += 1
#     if ct == 5:
#         shouldGo = False
#     print("labas",ct)
#
# print("------")
# #       0,1,2,3,4,5, 6, 7
# list = [4,5,6,7,8,21,5]
# print(list)
# for i in list:
#     print(i)
#
# print("------")
# print(list[0])# atspausdinti reikme 4
# list[0] = 14 # pakeiciu 0-oj pozijijoje 4to reiksme i 14
# print(list[0]) # isspausdinu nauja 0os pozicijos reiksme
# print(len(list))
# print(list[6],"6ta pos")
# # print(list[7])
# list.append(5)
# print(list[7])
# del list[7]
# list.pop()
#
# print(list)
# # list = [] # isvalome masyva
# # list.clear() # arba taip isvalom
# print(list.pop(2))
# print(list)
#
# dict_pavadinimas = {
# 'savybe1': 'savybes reiksme1',
# 'savybe2': 'savybes reiksme2',
# 'savybe3': 'savybes reiksme3'
# }
# print(dict_pavadinimas["savybe2"])
#
# studentas = {
#     "vardas":"Jonas",
#     "pavarde":"Jankauskas",
#     "amzius": 32,
#     "issilavinimas": "vidurinis",
#     'ugis': 1.85,
#     'disciplinos': {
#         'matematika' : [1,5,9,8,7,6],
#         'fizika' : [10,8,9,8,7,6],
#         'lietuviu' : [1,5,4,7,6],
#     }
# }
# print(studentas['vardas'] + " " + studentas['pavarde'])
# print(statistics.mean(studentas["disciplinos"]['fizika']))
#
# arr2d = [
#     [1,5,10],
#     [7,8,3],
#     [4,15,10]
# ]
# print(arr2d[1][1])
# skaiciai = (4, 7, 8, 5, 4, 6, 8, 4)
# print(skaiciai.index(5))


for i in range(3):# 0,1,2
    print(f'{i+1}-a isorinio ciklo iteracija')
    for a in range(3):# 0,1,2
        print(f'--{a+1}-a vidinio ciklo iteracija')

for i in range(1, 11):
    line = ""
    for a in range(1, 11):
        line += str(i * a) + " "
    print(line)
import random
# Sugeneruokite 300 +
# atsitiktinių skaičių nuo 0 iki 300, +
# atspausdinkite juos atskirtus tarpais +
# ir suskaičiuokite kiek tarp jų yra didesnių už 150. +
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “. +

line = ""
count = 0
for i in range(300):
    rnd = random.randint(0, 300)
    if rnd > 150:
        count += 1
    if rnd > 275:
        line += "[" + str(rnd) + "] "
    else:
        line += str(rnd) + " "
print(line)
print(count)
print("--------------------------")

numbers = [1,5,8,3,4,6,5]
countEven = 0
for number in numbers:
    if number % 2 == 0:
        countEven += 1

print(countEven)

#Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, +
# kurie dalijasi iš 77 be liekanos. +
# Skaičius atskirkite kableliais.
# Po paskutinio skaičiaus kablelio neturi būti.
print("--------------------------")
line = ""
for i in range(1, 3001):
    if i % 77 == 0:
        if 3001 // 77 * 77 == i:
            line += str(i)
            break
        else:
            line += str(i) + ","
print(line[0 : len(line) - 1])

line = ""
for i in range(0, 3001, 77):
    line += str(i) + ","
print(line[0 : -1])