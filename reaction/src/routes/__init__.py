from routes.ajouter_comment_reaction_route import  create_comment_reaction_bp
from routes.comment_get_route import comment_get_bp
from routes.comment_route import comment_bp
from routes.comment_update_route import update_comment_bp
from routes.delete_comment_route import delete_comment_bp
from routes.delete_reaction_comment_route import reactions_bp
from routes.get_reactions_stats_comment_route import tweet_reaction_stat_bp
from routes.reaction_tweet_route import reaction_bp
from routes.reaction_comment_route import comment_reaction_bp
from routes.tweet_reaction_route import tweet_reaction_bp

blueprints =[ create_comment_reaction_bp, comment_get_bp, comment_bp,
             update_comment_bp,delete_comment_bp, reactions_bp,
             tweet_reaction_stat_bp, reaction_bp, comment_reaction_bp,
             tweet_reaction_bp
            ]
