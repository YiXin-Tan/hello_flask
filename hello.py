from flask import Flask
app = Flask(__name__)

def make_bold(funct):
    def wrapper_function():
        return f'<b>{funct()}</b>'
    return wrapper_function

def make_emphasis(funct):
    def wrapper_function():
        return f'<em>{funct()}</em>'
    return wrapper_function

def make_underline(funct):
    def wrapper_function():
        return f'<u>{funct()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<img src="https://i.giphy.com/media/eZsKqkZUEM5vG/giphy.webp" alt="cat pic">'

@app.route('/hi')
@make_bold
@make_emphasis
@make_underline
def say_hi():
    return 'Hi'

@app.route('/username/<string:username>/<int:age>')
def hi_user(username, age):
    return f'Hello there {username}, you are {age} years old!'

if __name__ == '__main__':
    app.run(debug=True)
