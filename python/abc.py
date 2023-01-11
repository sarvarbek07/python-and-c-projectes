# while True:
#     a,b,c=map(int,input().split())
#     if a>b and a<c or a<b and a>c:
#         print(a)
#     elif b>a and b<c or b<a and b>c:
#         print(b)
#     elif c<a and c>b or c>a and c<b:
#         print(b)




# import random

# a=["1","2","3","4","5"]
# random.shuffle(a)
# print(a)


from selenium import webdriver
import time
driver=int(input("enter numter of driver:"))
url=input("enter URL:")
refleshtime=int(input("enter refresh rate in secons:"))
drivers=[]

for i in range(driver):
    drivers.append(webdriver.Chrome(executable_path="chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(refleshtime)
    for i in range(driver):
        drivers[i].refresh()