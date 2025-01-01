from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models.err_input import ErrInput
from models.user import User

users = [] # representa o banco de dados

# criando a aplicação ===============
app = Flask(__name__)

# cofigurando o login manager ===============
# https://flask-login.readthedocs.io/en/latest/
app.secret_key = 'super secret string'  # utilizado pelo login manager para criptografar a informação
login_manager = LoginManager(app) # inicializa o login manager
login_manager.login_view = "login" # página para a qual o usuário é redirecionado ao tentar acessar uma página protegida

# define o user_loader
# trata-se de um método que busca o usuário baseado em alguma chave. 
# Nesse exemplo pelo e-mail
@login_manager.user_loader
def user_loader(id) -> User:
    id = int(id)
    
    user = None
    for u in users:
        if u.id == id:
            user = u
            break
    
    return user

# definindo rotas ===============
@app.route("/")
def home():
    if current_user.is_authenticated: 
        return redirect(url_for('records'))
    
    return render_template("home.html")

@app.route("/new_account", methods=["GET", "POST"])
def new_account():
    if current_user.is_authenticated: 
        return redirect(url_for('records'))
    
    if request.method == 'POST':
        err_list = {}
        data = {
            'name': request.form.get('name'),
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }
        
        if len(data['name']) == 0:
            err_list['name'] = ErrInput('name', data['name'], 'Nome é necessário')
        if len(data['username']) == 0:
            err_list['username'] = ErrInput('username', data['username'], 'Usuário é necessário')
        if len(data['password']) == 0:
            err_list['password'] = ErrInput('password', data['password'], 'Senha é necessária')
        if len(err_list) > 0:
            return render_template("new_account.html", data=data, err_list=err_list)
        
        user = None
        for u in users:
            if u.username == data['username']:
                user = u
                break

        if user:
            return render_template("new_account.html", data=data, err_form='O usuário já existe')
        
        users.append( User( len(users) + 1, data['name'], data['username'], data['password']) )
        return redirect(url_for('login'))

    return render_template("new_account.html", data=None, err_list=None)

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if current_user.is_authenticated: 
        return redirect(url_for('records'))
    
    if request.method == 'POST':
        err_list = {}
        data = {
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }
        
        if len(data['username']) == 0:
            err_list['username'] = ErrInput('username', data['username'], 'Usuário é necessário')
        if len(data['password']) == 0:
            err_list['password'] = ErrInput('password', data['password'], 'Senha é necessária')
        if len(err_list) > 0:
            return render_template("login.html", data=data, err_list=err_list)
        
        user = None
        for u in users:
            if u.username == data['username'] and u.password == data['password']:
                user = u
                break
        
        if not user:
            return render_template("login.html", data=data, err_form='Credenciais inválidas')
        
        login_user(user)
        
        next = request.args.get('next')
        return redirect(next or url_for('records'))

    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/records')
@login_required
def records():
    # bons exemplos do jinja2
    # https://www.codecademy.com/learn/learn-flask-jinja2-templates-and-forms/modules/flask-jinja2-templates-and-forms/cheatsheet
    return render_template("records.html", current_user=current_user)

if __name__ == '__main__':
    app.run(debug=True)