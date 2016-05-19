import markovify
import tweepy

username = 
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret =  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user(username)
num_tweets = 5
status_id = 0
text_list = []
def get_more_tweets(username, status_id):
	x = api.user_timeline(id = username, count = 200, max_id = status_id)
	for status in x:
		text = unicode(status.text).encode('utf8')
		text+='\n'
		text_list.append(text)
		status_id = status.id
	return status_id

x = api.user_timeline(id = username, count = 200)
for status in x:
	text = unicode(status.text).encode('utf8')
	text_list.append(text)
	status_id = status.id
counter = 0
while True:
	new_id = get_more_tweets(username,status_id)
	if (new_id == status_id):
		break
	else:
		status_id = new_id




text_list = ''.join(text_list)
text_model = markovify.Text(text_list)

for i in range(num_tweets):
	status_update = (text_model.make_short_sentence(140))
	if not ('@' in status_update):
		api.update_status(status = status_update)
