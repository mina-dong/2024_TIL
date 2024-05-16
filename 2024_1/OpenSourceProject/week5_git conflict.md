# git

# pull request 


# git conflict 
[주의] 팀프로젝트는 fork를 사용하지 않는다.

## 충돌 발생시키기
충돌을 발생시키기 위해, 로컬에서 수정하고, 원격에서도 수정한다. 

git pull origin main  을 하면, CONFLICT 라는 오류가 발생한다. 
해당하는 오류 파일을 들어가보면 아래와 같이 보인다. 

<<<< HEAD
print("adam")

=====
adam
#adam
>>>>>>c34247q9814


라고 나오는데,  ==== 이 전부분은 로컬 저장소 기준이고, 이후 부분은 원격에 있는 내용을 의미한다.

## 충돌 해결하기 
충돌된 파일을 확인해서 수정한다. 


# git fork

포크하고 clone 한다 :  git clone git@github.com:user-name/repo-name.git
브랜치를 생성한다 : git checkout -b feature_3dan
내용을 수정한다 :  vi hello.txt 등
add : git add hello.txt
commit: git commit -m "hello.txt changed"
push: git push origin feature_3dan
merge: git merge feature_3dan

이 경우, 원작자가 허용하면 원본 코드에 합쳐지게 된다. 



