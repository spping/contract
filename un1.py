import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from FutureContract import FutureContract


#
engine = create_engine('postgresql://postgres:yisheng@192.168.23.180:5432/postgres', echo=True)

DBSession = sessionmaker(bind=engine)

url_prefix = 'http://www.shfe.com.cn/'
products = {}

if __name__ == '__main__':
    r = requests.get('http://www.shfe.com.cn/products/cu/')
    soup = BeautifulSoup(r.text, 'html.parser')
    uls = soup.find(class_ = 'came box fl').find_all('ul')
    for ul in uls:
        lis = ul.find_all('li')
        for li in lis:
            products[li.a.text] = url_prefix + li.a['href']
    for product in products:
        tem = BeautifulSoup(requests.get(products[product]).text, 'html.parser').find(class_ = 'kk1')
        if tem:
            table_href = url_prefix + tem['href']
        table = BeautifulSoup(requests.get(table_href).text, 'html.parser').find('table')
        contract = {}
        for tr in table.find_all('tr'):
            
            tds = tr.find_all('td')
            if tds[0].text.strip() == '交易品种' and tds[1].text.strip() == None:
                continue
            contract[tds[0].text.strip()] = tds[1].text.strip()
        fc = FutureContract(**contract)
        session = DBSession()
        session.add(fc)
        session.commit()
        session.close()
