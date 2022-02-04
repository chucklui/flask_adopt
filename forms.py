"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species Type", choices=[('cat', 'Cat'),
                                                     ('dog', 'Dog'),
                                                      ('porcupine', 'Porcupine')],
                                                      validators=[InputRequired()])
    photo_url = StringField("Image URL",
                            validators=
                                [InputRequired(),
                                URL(require_tld=False, 
                                    message='Please enter a valid URL.')])
    age = SelectField("Pet Age", choices=[('baby','Baby'),
                                         ('young','Young'),
                                          ('adult','Adult'),
                                          ('senior', 'Senior')],
                                           validators=[InputRequired()])
    notes = StringField("Notes", validators=[Optional()])
