from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/where')
def where():
    return render_template("where.html")


@app.route('/cataloge')
def cataloge():
    return render_template("cataloge.html")


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/more1')
def more1():
    return render_template("more1.html")


@app.route('/more2')
def more2():
    return render_template("more2.html")


@app.route('/more3')
def more3():
    return render_template("more3.html")


@app.route('/more4')
def more4():
    return render_template("more4.html")


@app.route('/more5')
def more5():
    return render_template("more5.html")


@app.route('/more6')
def more6():
    return render_template("more6.html")


@app.route('/more7')
def more7():
    return render_template("more7.html")


@app.route('/more8')
def more8():
    return render_template("more8.html")


@app.route('/more9')
def more9():
    return render_template("more9.html")


@app.route('/buy')
def buy():
    return render_template("buy.html")


if __name__ == "__main__":
    app.run()
