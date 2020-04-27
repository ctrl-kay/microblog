from flask import render_template #import render template function
from app import app	
from app.forms import LoginForm # import LoginForm class from app.forms module

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Kaylan'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST']) # GET default request type, added in POST
def login():
    form = LoginForm() # instantiate form LoginForm object
    if form.validate_on_submit(): # when submit button is clicked, process form data
    	flash('Login request for user {}', remember_me={}.format( # store flash message
    		form.username.data, form.remember_me.data))
    	return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)