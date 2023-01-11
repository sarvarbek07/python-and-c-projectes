import time

def con(a,b=0):
    for i in range(b,a+1):
        print(i)
        time.sleep(0.5)
    print("done")
con(30,15)