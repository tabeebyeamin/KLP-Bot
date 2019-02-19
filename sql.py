import sqlite3



def add_to_table(product_name, product_price, location, link, date, table_name):
    '''(str, str, float, str, str) -> NoneType
    This allows you to choose a table to store and save your retrieved info
    to. The table will have a name, price, link and date column.
    '''
    # set up connection and cursor
    conn = sqlite3.connect(table_name + '.db')
    cursor = conn.cursor()
    
    # create the table if it doesn't exist
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS products(product TEXT, price REAL, location TEXT, link TEXT, date TEXT)')
    # add the product to the table
    cursor.execute(
        'INSERT INTO products (product, price, location, link, date) VALUES (?, ?, ?, ?, ?)', (product_name, product_price, location, link, date))
    
    print('Done adding to db!')
    # save and close
    conn.commit()
    cursor.close()
    conn.close()