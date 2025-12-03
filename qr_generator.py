import qrcode
url = input("Enter Your URL ✏️ : ")
filepath = 'D:\qrcode.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(filepath)

print('Qr Generated Successfully..')

