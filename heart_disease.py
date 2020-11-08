import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from tensorflow.keras import models 
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from enter_results import person
import time
import sys
import os
######### НЕОБХОДИМАЯ ДЛЯ ПОДГОТОВКИ ДАННЫХ ФУНКЦИЯ ###############
def normalize(sequences, dimension = 65536):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence]=1
    return results
def heart():
    def typing_effect(words):
        for typing in words[0]: 
            time.sleep(0.02) 
            sys.stdout.write(typing)
            sys.stdout.flush()
    ### Загрузка данных, деление на тестовые и обучающие данные ###
    heart_data = pd.read_csv('heart.csv')
    y = heart_data.target
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    ###### ЭТАП ВВОДА ДАННЫХ ПОЛЬЗОВАТЕЛЯ С КЛАВИАТУРЫ ###########
    patient=person()
    for i in range(13):
        if(patient[i]==""):
            patient[i]= np.nan
        else:
            patient[i]=np.int64(patient[i])
    patient = np.array(patient)
    ########## ОБРАБОТКА ОТСУТСТВУЮЩИХ У ПОЛЬЗОВАТЕЯ АНАЛИЗОВ ##############
    from sklearn.impute import SimpleImputer

    indexNames = heart_data[heart_data['target'] == 1].index
    ######### Далее heart_data будет использована для того, чтобы заполнить пустые параметры пациента средними значениями среди
    ######### ЗДОРОВЫХ испутыемых. Это сделано для того, чтобы дать более реалистичный прогноз - на планете далеко не половина людей
    ######### имеет порок сердца.
    healthy = (heart_data.drop(indexNames)).astype(heart_data.dtypes.to_dict())

    healthy=healthy[features]

    my_imputer = SimpleImputer(strategy = 'most_frequent') # Your code here

            

    healthy=np.float64(np.array(healthy))
    healthy = np.vstack((healthy, patient)) ###### На этом этапе данные пациента становятся последней строчкой данных о здоровых
                                                    ###### испытуемых.

    healthy = pd.DataFrame(healthy)
    imputed_healthy = pd.DataFrame(my_imputer.fit_transform(healthy))

    imputed_healthy=np.array(imputed_healthy)
    patient=imputed_healthy[-1]
    patient = np.array(patient)
    print(patient)
    print(type(patient))
    patient=np.int64(patient*10)
    patient=normalize(patient.reshape(1, -1))
    ############# ЗАГРУЖАЕМ РАНЕЕ ОБУЧЕННУЮ МОДЕЛЬ (МОДЕЛЬ ОБУЧЕНА С ПОМОЩЬЮ СКРИПТА model_build.py) #############
    from tensorflow import keras
    model = keras.models.load_model("heart_model")
    patientsheart=model.predict(patient)

    score_disease=float(patientsheart)
    patientsheart=np.int64(np.around(patientsheart, decimals=0))
    patientsheart=int(patientsheart)

    os.system('cls' if os.name == 'nt' else 'clear')
    if((score_disease>=0.45 and score_disease<=0.55 and skipped > 0)):
        print("I'm sorry, but the tests you entered aren't enough to make a prediction")
        print("Try to pass more tests and come back again")
    else:
        if(patientsheart==1):
            print("Most likely you have a heart-disease")
            print("you need to undergo a comprehensive examination to determine the cause of your heart disease")
            print("dont worry, its fixable :*")
        else:
            print("I did not find any reason to be worry")
            print("have a nice day :3")
    print(score_disease)
    
