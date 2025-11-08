from flask import Flask, render_template
import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def dashboard():
    return render_template("index.html", time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 
