import bottle


class User:

    def __init__(self):
        pass

    def is_authenticated(self):
        '''
        If `username` is not None, return true 
        '''
        if self.username():
            return True
        return False

    def real_name(self):
        return bottle.request.get_cookie('real_name')

    def username(self):
        '''
        Get value of `username` cookie
        '''
        return bottle.request.get_cookie('username')

    def is_username_available(self, username):
        # open users file and check if username is already written to it
        # if yes then username is taken, return false, otherwise return true
        pass

    def register(self, username, real_name, password):
        errors = []
        #################### TASK 2.1 ########################
        # Complete `is_user_name_available` method above

        #################### TASK 2.2 ########################
        # open users.csv file and save this row as csv if username is available
        # NOTE: 
        # The controller is expecting a list of errors, if no error, return an empty list
        return errors

    def login(self, username, password):
        #################### TASK 4 ########################    
        # Here we need to check if user exists and password is correct
        # NOTE: The controller is still expecting an array of `errors`, if no errors, return []

        # Add code to itearate over `users.csv` until it finds a row where `row[0]` == `username`
        # 1) If it does find a row:
        #       a) Check if row[2] == `password`
        #           i) If so, then set a cookie to establish identity and return []
        #           ii) If not, then set 'Invalid password' error
        # 2) If it doesn't find a row, set an error 'Username not registered'  


        # You need to set two cookies if login succesful, one for `real_name` and other for `username`

        ######## HINT ########
        # To set a cookie, do this 
        # bottle.response.set_cookie('Key', `Value`)
        
        pass

    def logout(self):
        # delete the cookies that establish identity of the user, 
        #i.e. `username` cookie and `real_name` cookie.
        

        ######## HINT ########
        # To delete a cookie, do this
        # bottle.response.delete_cookie('real_name')
        pass

    def delete_account(self, username):
        pass
