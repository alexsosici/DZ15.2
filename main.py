from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ja")
def o_meni():
    return render_template("o_meni.html")


if __name__ == '__main__':
    app.run()