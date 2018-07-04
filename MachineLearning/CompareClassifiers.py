# Scikit-Learn modules~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.naive_bayes import *
from sklearn.dummy import *
from sklearn.ensemble import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.svm import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.calibration import *
from sklearn.linear_model import *
from sklearn.multiclass import *
from sklearn.model_selection import *
from sklearn.svm import *

# Other Modules
import pandas as pd

# Performance comparison between available classifiers~~~~~~~~~~~~~~~~~~~~~~~~~
def performance(classifiers, vectorizers, train_data, test_data):
    scores = pd.DataFrame(columns=['classifier', 'vectorizer', 'score'])
    for clf in classifiers:
        for vec in vectorizers:
            # Train Models
            vectorize = vec.fit_transform(train_data)
            clf.fit(vectorize, train_data)
            
            # Score Models
            vectorize = vec.transform(test_data)
            score = clf.score(vectorize, test_data)
            scores.loc[len(scores)] = \
                ([clf.__class__.__name__, vec.__class__.__name__, score])
            print(scores.loc[len(scores)-1])
            print()
    return scores


data = pd.read_csv('data/spam.csv', encoding='latin-1')
print('Data Loaded...')
print('Preprocessing data...')

data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
data.rename(columns={'v1': 'label', 'v2': 'message'}, inplace = True)
data['label'] = data['label'].map({'spam': 1, 'ham': 0})
print(data.head())

print('Splitting data...')
X = data
n_features = X.shape[1]

target = np.array(X['label'])
target_names = np.array(['ham', 'spam'])
labels = target_names[target]
is_spam = (labels == 'spam')

y = target
n_classes = target_names.shape[0]

X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.33, random_state=42)
print('Training Set: ', len(X_train))
print('Testing Set: ', len(X_test))

print('Measuring Model Performances...')
performance(
    [
        BernoulliNB(),
        RandomForestClassifier(n_estimators=100, n_jobs=-1),
        AdaBoostClassifier(),
        BaggingClassifier(),
        ExtraTreesClassifier(),
        GradientBoostingClassifier(),
        DecisionTreeClassifier(),
        CalibratedClassifierCV(),
        DummyClassifier(),
        PassiveAggressiveClassifier(),
        RidgeClassifier(),
        RidgeClassifierCV(),
        SGDClassifier(),
        SVC(kernel = 'rbf', C = 10000),
        OneVsRestClassifier(SVC(kernel='linear')),
        OneVsRestClassifier(LogisticRegression()),
        KNeighborsClassifier()
    ],
    [
        CountVectorizer(),
        TfidfVectorizer(),
        #HashingVectorizer()
    ],
    X_train['message'],
    X_test['message']
)