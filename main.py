print("sveiki")

#print(list(range(1,10)))
numbersSequence = range(100, 110)
print(list(numbersSequence))
for i in numbersSequence:
    print("spausdiname ")
    print(" dar")
    print("kart")
print("po visko")

for i in numbersSequence:
    print(i)


#           0           1       2
fruits = ["apple", "banana", "cherry","pineapple","plum","kiwi"]
print(fruits)
for fruit in fruits:
  print(fruit.upper())
print("----------------------")
skaiciai = [100, 101, 102, 4, 5, 6, 7, 8, 9]
for number in skaiciai:
    if number % 2 == 0:
        print(number)
print("po ciklo")

print("----------------------")
for number in skaiciai:
    if number < 100:
        break
    print(number)
print(";)")

print("----------------------")
for number in skaiciai:
    if number % 2 == 0:
        continue
    print(number)
print(";)")
print("----------------------")
fruits = ["apple", "banana", "cherry","pineapple","plum","kiwi"]

for fruit in fruits:
    if fruit == "pineapple":
        continue
    print(fruit)
print("----------------------")

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
print("----------------------")
# inputStr = input("select a fruit:")
# hasFruit = False
# for fruit in fruits:
#     if fruit == inputStr:
#         print("there you are, one",fruit)
#         hasFruit = True
#         break


# if not hasFruit:
#     print("sorry, we dont have such fruit")

for i in reversed(range(0, 10)):
    print(i)
print("----------------------")

for i in reversed("labas"):
    print(i)

# counter = 0
# while True:
#     counter +=1
#     if counter % 1000000 == 0:
#         print(counter / 1000000)
#     if counter > 14565316:
#         break
#
# prekiu_kiekis = 24
# while prekiu_kiekis > 0:
#     print(f'turimas prekiu kiekis: {prekiu_kiekis}')
#     nupirkta = int(input("Kiek norite nupirkti?"))
#     if nupirkta > prekiu_kiekis:
#         print("deje tiek prekiu neturime")
#         continue
#     print(f'nupirkote: {nupirkta}\n')
#     prekiu_kiekis -= nupirkta
#
# print("prekes isparduotoss")

ct = 0
while True:
    ct += 1
    if ct == 5:
        break
    print("labas",ct)
print("------")
ct = 0
shouldGo = True
while shouldGo:
    ct += 1
    if ct == 5:
        shouldGo = False
    print("labas",ct)

print("------")
#       0,1,2,3,4,5, 6, 7
list = [4,5,6,7,8,21,5]
print(list)
for i in list:
    print(i)

print("------")
print(list[0])# atspausdinti reikme 4
list[0] = 14 # pakeiciu 0-oj pozijijoje 4to reiksme i 14
print(list[0]) # isspausdinu nauja 0os pozicijos reiksme
print(len(list))
print(list[6],"6ta pos")
# print(list[7])
list.append(5)
print(print(7))
del list[7]
print(print(7))
