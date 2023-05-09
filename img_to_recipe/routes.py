from flask import render_template, url_for, flash, redirect, request
from img_to_recipe import app
from img_to_recipe.output import output
import os


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    imagefile = request.files['imagefile']
    image_path = os.path.join(app.root_path, 'static/images/uploads', imagefile.filename)
    imagefile.save(image_path)
    img = "/images/uploads/" + imagefile.filename
    title, ingredients, recipe = output(image_path)
    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)


@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile = os.path.join(app.root_path, 'static\\images', str(samplefoodname) + ".jpg")
    img = "/images/" + str(samplefoodname) + ".jpg"
    title, ingredients, recipe = output(imagefile)
    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)
