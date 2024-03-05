from flask import Flask, redirect, url_for, render_template, request
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import jwt
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Função para enviar e-mail
def send_email(to_email, token):
    subject = "Seu Token de Acesso"
    body = f"Seu token de acesso é: {token}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "seu_email@gmail.com"
    msg["To"] = to_email

    # Configurar servidor SMTP e enviar e-mail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("seu_email@gmail.com", "sua_senha")
        server.sendmail("seu_email@gmail.com", to_email, msg.as_string())

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Lógica de autenticação aqui (substitua pelo seu sistema real)
    if username == "usuario" and password == "12345":
        user = User(username)
        login_user(user)

        # Geração de token e envio por e-mail
        token = jwt.encode({"username": username}, "chave_secreta", algorithm="HS256")
        send_email("user@example.com", token)

        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login_page'))

# Rota protegida
@app.route('/dashboard')
@login_required
def dashboard():
    return f"Bem-vindo, {current_user.id}!"

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

# Rota para a página de login
@app.route('/')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=5001)