import qrcode
import os

def generate_qr_code(email):
    """Generates and saves a QR code for an email 'mailto' link."""
    # Email details
    subject = "Insurance Questions"
    body = "I have questions about Insurance. \nMy phone number is: \nmy email is:"
    
    # Encode email details as a mailto link
    mailto_link = f"mailto:{email}?subject={subject}&body={body}"
    
    # File path for saving the QR code
    filename = f"../../qr-codes/{email}_qrcode.png"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mailto_link)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

    print(f"QR Code saved at: {filename}")

if __name__ == "__main__":
    email = "gmail@gmail.com"
    generate_qr_code(email)
