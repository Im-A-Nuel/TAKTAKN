def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
    print('Rp ' + formatrupiah(q) + '.' + p)
    
print(" ****************************** \n SISTEM UPAH YANG HARUS DIBAYAR \n -------------------------------")

a=input("Nama \t\t: ")
b=str(input("Jenis Kelamin \t: "))
c=int(input("Umur \t\t: "))
d=int(input("Hari Kerja \t: "))
e=d*700000
f=d*750000
g=d*800000
h=d*850000

if b=="Pria" and c>=18 and c<30:
  print("Jumlah Total Upah Yang Diterima : ", formatrupiah(e))
elif b=="Wanita" and c>=18 and c<=30:
  print("Jumlah Total Upah Yang Diterima : ", formatrupiah(f))
elif b=="Pria" and c>=30 and c<=40:
  print("Jumlah Total Upah Yang Diterima : ", formatrupiah(g))
elif b=="Wanita" and c>=30 and c<=40:
  print("Jumlah Total Upah Yang Diterima : Rp. ", formatrupiah(h)) 
