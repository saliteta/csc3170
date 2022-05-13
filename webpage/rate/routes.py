from rate import app
from rate import db
from rate import render_template
from rate.models import Item, User
from rate.forms import Register_form,  Login_form, Rate_form, Rerate_form
from flask import redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/rate')
@login_required
def rate_page():
    newRateForm = Rate_form()
    if newRateForm.validate_on_submit():
        print(newRateForm['submit'])
    items = Item.query.all()
    return render_template('rate.html', items = items, newRateForm = newRateForm) 
    # input an arguement called items. Passing the whole table called Item to the html
    #newRateForm will be access through the html file

@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    form = Register_form()
    if form.validate_on_submit(): # on submit means this action will only start to work when client click on submit
        user_to_create = User(username = form.username.data, email_address = form.email_address.data,password = form.password1.data)
        #pass the data from the form by writting form.filed.data
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'You have successfully created an count! You are logged in as: {user_to_create.username}', category = 'success')
        return redirect(url_for('rate_page'))

    # if the register form's requirement is not satisfied then: form.erros will not be an empty dictionary
    # forms.erros is a biult in dictionary
    if form.errors != {}:
        for err_msg in form.errors.values():
            #using print, it will print the error message to the sever side 
            #using flash, it will be return to the user side
            #flash will send the flash result to the html by using the get_flash_message with jinja syntax
            flash(f'There was an error with creating a user: {err_msg[0]}', category='danger')
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = Login_form()
    if form.validate_on_submit():
        attemped_user = User.query.filter_by(username = form.username.data).first() #filter the user name with the same with the username in the database
        if attemped_user and attemped_user.check_password_correction(attempted_password = form.password.data):
            #if true, login
            login_user(attemped_user)
            flash(f'Success! You are logged in as: {attemped_user.username}', category = 'success')
            return redirect(url_for('rate_page'))
        else:
            flash('Username and password are not match! Please try again', category = 'danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("you have been logout", category="info")
    return redirect(url_for("home_page"))



# creating html in the template
