from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import joblib
from flask import request
import mysql.connector
from datetime import date
from flask import jsonify
from flask_cors import CORS



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Avinash1906",
  database="sample"

)
mycursor = mydb.cursor()

# load the model from disk
filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)
CORS(app)
cors = CORS(app,resources = {
 	r"/*" :{
 		"origins":"*"
 	}
})

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		username = request.form['username']
		print(username)
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
		if my_prediction:
			result = "Non-Abusive"
		else:
			result = "Abusive"
		today = date.today()
		print(today)
		sql = "INSERT INTO login_history (username,time,search,result) VALUES (%s, %s,%s, %s)"
		val = (username,today,message,result)
		mycursor.execute(sql, val)
		mydb.commit()
	return render_template('result.html',prediction = my_prediction,username=username)


@app.route('/post_login')
def post_login():
	data = request.args
	mycursor.execute("SELECT * from login where username = '"+data['username']+"' and password = '"+data['password']+"'")
	myresult = mycursor.fetchall()
	if not len(myresult) == 0:
		return render_template('home.html',username = str(data['username']))
	else:
		return render_template('login.html')



@app.route('/register_login', methods = ['POST'])
def register_login():
	username  = request.form['username']
	password = request.form['password']
	email = request.form['email']
	mycursor.execute("SELECT * from login where username = '"+username+"' and password = '"+password+"'")
	myresult = mycursor.fetchall()
	if len(myresult) > 0:
		return render_template('loginerror.html')
	else:
		sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
		val = (username,password)
		mycursor.execute(sql, val)
		mydb.commit()
		return render_template('loginsuccess.html')



@app.route('/getResultsList',methods = ['POST'])
def getResultsList():
	print("in here")
	username = request.data.decode("utf-8") 
	print(username)
	mycursor.execute("SELECT * from login_history where username = '"+username+"' ")
	myresult = mycursor.fetchall()
	print(myresult)
	return jsonify(myresult)



@app.route('/renderResultsPage/<string:username>',methods = ['GET','POST'])
def renderResultsPage(username):
	return render_template('resultsList.html',username = username)


@app.route('/renderHomePage/<string:username>',methods = ['GET','POST'])
def renderHomePage(username):
	return render_template('home.html',username = username)



if __name__ == '__main__':
	app.run(host = '0.0.0.0',debug=True,port=8081)


