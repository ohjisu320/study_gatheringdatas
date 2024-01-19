# from : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033
import requests

url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

params = {'serviceKey':'n8q0vxEC5P2BMwv1kLcYxS7kTyu6EUP6HDeneaUs4TXvp/m6Xfg5ljzg7A/QssE2VA+uOdmlkYItOj7tngykpA==',
          'pageNo' : 1,
          'numOfRows' :10,
          'dataType' : 'JSON'
    
}

response = requests.get(url, params=params)


print(response.content)

import json
contents = json.loads(response.content)

type(contents)
# <class 'dict'>
contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}
type(contents['body']['items'])
# <class 'list'>

from pymongo import MongoClient
def dbconnect(collection_name) :
    # MongoDB 클라이언트 설정
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["data_go_kr"]
    collection = database[collection_name]
    return collection
pass
collection = dbconnect('rent_loan_rate_info_rate_list')
collection.insert_many(contents['body']['items'])