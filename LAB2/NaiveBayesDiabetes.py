from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.cross_validation import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


diabetesdatasets = pd.read_table('diabetes.txt')
fig = plt.figure(figsize=(8,4))
fig.add_subplot(1,1,1)
ax = sns.countplot(diabetesdatasets['AGE'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['SEX'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['BMI'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['BP'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S1'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S2'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S3'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S4'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S5'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['S6'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()

ax = sns.countplot(diabetesdatasets['Y'],label="Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=6)
plt.tight_layout()
plt.show()


diadatasets=datasets.load_diabetes()
x=diadatasets.data
y=diadatasets.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

gauss=GaussianNB()
gauss.fit(x_train,y_train).predict(x_test)

print("The Accuarcy for Naive Bayes on training set is: {:.2f}" .format(gauss.score(x_train, y_train)))
print("The Accuarcy for Naive Bayes on test set is: {:.2f}" .format(gauss.score(x_test, y_test)))
