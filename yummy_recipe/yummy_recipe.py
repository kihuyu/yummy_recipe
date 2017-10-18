import os
import sqlite3
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from tabledef import User, Recipecategory, Recipe
users = {}
recipecategories = {}
recipes = {}
user_session = False

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'yummy_recipe.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('YUMMY_RECIPE_SETTINGS', silent=True)





@app.route('/recipecategory')
def recipecategorys():
    if user_session == False:
        abort(401)
    entries = recipecategories
    recipez = recipes
    print(str(recipecategories))
    return render_template('recipecategory.html', entries=entries, recipez=recipez)


@app.route('/addrecipecategory', methods=['GET','POST'])
def add_recipe_category():
    if user_session == False:
        abort(401)
    if request.method == 'POST':
        newrecipe = str(request.form['recipecategory'])
        recipecategories[newrecipe] = str(request.form['furtherinfo'])
        flash('New category succesfully added')
        return redirect('/recipecategory')
    return render_template('addrecipecategory.html')

@app.route('/addrecipe', methods=['GET','POST'])
def add_recipe():
    if user_session == False:
        abort(401)
    if request.method == 'POST':
        newrecipe = str(request.form['recipename'])
        recipes[newrecipe] = str(request.form['steps'])
        flash('New Recipe succesfully added')
        return redirect('/recipecategory')
    return render_template('addrecipe.html')


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users[request.form['username']] = request.form['password']
        flash('New user successfully added')
        return redirect('/')
    return render_template('register.html')

@app.route('/', methods=['GET','POST'])
def login():
 
    if request.method == 'POST':
        key = request.form['username']
        value = request.form['password']
        if key in users and value == users[key]:
            global user_session
            user_session = True
            return redirect('/recipecategory')
        else:
            flash('Wrong credentials')
    
    return render_template('login.html')