import sys
# from PyPDF2 import PdfReader, PdfWriter
import PyPDF2
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_watermark(file_name, content):
    c = canvas.Canvas(file_name, pagesize=(30 * cm, 30 * cm))
    width, height = letter
    c.setFillColorRGB(0, 0, 0)
    c.setFillAlpha(0.3)
    c.setFont("Helvetica", 36)
    # Calculate positions to repeat the watermark across the page
    for x in range(0, int(width), 350):
        for y in range(int(x/100), int(height), 100):
            c.saveState()
            c.translate(x + 100, y + 80)
            c.rotate(45)  # Rotate the text for diagonal watermark
            c.drawCentredString(0, 0, content)
            c.restoreState()
    c.save()
    return file_name


def embed_watermark(pdf_file_in, tmp_file, watermarkInfo, pdf_file_out):
    pdf_file_mark = create_watermark(tmp_file, watermarkInfo)

    pdf_input = PyPDF2.PdfReader(open(pdf_file_in, 'rb'))
    pdf_watermark = PyPDF2.PdfReader(open(pdf_file_mark, 'rb'))
    pdf_output = PyPDF2.PdfWriter()

    pageNum = len(pdf_input.pages)
    for i in range(pageNum):
        page = pdf_input.pages[i]
        page.merge_page(pdf_watermark.pages[0])
        page.compress_content_streams() 
        pdf_output.add_page(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


if __name__ == '__main__':
    pdf_file = sys.argv[1]
    tmp_file = sys.argv[2]
    watermarkInfo = sys.argv[3]
    file_out = sys.argv[4]

    embed_watermark(pdf_file, tmp_file, watermarkInfo, file_out)
