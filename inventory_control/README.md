# Inventory Control
![inventoryERD](https://github.com/user-attachments/assets/17cb9569-a766-4db1-80c6-7bdd1d8d0270)

> A company wishes to create a database to control its inventory,
which consits of a number of products divided into a number of categories,
such as clothing, food, and stationery. An employee raises a purchase order
when a product has to be recorded from the supplier.
The tracking supplies received, units sold, and any wastage.

## Product
* productNo
* productName
* serialNo
* unitPrice
* quantityOnHand
* reorderLevel
* reorderQuantity
* reorderLeadTime
* categoryNo

## Product Category
* CategoryNo
* categoryDescription

## Purchase Order
* purchaseOrderNo
* purchaseOrderDescription
* orderDate
* dateRequired
* shippedDate
* freightCharge
* supplierNo
* employeeNo

## Supplier
* supplierNo
* supplierName
* supplierStreet
* supplierCity
* supplierState
* supplierZipCode
* suppTelNo
* suppFaxNo
* suppEmailAddress
* suppWebAddress
* contactName
* contactTelNo
* contactFaxNo
* contactEmailAddress
* paymentTerms

## Transaction
* transactionNo
* transactionDate
* transactionDescription
* unitPrice
* unitsOrdered
* unitsReceived
* unitsSold
* unitsWastage
* productNo
* purchaseOrderNo

## Required
1. Draw an E/R model from the above list of tables, attributes, and key constraints.
2. Create a database. Create all the tables above taking into consideration the referential keys. Specify appropriate data types, field lengths and other constraints you find necessary.
3. Design a user interface in any object-oriented programming language.. Your interface should be linked to one or more tables through an API (connection string) to access the database.
4. On the user interface, provide at least four buttons;
	a. insert record
	b. retrieve record
	c. update record
	d. delet record
from the database table(s)
5. Write a program in your chosen object-oriented programming language to perform the appropriate tasks when the user clicks on the buttons in 4 above.
6. Use triggers to log user activities into a specific table.
