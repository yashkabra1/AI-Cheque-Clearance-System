from database.models import (
    Cheque,
    Transaction,
    AuditLog
)

from database.queries import (
    update_balance,
    save_cheque,
    save_transaction,
    save_audit_log
)

from services.utils import (
    convert_to_date,
    to_float,
    clean_string
)

from services.Verification import verify_cheque


# ==========================================================
# PROCESS CHEQUE
# ==========================================================

def process_cheque(cheque_data):

    verification = verify_cheque(cheque_data)

    # ------------------------------------------------------
    # CHEQUE OBJECT
    # ------------------------------------------------------

    cheque = Cheque(

        image_name=cheque_data["IMAGE"],

        amount=to_float(cheque_data["AMOUNT"]),

        amount_words=clean_string(
            cheque_data["ALPHABET_AMT"]
        ),

        cheque_date=convert_to_date(
            cheque_data["DATE"]
        ),

        micr=clean_string(
            cheque_data["MICR"]
        ),

        signature_image=cheque_data["SIGNATURE"]

    )

    # ------------------------------------------------------
    # REJECTED
    # ------------------------------------------------------

    if not verification["approved"]:

        cheque.status = "REJECTED"

        cheque.rejection_reason = verification["reason"]

        saved_cheque = save_cheque(cheque)

        log = AuditLog(

            cheque_id=saved_cheque.cheque_id,

            action="CHEQUE REJECTED",

            details=verification["reason"]

        )

        save_audit_log(log)

        return {

            "status": "REJECTED",

            "reason": verification["reason"]

        }

    # ------------------------------------------------------
    # APPROVED
    # ------------------------------------------------------

    account = verification["account"]

    balance_before = to_float(account.balance)

    balance_after = balance_before - to_float(
        cheque_data["AMOUNT"]
        )

    update_balance(

        account.account_number,

        balance_after

    )

    cheque.status = "APPROVED"

    cheque.rejection_reason = ""

    saved_cheque = save_cheque(cheque)

    transaction = Transaction(

        account_number=account.account_number,

        cheque_id=saved_cheque.cheque_id,

        amount=cheque.amount,

        balance_before=balance_before,

        balance_after=balance_after

    )

    saved_transaction = save_transaction(transaction)

    log = AuditLog(

        cheque_id=saved_cheque.cheque_id,

        action="CHEQUE APPROVED",

        details=f"Transaction ID : {saved_transaction.transaction_id}"

    )

    save_audit_log(log)

    return {

        "status": "APPROVED",

        "transaction_id": saved_transaction.transaction_id,

        "remaining_balance": balance_after

    }