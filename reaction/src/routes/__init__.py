from routes.get_reactions_route import tweet_reaction_bp
from routes.comment_route import comment_bp
from routes.reaction_tweet_route import reaction_bp
from routes.reaction_comment_route import comment_reaction_bp
blueprints =[ tweet_reaction_bp, comment_bp,reaction_bp, comment_reaction_bp ]
