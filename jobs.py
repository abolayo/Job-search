from flask import Flask, render_template

app = Flask(__name__)


def bold(function):
    def wrapper():
        return f"<b>" + function() + "</b>"

    return wrapper


def italics(function):
    def wrapper():
        return f"<i>" + function() + "</i>"

    return wrapper


@app.route("/")
def hello_world():
    return render_template('main.html')


@bold
@italics
@app.route('/bye')
def bye():
    return render_template('form.html')


if __name__ == '__name__':
    app.run(debug=True)
