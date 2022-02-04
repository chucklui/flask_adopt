"""Flask app for adopt app."""
from models import Pet
from flask import Flask, render_template, redirect, flash
from forms import AddPetForm

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def homepage():
    """ Display list of pets on the home page """
    pets = Pet.query.all()
    return render_template('list_pets.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """doc"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        # do stuff with data/insert to db

        flash(f"Added {name}")
        # redirect to homepage if validate
        return redirect("/")

    else:
        return render_template(
            "add_pet_form.html", form=form)
        
@app.route('/<pet_id_number>',methods=["GET", "POST"])
def show_pet_and_form(pet_id_number):
    """doc"""

    pet = Pet.query.get_or_404(pet_id_number)

    name = pet.name
    age = pet.age
    species = pet.species
    photo = pet.photo_url

    return render_template('show_pet.html', pet = pet)
