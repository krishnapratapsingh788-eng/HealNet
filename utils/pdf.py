from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(patient_name, report):

    filename = f"{patient_name}_report.pdf"

    pdf = canvas.Canvas(filename, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 760, "HealNet AI Report")

    pdf.setFont("Helvetica", 12)

    y = 720

    for line in report.split("\n"):
        pdf.drawString(50, y, line)
        y -= 20

    pdf.save()

    return filename