from clickhouse_connect import get_client

client = get_client(host = 'localhost' , port = 8123 , database = 'AdityaDB' , username = 'default')

# Insert Data
client.command("""
INSERT INTO orders (order_id, user_id, amount, order_date) VALUES
(101, 1, 250.75, '2024-05-10'),
(102, 2, 480.00, '2024-05-11'),
(103, 3, 99.99,  '2024-05-11'),
(104, 1, 150.50, '2024-05-12'),
(105, 5, 300.00, '2024-05-13'),
(106, 4, 520.10, '2024-05-13'),
(107, 6, 175.75, '2024-05-14'),
(108, 7, 89.95,  '2024-05-14'),
(109, 2, 225.00, '2024-05-15'),
(110, 10, 400.00,'2024-05-15')
""")

print("Inserted rows into 'orders' table.")
