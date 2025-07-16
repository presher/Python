import qrcode
from PIL import Image

# File paths
qr_output_path = "/handyman-wrench-hammer.png" 
icon_path = "/Documents/python/qr-code/hammer-wrench-icon.png"  # Update if you move it

# Create QR code with high error correction
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
data = "tel:+0000000000"
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load and resize the icon
icon = Image.open(icon_path).convert("RGBA")
qr_width, qr_height = qr_img.size
icon_size = int(qr_width * 0.25)
icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

# Create white background behind the icon
white_bg = Image.new("RGBA", icon.size, (255, 255, 255, 255))
icon_with_bg = Image.alpha_composite(white_bg, icon)

# Paste icon with white background in center of QR
pos = ((qr_width - icon_size) // 2, (qr_height - icon_size) // 2)
qr_img.paste(icon_with_bg, pos, mask=icon_with_bg)

# Save final QR code
qr_img.save(qr_output_path)
