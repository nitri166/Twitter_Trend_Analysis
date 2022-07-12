import tweepy
from twitter_client import get_twitter_auth
import sys
# Create Streamlistener
# on data 

#on error
class MaxListener(tweepy.StreamListener):

    def __init__(self, fname):
        self.outfile = "corona18july%s.jsonl" % fname


	
    def on_data(self, data):
        self.process_data(data)

        return True

        print(data) 
    def process_data(self, data):
        with open(self.outfile, "a") as f:
            f.write(data)       

    def on_error(self, status):
        if status  == 420:
            sys.stderr.write("Rate limit exceeded\n")
            return False  
        else:
            sys.stderr.write("Error {}\n".format(status))
            return True
            sys.stderr.write("Error {}\n".format(status))
            return True

# Creat a stream

class MaxStream():
	def __init__(self,auth, listener):
		self.stream = tweepy.Stream(auth = auth, listener = listener)

	def start(self, keyword_list):
	    self.stream.filter(track=keyword_list)

#Start the stream
if __name__ == "__main__":
    query = sys.argv[1:] # list of CLI arguments
    query_fname = ' '.join(query)
    listener = MaxListener(query_fname)
    auth = get_twitter_auth()
    stream = MaxStream(auth, listener)
    stream.start(['Corona', 'Covid19', 'CoronaVirus'])
