import requests


from nytimesarticle import articleAPI
response=requests.get('https://nytimes.com',auth=('87c4d119d268416dabca815fb87cdbbb'))
print(response.contents)
# CACHE_FNAME = "response.json"
# cache_file=open(CACHE_FNAME,'r')
# cache_contents=cache_file.read()
# CACHE_DICTION=json.loads(cache_contents)
# cache_file.close()



# Put the rest of your caching setup here:
try:
    # cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
#     cache_contents = cache_file.read()  # If it's there, get it into a string
#     CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
#     cache_file.close() # Close the file, we're good, we got the data in a dictionary.
# except:
#     CACHE_DICTION = {}
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
