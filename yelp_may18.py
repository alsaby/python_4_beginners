import urllib
from bs4 import BeautifulSoup
import re
from threading import Thread

#List of yelp urls to scrape
url=['http://www.yelp.com/biz/liman-fisch-restaurant-hamburg','http://www.yelp.com/biz/casa-franco-caramba-hamburg','http://www.yelp.com/biz/o-ren-ishii-hamburg','http://www.yelp.com/biz/gastwerk-hotel-hamburg-hamburg-2','http://www.yelp.com/biz/superbude-hamburg-2','http://www.yelp.com/biz/hotel-hafen-hamburg-hamburg','http://www.yelp.com/biz/hamburg-marriott-hotel-hamburg','http://www.yelp.com/biz/yoho-hamburg']

i=0
#function that will do actual scraping job
def scrape(ur):

          html = urllib.urlopen(ur).read()
          soup = BeautifulSoup(html)

          title = soup.find('h1',itemprop="name")
          saddress = soup.find('span',itemprop="streetAddress")
          postalcode = soup.find('span',itemprop="postalCode")
          print title.text
          print saddress.text
          print postalcode.text
          print "-------------------"

threadlist = []

#making threads
while i<len(url):
          t = Thread(target=scrape,args=(url[i],))
          t.start()
          threadlist.append(t)
          i=i+1

for b in threadlist:
          b.join()