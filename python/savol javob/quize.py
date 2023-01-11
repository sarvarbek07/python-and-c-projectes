a={"O`zbekiston poytaxt qayer: ":"toshkent","eng katta davlat: ":"rossiya"}
for i in a.keys():
    s=input("{0}".format(i))
    if s==a[i]:
        print("to`g`ri")
    else:
        print("noto`g`ri")