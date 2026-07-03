from Database.connection import SessionLocal
from Database.models import (
    Customer,
    Branch,
    Account,
    Cheque,
    Transaction,
    AuditLog
)

# ==========================================================
# DATABASE SESSION
# ==========================================================

def get_session():
    return SessionLocal()

# ==========================================================
# CUSTOMER
# ==========================================================

def get_customer(customer_id):

    session = get_session()

    try:

        return session.query(Customer).filter(
            Customer.customer_id == customer_id
        ).first()

    finally:

        session.close()


# ==========================================================
# ACCOUNT
# ==========================================================

def get_account(account_number):

    session = get_session()

    try:

        return session.query(Account).filter(
            Account.account_number == account_number
        ).first()

    finally:

        session.close()


# ==========================================================
# ACCOUNT BY MICR
# ==========================================================

def get_account_by_micr(micr):

    session = get_session()

    try:

        return session.query(Account).filter(
            Account.micr == micr
        ).first()

    finally:

        session.close()


# ==========================================================
# UPDATE BALANCE
# ==========================================================

def update_balance(account_number, new_balance):

    session = get_session()

    try:

        account = session.query(Account).filter(
            Account.account_number == account_number
        ).first()

        if account is None:
            return False

        account.balance = new_balance

        session.commit()

        return True

    finally:

        session.close()


# ==========================================================
# SAVE CHEQUE
# ==========================================================

def save_cheque(cheque):

    session = get_session()

    try:

        session.add(cheque)

        session.commit()

        session.refresh(cheque)

        return cheque

    finally:

        session.close()


# ==========================================================
# SAVE TRANSACTION
# ==========================================================

def save_transaction(transaction):

    session = get_session()

    try:

        session.add(transaction)

        session.commit()

        session.refresh(transaction)

        return transaction

    finally:

        session.close()


# ==========================================================
# SAVE AUDIT LOG
# ==========================================================

def save_audit_log(log):

    session = get_session()

    try:

        session.add(log)

        session.commit()

    finally:

        session.close()


# ==========================================================
# GET SIGNATURE PATH
# ==========================================================

def get_signature_path(account_number):

    session = get_session()

    try:

        account = session.query(Account).filter(
            Account.account_number == account_number
        ).first()

        if account:

            return account.signature_path

        return None

    finally:

        session.close()