# 0. Pycharm community version 설치

- 이전에 mondgodb 최신판 설치 및 compass도 같이 설치

# 1. Anaconda 설치
 ## 시스템환경변수 설정하기
 - [시스템속성]-[고급]-환경변수 클릭  
 - PATH 더블클릭
 - 아래와 같이 추가하기
   - c\users\(username)\anaconda3
   - c\users\(username)\anaconda3\Library
   - c\users\(username)\anaconda3\Scripts

# 2. Anaconda prompt
기본적으로 base 환경에 속해있다. 

- conda--name practice python=3.12 // practice는환경이름
- conda env list
- conda deactivate
- conda activate practice
- python--version

# 3. PyCharm 
- Projects– New Project
costom env? 클릭해서 conda로 변경처리.
만든 환경으로 연결함.

## terminal 이용하기
- python--version
- pip list
- python-m pip install--upgrade pip
- pip install pymongo

프로젝트내 폴더에서  
File– New– Python File  
Practice1.py 생성.  

```
import pymongo

def main():
    client = pymongo.MongoClient()
    print(client)

    for db in client.list_databases():
        print(db)

    db_conn = client.get_database("practice")
    print(db_conn)

    for col in db_conn.list_collection_names():
        print(col)

    collection = db_conn.get_collection("students")
    print(collection)

    results = collection.find()
    ds = list(results)
    print("Number of data:{}".format(len(ds)))

    for data in ds:
        print(data)

main()
```

compass 를이용해서 practice라는 데이터베이스 생성.  
데이터셋 import  
