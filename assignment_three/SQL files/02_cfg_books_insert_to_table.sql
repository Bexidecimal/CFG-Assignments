-- USE cfg_books;

-- INSERT INTO author (author_id, first_name, last_name)
-- VALUES
-- (1, "Christopher", "Paolini"),
-- (2, "Sarah", "Penner"),
-- (3, "Darren", "Shan"),
-- (4, "Andy", "Weir"),
-- (5, "Katherine", "Rundell"),
-- (6, "David", "Mitchell"),
-- (7, "Lesley", "Downer"),
-- (8, "Kanehito", "Yamada"),
-- (9, "Claire", "Douglas"),
-- (10, "Stephen", "King"),
-- (11, "Susan", "Hill"),
-- (12, "Elly", "Griffiths"),
-- (13, "Barbara", "Erskine"),
-- (14, "Hannah", "Grace"),
-- (15, "Moira", "Buffini");

-- INSERT INTO genre (genre_id, genre)
-- VALUES
-- (1, "fantasy"),
-- (2, "Romance"),
-- (3, "Science-fiction"),
-- (4, "Thriller"),
-- (5, "Horror"),
-- (6, "Non-fiction"),
-- (7, "Self help"),
-- (8, "Manga"),
-- (9, "Childrens"),
-- (10, "Young adult"),
-- (11, "Mystery"),
-- (12, "Historical fiction");


-- INSERT INTO book (isbn, title, book_description, author_id, genre_id, price)
-- VALUES
-- ("978-0-37-582668-9", "Eragon", "When Eragon finds a polished blue stone in the forest, he thinks it is the lucky discovery of a poor farm boy; perhaps it will buy his family meat for the winter. But when the stone brings a dragon hatchling, Eragon soon realizes he has stumbled upon a legacy nearly as old as the Empire itself.", 1, 1, 7.49),
-- ("978-1-48-807749-4", "The lost apothecary", "A female apothecary secretly dispenses poisons to liberate women from the men who have wronged them - setting three lives across centuries on a dangerous collision course.", 2,11,12.99),
-- ("978-0-31-660684-4", "The vampires assistant", "Darren Shan was just an ordinary schoolboy - until his visit to the Cirque Du Freak. Now, as he struggles with his new life as a Vampire's Assistant, he tries desperately to resist the one temptation that sickens him, the one thing that can keep him alive. But destiny is calling... the Wolf Man is waiting.", 3, 9, 5.49),
-- ("978-0-59-313521-1", "Project Hail Mary", "Ryland Grace is the sole survivor on a desperate, last-chance mission—and if he fails, humanity and the earth itself will perish.Except that right now, he doesn’t know that. He can’t even remember his own name, let alone the nature of his assignment or how to complete it.", 4, 3, 10.00),
-- ("978-0-59-380986-0", "Impossible creatures", "The day Christopher saved a drowning baby griffin from a hidden lake would change his life forever. It’s the day he learned about the Archipelago, a cluster of unmapped islands where magical creatures of every kind have thrived for thousands of years—until now. And it’s the day he met Mal, a girl on the run who desperately needs his help.", 5, 1, 16.95),
-- ("978-1-40-595318-4", "Unruly", "In Unruly , David Mitchell explores how early England’s monarchs, while acting as feared rulers firmly guiding their subjects’ destinies, were in reality a bunch of lucky bastards who were mostly as silly and weird in real life as they appear to us today in their portraits.", 6, 6, 10.56),
-- ("978-1-76-064385-0", "The shortest history of Japan", "Zen, haiku, martial arts, sushi, anime, manga, film, video games . . . Japanese culture has long enriched our Western way of life. Yet from a Western perspective, Japan remains a remote island country that has long had a complicated relationship with the outside world.", 7, 6, 12.45),
-- ("978-1-97-472576-2", "Frieren: Beyond journey's end", "Elf mage Frieren and her courageous fellow adventurers have defeated the Demon King and brought peace to the land. But Frieren will long outlive the rest of her former party. How will she come to understand what life means to the people around her?", 8, 8, 9.85),
-- ("978-1-40-595759-5", "The wrong sister", "Tasha has always felt in the shadow of her older sister, Alice. Their lifestyles couldn't be more different; Alice is married to wealthy entrepreneur Kyle and has a high-flying career, Tasha is married to her childhood sweetheart and lives in a Bristol suburb with their four-year-old twins.", 9, 4, 8.10),
-- ("978-0-34-580678-9", "The shining", "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister. And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.", 10, 5, 6.90),
-- ("978-0-09-928847-3", "The woman in black", "Set on the obligatory English moor, on an isolated causeway, the story has as its hero Arthur Kipps, an up-and-coming young solicitor who has come north from London to attend the funeral and settle the affairs of Mrs. Alice Drablow of Eel Marsh House. The routine formalities he anticipates give way to a tumble of events and secrets more sinister and terrifying than any nightmare: the rocking chair in the deserted nursery, the eerie sound of a pony and trap, a child's scream in the fog, and most dreadfully--and for Kipps most tragically--The Woman In Black", 11, 5, 4.99),
-- ("978-0-54-738606-5", "The crossing places", "When she's not digging up bones or other ancient objects, quirky, tart-tongued archaeologist Ruth Galloway lives happily alone in a remote area called Saltmarsh near Norfolk, land that was sacred to its Iron Age inhabitants—not quite earth, not quite sea.", 12, 11, 8.20),
-- ("978-0-00-856091-1", "The story spinner", "Elen is a princess promised to a general of Rome. Macsen came to Wales seeking an alliance that would advance his quest for power. Despite warnings her marriage is destined for heartache, Elen is determined to honour her vows. But this union will change her destiny forever", 13, 12, 4.50),
-- ("978-1-39-852574-0", "Daydream", "The third in the New York Times bestselling Maple Hills series follows fan-favorite Henry and a bookish fellow student who come up with a plan to help them both overcome their respective challenges in a difficult year.", 14, 2, 12.50),
-- ("978-0-57-138566-9", "Songlight", "Elsa is used to hiding the most important parts of herself—her feelings for Rye, her distaste for a world ruled by men, and, most crucially, her gift of songlight. She buries that secret deep inside. In Brightland, those with songlight are called Unhumans and are abhorred. Rye is the only other person Elsa has known with songlight, and their shared bond has brought them together.", 15, 3, 14.50);

