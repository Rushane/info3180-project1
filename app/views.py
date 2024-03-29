"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, ProfileForm
from werkzeug.utils import secure_filename
from app.models import UserProfile
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.

            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.

            # get user id, load into session
            login_user(user)

            # remember to flash a message to the user
            return redirect(url_for("home"))  # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)
    

@app.route("/profile",  methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            location = form.location.data
            email = form.email.data
            biography = form.biography.data
            gender = form.gender.data
            
            #form.photo.label.text = 'Browse...'
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            
            date_created = datetime.datetime.now().strftime("%B %d, %Y")
            
            new_user = UserProfile(firstname=firstname, lastname=lastname, biography=biography, photo=filename,
                gender=gender, location=location, created_on=date_created, email=email)
                
            db.session.add(new_user)
            db.session.commit()
           
            flash('Profile added', 'success')
            return redirect(url_for("profiles"))
    return render_template('profile.html', form=form)
    
    
@app.route("/profiles",  methods=["GET", "POST"])
def profiles():
    userlist = db.session.query(UserProfile).all()
    
    return render_template('profiles.html', userlist=userlist)
    
@app.route('/profile/<userid>')
def profileuserid(userid):
    """Render the website's profile/<userid> page."""
    
    user = UserProfile.query.filter_by(userid=userid).first()
    
    return render_template('profileuser.html', user=user)


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(userid))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
