CREATE DATABASE halloween_monsters;
USE halloween_monsters;

CREATE TABLE country (
country_id int PRIMARY KEY AUTO_INCREMENT,
country varchar(255) UNIQUE NOT NULL
);

CREATE TABLE halloween_monster(
monster_id int PRIMARY KEY AUTO_INCREMENT,
monster_name varchar (255) NOT NULL,
country_id int NOT NULL,
weakness varchar (255),
favourite_food varchar (255),
identifying_features varchar(255),
url varchar (255),
FOREIGN KEY (country_id) REFERENCES country(country_id)
);

INSERT INTO country (country) VALUES
('Haiti'),
('Greece'),
('Romania'),
('America'),
('Unknown');

INSERT INTO halloween_monster (monster_name, country_id, weakness, favourite_food, identifying_features, URL) VALUES
('Witch',5,'Water','Frogs legs','Pointy hat','https://en.wikipedia.org/whttps://www.parliament.uk/about/living-heritage/transformingsociety/private-lives/religion/overview/witchcraft/iki/Witchcraft'),
('Vampire',3,'Stake to the heart','Human blood','Pointy fangs','https://shorturl.at/kCal3'),
('Werewolf',2,'Silver bullet','Raw meat','Lots of pointy teeth','https://www.beano.com/facts/general-knowledge/werewolf-facts'),
('Zombie',1,'Loss of head','Human Flesh','Shuffling and groaning','https://www.thefactsite.com/zombie-facts/'),
('Swamp Monster',4,'Fire','Alligators','They smell terrible','https://en.wikipedia.org/wiki/List_of_swamp_monsters#:~:text=6%20References-,Description,folklore%20and%20different%20media%20appearances.'),
('Invisible man',5,'Flour','Cheeseburgers',NULL,'https://en.wikipedia.org/wiki/Invisible_Man');

