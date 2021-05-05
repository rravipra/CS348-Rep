from flask import abort, Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import yaml
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

bcrypt = Bcrypt(app)

db = yaml.load(open('database.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['pass']
app.config['MYSQL_DB'] = db['db']

my_conn = create_engine("mysql+mysqldb://flask:flask@localhost/resort_management")

mysql = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask:flask@localhost/resort_management'
# CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST', 'GET'])
def data():

    # POST a data to database
    if request.method == 'POST':
        #body = request.json

        firstname = request.form.get("first_name")
        lastname = request.form.get("last_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        time = request.form.get("check_in_time")
        room_no = request.form.get("room_no")
        total_cost = request.form.get("total_cost")


        # session = mysql.session()
        id = my_conn.execute(f'INSERT INTO guest(firstname, room_no) VALUES ("{str(firstname)}", {str(room_no)})')
                                #(str(firstname), str(lastname), int(age), str(gender), int(room_no), int(total_cost))).cursor
                                #, str(lastname), int(age), str(gender), time, int(room_no), int(total_cost))

        #cursor.execute('INSERT INTO users VALUES(null, %s, %s)',(str(name), str(age)))

        # session.connection().commit()
        # cursor.close()

        status = {
            'status': 'Data is posted to MySQL!',
            'name': firstname,
            'id': id.lastrowid
        }
        return render_template("successfully.html", status = status)
    
    # GET all data from database
    if request.method == 'GET':
        session = mysql.session()
        cursor = session.execute('SELECT * FROM guest').cursor
        #cursor = mysql.connection.cursor()
        #cursor.execute('SELECT guest_id, firstname, lastname  FROM guest')

        users = cursor.fetchall()

        allData = []

        for i in range(len(users)):
            id = users[i][0]
            name = users[i][1]
            lastname = users[i][2]
            age = users[i][3]
            gender = users[i][4]
            room_no = users[i][5]
            check_in_time = users[i][6]
            total_cost = users[i][7]
            dataDict = {
                "id": id,
                "name": name,
                "lastname": lastname,
                "age": age,
                "gender": gender,
                "room_no": room_no,
                "check_in_time": check_in_time,
                "total_cost": total_cost
            }
            allData.append(dataDict)

        return render_template('table.html', users = allData)

        #return render_template(table.html, users = users)

@app.route('/insert')
def insert():
    
    return render_template('insert.html')

# @app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
# def onedata(id):

#     # GET a specific data by id
#     if request.method == 'GET':
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT * FROM users WHERE id = %s', (id))
#         users = cursor.fetchall()
#         print(users)
#         data = []
#         for i in range(len(users)):
#             id = users[i][0]
#             name = users[i][1]
#             age = users[i][2]
#             dataDict = {
#                 "id": id,
#                 "name": name,
#                 "age": age
#             }
#             data.append(dataDict)
#         return jsonify(data)

#     # DELETE a data
#     if request.method == 'DELETE':
#         cursor = mysql.connection.cursor()
#         cursor.execute('DELETE FROM users WHERE id = %s', (id))
#         mysql.connection.commit()
#         cursor.close()
#         return jsonify({'status': 'Data '+id+' is deleted on MySQL!'})

#     # UPDATE a data by id
#     if request.method == 'PUT':
#         body = request.json
#         name = body['name']
#         age = body['age']

#         cursor = mysql.connection.cursor()
#         cursor.execute('UPDATE users SET name = %s, age = %s WHERE id = %s', (name, age, id))
#         mysql.connection.commit()
#         cursor.close()
#         return jsonify({'status': 'Data '+id+' is updated on MySQL!'})


if __name__ == '__main__':
    app.run(debug=True)
