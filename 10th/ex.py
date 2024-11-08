import numpy as np
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # XGBoost 모델 정의
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

    # 하이퍼파라미터 탐색 공간 세분화
    param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1, 0.2],
        'max_depth': [3, 5, 7, 9],
        'subsample': [0.7, 0.8, 0.9],
        'colsample_bytree': [0.7, 0.8, 0.9],
        'gamma': [0, 0.1, 0.2],
        'min_child_weight': [1, 3, 5],
        'scale_pos_weight': [1, 2]
    }

    # GridSearchCV로 하이퍼파라미터 최적화
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(wdbc.data, wdbc.target)

    # 최적 하이퍼파라미터와 성능 출력
    print(f"\nBest hyperparameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_:.4f}")
