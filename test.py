from bs4 import BeautifulSoup
import requests
import datetime
import json

info_url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20140301&endde=20210715&pageNo=1&numOfRows=50&ServiceKey=h1cEt88bY%2Bhl2Wqt%2BnupKk%2BeT%2B8gfanHWmZ4LQvvQ1lSewcYkBcRcGQYWPHZvMtGQCFPfI81gdgE8eP%2BuvL4TQ%3D%3D'
response = requests.get(info_url)
soup = BeautifulSoup(response.content, 'lxml')
print(soup)
data_f = []
datas = soup.find_all('item')
# for data in datas:
    # print("{상태 : ", data.find('processstate').text, "}")
    # o = data.find('happenPlace')
    # p = data.find('processstate').text
    # n = data.find('noticeEdt').text
    # print(p)
    

    # data_f.append({"자치구" : o}, {"공고종료일" : n}, {"상태" : p})

    '''
    Trip_Info.append({'img_url':img_url, 'trip_name':trip_name, 'trip_page':trip_page})

    '''
    
# print(data_f)