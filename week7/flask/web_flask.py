from flask import Flask, render_template


class UserProfileApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

        # Sample user data
        self.users = {
            "john": {"name": "John Doe", "age": 30, "email": "john@example.com"},
            "jane": {"name": "Jane Smith", "age": 25, "email": "jane@example.com"},
            "doe": {"name": "Doe Ray", "age": 22, "email": "doe@example.com"}
        }

    def setup_routes(self):
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/user/<username>', 'profile', self.profile)

    def home(self):
        return render_template('home.html', users=self.users)

    def profile(self, username):
        user = self.users.get(username)
        if user:
            return render_template('profile.html', user=user)
        else:
            return "User not found", 404

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    app = UserProfileApp()
    app.run()
