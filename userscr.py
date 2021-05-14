from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index ():
    connection = connectToMySQL('users')
    result = connection.query_db('SELECT * FROM users;')
    
    return render_template('index.html', users = result )

@app.route('/new', methods=['GET'])
def user_new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def user_create():
    connection = connectToMySQL('users')
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s,NOW());"
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email': request.form['email']
    }
    new_user = connection.query_db(query, data)
    return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)