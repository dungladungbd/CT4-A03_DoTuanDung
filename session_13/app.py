from flask import Flask, redirect, render_template, request
import psycopg2
from secret import username, password, db_name
'''
Status code hay gap
200 OK
404 Not found
403 Ko du quyen
405 Method not allowed
500 Internal server error
502 Bad gateway
'''

app = Flask(__name__)


@app.route('/')
def index():
    return 'hehehe'


@app.route('/sample')
def sample():
    return 'hahahaha'


@app.route('/redirect')
def test_redirect():
    return redirect('https://www.facebook.com/')


@app.route('/website', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        form = request.form
        print(form)
        answer1 = form['question1']
        answer2 = form['question2']
        print(answer1, answer2)

        user_agent = request.user_agent
        print(user_agent.platform)
        print(user_agent.version)
        print(user_agent.browser)
        print(user_agent.language)

        src_string = 'postgresql://{}:{}@localhost:5432/{}'.format(
            username, password, db_name)
        conn = psycopg2.connect(src_string)

        sql = '''
            insert into answers(answer1, answer2, platform, browser) values('{}','{}','{}','{}')
            '''.format(answer1, answer2, user_agent.platform, user_agent.browser)
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()
        conn.close()

        return 'hello'
    elif request.method == 'GET':
        src_string = 'postgresql://{}:{}@localhost:5432/{}'.format(
            username, password, db_name)
        conn = psycopg2.connect(src_string)

        sql = '''
           Create table if not exists  answers
            (
                id serial primary key,
                answer1 varchar,
                answer2 varchar,
                platform varchar,
                browser varchar
            )
            '''
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()
        conn.close()

        return render_template('test.html')


if __name__ == '__main__':
    app.run()
