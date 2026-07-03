import os
import re
import cv2

from gemini_client import gemini_ocr

# =====================================================
# IMAGE PREPROCESSING
# =====================================================

def preprocess_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return thresh


# =====================================================
# SAVE TEMP IMAGE
# =====================================================

def save_temp_image(image, field):

    temp_folder = "temp"

    os.makedirs(temp_folder, exist_ok=True)

    temp_path = os.path.join(
        temp_folder,
        f"{field}.png"
    )

    cv2.imwrite(temp_path, image)

    return temp_path


# =====================================================
# CLEAN TEXT
# =====================================================

def clean_text(text):

    if text is None:
        return ""

    text = text.replace("|", "")

    text = text.replace("\n", " ")

    text = text.strip()

    return text


# =====================================================
# EXTRACT AMOUNT
# =====================================================

def extract_amount(text):

    match = re.findall(
        r'\d[\d,]*\.?\d*',
        text
    )

    if match:

        return match[0]

    return text


# =====================================================
# FORMAT DATE
# =====================================================

def format_date(text):

    match = re.findall(

        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',

        text

    )

    if match:

        return match[0]

    return text


# =====================================================
# OCR MAIN FUNCTION
# =====================================================

def read_field(field_name, crop):

    processed = preprocess_image(crop)

    image_path = save_temp_image(

        processed,

        field_name

    )

    text = gemini_ocr(

        image_path,

        field_name

    )

    text = clean_text(text)

    if field_name == "AMOUNT":

        text = extract_amount(text)

    if field_name == "DATE":

        text = format_date(text)

    return text