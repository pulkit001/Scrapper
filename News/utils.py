import requests
import lxml
from  bs4 import BeautifulSoup


def  getData(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}

    r = requests.get(url , headers=headers)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent , 'lxml')
    Title = soup.find_all('div', class_='title')
    Snap = soup.find_all('div', class_='snaps')
    Date = soup.find_all('div', class_='date')

    DateList = []
    for item in Date:
        Date = item.get_text()
        DateList.append(Date)

    PostContentList = []
    count =0
    for item in Title :
        if(count<10):
            count = count + 1
            PostContent = item.findNext('p')
            PostContent = PostContent.get_text()
            PostContentList.append(PostContent)
    ArticleLinkList=[]
    TitleFinal = []
    count2=0
    for item in Title :
        if(count2<10):
            count2 = count2 +1
            TitleFinal.append(item.get_text())
            ArticleLink = item.find('a')
            ArticleLink = ArticleLink.get('href')
            ArticleLinkList.append(ArticleLink)

    UrlList = []
    for item in Snap :
        img1 = item.find('img' , class_='attachment-thumbnail size-thumbnail wp-post-image')
        img1 = img1.get('src')
        UrlList.append(img1)
    return TitleFinal , PostContentList , UrlList , ArticleLinkList , DateList



def getDetail(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}

    r = requests.get(url , headers=headers)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent , 'lxml')
    Detail =  soup.find('div' , class_="full-details")
    Detail = Detail.find_all('p' , class_='')
    DetailList = []
    for item in Detail :
        data_f = item.get_text()
        DetailList.append(data_f)

    return DetailList
