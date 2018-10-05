from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    container = os.environ["ContainerName"]
    node = os.environ["NodeName"]
    return """
    <center>
    <img src="/static/banner.png">
    <h1>Hello, Pycon India from {0} on {1}!!</h1>
    </center>""".format(container,node)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)