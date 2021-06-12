import PyPDF2
import playsound
from gtts import gTTS

pdf_File = open('CDS--Q1.pdf', 'rb')

pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages
TextList = []

for i in range(count):
    try:
        page = pdf_Reader.getPage(i)
        print(page.extractText())
        TextList.append(page.extractText())
    except:
        pass

TextString = " ".join(TextList)

language = 'en'
myobj = gTTS(text=TextString, lang=language, slow=False)
myobj.save("AudioBook.mp3")
playsound.playsound("AudioBook.mp3", True)
