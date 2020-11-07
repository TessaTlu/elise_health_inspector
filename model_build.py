import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from keras import models 
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics
def normalize(sequences, dimension = 128):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence]=1
    return results
def heart_fit():
    ### Загрузка данных, деление на тестовые и обучающие данные ###
    heart_data = pd.read_csv('heart.csv')
    y = heart_data.target
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    X = heart_data[features]
    train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=1)
    train_data=np.int8(np.array(train_X))
    train_labels=np.int8(np.array(train_y))
    test_data=np.int8(np.array(val_X))
    test_labels=np.int8(np.array(val_y))
    train_data = train_data.tolist()
    test_data = test_data.tolist()
    x_train=normalize(train_data)
    x_test=normalize(test_data)
    y_train=np.asarray(train_labels).astype('float32')
    y_test=np.asarray(test_labels).astype('float32')

    model = models.Sequential()
    model = models.Sequential()
    model.add(layers.Dense(16, activation = 'relu', input_shape = (128, )))
    model.add(layers.Dense(16, activation = 'relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop',
                loss='binary_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs = 20, batch_size=16)
    model.save("final_model")
heart_fit()