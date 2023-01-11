# while(True):
#     a=str(input("biron sonni kiriting:"))
#     b=len(a)
#     c=a%10
#     print(b)
#     print(c)



while(True):
    x=str(input("bu generator ko`plab xonali sonlarni  boshidagi va oxiridagi raqamlarni topib  va ko`paytirib beradi: "))
    if len(x)==1:
        print("bir xonali son mumkin emas")
        break
    s=int(x)
    f=len(x)
    v=int(10**f)
    v=v*0.1
    a=s//v
    d=s%10
    n=a*d
    print('oxirgi raqam: {}'.format(d))
    print("birinchi raqam: {}".format(a))
    print("ikki raqam ko`paytmasi: {}".format(n))








# a=int(x//1000)
# b=int(x%10)
# c=a*b

# print(c)





# x=int(input())
# a=x//1000
# b=x%10
# c=a*b

# print(c)
# print(a)
# print(b)