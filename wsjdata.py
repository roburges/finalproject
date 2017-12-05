import requests

url = ('https://newsapi.org/v2/everything?'
       'q=AAPL&'
       'from=2017-12-04&'
       'sortBy=popularity&'
       'apiKey=20c32860b43c40dc89c7654bb9140192')

data = requests.get(url)

print (data)
