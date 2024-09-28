-- USE cfg_books;

-- This procedure allows a user to input their customer id and a date to show what books have not shipped since the date they have typed in.


-- DELIMITER //

-- CREATE PROCEDURE unshipped_items (IN user_id INT, IN ordered_since date )
-- BEGIN
-- IF ordered_since IS NULL THEN
-- 	SET ordered_since = "1900-01-01";
-- END IF;

-- SELECT b.title, os.order_date, oi.shipped
-- FROM order_item AS oi
-- JOIN order_summary AS os ON oi.order_id = os.order_id
-- JOIN book AS b ON b.isbn = oi.isbn
-- WHERE oi.shipped = FALSE AND os.customer_id = user_id AND os.order_date >= ordered_since;

-- END //

-- DELIMITER ; 

