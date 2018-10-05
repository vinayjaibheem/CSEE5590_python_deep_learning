# Required Imports
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plot
from sklearn import metrics
from sklearn.model_selection import train_test_split
#Scikit-learn has a very straightforward set of data on these iris species. The data consist of the following:
'''
Features in the Iris dataset:
sepal length (cm) sepal width (cm) petal length (cm) petal width (cm)
Target classes to predict:
Setosa Versicolour Virginica
scikit-learn embeds a copy of the iris CSV file along with a function to load it into numpy arrays:'''
# Loading Iris datasets
iris = datasets.load_iris()
#The features of each sample flower are stored in the data attribute of the dataset:
print(iris.data.shape)
n_samples,n_features = iris.data.shape

print(n_samples)
print(n_features)
print(iris.data[0])
#The information about the class of each sample is stored in the target attribute of the dataset:
print(iris.target.shape)
print(iris.target)
#he names of the classes are stored in the last attribute, namely target_names:
print(iris.target_names)

# Fitting Naive Bayes model to the data
model = GaussianNB()
model.fit(iris.data, iris.target)
print(model)

# Making Prediction based on X, Y
expected = iris.target
predicted = model.predict(iris.data)
print(expected,":", predicted)
# Matlib Plot
plot.plot(expected, predicted)
plot.show()

# Cross Validation

print(metrics.classification_report(expected, predicted))
# confusion_matrix - To evaluate Accuracy of classification
print(metrics.confusion_matrix(expected, predicted))

# splitting data and target into training and testing sets
"""http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html"""
"""https://www.scipy-lectures.org/packages/scikit-learn/index.html"""
# If int, random_state is the seed used by the random number generator
# If float, test_size represent the proportion of the dataset to include in the test split [Default: 0.25]
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=1)

# Training the Model on Training Set
model.fit(X_train, Y_train)

# Training the Model on Testing Set
Y_predicted = model.predict(X_test)

# Evaluating the Model based on Testing Part
print("Gaussian Model Accuracy is ", metrics.accuracy_score(Y_test, Y_predicted) * 100)