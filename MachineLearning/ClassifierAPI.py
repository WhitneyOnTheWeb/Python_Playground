from sklearn.svm import *
from sklearn.multiclass import *
from sklearn.model_selection import *
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import csv
import pandas as pd
import numpy as np

app = Flask(__name__)
global clf
global vec

# Load data 
data = pd.read_csv('data/spam.csv', encoding='latin-1')
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
data.rename(columns={'v1': 'label', 'v2': 'message'}, inplace = True)
data['label'] = data['label'].map({'spam': 1, 'ham': 0})
    
# Split data into training/testing sets
X = data
n_features = X.shape[1]
target = np.array(X['label'])
target_names = np.array(['ham', 'spam'])
labels = target_names[target]
is_spam = (labels == 'spam')
y = target
n_classes = target_names.shape[0]

train_data, test_data, train_label, test_label = \
train_test_split(X, y, test_size=0.25, random_state=77)

tr_target = np.array(train_data['label'])
tr_target_names = np.array(['ham', 'spam'])
tr_labels = tr_target_names[tr_target]

# Train the Model
clf = OneVsRestClassifier(SVC(kernel='linear', probability=True))
vec = TfidfVectorizer()
vector = vec.fit_transform(train_data['message'])
clf.fit(vector, tr_labels)

# Get prediction API
@app.route('/', methods=['GET'])
def index():
    message = request.args.get('message', '')
    error = ''
    prob = ''
    pred = ''
    
    global clf
    global vec
    try:
        if len(message) > 0:
            vec_msg = vec.transform([message])
            pred = clf.predict(vec_msg).tolist()
            prob = clf.predict_proba(vec_msg).tolist()
    except BaseException as inst:
        error = str(type(inst).__name__) + ' ' + str(inst)
    return jsonify(message=message
                , predict_proba=prob
                , predict=pred
                , error=error)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 666))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)