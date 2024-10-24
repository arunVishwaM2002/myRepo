from modules import app, get_db
from sqlalchemy.orm import Session
from modules.controllers import read_customer_by_id, read_transactions_by_customer, read_payment_summary
from modules.controllers import read_cashflow_by_customer, read_income_expense_by_customer, create_new_customer
from modules.controllers import create_new_account, get_added_beneficiaries, read_consolidated_balance, create_or_update_beneficiary
from fastapi import Depends
from modules.pydantic_models import BeneficiaryCreate,CustomerCreate, BankAccountCreate

# new_customer_details={
#     "escrow_va": "VA123456",
#     "company_name": "Tech Innovations Ltd.",
#     "ifsc_code": "ABC1234567",
#     "gst_in": "GST123456789",
#     "vpa": "techinnovations@upi",
#     "business_category": "Technology",
#     "swift_code": "TIL12345"
# }

# new_bank_account={
#   "account_holder_name": "Pundrik Doe",
#   "bank_name": "State Bank of India",
#   "account_number": "1234567890",
#   "account_type": "Savings",
#   "ifsc_code": "SBIN0001234",
#   "branch_location": "Mumbai, India",
#   "linked_mobile_number": "+919876543210",
#   "account_nickname": "Personal Savings",
#   "primary_check": False
# }

# {
#         "beneficiary_name": "Olivia Garcia",
#         "bank_name": "Omicron Bank",
#         "percentage_allocation": 22.00,
#         "relation_to_beneficiary": "Cousin",
#         "beneficiary_account_number": "3456019876",
#         "ifsc_code": "OMICRON015",
#         "phone_number": "9876512345",
#         "beneficiary_nickname": "Liv",
#         "payment_amount": 2200.00,
#         "email_address": "olivia.garcia@example.com",
#         "primary_check": True,
#         "agree_conditions": True
#     }


@app.get('/')
def sayHello():
    return {"Message": "Hello bro!"}


@app.get('/customers/{customer_id}')
def fetch_customer(customer_id: int, db: Session = Depends(get_db)):
    return read_customer_by_id(customer_id, db)


@app.get('/transactions/{customer_id}')
def fetch_transactions(customer_id: int, skip: int = 0, limit: int = 2, db: Session = Depends(get_db)):
    return read_transactions_by_customer(customer_id, skip, limit, db)

# @app.get('/payment')
# def fetch_payment_summary(skip:int=0, limit: int=2,db:Session=Depends(get_db)):
#     return read_payement_summary(skip,limit,db)

@app.get('/payment/{customer_id}')
def fetch_payment_summary(customer_id: int, db: Session = Depends(get_db)):
    return read_payment_summary(customer_id, db)

@app.get('/cash_flow/{customer_id}')
def fetch_cash_flow(customer_id: int, db: Session = Depends(get_db)):
    return read_cashflow_by_customer(customer_id, db)

@app.get('/income_expenses/{customer_id}')
def fetch_income_expenses(customer_id: int, db: Session = Depends(get_db)):
    return read_income_expense_by_customer(customer_id, db)

@app.post('/new_customer')
def add_new_customer(customer_create:CustomerCreate, db:Session=Depends(get_db)):
    new_customer_details=customer_create.dict()
    return create_new_customer(new_customer_details,db)

@app.post('/new_account')
def add_new_account(account_create:BankAccountCreate, db:Session=Depends(get_db)):
    new_bank_account=account_create.dict()
    return create_new_account(new_bank_account,db)

@app.post('/add_beneficiaries')
def create_beneficiary(beneficiary: BeneficiaryCreate, db: Session = Depends(get_db)):
    beneficiary_data = beneficiary.dict()  
    return create_or_update_beneficiary(beneficiary_data, db)

@app.put('/beneficiaries/{beneficiary_id}')
def update_beneficiary(beneficiary_id: int, beneficiary: BeneficiaryCreate, db: Session = Depends(get_db)):
    beneficiary_data = beneficiary.dict()
    return create_or_update_beneficiary(beneficiary_data, db, beneficiary_id)

@app.get('/beneficiaries')
def fetch_beneficiaries(db:Session=Depends(get_db)):
    return get_added_beneficiaries(db)

@app.get('/consolidated_balance/{customer_id}')
def fetch_consolidated_balances(customer_id:int,db:Session=Depends(get_db)):
    return read_consolidated_balance(customer_id,db)