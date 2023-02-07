for i in range(50):
    print('*', end='')
print("\n\t\tKonverter Suhu")
for i in range(50):
    print('*', end='')

print('\nPilihan konverter : \n 1) Celcius ke Fahrenheit \n 2) Fahrenheit ke Celcius \n 3) Celcius ke Kelvin \n 4) Kelvin ke Celcius')
for i in range(50):
    print('*', end='')
    break
for i in range(50):
    print('*', end='')
print('')
for i in range(51):
    print('*', end='')

def celcius_fah():
    p=float(input("suhu Asal Celcius = "))
    x=(9/5*p)+32
    print("suhu Hasil = ", x,"Fahrenheit")
def fahren_cel():
    p=float(input("suhu Asal Fahrenheit = "))
    x=5/9*(p-32)
    print("suhu Hasil = ", x,"Celcius")
def celcius_kel():
    p=float(input("suhu Asal Celcius = "))
    x=p+273.15
    print("suhu Hasil = ", x,"Kelvin")
def kel_cel():
    p=float(input("suhu Asal Kelvin = "))
    x=p-273.15
    print("suhu Hasil = ", x,"Celcius")

a=int(input("\nPilihan Konverter : ") )

if a==1:
    celcius_fah()
elif a==2:
    fahren_cel()
elif a==3:
    celcius_kel()
elif a==4:
    kel_cel()
else :
    print("Tidak ada dalam pilihan \n PROGRAM SELESAI")