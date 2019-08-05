from program import app
from flask import render_template
from datetime import datetime
import requests

# time wont update if the variable is defined here
# timenow = str(datetime.today())

# decorators create url
@app.route('/')
@app.route('/index')
# code to run against decorators
# define functions similar to url
def index():
  timenow = str(datetime.today())
  return render_template('index.html', time = timenow)

@app.route('/100Days')
def p100Days():
  return render_template('100Days.html')

@app.route('/chuck')
def chuck():
  joke = get_chuck_joke()
  return render_template('chuck.html', joke=joke)

def get_chuck_joke():
  r = requests.get('https://api.chucknorris.io/jokes/random')
  data = r.json()
  return data['value']