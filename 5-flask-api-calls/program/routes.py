from program import app
from flask import render_template, request
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

@app.route('/pokemon', methods = ['GET', 'POST'])
def pokemon():
  pokemon = []
  if request.method == 'POST' and 'pokecolor' in request.form:
    color = request.form.get('pokecolor')
    pokemon = get_poke_colors(color)
  return render_template('pokemon.html', pokemon = pokemon)

def get_chuck_joke():
  r = requests.get('https://api.chucknorris.io/jokes/random')
  data = r.json()
  return data['value']

def get_poke_colors(color):
  r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + color.lower())
  pokedata = r.json()
  pokemon = []

  for i in pokedata['pokemon_species']:
    pokemon.append(i['name'])

  return pokemon