import psycopg2
from secret import username, password, db_name

src_string = 'postgresql://{}:{}@localhost:5432/{}'.format(username, password, db_name)
conn = psycopg2.connect(src_string)

sql = '''
    insert into answers(answer1, answer2, platform, browser)
values ('good','bad','chrome','iphone');
'''
cursor = conn.cursor()

cursor.execute(sql)
conn.commit()
conn.close()