from flask import render_template, request,flash, redirect, url_for
from student import app, db
from student.models import Student


#@app.route('/')
#@app.route('/index')
#def index():
#    user = {'nickname': 'Miguel'}
#    posts = [
#        {
#            'author': {'nickname': 'John'},
#            'body': 'Beautiful day in Portland!'
#        },
#        {
#            'author': {'nickname': 'Susan'},
#            'body': 'The Avengers movie was so cool!'
#        }
#    ]
#    return render_template("index.html", title='Home', user=user, posts=posts)


#@app.route('/add-student', methods=['GET','POST'])
#def add_student():
#    return render_template("add-student.html")


@app.route('/')
def index():
    student_list = Student.query.all()
    return render_template("student-list.html",**locals())


@app.route('/add-student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        st = Student(request.form['name'], request.form['age'], request.form['address'], request.form['phone_number'])
        db.session.add(st)
        db.session.commit()
        flash("Student added Successfully")
        return redirect("/", code=302)
    return render_template("add-student.html")


@app.route('/edit-student/<int:student_id>', methods=['POST', 'GET'])
def edit_student(student_id):
    student_obj = Student.query.get(int(student_id))
    if request.method == 'POST':
        student_obj.name = request.form['name']
        student_obj.age = request.form['age']
        student_obj.address = request.form['address']
        student_obj.phone_number = request.form['phone_number']
        db.session.commit()
        flash("Student updated Successfully")
        return redirect("/", code=302)
    return render_template("edit-student.html", student_id=student_id, student_obj=student_obj)










