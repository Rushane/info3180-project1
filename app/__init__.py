from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wcwnsxblfdiwuw:bbf85b778237cfa7ce72b95422b62b73231e1c8f7f64e57d2036ae0ca23a5cbd@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d49k22fhkfboe4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
