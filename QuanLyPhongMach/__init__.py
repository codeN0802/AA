from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nghi0802@localhost/qlpm3?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
app.config['ROOT_PROJECT_PATH'] = app.root_path
db = SQLAlchemy(app=app)
admin = Admin(app=app, name="OU HOSPITAL", template_mode="bootstrap4")