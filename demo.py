from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy 
import psycopg2 

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:root@localhost/superheros'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)
class Favhero(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30))
	age = db.Column(db.Integer)
	planet = db.Column(db.String(30))
	

@app.route('/')
def index():
	result=Favhero.query.all()
	return render_template('index.html',result=result)

@app.route('/add')
def add():
	return render_template('add.html')


@app.route('/delete')
def delete():
	return render_template('delete.html')

@app.route('/process',methods =['POST'])
def process():
	id=request.form['id']
	name=request.form['name']
	age=request.form['age']
	planet=request.form['planet']
	superherodata=Favhero(id=id,name=name,age=age,planet=planet)
	db.session.add(superherodata)
	db.session.commit()

	return redirect(url_for('index'))


@app.route('/delprocess',methods =['POST','GET'])
def delprocess():
	id=request.form['id']
	obj=Favhero.query.get(id)
	#obj=Favhero.query.filter_by(id=id)
	#db.session.query(Model).delete(obj) 
	db.session.delete(obj)
	db.session.commit()

	return redirect(url_for('index'))