from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, URL, EqualTo, Email, ValidationError
from flask_ckeditor import CKEditorField
from apartments.models import User

# Naudotojo registracijos forma
class UserRegistrationForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired(), Email()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    confirm_password = PasswordField("Pakartoti slaptažodį", validators=[DataRequired(), EqualTo('password')])
    birth_date = DateField("Gimimo data", validators=[DataRequired()])
    phone_number = IntegerField("Telefono numeris", validators=[DataRequired()])
    submit = SubmitField("Registruotis")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class UserLoginForm(FlaskForm):
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    submit = SubmitField("Prisijungti")

# Naudotojo registracijos forma
class UpdateProfileForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired(), Email()])
    birth_date = DateField("Gimimo data", validators=[])
    phone_number = IntegerField("Telefono numeris", validators=[])
    submit = SubmitField("Išsaugoti")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

#Nuomotojo registracijos forma
class VendorRegistrationForm(FlaskForm):
    name = StringField("Vardas", validators=[DataRequired()])
    last_name = StringField("Pavardė", validators=[DataRequired()])
    username = StringField("Prisijungimo vardas", validators=[DataRequired()])
    email = StringField("El. paštas", validators=[DataRequired()])
    password = PasswordField("Slaptažodis", validators=[DataRequired()])
    confirm_password = PasswordField("Pakartoti slaptažodį", validators=[DataRequired(), EqualTo('password')])
    birth_date = DateField("Gimimo data", validators=[DataRequired()])
    phone_number = IntegerField("Telefono numeris", validators=[DataRequired()])
    company_name = StringField("Įmonės pavadinimas", validators=[DataRequired()])
    submit = SubmitField("Registruotis")

# Užsakymo forma
class BookingForm(FlaskForm):
    room_type = SelectField('Kambario tipas', validators=[DataRequired()])
    arrival_date = DateField('Atvykimo data', validators=[DataRequired()])
    departure_date = DateField('Išvykimo data', validators=[DataRequired()])
    people_nr = StringField('Žmonių skaičius', validators=[DataRequired()])
    submit = SubmitField("Užsakyti")

