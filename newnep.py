#web_scrapper used to scrape data in CSV's from companies website.
import csv
import requests
from bs4 import BeautifulSoup
f=open('aa.csv','w',newline='')
writer=csv.writer(f)
url=requests.get('http://www.nepalstock.com/main/stockwiseprices/index/3/?startDate=2014-01-01&endDate=2019-09-07&stock-symbol=131&_limit=1315').text
soup=BeautifulSoup(url,'html.parser')
mtable=soup.find('table',{'class':'table'})
tdata=mtable.find_all('tr')[1:-1]
#print(tdata)
for row in tdata:
    cols=row.findChildren(recursive=False)
    cols=[ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)
