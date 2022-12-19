from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # root / home
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return 'success'

@app.route('/hello/<string:name>/<int:num>')
def hello(name,num):
    return render_template('hello.html',name=name,num=num)

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f' hi {name}'

@app.route('/repeat/<string:name>/<int:num>')
def say_multiple(name,num):
    return f'hi {name * num}'

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Michael Choi', 'age' : 35},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsupin', 'age' : 47},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen', 'age' : 27},
        {'first_name' : 'Jordan', 'last_name' : 'Ronk', 'full_name' : 'Jordan Ronk', 'age' : 28},

    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


if __name__=="__main__":   
    app.run(debug=True)

