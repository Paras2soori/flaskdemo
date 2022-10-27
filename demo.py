import psycopg2

connection  = psycopg2.connect('user=postgres dbname=example')
cur  = connection.cursor()

cur.execute('DROP TABLE IF EXISTS table2')
cur.execute('''
            CREATE TABLE table2(
              id INTEGER PRIMARY KEY,
              completed BOOLEAN NOT NULL DEFAULT FALSE
            );''')

sql = 'INSERT INTO table2(id , completed) values (%(id)s,%(completed)s);'
data = {'id':5,'completed':True}

cur.execute(sql,data)

cur.execute('SELECT * FROM table2')
print(cur.fetchall())


connection.commit()
connection.close()
cur.close()