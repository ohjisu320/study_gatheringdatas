# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests  # postman app 역할

# request API 요청
url = 'https://openapi.naver.com/v1/search/shop'

params = {
    'query':'인공지능'
}

headers ={
    'X-Naver-Client-Id' : 'NtLeqJGtcTpNKXOlmtzV',
    'X-Naver-Client-Secret' : '3ndCmeLwzE'
}

response = requests.get(url, params=params, headers=headers)

raw_content = response.content

# json 변환
import json
contents = json.loads(raw_content)

shop_info = [
    {
        'lastBuildDate' : contents['lastBuildDate'],
        'total' : contents['total'],
        'start' : contents['start'],
        'display' : contents['display']
    }
]

# mongodb 저장

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["naver"]
# collection 작업
collection_info = database['serch_shop_info']
collection_item = database['serch_shop_list']

# insert 작업 진행
result_info = collection_info.insert_many(shop_info)

elements_info = collection_info.find_one({},{'_id' : 1})
print(elements_info)
id_relative = elements_info['_id']
print(id_relative)
pass
item_list = contents['items']

for i in range(len(item_list)):
    item_list[i]['id_relative'] = id_relative
    pass






result_item = collection_item.insert_many(item_list)

pass