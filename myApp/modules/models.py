from sqlalchemy import Column,Integer,VARCHAR,ForeignKey,DECIMAL,Boolean,TIMESTAMP,DateTime
from modules import Base,engine
from sqlalchemy.orm import relationship
from datetime import datetime

class Customers(Base):
    __tablename__="customers"

    customerID=Column(Integer,primary_key=True, index=True,autoincrement=True)
    companyName=Column(VARCHAR(255),nullable=False)
    escrowVa=Column(VARCHAR(255),nullable=False)
    ifscCode=Column(VARCHAR(20),nullable=False)
    gstIn=Column(VARCHAR(20),nullable=False)
    vpa=Column(VARCHAR(255),nullable=False)
    buisnessCategory=Column(VARCHAR(255),nullable=False)
    swiftCode=Column(VARCHAR(20),nullable=False)
    ## Relationships
    beneficiaries = relationship("Beneficiaries", back_populates="customer")
    bankAccounts=relationship("BankAccounts",back_populates="customer")
    transactions = relationship("Transactions", back_populates="customer")
    accountBalances = relationship("AccountBalances", back_populates="customer")
    paymentSummary = relationship("PaymentSummary", back_populates="customer")
    cashflows=relationship("CashFlow",back_populates="customer")
    incomeExpenses=relationship("IncomeExpense",back_populates="customer")

class Beneficiaries(Base):
    __tablename__ = "beneficiaries"

    beneficiaryId = Column(Integer, primary_key=True,autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    beneficiaryName = Column(VARCHAR(255))
    relationToBeneficiary = Column(VARCHAR(100))
    bankName = Column(VARCHAR(255))
    beneficiaryAccountNumber = Column(VARCHAR(50), nullable=False)
    ifscCode = Column(VARCHAR(11))
    phoneNumber = Column(VARCHAR(15))
    beneficiaryNickname = Column(VARCHAR(50))
    percentageAllocation = Column(DECIMAL(5, 2))
    paymentAmount = Column(DECIMAL(15, 2))
    emailAddress = Column(VARCHAR(255))
    primaryCheck = Column(Boolean, default=False)
    agreeConditions = Column(Boolean, default=True)
    createdAt = Column(TIMESTAMP,default=datetime.now)
    ## Relationships
    customer = relationship("Customers", back_populates="beneficiaries")

class BankAccounts(Base):
    __tablename__ = "bank_accounts"

    accountId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    accountHolderName = Column(VARCHAR(255))
    bankName = Column(VARCHAR(255))
    accountNumber = Column(VARCHAR(50))
    accountType = Column(VARCHAR(50))
    ifscCode = Column(VARCHAR(11))
    branchLocation = Column(VARCHAR(255))
    linkedMobileNumber = Column(VARCHAR(15))
    accountNickname = Column(VARCHAR(50), nullable=True)
    accountBalance = Column(DECIMAL(15, 2))
    primaryCheck = Column(Boolean, default=False)
    createdAt = Column(TIMESTAMP, default=datetime.now)
    ## Relationships
    customer = relationship("Customers", back_populates="bankAccounts")
    transactions = relationship("Transactions", back_populates="bankAccounts")

class Transactions(Base):
    __tablename__="transactions"

    transactionId = Column(Integer, primary_key=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    accountId = Column(Integer, ForeignKey("bank_accounts.accountId"), nullable=True)
    transactionType = Column(VARCHAR(10))  
    transactionDate = Column(DateTime)
    amount = Column(DECIMAL(15, 2))
    payee = Column(VARCHAR(255))
    method = Column(VARCHAR(50))  
    status = Column(Boolean,default=True)
    consolidateBalance = Column(DECIMAL(15, 2))
    createdAt = Column(TIMESTAMP, default=datetime.now)
    ## Relationships

    customer = relationship("Customers", back_populates="transactions")
    bankAccounts = relationship("BankAccounts", back_populates="transactions")

class PaymentSummary(Base):
    __tablename__ = "payment_summary"

    summaryId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    date = Column(DateTime)
    todayCreditAmount = Column(DECIMAL(15, 2))
    todayDebitAmount = Column(DECIMAL(15, 2))
    todayCreditTransactions = Column(Integer)
    todayDebitTransactions = Column(Integer)
    yesterdayCreditAmount = Column(DECIMAL(15, 2))
    yesterdayDebitAmount = Column(DECIMAL(15, 2))
    yesterdayCreditTransactions = Column(Integer)
    yesterdayDebitTransactions = Column(Integer)
    createdAt = Column(TIMESTAMP, default=datetime.now)
    ##Relationship
    customer = relationship("Customers", back_populates="paymentSummary")

class IncomeExpense(Base):
    __tablename__ = "income_expense"

    incomeExpenseId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    dayOfWeek = Column(VARCHAR(10))
    income = Column(DECIMAL(15, 2))
    expense = Column(DECIMAL(15, 2))
    createdAt = Column(TIMESTAMP, default=datetime.now)
    ## Relationship
    customer = relationship("Customers", back_populates="incomeExpenses")

class CashFlow(Base):
    __tablename__ = "cash_flow"

    cashflowId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    dayOfWeek = Column(VARCHAR(10))
    cashInflow = Column(DECIMAL(15, 2))
    cashOutflow = Column(DECIMAL(15, 2))
    createdAt = Column(TIMESTAMP, default=datetime.now)

    customer = relationship("Customers", back_populates="cashflows")

class AccountBalances(Base):
    __tablename__ = "account_balances"

    balanceId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey("customers.customerID"), nullable=True)
    totalAccountBalance = Column(DECIMAL(15, 2))
    escrowVaBalance = Column(DECIMAL(15, 2))
    balanceDate = Column(DateTime)
    createdAt = Column(TIMESTAMP, default=datetime.now)

    customer = relationship("Customers", back_populates="accountBalances")
