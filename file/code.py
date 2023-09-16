import tweepy

# Twitter API credentials
consumer_key = "give api"
consumer_secret = "give api secret"
access_token = "give access_token key"
access_token_secret = "give access_tocken secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def calculate_fake_percentage(username):
    try:
        user = api.get_user(screen_name=username)  
        followers_count = user.followers_count
        tweets_count = user.statuses_count
        fake_percentage = (followers_count + 1) / (tweets_count + 1) 
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

if fake_percentage >= 100:
    print("This account is likely to be a professional account")
else:
    print("This account is likely to be a personal/bot account")
