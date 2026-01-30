from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models import db, Movie
from forms import FindMovieForm, RateMovieForm
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_KEY", "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI", "sqlite:///movies.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)
db.init_app(app)

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

with app.app_context():
    db.create_all()
    # Seed database if empty (placeholder for seed logic)
    if not db.session.execute(db.select(Movie)).first():
        pass


@app.route("/")
def home():
    # Get all movies sorted by rating (descending)
    all_movies = (
        db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
        .scalars()
        .all()
    )

    # Update ranking: 1 is best (highest rating)
    for i, movie in enumerate(all_movies):
        movie.ranking = i + 1
    db.session.commit()

    # Display sorted by ranking descending (n to 1) as per requirements
    display_movies = (
        db.session.execute(db.select(Movie).order_by(Movie.ranking.desc()))
        .scalars()
        .all()
    )
    return render_template("index.html", movies=display_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            TMDB_SEARCH_URL, params={"api_key": TMDB_API_KEY, "query": movie_title}
        )
        data = response.json().get("results", [])
        if not data:
            form.title.errors.append("No matches found.")
            return render_template("add.html", form=form)
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{TMDB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": TMDB_API_KEY})
        data = response.json()

        new_movie = Movie(
            title=data["title"],
            year=(
                data["release_date"].split("-")[0]
                if data.get("release_date")
                else "Unknown"
            ),
            image_url=f"{TMDB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
            rating=0.0,
            ranking=0,
            review="None",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    form.rating.data = movie.rating
    form.review.data = movie.review
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
