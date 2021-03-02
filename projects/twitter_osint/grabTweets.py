# Import tweepy as tw
import tweepy as tw
import sys
from datetime import datetime as dt
from elasticsearch import Elasticsearch

# Initializing objects
twitter_cred = dict()
api = ''
es = ''

def acqData(search, acq):

    index_name = idx + dt.today().strftime('%Y-%m-%d')
    feed = []
    
    print(': :Acquiring Data::')
   
    for tweet in tw.Cursor(api.search, q=search, tweet_mode='extended').items(acq):
        feed.append(tweet._json)

    count = 0
    
    print(': :Transferring to Elasticsearch Search::')
    
    while count < len(feed):
        doc = {
            '@timestamp': dt.now(),
            'created_at': str(feed[count]['created_at']),
            'twitter_id' : int(feed[count]['id']),
            'id_str' : int(feed[count]['id_str']),
            'full_text' : str(feed[count]['full_text']),
            'truncated' : str(feed[count]['truncated']),
            'display_text_range' : str(feed[count]['display_text_range']),
            'entities' : str(feed[count]['entities']), # Already split the dictionary, no longer needed 
            'metadata' : str(feed[count]['metadata']),
            'source' : str(feed[count]['source']),
            'in_reply_to_status_id' : str(feed[count]['in_reply_to_status_id']),
            'in_reply_to_status_id_str' : str(feed[count]['in_reply_to_status_id_str']),
            'in_reply_to_user_id' : str(feed[count]['in_reply_to_user_id']),
            'in_reply_to_user_id_str' : str(feed[count]['in_reply_to_user_id_str']),
            'in_reply_to_screen_name' : str(feed[count]['in_reply_to_screen_name']),
            'user' : str(feed[count]['user']), # Already split the dictionary, no longer needed
            'geo' : str(feed[count]['geo']),
            'coordinates' : str(feed[count]['coordinates']),
            'place' : str(feed[count]['place']),
            'contributors' : str(feed[count]['contributors']),
            #'retweeted_status' : str(feed[count]['retweeted_status']),
            'is_quote_status' : str(feed[count]['is_quote_status']),
            'retweet_count' : str(feed[count]['retweet_count']),
            'favorite_count' : str(feed[count]['favorite_count']),
            'favorited' : str(feed[count]['favorited']),
            'retweeted' : str(feed[count]['retweeted']),
            'lang' : str(feed[count]['lang']),
            'user_id' : str(feed[count]['user']['id']),
            'user_id_str' : str(feed[count]['user']['id_str']),
            'user_name' : str(feed[count]['user']['name']),
            'user_screen_name' : str(feed[count]['user']['screen_name']),
            'user_location' : str(feed[count]['user']['location']),
            'user_description' : str(feed[count]['user']['description']),
            'user_url' : str(feed[count]['user']['url']),
            'user_protected' : str(feed[count]['user']['protected']),
            'user_followers_count' : str(feed[count]['user']['followers_count']),
            'user_friends_count' : str(feed[count]['user']['friends_count']),
            'user_listed_count' : str(feed[count]['user']['listed_count']),
            'user_created_at' : str(feed[count]['user']['created_at']),
            'user_favourites_count' : str(feed[count]['user']['favourites_count']),
            'user_utc_offset' : str(feed[count]['user']['utc_offset']),
            'user_time_zone' : str(feed[count]['user']['time_zone']),
            'user_geo_enabled' : str(feed[count]['user']['geo_enabled']),
            'user_verified' : str(feed[count]['user']['verified']),
            'user_statuses_count' : str(feed[count]['user']['statuses_count']),
            'user_lang' : str(feed[count]['user']['lang']),
            'user_contributors_enabled' : str(feed[count]['user']['contributors_enabled']),
            'user_is_translator' : str(feed[count]['user']['is_translator']),
            'user_is_translation_enabled' : str(feed[count]['user']['is_translation_enabled']),
            'user_profile_background_color' : str(feed[count]['user']['profile_background_color']),
            'user_profile_background_image_url' : str(feed[count]['user']['profile_background_image_url']),
            'user_profile_background_image_url_https' : str(feed[count]['user']['profile_background_image_url_https']),
            'user_profile_background_tile' : str(feed[count]['user']['profile_background_tile']),
            'user_profile_image_url' : str(feed[count]['user']['profile_image_url']),
            'user_profile_image_url_https' : str(feed[count]['user']['profile_image_url_https']),
            #'user_profile_banner_url' : str(feed[count]['user']['profile_banner_url']),
            'user_profile_link_color' : str(feed[count]['user']['profile_link_color']),
            'user_profile_sidebar_border_color' : str(feed[count]['user']['profile_sidebar_border_color']),
            'user_profile_sidebar_fill_color' : str(feed[count]['user']['profile_sidebar_fill_color']),
            'user_profile_text_color' : str(feed[count]['user']['profile_text_color']),
            'user_profile_use_background_image' : str(feed[count]['user']['profile_use_background_image']),
            'user_has_extended_profile' : str(feed[count]['user']['has_extended_profile']),
            'user_default_profile' : str(feed[count]['user']['default_profile']),
            'user_default_profile_image' : str(feed[count]['user']['default_profile_image']),
            'user_following' : str(feed[count]['user']['following']),
            'user_follow_request_sent' : str(feed[count]['user']['follow_request_sent']),
            'user_notifications' : str(feed[count]['user']['notifications']),
            'user_translator_type' : str(feed[count]['user']['translator_type']),
            'entities_hashtags' : str(feed[count]['entities']['hashtags']),
            'entities_symbols' : str(feed[count]['entities']['symbols']),
            'entities_user_mentions' : str(feed[count]['entities']['user_mentions']),
            'entities_urls' : str(feed[count]['entities']['urls']),
            #'entities_media' : str(feed[count]['entities']['media']),
            #'extended_entities_media' : str(feed[count]['extended_entities']['media']),
            'metadata_iso_language_code' : str(feed[count]['metadata']['iso_language_code']),
            'metadata_result_type' : str(feed[count]['metadata']['result_type']),
            #'retweeted_status_created_at' : str(feed[count]['retweeted_status']['created_at']),
            #'retweeted_status_id' : str(feed[count]['retweeted_status']['id']),
            #'retweeted_status_id_str' : str(feed[count]['retweeted_status']['id_str']),
            #'retweeted_status_full_text' : str(feed[count]['retweeted_status']['full_text']),
            #'retweeted_status_truncated' : str(feed[count]['retweeted_status']['truncated']),
            #'retweeted_status_display_text_range' : str(feed[count]['retweeted_status']['display_text_range']),
            #'retweeted_status_source' : str(feed[count]['retweeted_status']['source']),
            #'retweeted_status_in_reply_to_status_id' : str(feed[count]['retweeted_status']['in_reply_to_status_id']),
            #'retweeted_status_in_reply_to_status_id_str' : str(feed[count]['retweeted_status']['in_reply_to_status_id_str']),
            #'retweeted_status_in_reply_to_user_id' : str(feed[count]['retweeted_status']['in_reply_to_user_id']),
            #'retweeted_status_in_reply_to_user_id_str' : str(feed[count]['retweeted_status']['in_reply_to_user_id_str']),
            #'retweeted_status_in_reply_to_screen_name' : str(feed[count]['retweeted_status']['in_reply_to_screen_name']),
            #'retweeted_status_geo' : str(feed[count]['retweeted_status']['geo']),
            #'retweeted_status_coordinates' : str(feed[count]['retweeted_status']['coordinates']),
            #'retweeted_status_place' : str(feed[count]['retweeted_status']['place']),
            #'retweeted_status_contributors' : str(feed[count]['retweeted_status']['contributors']),
            #'retweeted_status_is_quote_status' : str(feed[count]['retweeted_status']['is_quote_status']),
            #'retweeted_status_retweet_count' : str(feed[count]['retweeted_status']['retweet_count']),
            #'retweeted_status_favorite_count' : str(feed[count]['retweeted_status']['favorite_count']),
            #'retweeted_status_favorited' : str(feed[count]['retweeted_status']['favorited']),
            #'retweeted_status_retweeted' : str(feed[count]['retweeted_status']['retweeted']),
            #'retweeted_status_possibly_sensitive' : str(feed[count]['retweeted_status']['possibly_sensitive']),
            #'retweeted_status_lang' : str(feed[count]['retweeted_status']['lang']),
            #'retweeted_status_entities_hashtags' : str(feed[count]['retweeted_status']['entities']['hashtags']),
            #'retweeted_status_entities_symbols' : str(feed[count]['retweeted_status']['entities']['symbols']),
            #'retweeted_status_entities_user_mentions' : str(feed[count]['retweeted_status']['entities']['user_mentions']),
            #'retweeted_status_entities_urls' : str(feed[count]['retweeted_status']['entities']['urls']),
            #'retweeted_status_entities_media' : str(feed[count]['retweeted_status']['entities']['media']),
            #'user_entities_description_urls': str(feed['user']['entities']['description']['urls'])
            'word_list':  str(feed[count]['full_text']).split(' ')
        }

        es.index(index=index_name, body=doc)
        
        count +=1
    
    print(f'Processed {tweet_count} records of {search} to {server}')

