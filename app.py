from flask import Flask, render_template, request, session, flash
import predict
import datetime

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password",
  database="cse_major",
  auth_plugin="mysql_native_password"
)

app.secret_key = 'your secret key'

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')

@app.route('/alogin', methods = ['POST', 'GET'])
def alogin():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        if uid == 'admin' and pwd == 'admin':
            return render_template('ahome.html')
        else:
            flash("Please Enter Valid Details")
            return render_template('admin.html')
        
@app.route('/ahome')
def ahome():
    return render_template('ahome.html')

@app.route('/auser')
def auser():
    cursor = mydb.cursor()
    cursor.execute('select * from user')
    d = cursor.fetchall()
    return render_template('auser.html', result = d)

@app.route('/acovid')
def acovid():
    return render_template('acovid.html')

@app.route('/crep', methods = ['POST', 'GET'])
def crep():
    if request.method == 'POST':
        loc = request.form['loc']
        noc = request.form['noc']
        da = request.form['da']
        cond = request.form['con']
        cid = 0;
        var = (cid,loc, noc, da, cond)
        cursor = mydb.cursor()
        cursor.execute('insert into covid values(%s, %s, %s, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            return render_template('ahome.html')
        else:
            return render_template('acovid.html')

@app.route('/atravel')
def atravel():
    cursor = mydb.cursor()
    cursor.execute('select * from travel')
    d = cursor.fetchall()
    return render_template('atravel.html', result = d)

@app.route('/aquality')
def aquality():
    return render_template('aquality.html')

@app.route('/aqut', methods = ['POST', 'GET'])
def aqut():
    if request.method == 'POST':
        da = request.form['da']
        pd = predict.predict_pollution(da)
        if float(pd)>18:
            pre='Dont go out'
        elif float(pd)<10:
            pre='Safe to go'
        elif float(pd)<15:
            pre='Be carefull,Wear Mask'
        elif float(pd)<18:
            pre='Be carefull,Wear Mask,Avoid unnecessary travel'
        cursor = mydb.cursor()
        var = (da,pd)
        cursor.execute('insert into predictttt values(%s,%s)', var)
        mydb.commit()
        if cursor.rowcount == 1:  
            cursor = mydb.cursor()
            vam = (0,pre,pd)
            cursor.execute('insert into precautions values(%s,%s,%s)', vam)
            mydb.commit()
            return render_template('ahome.html')
        else:
            return render_template('aquality.html')

@app.route('/apre', methods = ['POST', 'GET'])
def apre():
    if request.method == 'POST':
        pre = request.form['con']
        da = datetime.datetime.now()
        var = (pre, da)
        cursor = mydb.cursor()
        cursor.execute('insert into pre values(0, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            flash("Precautions Uploaded Successfully...")
            return render_template('pre.html')
        else:
            flash("Precautions not Uploaded")
            return render_template('pre.html')
        
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/ureg', methods = ['POST', 'GET'])
def ureg():
    if request.method == 'POST':
        name = request.form['name']
        uid = request.form['uid']
        pwd = request.form['pwd']
        mob = request.form['mob']
        loc = request.form['loc']
        var = (name, uid, pwd, mob, loc)
        cursor = mydb.cursor()
        cursor.execute('insert into user values(%s, %s, %s, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            flash("User Registered Successfuly")
            return render_template('user.html')
        else:
            flash("Please Enter Valid Details")
            return render_template('reg.html')

@app.route('/ulogin', methods = ['POST', 'GET'])
def ulogin():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        cursor = mydb.cursor()
        cursor.execute('select * from user where email=%s and password=%s', (uid, pwd))
        d = cursor.fetchone()
        if d:
            session['uid'] = uid
            session['name'] = d[0]
            return render_template('uhome.html', result = d[0])
        else:
            flash("Please Enter Valid Details")
            return render_template('user.html')
        
@app.route('/uhome')
def uhome():
    name = session['name']
    return render_template('uhome.html', result = name)
        
@app.route('/covid')
def covid():
    cursor = mydb.cursor()
    cursor.execute('select * from covid')
    d = cursor.fetchall()
    return render_template('covid.html', result = d)

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/utravel', methods = ['POST', 'GET'])
def utravel():
    if request.method == 'POST':
        uid = session['uid']
        tp = request.form['tp']
        tm = request.form['tm']
        Age = request.form['age']
        gen = request.form['gen']
        hc = request.form['hc']
        sdd = request.form['sd']
 
        var = (uid, tp, tm, Age, gen, hc, sdd, pd)
        cursor = mydb.cursor()
        
        cursor.execute('insert into travel values(%s,%s,%s,%s,%s, %s, %s,%s)', var)
        mydb.commit()
        cursor = mydb.cursor()
        
        cursor.execute("SELECT sd,COUNT(UserId) FROM travel WHERE sd = (%s)",[sdd])
        d = cursor.fetchall()
        return render_template('utravel.html',result=d)

@app.route('/qual')
def qual():
    cursor = mydb.cursor()
    cursor.execute('select predictttt.Date,predictttt.pred,precautions.precautions from predictttt left join precautions on predictttt.pred = precautions.pred;')
    d = cursor.fetchall()
    return render_template('qual.html', result = d)

@app.route('/mes')
def mes():
    cursor = mydb.cursor()
    cursor.execute('select * from pre')
    d = cursor.fetchall()
    return render_template('mes.html', result = d)

if __name__ == '__main__':
   app.run()