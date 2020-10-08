# Import tweepy as tw
import tweepy as tw
import sys
from datetime import datetime as dt
from elasticsearch import Elasticsearch

def acqData(search, acq):

    index_name = idx + dt.today().strftime('%Y-%m-%d')
    feed = []
    
    print('::Acquiring Data::')
   
    for tweet in tw.Cursor(api.search, q=search, tweet_mode='extended').items(acq):
        feed.append(tweet._json)

    count = 0
    
    print('::Transferring to Elasticsearch Search::')
    
    while count < len(feed):
        tweet_date = feed[count]['created_at']
        username = feed[count]['user']['screen_name']
        account_creation_date = feed[count]['created_at']
        user_description = feed[count]['user']['description']
        user_url = feed[count]['user']['url']
        verified_status = feed[count]['user']['verified']
        geo_enabled = feed[count]['user']['geo_enabled']
        friends_count = feed[count]['user']['friends_count']
        followers_count = feed[count]['user']['followers_count']
        retweeted_count = feed[count]['retweet_count']
        favorite_count = feed[count]['favorite_count']
        hashtags = feed[count]['entities']['hashtags']
        tweet_full_text = feed[count]['full_text']

        doc = {
            '@timestamp': dt.now(),
            'tweet_date': tweet_date,
            'username': str(username),
            'account_creation_date': str(account_creation_date),
            'user_description': str(user_description),
            'user_url': str(user_url),
            'verified_status': bool(verified_status),
            'geo_enabled': bool(geo_enabled),
            'friends_count': int(friends_count),
            'followers_count': int(followers_count),
            'retweeted_count': int(retweeted_count),
            'favorite_count': int(favorite_count),
            'hashtags': hashtags,
            'tweet_full_text': str(tweet_full_text),
            'word_list': str(tweet_full_text).split(' ')
        }

        es.index(index=index_name, body=doc)
        
        count +=1
    
    print(f'Processed {tweet_count} records of {search} to {server}')
   
def help():
    print('usage: \n python3 grabTweets.py ["search"] [tweet_count] ["elasticsearch node"] \n')
    print(f'    python3 grabTweets.py "palantir OR PLTR" 2500 "172.16.100.200" "palantir-index-" \n')

try:
    search = sys.argv[1] 
    tweet_count = sys.argv[2]
    server = sys.argv[3]
    idx = sys.argv[4]

    # Import keys from a saved file instead of inputting it directly into the script.  
    # Strip whitespaces and split on = as I only want the key values
    key_location = 'twitter.keys'
    apikeys = []
    with open(key_location) as keys:
        for i in keys:
            apikeys.append(i.split("=")[1].strip(" ").strip("\n"))
    keys.close()

    # Initialize dictionary
    twitter_cred = dict()

    # Enter API keys
    twitter_cred["CONSUMER_KEY"] = apikeys[0]
    twitter_cred["CONSUMER_SECRET"] = apikeys[1]

    # Access Tokens
    twitter_cred["ACCESS_KEY"] = apikeys[2]
    twitter_cred["ACCESS_SECRET"] = apikeys[3]

    # Set authentication object
    auth = tw.OAuthHandler(twitter_cred["CONSUMER_KEY"], twitter_cred["CONSUMER_SECRET"])
    auth.set_access_token(twitter_cred["ACCESS_KEY"], twitter_cred["ACCESS_SECRET"])

    # Create api object with authentication
    api = tw.API(auth, wait_on_rate_limit=True)

    # Set Elasticsearch Server
    es = Elasticsearch(server, port=9200)

    # Execute search
    acqData(str(search), int(tweet_count))

except FileNotFoundError:
    # Key not found
    print(f'\n !!! You need to create a twitter.key file !!!\n')
    print(f'*** If you haven't done so, create a twitter.key file in the same directory of this script ***')
    print(f'Example of twitter.key file:\n')
    print(f'api_key = [key]\n api_secret_key = [key]\n access_token = [key]\n access_token_secret = [key]\n')

except IndexError:
    # Didn't input any arguments
    print(f'\n !!! You need to add some arguments!!!')
    help()
