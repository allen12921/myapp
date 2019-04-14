From flask import Flask
import redis, os
import psycopg2


app = Flask(__name__)

r = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')

try:
    conn = psycopg2.connect("dbname='template1' user=os.environ['DB_USER'] host=os.environ['DB_HOST'] password=os.environ['DB_PASS']")
except:
    print "unable to connect to the database"


cur = conn.cursor()
cur.execute("SELECT name, value from mytable")
cur.execute("INSERT INTO mytable VALUES(%s,%s);",('a',123))
cur.execute("UPDATE mytable SET value =  %s WHERE name = %s;",(123,'a'))

result = cur.fetchone()[1]

@app.route('/')
def helloworld:
    return 'Hey, we are running Flask in a Docker container!'


if __name == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)
