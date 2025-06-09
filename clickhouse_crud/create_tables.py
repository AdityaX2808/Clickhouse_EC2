from clickhouse_connect import get_client

# Replace with your actual credentials if different
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    database='AdityaDB'
)

# Drop tables if they already exist (for idempotency)
client.command("DROP TABLE IF EXISTS users")
client.command("DROP TABLE IF EXISTS orders")

# Create `users` table
client.command("""
CREATE TABLE users (
    id UInt32,
    name String,
    age UInt8,
    signup_date Date
)
ENGINE = MergeTree()
ORDER BY id
""")

# Create `orders` table
client.command("""
CREATE TABLE orders (
    order_id UInt32,
    user_id UInt32,
    amount Float32,
    order_date Date
)
ENGINE = MergeTree()
ORDER BY order_id
""")

print("Successfully created 'users' and 'orders' tables.")
