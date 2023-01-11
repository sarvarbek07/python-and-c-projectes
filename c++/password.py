a=int(input())
j=str(a)
p=len(j)
r=0
while a>0:
    d=a%10
    r=r+d
    a=a//10

if p==9 and r%2==1:
    print("yes")
else:
    print("no")