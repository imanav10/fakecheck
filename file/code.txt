import tweepy

# Twitter API credentials
consumer_key = "enter your api key"
consumer_secret = "enter your api secret key"
access_token = "enter access token code"
access_token_secret = "enter access token secret code"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def calculate_fake_percentage(username):
    try:
        user = api.get_user(screen_name=username)  
        followers_count = user.followers_count
        tweets_count = user.statuses_count
        fake_percentage = (followers_count + 1) / (tweets_count + 1) * 100
        fake_percentage = round(fake_percentage, 2)
        return fake_percentage

    except tweepy.error.TweepError as e:
        if "Not Found" in str(e):
            return "User not found"
        else:
            return f"Error: {e}"

if __name__ == "__main__":
    username = input("Enter the Twitter username: ")
    fake_percentage = calculate_fake_percentage(username)
    print(f"Fake Percentage for @{username}: {fake_percentage}%")
