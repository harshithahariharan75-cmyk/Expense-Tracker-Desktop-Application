# This file handles all database-related operations,
# for the Expense Tracker Application.

# Import PyQt6 SQL classes for database connection and SQL queries.
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


def init_db(db_name):
    database = QSqlDatabase.addDatabase("QSQLITE") ## Create SQLite database connection
    database.setDatabaseName(db_name)

    if not database.open():
        return False

    query = QSqlQuery()
    query.exec("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    category TEXT,
                    amount REAL,
                    description TEXT
                    )
                    """)
    return True

# Fetches all expense records from the database
# and returns them as a list.

def fetch_expenses():
    query = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")
    expenses = []   
    while query.next():
        row = [query.value(i) for i in range(5)]
        expenses.append(row)
    return expenses


# Inserts a new expense record into the database

def add_expenses(date, category, amount, description):
    query = QSqlQuery()
    query.prepare("""
                  INSERT INTO expenses (date, category, amount, description)
                  VALUES (?, ?, ?, ?)
                    """)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)

    return query.exec()

# Deletes an expense record from the database using its ID

def delete_expenses(expense_id):
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = ?")
    query.addBindValue(expense_id)

    return query.exec()

    
    
    

            
