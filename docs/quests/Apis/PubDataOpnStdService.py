import requests

url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
params = { 'ServiceKey' : 'n8q0vxEC5P2BMwv1kLcYxS7kTyu6EUP6HDeneaUs4TXvp/m6Xfg5ljzg7A/QssE2VA+uOdmlkYItOj7tngykpA==',
          'pageNo':1,
          'numOfRows':10,
          'type':'json',
          'bidNtceBgnDt': '201712010000',
          'bidNtceEndDt' : '201712312359'
          }

response = requests.get(url, params=params)

import json

contents = json.loads(response.content)

from pymongo import MongoClient
def dbconnect(collection_name) :
    # MongoDB 클라이언트 설정
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["data_go_kr"]
    collection = database[collection_name]
    return collection
pass
collection = dbconnect('PubDataOpnStdService')
collection.insert_many(contents['response']['body']['items'])
pass

