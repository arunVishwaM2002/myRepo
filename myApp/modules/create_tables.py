
from sqlalchemy.orm import sessionmaker
from models import  Customers, Beneficiaries, BankAccounts, Transactions, PaymentSummary, IncomeExpense, CashFlow, AccountBalances
from datetime import datetime
from modules import Base,engine


# CashFlow.__table__.drop(engine, checkfirst=True)
# IncomeExpense.__table__.drop(engine, checkfirst=True)
# PaymentSummary.__table__.drop(engine, checkfirst=True)
# Transactions.__table__.drop(engine, checkfirst=True)
# BankAccounts.__table__.drop(engine, checkfirst=True)
# Beneficiaries.__table__.drop(engine, checkfirst=True)
# Customers.__table__.drop(engine, checkfirst=True)
# AccountBalances.__table__.drop(engine, chekfirst=True)

# Create all tables
# Base.metadata.drop_all(engine,checkfirst=True, cascade=True)
Base.metadata.create_all(engine)

# # Create a session
Session = sessionmaker(bind=engine)
session = Session()

# # Adding one row for each model

# # Add a customer
customer = Customers(
    companyName="ABC Corp",
    escrowVa="ESCROW123",
    ifscCode="IFSC0001",
    gstIn="GST123456",
    vpa="vpa@abc",
    buisnessCategory="IT Services",
    swiftCode="SWIFT123"
)
# session.add(customer)
# session.commit()

# # # Add a beneficiary
beneficiary = Beneficiaries(
    customerId=customer.customerID,
    beneficiaryName="John Doe",
    relationToBeneficiary="Friend",
    bankName="XYZ Bank",
    beneficiaryAccountNumber="123456789",
    ifscCode="IFSC0002",
    phoneNumber="1234567890",
    beneficiaryNickname="Johnny",
    percentageAllocation=50.00,
    paymentAmount=1000.00,
    emailAddress="john.doe@example.com",
    primaryCheck=True,
    agreeConditions=True
)
session.add(beneficiary)
session.commit()

# # # Add a bank account
bank_account = BankAccounts(
    customerId=customer.customerID,
    accountHolderName="ABC Corp",
    bankName="XYZ Bank",
    accountNumber="987654321",
    accountType="Current",
    ifscCode="IFSC0003",
    branchLocation="City Branch",
    linkedMobileNumber="0987654321",
    accountNickname="Main Account",
    accountBalance=50000.00,
    primaryCheck=True
)
session.add(bank_account)
session.commit()

# # # Add a transaction
transaction = Transactions(
    customerId=customer.customerID,
    accountId=bank_account.accountId,
    transactionType="Credit",
    transactionDate=datetime.now().date(),
    amount=1000.00,
    payee="John Doe",
    method="Bank Transfer",
    status=True,
    consolidateBalance=51000.00
)
session.add(transaction)

# # # Add an account balance
account_balance = AccountBalances(
    customerId=customer.customerID,
    totalAccountBalance=50000.00,
    escrowVaBalance=10000.00,
    balanceDate=datetime.now().date()
)
session.add(account_balance)

# # # Add a payment summary
payment_summary = PaymentSummary(
    customerId=customer.customerID,
    date=datetime.now().date(),
    todayCreditAmount=2000.00,
    todayDebitAmount=500.00,
    todayCreditTransactions=1,
    todayDebitTransactions=1,
    yesterdayCreditAmount=1500.00,
    yesterdayDebitAmount=300.00,
    yesterdayCreditTransactions=1,
    yesterdayDebitTransactions=1
)
session.add(payment_summary)

# # # Add an income expense record
income_expense = IncomeExpense(
    customerId=customer.customerID,
    dayOfWeek="Monday",
    income=3000.00,
    expense=1000.00
)
session.add(income_expense)

# # # Add a cashflow record
cashflow = CashFlow(
    customerId=customer.customerID,
    dayOfWeek="Monday",
    cashInflow=3000.00,
    cashOutflow=1000.00
)
session.add(cashflow)

# # # Commit all changes
session.commit()

# # # Close the session


session.close()

















































































