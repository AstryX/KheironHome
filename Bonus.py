#Robertas Dereskevicius 2021 Kheiron Take-home Exercise
#The logic for a basic web-based interface calculator with flask
    
import flask
from flask import request
from collections import deque
from Part1 import compute

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Basic html for a calculator input
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Basic Web Prefix Calculator</h1>
<form action="calculate" method="post">
  <label for="fname">Prefix Calculator Input:</label><br>
  <input type="text" name="input_nums"><br><br>
  <input type="submit" value="Submit">
</form>'''

@app.route('/calculate', methods=['POST'])
def calculate():
    input_data = request.form['input_nums'].split()
    return str(compute(deque(input_data)))

app.run()