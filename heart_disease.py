import pandas as pd
import numpy as np  
import joblib
import time
import sys
import os
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
def heart(patient):
    skipped = 0
    ### Загрузка данных, деление на тестовые и обучающие данные ###
    heart_data = pd.read_csv('heart.csv')
    y = heart_data.target
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    for i in range(13):
        if(patient[i]==""):
            patient[i]= np.nan               ####### ПРИВЕДЕНИЕ НЕ ВВЕДЁННЫХ ПОЛЬЗОВАТЕЛЕМ ДАННЫХ К НОРМАЛЬНОМУ ВИДУ
            skipped = skipped + 1
    ########## ОБРАБОТКА ОТСУТСТВУЮЩИХ У ПОЛЬЗОВАТЕЯ АНАЛИЗОВ ##############
    from sklearn.impute import SimpleImputer

    indexNames = heart_data[heart_data['target'] == 1].index
    ######### Далее heart_data будет использована для того, чтобы заполнить пустые параметры пациента средними значениями среди
    ######### ЗДОРОВЫХ испутыемых. Это сделано для того, чтобы дать более реалистичный прогноз - на планете далеко не половина людей
    ######### имеет порок сердца.
    healthy = (heart_data.drop(indexNames)).astype(heart_data.dtypes.to_dict()) ### Теперь healthy содержит данные только здоровых испытуемых

    healthy=healthy[features]
    my_imputer = SimpleImputer(strategy = 'mean')                               ### Заменять отсутствующие данные будем средними значениями 


    healthy =healthy.append(pd.Series(patient, index = healthy.columns), ignore_index=True)         ### Добавим в конец дата фрейма данные о пациенте

    imputed_healthy = pd.DataFrame(my_imputer.fit_transform(healthy), columns = features)           ### Используем imputer

    patient=imputed_healthy.iloc[-1:]                       ### Заменяем patient на обработанную строку из дата фрейма                                               

    ############# ЗАГРУЖАЕМ РАНЕЕ ОБУЧЕННУЮ МОДЕЛЬ (МОДЕЛЬ ОБУЧЕНА С ПОМОЩЬЮ СКРИПТА model_build.py) #############
    loaded_model = joblib.load("heart_model.dat")
    patientsheart = np.int(loaded_model.predict(patient))


    os.system('cls' if os.name == 'nt' else 'clear')

    if(patientsheart==1):
        print("Most likely you have a heart-disease")
        print("you need to undergo a comprehensive examination to determine the cause of your heart disease")
        print("dont worry, its fixable :*")
        input()
    else:
        if(skipped>3):
            print("You have not several results so my prediction is not accurate enough")
            print("If I see missing analysis I replace them by results of heatlhy human")
            print("Just keep this in mind")
        print("Following the results..")
        print("I did not find any reason to be worry +_+")
        print("Have a nice day!")
        input()

    
