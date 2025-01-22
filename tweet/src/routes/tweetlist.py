from flask import jsonify, request
from src.routes.blueprint import bp

# Mock data for demonstration - in real app, this would come from a database
MOCK_TWEETS = [
    {
        "id": 1,
        "message": "First tweet",
        "autor": "BiduleLaCartouse",
        "reaction": {"like": 10, "comment": 2, "retweet": 3}
    },
    {
        "id": 2,
        "message": "Second tweet",
        "autor": "BiduleLaCartouse",
        "reaction": {"like": 5, "comment": 1, "retweet": 2}
    }
]

@bp.route('/tweetlist', methods=['GET'])
def get_tweet_list():
    try:
        # Get pagination parameters
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        # Validate pagination parameters
        if page < 1 or limit < 1 or limit > 100:
            return jsonify({
                "message": "Invalid pagination parameters"
            }), 400

        # Calculate pagination
        start_idx = (page - 1) * limit
        end_idx = start_idx + limit
        
        # Get paginated tweets
        paginated_tweets = MOCK_TWEETS[start_idx:end_idx]
        
        total_tweets = len(MOCK_TWEETS)
        total_pages = (total_tweets + limit - 1) // limit

        return jsonify({
            "tweets": paginated_tweets,
            "pagination": {
                "total": total_tweets,
                "pages": total_pages,
                "current_page": page,
                "per_page": limit
            }
        }), 200

    except ValueError:
        return jsonify({
            "message": "Invalid pagination parameters"
        }), 400
    except Exception as e:
        return jsonify({
            "message": "Internal server error"
        }), 500 