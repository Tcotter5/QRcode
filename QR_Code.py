#pip install qrcode
import qrcode

#version is an integer, options of 1-40 available
#error_correction has 4 options each with a % difference in error correction (m is default)
#box size controls how many pixles each box of QR code is

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=70, border=3)
qr.add_data("https://tcotter5.github.io/")
qr.make(fit=True)

#color, can also use RGB color tuples
image = qr.make_image(fill_color="black", back_color="white")
image.save("TC_website.png")