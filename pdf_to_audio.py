import pyttsx4, PyPDF2

pdfreader = PyPDF2.PdfFileReader(open("me.pdf","rb"))
speaker = pyttsx4.init()

full_text = ""
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace("\n"," ")
    full_text += clean_text

print(full_text)

speaker.save_to_file(full_text, "audio.mp3")
speaker.runAndWait()

speaker.stop()
