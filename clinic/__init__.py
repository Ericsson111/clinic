import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from functools import wraps
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' # SQL db, connect to site.db
app.config['SQLALCHEMY_BINDS'] = {'detail' : 'sqlite:///detail.db',
                                  'patient' : 'sqlite:///patient.db',
                                  'medicine' : 'sqlite:///medicine.db',
                                  'announcement': 'sqlite:///announcement.db',
                                  'work_log': 'sqlite:///worklog.db'}    
db = SQLAlchemy(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 578
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = 'clinicdonotreply@gmail.com'
app.config['MAIL_PASSWORD'] = 'idontcarelol'
mail = Mail(app) 

from clinic import routes