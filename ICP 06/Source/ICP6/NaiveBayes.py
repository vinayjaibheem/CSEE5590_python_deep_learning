from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

gauss=GaussianNB()
gauss.fit(x_train,y_train).predict(x_test)

print("The Accuarcy for Naive Bayes on training set is: {:.2f}" .format(gauss.score(x_train, y_train)))
print("The Accuarcy for Naive Bayes on test set is: {:.2f}" .format(gauss.score(x_test, y_test)))



svm = SVC(kernel='linear')
svm.fit(x_train, y_train)
print('Accuracy of SVM (linear) classifier on training set: {:.2f}'.format(svm.score(x_train, y_train)))
print('Accuracy of SVM (linear) classifier on test set: {:.2f}'.format(svm.score(x_test, y_test)))

svm1 = SVC()
svm1.fit(x_train, y_train)
print('Accuracy of SVM (RBF) classifier on training set: {:.2f}'.format(svm1.score(x_train, y_train)))
print('Accuracy of SVM (RBF) classifier on test set: {:.2f}'.format(svm1.score(x_test, y_test)))

