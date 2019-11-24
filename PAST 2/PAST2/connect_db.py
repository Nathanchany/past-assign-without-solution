import pyodbc

def connect_db():
    ODBC_STR = "REPLACE WITH YOUR CONNECTION STRING"
    return pyodbc.connect(ODBC_STR)


if __name__ == '__main__':
    print (connect_db())
