dosya = open(r"D:\ibrahim_ediz\Ornekler\deneme.txt","r+",encoding='UTF-8')
metin = dosya.read()
dosya.seek(0)
metin2 = dosya.read()

dosya.seek(0)
print(dosya.read())
dosya.seek(0)
print(dosya.readline())
dosya.seek(0)
print(dosya.readlines())
dosya.writelines(["\nNECİP FAZIL KISAKÜREK"])

dosya.close()
input()


