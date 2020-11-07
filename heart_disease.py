import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from tensorflow.keras import models 
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
import time
import sys
import os
######### НЕОБХОДИМАЯ ДЛЯ ПОДГОТОВКИ ДАННЫХ ФУНКЦИЯ ###############
def normalize(sequences, dimension = 128):
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
    def breathe():
        print("\n")
        time.sleep(0.5)
    ### Загрузка данных, деление на тестовые и обучающие данные ###
    heart_data = pd.read_csv('heart.csv')
    y = heart_data.target
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    X = heart_data[features]
    os.system('cls' if os.name == 'nt' else 'clear')
    message = ["Hello, my name is Indi"] 
    typing_effect(message)
    breathe()
    message = ["I am going give you advices based on your analysis results"]
    typing_effect(message)
    breathe()
    message = ["to talk about your health prepare latests analysis +_+"]
    typing_effect(message)
    breathe()
    message = ["If you have not some analysis, type -1 instead of result"]
    typing_effect(message)
    breathe()
    message = ["Firstly, how old are you?"]
    typing_effect(message)
    breathe()
    ###### ЭТАП ВВОДА ДАННЫХ ПОЛЬЗОВАТЕЛЯ С КЛАВИАТУРЫ ###########
    age=input()
    print("Are you female(0) or male(1)?")
    sex=input()
    print("Which chest pain type you have?")
    print("this is a value between 0 and 3:")
    cp=input()
    print("I need to know your resting blood pressure in mm Hg, type it please:")
    trestbps=input()
    print("Do you love fried patato? :D")
    print("dont answer, just type your serum cholestoral in mg/dl and I will know")
    chol=input()
    print("I hope dont have any problem with sweets +_+")
    print("look at your fasting blood sugar")
    print("if sugar > 120 mg/dl type 1 or 0 if not")
    fbs = input()
    print("I need data about a resting electrocardiographic results")
    print("value should be between 0 and 2:")
    restecg=input()
    print("Heart beat determines whether you're alive or not")
    print("What is a largest value of your heart BPM?")
    thalach=input()
    print("Did you work too hard on your last run?")
    print("if your exercise induced angina type 1, or 0 if not")
    exang=input()
    print("We need to know if you have myocardial ischemia")
    print("to do this, enter the value of the degree of ST depression induced by exercise relative to rest")
    oldpeak=input()
    print("I need to know the slope of the peak exercise ST segment too")
    slope=input()
    print("What is number of your major vessels (0-3) colored by flourosopy?")
    ca=input()
    print("Had you heart defects before?") 
    print("Type 1 if not, 2 if your defect was fixed or 3 if you have reversable one") 
    thal=input()
    
    ########## ОБРАБОТКА ОТСУТСТВУЮЩИХ У ПОЛЬЗОВАТЕЯ АНАЛИЗОВ ##############
    from sklearn.impute import SimpleImputer

    my_imputer = SimpleImputer(strategy = 'mean') 
    indexNames = heart_data[heart_data['target'] == 1].index
    heart_data_save=heart_data
    heart_data.drop(indexNames , inplace=True) ######### ИЗБАВЛЯЕМСЯ В МАССИВЕ ДАННЫХ ОТ ПАЦИЕНТОВ, ИМЕЮЩИХ ПОРОК СЕРДЦА
    healthy=heart_data
    healthy=healthy[features]
    healthy=np.array(healthy)
    skipped = 0
    patient=np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    for i in range (len(patient)):
        if(patient[i]==-1):
            patient[i]=float("Nan")
            skipped +=1
    healthy = np.vstack((healthy, patient))
    healthy = pd.DataFrame(healthy)
    imputed_healthy = pd.DataFrame(my_imputer.fit_transform(healthy))
    imputed_healthy=np.array(imputed_healthy)
    patient=imputed_healthy[-1]
    patient=np.int8(patient)
    patient=normalize(patient.reshape(1, -1))
    ############# ЗАГРУЖАЕМ РАНЕЕ ОБУЧЕННУЮ МОДЕЛЬ (МОДЕЛЬ ОБУЧЕНА С ПОМОЩЬЮ СКРИПТА model_build.py) #############
    from tensorflow import keras
    model = keras.models.load_model("final_model")
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
    
