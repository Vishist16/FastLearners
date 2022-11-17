from flask import Blueprint, render_template, request, jsonify,flash, session, redirect, url_for
from flask_mysqldb import MySQL,MySQLdb

from . import mysql
views = Blueprint('views', __name__)

@views.route('/')
def home():
    if 'loggedin' in session:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT distinct class from student order by class ASC")
        classlst = cur.fetchall()  
        return render_template('home.html', classlst = classlst)
    return redirect(url_for('auth.login'))
    
@views.route("/fetchrecords",methods=["POST","GET"])
def fetchrecords():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #print(query)
        if query == '':
            cur.execute("SELECT * FROM student")
            datalst = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            print(search_text)
            if search_text=='21BCS-713':
                cur.execute("select * from student where class='21BCS-713'")
                datalst = cur.fetchall()
            if search_text=='21BCS-714':
                cur.execute("select * from student where class='21BCS-714'")
                datalst = cur.fetchall()
            if search_text=='21BCS-715':
                cur.execute("select * from student where class='21BCS-715'")
                datalst = cur.fetchall() 
    return jsonify({'htmlresponse': render_template('newresstu.html', datalst=datalst)})

@views.route("/studata",methods=["POST","GET"])
def studata():
    if 'loggedin' in session:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select distinct class from student order by class ASC")
        student = cur.fetchall() 
        #print(student) 
        return render_template('stu.html', student = student)
    return redirect(url_for('auth.login'))
@views.route("/sturecords",methods=["POST","GET"])
def sturecords():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #category_id = request.form['category_id']
        print(query)
        #print(category_id)
        if query == '':
            cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid")
            stulist = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            print(search_text)
            if search_text=='21BCS-713':
                cur.execute("select student.class, max(marks.total) from marks inner join student on marks.uid=student.uid group by student.class")
                tem = cur.fetchall()
                #print(tem)
                #print(tem[2]["max(marks.total)"])
                mmar=tem[2]["max(marks.total)"]
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where total=%s",[mmar])
                stulist = cur.fetchall()
            if search_text=='21BCS-714':
                cur.execute("select student.class, max(marks.total) from marks inner join student on marks.uid=student.uid group by student.class")
                tem = cur.fetchall()
                #print(tem)
                #print(tem[1]["max(marks.total)"])
                mmar=tem[1]["max(marks.total)"]
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where total=%s",[mmar])
                stulist = cur.fetchall()
            if search_text=='21BCS-715':
                cur.execute("select student.class, max(marks.total) from marks inner join student on marks.uid=student.uid group by student.class")
                tem = cur.fetchall()
                #print(tem)
                #print(tem[0]["max(marks.total)"])
                mmar=tem[0]["max(marks.total)"]
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where total=%s",[mmar])
                stulist = cur.fetchall()  
    return jsonify({'htmlresponse': render_template('newres.html', stulist=stulist)})

@views.route("/subtop",methods=["POST","GET"])
def subtop():
    if 'loggedin' in session: 
        mcur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mcur.execute("select distinct sub from subjects order by sub ASC")
        subject = mcur.fetchall() 
        #print(student) 
        return render_template('subd.html', subject=subject)
    return redirect(url_for('auth.login'))
@views.route("/subtoprecords",methods=["POST","GET"])
def subtoprecords():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        query = request.form['query']
        #category_id = request.form['category_id']
        print(query)
        #print(category_id)
        if query == '':
            cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid")
            stulist = cur.fetchall()
            print('all list')
        else:
            search_text = request.form['query']
            a=search_text
            print(a)
            print(type(a))
            if search_text=='DBMS':
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where dbms in (select max(dbms) from marks)")
                stulist = cur.fetchall()
            elif search_text=='JAVA':
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where java in (select max(java) from marks)")
                stulist = cur.fetchall()
            elif search_text=='DSA':
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where dsa in (select max(dsa) from marks)")
                stulist = cur.fetchall()
            else:
                search_text=='Aptitude'
                cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where aptitude in (select max(aptitude) from marks)")
                stulist = cur.fetchall()
            #cur.execute("select student.uid, student.name, student.class, marks.dbms, marks.java, marks.dsa, marks.aptitude, marks.total from marks inner join student on marks.uid=student.uid where class in (%s)", [search_text])
            #stulist = cur.fetchall()  
    return jsonify({'htmlresponse': render_template('newres2.html', stulist=stulist)})


