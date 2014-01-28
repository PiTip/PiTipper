import time
import praw
r = praw.Reddit('Pi DogeTipBot by /u/pitipper aka JC300. Source code is available.')
r.login('NOT LETTING YOU GUYS', 'GET MY BELOVED PASSWORD')
already_done = set()
while True:
	subreddit = r.get_subreddit('test')
		# Look for recent submissions in r/dogecoin
subreddit_comments = subreddit.get_comments()
print('Getting comments from subreddit..')
        # Look for comments in r/dogecoin
forest_comments = submission.comments
flat_comments = praw.helpers.flatten_tree(subreddit_comments)
for comment in flat_comments:
	if comment.body == "Tip"and comment.id not in already_done:
		comment.reply('+/u/DogeTipBot 31.415926 doge') 
		already_done.add(comment.id)
		print('Done!')
	else:
		print('Error')
