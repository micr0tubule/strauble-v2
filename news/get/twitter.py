import tweepy 

consumer_key = 'HaVICyimwI15apzawXlaZvzxn'
consumer_secret = 'WprMebUWlJhQWywBYB3hAqKij2jp5moDbXsraK8FkxtrPxpKKQ'
access_token = '1357983754321604608-SoBrnDqwZqNax5jOOrpU0OeBArhKDX'
access_token_secret = '2rp3ZVUkiOuRZTQehvfA6LiYZjO0LfL1QpVQGpnaSzj3H'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_timeline(user, num_posts):
    timeline = api.user_timeline(user)
    timeline = timeline if num_posts > len(timeline) else timeline[:num_posts] 
    return list(map(lambda x: f'https://twitter.com/{user}/status/' + x._json["id_str"], timeline))
