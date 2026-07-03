from Database.connection import SessionLocal
from Database.models import Customer, Branch, Account

# ==========================================================
# DATABASE SESSION
# ==========================================================

session = SessionLocal()

# ==========================================================
# DON'T INSERT TWICE
# ==========================================================

if session.query(Customer).count() > 0:
    print("Sample data already exists.")
    session.close()
    exit()

# ==========================================================
# CUSTOMERS
# ==========================================================

customer1 = Customer(
    first_name="Yash",
    last_name="Kabra",
    phone="9876543210",
    email="yash@gmail.com"
)

customer2 = Customer(
    first_name="Rahul",
    last_name="Sharma",
    phone="9876543211",
    email="rahul@gmail.com"
)

customer3 = Customer(
    first_name="Priya",
    last_name="Singh",
    phone="9876543212",
    email="priya@gmail.com"
)

customer4 = Customer(
    first_name="Amit",
    last_name="Verma",
    phone="9876543213",
    email="amit@gmail.com"
)

customer5 = Customer(
    first_name="Neha",
    last_name="Gupta",
    phone="9876543214",
    email="neha@gmail.com"
)

session.add_all([
    customer1,
    customer2,
    customer3,
    customer4,
    customer5
])

session.commit()

# ==========================================================
# BRANCHES
# ==========================================================

branch1 = Branch(
    branch_name="Kolkata Main Branch",
    ifsc_code="HDFC0001001",
    city="Kolkata",
    state="West Bengal"
)

branch2 = Branch(
    branch_name="Delhi Branch",
    ifsc_code="HDFC0001002",
    city="Delhi",
    state="Delhi"
)

session.add_all([branch1, branch2])

session.commit()

# ==========================================================
# ACCOUNTS
# ==========================================================

accounts = [

    Account(
        account_number=1000000001,
        customer_id=customer1.customer_id,
        branch_id=branch1.branch_id,
        balance=250000,
        micr="MICR000001",
        signature_path="Customer_Signatures/1000000001.png",
        account_status="ACTIVE",
        daily_limit=100000
    ),

    Account(
        account_number=1000000002,
        customer_id=customer2.customer_id,
        branch_id=branch1.branch_id,
        balance=85000,
        micr="MICR000002",
        signature_path="Customer_Signatures/1000000002.png",
        account_status="ACTIVE",
        daily_limit=50000
    ),

    Account(
        account_number=1000000003,
        customer_id=customer3.customer_id,
        branch_id=branch2.branch_id,
        balance=540000,
        micr="MICR000003",
        signature_path="Customer_Signatures/1000000003.png",
        account_status="ACTIVE",
        daily_limit=300000
    ),

    Account(
        account_number=1000000004,
        customer_id=customer4.customer_id,
        branch_id=branch2.branch_id,
        balance=12000,
        micr="MICR000004",
        signature_path="Customer_Signatures/1000000004.png",
        account_status="ACTIVE",
        daily_limit=10000
    ),

    Account(
        account_number=1000000005,
        customer_id=customer5.customer_id,
        branch_id=branch2.branch_id,
        balance=900000,
        micr="MICR000005",
        signature_path="Customer_Signatures/1000000005.png",
        account_status="ACTIVE",
        daily_limit=500000
    )

]

session.add_all(accounts)

session.commit()

session.close()

print("=" * 60)
print("Sample Banking Database Created Successfully!")
print("=" * 60)
print("Customers : 5")
print("Branches  : 2")
print("Accounts  : 5")
print("=" * 60)