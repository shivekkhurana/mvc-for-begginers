from user import User

import bottle

me = User()

@bottle.get('/statics/<filename>')
def statics(filename):
    return bottle.static_file(filename, root='./statics')

#########################################################

@bottle.route('/')
def landing():
    if me.is_authenticated(): bottle.redirect('/home')
    return bottle.template('landing')

@bottle.get('/register')
def register():
    return bottle.template('register')

@bottle.get('/login')
def login():
    return bottle.template('login')

@bottle.get('/logout')
def logout():
    me.logout()
    return bottle.redirect('/')


@bottle.get('/home')
def home():
    if not me.is_authenticated(): bottle.redirect('/login')
    return bottle.template('home', real_name = me.real_name(), username = me.username())



bottle.run(host='localhost', port=8000, debug=True, reloader=True)