# 깃 GIT


# SSH Key 생성

~$ cd .ssh  

~/.ssh$ ls  

id_rsa id_rsa.pub   

~/.ssh$ rm *  


기존에 생성된 SSH파일은 삭제처리.  



ssh-keygen -t rsa -b 4096 -C "id@gmail.com"  



를 통해 ssh 키 생성.  



# Git clone

cat id_rsa.pub  를 통해 SSH키를 확인하고,   

SSH public key를 복사하고 git허브에서 setting  ssh키를 생성한다.



# 협업 git clone 시 주의점

git init 명령어를 통해 local 존재하는 project 디렉토리를 repository 로 만들고 이를 push 하는 방법도 있으나,   

일단 팀 프로젝트용 repository를 github 에서 만들었으므로, 이를 clone 를 사용한다.  


#git merge

로컬상에서 머지해도 되고, 머지가 되지 않은 상태에서 브랜치에 올린다음에 검토받고 머지할 수도 있다.

보통 후자의 방식이 더 낫다. 



# 브랜치 생성 및 머지하기



## 브랜치 생성

$ git checkout –b feature_1dan   

-b는 브랜치의 약어다.  : 브랜치 생성   



이후 git status를 하면 현제 브랜치가 어딘지 확인할 수 있다(On branch feature_1dan)    



## 작업, commit 추가하기

$ git add (작업한파일들)   

$ git commit –m “1x1 … 1x5”  

## 1) 머지하기 (전자)

git merge feature_2dan

 git push origin master


## 2) 머지 request 이용하기(후자) = MR

깃허브에서 issue 생성 하고   

$ git push origin feature_2dan   

깃허브에서 pull request에서 new pull request한다.(내용확인하고 create pull request)  

다른 사용자가 승인처리.  

