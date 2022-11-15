from flask import  render_template, url_for, redirect
from apartaments import app
from apartaments.forms import UserRegistrationForm,  BookingForm, UpdateProfileForm, UserLoginForm
# from apartaments.models import

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/apartment")
def show_apartment():
    form = BookingForm()
    return render_template('apartment.html', form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegistrationForm()
    #Test
    if form.validate_on_submit():
        return redirect(url_for('main_page'))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLoginForm()
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    return redirect(url_for('main_page'))

@app.route("/profile")
def profile_page():
    form = UpdateProfileForm()
    return render_template("profile.html", form=form)

@app.route("/booking-history")
def history_page():
    return render_template("booking-history.html")