# Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik.
# Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz.

# Buning uchun biz input() funktsyasidan foydalanamiz.

ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)

# Yuqoridagi dastur, avval 1-qatorda foydalanuvchining ismini so'raydi.
# Foydalanuvchi ismini kiritib, Enter tugmasini bosgach, foydalanuvchi kiritgan matn
# ism degan o'zgaruvchiga yuklanadi va dasturining 2-qatori bajaradi:

# Keling yuqoridagi kod va uning natijasini chiroyliroq ko'rinishga keltiramiz.

ism = input("Familiyangiz nima? >>>")
print("Assalom alaykum, " + ism.title())

# Quyidagi mashqlarni bajarib ko'ramiz:
#
# Quyidagi o'zgaruvchilarni yarating:
#
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
#
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang.
# Va avvalgi mashqni takrorlang.
#
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
#
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
#
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

kocha = "....."
mahalla = "....."
tuman = "......"
viloyat = "......"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaramiz:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'raymiz.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: >>>")
mahalla = input("Mahallangiz: >>>")
tuman = input("Tumaningiz: >>>")
viloyat = input("Viloyatingiz: >>>")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozamiz
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklaymiz
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ramiz.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
