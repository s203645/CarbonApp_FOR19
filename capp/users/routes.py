from flask import render_template, Blueprint, redirect, flash, url_for
from capp.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your account has been created!', 'success')
        return redirect(url_for('home.home_home'))
    return render_template('users/register.html', title='register', form=form)

@users.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'test@demo.com' and form.password.data == 'test':
        flash('You successfully signed in!', 'success')
        return redirect(url_for('home.home_home'))
    else:
        flash('Login Failed. Please enter correct email and password.', 'danger')  
  return render_template('users/sign_in.html', title='sign_in', form=form)

