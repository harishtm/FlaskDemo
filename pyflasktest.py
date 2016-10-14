from flask import Flask, render_template
import datetime



app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('templates/index.html')


@app.route('/<name>')
def get_display_name(name):
    msg = "Sorry no time ..."
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        msg = "Good Morning"
    elif 12 <= currentTime.hour < 18:
        msg = "Good afternoon"
    else:
        msg = "Good Evening"
    msg = "Hello {}!!!".format(name) + msg
    return msg


if __name__ == '__main__':
    app.run(debug=True)
