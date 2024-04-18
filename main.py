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
input = input("select a fruit:")
hasFruit = False
for fruit in fruits:
    if fruit == input:
        print("there you are, one",input)
        hasFruit = True
        break


if not hasFruit:
    print("sorry, we dont have such fruit")