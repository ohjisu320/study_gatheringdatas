# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests
import xml.etree.ElementTree as ET
from pymongo import MongoClient
import urllib.parse

# API 호출
def get_hosp_info(numOfRows, page_num):
    url = 'http://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList?'
    raw_service_key = 'y5zk2Il3wqLeADyw4OnaRsn0CBXC7/FzuIGDg+V0pxfV8/4zQeYhESnXSRJ56xFG1HiQqU2MlxHIKpN1K7hDzA=='
    encoded_service_key = urllib.parse.quote(raw_service_key)
    params = {
        'numOfRows' : numOfRows,
        'page_num' : page_num,
        'serviceKey': raw_service_key}
    response = requests.get(url, params=params)
    print(response.content)
    root = ET.fromstring(response.content)
    for item in root.findall('./body/items/'):
        # 예시: 'name' 태그와 'price' 태그의 텍스트를 가져옵니다.
        addr = item.find('addr').text
        clCd = item.find('clCd').text
        clCdNm = item.find('clCdNm').text
        estbDd = item.find('estbDd').text
        try  :
            hospUrl = item.find('hospUrl').text
        except :
            hospUrl = ''
        yadmNm = item.find('yadmNm').text
        ykiho = item.find('ykiho').text
        collection.insert_one({'addr': addr
                                , 'clCd':clCd
                                , 'clCdNm': clCdNm
                                , 'estbDd': estbDd
                                , 'hospUrl': hospUrl
                                ,  'yadmNm': yadmNm
                                ,  'ykiho': ykiho})

from pymongo import MongoClient
def dbconnect(collection_name) :
    # MongoDB 클라이언트 설정 mongodb://localhost:27017
    mongoClient = MongoClient("mongodb://192.168.10.236:27017")
    database = mongoClient["teamkim"]
    collection = database[collection_name]
    return collection

totalcount = 77316
page_num = 1
numOfRows = 10000

collection = dbconnect('info_institution_hospital_info')
while True :
    page_num = page_num+1
    try : 
        get_hosp_info(numOfRows, page_num)
    except :
        break
# type(contents)
# # <class 'dict'>
# contents['header']
# # {'resultCode': '00', 'resultMsg': '정상'}
# type(contents['body']['items'])
# # <class 'list'>



