from django.shortcuts import render
from .utils import getDetail,getData
from django.utils.text import slugify

class DataF:
    def __init__(self, Title1 , Content1  , Url , link , date ,idd):
        self.title = Title1
        self.content = Content1
        self.url = Url
        self.link = link
        self.date = date
        self.id = idd

url1 = 'https://indianexpress.com/latest-news/'
PostTitle , PostContent , UrlList , ArticleLinkList , DateList = getData(url1)
finalList = []
for item in range(len(PostTitle)):
    content = DataF(PostTitle[item] , PostContent[item] , UrlList[item] , ArticleLinkList[item] , DateList[item] , item)
    finalList.append(content)

def index(request):
    context = { 'final' : finalList}
    return render(request , "News/index.html" , context  )

def detail(request , prime):
    for item in finalList:
        if prime == item.id:
            break
    context = { 'Data' : getDetail(item.link) , "Title" : item.title , "Content" : item.content}
    return render(request , "News/detail.html"  ,context )
