#4 variant 3 ul
sobrad = int(input("sisesta soprade arv: "))
loeb = 0

for i in range(sobrad):
    vanus = int(input(f"sobra {i + 1} vanus: "))
    if vanus > 16:
        loeb += 1

print(f"ohtusoogile paaseb {loeb} sopra.")

#1variant ul 4
try:
    K = 15
    M = 3
    aeg = 1
    if K < -1:
        print("viga")
    else:
        podhod= (K + M - 1 )// M
        jaak=K%M
        print("podhodov", podhod)
except:
    print("viga ")



#2 variant ul 1
try:
    sum = 0 
    N=int(input("sisesta number: "))
    for i in range (N):
        num = int(input(f"sisesta arv {i+1}: "))
    if num>0:
        sum += num
        print("summa on", sum)
except:
    print("VIGA")

#4 variant ul 2
try:
    vastus=0
    p=int(input("mitu korda kordame?"))
    while True:
        arv=float(input("Sisesta arv: "))
        if arv<0: vastus+=arv
        p-=1
        if p==0:break
        print("Vastus on", vastus)
except:
    print("Viga")




#5 variant ul 3
for o in range(20):
    print(f"sooritab eksamit {o+1}. opilane")
    for e in range(3):
        print(f"{e+1}. eksam")

 #V4 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.
vastus=0
P=int(input("Mitu korda kordame?"))
while True:
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
    P-=1
    if P==0: break
print("Summa on: ",vastus)

vastus=0
P=int(input("Mitu korda kordame?"))
for i in range(P):
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
print("Summa on: ",vastus)


#V1 4.(3) Koostage plokkskeem kotlette praadiva roboti jaoks.
kokku=int(input("Kokku kotlete: "))
panni_maht=int(input("Panni maht: "))
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0: lahenemine+=1
print(f"Praeme. Tuleb {lahenemine} lahenemist.")
for l in range(lahenemine):
    if jaak>0 and l==lahenemine-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {panni_maht} kotlet.")
    print(f"{l+1}. lahenemine. Praeme esimene pool.")
    sleep(aeg)
    print("Ümberpöörame")
    print(f"{l+1}. lahenemine. Praeme teine pool.")
    sleep(aeg)
    print(f"Valmis!")

print("Kõik kotletid on praetud!")
