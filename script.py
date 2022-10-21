from flask import Flask,render_template,request,redirect
from flask import *
import os

###

from datetime import date
from test import ChatBot





#database connectivity
"""mydb = mysql.connector.connect(
  host="localhost",
  port='3306',
  user="root",
  password="",
  database="chatbot"
)"""

DIR = os.getcwd()
print(DIR)

DIR.replace('\\','\\\\')

#app = Flask(__name__,template_folder=DIR+'\\templates')
app = Flask(DIR,template_folder=DIR+'\\templates')

app.config['UPLOAD_FOLDER']=DIR+"\\input"

app.secret_key="abc"


@app.route('/')
def home():
	return render_template('success.html')
	#return "hello world!"
	
@app.route('/chatbot', methods = ['GET', 'POST'])
def chatbot():
	if request.method == 'POST':
		bot=ChatBot()
		bot.start_chat()
		print("Chatbot Activated")
		return render_template('success1.html')
	return render_template('success1.html')
	

	
	
if __name__ == '__main__':
	app.run(debug = True)