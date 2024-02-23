# from : https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%87%BC%ED%95%91%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B6%84%EC%95%BC%EB%B3%84-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EC%A1%B0%ED%9A%8C

import requests # postman app 역할

# request API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"
data = {
            "startDate": "2023-08-01",
            "endDate": "2023-09-30",
            "timeUnit": "month",
            "category": [
                {"name": "패션의류", "param": [ "50000000"]},
                {"name": "화장품/미용", "param": [ "50000002"]}
            ],
            "device": "pc",
            "gender": "f",
            "ages": [ "20",  "30"]
            }
headers = {'X-Naver-Client-Id':'FgRcI134o3JcUtBEYT8v'
           , 'X-Naver-Client-Secret':"kdq7Y9wHFh"}

response = requests.post(url=url ,json=data, headers=headers)

print(response.content)

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
collection.insert_many(contents['response']['data']['items'])
pass
