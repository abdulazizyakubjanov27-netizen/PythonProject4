cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

print(sorted(mehmonlar, reverse=True))

# sonli ro'yxatni ham tartiblashishimiz mumkin

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
