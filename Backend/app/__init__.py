from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danlowo:icui4cuicu2@localhost/blogify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'daniel'
db = SQLAlchemy(app)

login_managers = LoginManager()
login_managers.session_protection = 'strong'
login_managers.login_view = 'auth.login'

login_managers.init_app(app)


from app.auth.controller import auth as auth_print
from app.blogger.controller import blogger as blogger_print
from app.main.controller import main as main_print



app.register_blueprint(auth_print)
app.register_blueprint(blogger_print)
app.register_blueprint(main_print)


# db.create_all()