-- INSERT INTO customer (title, first_name, last_name, membership_no, email) 
-- VALUES
-- ('Mr', 'Eragon', 'Bromsson', 100, 'dragon_rider@cfg.com'),
-- ('Ms', 'Mona', 'Baker', 101, 'bread4lyfe@cfg.com'),
-- (NULL, 'Lemony', 'Snicket', NULL, 'Lemon_man@cfg.com'),
-- ('Mrs', 'Adie', 'La-Rue', NULL, 'invisible@cfg.com'), -- I ran this and realised that I had put a constraint of 3 characters on my title column.
-- ('Mr', 'Ryland', 'Grace', 102, 'Stuck_in_space@cfg.com'),
-- ('Ms', 'Elena', 'Danvers', NULL, 'Elena.Danvers@cfg.com'),
-- ('Mr','Harold','Fry',NULL,'Wandering@cfg.com'),
-- ('Mr', 'Larten', 'Crepsley', NULL, 'Madame_octa@cfg.com');

-- INSERT INTO customer_contact (contact_id, customer_id, phone_no, address_no, address_line_1, address_line_2, city,postcode) -- Doesn't work
-- VALUES
-- (1, 9, "07938728116", 17, "Saphira Street", "Wistaston", "Crewe", "CW1 1AH"),  
-- (2 ,10 ,"07843127398", 24, "Yeast Lane", "Scapa", "Kirkwall", "KW1 4UQ"),
-- (3, 11, NULL, 3, "Unfortunate Drive", "Caldmore", "Walsall", "WS1 1PW"),  
-- (4, 12, "07998832718", 145, "Blank Close", "Hounslow", "London", "W10 4LP"),  
-- (5, 13, "07666391844", 189, "Starlight Street", "Horfield", "Bristol", "BR1 1RX"), 
-- (6, 14, "07080133425", 21, "Moonlight Street", "Norwood", "Croydon", "CR0 0PG"), 
-- (7, 15, "07183291844", 92, "Chip Alley", "Stuppington", "Canterbury", "CT1 1NW"),  
-- (8, 16, NULL, 12, "Mountain Drive", "Derker", "Oldham", "OL1 1HB");

-- INSERT INTO order_summary (order_id, customer_id, contact_id, order_date) 
-- VALUES
-- (1, 10, 2, "2024-09-05"),
-- (2, 12, 4, "2024-09-10"),
-- (3, 15, 7, "2024-09-12"),
-- (4, 10, 2, "2024-09-12"),
-- (5, 16, 8, "2024-09-13"),
-- (6, 9, 1, "2024-09-20"),
-- (7, 14, 6, "2024-09-21"),
-- (8, 13, 5, "2024-09-22");


-- INSERT INTO order_item (order_item_id, order_id, isbn, shipped) 
-- VALUES
-- (1, 1, "978-0-59-380986-0", TRUE),
-- (2, 1, "978-0-57-138566-9", TRUE),
-- (3, 2, "978-1-48-807749-4", FALSE),
-- (4, 3, "978-0-37-582668-9", TRUE),
-- (5, 3, "978-0-09-928847-3", TRUE),
-- (6, 3, "978-0-59-313521-1", TRUE),
-- (7, 3, "978-0-00-856091-1", TRUE),
-- (8, 4, "978-1-97-472576-2", FALSE);

-- USE cfg_books;


