import PyPDF2
import pyttsx3

def text_extraction(path):
    f = open(path, 'rb')
    pdf = PyPDF2.PdfFileReader(f)
    if pdf.isEncrypted:
        pdf.decrypt('')
    page = pdf.getPage(47)
    text = page.extractText()
    print(text)
    audio(text)
    

def audio(text):
    engin = pyttsx3.init()
    engin.setProperty('rate', 140)
    engin.say(text)
    engin.runAndWait()

# Path to your pdf file
text_extraction('path_to_pdf_file.pdf')
