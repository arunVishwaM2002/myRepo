SELECT * FROM customers;
SELECT * FROM beneficiaries;
SELECT * FROM bank_accounts;
SELECT * FROM cash_flow;
SELECT * FROM income_expense;
SELECT * FROM payment_summary;
SELECT * FROM transactions;

UPDATE bank_accounts
SET "customerId"=1
WHERE "accountId"=1;

UPDATE bank_accounts
SET "customerId"=2
WHERE "accountId"=2;