# Set credentials 
def setConfig(server):
    # Import keys from a saved file instead of inputting it directly into the script.  
    # Strip whitespaces and split on = as I only want the key values
    key_location = 'twitter.keys'
    apikeys = []

    global api
    global es

    with open(key_location) as keys:
        for i in keys:
            apikeys.append(i.split("=")[1].strip(" ").strip("\n"))
    keys.close()

    # Initialize dictionary
    #twitter_cred = dict()

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
   
def help():
    print('\n#######################################################################################')
    print('# usage: python3 grabTweets.py ["search"] [tweet_count] ["elasticsearch node"]        #')
    print(f'#    python3 grabTweets.py "palantir OR PLTR" 2500 "172.16.100.200" "palantir-index-" #')
    print('#######################################################################################\n')
    
try:
    search = sys.argv[1] 
    tweet_count = sys.argv[2]
    server = sys.argv[3]
    idx = sys.argv[4]

    # Execute search
    setConfig(server)
    acqData(str(search), int(tweet_count))

except FileNotFoundError:
    # API keys not found
    print(f'\n Error: no twitter.keys file found in current directory\n')
    print(f'*** If you have not done so, create a twitter.keys file in the same directory of this script ***\n')
    print(f'Example of twitter.key file:\n')
    print(f'api_key = [key]\n api_secret_key = [key]\n access_token = [key]\n access_token_secret = [key]\n')

except IndexError:
    # No arguments entered
    print(f'\n Error: No arguments given.')
    help()
    response = input('  - Did you want to grab sample data? [Y/n]: ')

    if response.lower() == 'y':

        # Default values selected
        search = 'palantir OR PLTR' 
        tweet_count = 100
        server = '127.0.0.1'
        idx = 'default-'

        # Execute Search
        setConfig(server)
        acqData(str(search), int(tweet_count))
    else:
        pass