import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score

def naiveBayes(x_train,x_test,y_train,y_test):
    classifier = GaussianNB()
    classifier.fit(x_train,y_train)
    y_pred = classifier.predict(x_test)
    matrix = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    print("naive bayes")
    print(matrix)
    print(accuracy)    

def dTree(x_train,x_test,y_train,y_test):
    classifier = DecisionTreeClassifier()
    classifier.fit(x_train,y_train)
    y_pred = classifier.predict(x_test)
    matrix = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    print("Tree")
    print(matrix)
    print(accuracy)    

def logReg(x_train,x_test,y_train,y_test):
    classifier = LogisticRegression(multi_class='multinomial',max_iter=1000)
    classifier.fit(x_train,y_train)
    y_pred = classifier.predict(x_test)
    matrix = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    print("logistic regression")
    print(matrix)
    print(accuracy) 

if __name__ == "__main__":
    sc = StandardScaler()
    wholeFile = pd.read_csv(r'oatTest.csv',low_memory=False)
    wholeFile.head()
    
    y = wholeFile.type
    x = wholeFile.drop('type',axis=1)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    x_train = sc.fit_transform(x_train)
    x_test =  sc.fit_transform(x_test) 
    naiveBayes(x_train,x_test,y_train,y_test)
    dTree(x_train,x_test,y_train,y_test)
    logReg(x_train,x_test,y_train,y_test)
    # print("shape of original dataset :", wholeFile.shape)
    # print("shape of input - training set", x_train.shape)
    # print("shape of output - training set", y_train.shape)
    # print("shape of input - testing set", x_test.shape)
    # print("shape of output - testing set", y_test.shape)