CREATE TABLE chemelm(
	id serial PRIMARY KEY,
	elm_name VARCHAR (50) UNIQUE NOT NULL
);

CREATE TABLE commodity(
	id serial PRIMARY KEY,
	comm_name VARCHAR (50) UNIQUE NOT NULL,
	inventory  integer,
	price integer,
	chemical_composition []
);