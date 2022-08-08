from flask import Flask,request, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SECRET_KEY"] = "LET_ME_TRY"

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False


db=SQLAlchemy(app)

class students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    grade=db.Column(db.Integer)

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
@app.route('/')
def index():
    all_student=students.query.all()
    return render_template("index.html",students=all_student)
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        name=request.form['name']
        grade=request.form['grade']
        my_data=students(name,grade)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/pass')
def passes():
    all_student=students.query.all()
    return render_template("pass.html",students=all_student)
@app.route('/delete/<id>/',methods = ["GET","POST"])
def delete(id):
    my_data=students.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
