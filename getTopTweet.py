import requests
import tweepy

accessToken = "3090377897-JA6gCWhRwolsaCW82hyToq76GKGO4Sec6iG5zUl"
accessTokenSecret = "a9ngGUk0yJpqg97NUTDHfhTw4VqqtgNXbvzqom1NbQY8f"
consumerKey = "t41SayBTK9RJtSs3gUoJRPLe6"
consumerKeySecret = "FjJliaQ72VuDEz2p3sJjU5I9MUsRyaxJ6vPsAmlMt4PJTihGUl"
    

def getTweet():
    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)

    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name="WHO", exclude_replies=True, include_rts=False, count=20)

    usableTweets = []

    allTweets = [tweet.text for tweet in tweets]
    for t in allTweets:
        usableTweets.append(t)

    return usableTweets[0]
