# 프로그램 설치도구
## sudo : 시스템 내에서 절대적인 권한을 잠시 빌려서 명령어를 실행할 수 있게 해줌
~$ sudo cp new.txt sudonew.txt
~$ ls -al


sudo 키워드를 사용해서 설치하면, 다른 계정에도 영향을 미치게 된다.


# 편집도구 vim
## 버전확인용 명령어    
cat /etc/issue

우분투에는 기본적으로 vi 에디터라는 편집 도구가 설치되어 있음

## 파일생성(또는 열기)
 vi ./test1.txt

## 편집모드 (i입력)
파일의 내용을 편집한다.

## 제어모드 ESC키 
편집이 되지 않은다.. 현재 상태에서 vi편집기를 종료하는 일을 할 수 있다.

: 콜론 누르기  
w를 누르면 파일 저장, q를 누르면 에디터 종료, wq 저장하고 에티터 종료.  

vi편집기를 편하게 사용하려면  
vi ~/.vimrc 파일이 있어야한다.   

제어모드에서  
gg : 맨 처음으로 이동  
10gg : 10번째 줄로 줄이동  
G : 맨 밑으로 이동.  
yy : 커서가 있는 줄이 복사.  
p : 붙여넣기  
dd : 줄 지우기  
10dd : 10번째 줄로 줄삭제  
v : v키를 누르고 커서를 이동하면, 블록에 포함시키고, y을 입력하면 클립보드에 복사된다. 


vi 에디터는 기본적으로 수정사항이 있는데 저장하지 않고 나갈려면, 에러가 발생한다. 만약 강제로 종료하려면 아래와 같은 명령어를 사용한다.  

q! :   저장하지 않고 종료
w! : 읽기 모드로 열렸지만, 억지로 저장. 

## 파일옮기기  
mv ./new.txt ./test/  

## 파일지우기  
rm 파일이름   
rm 파일이름1 파일이름2 파일이름3  

## 디렉토리 지우기
rmdir 디렉토리이름 : 디렉토리가 비어있어야 지울 수 있음  
rm -r 디렉토리이름 : 디렉토리 안에 있는거 까지 통째로 지움

# Shell 프로그래밍
쉘 프로그래밍을 할 때에는, mysample.sh 라는 확장자를 입력한다.(sh)  

---

# 파이썬 가상환경 생성 및 사용
파이썬을 위해 관리자 권한으로 설치하는 것들  
~$ sudo apt update  
~$ sudo apt install python3-dev python3-pip python3-venv  


가상환경 생성 : ~$ python3 -m venv --system-site-packages ~/venv  
가상환경 접속 : ~$ source ~/venv/bin/activate  
가상환경 종료 : deactivate

# 깃 클론하기 
git clone 주소  

ls하면 내가 클론한 내용들을 볼 수 있다... 

# export PYTHONPATH=$PYTHONPATH:/home/내아이디/


# 계정관련 명령어
whoami  
계정추가 : sudo adduser OOOOO  : 홈디렉토리가 자동으로 생성  
sudo useradd OOOOO
비밀번호변경: passwd : 홈디렉토리, 패스워드 등의 설정을 직접해야함. 
로그인한 사용자 확인 : uesrs  


# 파일 위치 찾기 find
(이름)파일찾기 : find ./ -name ‘*.txt’  
(타입,이름)디렉토리 찾기 : find ./ -type d -name ‘*test*’  

# 파일 소유 권한 변경
소유 변경: chown 사용자명:그룹명 ./test.py   

chmod 권한(8진수)   
chmod 220 ./test.py  
220 → 010 010 000 → d rwx rwx rwx → - -w- -w- ---



# 링크 파일
## symbolic 링크 (소프트링크) : 바로가기와 비슷하다
ln -s ./test.py ./soft_link  

## hard 링크 
원본이 변경되면 복제본도 변경됨, 원본이 삭제되어도 복제본이 남아 있음 
 ln ./test.py ./hard_link

 # 프로세스 확인 및 종료시키기
ps -ef  

실행중인 프로세스를 확인할 수 있다.  

파이썬으로 실행한 프로세스 : ps -ef | grep python3  

내가 실행한 프로세스 :  ps -ef | grep 내아이디  

프로세스 강제 종료 :
kill -9 PID  