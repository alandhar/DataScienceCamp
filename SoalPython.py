print("---Perhitungan FPB dan KPK---")
a = int(input("Masukkan Angka Pertama: "))
b = int(input("Masukkan Angka Kedua: "))

def fpb(a, b):
  if b == 0: return a
  else: return fpb(b, a % b)

def kpk(a, b):
  return a / fpb(a, b) * b

print(f'\nFPB dari kedua angka adalah {fpb(a,b)}')
print(f'KPK dari kedua angka adalah {kpk(a,b)}')


def konvertRomawi(num):
    romawi = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    angka = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    index = 0
    result = ""
    while num >= 1:
        tempres = int(num/angka[index])
        for i in range(tempres):
            result += romawi[index]
        num %= angka[index]
        index += 1
    return result

print("\n---Konversi Desimal ke Romawi---")
number = int(input("Masukkan angka: "))
print(konvertRomawi(number))