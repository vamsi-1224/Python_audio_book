import pyttsx3  #pyttsx3 python text to speech version 3
import PyPDF2 

my_file=open("Python Notes.pdf","rb") #To open a file 
my_pdf_reader=PyPDF2.PdfReader(my_file)
pages=len(my_pdf_reader.pages)
print(f"The PDF has {pages} pages.")

#for single page 
speaker=pyttsx3.init()
page=my_pdf_reader.pages[75]
page_text=page.extract_text()
speaker.say(page_text)
speaker.runAndWait()


#for multiple pages
'''
for page_num in range(23,pages):
    speaker=pyttsx3.init()
    page=my_pdf_reader.pages[page_num]
    page_text=page.extract_text()
    speaker.say(page_text)
    speaker.runAndWait()





'''
