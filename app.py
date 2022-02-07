from flask import Flask, flash, redirect, render_template, request, session, abort, Response, url_for
import os
import mysql.connector as mariadb
import pandas as pd
import sys
import threading
from subprocess import call

app = Flask(__name__)
app.secret_key = os.urandom(12)

def thread_second():
    call(["xterm","-e", "python3 script.py"])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/questions")
def questions():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()
    username = session.get('username')

    query2 = "SELECT * FROM questions;"
    df = pd.read_sql_query(query2, mariadb_connection)

    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('questions.html',arrayques = df)

@app.route("/dashboard")
def dashboard():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()
    username = session.get('username')

    #query2 = "SELECT id,status FROM bots;"
    #df = pd.read_sql_query(query2, mariadb_connection)

    #idbot1 = df['id'][0]
    #idbot2 = df['id'][1]
    #idbot3 = df['id'][2]

    #statbot1 = df['status'][0]
    #statbot2 = df['status'][1]
    #statbot3 = df['status'][2]

    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('dashboard.html', username=username,whatsid="idbot1",faceid="idbot2",instaid="idbot3",whatsstat="statbot1",facestat="statbot2",instastat="statbot3")

@app.route('/dologin', methods=['POST'])
def dologin():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    query = "SELECT usuario,clave FROM users WHERE usuario = %s and clave = %s;"
    adr = (request.form['usuario'], request.form['clave'])
    cursor1.execute(query, adr)
    result = cursor1.fetchall()
    usuario = result[0][0]
    password = result[0][1]




    if request.form['clave'] == password and request.form['usuario'] == usuario:
            session['logged_in'] = True
            session['username'] = usuario

            return dashboard()
    else:
        return index()

@app.route('/dow', methods=['POST'])
def dow():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    if sys.platform == "win32":

        #cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('on', request.form['id']))
        #mariadb_connection.commit()
        import subprocess
        UDP_IP = request.form['keywords']
        #user = request.form['username']
        #clave = request.form['clave']
        print(UDP_IP)
        #subprocess.Popen(["script4.py", UDP_IP])
        os.system('python script4.py {}'.format(UDP_IP))
        #os.startfile('script4.py {}'.format(UDP_IP))
        return dashboard()
    else:

        processThread = threading.Thread(target=thread_second)  # <- note extra ','
        processThread.start()


@app.route('/dof', methods=['POST'])
def dof():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()
    UDP_IP = str(request.form['hashtag'])
    user = request.form['usuario']
    clave = request.form['clave']
    if sys.platform == "win32":
        #cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('on', request.form['idfa']))
        #mariadb_connection.commit()
        os.system('python script6.py {} {} {}'.format(UDP_IP, user, clave))
        return dashboard()
    else:

        processThread = threading.Thread(target=thread_second)  # <- note extra ','
        processThread.start()

@app.route('/doi', methods=['POST'])
def doi():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    if sys.platform == "win32":
        cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('on', request.form['idi']))
        mariadb_connection.commit()
        os.startfile('script3.py')
        return dashboard()
    else:

        processThread = threading.Thread(target=thread_second)  # <- note extra ','
        processThread.start()

@app.route('/dowof', methods=['POST'])
def dowof():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('off', request.form['idof']))
    mariadb_connection.commit()

    return dashboard()



@app.route('/dofof', methods=['POST'])
def dofof():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('off', request.form['idfaof']))
    mariadb_connection.commit()

    return dashboard()


@app.route('/doiof', methods=['POST'])
def doiof():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()


    cursor1.execute("""UPDATE bots SET status = %s WHERE id = %s""", ('off', request.form['idiof']))
    mariadb_connection.commit()

    return dashboard()

@app.route('/createquest', methods=['POST'])
def createquest():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    cursor1.execute(
        "INSERT INTO questions (question,response) VALUES (%s,%s)",
        (request.form['pregunta'], request.form['respuesta']))
    mariadb_connection.commit()

    return questions()

@app.route('/editquest', methods=['POST'])
def editquest():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()

    cursor1.execute("""UPDATE questions SET question = %s, response = %s WHERE id = %s""",
                    (request.form['pregunta'], request.form['respuesta'],request.form['questid']))
    mariadb_connection.commit()

    return questions()

@app.route('/checkquest', methods=['POST'])
def checkquest():
    mariadb_connection = mariadb.connect(user='root', password='', database='autobot', host='127.0.0.1', port='3306')
    cursor1 = mariadb_connection.cursor()



    query = "SELECT * FROM questions WHERE id = %s;"
    adr = (request.form['questid'],)
    cursor1.execute(query, adr)
    result = cursor1.fetchall()
    id = result[0][0]
    question = result[0][1]
    response = result[0][2]

    return render_template('checkquest.html', id=id,question=question,response=response)


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return index()


if __name__ == '__main__':
    app.run()
