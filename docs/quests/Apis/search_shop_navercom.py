# from : https://developers.naver.com/docs/common/openapiguide/apilist.md#%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%B0%A9%EC%8B%9D-%EC%98%A4%ED%94%88-api

import requests # postman app 역할

# request API 요청
url = "https://openapi.naver.com/v1/search/shop"
params = {
    "query" : "인공지능"
}
headers = {
    "X-Naver-Client-Id":"kwdXpKQ167u_KCfNitrJ",
    "X-Naver-Client-Secret":"n84XwGnzIV"
}
response = requests.get(url=url, params=params, headers=headers)

# response API
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)

pass

from pymongo import MongoClient
def dbconnect(collection_name) :
    # MongoDB 클라이언트 설정
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["data_go_kr"]
    collection = database[collection_name]
    return collection

collection_shop_info = dbconnect('shop_info')
shop_info = {
    "lastBuildDate": "Fri, 19 Jan 2024 15:42:18 +0900",
    "total": 180074,
    "start": 1,
    "display": 10,}
collection_shop_info.insert_one(shop_info)
list_shop_info = collection_shop_info.find({})
shop_info_id = list_shop_info[0]['_id']


collection_shop_list = dbconnect('shop_list')
for x in range(len(contents["items"])) : 
    contents["items"][x]["shop_info_id"]=shop_info_id

collection_shop_list.insert_many(contents["items"]) 
pass




