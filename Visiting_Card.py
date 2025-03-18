from fpdf import FPDF
import qrcode
from PIL import Image
import os

# Function to generate QR Code for location
def generate_qr_code(location, qr_filename="qr_code.png"):
    qr = qrcode.make(location)
    qr.save(qr_filename)
    return qr_filename

# Function to create a Visiting Card
def create_visiting_card(company, phone, address, location, logo_path=None):
    card_width, card_height = 90, 50  # Business card size in mm
    pdf_filename = "Visiting_Card.pdf"

    # Create PDF
    pdf = FPDF(orientation='L', unit='mm', format=(card_width, card_height))
    pdf.add_page()

    # Background color
    pdf.set_fill_color(240, 240, 240)  # Light grey background
    pdf.rect(0, 0, card_width, card_height, style='F')

    # Add Company Logo (if provided)
    if logo_path and os.path.exists(logo_path):
        pdf.image(logo_path, x=5, y=5, w=15, h=15)  # Adjust size & position

    # Set font for Company Name
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, company, ln=True, align='C')

    # Line separator
    pdf.set_line_width(0.5)
    pdf.line(10, 20, 80, 20)

    # Add Contact Details
    pdf.set_font("Arial", size=10)
    pdf.ln(5)
    pdf.cell(0, 10, f"📞 {phone}", ln=True, align='C')
    pdf.cell(0, 10, f"🏠 {address}", ln=True, align='C')

    # Generate and Insert QR Code for Location
    qr_path = generate_qr_code(location)
    pdf.image(qr_path, x=65, y=30, w=20, h=20)  # Adjust QR code position & size

    # Save the PDF
    pdf.output(pdf_filename)
    print(f"✅ Visiting Card Generated: {pdf_filename}")

    return pdf_filename

# Function to Display the Visiting Card
def show_visiting_card(pdf_filename):
    # Convert the PDF to an image (Preview)
    img = Image.open(pdf_filename)
    img.show()

# User Input
company = input("Enter Company Name: ")
phone = input("Enter Phone Number (India Format): ")
address = input("Enter Address (India): ")
location = input("Enter Google Maps Location URL: ")
logo_path = input("Enter Logo Image Path (Optional): ") or None

# Generate the Visiting Card
pdf_file = create_visiting_card(company, phone, address, location, logo_path)

# Show the Visiting Card
show_visiting_card(pdf_file)
