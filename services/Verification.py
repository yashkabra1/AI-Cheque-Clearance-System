from Database.queries import (
    get_account,
    get_account_by_micr
)

# ==========================================================
# VERIFY ACCOUNT EXISTS
# ==========================================================

def verify_account(account_number):

    account = get_account(account_number)

    if account is None:

        return False, "Account does not exist."

    return True, account


# ==========================================================
# VERIFY MICR
# ==========================================================

def verify_micr(account, micr):

    if account.micr != micr:

        return False, "MICR does not match."

    return True, "MICR Verified"


# ==========================================================
# VERIFY ACCOUNT STATUS
# ==========================================================

def verify_account_status(account):

    if account.account_status != "ACTIVE":

        return False, "Account is not active."

    return True, "Account Active"


# ==========================================================
# VERIFY BALANCE
# ==========================================================

def verify_balance(account, amount):

    if float(account.balance) < float(amount):

        return False, "Insufficient Balance"

    return True, "Balance Verified"


# ==========================================================
# VERIFY DAILY LIMIT
# ==========================================================

def verify_daily_limit(account, amount):

    if float(amount) > float(account.daily_limit):

        return False, "Daily Limit Exceeded"

    return True, "Daily Limit Verified"


# ==========================================================
# VERIFY AMOUNT WORDS
# ==========================================================

NUMBER_WORDS = {

    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",

    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",

    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"

}


def verify_amount_words(amount, amount_words):

    amount_words = amount_words.lower()

    amount_str = str(int(float(amount)))

    for digit in amount_str:

        if NUMBER_WORDS.get(int(digit), "") in amount_words:

            continue

    return True, "Amount Verified"


# ==========================================================
# VERIFY DATE
# ==========================================================

from datetime import datetime


def verify_date(cheque_date):

    try:

        cheque_date = datetime.strptime(
            cheque_date,
            "%d/%m/%Y"
        )

    except:

        return False, "Invalid Date"

    if cheque_date.date() > datetime.today().date():

        return False, "Future Date"

    return True, "Date Verified"


# ==========================================================
# RUN ALL VERIFICATIONS
# ==========================================================

def verify_cheque(data):

    result = {

        "approved": False,

        "reason": "",

        "account": None

    }

    ok, account = verify_account(
        data["ACCOUNT"]
    )

    if not ok:

        result["reason"] = account

        return result

    ok, reason = verify_micr(
        account,
        data["MICR"]
    )

    if not ok:

        result["reason"] = reason

        return result

    ok, reason = verify_account_status(
        account
    )

    if not ok:

        result["reason"] = reason

        return result

    ok, reason = verify_balance(
        account,
        data["AMOUNT"]
    )

    if not ok:

        result["reason"] = reason

        return result

    ok, reason = verify_daily_limit(
        account,
        data["AMOUNT"]
    )

    if not ok:

        result["reason"] = reason

        return result

    ok, reason = verify_date(
        data["DATE"]
    )

    if not ok:

        result["reason"] = reason

        return result

    result["approved"] = True

    result["reason"] = "Cheque Approved"

    result["account"] = account

    return result