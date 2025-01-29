from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response

@app.route('/stats')
def get_stats():
    mealPref = {}
    programPref = {}
    
    for student in data:
        mPref = student.get('pref')
        pPref = student.get('programme')
        if mPref in mealPref:
            mealPref[mPref] += 1
        else:
            mealPref[mPref] = 1

        if pPref in programPref:
            programPref[pPref] += 1
        else:
            programPref[pPref] = 1
    
    return jsonify(mealPref, programPref)

@app.route('/add/<a>/<b>')
def add_a_b(a,b):
    a = float(a)
    b = float(b)
    total = 0

    total = a + b
    return jsonify(total)

@app.route('/subtract/<a>/<b>')
def sub_a_b(a,b):
    a = float(a)
    b = float(b)
    total = 0

    total = a - b
    return jsonify(total)

@app.route('/multiply/<a>/<b>')
def mul_a_b(a,b):
    a = float(a)
    b = float(b)
    total = 0

    total = a * b
    return jsonify(total)

@app.route('/divide/<a>/<b>')
def div_a_b(a,b):
    a = float(a)
    b = float(b)
    total = 0

    total = a / b
    return jsonify(total)

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref') 
    if pref:
        for student in data: 
            if student['pref'] == pref: 
                result.append(student) 
        return jsonify(result) 
    return jsonify(data) 

@app.route('/students/<id>')
def get_students_id(id):
    for student in data:
        if (student ['id'] == id):
            return jsonify (student)
    return f"Student {id} does not exist in the database"

#return jsonify(data)# return student data in response

app.run(host='0.0.0.0', port=8080, debug=True)
