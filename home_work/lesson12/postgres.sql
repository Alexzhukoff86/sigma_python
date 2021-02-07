--docker run -e POSTGRES_PASSWORD=app postgres

--1. create database
CREATE DATABASE shop;

--2. create admin role
CREATE ROLE admin PASSWORD 'qwerty123';
GRANT ALL ON SCHEMA public TO admin;

--3. create viewer role
CREATE ROLE viewer NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN PASSWORD 'qwerty123';
GRANT USAGE ON SCHEMA public TO viewer;

--4. create category table
CREATE TABLE IF NOT EXISTS category
(
	id serial not null,
	name varchar(255) not null,
	constraint category_pk
			primary key(id)
);

--5. insert new categories
INSERT INTO category (name) VALUES ('cards'), ('balls'), ('something') , ('test');

--6. create a table for products
CREATE TABLE IF NOT EXISTS product
(
	id serial not null,

	name varchar(255) not null,
	category_id int not null,
	price money,
	constraint product_pk
	    primary key (id),
	constraint product_category_id_fk
		foreign key (category_id) references category(id)
);

--7. insert products with price 100.00
INSERT INTO product (name, category_id, price) VALUES ('thing1', 4, 100.00),
                                                      ('thing2', 3, 100.00),
                                                      ('thing3', 5, 100.00),
                                                      ('thing4', 6, 100.00),
                                                      ('thing5', 4, 100.00);

--8. change product price to 350.00
UPDATE product SET price = 350.00 WHERE name='thing1';

--9. increase all prices to 10%
UPDATE product SET price=price * 1.1;

--10. delete 2nd product
DELETE FROM product WHERE name='thing2';

--11. select all products sorted by name
SELECT * FROM product ORDER BY name;

--12. select all products sorted by price desc
SELECT * FROM product ORDER BY price DESC;

--13. select 3 most expensive product
SELECT * FROM product ORDER BY price DESC LIMIT 3;

--14. select 3 cheapest product
SELECT * FROM product ORDER BY price LIMIT 3;

--15. select next 3 most expensive product
SELECT * FROM product ORDER BY price DESC OFFSET 3 LIMIT 3;

--16. select name of most expensive product
SELECT name FROM product ORDER BY price DESC LIMIT 1;

--17. select name of cheapest product
SELECT name FROM product ORDER BY price LIMIT 1;

--18. select count of all products
SELECT count(*) FROM product;

--19. select avg price for all products
SELECT avg(price::numeric) FROM product;

--20. create view
CREATE VIEW  new_view AS
    SELECT * FROM product ORDER BY price DESC LIMIT 3;
