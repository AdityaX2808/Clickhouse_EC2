import clickhouse_connect

client = clickhouse_connect.get_client(host='localhost', port=8123)

client.command("CREATE DATABASE IF NOT EXISTS AdityaDB")

client.command("""
    CREATE TABLE IF NOT EXISTS AdityaDB.employees (
        id UInt32,
        name String,
        salary Float32
    ) ENGINE = MergeTree()
    ORDER BY id
""")

client.command("""
    INSERT INTO AdityaDB.employees (id, name, salary) VALUES
    (1, 'Alice', 60000.0),
    (2, 'Bob', 55000.5),
    (3, 'Charlie', 72000.25)
""")


rows = client.query('SELECT * FROM AdityaDB.employees').result_rows
for row in rows:
    print(row)
