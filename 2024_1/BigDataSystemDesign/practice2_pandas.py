import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "C:/Users/skfo9/Downloads/titanic/titanic.csv"

titanic_df = pd.read_csv(link)
# print(titanic_df)

# titanic_df.info()

# sns.catplot(x="Gender", hue ="Survived", kind ="count", data = titanic_df)
# plt.show()

# print("haed: print out the first 5 rows")
# print(titanic_df.head())
# print("tail: print out the last 5 rows")
# print(titanic_df.tail())

#
# titanic_df.drop(columns='Name', inplace=True)
# titanic_df.info()

# titanic_df.drop(columns=['Cabin', 'Ticket', 'Embarked'], inplace = True)
# print(titanic_df.head(5))

# titanic_df.drop(columns=['Cabin', 'Ticket', 'Embarked', 'PassengerId'], inplace=True)
# titanic_df.drop_duplicates(inplace=True)
# print(titanic_df[titanic_df.duplicated()])
# print(titanic_df.tail(10))



# from sklearn.datasets import fetch_20newsgroups
#
# cats = ['rec.motorcycles', 'rec.sport.baseball', 'comp.graphics',
#         'comp.windows.x', 'talk.politics.mideast', 'sci.space',
#         'sci.electronics', 'sci.med']
#
# news_df = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'),
#                              categories=cats, random_state=15)
# # 랜덤스테이트 : 15 난수.
# print(news_df["data"][0])



# from sklearn.datasets import fetch_20newsgroups
#
# cats = ['rec.motorcycles', 'rec.sport.baseball', 'comp.graphics',
#         'comp.windows.x', 'talk.politics.mideast', 'sci.space',
#         'sci.electronics', 'sci.med']
#
# news_df = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'),
#                              categories=cats, random_state=15)
#
# print(type(news_df))
# print(news_df.keys())
# print(type(news_df.data), type(news_df.target_names), type(news_df.target))
#
# for i, val in zip(np.unique(news_df.target),news_df.target_names):
#     print("index ({}): topic {}".format(i, val))


"""
데이터 나누기.
빅데이터를 분석할 때, 어떻게 분석해야할까?

텍스트 자체를 분석하는 방법은 없다! 단, 텍스트를 숫자 형태로 바꾸는 방법은 있다.
Vectiorizer 

A라는 알파벳이 있다면, 001 이렇게 매핑을 해주는 걸 의미한다. 

가장 중요한 건? 단어의 "빈도수" 
확률분포를 따르는 그 로직을 따르는 식으로 된다.

CountVectorizer 
TF-IDF Vectorizer가 있으며

해당 수업에서는 countVectorizer를 사용한다.  

word_vect = cnt_vect.fit_transform(x_total) 
-> 이렇게 하면 벡터를 만들어 준다.

거기서 특정한 단어들 중에서 나오냐, 안나오냐... 

이 뉴스 자체가 숫자 형태로 표현이 됬으면, 

왜 토픽모델링을 할까?
벡터화된 모델들이 문서를 합니다. 비슷한 용어를 사용하는 문서들 = 유사하다 즉, 그룹을 만들 수 있다. 
그룹에서 가장 빈도가 높은 단어는 무엇일까? -> latenDirichletAllocation(n_componets=개수(꺼낼 단어?개수), radom_state=15)

8개의 카테고리에 1500개의 단어를 가져와서 각각의 토픽별로 어떤 걸로 하는지 산이 되고, 
토픽을 꺼내면, 결과를 확인할 수 있다.  


"""