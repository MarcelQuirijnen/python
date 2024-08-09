/*
DROP TABLE contractors;
DROP TABLE clients;
DROP TABLE invoices;
DROP TABLE rate_plans;
DROP TABLE business_rules;
*/

/*
CREATE DATABASE hh;
CREATE USER 'hh'@'localhost' IDENTIFIED BY 'hh';
GRANT ALL PRIVILEGES ON hh.* TO 'hh'@'localhost';
FLUSH PRIVILEGES;
*/

CREATE TABLE IF NOT EXISTS contractors (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(10) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	address1 VARCHAR(50) NOT NULL,
	address2 VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	zip VARCHAR(5) NOT NULL,
	state VARCHAR(2) NOT NULL,
	phone VARCHAR(15) NOT NULL,
	email VARCHAR(25),
	startdate date not null,
	UpdatedTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	UNIQUE KEY k_name (firstname, lastname)
);

insert into contractors values (null, 'Sandra','Fleming', '','','','','AR','','', now(), null);
insert into contractors values (null, 'Dayna','Quirijnen', '','','','','AR','','', now(), null);
insert into contractors values (null, 'Brandon','Davisson', '','','','','AR','','', now(), null);
insert into contractors values (null, 'Kelly','Hunter', '','','','','AR','','', now(), null);

CREATE TABLE IF NOT EXISTS clients (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(10) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	address1 VARCHAR(50) NOT NULL,
	address2 VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	zip VARCHAR(5) NOT NULL,
	state VARCHAR(2) NOT NULL,
	phone VARCHAR(15) NOT NULL,
	plan_id INTEGER UNSIGNED,
	startdate date not null,
	updatedtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

insert into clients values (null, 'Dr. Oran','Carter', '','','','','AR','',0,now(),null);

CREATE TABLE IF NOT EXISTS rate_plans (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	plan VARCHAR(25) NOT NULL,
	client_billrate DECIMAL(5,2) not null,
	client_billrate_unit VARCHAR(2) not null,
	contractor_payrate DECIMAL(5,2) not null,
	contractor_payrate_unit VARCHAR(2) not null,
	comments tinytext,
	updatedtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

insert into rate_plans values (null, 'Day shift', 12.50, 'hr', 9, 'hr', '8 hour day shift', null);
insert into rate_plans values (null, 'Overtime', 18.80, 'hr', 13.50, 'hr', 'Overtime rate', null);
insert into rate_plans values (null, 'Holiday', 25.00, 'hr', 18.00, 'hr', 'Holiday rate', null);
insert into rate_plans values (null, 'Overnite', 181.00, 'shift', 130.00, 'shift', 'Overnight rate, 16 hour shift', null);
insert into rate_plans values (null, '24H', 225.00, 'shift', 162.00, 'shift', '24 hour shift', null);
insert into rate_plans values (null, '2 person', 150.00, 'shift', 108.00, 'shift', 'husband + wife day shift', null);
insert into rate_plans values (null, 'Early Bird', 56.00, 'shift', 40.00, 'shift', 'Early Bird, 4 hour morning shift', null);
insert into rate_plans values (null, 'Tuck-In', 56.00, 'shift', 40.00, 'shift', 'Tuck-in, 4 hour evening shift', null);
insert into rate_plans values (null, '4 hour shift', 50.00, 'shift', 36.00, 'shift', '1/2 day shift', null);

CREATE TABLE IF NOT EXISTS business_rules (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	days_a_week	INTEGER UNSIGNED NOT NULL,
	weeks_a_month INTEGER UNSIGNED NOT NULL,
	weeks_a_year INTEGER UNSIGNED NOT NULL,
	hours_a_day INTEGER UNSIGNED NOT NULL,
	base_rate_caregiver decimal(2,1) not null,
	overtime_perc decimal(4,1) not null,
	holiday_perc decimal(4,1) not null,
	overnite_perc decimal(3,1) not null,
	twenty4hour_perc decimal(3,1) not null,
	se_tax_perc decimal(3,1) not null,
	two_pers_perc decimal(4,1) not null,
	updatedtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

insert into business_rules values (null, 5, 4, 52, 8, 12.5, 150.0, 200.0, 90.0, 75.0, 15.3, 150.0, now());

