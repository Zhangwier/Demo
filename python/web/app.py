#My_Web.html
import flask
app=flask.Flask(__name__)

@app.route("/")
def hello():
    return "你好"

@app.route("/hi")
def hi():
    return "Hi,你好"

@app.route('/response/')
def res():
    return '我是响应'

if __name__ == "_main_":
    app.run(host="127.0.0.1",port=4301,debug=True)