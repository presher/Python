import qrcode
from PIL import Image

# Phone number to be encoded
number = '0000000000'
phone_number = f"tel:{number}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(phone_number)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')
img_path = f"../../qr-codes/{number}call_qr_code.png"
img.save(img_path)

img_path
