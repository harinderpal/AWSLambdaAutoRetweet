import json, config
from twython import Twython, TwythonError

def retweet(event, context):

    twitter = Twython(config.APP_KEY, config.APP_SECRET, config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)

    search_results = twitter.search(q='#Quote', result_type='mixed', lang='en')
    message = ""

    for tweet in search_results['statuses']:
        try:
            twitter.retweet(id=tweet['id'])
            message = f"Retweeted \"{tweet['text']}\" by {tweet['user']['name']}"
            twitter.create_friendship(id=tweet['user']['id'])
            break
        except TwythonError:
            pass

    body = {
        "message": message,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

