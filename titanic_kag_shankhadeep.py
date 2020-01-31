#import important modules
import pandas as pd
import numpy as np
#from sklearn.linear_model import LogisticRegression (activate this if using existing logistic regression model)

#define functions
#function to return the sigmoid value
def sigmoid(z):
    s = 1 / (1+np.exp(-z))
    return s

#function for propagation
def propagate(x, y, w, b):
    m = x.shape[0]
    s = sigmoid(np.dot(w.T,x.T)+b)
    cost = (-1./m) * np.sum(y*np.log(s) + (1 - y)*np.log(1-s))
    dw = (1./m) * np.dot(x.T,(s-y).T)
    db = (1./m) * np.sum(s-y)
    return dw, db, cost

#function to run gradient descent
def grad_des (x, y, w, b, iters, rate):
    costs = []

    for i in range(iters):
        dw, db, cost = propagate(x, y, w, b)
        w = w - rate*dw
        b = b - rate*db
        costs.append(cost)

    print(costs[iters-1])
    return w, b

#function to predict the output
def predict(x, w, b):
    m = x.shape[0]
    y_pred = np.zeros(shape=(m,), dtype = int)
    A = sigmoid(np.dot(w.T, x.T) + b)

    for i in range(A.shape[1]):
        if A[0,i] > 0.5:
            y_pred[i] = 1
        else:
            y_pred[i] = 0

    return y_pred

#input section
#read the test and training files
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#pre-processing stage
#replacing the strings in the header 'Sex' with numbers for analysis (in both the test and training sets)
Sex = {'male': 1, 'female': 2}
train.Sex = [Sex[item] for item in train.Sex]
test.Sex = [Sex[item] for item in test.Sex]

#choosing independent variables for analysis
X_variables = ['Pclass','Sex','SibSp','Parch']

#assigning independent variables in both test and training sets
X_train = train[X_variables].values
X_test = test[X_variables].values

#assigning the dependent variable in the training set (the test set will not have this number)
y_train = train.Survived.values

#start calculation
#initalise weights, intercept, times to run and learning rate
w = np.zeros(shape=(X_train.shape[1],1))
b = 0
iters = 20000
rate = 1.15

print(iters, rate)

#running gradint descent and getting the parameters
w, b = grad_des(X_train, y_train, w, b, iters, rate)

#predict output with text figures
y_pred = predict(X_test, w, b)

#running the logistic regression - use this if you need to run the model already available in sklearn
#model1 = LogisticRegression()    #initialise
#model1.fit(X_train, y_train)     #fitting
#y_test = model1.predict(X_test)  #predicting

#output section
#stripping the passenger id into the output file, merging it with the model output and writing output file
pax = test.PassengerId
output = pd.DataFrame({'PassengerId': pax, 'Survived': y_pred})
printoutput = pd.DataFrame(output, columns = ['PassengerId', 'Survived'])
printoutput.to_csv('result_shankhadeep.csv', index = False)
