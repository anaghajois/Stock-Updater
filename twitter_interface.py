import tweepy
import glob
import random
import os
import time

#Personal, every user should complete.
def tweet_images_in_folder(folder_name):
    api_key = os.environ['TWITTER_API_KEY']
    api_secret = os.environ['TWITTER_API_SECRET']
    oauth_token = os.environ['TWITTER_OAUTH_TOKEN'] # Access Token
    oauth_token_secret = os.environ['TWITTER_OAUTH_TOKEN_SECRET'] # Access Token Secret
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(oauth_token, oauth_token_secret)
    api = tweepy.API(auth)
    #Changes directory to where the script is located (easier cron scheduling, allows you to work with relative paths)
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    def tweet_all(folder):
        #Takes the folder where your images are as the input and tweets all files in it.
        images = glob.glob(folder + "*")
        for image in images:
            print image
            api.update_with_media(image)
            time.sleep(1)
    tweet_all(folder_name)
