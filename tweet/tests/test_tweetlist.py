import unittest
from src.app import create_app

class TweetListRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_tweet_list_default_pagination(self):
        response = self.client.get('/tweetlist')
        self.assertEqual(response.status_code, 200)
        self.assertIn('tweets', response.json)
        self.assertIn('pagination', response.json)
        self.assertEqual(response.json['pagination']['current_page'], 1)
        self.assertEqual(response.json['pagination']['per_page'], 10)

    def test_get_tweet_list_custom_pagination(self):
        response = self.client.get('/tweetlist?page=1&limit=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('tweets', response.json)
        self.assertIn('pagination', response.json)
        self.assertEqual(response.json['pagination']['current_page'], 1)
        self.assertEqual(response.json['pagination']['per_page'], 2)
        
        # Verify the response structure matches swagger specification
        pagination = response.json['pagination']
        self.assertIn('total', pagination)
        self.assertIn('pages', pagination)
        self.assertIn('current_page', pagination)
        self.assertIn('per_page', pagination)

    def test_get_tweet_list_invalid_pagination(self):
        # Test invalid page number
        response = self.client.get('/tweetlist?page=0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json)

        # Test invalid limit
        response = self.client.get('/tweetlist?limit=101')
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json)

        # Test invalid parameter type
        response = self.client.get('/tweetlist?page=abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json)

    def test_tweet_list_content(self):
        response = self.client.get('/tweetlist?limit=1')
        self.assertEqual(response.status_code, 200)
        
        # Verify tweet structure matches swagger specification
        tweets = response.json['tweets']
        self.assertTrue(len(tweets) > 0)
        tweet = tweets[0]
        self.assertIn('id', tweet)
        self.assertIn('message', tweet)
        self.assertIn('autor', tweet)
        self.assertIn('reaction', tweet)
        
        # Verify reaction structure
        reaction = tweet['reaction']
        self.assertIn('like', reaction)
        self.assertIn('comment', reaction)
        self.assertIn('retweet', reaction)

if __name__ == '__main__':
    unittest.main() 