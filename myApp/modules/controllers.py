from modules.models import Customers, Transactions, PaymentSummary, IncomeExpense, CashFlow, BankAccounts
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime,timedelta
from modules.models import Beneficiaries, AccountBalances
from sqlalchemy import and_

def read_customer_by_id(customer_id: int, db):
    customer = db.query(Customers).filter(Customers.customerID == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    customer_data = customer.__dict__
    customer_data.pop("_sa_instance_state", None)

    return customer_data


def read_transactions_by_customer(customer_id: int, skip: int, limit: int, db):
    transactions = db.query(Transactions).filter(Transactions.customerId == customer_id).offset(skip).limit(limit).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this customer")

    result = []
    for transaction in transactions:
        result.append({
            "transaction_id": transaction.transactionId,
            "date": transaction.transactionDate.strftime("%Y-%m-%d") if transaction.transactionDate else None,
            "type": transaction.transactionType,
            "amount": str(transaction.amount),  
            "account": transaction.accountId, 
            "payee": transaction.payee,
            "method": transaction.method,
            "status": transaction.status,
            "consolidate_balance": str(transaction.consolidateBalance)
        })

    return {
        "status": True,
        "message": "",
        "data": result
    }
    transactions = db.query(Transactions).offset(skip).limit(limit).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No Transactions Found")

    result = []
    for transaction in transactions:
        result.append({
            "transaction_id": transaction.transactionId,
            "date": transaction.transactionDate.strftime("%Y-%m-%d") if transaction.transactionDate else None,
            "type": transaction.transactionType,
            "amount": str(transaction.amount),  
            "account": transaction.accountId,  
            "payee": transaction.payee,
            "method": transaction.method,
            "status": transaction.status,
            "consolidate_balance": str(transaction.consolidateBalance)
        })

    return {
        "status": True,
        "message": "",
        "data": result
    }




def read_payment_summary(customer_id: int, db):
    p_summary = db.query(PaymentSummary).filter(PaymentSummary.customerId == customer_id).first()
    
    if not p_summary:
        raise HTTPException(status_code=404, detail="No payment summary found for this customer")

    return p_summary



def read_cashflow_by_customer(customer_id: int, db):
    cashflow_data = db.query(CashFlow).filter(CashFlow.customerId == customer_id).all()
    
    if not cashflow_data:
        raise HTTPException(status_code=404, detail="No cashflow data found for this customer")

    cash_inflow = [entry.cashInflow for entry in cashflow_data]
    cash_outflow = [entry.cashOutflow for entry in cashflow_data]

    response = {
        "y-aixs": [
            {
                "name": "Cash Inflow",
                "data": cash_inflow
            },
            {
                "name": "Cash Outflow",
                "data": cash_outflow
            }
        ],
        "x-aixs": ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
    }
    return response



def read_income_expense_by_customer(customer_id: int, db):
    income_expense_data = db.query(IncomeExpense).filter(IncomeExpense.customerId == customer_id).all()

    if not income_expense_data:
        raise HTTPException(status_code=404, detail="No income/expense data found for this customer")
    income = [entry.income for entry in income_expense_data]
    expense = [entry.expense for entry in income_expense_data]

    response = {
        "y-aixs": [
            {
                "name": "Income",
                "data": income
            },
            {
                "name": "Expense",
                "data": expense
            }
        ],
        "x-aixs": ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
    }
    return response





def create_new_customer(customer_data: dict, db):
    try:
        if customer_data:
            new_customer = Customers(
            escrowVa=customer_data['escrow_va'],
            companyName=customer_data['company_name'],
            ifscCode=customer_data['ifsc_code'],
            gstIn=customer_data['gst_in'],
            vpa=customer_data['vpa'],
            buisnessCategory=customer_data['business_category'],
            swiftCode=customer_data['swift_code']
        )
        db.add(new_customer)  
        db.commit()           
        db.refresh(new_customer)  
        return {"message": "Customer overview created successfully", "customer_id": new_customer.customerID}
    
    except SQLAlchemyError as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail=str(e))


