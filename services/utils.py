from datetime import datetime

# ==========================================================
# STRING -> DATE
# ==========================================================

def convert_to_date(date_string):
    """
    Converts OCR date string to Python date object.
    """

    formats = [

        "%d/%m/%Y",
        "%d-%m-%Y",

        "%d/%m/%y",
        "%d-%m-%y",

        "%Y-%m-%d"

    ]

    for fmt in formats:

        try:

            return datetime.strptime(
                date_string.strip(),
                fmt
            ).date()

        except:

            pass

    return None


# ==========================================================
# DATE VALIDATION
# ==========================================================

def is_future_date(date_obj):

    if date_obj is None:

        return True

    return date_obj > datetime.today().date()


# ==========================================================
# SAFE FLOAT
# ==========================================================

def to_float(value):

    try:

        return float(
            str(value).replace(",", "")
        )

    except:

        return 0.0


# ==========================================================
# SAFE STRING
# ==========================================================

def clean_string(text):

    if text is None:

        return ""

    return str(text).strip()