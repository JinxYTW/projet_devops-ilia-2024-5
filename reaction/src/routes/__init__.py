from routes.get_reactions_route import tweet_reaction_bp
from routes.comment_route import comment_bp
from routes.supp_comments_route import supp_comment_bp
from routes.comment_update_route import update_comment_bp
from Ajouter_comment_reaction_route import  comment_reaction_bp
blueprints =[ tweet_reaction_bp, comment_bp,supp_comment_bp, update_comment_bp, comment_reaction_bp ]
