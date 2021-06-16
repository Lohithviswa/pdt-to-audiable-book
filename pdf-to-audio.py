# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:21:01 2020

@author: User
"""

from gtts import gTTS
import PyPDF2

#Open file Path
pdf_File = open('short-stories-eng.pdf', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
print("Pages counted Pages",count,end=':')
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'en'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)
print('converted')

#Save as mp3 file
myAudio.save("short-stories-eng Audio.mp3")
print('saved')