INSERT INTO customers ("companyName", "escrowVa", "ifscCode", "gstIn", "vpa", "buisnessCategory", "swiftCode")
VALUES ('ABC Corp', 'ESCROW123', 'IFSC0001', 'GST123456', 'vpa@abc', 'IT Services', 'SWIFT123');

SELECT * FROM customers;

INSERT INTO beneficiaries(
	"beneficiaryName",
	"relationToBeneficiary",
	"bankName",
	"beneficiaryAccountNumber",
	"ifscCode",
	"phoneNumber",
	"beneficiaryNickname",
	"percentageAllocation",
	"paymentAmount",
	"emailAddress",
	"primaryCheck",
	"agreeConditions"	
) VALUES(
"Olivia Garcia",
"Cousin",
"Omicron Bank",
"3456019876",
"OMICRON015",
"9876512345",
"Liv",
22.00,
2200.00,
"olivia.garcia@example.com",
TRUE,
FALSE
);

SELECT * FROM beneficiaries;

UPDATE beneficiaries
SET "customerId"=1
WHERE "beneficiaryId"=1;

UPDATE beneficiaries
SET "customerId"=2
WHERE "beneficiaryId"=2;

-- UPDATE beneficiaries
-- SET "customerId"=3
-- WHERE "beneficiaryId"=3;