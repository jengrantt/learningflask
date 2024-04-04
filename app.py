from flask import Flask

app =Flask(__name__)

@app.route("/")
def index():
    return "hello world"


@app.route("/jenna")
def jenna():
    return "hello world, jenna"

if __name__ == "__main__":
    app.run(debug=True, port=8000)