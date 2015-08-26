from user import User
from blog import Blog

import bottle

me = User()

@bottle.get('/statics/<filename>')
def statics(filename):
    return bottle.static_file(filename, root='./statics')

#########################################################

@bottle.get('/')
def landing():
    if me.is_authenticated(): bottle.redirect('/home')
    return bottle.template('landing')

@bottle.get('/register')
def register():
    return bottle.template('register')

@bottle.post('/register')
def registerPost():
    username = bottle.request.forms.get('username')
    real_name = bottle.request.forms.get('real-name')
    password = bottle.request.forms.get('password')

    errors = me.register(username, real_name, password)
    if errors:
        return bottle.template('register', errors=errors)

    me.login(username, password)
    return bottle.redirect('/home')

@bottle.get('/login')
def login():
    return bottle.template('login')

@bottle.post('/login')
def loginPost():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    errors = me.login(username, password)
    if errors:
        return bottle.template('login', errors=errors)

    return bottle.redirect('/home')

@bottle.get('/logout')
def logout():
    me.logout()
    return bottle.redirect('/')


@bottle.get('/home')
def home():
    if not me.is_authenticated(): bottle.redirect('/login')
    return bottle.template('home', real_name = me.real_name(), username = me.username(), posts=Blog().posts_by_user(me.username()))

@bottle.post('/new-blog-post')
def new_post(): 
    if not me.is_authenticated(): bottle.redirect('/login')

    title = bottle.request.forms.get('title')
    body = bottle.request.forms.get('body')

    errors = Blog().new_post(me.username(), title, body)
    if errors: 
        return bottle.template('home', real_name = me.real_name(), username = me.username(), posts=Blog().posts_by_user(me.username()), errors=errors)

    else: 
        return bottle.redirect('/home')

bottle.run(host='localhost', port=8000, debug=True, reloader=True)