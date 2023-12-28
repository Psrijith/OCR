import cv2
import pytesseract

# Set the path to your image
#image_path = r"C:\Users\peddi\OneDrive\Desktop\me\hand written to text\handwr.jpg"
image_path = "C:\\Users\\peddi\\OneDrive\\Desktop\\me\\hand written to text\\handwr2.jpg"

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or other preprocessing if needed

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(gray)

# Print the recognized text
print("Recognized Text:")
print(text)
