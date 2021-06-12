

from gtts import gTTS
from tkinter import *
import os
import playsound
from tkinter import filedialog
import PyPDF2  # for Audiobook
from textblob import TextBlob
import winsound

(TextString) =""
"""Text-to-speech"""
txt = ""
txt2 = ""

language_list = ["English", "Hindi", "Gujarati", "Marathi"]
languageCode_list = ["en", "hi", "gu", "mr"]


def click1():
    myobj = gTTS(text=txt.get(), lang=variable1.get(), slow=False)
    # print("\n\n Text = ", txt.get())
    # print("\n\n Code = ", variable1.get(), "\n\n")
    myobj.save("converted.mp3")
    playsound.playsound("converted.mp3", True)
    os.remove("converted.mp3")


"""Audiobook"""


def upload_pdf():
    global TextString
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title="upload PDF File",
                                     filetypes=(("PDF File", "*.pdf"),
                                                ("All Files", ".")))

    pdf_File = open(str(fln), 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages
    textlist = []

    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            # print(page.extractText())
            (textlist).append(page.extractText())
        except:
            pass

    (TextString) = " ".join(textlist)
    language = 'en'
    print(str(TextString))


def click2():
    global TextString
    print(TextString)
    myobj = gTTS(text=TextString, lang='en', slow=False)
    myobj.save("AudioBook.mp3")
    playsound.playsound("AudioBook.mp3", True)
    os.remove("AudioBook.mp3")

    """Spell-checker"""

def stop():
    # winsound.PlaySound(r'C:\sound.wav', winsound.SND_ASYNC)
    winsound.PlaySound(None, winsound.SND_PURGE)

def clearAll():
    
    word1_field.delete(0, END)
    word2_field.delete(0, END)


def correction():
    
    input_word = word1_field.get()

    
    blob_obj = TextBlob(input_word)

    
    corrected_word = str(blob_obj.correct())

    
    word2_field.insert(10, corrected_word)


"""GUI"""

window = Tk()
window.title("Speech-Synthesizer")
window.geometry('700x500')
window.iconbitmap(r'favicon.ico')

variable1 = StringVar(window)
variable1.set("select-lang")

lbl2 = Label(window, text="Welcome to Speech-synthesizer", font=('lato black', 17, 'bold'), fg="blue")
lbl2.grid(column=0, row=0)
lbl2.place(relx=0.50,
           rely=0.0,
           anchor='n')

lbl2 = Label(window, text="", font=('lato black', 20, 'bold'), fg="red")
lbl2.grid(column=0, row=1)  # empty space

lbl2 = Label(window, text="Text to Speech Converter :", font=('lato black', 12, 'bold'), fg="red")
lbl2.grid(column=0, row=2)

lbl2 = Label(window, text="", font=('lato black', 20, 'bold'), fg="red")
lbl2.grid(column=0, row=2)

lbl2 = Label(window, text="Enter text : ", font=('lato black', 12, 'bold'))
lbl2.grid(column=0, row=3)

txt = Entry(window, textvariable=txt, font=('lato black', 12, 'normal'))
txt.grid(column=1, row=3)

lbl2 = Label(window, text="               ", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=2, row=3)

btn = Button(window, font=('lato', 13, 'bold'), text="Play Sound", padx=2, pady=2, bg="red", fg="white",
             command=click1)
btn.grid(column=3, row=3)

lbl2 = Label(window, text="Select Accent : ", font=('lato black', 12, 'bold'))
lbl2.grid(column=0, row=4)

txt2 = OptionMenu(window, variable1, *languageCode_list)
txt2.grid(column=1, row=4)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=5)

lbl2 = Label(window, text="PDF to Speech Converter :", font=('lato black', 12, 'bold'), fg="red")
lbl2.grid(column=0, row=6)

btn = Button(window, font=('lato', 13, 'bold'), text="Upload PDF file", padx=2, pady=2, bg="red", fg="white",
             command=upload_pdf)
btn.grid(column=1, row=7)

btn = Button(window, font=('lato', 13, 'bold'), text="play Audiobook", padx=2, pady=2, bg="red", fg="white",
             command=click2)
btn.grid(column=3, row=7)

btn = Button(window, font=('lato', 13, 'bold'), text="stop", padx=2, pady=2, bg="red", fg="white",
             command=stop)
btn.grid(column=3, row=8)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=8)

lbl2 = Label(window, text="Spelling Checker :", font=('lato black', 12, 'bold'), fg="red")
lbl2.grid(column=0, row=9)

# Create a "Input Word": label
label1 = Label(window, text="Input Word : ")
label1.grid(row=10, column=0)

# Create a "Corrected Word": label
label2 = Label(window, text="Corrected Word : ")
label2.grid(row=12, column=0, padx=10)

# Create a text entry box
# for filling or typing the information.
word1_field = Entry(window, width=30)
word2_field = Entry(window, width=30)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=11)
# padx keyword argument used to set paading along x-axis .
# pady keyword argument used to set paading along y-axis .
word1_field.grid(row=10, column=1, padx=10, pady=10)
word2_field.grid(row=12, column=1, padx=10, pady=10)

# Create a Correction Button and attached
# with correction function
button1 = Button(window, text="Correction", font=('lato', 13, 'bold'), bg="red", fg="white", command=correction)

button1.grid(row=11, column=3)

# Create a Clear Button and attached
# with clearAll function
button2 = Button(window, text="Clear", font=('lato', 13, 'bold'), bg="red", fg="white", command=clearAll)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=13)

button2.grid(row=13, column=1)

lbl2 = Label(window, text="", font=('lato black', 18, 'bold'), fg="red")
lbl2.grid(column=0, row=12)

window.mainloop()
