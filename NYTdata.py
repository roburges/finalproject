import requests


from nytimesarticle import articleAPI
api=articleAPI('87c4d119d268416dabca815fb87cdbbb')

articleS=api.search(q='AAPL', fq={'source':['Reuters','AP','The New York Times']},begin_date=20160101)
fix=articleS + urllib.parse.urlencode({'address'})
CACHE_FNAME = "NYT.json"
# Put the rest of your caching setup here:
try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}
# Define your function get_user_tweets here:

# def get_user_tweets(tweets):
# 	# CACHE_DICTION={}
# 	#tweets='@umich' ##gives variable to key word for easy editing later
#     if tweets in CACHE_DICTION: ##LOOP, READ, AND ASSIGN RESULTS VARIABLE FOR CACHE DICTION
#         twitter_results=CACHE_DICTION[tweets]
#         print('using cached data')##let user know data was in cache
#     else:
#         print('getting data from the internet')##let user know not in cache/scraping
#         twitter_results=api.user_timeline(tweets)##if tweet not in cache already scrape twitter
#         CACHE_DICTION[tweets]=twitter_results
#         f=open(CACHE_FNAME,'w')##open file internet option to cache
#         f.write(json.dumps(CACHE_DICTION))##write scrape to cache for json
#         f.close()##close file
#         print(type(twitter_results))##for my sanity
#     return(twitter_results)
# print(articleS)
