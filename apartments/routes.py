from flask import render_template, url_for, redirect, flash, request
from apartments import app, db
from apartments.forms import UserRegistrationForm, BookingForm, UpdateProfileForm, UserLoginForm, VendorRegistrationForm
from apartments.models import User, PropertyOwner, Apartment, Tenant, Room, RoomType, Feedback, room_reservation, \
    BookingStatus, Booking, Bill, Payment, admin_only, owner_only
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/apartment")
@admin_only
def show_apartment():
    form = BookingForm()
    return render_template('apartment.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = UserRegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            name=form.name.data,
            last_name=form.name.data,
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
            birth_date=form.birth_date.data,
            phone_number=form.phone_number.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("main_page"))
    return render_template("register.html", form=form)


@app.route("/register-for-owner", methods=["GET", "POST"])
def register_for_owner():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = VendorRegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            name=form.name.data,
            last_name=form.name.data,
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
            birth_date=form.birth_date.data,
            phone_number=form.phone_number.data
        )
        new_company = PropertyOwner(
            company_name=form.company_name.data
        )
        new_user.property_owner.append(new_company)
        db.session.add(new_user)
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for("main_page"))
    return render_template("register-for-owner.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = UserLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main_page'))
        else:
            flash('Prisijungimas nesėkmingas. Bandykite dar kartą.', 'danger')

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main_page'))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile_page():
    form = UpdateProfileForm(
        name=current_user.name,
        last_name=current_user.last_name,
        username=current_user.username,
        email=current_user.email,
        birth_date=current_user.birth_date,
        phone_number=current_user.phone_number
    )
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        db.session.commit()
        flash('Jūsų duomenys sėkmingai atnaujinti!', 'success')
        return redirect(url_for('profile_page'))
    return render_template("profile.html", form=form)


@app.route("/booking-history")
@login_required
# @owner_only
def history_page():
    print(current_user.id)
    user_tenant_id = Tenant.query.filter(Tenant.fk_user_id == current_user.id).with_entities(Tenant.id).all()
    try:
        result = Booking.query.filter(Booking.fk_tenant_id == user_tenant_id[0][0]).filter(Booking.status == BookingStatus.finished).all()
    except IndexError:
        result = []

    print(result[0].id)
    test = db.session.query(room_reservation, Booking, Room).join(Booking).join(Room).all()
    print(test)
    for room_res, booking_res, booking, room in test:
        print(room_res, booking_res, booking.id, room.id)

    return render_template("booking-history.html", history=result)
