# STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri.
# Avvalgi darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun
# matn qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

shahar = "Chust shahar"
viloyat = 'Namangan viloyatidan'
print(shahar)
print(viloyat)

# Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan iborat bo'lishi mumkin
# (jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli emoji-smayliklar).

matn = "yangi 📱 oldim"
print(matn)

# Matnlarni qo'shish uchun '+' operatoridan foydalanmiz:

ism = 'Azizbek'
print('Mening ismim ' + ism)
print('Meni ismimni ' + ism, 'deb katta bobom qo\'yganlar')

ism = 'Abdulaziz'
familiya = 'Yoqubjonov'
print('Meni ism familiyamni ' + familiya + ism , 'deb katta bobom qo\'yganlar')

#Yuqoridagi kodda ism va familiya orasiga bo'shliq belgisini qo'shmaganimiz uchun
# ikki matn qo'shilib yozildi. Buni to'g'rilash uchun, 3-qatorni quyidagicha yozamiz:

ism = 'Abdulaziz'
familiya = 'Yoqubjonov'
print('Meni ism familiyamni ' + familiya + ' ' + ism , 'deb katta bobom qo\'yganlar')

# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan
# f"{matn1} {matn2}" ham foydalansak bo'ladi:
# Misol:

ism = "Ahmad"
familiya = 'Qodirov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)
print('Do\'stimni ism sharifi ' + ism_sharif)

# bu usul bilan uzun matn yozish ham mumkin:

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# Matnga bo'shliq qo'shish uchun \t belgisidan,
# yangi qatordan boshlash uchun \n belgisidan foydalanamiz:

print('Salomat bo\'ling!')
print('Salomat \tbo\'ling!')
print('Salomat \nbo\'ling!')

# Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud.
# Bunday amallar to'plami metodlar deb ataladi.

# Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi.
# Keling shunday metodlarning ba'zilari bilan tanishaylik.

# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.

ism = 'Ahmad'
familiya = 'Qodirov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi

ism = 'Ahmad'
familiya = 'Qodirov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.

ism = 'Ahmad'
familiya = 'Qodirov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.title())

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.

ism = 'Ahmad'
familiya = 'Qodirov'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.capitalize())

# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin
# (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)

# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#
# lstrip() — matn boshidagi bo'shliqni,
#
# rstrip() – matn oxiridagi bo'shliqni,
#
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

# Misol:

meva = "     olma     "
print("Men " + meva.lstrip() + "ni yaxshi ko'raman")
print("Men " + meva.rstrip() + "ni yaxshi ko'raman")
print("Men " + meva.strip() + "ni yaxshi ko'raman")
print("Men " + meva + "ni yaxshi ko'raman")

# MUHIM QOIDA!!!
# Metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi!

