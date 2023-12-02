from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=None):
    #return 'Index Page'
    return render_template('index.html', name=name)

#ctrl d to exit venv?? exit command worked but it didnt seem to like

#converter types for specifying type of a variable passed to the url
#string (default)
#int positive ints
#float positibe floats
#path like string but accepts slashes
#uuid accepts uuid strings
# ex @app.route("/post/<int:post_id>")
#def show_post(post_id):
#   return f'Post {post_id}'

#use url_for() to make absolute urls everytime instead of hard coding, i think you pass the func name to it

#add methods=['GET', 'POST'] to app.route args
#can also do app.get('/place/') AND app.post('/place') to do an overloaded method type thing
#make folder at root level? called static to put style.css in

#make templates folder at root level to put html files in
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)

#<!doctype html>
#<title>Hello from Flask</title>
#{% if name %}
#  <h1>Hello {{ name }}!</h1>
#{% else %}
#  <h1>Hello, World!</h1>
#{% endif %}

@app.route("/hello")
def hello():
    return 'Hello, world'