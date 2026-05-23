# Import
import email

from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text



app = Flask(__name__)

# Configuración SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Ruta principal (GET + POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        if not email or not text:
            return "Email and feedback text are required.", 400
        # Guardar en la base
        nuevo_feedback = Feedback(email=email, text=text)
        db.session.add(nuevo_feedback)
        db.session.commit()

        return redirect('/') # evita reenvío del formulario

    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_html = request.form.get('button_html')
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_html=button_html, button_python=button_python, button_discord=button_discord)


if __name__ == "__main__":
    app.run(debug=True)
