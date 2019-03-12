from flask import Flask, render_template
app = Flask(__name__, template_folder='../frontend')
import random

def ourlist():
    lista = ['mango', 'eagle', 'babies', 'cars']
    return random.choice(lista)
    # for a in range(0,10):
    #     return str(a)

@app.route('/')
def home():
    return ourlist()


@app.route('/frontend')
def frontend():
    return render_template('index.html')