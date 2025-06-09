from clickhouse_connect import get_client

# Connect to ClickHouse
client = get_client(
    host='localhost',
    port=8123,
    username='default',
    password='',
    database='AdityaDB'
)

# AVG user age
query = "SELECT AVG(age) AS average_age FROM users"

try:
    result = client.query(query)
    average_age = result.result_rows[0][0]
    print(f"Average Age of Users: {average_age:.2f} years")
except Exception as e:
    print("AVG query failed:", e)
