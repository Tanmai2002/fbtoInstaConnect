from sklearn.datasets import load_digits
import  numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
mnist=load_digits()
X,y=mnist['data'],mnist['target']
x_train,x_test=train_test_split(X,test_size=0.2,random_state=42)
y_train,y_test=train_test_split(y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
#model.fit(x_train,y_train)

from sklearn.model_selection import cross_val_score
#is N
n=2
y_train=(y_train==n)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

my_pipeline = Pipeline([

    #     ..... add as many as you want in your pipeline
    ('std_scaler', StandardScaler())
])
x_train_np=my_pipeline.fit_transform(x_train)
model.fit(x_train_np,y_train)
cvs=cross_val_score(model,x_train_np,y_train,scoring='accuracy')
c=0
###############################################################
# from matplotlib import pyplot,_cm
# pyplot.gray()
# z=1
# plt=pyplot.subplot(2,2,1)
# for i,j in  zip(model.predict(my_pipeline.fit_transform(x_test)),y_test==2):
#         #print(i,j)
#         if j:
#             n1 = np.reshape(x_test[c], [8, 8])
#             t=pyplot.subplot(7,7,z)
#             #t.gray()
#             t.imshow(n1)
#             z=z+1
#
#             print(c)
#         c+=1
#
# n1=x_test[5]
#
# pyplot.show()
##############################################################
#print(n1)

#dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])