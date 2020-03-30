from flask import Flask, render_template, request
from random import choice
from backend import *
from nocache import nocache




web_site = Flask(__name__)
web_site.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@nocache

@web_site.route('/')

def index():
  overwrite()
  return render_template('index.html')
@nocache

@web_site.route('/', methods=['POST'])
def my_form_post():
  text = request.form['text']
  get_cases(text)
  return render_template('index.html')
@web_site.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
@web_site.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


web_site.run(host='0.0.0.0', port=8080)
