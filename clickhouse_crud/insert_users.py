from clickhouse_connect import get_client

# Connection to ClickHouse
client = get_client(
host = 'localhost' ,
port = 8123 ,
username = 'default' ,
database = 'AdityaDB'
)

# Insert Data
client.command("""
INSERT INTO users (id, name, age, signup_date) VALUES
(1, 'Alice', 28, '2024-05-01'),
(2, 'Bob', 34, '2024-05-02'),
(3, 'Charlie', 25, '2024-05-03'),
(4, 'David', 40, '2024-05-04'),
(5, 'Eva', 29, '2024-05-05'),
(6, 'Frank', 32, '2024-05-06'),
(7, 'Grace', 27, '2024-05-07'),
(8, 'Helen', 35, '2024-05-08'),
(9, 'Ian', 30, '2024-05-09'),
(10, 'Jane', 26, '2024-05-10')
""")

print("Inserted rows into 'users' table.")
