import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

### Загрузка данных, деление на тестовые и обучающие данные ###
heart_data = pd.read_csv('heart.csv')
y = heart_data.target
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = heart_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=1) ### Делим данные на обучающие и тестовые



### Компиляция модели
my_model = XGBClassifier(n_estimators = 1000, learning_rate = 0.05 ) 
my_model.fit(train_X, train_y,
               early_stopping_rounds = 5,
               eval_set = [(val_X, val_y)],
               verbose = False
) 
scores = cross_val_score(my_model, X, y,
                              cv=5,
                              scoring='accuracy')
print(scores*100)
joblib.dump(my_model, "heart_model.dat")
