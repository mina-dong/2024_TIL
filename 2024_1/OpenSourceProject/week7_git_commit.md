# github ssh key management

(1) ssh-keygen -t rsa -b 4096 -C “nnnn@개인메일.com”

(2) ssh-keygen -t ed25519 -C “nnnn@개인메일.com”


동일한github계정으로 2개의 키를 관리하려면, passpharse를 입력해서 key가 달라지게 한다. 예) key1 입력하면, your identification has been saved in /경로/ .ssh/key1 라는 문구가 발생한다. 


클론 받아올때는  

git clone git@git~.com-key1:회사이름/p1.git  

이런식으로 키 생성할때 입력했던 passhpharse를 입력한다.  

# customized git 

branch를 통째로 옮기는  git명령어 = git move


#커밋 개수가 안올라가는 이유, 잘못된 계저응로 repo에 push

원인: Clone 받아서 작업중인 Local repository 에서, git 설정할 때 잘못된 “github 계정정보”를 입력한 것  


계정정보 입력해둔 것 확인  

• ~/project$ git config user.name  

• ~/project$ git config user.email  


local machine 에서의 OS 계정과 github 계정은 서로 다른 것

git config user.name “USERNAME" global 옵션을 적용할 경우 일괄 적용되므로, 신중히 사용해야한다.   



## 해결방법

 commit 들을 rebase, 해시값과 직전 커밋의 해시값 기억하고  

git rebase -i -p 306ff13 이런식으로 입력한다. 

git commit --amend “이름 <이메일주소>”

git rebase --continue  

git push -f origin main


수행후 새로운 해시값이 입력된 것을 확인할 수 있다.   


# 파이썬 unitTest : S/W 가 requirements 에 부합하는지 여부를 검증하는 작업  


Python ‘unittest’ : UnitTest 를 위한 기능을 모아놓은 라이브러리  

• TestCase : Test 기본 단위   

• Fixture  

-Test 수행 전: Test 환경이 적절한 상태인지 확인. 데이터베이스 Table 생성 등  

- Test 수행 후: Test 에 사용한 resource 반납  

• Assertion  

-Test 통과/실패 결정  

-객체 적합성, 예외발생 등의 점검 수  


```

def f():

 print("w")



class CustomTest(unittest.TestCase):

def test_run(self):

f1()



if __name__ == '__main__':

unittest.main()

```


```

def f():

 print("w")


// 클래스 이름은 자유롭게 설정. 

class C(unittest.TestCase):

def test_run1(self):

f1()

def test_run2(self):

f1()

def te(self):

f1()



if __name__ == '__main__':

unittest.main()

```

test로 시작하는 2개의 함수만 테스트 대상. 위 결과를 통해 te()는 실행이 안된것을 확인할 수 있다. 



## unitest.main() 