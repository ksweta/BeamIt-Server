
def create_signup_routes(app):

    @app.route('/')
    def signup():
        return 'Hello world'
