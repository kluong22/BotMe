import markovify
import tweepy
import botmeconstants
import sys

create_num_tweets = 5
max_tweet_request = 200
max_tweet_length = 140

def tweet_request(username, status_id):
	tweets = api.user_timeline(id = username, count = max_tweet_request,
	 max_id = status_id)
	for tweet in tweets:
		text = unicode(tweet.text).encode('utf8')
		text+='\n'
		.append(text)
		status_id = status.id
	return status_id

def get_tweets(username):
	status_id = 0
	tweet_list = []
	x = api.user_timeline(id = username, count = max_tweet_request)
	for status in x:
		text = unicode(status.text).encode('utf8')
		tweet_list.append(text)
		status_id = status.id

	while (new_id != status_id)
		new_id = tweet_request(username,status_id)
		status_id = new_id
	return tweet_list

def create_tweets(tweet_list):
	tweet_list = ''.join(tweet_list)
	text_model = markovify.Text(tweet_list)

	for i in range(num_tweets):
		status_update = (text_model.make_short_sentence(max_tweet_length))
		if not ('@' in status_update):
			api.update_status(status = status_update)

def main(argv):
	# Authentication
	username = argv[1]
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	user = api.get_user(username)

	tweet_list = get_tweets(username)
	create_tweets(tweet_list)

if __name__ = "__main__":
	main(sys.argv)
