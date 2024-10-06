-- USE cfg_books;

-- SELECT b.title, a.first_name, a.last_name, g.genre
-- FROM book AS b
-- JOIN author AS a ON a.author_id = b.author_id
-- JOIN genre AS g ON g.genre_id = b.genre_id
-- ORDER BY last_name, first_name;

-- SELECT CONCAT(c.first_name," ", c.last_name) AS customer, os.order_id, b.title, CONCAT(a.first_name, " ", a.last_name) AS author, b.price, oi.shipped
-- FROM order_item AS oi
-- JOIN order_summary AS os ON oi.order_id = os.order_id
-- JOIN customer AS c ON c.customer_id = os.customer_id
-- JOIN book AS b ON b.isbn = oi.isbn
-- JOIN author AS a ON a.author_id = b.author_id
-- ORDER BY customer, shipped, title;