# std python imports
import json
import MySQLdb

# import the Flask class from the flask package
from flask import Flask, render_template
from flask import g   #g is a thread local and is per-request
from flask import Response
from flask import request


# create the application object
app = Flask(__name__)
app.config.from_object('config')

@app.before_request
def db_connect():
  g.conn = MySQLdb.connect(host=app.config['db_hostname'], user=app.config['db_username'], passwd=app.config['db_password'], db='db_name')
  g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.conn.close()
  return response

def query_db(query, args=(), one=False):
  g.cursor.execute(query, args)
  rv = [ dict( (g.cursor.description[idx][0], value) for idx, value in enumerate(row) ) for row in g.cursor.fetchall() ]
  return (rv[0] if rv else None) if one else rv

@app.route("/add", methods=['POST'])
def add():
  req_json = request.get_json()
  g.cursor.execute("INSERT INTO test.name (firstname, lastname) VALUES (%s,%s)", (req_json['firstname'], req_json['lastname']))
  g.conn.commit()
  resp = Response("Updated", status=201, mimetype='application/json')
  return resp

@app.route("/contractors", methods=['GET'])
def contractors():
  #result = query_db("SELECT firstname,lastname,address1,address2,city,zip,state,phone,email, date_format(startdate, '%m/%d/%Y') as startdate FROM hh.contractors")
  #print d.strftime("%d/%m/%Y %H:%M:%S")
  result = query_db("SELECT firstname,lastname,address1,address2,city,zip,state,phone,email FROM hh.contractors")
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp

# use decorators to link the function to a url
@app.route("/")
def main():
    return render_template('index.html')

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
