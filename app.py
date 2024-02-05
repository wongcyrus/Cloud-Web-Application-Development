from flask import Flask, render_template, redirect, flash
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/index")
def index():
    user = {'username': "Miguel"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():   
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form = form)