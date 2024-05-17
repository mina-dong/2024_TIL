# mongoDB
Document 기반의 DBMS으로 noSQL에 속한다.
Document-based
total_ratings, rating_count 를 이용하여, 추후 간단하게 ‘평균 rating’ 계산 가능


# 데이터 수집 방법 & 고려할 사항
1. 웹데이터 크롤러(crawler) 사용 : 여러 웹페이지들을 자동/반자동 방식으로 돌아다니면서 데이터 수집
2. 웹데이터 스크래퍼(scraper) 사용: 원하는 target 데이터 추출

**데이터 수집시 수집해도 되는지 policy 등 확인해 볼것.
** 또는 robots.txt 확인한다( chunk.ac.kr/robots.txt

# 데이터 수집 도구
Beautifulsoup4

# 데이터베이스 접근 도구
pymongo

#Vi 에디터에서 화면 분할 사용
(vi data_collect2.py / 제어 모드에서 :vsplit data_collect.py)
화면 하단의 파일 이름으로 어떤 파일인지 확인 가능
Ctrl+w 누른 후 방향키 왼쪽 or 오른쪽 누르면 해당 분할화면으로 이동
하나의 vi 프로세스 상에서 화면이 분할된 것이므로 yy 등을 통한 복사 + 붙여넣기 가능
