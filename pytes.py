from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import json


def pdf_to_text():
    try:
        # you need to install tesseract-ocr in your local machine and add the path here
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # need to install poppler for your os and add the path here
        poppler_path = r'C:\Program Files\poppler-0.68.0\bin'

        pdf_file = "sample.pdf"
        pages = convert_from_path(pdf_file, 500, poppler_path=poppler_path)
        image_counter = 1

        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            page.save(filename, 'JPEG')
            image_counter = image_counter + 1

        filelimit = image_counter - 1

        outfile = "output.txt"
        f = open(outfile, "a")

        for i in range(1, filelimit + 1):
            filename = "page_" + str(i) + ".jpg"
            img = Image.open(filename)
            text = str((pytesseract.image_to_string(img)))
            text = text.replace('-\n', '')
            print(json.dumps(text))
            f.write(text)
        f.close()

    except ImportError as e:
        print(e)


pdf_to_text()



