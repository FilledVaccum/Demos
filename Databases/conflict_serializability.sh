import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()


# Start Transaction 1
cursor.execute("BEGIN TRANSACTION")
cursor.execute("SELECT balance FROM accounts WHERE id = 1")
balance_t1 = cursor.fetchone()[0]
cursor.execute("UPDATE accounts SET balance = ? WHERE id = 1", (balance_t1 + 500,))
conn.commit()

# Start Transaction 2
cursor.execute("BEGIN TRANSACTION")
cursor.execute("SELECT balance FROM accounts WHERE id = 1")
balance_t2 = cursor.fetchone()[0]
cursor.execute("UPDATE accounts SET balance = ? WHERE id = 1", (balance_t2 - 300,))
conn.commit()

# Final balance check
cursor.execute("SELECT balance FROM accounts WHERE id = 1")
final_balance = cursor.fetchone()[0]
print(f"Final balance: {final_balance}")

conn.close()

