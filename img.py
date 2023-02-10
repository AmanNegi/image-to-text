import cv2
import os
import pytesseract

# Load the image
path = "./images";

# Using list comprehension to get the list of images
images = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Delete the output file if it exists from a previous execution
if os.path.exists('output.txt'):
    os.remove('output.txt');


for imgName in images:
    img = cv2.imread(imgName)

    # Extract the text using pytesseract
    text = pytesseract.image_to_string(img)

    # Append the text to the file
    with open('output.txt', 'a') as file:
        file.write(f"\n-----------{imgName}-----------\n");
        file.write(text)

print("Text Extracted Successfully")