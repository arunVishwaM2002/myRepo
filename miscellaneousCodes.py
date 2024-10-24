# def read_cashflow(db):
#     cashflow_data = db.query(CashFlow).all()
    
#     cash_inflow = [entry.cashInflow for entry in cashflow_data]
#     cash_outflow = [entry.cashOutflow for entry in cashflow_data]

#     response = {
#         "y-aixs": [
#             {
#                 "name": "Cash Inflow",
#                 "data": cash_inflow
#             },
#             {
#                 "name": "Cash Outflow",
#                 "data": cash_outflow
#             }
#         ],
#         "x-aixs": ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
#     }
#     return response 



# def read_income_expense(db):
#     income_expense_data = db.query(IncomeExpense).all()

#     income = [entry.income for entry in income_expense_data]
#     expense = [entry.expense for entry in income_expense_data]

#     response = {
#         "y-aixs": [
#             {
#                 "name": "Income",
#                 "data": income
#             },
#             {
#                 "name": "Expense",
#                 "data": expense
#             }
#         ],
#         "x-aixs": ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
#     }
#     return response


# def create_or_update_beneficiary(beneficiary_data: dict, db, beneficiary_id: int = None):
#     try:
#         if beneficiary_id:
            
#             beneficiary = db.query(Beneficiaries).filter(Beneficiaries.beneficiaryId == beneficiary_id).first()
#             if not beneficiary:
#                 raise HTTPException(status_code=404, detail="Beneficiary not found")
            
            
#             for key, value in beneficiary_data.items():
#                 setattr(beneficiary, key, value)
#         else:
            
#             new_beneficiary = Beneficiaries(
#                 beneficiaryName=beneficiary_data['beneficiary_name'],
#                 bankName=beneficiary_data['bank_name'],
#                 percentageAllocation=beneficiary_data.get('percentage_allocation'),
#                 relationToBeneficiary=beneficiary_data['relation_to_beneficiary'],
#                 beneficiaryAccountNumber=beneficiary_data['beneficiary_account_number'],
#                 ifscCode=beneficiary_data['ifsc_code'],
#                 phoneNumber=beneficiary_data['phone_number'],
#                 beneficiaryNickname=beneficiary_data.get('beneficiary_nickname'),
#                 paymentAmount=beneficiary_data['payment_amount'],
#                 emailAddress=beneficiary_data['email_address'],
#                 primaryCheck=beneficiary_data.get('primary_check', False),
#                 agreeConditions=beneficiary_data.get('agree_conditions', True),
#                 createdAt=datetime.now()
#             )
#             db.add(new_beneficiary)
        
#         db.commit()
#         return {"message": "Beneficiary information saved successfully"}

#     except SQLAlchemyError as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=str(e))




# def read_payment_summary(skip,limit,db):
#     p_summary = db.query(PaymentSummary).filter(PaymentSummary.customerId==customer_id).first()
#     # p_summary=db.query(PaymentSummary).offset(skip).limit(limit).all()
#     if not p_summary:
#         raise HTTPException(status_code=404, detail="No Payment Summary Found")

#     result=[payment.__dict__ for payment in p_summary]

#     return result











# def read_payment_summary(customer_id,db):
#     p_summary = db.query(PaymentSummary).filter(PaymentSummary.customerId==customer_id).first()
#     # p_summary=db.query(PaymentSummary).offset(skip).limit(limit).all()
#     if not p_summary:
#         raise HTTPException(status_code=404, detail="No Payment Summary Found")

#     # result=[payment.__dict__ for payment in p_summary]

#     return p_summary


# def read_customers(skip,limit,db):
    
#     customers=db.query(Customers).offset(skip).limit(limit).all()
#     if not customers:
#         raise HTTPException(status_code=404, detail="No Customers Found")
        
#     result=[customer.__dict__ for customer in customers]

#     for r in result:
#         r.pop("_sa_instance_state", None)

#     return result


# from modules import Base,engine
# from sqlalchemy.orm import sessionmaker
# from modules.models import Customers

# Base.metadata.create_all(bind=engine)
# Session=sessionmaker(bind=engine)
# db=Session()
# customer_data={
#     "companyName": "bluswap",
#     "escrowVa":"bhbhbhsbhbhbcbshsbbs",
#     "ifscCode":"yqgwhdybh",
#     "gstIn":"bwjcbjbn",
#     "vpa":"bfehdhbchhhdv",
#     "buisnessCategory":"fintech",
#     "swiftCode":"ewbfchdbhdbh"
# }


# customer_one=Customers(**customer_data)
# db.add(customer_one)
# db.commit()
# db.refresh(customer_one)
# db.close()
