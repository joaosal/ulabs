# Setup database for Data Analyst Exercises
DROP DATABASE IF EXISTS dualcore;
CREATE DATABASE dualcore;

USE dualcore;

-- # setup employees table
CREATE TABLE employees (
	emp_id CHAR(9) PRIMARY KEY NOT NULL,
	fname VARCHAR(15) NULL,
	lname VARCHAR(20) NULL,
	address VARCHAR(40) NULL,
	city VARCHAR(30) NULL,
	state CHAR(2) NULL,
	zipcode CHAR(5) NULL,
	job_title VARCHAR(35) NULL,
	email VARCHAR(25) NULL,
	active CHAR(1) NOT NULL default 'Y',
	salary INT NULL
);

LOAD DATA LOCAL INFILE 'employees.txt' INTO TABLE dualcore.employees;


-- # setup products table
CREATE TABLE products (
	prod_id INT PRIMARY KEY NOT NULL,
	brand VARCHAR(20) NULL,
	name VARCHAR(75) NULL,
	price INT NULL,
	cost INT NULL,
	shipping_wt SMALLINT NULL
);

LOAD DATA LOCAL INFILE 'products.txt' INTO TABLE dualcore.products;


-- # setup customers table
CREATE TABLE customers (
	cust_id INT PRIMARY KEY NOT NULL,
	fname VARCHAR(15) NULL,
	lname VARCHAR(20) NULL,
	address VARCHAR(40) NULL,
	city VARCHAR(30) NULL,
	state CHAR(2) NULL,
	zipcode CHAR(5) NULL
);

LOAD DATA LOCAL INFILE 'customers.txt' INTO TABLE dualcore.customers;


-- # setup orders table
CREATE TABLE orders (
	order_id INT PRIMARY KEY NOT NULL,
	cust_id INT NOT NULL,
	order_date DATETIME NOT NULL
);

LOAD DATA LOCAL INFILE 'orders.txt'
	INTO TABLE dualcore.orders (order_id, cust_id, @order_date)
	SET order_date = STR_TO_DATE(@order_date,'%m-%d-%Y %H:%i:%s');

-- # setup order_details table
CREATE TABLE order_details (
	order_id INT NOT NULL,
	prod_id INT NOT NULL
);

LOAD DATA LOCAL INFILE 'order_details.txt' INTO TABLE dualcore.order_details;

-- # setup suppliers table
CREATE TABLE suppliers (
    supp_id INT PRIMARY KEY NOT NULL,
    company VARCHAR(60) NULL,
    contact VARCHAR(60) NULL,
    address VARCHAR(50) NULL,
    city VARCHAR(30) NULL,
    state CHAR(2) NULL,
    zipcode CHAR(2) NULL,
    phone CHAR(14) NULL
);

LOAD DATA LOCAL INFILE 'suppliers.txt' INTO TABLE dualcore.suppliers;
