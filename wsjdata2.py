#newsapi-bloomberg
import requests
import json
import pprint
# r = requests.get(url, params)
# responses = r.text
# results = json.loads(responses)
CACHE_FNAME = "wsjdata.json"
# Put the rest of your caching setup here:
try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}
# Define your function get_user_tweets here:
params = {}
params['sources'] = "the-wall-street-journal"
params['q']="Apple"
params['from']='2016-1-1'
params['limit']=100
params['apiKey'] = "20c32860b43c40dc89c7654bb9140192"
url = ('https://newsapi.org/v2/everything?')
def get_user_tweets(price):
	# CACHE_DICTION={}
	#tweets='@umich' ##gives variable to key word for easy editing later
    if price in CACHE_DICTION: ##LOOP, READ, AND ASSIGN RESULTS VARIABLE FOR CACHE DICTION
        results=CACHE_DICTION[price]
        print('using cached data')##let user know data was in cache
    else:
        print('getting data from the internet')##let user know not in cache/scraping
        results= requests.get(url, params)
        CACHE_DICTION[price]=results
        f=open(CACHE_FNAME,'w')##open file internet option to cache
        f.write(json.dumps(CACHE_DICTION))##write scrape to cache for json
        f.close()##close file
    return(results)
    print(results)
# description = results['articles'][0]['description']
# title = results['articles'][0]['title']
#
# params = {}
# params['sources'] = "newyorktimes"
# params['apiKey'] = "87c4d119d268416dabca815fb87cdbbb"
# base_url = "https://api.nytimes.com/svc/topstories/v2/home.json" #search top_stories

#pprint(description)
