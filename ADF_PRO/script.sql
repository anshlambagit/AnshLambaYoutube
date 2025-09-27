CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATETIME,
    last_updated DATETIME DEFAULT GETDATE()
);


-- INITIAL
INSERT INTO Orders (order_id, customer_name, product_name, quantity, price, order_date, last_updated)
VALUES
(1, 'John Doe', 'Laptop', 1, 1200.00, '2025-09-20', '2025-09-20 10:15:00'),
(2, 'Alice Smith', 'Phone', 2, 800.00, '2025-09-21', '2025-09-21 14:30:00'),
(3, 'Bob Johnson', 'Headphones', 3, 150.00, '2025-09-22', '2025-09-22 09:45:00'),
(4, 'Charlie Brown', 'Monitor', 1, 300.00, '2025-09-22', '2025-09-22 18:10:00'),
(5, 'Diana Prince', 'Keyboard', 2, 100.00, '2025-09-23', '2025-09-23 11:20:00'),
(6, 'Ethan Hunt', 'Mouse', 5, 50.00, '2025-09-23', '2025-09-23 16:40:00'),
(7, 'Fiona Adams', 'Printer', 1, 200.00, '2025-09-24', '2025-09-24 09:05:00'),
(8, 'George Wilson', 'Tablet', 2, 450.00, '2025-09-24', '2025-09-24 13:25:00'),
(9, 'Hannah Lee', 'Smartwatch', 1, 220.00, '2025-09-25', '2025-09-25 08:50:00'),
(10, 'Ian Carter', 'Camera', 1, 900.00, '2025-09-25', '2025-09-25 15:15:00');


-- INCREMENTAL
INSERT INTO Orders (order_id, customer_name, product_name, quantity, price, order_date, last_updated)
VALUES
(11, 'Jack Miller', 'Drone', 1, 1500.00, '2025-09-26', '2025-09-26 10:00:00'),
(12, 'Kelly Green', 'Speakers', 2, 180.00, '2025-09-26', '2025-09-26 14:45:00'),
(13, 'Liam Scott', 'Charger', 3, 25.00, '2025-09-27', '2025-09-27 09:30:00'),
(14, 'Mia Turner', 'Desk Lamp', 1, 60.00, '2025-09-27', '2025-09-27 12:20:00'),
(15, 'Noah Brooks', 'Gaming Chair', 1, 350.00, '2025-09-27', '2025-09-27 18:10:00');
