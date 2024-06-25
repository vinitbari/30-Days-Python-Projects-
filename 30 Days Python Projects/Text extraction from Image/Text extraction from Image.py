import pytesseract 
from PIL import Image 

# Provide the correct path to the Tesseract executable 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\TesseractOCR\tesseract.exe" 

# Open the image 

img = Image.open("1.png") 
# Use pytesseract to extract text from the image 
text = pytesseract.image_to_string(img) 
# Print the extracted text 
print(text) 