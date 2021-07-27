from bottle import Bottle, run, route, request, redirect, post, template
from bottle_flash2 import FlashPlugin

# Flash Setup
app = Bottle()
COOKIE_SECRET = 'super_secret_string'
app.install(FlashPlugin(secret=COOKIE_SECRET))

@route('/')
def sample():
    return template('index.html', app = app)

@route('/done')
def done_get():
    redirect('/')

@post('/done')
def done_post():
    app.flash("FLASH MESSAGE")
    app.flash("Using SimpleTemplate")
    app.flash(request.forms.get('message'))
    return template('done.html', app = app)

run(host='localhost', port=8080, debug=True)
