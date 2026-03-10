# bu mavzu
#O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy.
# Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani
# esa qiymat deb tasavvur qilish mumkin.
# Pythonda qiymatlar son, matn, ro'yxat va hokazo ko'rinishida bo'lishi mumkin.
# Misol: ism, yosh o'zgaruvchilarni oldik va print ichiga o'sha o'zgaruvchilarni joylashtirdik
#  hamda ekranga o'zgaruvchini ichidagi ma'lumotni chiqardik
ism = "Abdulloh"
yosh = 25
print(ism)
print(yosh)

# (variable) bunday deyilishiga sabab, uning qiymati istalgan vaqt o'zgartirilishi mumkin:
ism = "Abduvohid"
print(ism)
ism="Muhammad"
print(ism)
# Yuqoridagi misolda ism nomli o'zgaruvchiga avval 'Abduvohid' keyin esa 'Muhammad' qiymatlarini berdik.




#  MUHIM QOIDALAR!!!

# O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
#
# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
#
# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
#
# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va
# pastki chiziq (_) qatnashishi mumkin
#
# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
#
# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi
# (ism, ISM, va Ism uchta turli o'zgaruvchi)
#Qo'shimcha qoida sifatida:

# O'zgaruvchi nomini kichik harflar bilan yozing.

# O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (_) bilan
# ajrating (ism_sharif="Anvar Narzullaev")

# O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas davlat = "Korea" va hokazo)

# Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va
# maxsus kalit so'zlarning (keywords) nomini bermang.

# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
matn = "Hello World!"
print(matn)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "Assalom alaykum"
print(xabar)

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# O'zgaruvchini class deb nomlash mumkin emas, sababi class bu maxsus kalit so'z.

#Quyidagi kodni bajaring
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
