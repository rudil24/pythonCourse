from flask import Flask

app = Flask(__name__)


@app.route("/")  # python decorator to define the route ("/") for the home page
def hello_world():
    return "<p>Hello, World!</p>"


# to run: at the Macos terminal, enter these two commands, one after the other:
# export FLASK_APP=hello.py
# flask run
# then open the browser and go to the URL: http://127.0.0.1:5000/ OR http://localhost:5000
# (for Windows CMD, use set instead of export)
# alternatively put this in code:
# if __name__ == "__main__":
#     app.run(debug=True)
# and run the script directly
# now that we've learned about decorator functions we can easily add a new endpoint for this Flask function above
@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"
