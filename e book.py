# from pypdf import PdfReader  #pdf to text
# from  gtts  import gTTS #voice engine
# def pdf_to_audio(pdf_path,output_file='output.mp3',language='en'):
#     with open(pdf_path, 'rb') as file:   
#         reader=PdfReader(pdf_path)   
#         text=""
#         for page in reader.pages:
#             text+=page.extract_text()
#     tts=gTTS(text=text,lang=language,slow=False)
#     tts.save(output_file)

# pdf_to_audio("D:\\GATE NOTES\\MECHANICS\\Engineering Mechanics Marut Tiwari","output.mp3")

from pypdf import PdfReader  # For reading the PDF
from gtts import gTTS        # For converting text to speech

def pdf_to_audio(pdf_path, output_file='output.mp3', language='en'):
    # Open and read the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Ensure the page has text
                text += page_text.strip() + " "  # Clean and add space between pages
    
    # Generate audio using Google Text-to-Speech
    if text.strip():  # Only proceed if text is non-empty
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)
        print(f"Audio saved to {output_file}")
    else:
        print("No text found in PDF.")

# Call the function with the uploaded PDF path
pdf_to_audio("D:\\GATE NOTES\\MECHANICS\\Engineering Mechanics Marut Tiwari", "output.mp3")
