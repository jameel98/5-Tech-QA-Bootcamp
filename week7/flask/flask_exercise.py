from flask import Flask


class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return self.home()

        @self.app.route('/about')
        def about():
            return self.about()

    def home(self):
        return "Welcome to the Home Page!"

    def about(self):
        return "Welcome to about page."

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    app = MyApp()
    app.run()
