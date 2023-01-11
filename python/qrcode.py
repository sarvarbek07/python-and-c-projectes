import qrcode

img = qrcode.make('hello world')
img.saved('save.png')
# img.show('save.png')