from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 

class User(object):
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

class Recipecategory(object):
    def __init__(self, recipecategory):
        self.recipecategory = recipecategory

    def __del__(self):
        print "Category deleted"

    def editcategory(self, editedcategory):
        if (editedcategory != ''):
            self.recipecategory = editedcategory
        return self.recipecategory


    
class Recipe(Recipecategory):
    def __init__(self, recipe, steps, recipecategory):
        Recipecategory.__init__(self, recipecategory)
        self.recipe = recipe
        self.steps = steps

    def __del__(self):
        print "Recipe deleted" 

    def editrecipe(self, editedrecipe):
        if (editedrecipe != ''):
            self.recipe = editedrecipe
        return self.recipe

    def editrecipe(self, editedsteps):
        if (editedsteps != ''):
            self.steps = editedsteps
        return self.steps

    