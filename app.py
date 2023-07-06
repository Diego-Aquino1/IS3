from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from Backend.blueprints.task_blueprint import task_blueprint

app = Flask(__name__,template_folder='Frontend',static_folder='Frontend/static')
# para que utilice vue compilado ( npm run build ). En la carpeta dist, esta lo compilado de vue
# app = Flask(__name__, template_folder= './Frontend')

app.register_blueprint(task_blueprint)

cors = CORS(app)
app.config['SECRET_KEY'] = 'keyy'

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def dender_vue(path):
#     return render_template("index.html")

# @app.route('/')
# def index():
#     return render_template('accounts/login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('home/index.html')

@app.route('/profesores')
def teacher():
    return render_template('home/teachers.html')

@app.route('/correos')
def mail():
    return render_template('home/mails.html')


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica para autenticar al usuario y redirigir a la página deseada
        return 'Inicio de sesión exitoso'
    return render_template('accounts/login.html', form=form)

@app.route('/register')
def register():
    return render_template('accounts/register.html')

if __name__ == "__main__":
    app.run(debug=True)
