import bottle
import csv


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
        for user_data in csv.reader(open('users.csv', 'r')):
            if user_data[0] == username:
                return False
        return True

    def validate_credentials(self, username, real_name, password):
        errors = []
        if len(username) < 4:
            errors.append('Username should be atleast 4 characters')
        if ' ' in username:
            errors.append('Username cannot contain spaces')
        if len(password) < 6:
            errors.append('Password should be atleast 6 characters')
        if len(real_name) < 4:
            errors.append('Real name should be atleast 4 characters')
        if not self.is_username_available(username):
            errors.append('Username already taken')

        return errors

    def register(self, username, real_name, password):
        errors = self.validate_credentials(username, real_name, password)
        if errors:
            return errors
        # create or open users file and save this row as csv if username is
        # available
        users = open('users.csv', 'a')
        data_file = csv.writer(users)
        data_file.writerow([username, real_name, password])
        users.close()
        return []

    def login(self, username, password):
        me = None
        for user_data in csv.reader(open('users.csv', 'r')):
            if user_data[0] == username:
                me = user_data
                break

        if not me: return ['Username not registered']
        if me[2] != password: return ['Password invalid']
        else:
            bottle.response.set_cookie('username', user_data[0])
            bottle.response.set_cookie('real_name', user_data[1])

        return []

    def logout(self):
        # delete that cookie
        bottle.response.delete_cookie('real_name')
        bottle.response.delete_cookie('username')

    def delete_account(self, username):
        pass
