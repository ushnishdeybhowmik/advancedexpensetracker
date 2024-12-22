import pytesseract
import cv2
import re
import datetime as dt
import os
import sys
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Set the path to `tesseract.exe` and `tessdata`
tesseract_exe = r'spendai\Tesseract-OCR\tesseract.exe' # Adjust path if needed
tessdata_dir = r'spendai\Tesseract-OCR\tessdata'
  
# Configure pytesseract
pytesseract.tesseract_cmd = tesseract_exe
os.environ["TESSDATA_PREFIX"] = tessdata_dir

os.environ["PATH"] += os.pathsep + r"spendai\Tesseract-OCR"

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
    print(corpus)
    for(i, line) in enumerate(corpus):
        if "To" in line and pattern.match(line):
            name = line.split(" ")[1:]
            name = " ".join(name)
            print(name)
            amount = ''
            for j in range(i+1, len(corpus)):
                if not corpus[j] == '' and not len(corpus[j]) > 7:
                    amount = corpus[j]
                    break
            if not amount[0].isdigit():
                amount = amount[1:].split(",")[:]
                amount = "".join(amount)
            else:
                amount = amount.split(",")[:]
                amount = "".join(amount)
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
            
    return name, int(amount), date.split(" ")[0], date.split(" ")[1], pmode, int(txn_id)