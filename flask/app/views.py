from flask import Flask, render_template, flash, redirect, url_for, request, session, g
from app import app, db, admin, models
import datetime
from .forms import addForm, modifyEntry, LoginForm, RegistrationForm
from functools import wraps
from flask_admin.contrib.sqla import ModelView
from app.models import User, Collection

################################################################################

#Modify the tables using a GUI localhost:5000/admin
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Collection, db.session))

################################################################################

@app.before_request #Acts as a wrapper to make a page password protected
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user'] #Global variable tracks session

################################################################################

@app.route('/')
def index():
    if g.user == None:
        return render_template('welcome.html') #rendering template
    else:
        userName = models.User.query.filter_by(username = session['user']).first()
    return render_template('welcome.html', userName=userName) #rendering template


################################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if g.user:
        flash('You are already logged in.')
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            registered_user = models.User.query.filter_by(username=username,password=password).first()
            if registered_user is None:
                flash('Invalid credentials. Please try again.') #Displays error message if login credentials are incorrect
            else:
                session['user'] = request.form['username'] #If credentials are correct then user will be redirected to home
                flash('You are now logged in. Welcome %s!'%(form.username.data)) #displays message to user upon login
            return redirect(url_for('viewHome'))
    return render_template('login.html') #rendering template

################################################################################

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    error = None
    if g.user: #Checks to see if the user is already signed in
        flash('You are already signed in. Please logout first.')
        return redirect(url_for('index'))
    else:
        if request.method == 'POST': #When the form is submitted, it will add the new item to the table
            registered_user = models.User.query.filter_by(username=request.form['username']).first()
            if registered_user is None:
                p = models.User(username=form.username.data,password=form.password.data, email=form.email.data, start_date=datetime.datetime.utcnow()) #Takes input from the form and turns it into an object that is ready to be added to the table
                db.session.add(p) #Adds the new entry to the database, though it is not visible
                db.session.commit() #Commits the entry that has been added making it visible in the table
                flash('Registration successful')
                return redirect(url_for('login'))
            else:
                flash('Error: username is already in use')
                return redirect(url_for('register'))
    return render_template('registration.html', title="Registration",error=error) #rendering template

################################################################################

@app.route('/logout')
def logout():
    if g.user:
        session.pop('user', None) #When get request is sent to logout route the value of true is replaced with none deleting the session key
        flash('You were successfully logged out')
        return redirect(url_for('login')) #redirecting user
    else:
        flash("You are not signed in.")
        return redirect(url_for('login'))

################################################################################

@app.route('/list', methods=['GET', 'POST'])
def viewHome():
    if g.user:
        form = addForm()
        user = models.User.query.filter_by(username = session['user']).first()
        readingList = []
        title = form.text1.data
        if request.method == 'POST' and form.validate_on_submit(): #When the form is submitted, it will add the new item to the table
            exists = models.Collection.query.filter_by(title=form.text1.data, user_id = user.id).first()
            if exists:
                flash('Already exists')
            else:
                p = models.Collection(title=form.text1.data,description=form.text2.data, author=form.text3.data, user_id=user.id, read=False, review="empty") #Takes input from the form and turns it into an object that is ready to be added to the table
                db.session.add(p) #Adds the new entry to the database, though it is not visible
                db.session.commit() #Commits the entry that has been added making it visible in the table
                flash('Successfully added %s to the list'%(form.text1.data))
                return redirect(url_for('viewHome'))
        for r in user.books.all():
            readingList.append(r)
        return render_template('main.html',title='List', books=user.books, form=form)
    else:
        flash("You are not signed in.")
        return redirect(url_for('login'))

################################################################################

@app.route('/review',methods=['GET', 'POST'])
def viewReview():
    form = modifyEntry()
    if g.user:
        title = form.title.data
        review = form.review.data
        user = models.User.query.filter_by(username=session['user']).first()
        found = False
        if form.validate_on_submit():  # When the form is submitted, it will add the new item to the table
            for r in user.books.all():
                if title == r.title:
                    r.read = True  # Sets read value to true so that it will appear as a completed review on completed.html
                    r.review = review
                    db.session.commit()
                    flash('Your review has been added!')
                    found = True
                    break
            if not found:
                flash('Error: Entry not valid!')
                return redirect(url_for('viewReview'))
        return render_template('review.html', title='Review', form=form)
    else:
        flash("You are not signed in.")
        return redirect(url_for('login'))


################################################################################

@app.route('/completed')
def viewCompleted():
    if g.user:
        user = models.User.query.filter_by(username = session['user']).first()
        readingList = []
        for r in user.books.all(): #Lists all books if read field is equal to true
                if r.read == True:
                    readingList.append(r)
        return render_template('completed.html',title='Completed', books=readingList)
    else:
        flash("You are not signed in.")
        return redirect(url_for('login'))
