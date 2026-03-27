# for BILAN TANISHAMIZ

# Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin.
# Masalan ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki
#  bo'lmasa har bir elementni kvdartaga oshirish va boshqalar.

# Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi.

# Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz.
# Buning uchun quyidagi kodni yozamiz:

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)

# 1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan to'ldirdik.
# 2-qatorda for tsiklini bog'ladik. Bu qator Pythonga mehmonlar degan ro'yxatdan har bir elementini olib uni yangi,
# mehmon degan o'zgaruvchiga yuklashni buyuryapti (o'zgaruvchiga istalgan nom berishingiz mumkin.
# Biz tushunarli bo'lishi uchun mehmon deb atadik).
# 3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik.
# Bu tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.

# muhim eslatma ;
# "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.

# Yuqoridagi kodni oddiy tilga tarjima qilsak
# "Mehmonlar ro'yxatidagi har bir mehmon uchun uning ismini konsolga chiqar" degan ma'noni beradi.
# biz python tilida qod orqali gaplashayotganimizni bir misoli

# bir misolda for qanday ishlashini ko'ramiz

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")

#     Natijada for tsikli orqali 5 marta takrorlanadi

# tushuntirishlar
# Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi.
# Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi.
# Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi.
# Tsikl boshlanishi ikki nuqta (:) bilan tugaydi.
# Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.

# Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi
# asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi.
# Agar biz mana shu surilishni tark qilsak kodimiz xato beradi:

# keling bir misol ko'ramiz
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")

# ko'rdingizmi xatolik berdi
# endi to'g'rilaymiz

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi\n")

# endi ishladi

# for yordamida sonli ro'yhatlar bilan ishlaymiz

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

#     bu yerda hozir biz sonlar degan ro'yxatga list range berib son kiritdik va
#     for bilan ro'yxat ichidagi sonlarni 2ga ko'paytir dedik va u for bilan 10 marta chiqardi

# for yordamida yangi bo'sh ro'yhat shakillantirish mumkin
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)

# for bilan input ishlatilishi
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)

# qodni tahlil qilib ko'ramiz

# 1-qatorda bo'sh dostlar ro'yxatini yaratdik
#
# 2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik
#
# 3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar ketma-ketligini yaratadi
# (0,1,2,3,4) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi.
#
# 4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik.
# Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi,
# foydalanuvchiga tushunarli bo'lishi uchun esa biz
# "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.
#
# 5-qatorda shakllangan ro'yxatni konsolga chiqardik.









