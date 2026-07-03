import os

# ======================================================
# PROJECT PATHS
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "runs",
    "detect",
    "train4",
    "weights",
    "best.pt"
)

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "Dataset",
    "Images"
)

OUTPUT_EXCEL = os.path.join(
    BASE_DIR,
    "cheque_output.xlsx"
)

CROPPED_FOLDER = os.path.join(
    BASE_DIR,
    "Cropped_Fields"
)

os.makedirs(CROPPED_FOLDER, exist_ok=True)

# ======================================================
# YOLO SETTINGS
# ======================================================

CONFIDENCE = 0.25

KEEP_CLASS_IDS = [0,1,2,3,4,5,6]

# ======================================================
# CLASS MAPPING
# ======================================================

FIELD_MAP = {

    0: "ALPHABET_AMT",

    1: "ACCOUNT",

    2: "AMOUNT",

    3: "DATE",

    4: "MICR",

    5: "PAYEE",

    6: "SIGNATURE"

}

# ======================================================
# OCR SETTINGS
# ======================================================

EASYOCR_LANG = ['en']

TROCR_MODEL = "microsoft/trocr-large-handwritten"