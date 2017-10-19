import os
import sqlite3
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from tabledef import User, Recipecategory, Recipe
current_user = User('admin', 'admin', 'admin')
current_category = Recipecategory('No category')
current_recipe = Recipe('No recipe', 'No Steps', current_category)
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
    global current_category
    global current_recipe
    entries = current_category
    recipes = current_recipe
    print(recipes.recipecategory)
    return render_template('recipecategory.html', entries=entries, recipes=recipes)

@app.route('/deleterecipecategory', methods=['POST'])
def delrecipecategorys():
    global current_category
    global current_recipe
    current_category = Recipecategory('No category')
    entries = current_category
    recipes = current_recipe
    return render_template('recipecategory.html', entries=entries, recipes=recipes)


@app.route('/deleterecipe', methods=['POST'])
def delrecipes():
    global current_recipe
    global current_category
    current_recipe = Recipe('No recipe', 'No Steps', current_category)
    entries = current_category
    recipes = current_recipe
    return render_template('recipecategory.html', entries=entries, recipes=recipes)


@app.route('/addrecipecategory', methods=['GET','POST'])
def add_recipe_category():
    global user_session
    global current_category
    if user_session == False:
        abort(401)
    if request.method == 'POST':
        current_category = Recipecategory(request.form['recipecategory'])
        flash('New category succesfully added')
        return redirect('/recipecategory')
    return render_template('addrecipecategory.html')


@app.route('/addrecipe', methods=['GET','POST'])
def add_recipe():
    global user_session
    global current_recipe
    global current_category
    entries = current_category
    if user_session == False:
        abort(401)
    if request.method == 'POST':
        current_recipe = Recipe(request.form['recipename'], request.form['steps'], current_category)
        current_recipe.recipecategory = request.form.get('recipecategory')
        flash('New Recipe succesfully added')
        return redirect('/recipecategory')
    return render_template('addrecipe.html', entries=entries)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        global current_user
        if (request.form['password'] != request.form['confirmpassword']):
            flash('Passwords do not match')
            return redirect('/register')
        current_user = User(request.form['username'], request.form['password'], request.form['name'])
        flash('New user successfully added')
        return redirect('/')
    return render_template('register.html')

@app.route('/', methods=['GET','POST'])
def login():
 
    if request.method == 'POST':
        userattempt = request.form['username']
        passwordattempt = request.form['password']
        global current_user
        if userattempt == current_user.username and passwordattempt == current_user.password: 
            global user_session
            user_session = True
            return redirect('/recipecategory')
        else:
            flash('Wrong credentials')
    
    return render_template('login.html')