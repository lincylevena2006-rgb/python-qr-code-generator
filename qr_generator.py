import qrcode

print("================================")
print("       QR CODE GENERATOR")
print("================================")

data = input("Enter text or URL: ")
filename = input("Enter file name: ")

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print("\nQR Code generated successfully! 🎉")
print("Saved as:", filename)