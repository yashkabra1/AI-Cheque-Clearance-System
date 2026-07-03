import os
import cv2
import pandas as pd

from ultralytics import YOLO

from config import (
    MODEL_PATH,
    IMAGE_FOLDER,
    CROPPED_FOLDER,
    OUTPUT_EXCEL,
    CONFIDENCE,
    KEEP_CLASS_IDS,
    FIELD_MAP
)

from ocr_utils import read_field
from Services.Decision_Engine import process_cheque

# ==========================================================
# LOAD MODEL
# ==========================================================

print("=" * 60)
print("AI CHEQUE CLEARANCE SYSTEM")
print("=" * 60)

print("\nLoading YOLO Model...")

model = YOLO(MODEL_PATH)

print("YOLO Loaded Successfully!")

# ==========================================================
# CHECK IMAGE FOLDER
# ==========================================================

if not os.path.exists(IMAGE_FOLDER):

    raise FileNotFoundError(
        f"Image folder not found:\n{IMAGE_FOLDER}"
    )

# ==========================================================
# CREATE CROPPED FOLDER
# ==========================================================

os.makedirs(
    CROPPED_FOLDER,
    exist_ok=True
)

# ==========================================================
# FIND ALL IMAGES
# ==========================================================

images = [

    file

    for file in os.listdir(IMAGE_FOLDER)

    if file.lower().endswith(
        (
            ".jpg",
            ".jpeg",
            ".png"
        )
    )

]

print(f"\nFound {len(images)} cheque(s).\n")

# ==========================================================
# FINAL REPORT
# ==========================================================

report = []

# ==========================================================
# PROCESS EACH IMAGE
# ==========================================================

for image_name in images:

    print("=" * 60)

    print(f"Processing : {image_name}")

    print("=" * 60)

    image_path = os.path.join(
        IMAGE_FOLDER,
        image_name
    )

    image = cv2.imread(image_path)

    if image is None:

        print("Unable to read image.")

        continue

    detections = model.predict(

        source=image,

        conf=CONFIDENCE,

        classes=KEEP_CLASS_IDS,

        verbose=False

    )

    cheque_data = {

        "IMAGE": image_name,

        "ACCOUNT": "",

        "PAYEE": "",

        "AMOUNT": "",

        "ALPHABET_AMT": "",

        "DATE": "",

        "MICR": "",

        "SIGNATURE": ""

    }

    # ==========================================================
    # DETECT FIELDS
    # ==========================================================

    for result in detections:

        boxes = result.boxes

        if boxes is None:

            continue

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            if class_id not in FIELD_MAP:

                continue

            field = FIELD_MAP[class_id]

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            crop = image[
                y1:y2,
                x1:x2
            ]

            if crop.size == 0:

                continue

            # -----------------------------------------
            # SAVE CROPPED IMAGE
            # -----------------------------------------

            crop_folder = os.path.join(
                CROPPED_FOLDER,
                os.path.splitext(image_name)[0]
            )

            os.makedirs(
                crop_folder,
                exist_ok=True
            )

            crop_path = os.path.join(
                crop_folder,
                field + ".png"
            )

            cv2.imwrite(
                crop_path,
                crop
            )

            print("-" * 40)

            print(f"FIELD : {field}")

            print(f"YOLO CONFIDENCE : {round(confidence*100,2)}%")

            # -----------------------------------------
            # OCR
            # -----------------------------------------

            try:

                if field == "SIGNATURE":

                    cheque_data["SIGNATURE"] = crop_path

                    print("Signature Image Saved")

                else:

                    text = read_field(
                        field,
                        crop
                    )

                    cheque_data[field] = text

                    print(f"TEXT : {text}")

            except Exception as e:

                print(f"OCR ERROR : {e}")

                cheque_data[field] = ""

            print("-" * 40)

    # ==========================================================
    # PROCESS CHEQUE
    # ==========================================================

    print("\nVerifying Cheque...")

    try:

        result = process_cheque(
            cheque_data
        )

    except Exception as e:

        print("\nERROR DURING VERIFICATION")

        print(e)

        continue

    print("\n")

    print("=" * 60)

    print("FINAL RESULT")

    print("=" * 60)

    print(f"STATUS : {result['status']}")

    if result["status"] == "APPROVED":

        print(
            f"Transaction ID : {result['transaction_id']}"
        )

        print(
            f"Remaining Balance : ₹{result['remaining_balance']}"
        )

    else:

        print(
            f"Reason : {result['reason']}"
        )

    print("=" * 60)

    # ==========================================================
    # SAVE REPORT
    # ==========================================================

    report_row = {

        "Image": cheque_data["IMAGE"],

        "Account": cheque_data["ACCOUNT"],

        "Payee": cheque_data["PAYEE"],

        "Amount": cheque_data["AMOUNT"],

        "Amount Words": cheque_data["ALPHABET_AMT"],

        "Date": cheque_data["DATE"],

        "MICR": cheque_data["MICR"],

        "Status": result["status"]

    }

    if result["status"] == "APPROVED":

        report_row["Transaction ID"] = result["transaction_id"]

        report_row["Remaining Balance"] = result["remaining_balance"]

        report_row["Reason"] = ""

    else:

        report_row["Transaction ID"] = ""

        report_row["Remaining Balance"] = ""

        report_row["Reason"] = result["reason"]

    report.append(report_row)

# ==========================================================
# CREATE REPORT
# ==========================================================

print("\nGenerating Report...")

df = pd.DataFrame(report)

column_order = [

    "Image",

    "Account",

    "Payee",

    "Amount",

    "Amount Words",

    "Date",

    "MICR",

    "Status",

    "Transaction ID",

    "Remaining Balance",

    "Reason"

]

for col in column_order:

    if col not in df.columns:

        df[col] = ""

df = df[column_order]

df.to_excel(

    OUTPUT_EXCEL,

    index=False

)

# ==========================================================
# SUMMARY
# ==========================================================

approved = len(

    df[df["Status"] == "APPROVED"]

)

rejected = len(

    df[df["Status"] == "REJECTED"]

)

print("\n")

print("=" * 70)

print("AI CHEQUE CLEARANCE SYSTEM")

print("=" * 70)

print(f"Total Cheques     : {len(df)}")

print(f"Approved Cheques  : {approved}")

print(f"Rejected Cheques  : {rejected}")

print()

print(f"Excel Report Saved")

print(OUTPUT_EXCEL)

print("=" * 70)

print("PROCESS COMPLETED SUCCESSFULLY")

print("=" * 70)

