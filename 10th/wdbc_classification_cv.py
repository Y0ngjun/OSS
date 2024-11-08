import numpy as np
from sklearn import (datasets, tree, model_selection)
from sklearn.ensemble import (RandomForestClassifier, GradientBoostingClassifier)
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Train a model
    model = XGBClassifier( # TODO
        n_estimators=100,  # 트리의 개수
        learning_rate=0.28183,  # 학습률
        max_depth=5,  # 트리의 최대 깊이
        subsample=0.8,  # 훈련 데이터의 샘플 비율
        colsample_bytree=0.83,  # 각 트리에서 사용할 특성의 비율
        objective='binary:logistic',  # 이진 분류 문제
        use_label_encoder=False, 
        eval_metric='logloss') # 18
    
    # low accuracy
    # model = RandomForestClassifier(n_estimators=100) # 16 
    # model = GradientBoostingClassifier() # 16
    # model = SVC(kernel='rbf', gamma='scale') # 11
    # model = LogisticRegression(penalty='l2', solver='liblinear') # 15
    # model = KNeighborsClassifier(n_neighbors=10) # 13
    # model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000) # 13

    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Accuracy @ training data: {acc_train:.3f}')
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')