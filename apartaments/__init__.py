from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap(app)

from apartaments import routes