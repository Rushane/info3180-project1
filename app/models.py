from . import db

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    userid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(300))
    created_on = db.Column(db.String(40))
    photo = db.Column(db.String(80))
    
    def __init__(self,firstname,lastname,gender,email,location,biography,created_on,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.created_on = created_on
        self.photo = photo
    
 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
