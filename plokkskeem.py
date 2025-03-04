
#1variant ul 4
try:
    K = 15
    M = 3
    aeg = 1
    if K < -1:
        print("viga")
    else:
        podhod= (K + M - 1 )// M
        print("podhodov", podhod)
except:
    print("viga ")

#2 variant ul 1

sum = 0 
N=int(input("sisesta number: "))
for i in range (N):
    num = int(input(f"sisesta arv {i+1}: "))
    if num>0:
        sum += num
        print("summa on", sum)

#4 variant ul 2
vastus=0
p=int(input("mitu korda kordame?"))
while True:
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
    p-=1
    if p==0:break
print("Vastus on", vastus)




#5 variant ul 3
for o in range(20):
    print(f"sooritab eksamit {o+1}. opilane")
    for e in range(3):
        print(f"{e+1}. eksam")

