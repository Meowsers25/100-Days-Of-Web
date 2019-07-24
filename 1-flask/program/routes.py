from program import app
from flask import render_template

# decorators create url
@app.route('/')
@app.route('/index')
# code to run against decorators
# define functions similar to url
def index():
  return render_template('index.html')

@app.route('/100Days')
def p100Days():
  return render_template('100Days.html')