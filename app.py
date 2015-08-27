from user import User

import bottle


# me is the instance of current logged in user. `User` class here is a model
me = User()


@bottle.get('/statics/<filename>')
def statics(filename):
    '''
    This is used to render static files like css and js.
    If you need to render say `my_photo.png`, then :
        1) Copy it to statics folder in project directory
        2) Send a get request to `/statics/my_photo.png`
        3) Same for any other kind of file
    '''
    return bottle.static_file(filename, root='./statics')

#########################################################


@bottle.get('/')
def landing():
    '''
    HTTP get request to `/` is routed to this function.
        1) If user is logged in, send her to home page (secure page)
        2) Else show the landing template
    '''

    # Before proceeding, see is_authenticated method in `user.py`
    if me.is_authenticated():
        bottle.redirect('/home')
    return bottle.template('landing')


@bottle.get('/register')
def register():
    '''
    This is responsible for showing the registration form. 
        bottle.template() function looks for a `views` directory in project root.
        The argument passed (`register`) is the name of the template with `.tpl` omitted 
    '''
    return bottle.template('register')


@bottle.post('/register')
def registerPost():
    '''
    This `post` route handles form data from `/register` form. 
    Notice that same route name `/register` is used for handling both `get` and `post`
    Only the handler function is different.
    '''

    # Get the form data from request. An input can be refered to using the `name`
    # attribute mentioned in html. for example, in register form, to get
    # `username` do:
    username = bottle.request.forms.get('username')

    #################### TASK 1 ########################
    # get the real name and password attribute from form
    # just like `username` above
    # and save them as :
    # real_name = ...
    # password = ...

    # Once we have the attributes, we validate them to see if they are of right length etc.
    # This is also a domain logic, so let `me` handle this.
    # NOTE: We call `me.register` function, and expect a list of errors:
    #   1) If no errors, the user is registered, log the user in and redirect
    #   2) Else return errors to `register` template

    # Now open `user.py`'s  `register` method for TASK 2
    errors = me.register(username, real_name, password)
    if errors:
        return bottle.template('register', errors=errors)

    me.login(username, password)
    return bottle.redirect('/home')


@bottle.get('/login')
def login():
    '''
    Same logic as `/register`
    '''
    return bottle.template('login')


@bottle.post('/login')
def loginPost():
    username = bottle.request.forms.get('username')
    #################### TASK 3 ########################    
    # get `password` from the form and save it to password variable
    # password = ...

    # Now open `user.py`'s  `login` method for TASK 4 
    errors = me.login(username, password)
    if errors:
        return bottle.template('login', errors=errors)

    return bottle.redirect('/home')


@bottle.get('/logout')
def logout():
    '''
    This shows domain logic encapsulation. Here we (the controller) doesn't know how to logout
    the user. But it has access to the user model. Hence it tells the user model instance `me` 
    to logout. 

    Also see, that the model doesn't know what will happen to `views`. After loggging out, the 
    `controller` redirects to home, i.e. glueing views and models.

    `/` renders landing page view.
    '''

    #################### TASK 5 ########################
    # Implement the `logout` method in user.py    
    me.logout()
    return bottle.redirect('/')


@bottle.get('/home')
def home():
    '''
    This is your secure route. A place to save private info. 

    Here first we ask the user model if current user `me` is logged id.
        1) If not, then we redirect `me` to login page.
        2) Else we return the home `view` with secure `me` data, 
            which in this case is her `real_name` and `username`

    Notice how variables are being passed to the template

    '''
    if not me.is_authenticated():
        bottle.redirect('/login')
    return bottle.template('home', real_name=me.real_name(), username=me.username())


bottle.run(host='localhost', port=8000, debug=True, reloader=True)
