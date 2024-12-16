-- Start transaction
START TRANSACTION;

-- Create category table
CREATE TABLE IF NOT EXISTS `category` (
    `categoryNo` INT AUTO_INCREMENT NOT NULL,
    `categoryDescription` VARCHAR(255),
    PRIMARY KEY (`categoryNo`)
);

-- Create employee table
CREATE TABLE IF NOT EXISTS `employee` (
    `employeeNo` INT AUTO_INCREMENT NOT NULL,
    `employeeName` VARCHAR(255),
    `employeeCity` VARCHAR(255),
    `employeeState` VARCHAR(255),
    `employeeZipCode` VARCHAR(20),
    `employeeTelNo` VARCHAR(20),
    `employeeFaxNo` VARCHAR(20),
    `employeeEmailAddress` VARCHAR(255),
    PRIMARY KEY (`employeeNo`)
);

-- Create orders table
CREATE TABLE IF NOT EXISTS `orders` (
    `purchaseOrderNo` INT AUTO_INCREMENT NOT NULL,
    `purchaseOrderDescription` VARCHAR(255),
    `orderDate` DATETIME,
    `dateRequired` DATE NOT NULL,
    `shippedDate` DATE NOT NULL,
    `freightCharge` INT NOT NULL,
    `supplierNo` INT,
    `employeeNo` INT,
    PRIMARY KEY (`purchaseOrderNo`),
    FOREIGN KEY (`employeeNo`) REFERENCES `employee`(`employeeNo`) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (`supplierNo`) REFERENCES `supplier`(`supplierNo`) ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Create products table
CREATE TABLE IF NOT EXISTS `products` (
    `productNo` INT AUTO_INCREMENT NOT NULL,
    `productName` VARCHAR(255),
    `serialNo` VARCHAR(255),
    `unitPrice` INT NOT NULL,
    `quantityOnHand` INT NOT NULL,
    `reorderLevel` INT NOT NULL,
    `reorderQuantity` INT NOT NULL,
    `reorderLeadTime` INT NOT NULL,
    `categoryNo` INT,
    PRIMARY KEY (`productNo`),
    FOREIGN KEY (`categoryNo`) REFERENCES `category`(`categoryNo`) ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Create supplier table
CREATE TABLE IF NOT EXISTS `supplier` (
    `supplierNo` INT AUTO_INCREMENT NOT NULL,
    `supplierName` VARCHAR(255),
    `supplierCity` VARCHAR(255),
    `supplierState` VARCHAR(255),
    `supplierZipCode` VARCHAR(20),
    `suppTelNo` VARCHAR(20),
    `suppFaxNo` VARCHAR(20),
    `suppEmailAddress` VARCHAR(255),
    `suppWebAddress` VARCHAR(255),
    `contactName` VARCHAR(255),
    `contactTelNo` VARCHAR(20),
    `contactFaxNo` VARCHAR(20),
    `contactEmailAddress` VARCHAR(255),
    `paymentTerms` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`supplierNo`)
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS `transactions` (
    `transactionNo` INT AUTO_INCREMENT NOT NULL,
    `transactionDate` DATETIME,
    `transactionDescription` VARCHAR(255),
    `unitPrice` INT NOT NULL,
    `unitsOrdered` INT NOT NULL,
    `unitsReceived` INT NOT NULL,
    `unitsSold` INT NOT NULL,
    `unitsWastage` INT NOT NULL,
    `productNo` INT,
    `purchaseOrderNo` INT,
    PRIMARY KEY (`transactionNo`),
    FOREIGN KEY (`productNo`) REFERENCES `products`(`productNo`) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (`purchaseOrderNo`) REFERENCES `orders`(`purchaseOrderNo`) ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Commit the transaction
COMMIT;
