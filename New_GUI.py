"""Text to speech module"""

from gtts import gTTS
from tkinter import *
import os
import playsound
from tkinter import filedialog
import PyPDF2  # for Audiobook
from textblob import TextBlob
import pyttsx3

# initializing the module
# engine = pyttsx3.init()

# .say() function is used to speak the text you have written inside this.
# inside the function

# this is used to process and run the program commands

TextString = ""
"""Text-to-voice"""
text = ""
txt = ""
txt2 = ""

language_list = ["English", "Hindi", "Gujarati", "Marathi"]
languageCode_list = ["en", "hi", "gu", "mr"]


def click1():
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

    # myobj = gTTS(text=txt.get(), lang=variable1.get(), slow=False)
    # print("\n\n Text = ", txt.get())
    # print("\n\n Code = ", variable1.get(), "\n\n")
    # myobj.save("converted.mp3")
    # playsound.playsound("converted.mp3", True)
    # os.remove("converted.mp3")


"""Audiobook"""

"""book = open('pythonBook.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)


page = pdfReader.getPage(16)
text = page.extractText()"""
speaker = pyttsx3.init()


def upload_pdf():
    global TextString
    global text
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title="upload PDF File",
                                     filetypes=(("PDF File", "*.pdf"),
                                                ("All Files", ".")))

    pdf_File = open(str(fln), 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages
    TextList = []

    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            text = page.extractText()
            # TextList.append(page.extractText())
        except:
            pass

    TextString = " ".join(TextList)
    language = 'en'
    print(TextString)


def click2():
    """global TextString
    print(TextString)
    myobj = gTTS(text=TextString, lang='en', slow=False)
    myobj.save("AudioBook.mp3")
    playsound.playsound("AudioBook.mp3", True)
    os.remove("AudioBook.mp3")"""

    speaker.say(text)
    speaker.runAndWait()
    """Spell-checker"""


def clearAll():
    # whole content of text entry area is deleted
    word1_field.delete(0, END)
    word2_field.delete(0, END)


def correction():
    # get a content from entry box
    input_word = word1_field.get()

    # create a TextBlob object
    blob_obj = TextBlob(input_word)

    # get a corrected word
    corrected_word = str(blob_obj.correct())

    # insert method inserting the
    # value in the text entry box.
    word2_field.insert(10, corrected_word)


"""GUI"""
window = Tk()
window.title("AudioBook")
window.geometry('1000x500')
window.iconbitmap(r'favicon.ico')

variable1 = StringVar(window)
variable1.set("select-lang")

# text = Label(window, text='Welcome to AudioBook!!')
# text.pack()

lbl2 = Label(window, text="          Text-to-Speech", font=('lato black', 17, 'bold'), fg="blue")
lbl2.grid(column=0, row=0)
lbl2 = Label(window, text="        using Python", font=('lato black', 17, 'bold'), fg="blue")
lbl2.grid(column=0, row=1)

lbl2 = Label(window, text="", font=('lato black', 20, 'bold'), fg="red")
lbl2.grid(column=0, row=2)

lbl2 = Label(window, text="Enter text : ", font=('lato black', 12, 'bold'))
lbl2.grid(column=0, row=3)

txt = Entry(window, textvariable=txt, font=('lato black', 12, 'normal'))
txt.grid(column=1, row=3)

lbl2 = Label(window, text="Select Accent : ", font=('lato black', 12, 'bold'))
lbl2.grid(column=0, row=4)

txt2 = OptionMenu(window, variable1, *languageCode_list)
txt2.grid(column=1, row=4)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=5)

btn = Button(window, font=('lato', 13, 'bold'), text="Play Sound", padx=2, pady=2, bg="red", fg="white",
             command=click1)
btn.grid(column=1, row=6)

btn = Button(window, font=('lato', 13, 'bold'), text="Upload PDF file", padx=2, pady=2, bg="red", fg="white",
             command=upload_pdf)
btn.grid(column=5, row=4)

btn = Button(window, font=('lato', 13, 'bold'), text="play Audiobook", padx=2, pady=2, bg="red", fg="white",
             command=click2)
btn.grid(column=5, row=5)

# Create a "Input Word": label
label1 = Label(window, text="Input Word",
               fg='black', bg='dark green')
label1.grid(row=8, column=0)

# Create a "Corrected Word": label
label2 = Label(window, text="Corrected Word",
               fg='black', bg='dark green')
label2.grid(row=9, column=0, padx=10)

# Create a text entry box
# for filling or typing the information.
word1_field = Entry()
word2_field = Entry()

# padx keyword argument used to set paading along x-axis .
# pady keyword argument used to set paading along y-axis .
word1_field.grid(row=8, column=1, padx=10, pady=10)
word2_field.grid(row=9, column=1, padx=10, pady=10)

# Create a Correction Button and attached
# with correction function
button1 = Button(window, text="Correction", font=('lato', 13, 'bold'), bg="red", fg="white", command=correction)

button1.grid(row=10, column=2)

# Create a Clear Button and attached
# with clearAll function
button2 = Button(window, text="Clear", font=('lato', 13, 'bold'), bg="red", fg="white", command=clearAll)

button2.grid(row=10, column=1)

window.mainloop()
