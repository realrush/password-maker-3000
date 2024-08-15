import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifrenizin kaç harf olmasini istersiniz?"))

sifre = ""
for i in range(sayi):
    sifre += random.choice(karakterler)

print(sifre)
