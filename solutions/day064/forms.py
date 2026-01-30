from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


class FindMovieForm(FlaskForm):
    """Form to search for a movie by title."""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    """Form to edit the rating and review of a movie."""

    rating = FloatField(
        "Your Rating Out of 10 e.g. 7.5",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")
