-- USE cfg_books;

-- SELECT * FROM order_item
-- WHERE shipped = FALSE
-- ORDER BY order_item_id;

-- SELECT * 
-- FROM book
-- WHERE genre_id = 3;
-- ;

-- SELECT title
-- FROM book
-- WHERE genre_id = 6
-- ORDER BY title
-- ;

-- SELECT *
-- FROM order_summary
-- WHERE order_date <= "2024-09-20"
-- ORDER BY order_date DESC;

-- SELECT * 
-- FROM order_item
-- WHERE order_id = 3;

-- SELECT title, book_description
-- FROM book
-- WHERE book_description LIKE "%dragon%" 
-- OR book_description LIKE "%vampire%"
-- OR book_description LIKE "%werewolves%"
-- OR book_description LIKE "%mage%"
-- ORDER BY title;