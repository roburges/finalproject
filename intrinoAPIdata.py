from intriniorealtime.client import IntrinioRealtimeClient
import pytz
import time
import requests
import json

url=("https://api.intrinio.com/data_point?identifier=AAPL&item=close_price",auth=('277ca1f8f79245d17fdef292f7765ae8','478d0608c500d84bb7a4914e2c75302a'))
# responsedate=requests.get("https://api.intrinio.com/data_point?identifier=AAPL&item=price_date",auth=('277ca1f8f79245d17fdef292f7765ae8','478d0608c500d84bb7a4914e2c75302a'))
CACHE_FNAME = "intrinio.json"
# Put the rest of your caching setup here:
try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}
def getting_apple_article(price):
	CACHE_DICTION={}
	#tweets='@umich' ##gives variable to key word for easy editing later
    if price in CACHE_DICTION: ##LOOP, READ, AND ASSIGN RESULTS VARIABLE FOR CACHE DICTION
        results=CACHE_DICTION[price]
        print('using cached data')##let user know data was in cache
    else:
        print('getting data from the internet')##let user know not in cache/scraping
        results= requests.get(url)
        CACHE_DICTION[price]=json.loads(results.text)
        f=open(CACHE_FNAME,'w')##open file internet option to cach
        f.write(json.dumps(CACHE_DICTION))##write scrape to cache for jso
        f.close()
    return(results)
#     print(type(results))
# json_article=getting_apple_article('')
#
# conn = sqlite3.connect('finalproject.sqlite')
# cur = conn.cursor()
# #create table within database for Facebook API
# cur.execute("DROP TABLE IF EXISTS Intrinio_price_data")
# cur.execute('''CREATE TABLE Intrinio_price_data (day_price FLOAT,  price_date DATETIME)''')
# #looping through every post and retrieving the post id, created time, message, story
# #from created time, finding the weekday and time period
# for articles in json_article:
#     mentions_lst=['apple']
# print(mentions_lst)
#     for mentions in articles:
#
#     app_title=articles['source']['title']
#     date_created=sourc['source']['publishedAt']
#     cur.execute('INSERT OR IGNORE INTO WSJ_Articles (apple_mention,date_created) VALUES (?,?)',tup)
# conn.commit()
# cur.close()
#
#
