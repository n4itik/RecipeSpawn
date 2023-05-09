from flask import Flask

app = Flask(__name__,template_folder='templates')


from img_to_recipe import routes