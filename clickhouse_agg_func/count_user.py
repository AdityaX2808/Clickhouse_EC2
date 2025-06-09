from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    password='',
    database='AdityaDB'
)

# COUNT total users
query = "SELECT COUNT(*) AS total_users FROM users"

try:
    result = client.query(query)
    total_users = result.result_rows[0][0]
    print(f"Total Users: {total_users}")
except Exception as e:
    print("COUNT query failed:", e)

