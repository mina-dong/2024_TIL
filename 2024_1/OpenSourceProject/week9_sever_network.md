# 서버, 클라이언트
- 서버(Server): 서비스를 제공하는 물리/논리적인 컴퓨터
- 클라이언트(Client): 서버에게 서비스를 요청 및 제공받는 컴퓨터

# 네트워크 기본
DNS(Domain Name System): 숫자 대신 기호를 주소로 사용하는 방식의 시스템
DNS 서버: 기호 주소  숫자 주소로 변환해주는 서버 (혹은, 반대로 변환)
URL(Uniform Resource Locator): 인터넷 상의 자원 위치를 나타내는 방식(포맷)

# RESTful O-DBS : RESTful 하게 동작하는 O-DBS
- REST (Representational State Transfer) :HTTP 기반으로 Web 상에서 리소스를 쉽게 주고받을 수 있게 한다. (Web 상의 Resource 에게 URI를 부여하고, 이를 이용해 접근)
=> Resource 중심으로 설계된 방식

- 리소스에 대하여 CRUD operation 제공
-HTTP method (get, post, put, delete)를 통해 제공
-데이터 주고받을 때는 주로 JSON, XML 형태로 이루어짐


#Logger
사용 이유 1: 프로젝트 문제 해결에 도움, Debugging 해야 함, 문제의 ‘원인’을 찾아내고, ‘해결방법‘을 결정 후 적용
사용 이유 2:Data 를 다루는 사람으로서,프로그램 동작도 ‘data로 기록‘