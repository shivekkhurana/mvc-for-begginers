import bottle


class User:

    def __init__(self):
        pass

    def is_authenticated(self):
        if self.username():
            return True
        return False

    def real_name(self):
        return bottle.request.get_cookie('real_name')

    def username(self):
        return bottle.request.get_cookie('username')

    def is_username_available(self, username):
        # open users file and check if username is alread written to it
        pass

    def register(self, username, real_name, password):
        # create or open users file and save this row as csv if username is available
        pass

    def login(self, username, password):
        # save a username cookie
        pass

    def logout(self):
        # delete that cookie
        bottle.response.delete_cookie('real_name')
        bottle.response.delete_cookie('username')

    def delete_account(self, username):
        pass
