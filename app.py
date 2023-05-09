from flask import Flask
from flask import render_template

app = Flask(__name__)
# Disable caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)