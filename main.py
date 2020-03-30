from flask import Flask, render_template, request, abort, make_response
from backend import *
from nocache import nocache


web_site = Flask(__name__)
web_site.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@nocache

@web_site.route('/')

def index():
  overwrite()
  get_file()
  return render_template('index.html')
@nocache

@web_site.route('/', methods=['POST'])
def my_form_post():
  text = request.form['text']
  res = make_response("Setting a cookie")
  res.set_cookie('state', text)
  get_cases(text)
  return render_template('index.html')
@web_site.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
@web_site.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
@web_site.errorhandler(418)
def im_a_teapot(error):
    return render_template('418.html'), 200
@web_site.route('/background_process_test')
def background_process_test():
  get_file()
  return ("nothing")
@web_site.route('/about')
def about():
  return render_template('about.html')
@web_site.route('/coffee')
def call_im_a_teapot():
  abort(418)
web_site.run(host='0.0.0.0', port=8080)
