import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,contact text,password text,salary text)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS manufacture(manufacture_id INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,description text)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS distributor(distributor_id INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,location text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS directory(directory_id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(product_id INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text,name text,price text ,quantity text,status text)")
    con.commit()
create_db()

