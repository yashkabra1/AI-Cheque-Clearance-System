from sqlalchemy import (
    Column,
    Integer,
    String,
    BigInteger,
    DECIMAL,
    Date,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

# ==========================================================
# CUSTOMERS
# ==========================================================

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50), nullable=False)

    phone = Column(String(15), unique=True)

    email = Column(String(100), unique=True)

    created_at = Column(DateTime, server_default=func.now())

    accounts = relationship("Account", back_populates="customer")


# ==========================================================
# BRANCHES
# ==========================================================

class Branch(Base):

    __tablename__ = "branches"

    branch_id = Column(Integer, primary_key=True, autoincrement=True)

    branch_name = Column(String(100), nullable=False)

    ifsc_code = Column(String(20), unique=True)

    city = Column(String(50))

    state = Column(String(50))

    accounts = relationship("Account", back_populates="branch")


# ==========================================================
# ACCOUNTS
# ==========================================================

class Account(Base):

    __tablename__ = "accounts"

    account_number = Column(BigInteger, primary_key=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id")
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.branch_id")
    )

    balance = Column(DECIMAL(12,2), default=0)

    micr = Column(String(20), unique=True)

    signature_path = Column(String(255))

    account_status = Column(String(20), default="ACTIVE")

    daily_limit = Column(DECIMAL(12,2), default=100000)

    customer = relationship(
        "Customer",
        back_populates="accounts"
    )

    branch = relationship(
        "Branch",
        back_populates="accounts"
    )

    transactions = relationship(
        "Transaction",
        back_populates="account"
    )


# ==========================================================
# CHEQUES
# ==========================================================

class Cheque(Base):

    __tablename__ = "cheques"

    cheque_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    image_name = Column(String(255))

    account_number = Column(
        BigInteger,
        ForeignKey("accounts.account_number")
    )

    payee = Column(String(150))

    amount = Column(DECIMAL(12,2))

    amount_words = Column(Text)

    cheque_date = Column(Date)

    micr = Column(String(20))

    signature_image = Column(String(255))

    status = Column(String(20))

    rejection_reason = Column(Text)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


# ==========================================================
# TRANSACTIONS
# ==========================================================

class Transaction(Base):

    __tablename__ = "transactions"

    transaction_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    account_number = Column(
        BigInteger,
        ForeignKey("accounts.account_number")
    )

    cheque_id = Column(Integer)

    amount = Column(DECIMAL(12,2))

    balance_before = Column(DECIMAL(12,2))

    balance_after = Column(DECIMAL(12,2))

    transaction_time = Column(
        DateTime,
        server_default=func.now()
    )

    account = relationship(
        "Account",
        back_populates="transactions"
    )


# ==========================================================
# AUDIT LOGS
# ==========================================================

class AuditLog(Base):

    __tablename__ = "audit_logs"

    log_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    cheque_id = Column(Integer)

    action = Column(String(100))

    details = Column(Text)

    timestamp = Column(
        DateTime,
        server_default=func.now()
    )