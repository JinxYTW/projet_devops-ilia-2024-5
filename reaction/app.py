from flask import Flask
#from routes.user_routes import user_bp
from routes.get_reactions_route import tweet_Reactions_bp

def create_app():
    app = Flask(__name__)
#   app.register_blueprint(user_bp)
    app.register_blueprint(tweet_Reactions_bp)
    return app
