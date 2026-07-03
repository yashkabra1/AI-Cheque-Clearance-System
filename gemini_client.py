import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# =====================================================
# LOAD ENVIRONMENT VARIABLES
# =====================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

# =====================================================
# CREATE GEMINI CLIENT
# =====================================================

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

# =====================================================
# PROMPTS FOR DIFFERENT CHEQUE FIELDS
# =====================================================

PROMPTS = {

    "ACCOUNT":
    """
    You are an OCR engine.

    Extract ONLY the bank account number.

    Return ONLY the account number.

    No explanation.
    """,

    "PAYEE":
    """
    You are an OCR engine.

    Extract ONLY the payee name.

    Return ONLY the person's name.

    No explanation.
    """,

    "AMOUNT":
    """
    You are an OCR engine.

    Extract ONLY the numeric cheque amount.

    Example:

    25000.00

    Return ONLY the number.

    No explanation.
    """,

    "ALPHABET_AMT":
    """
    You are an OCR engine.

    Extract ONLY the handwritten amount in words.

    Return ONLY the text.

    No explanation.
    """,

    "DATE":
    """
    You are an OCR engine.

    Extract ONLY the cheque date.

    Return ONLY the date.

    No explanation.
    """,

    "MICR":
    """
    You are an OCR engine.

    Extract ONLY the MICR line.

    Return ONLY the MICR text.

    No explanation.
    """,

    "SIGNATURE":
    """
    This image contains a signature.

    Do NOT attempt OCR.

    Simply return:

    SIGNATURE_DETECTED
    """
}

# =====================================================
# GEMINI OCR FUNCTION
# =====================================================

def gemini_ocr(image_path, field):

    prompt = PROMPTS.get(
        field,
        "Extract all visible text."
    )

    uploaded_file = client.files.upload(
        file=image_path
    )

    response = client.models.generate_content(

        model=MODEL,

        contents=[
            uploaded_file,
            prompt
        ],

        config=types.GenerateContentConfig(
            temperature=0
        )

    )

    return response.text.strip()