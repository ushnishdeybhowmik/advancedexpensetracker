from PIL import Image
import pytesseract
import cv2
import re
import datetime as dt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this for your system

def detect_text(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    text = pytesseract.image_to_string(thresh)

    return text


def extract_info_gpay(image):
    image_path = image
    detected_text = detect_text(image_path)
    pattern = re.compile(r"^[a-zA-Z0-9 ]+$")
    date_pattern = r"(\d{1,2})\s([A-Za-z]{3})\s(\d{4}),\s(\d{1,2}):(\d{2})\s([apAP][mM])"
    
    name = amount = date = pmode = txn_id = ""

    corpus = detected_text.split("\n")
    # print(corpus)
    for(i, line) in enumerate(corpus):
        if "To" in line and pattern.match(line):
            name = line.split(" ")[1:]
            name = " ".join(name)
            print(name)
            amount = corpus[i+3]
            amount = amount[1:]
            print(amount)
            corpus.pop(i)
        elif re.match(date_pattern, line):
            
            date = dt.datetime.strptime(line, "%d %b %Y, %I:%M %p")
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            print(date)
            corpus.pop(i)

        elif "UPI" in line:
            pmode = "UPI"
            txn_id = corpus[i+1]
            print(txn_id)
            corpus.pop(i)
            
    return name, int(amount), date, pmode, int(txn_id)