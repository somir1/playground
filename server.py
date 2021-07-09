from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return "go to http://localhost:5000/play"

@app.route("/play")
def box_spawn():
    return render_template('index.html', copy = 3, color = "blueviolet")

@app.route("/play/<num>")
def box_muliple(num):
    copy = int(num)
    return render_template('index.html', copy = copy, colors = "blueviolet")

@app.route("/play/<num>/<color>")
def box_color(num, color):
    copy = int(num)
    colors = str(color)
    return render_template('index.html', copy = copy, colors = colors)


if __name__ == "__main__":
    app.run(debug=True)
