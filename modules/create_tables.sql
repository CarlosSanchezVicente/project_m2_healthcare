-- CREATE TABLE 'patients'
CREATE TABLE patients (
	id_patient INT PRIMARY KEY,
   	name_patient VARCHAR ( 50 ) NOT NULL,
	age INT NOT NULL,
	gender VARCHAR ( 50 ) NOT NULL,
  	blood_type VARCHAR ( 50 ) NOT NULL,
  	medical_condition VARCHAR ( 50 ) NOT NULL,
  	date_admission TIMESTAMP  NOT NULL,
  	date_discharge TIMESTAMP  NOT NULL,
  	hospital_stay TIMESTAMP  NOT NULL,
  	room_number INT NOT NULL,
  	admission_type VARCHAR ( 50 ) NOT NULL,
  	test_result VARCHAR ( 50 ) NOT NULL,
  	billing_amount FLOAT NOT NULL,
  	years INT  NOT NULL,
  	id_hospital INT NOT NULL,
  	id_doctors INT NOT NULL,
  	id_medication INT NOT NULL,
  	id_provider INT NOT NULL
);

-- CREATE TABLE 'hospital'
CREATE TABLE hospital (
  	id_hospital INT PRIMARY KEY,
  	name_hospital VARCHAR ( 50 ) NOT NULL,
  	state VARCHAR ( 50 ) NOT NULL
);

-- CREATE TABLE 'doctors'
CREATE TABLE doctors (
  	id_doctors INT PRIMARY KEY,
  	name_doctors VARCHAR ( 50 ) NOT NULL,
  	medical_specialty VARCHAR ( 50 ) NOT NULL
);

-- CREATE TABLE 'medication'
CREATE TABLE medication (
  	id_medication INT PRIMARY KEY,
  	name_medication VARCHAR ( 50 ) NOT NULL,
  	medication_type VARCHAR ( 50 ) NOT NULL,
  	api VARCHAR ( 50 ) NOT NULL
);

-- CREATE TABLE 'insurance_provider'
CREATE TABLE insurance_provider (
  	id_provider INT PRIMARY KEY,
  	name_provider VARCHAR ( 50 ) NOT NULL
);

-- CREATE TABLE 'insurance_provider'
CREATE TABLE date (
  	years INT PRIMARY KEY,
  	start_date TIMESTAMP NOT NULL,
  	end_date TIMESTAMP NOT NULL,
  	fiscal_year VARCHAR NOT NULL
);