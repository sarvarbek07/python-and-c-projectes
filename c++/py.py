# a,n,s=map(int,input().split())
# print(a+n+s)
# class Car:
#     def __init__(self,tezlik,narx):
#         self.tez=tezlik
#         self.cost=narx

# class Like(Car):
#     pass
# nexia=Like(200,120000000)
# print(nexia.tez,nexia.cost)

import random

a=1
b=100
s=0
n=random.randint(a,b)

while True:
    sa=int(input(f"({a}-{b}) sonlar orasidagi sonni toping:"))
    s+=1
    if sa<n:
        print(F"{sa} kichik")
    elif sa>n:
        print(F"{sa} katta")
    else:
        print(f"{sa} to`g`ri")
        break
print(f"siz {s} urinishda topdingiz")
