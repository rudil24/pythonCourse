# rudil24
# Day 56 - Quick website using templates
# use the html5up.net template "Identity" (which is long gone, so i'm using one called Fractal instead)
# to make a business-card-like webpage
# magic command in dev tools console to make the html page you are viewing editable (WYSIWYG):
#   document.body.contentEditable=true
# then just make sure you save webpage as <filename>.html before you leave your edits!
# also, instead of editing all the paths in the image and css files, you can do it programmatically via
# redirect package and new app routes, as follows:
#
# import redirect
# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/favicon.ico")
# def favicon():
#     return redirect("/static/favicon.ico")


# @app.route("/images/<img>")
# def images(img):
#     return redirect(f"/static/images/{img}")


# @app.route("/css/<file>")
# def css(file):
#     return redirect(f"/static/css/{file}")

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return redirect("/static/favicon.ico")


@app.route("/images/<img>")
def images(img):
    return redirect(f"/static/images/{img}")


@app.route("/css/<file>")
def css(file):
    return redirect(f"/static/css/{file}")


@app.route("/assets/<file>")
def assets(file):
    return redirect(f"/static/assets/{file}")


if __name__ == "__main__":
    app.run(debug=True)

#
