import csv

class Blog(object):

    def __init__(self):
        super(Blog, self).__init__()

    def validate(self, username, title, body):
        errors = []
        if not username:
            errors.append('Username is required')
        if len(title) < 5:
            errors.append('Title must be atleast 5 characters')
        if len(body) < 5:
            errors.append('Body must be atleast 5 characters')
        return errors

    def new_post(self, username, title, body):
        errors = self.validate(username, title, body)
        if errors:
            return errors

        blog = open('blog.csv', 'a')
        data_file = csv.writer(blog)
        data_file.writerow([username, title, body])
        blog.close()
        return []

    def posts_by_user(self, username):
        posts = []
        for user_data in csv.reader(open('blog.csv', 'r')):
            if user_data[0] == username:
                posts.append(user_data)

        return posts