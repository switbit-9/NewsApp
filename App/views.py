
from django.http import response
from django.http.request import HttpHeaders, RawPostDataException
from django.shortcuts import render
from requests.models import ContentDecodingError
from newsapi import NewsApiClient
import requests 
from datetime import datetime
'''request library to fetch data from the URL '''


# Create your views here.
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
pxpage = [20, 40, 60, 80, 100]

def newsfeed(request):

    url = 'https://newsapi.org/v2/top-headlines'
    date =datetime.now()
    mydate = date.strftime("%Y-%m-%dT%H:%M:%S")
    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    p = request.GET.get('p')
    query_params = { 'language': 'en', 'pageSize': 20, 'page': p, 'sortBy': 'publishedAt', 'to': mydate}

    response = requests.get(url ,headers=headers, params=query_params).json()

    #pages = range(int(response['totalResults'] / 20))
    

    title =[]
    url = []
    img = []
    author = []
    desc = []
    url = []
    publishedat = []
    source = []

    for dic in response['articles']:
        url.append(dic['url'])
        img.append(dic['urlToImage'])
        author.append(dic['author'])
        desc.append(dic['description'])
        title.append(dic['title'])
        publishedat.append(dic['publishedAt'])
        source.append(dic['source']['id'])

    mylist = zip(title ,url, img, author, desc, publishedat, source)
  
    context = {
            'mylist' : mylist ,
            'categories' : categories,
            #'pages' : pages
        }
    
    return render(request, 'newsfeed.html', context)


def top(request):

    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    url = 'https://newsapi.org/v2/top-headlines'
    query_params = {'language' : 'en', 'page' : 2,  'sortBy': 'popularity'}

    response = requests.get(url , headers= headers, params=query_params).json()

    results = response['totalResults']
    title=[]
    url = []
    img = []
    author = []
    desc =[]
    url = []
    publishedat = []
    source = []
   

    for dic in response['articles']:
        url.append(dic['url'])
        img.append(dic['urlToImage'])
        author.append(dic['author'])
        desc.append(dic['description'])
        title.append(dic['title'])
        publishedat.append(dic['publishedAt'])
        source.append(dic['source']['id'])
        

    mylist = zip(title ,url, img, author, desc, publishedat, source)
  
    context = {
            'mylist' : mylist,
            'categories': categories
        }
    
    return render(request, 'newsfeed.html', context)


def search(request):

    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    endpoint = 'https://newsapi.org/v2/everything/'

    q =  request.GET.get('q')
    print(q)
    query_params = {'qInTitle' : q, 'language': 'en'}

    response = requests.get(endpoint, headers=headers, params=query_params).json()
    print(type(response))
    print(response)

    title=[]
    url = []
    img = []
    author = []
    desc =[]
    url = []
    publishedat = []

    for dic in response['articles']:
        url.append(dic['url'])
        img.append(dic['urlToImage'])
        author.append(dic['author'])
        desc.append(dic['description'])
        title.append(dic['title'])
        publishedat.append(dic['publishedAt'])

    mylist = zip(title ,url, img, author, desc, publishedat)
  
    context = {
            'mylist' : mylist
        }
    
    return render(request, 'index.html', context)


def sources(request):

    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    endpoint = 'https://newsapi.org/v2/top-headlines/sources'
    query_params = {'language' : 'en'}
    response = requests.get(endpoint, headers=headers, params=query_params).json()

    sources = response['sources']
    print(type(sources))
    
    id = []
    name=[]
    desc = []
    url = []
    cat =[]

    for i in sources:
        id.append(i['id'])
        name.append(i['name'])
        desc.append(i['description'])
        url.append(i['url'])
        cat.append(i['category'])

    mylist = zip(id, name, desc, url, cat)
    print(id)


    return render(request, 'sources.html', context={'mylist': mylist})

def osources(request, id):
    
    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    endpoint = 'https://newsapi.org/v2/everything'
    
    query_params = {'sources': id}
    
    response = requests.get(endpoint, headers=headers, params=query_params).json()
    
    query_params1 = {'language' : 'en'}
    endpoint1 =  'https://newsapi.org/v2/top-headlines/sources'
    response1 = requests.get(endpoint1, headers=headers, params=query_params1).json()   

    source_id = []
    source_name = []
    source_description = []
    source_category = []
    source_url = []

    for dic in response1['sources']:
        if dic['id'] == id:
            print(dic['id'])
            source_id.append(dic['id'])
            source_name.append(dic['name'])
            source_description.append(dic['description'])
            source_category.append(dic['category'])
            source_url.append(dic['url'])  

    
    sourcelist = zip( source_id ,source_name, source_description, source_category, source_url)


    title=[]
    url = []
    img = []
    author = []
    desc =[]
    url = []
    publishedat = []
    cat = []

    for dic in response['articles']:
        url.append(dic['url'])
        img.append(dic['urlToImage'])
        author.append(dic['author'])
        desc.append(dic['description'])
        title.append(dic['title'])
        publishedat.append(dic['publishedAt'])
        #cat.append(dic['category'])

    mylist = zip( title ,url, img, author, desc, publishedat)
    
  
    context = {
            'mylist' : mylist,
            'id' : id,
            'sourcelist' : sourcelist
        }
    
    return render(request, 'sources-page.html', context)


def index(request):

    newsapi = NewsApiClient(api_key ='c87f66fec2b9440cad5cb42f04d02901')
    top = newsapi.get_top_headlines(sources ='techcrunch')
    print(type(top))

    l = top['articles']
    print(type(l))
    desc =[]
    news =[]
    img =[]
    url = []
    author = []
    publishedat = []

  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
        author.append(f['author'])
        publishedat.append(f['publishedAt'])

    mylist = zip(news, desc, img)
    print(type(mylist))
    print(mylist)
  
    return render(request, 'index.html', context ={"mylist":mylist})


def article(request, title):
    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    endpoint = 'https://newsapi.org/v2/everything/'
    print(title)

    query_params = {'qInTitle' : title }
    response = requests.get(endpoint, headers=headers, params=query_params).json()
    print(response)

    first = response['articles']
    article = first[0] 

    return render(request, 'article.html', context={'article' : article})

def fcategory(request, category):
    
    url = 'https://newsapi.org/v2/top-headlines'
    date =datetime.now()
    mydate = date.strftime("%Y-%m-%dT%H:%M:%S")

    headers = { 'X-Api-Key' : 'c87f66fec2b9440cad5cb42f04d02901'}
    print(category)

    query_params = { 'language': 'en', 'pageSize': 20, 'page': 2, 'sortBy': 'publishedAt', 'to': mydate, 'category' : category}

    response = requests.get(url ,headers=headers, params=query_params).json()

    
    title =[ ]
    url = []
    img = []
    author = []
    desc = []
    url = []
    publishedat = []

    for dic in response['articles']:
        url.append(dic['url'])
        img.append(dic['urlToImage'])
        author.append(dic['author'])
        desc.append(dic['description'])
        title.append(dic['title'])
        publishedat.append(dic['publishedAt'])

    mylist = zip(title ,url, img, author, desc, publishedat)
  
    context = {
            'mylist' : mylist ,
            'categories' : categories,
        }
    
    return render(request, 'newsfeed.html', context)
