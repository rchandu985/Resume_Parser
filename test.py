import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = 'incoming/Dice_Profile_Ashish_Bandgar (1).pdf'
extracted_text = extract_text_from_pdf(pdf_path)

print(extracted_text)
