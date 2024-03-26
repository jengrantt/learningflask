from flask import Flask

app =Flask(__name__)

@app.route("/")
def index():
    return "hello world"


@app.route("/Jenna")
def index():
    return "hello world, Jenna"

if __name__ == "__main__":
    app.run(debug=True)