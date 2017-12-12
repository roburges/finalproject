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
urlparams = {}
urlparams['sources'] = "the-wall-street-journal"
urlparams['q']="Apple"
urlparams['from']='2016-1-1'
urlparams['limit']=100
urlparams['apiKey'] = "20c32860b43c40dc89c7654bb9140192"
url = ('https://newsapi.org/v2/everything?')
def gettingapplearticle(article):
	# CACHE_DICTION={}
	#tweets='@umich' ##gives variable to key word for easy editing later
    if article in CACHE_DICTION: ##LOOP, READ, AND ASSIGN RESULTS VARIABLE FOR CACHE DICTION
        results=CACHE_DICTION[article]
        print('using cached data')##let user know data was in cache
    else:
        print('getting data from the internet')##let user know not in cache/scraping
        results= requests.get(url, params=urlparams)
        CACHE_DICTION[article]=json.loads(results.text)
        intdict=json.dumps(CACHE_DICTION)##write scrape to cache for jso
        f=open(CACHE_FNAME,'w')##open file internet option to cach
        f.write(intdict)
        f.close()

    return(results)
articles=gettingapplearticle('apple')
conn = sqlite3.connect('finalproject.sqlite')
cur = conn.cursor()
#create table within database for Facebook API
cur.execute("DROP TABLE IF EXISTS WSJ_Articles")
cur.execute('''CREATE TABLE WSJ_Articles (title TEXT,  Date_Created DATETIME)'''
#looping through every post and retrieving the post id, created time, message, story
#from created time, finding the weekday and time period
for apple in gettingapplearticle:


    tup=correct_title=apple['title'],apple['publishedAt']
    cur.execute('''INSERT or IGNORE INTO WSJ_Articles(title, Date_Created)''' VALUES (?,?,?,?),tup)
