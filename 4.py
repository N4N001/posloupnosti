n1=0
n2=1
x=input("Kolik čísel vypsat? (pokud zadáš liché číslo vypíše o jedno navíc)")
x=int(x)
if x%2==1:
    x=x+1
x=int(x/2)
for i in range(x):
    print(n1)
    n1=n1+n2
    print(n2)
    n2=n1+n2
input()