from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db
from market import csrf


@app.route('/')  # defining a root url
@app.route('/home')
def home_page():
    return render_template('home.html')

# the way we display data in template is to define a parameter "item_name" in render_template() and to assignt some data
# to this parameter. in templates we use {{ <item_name> }}
@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/about/<username>')
# <it is called dynamic routing>
def about(username):
    return f'{username}, I want to inform you, that Vania died...'


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():  # on_submit check if user has clicked on submit button
        user_to_create = User(username=form.username.data,
                              # we use "form.username.data" to pass values to function from the submitted form
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:  # if there are no errors after validation
        for error in form.errors.values():
            print(f'there was an error when creating user {error}')

    return render_template('register.html', form=form)
