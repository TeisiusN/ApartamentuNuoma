from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, URL, EqualTo
from flask_ckeditor import CKEditorField

# Naudotojo registracijos forma
class UserRegistrationForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    confirm_password = PasswordField("Pakartoti slaptažodį", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Registruotis")

class UserLoginForm(FlaskForm):
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    submit = SubmitField("Prisijungti")

# Naudotojo registracijos forma
class UpdateProfileForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    confirm_password = PasswordField("Pakartoti slaptažodį", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Išsaugoti")

#Nuomotojo registracijos forma
class VendorRegistrationForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    submit = SubmitField("Registruotis")

# Užsakymo forma
class BookingForm(FlaskForm):
    room_type = SelectField('Kambario tipas', validators=[DataRequired()])
    arrival_date = DateField('Atvykimo data', validators=[DataRequired()])
    departure_date = DateField('Išvykimo data', validators=[DataRequired()])
    people_nr = StringField('Žmonių skaičius', validators=[DataRequired()])
    submit = SubmitField("Užsakyti")