def create_new_account(account_data: dict, db):
    try:
        if account_data:
            new_account = BankAccounts(
            accountHolderName=account_data['account_holder_name'],
            bankName=account_data['bank_name'],
            accountNumber=account_data['account_number'],
            accountType=account_data['account_type'],
            ifscCode=account_data['ifsc_code'],
            branchLocation=account_data['branch_location'],
            linkedMobileNumber=account_data['linked_mobile_number'],
            accountNickname=account_data.get('account_nickname'),
            primaryCheck=account_data.get('primary_check', False), 
            createdAt=datetime.now()
        )
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return {"message": "Bank account created successfully", "account_id": new_account.accountId}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))





def get_added_beneficiaries(db):
    beneficiaries = db.query(Beneficiaries).all()
    response_data = [
        {
            "relation_to_beneficiary": beneficiary.relationToBeneficiary,
            "beneficiary_name": beneficiary.beneficiaryName,
            "percentage_allocation": beneficiary.percentageAllocation,
            "payment_amount": beneficiary.paymentAmount
        }
        for beneficiary in beneficiaries
    ]
    return {"status": True, "message": "Beneficiaries retrieved successfully", "data": response_data}


def read_consolidated_balance(customer_id,db):
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    today_balance = db.query(AccountBalances).filter(
        and_(
            AccountBalances.customerId == customer_id,
            AccountBalances.balanceDate == today.date()
        )
    ).first()

    
    yesterday_balance = db.query(AccountBalances).filter(
        and_(
            AccountBalances.customerId == customer_id,
            AccountBalances.balanceDate == yesterday.date()
        )
    ).first()

    
    today_total_account = today_balance.totalAccountBalance if today_balance else 0
    today_escrow_va_balance = today_balance.escrowVaBalance if today_balance else 0

   
    yesterday_total_account = yesterday_balance.totalAccountBalance if yesterday_balance else 0
    yesterday_escrow_va_balance = yesterday_balance.escrowVaBalance if yesterday_balance else 0

    
    return {
        "today_total_account": today_total_account,
        "today_balance": today_total_account,
        "today_escrow_va_balance": today_escrow_va_balance,
        "yesterday_total_account": yesterday_total_account,
        "yesterday_balance": yesterday_total_account,
        "yesterday_escrow_va_balance": yesterday_escrow_va_balance,
    }

def create_or_update_beneficiary(beneficiary_data: dict, db, beneficiary_id: int = None):
    try:
        if beneficiary_id:
           
            beneficiary = db.query(Beneficiaries).filter(Beneficiaries.beneficiaryId == beneficiary_id).first()
            
            if not beneficiary:
                raise HTTPException(status_code=404, detail="Beneficiary not found")

          
            for key, value in beneficiary_data.items():
                if hasattr(beneficiary, key):  
                    setattr(beneficiary, key, value)
            
        else:
           
            new_beneficiary = Beneficiaries(
                beneficiaryName=beneficiary_data['beneficiary_name'],
                bankName=beneficiary_data['bank_name'],
                percentageAllocation=beneficiary_data.get('percentage_allocation'),
                relationToBeneficiary=beneficiary_data['relation_to_beneficiary'],
                beneficiaryAccountNumber=beneficiary_data['beneficiary_account_number'],
                ifscCode=beneficiary_data['ifsc_code'],
                phoneNumber=beneficiary_data['phone_number'],
                beneficiaryNickname=beneficiary_data.get('beneficiary_nickname'),
                paymentAmount=beneficiary_data['payment_amount'],
                emailAddress=beneficiary_data['email_address'],
                primaryCheck=beneficiary_data.get('primary_check', False),
                agreeConditions=beneficiary_data.get('agree_conditions', True),
                createdAt=datetime.now()
            )
            db.add(new_beneficiary)  
        
        db.commit() 
        
        
        if beneficiary_id:
            return {"message": "Beneficiary updated successfully"}
        else:
            return {"message": "Beneficiary created successfully"}
    
    except SQLAlchemyError as e:
        db.rollback() 
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing required field: {str(e)}")
































































































