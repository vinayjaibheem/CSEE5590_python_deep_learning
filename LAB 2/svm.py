from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

diabetes_datasets = datasets.load_diabetes()
x = diabetes_datasets.data
y = diabetes_datasets.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

svm = SVC(kernel='poly', degree=4, C=1.0, gamma=0.2)
svm.fit(x_train, y_train)
print('Accuracy of SVM (poly kernel with degree 4) classifier on training set: {:.2f}'.format(svm.score(x_train, y_train)))
print('Accuracy of SVM (poly kernel with degree 4) classifier on test set: {:.2f}'.format(svm.score(x_test, y_test)))


svm = SVC(kernel='rbf', C=1.0, gamma=0.2)
svm.fit(x_train, y_train)
print('Accuracy of SVM (rbf kernel) classifier on training set: {:.2f}'.format(svm.score(x_train, y_train)))
print('Accuracy of SVM (rbf kernel) classifier on test set: {:.2f}'.format(svm.score(x_test, y_test)))