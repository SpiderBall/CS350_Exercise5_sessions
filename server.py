import psycopg2
import psycopg2.extras

from flask import Flask, render_template, session, request
import os
app = Flask(__name__)

app.secret_key = os.urandom(24).encode('hex')
#used to sign cookies

def connectToDB():
  connectionString = 'dbname=session user=sstuart password=Bibarel666 host=localhost'
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")

@app.route('/', methods=['GET', 'POST'])
def mainIndex():
    conn = connectToDB()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    queryType = 'None'

    if 'username' not in session:
        session['username'] = ''
    else:
        print('User: ' + session['username'])

    rows = []
    # if user typed in a post ...
    if request.method == 'POST':
      searchTerm = request.form['search']
      if searchTerm == 'movies':
        if 'zipcode' in session:
            print "zip in session movies"
            query = "SELECT * from movies where zip = %s"
            queryType = 'movies'
            cur.execute(query, (session['zipcode'],))
        else:
            print "zip not in session movies"
            query = "SELECT * from movies" 
            queryType = 'movies'
            cur.execute(query)
      else:
        if 'zipcode' in session:
            print "zip in session stores"
            query = "SELECT * FROM stores where name LIKE %s OR type LIKE %s AND zip = %s ORDER BY name;"
            queryType = 'stores'
            print (query)
            cur.execute(query, (searchTerm, searchTerm, session['zipcode']))
        else:
            print "zip not in session stores"
            query = "SELECT * FROM stores where name LIKE %s OR type LIKE %s ORDER BY name;"
            cur.execute(query, (searchTerm, searchTerm))
      rows = cur.fetchall()


    return render_template('index.html', queryType=queryType, results=rows, selectedMenu='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = connectToDB()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    not_registered = False
    # if user typed in a post ...
    if request.method == 'POST':
      username = request.form['username']
      pw = request.form['pw']
      query = "select * from users WHERE username = %s AND password = crypt(%s, password)"
      print query
      cur.execute(query, (username, pw))
      currentUser = cur.fetchone()
      if not currentUser:
          print "This account is not recognized. Please register."
          not_registered = True
      else:
        print "this account is recognized"
        session['username'] = username
        session['zipcode'] = currentUser['zipcode']
        print session['zipcode']

    return render_template('login.html', selectedMenu='Login', not_registered = not_registered)


@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = connectToDB()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    username_in_use = False
    incomplete_form = False
    if request.method == 'POST':
      username = request.form['username']
      pw = request.form['pw']
      zipcode = request.form['zipcode']
      select_query = "SELECT * FROM users where username = %s;"
      cur.execute(select_query, (username,))
      existing_users = cur.fetchall()
      print existing_users
      
      if username and pw and zipcode:
        if not existing_users:
            session['username'] = username
            insert_query = "INSERT INTO users (id, username, password, zipcode) VALUES (DEFAULT, %s,crypt(%s, gen_salt('bf')), %s);"
            cur.execute(insert_query, (session['username'], pw, zipcode))
            conn.commit()
        else:
            print("This username is already in use")
            username_in_use = True
      else:
          print ("Elements of the form are missing, please try again.")
          incomplete_form = True
    return render_template('register.html', selectedMenu='Register', username_in_use = username_in_use, incomplete_form = incomplete_form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return render_template('index.html', selectedMenu='Home')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
