"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species Type", validators=[InputRequired()])
    photo_url = StringField("Image URL",
                            validators=
                                [InputRequired(),
                                URL(require_tld=False, 
                                    message='Please enter a valid URL.')])
    age = IntegerField("Pet Age", validators=[InputRequired()])
    notes = StringField("Notes", validators=[Optional()])
