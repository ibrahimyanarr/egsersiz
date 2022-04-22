Şekil=input("Hangi Şeklin Tipini Öğrenmek İstiyorsunuz?")

if Şekil=="Dörtgen":
    print("Lütfen Kenarları Sırayla Giriniz.")

a=int(input("kenar1:"))
b=int(input("kenar2:"))
c=int(input("kenar3:"))
d=int(input("kenar4:"))

if (a==b and a==c):
    print("KARE")
elif(a==c and b==d):
    print("DİKDÖRTGEN")
else:
    print("DÖRTGEN")


if Şekil=="Üçgen":
    print("Lütfen Kenarları Sırayla Giriniz.")

a=int(input("kenar1:"))
b=int(input("kenar2:"))
c=int(input("kenar3:"))

if(a==b and a==c):
    print("EŞKENAR ÜÇGEN")

elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print("İKİZ KENAR ÜÇGEN")

else:
    print("ÇEŞİT KENAR ÜÇGEN")


