import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib as plt
from tensorflow.python.keras.utils import np_utils
from tensorflow.keras import Sequential
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.layers import Input, Dense, Dropout, Activation, Flatten
from tensorflow.keras.optimizers import Adam, RMSprop
### Загрузка данных, деление на тестовые и обучающие данные ###
heart_data = pd.read_csv('heart.csv')
y = heart_data.target
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = heart_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=1) ### Делим данные на обучающие и тестовые
train_data=np.int16(np.array(np.around(train_X*10, decimals=0))) ### Готовим наши данные к тому, чтобы они стали последовательностью единиц и нулей
train_labels=np.int16(np.array(train_y))
test_data=np.int16(np.array(np.around(val_X*10, decimals=0)))
test_labels=np.int16(np.array(val_y))
### Функцтя нормализации будет использована для того, чтобы подготовить данные к отправке в input первого слоя нейросети
def normalize(sequences, dimension = 65536 ):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence]=1
    return results

### Сама нормализация
x_train=normalize(train_data)
x_test=normalize(test_data)
y_train=np.asarray(train_labels).astype('float32')
y_test=np.asarray(test_labels).astype('float32')
### Введение модели
model = Sequential()
model.add(layers.Dense(32, activation = 'relu', input_shape = (65536, )))
model.add(layers.Dense(16, activation = 'relu'))
model.add(layers.Dense(1, activation='sigmoid'))


### Компиляция модели
model.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
             metrics=['acc'])
### Этап обучения 
history = model.fit(x_train,
                   y_train,
                   epochs=13,
                   batch_size=16,
                   validation_data=(x_test, y_test))
model.save("heart_model")
