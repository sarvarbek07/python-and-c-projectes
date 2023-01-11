# import turtle

# wn = turtle.Screen()
# tr = turtle()
# wn.title("birnarsa")

# colors = ["blue","red","pink","orange","green"]
# tr.shape("arrow")
# tr.width(10)
# tr.speed(0)
# f = 300
# r = 220
# f += 5
# r += 5
# for i in range(len(colors)):
#     r = 120 - 1
#     tr = 120 - 1
#     tr.width(3)
#     tr.forward(f)
#     tr.right(r)
#     tr.color(colors[i])

# wn.mainloop()



# from calendar import c
# from this import d














# s = input('ismingiz nima:')
# print('{0} siz bilan tanishganimdan xursandman'.format(s))
# a = input('siz qayerliksiz:')
# print('men {} haqida ko`p eshitganman'.format(a))
# b = input('hozir qayerda yashaysiz:')
# print("ha {} yaxshi joy deb eshitganmandsad".format(b))






















from calendar import c
from random import randint

a = randint(1,200)
b = randint(1,200)

c = input('{}+{}='.format(a,b))

if c == (a+b):
    print('to`g`ri')
else:
    print('xato')








# from calendar import c
# from random import randint
# kod = randint(1,10)
# c = (5)
# a = (3)

# print(kod)
# if c == kod:
#     print("yutdingiz :)")
# elif a == kod:
#     print('yutdingiz :)')
# else:
#     print("ya`na urinib ko`ring :(")


# from datetime import datetime

# sana = input("tug`ilgan yilingizni kiriting: ")
# bugun = datetime.today()
# natija = bugun.year - int(sana)
# print('natija {}'.format(natija))