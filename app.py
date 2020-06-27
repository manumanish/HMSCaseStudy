from flask import Flask , render_template,request,session,redirect,url_for
import datetime
from flask_mysqldb import MySQL 
app = Flask(__name__, template_folder='template')
app.secret_key="casestudy"



@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


app.run()