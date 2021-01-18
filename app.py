from flask import Flask, render_template, request
from pokeapi import PokeAPI
from random import randrange

app = Flask(__name__)
api = PokeAPI()

@app.route('/')
def index():
    # here we want to get the value of user (i.e. ?user=some-value)
    name = request.args.get('pokemon')
    pokemon = api.getPokemon(name)
    return render_template('index.html', pokemon=pokemon)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
