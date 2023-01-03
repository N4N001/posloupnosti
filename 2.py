a1=52
a2=49
diff=a2-a1
print("Další člen je od členu před ním jiný o ",diff)
print("Kolikátý člen hledáš?")
n=int(input())
m=n-1
k=diff*m
vysledek=a1+k
print(vysledek)
soucet=(int(n/2)*(a1+vysledek))
print(soucet)
input()