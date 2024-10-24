from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class BankAccountCreate(BaseModel):
    account_holder_name: str
    bank_name: str
    account_number: str
    account_type: str
    ifsc_code: str
    branch_location: str
    linked_mobile_number: str
    account_nickname: Optional[str] = None
    account_balance: Decimal
    primary_check: bool = False

class CustomerCreate(BaseModel):
    company_name: str
    escrow_va: str
    ifsc_code: str
    gst_in: str
    vpa: str
    business_category: str
    swift_code: str

class BeneficiaryCreate(BaseModel):
    beneficiary_name: str
    bank_name: str
    percentage_allocation: float
    relation_to_beneficiary: str
    beneficiary_account_number: str
    ifsc_code: str
    phone_number: str
    beneficiary_nickname: str
    payment_amount: float
    email_address: str
    primary_check: bool = False
    agree_conditions: bool = True
