#docker run -p 3306:3306 --env MYSQL_ROOT_PASSWORD=root mysql:latest

#1. create database
CREATE DATABASE shop;

#2. create admin role
CREATE USER 'admin'@'localhost' IDENTIFIED by 'qwerty123';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';

#3. create viewer role
CREATE USER 'viewer'@'localhost';
GRANT SELECT ON *.* TO 'viewer'@'localhost';

#4. create category table
CREATE TABLE IF NOT EXISTS shop.category
(
	id int auto_increment,
	name varchar(255) not null,
	constraint category_pk
			primary key(id)
);

#5. insert new categories
INSERT INTO shop.category (name) VALUES ('cards'), ('balls'), ('something') , ('test');

#6. create a table for products
CREATE TABLE IF NOT EXISTS shop.product
(
	id int auto_increment,

	name varchar(255) not null,
	category_id int not null,
	price decimal(15,2),
	constraint product_pk
	    primary key (id),
	constraint product_category_id_fk
		foreign key (category_id) references category(id)
);

#7. insert products with price 100.00
INSERT INTO shop.product (name, category_id, price) VALUES ('thing1', 4, 100.00),
                                                           ('thing2', 3, 100.00),
                                                           ('thing3', 1, 100.00),
                                                           ('thing4', 2, 100.00),
                                                           ('thing5', 4, 100.00);

#8. change product price to 350.00
UPDATE shop.product SET price = 350.00 WHERE name='thing1';

#9. increase all prices to 10%
UPDATE shop.product SET price=price * 1.1;

#10. delete 2nd product
DELETE FROM shop.product WHERE name='thing2';

#11. select all products sorted by name
SELECT * FROM shop.product ORDER BY name;

#12. select all products sorted by price desc
SELECT * FROM shop.product ORDER BY price DESC;

#13. select 3 most expensive product
SELECT * FROM shop.product ORDER BY price DESC LIMIT 3;

#14. select 3 cheapest product
SELECT * FROM shop.product ORDER BY price LIMIT 3;

#15. select next 3 most expensive product
SELECT * FROM shop.product ORDER BY price DESC LIMIT 3,3;

#16. select name of most expensive product
SELECT name FROM shop.product ORDER BY price DESC LIMIT 1;

#17. select name of cheapest product
SELECT name FROM shop.product ORDER BY price LIMIT 1;

#18. select count of all products
SELECT count(*) FROM shop.product;

#19. select avg price for all products
SELECT avg(price) FROM shop.product;

#20. create view
CREATE VIEW  new_view AS SELECT * FROM shop.product ORDER BY price DESC LIMIT 3;