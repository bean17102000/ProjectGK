import sqlite3
def get_all(query):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(query).fetchall()
    conn.close()

    return data

def get_news_by_id():
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    SELECT N.subject, N.,description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C ON N.category_id=C.id 
    WHERE id=?
    '''
    conn.close()

if __name__ == "__main__":
   print(get_all("SELECT * from category"))