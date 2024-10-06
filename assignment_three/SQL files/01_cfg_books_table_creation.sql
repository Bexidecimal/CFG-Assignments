-- CREATE DATABASE cfg_books;
-- USE cfg_books;

CREATE TABLE genre(
genre_id int PRIMARY KEY AUTO_INCREMENT,
genre varchar (255) NOT NULL UNIQUE
);

CREATE TABLE author(
author_id int PRIMARY KEY AUTO_INCREMENT,
first_name varchar (255) NOT NULL,
last_name varchar (255) NOT NULL
);

CREATE TABLE customer(
customer_id int PRIMARY KEY AUTO_INCREMENT,
title varchar(3),
first_name varchar (255) NOT NULL,
last_name varchar (255) NOT NULL,
membership_no int UNIQUE,
email varchar (255) UNIQUE NOT NULL
);

CREATE TABLE customer_contact(
contact_id int(10) PRIMARY KEY AUTO_INCREMENT,
customer_id int NOT NULL,
phone_no varchar (15),
address_no int NOT NULL,
address_line_1 varchar(255) NOT NULL,
address_line_2 varchar (255) NOT NULL,
city varchar (255) NOT NULL,
postcode varchar (8) NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE book (
isbn varchar (17) PRIMARY KEY,
title varchar (255) NOT NULL,
book_description text NOT NULL,
author_id int NOT NULL,
genre_id int NOT NULL,
price decimal (5,2) NOT NULL,
FOREIGN KEY (author_id) REFERENCES author (author_id),
FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
);

CREATE TABLE order_summary(
order_id int PRIMARY KEY AUTO_INCREMENT,
customer_id int NOT NULL,
contact_id int NOT NULL,
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
FOREIGN KEY (contact_id) REFERENCES customer_contact (contact_id)
);

CREATE TABLE order_item(
order_item_id int PRIMARY KEY AUTO_INCREMENT,
order_id int NOT NULL,
isbn varchar (17) NOT NULL UNIQUE,
shipped BOOLEAN NOT NULL,
FOREIGN KEY (order_id) REFERENCES order_summary (order_id),
FOREIGN KEY (isbn) REFERENCES book (isbn)
);
