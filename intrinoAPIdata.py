from intriniorealtime.client import IntrinioRealtimeClient
import pytz
import time
import requests

response=requests.get("https://api.intrinio.com/data_point?identifier=AAPL&item=close_price",auth=('277ca1f8f79245d17fdef292f7765ae8','478d0608c500d84bb7a4914e2c75302a'))

print(response.content)
##Define your function get_user_tweets here:
#
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
