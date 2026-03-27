# for takrorlash amaliyoti
for i in range(5):
    print(i)
# natija-> 0 1 2 3 4

# 1-dan 10-gacha chiqaradi
for i in range(1, 11):
    print(i)
# natija-> 1 2 3 4 5 6 7 8 9 10

# 2-qadam tashab sanaydi
for i in range(2, 11, 2):
    print(i)
# natija-> 2 4 6 8 10

# list ichidagi mevalarni consolga chiqaradi
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# natija-> apple
#          banana
#          cherry

# har bitta harfni consolga chiqaradi
word = "hello"
for letter in word:
    print(letter)
# natija->h
#         e
#         l
#         l
#         o


# 1-6 gacha qo'shib natijasini chiqaradi
summa = 0

for i in range(1, 6):
    summa += i

print(summa)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(3):
    for j in range(3):
        print(i, j)

numbers = [1, 5, 8, 10, 3]

for num in numbers:
    if num > 5:
        print(num)

student = {
    "name": "Ali",
    "age": 20,
    "city": "Tashkent"
}

for key, value in student.items():
    print(key, ":", value)

for i in range(1, 11):
    print(i, "->", i*i)