from random import choice, randint

harf = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
        'J','K','L','M', 'N', 'O', 'P', 'R','Q',
        'S', 'T', 'U', 'W', 'X', 'Y', 'Z'
    ]


print('Salom Men mashinangiz uchun chiroyli raqamlarni generatsiya qilib beraman :)')
tarif_sorovi = input('Sizni qaysi tarifdagi raqamlar qiziqtiradi Premum/Gold/Silver/Bronze/StepByStep/Simple ')
shahar_codi = input('Shahar kodini kiriting ')

def GenerateNumber():
# 00 A 123 NN UZ
    i = 0 
    while True:
        i += 1
        def seria_1():
            a = choice(harf)        
            return a    
        def seria_2():
            h1 = choice(harf)
            h2 = choice(harf)
            return h1, h2
        def number():
            c = randint(100,999)
            a = str(c)
            return a
        serias_1 = seria_2()[0]
        serias_2 = seria_2()[1]
        numberList = number()
        n0 = int(numberList[0])
        n1 = int(numberList[1])
        n2 = int(numberList[2])
        def Premum(): # 777 AA
            if n0 == n1 and n2 and n2 == n1 and serias_1 == serias_2:
                a = f'{n0}{n1}{n2}'
                print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')

        def Gold(): # 771 AA
            if n0 == n1 and n2 != n0 and serias_1 == serias_2:
                a = f'{n0}{n1}{n2}'
                print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')

        def Silver(): # 771 AB
            if n0 == n1 and n2 != n0 and serias_1 != serias_2:
                a = f'{n0}{n1}{n2}'
                print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')

        def Bronze(): #707 AB
            if n0 == n2 and n0 != n1 and serias_1 != serias_2:
                a = f'{n0}{n1}{n2}'
                n = print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')
                return n
        def StepByStep(): #123 AN
            f = n0
            s = f + 1
            t = s + 1
            a = f'{f}{s}{t}'
            if len(a) >= 4:
                print (f'{shahar_codi} {seria_1()} {a[:3]} {serias_1}{serias_2}')
            else:
                print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')
        def Simple(): #135 AL
            if n0 < n1 < n2 and serias_1 != serias_2:
                a = f'{n0}{n1}{n2}'
                n = print(f'{shahar_codi} {seria_1()} {a} {serias_1}{serias_2}')
                return n

        if tarif_sorovi.lower() == 'premum':
            Premum()
        elif tarif_sorovi.lower() == 'gold':
            Gold()
        elif tarif_sorovi.lower() == 'silver':
            Silver()
        elif tarif_sorovi.lower() == 'bronze':
            Bronze()
        elif tarif_sorovi.lower() == 'stepbystep':
            StepByStep()
        elif tarif_sorovi.lower() == 'simple':
            Simple()

        if i == 10000: #loop == 10 000
            break

GenerateNumber()     
for i in range(10):
    s = input('Generate qilingan raqam yoqdimi ? siz boshqa raqamlarni ham korishni hoxlaysizmi ? xa / yoq ')   
    if s == 'xa':
        GenerateNumber()
    elif s == 'yoq':
        input = ('Dasturdan chiqish uchun Enterni bosing :( ')  
        break     
    else:
        print('Bunday Tanlov Yoq!')
        break 