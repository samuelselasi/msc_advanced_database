# Database

## Create Database and User
```
CREATE DATABASE your_database_name;
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER ROLE your_username SET client_encoding TO 'utf8';
ALTER ROLE your_username SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
ALTER USER your_username WITH SUPERUSER;
```

## Create Tables
```
BEGIN;


CREATE TABLE IF NOT EXISTS public.category
(
    "categoryNo" serial NOT NULL,
    "categoryDescription" character varying COLLATE pg_catalog."default",
    CONSTRAINT category_pkey PRIMARY KEY ("categoryNo")
);

CREATE TABLE IF NOT EXISTS public.employee
(
    "employeeNo" serial NOT NULL,
    "employeeName" character varying COLLATE pg_catalog."default",
    "employeeCity" character varying COLLATE pg_catalog."default",
    "employeeState" character varying COLLATE pg_catalog."default",
    "employeeZipCode" character varying COLLATE pg_catalog."default",
    "employeeTelNo" character varying COLLATE pg_catalog."default",
    "employeeFaxNo" character varying COLLATE pg_catalog."default",
    "employeeEmailAddress" character varying COLLATE pg_catalog."default",
    CONSTRAINT employee_pkey PRIMARY KEY ("employeeNo")
);

CREATE TABLE IF NOT EXISTS public.orders
(
    "purchaseOrderNo" serial NOT NULL,
    "purchaseOrderDescription" character varying COLLATE pg_catalog."default",
    "orderDate" timestamp without time zone,
    "dateRequired" date NOT NULL,
    "shippedDate" date NOT NULL,
    "freightCharge" integer NOT NULL,
    "supplierNo" integer,
    "employeeNo" integer,
    CONSTRAINT orders_pkey PRIMARY KEY ("purchaseOrderNo")
);

CREATE TABLE IF NOT EXISTS public.products
(
    "productNo" serial NOT NULL,
    "productName" character varying COLLATE pg_catalog."default",
    "serialNo" character varying COLLATE pg_catalog."default",
    "unitPrice" integer NOT NULL,
    "quantityOnHand" integer NOT NULL,
    "reorderLevel" integer NOT NULL,
    "reorderQuantity" integer NOT NULL,
    "reorderLeadTime" integer NOT NULL,
    "categoryNo" integer,
    CONSTRAINT products_pkey PRIMARY KEY ("productNo")
);

CREATE TABLE IF NOT EXISTS public.supplier
(
    "supplierNo" serial NOT NULL,
    "supplierName" character varying COLLATE pg_catalog."default",
    "supplierCity" character varying COLLATE pg_catalog."default",
    "supplierState" character varying COLLATE pg_catalog."default",
    "supplierZipCode" character varying COLLATE pg_catalog."default",
    "suppTelNo" character varying COLLATE pg_catalog."default",
    "suppFaxNo" character varying COLLATE pg_catalog."default",
    "suppEmailAddress" character varying COLLATE pg_catalog."default",
    "suppWebAddress" character varying COLLATE pg_catalog."default",
    "contactName" character varying COLLATE pg_catalog."default",
    "contactTelNo" character varying COLLATE pg_catalog."default",
    "contactFaxNo" character varying COLLATE pg_catalog."default",
    "contactEmailAddress" character varying COLLATE pg_catalog."default",
    "paymentTerms" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT supplier_pkey PRIMARY KEY ("supplierNo")
);

CREATE TABLE IF NOT EXISTS public.transactions
(
    "transactionNo" serial NOT NULL,
    "transactionDate" timestamp without time zone,
    "transactionDescription" character varying COLLATE pg_catalog."default",
    "unitPrice" integer NOT NULL,
    "unitsOrdered" integer NOT NULL,
    "unitsReceived" integer NOT NULL,
    "unitsSold" integer NOT NULL,
    "unitsWastage" integer NOT NULL,
    "productNo" integer,
    "purchaseOrderNo" integer,
    CONSTRAINT transactions_pkey PRIMARY KEY ("transactionNo")
);

ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT "orders_employeeNo_fkey" FOREIGN KEY ("employeeNo")
    REFERENCES public.employee ("employeeNo") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT "orders_supplierNo_fkey" FOREIGN KEY ("supplierNo")
    REFERENCES public.supplier ("supplierNo") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.products
    ADD CONSTRAINT "products_categoryNo_fkey" FOREIGN KEY ("categoryNo")
    REFERENCES public.category ("categoryNo") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transactions
    ADD CONSTRAINT "transactions_productNo_fkey" FOREIGN KEY ("productNo")
    REFERENCES public.products ("productNo") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transactions
    ADD CONSTRAINT "transactions_purchaseOrderNo_fkey" FOREIGN KEY ("purchaseOrderNo")
    REFERENCES public.orders ("purchaseOrderNo") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;
```
