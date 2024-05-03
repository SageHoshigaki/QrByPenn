from pathlib import Path
import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage

def generate_qr_code(url, img_path, is_paid):
    if not is_paid:
        url = "https://example.com/payment_required"  # Redirect to a payment page or a notice

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    embedded_image = Image.open(img_path)
    img = qr.make_image(image_factory=StyledPilImage, embeded_image=embedded_image)
    
    # Optionally, save the QR code to a file
    img.save("generated_qr.png")
    
    return img

# Usage example
image_link = Path("img/google.png")
dynamic_url = "https://www.google.com"
payment_status = True  # This should be dynamically set based on your payment logic

qr_image = generate_qr_code(dynamic_url, image_link, payment_status)
print(qr_image)
