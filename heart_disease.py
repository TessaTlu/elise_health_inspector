import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from keras import models 
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
def heart():
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
    def normalize(sequences, dimension = 128):
        results = np.zeros((len(sequences), dimension))
        for i, sequence in enumerate(sequences):
            results[i, sequence]=1
        return results
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

    model.fit(x_train, y_train, epochs = 36, batch_size=16)
    print("Hello, my name is Indi")  
    print("I am going give you advices based on your analysis results")
    print("to talk about your health prepare latests analysis +_+")
    print("If you have not some analysis, type -1 instead of result")
    print("Firstly, how old are you?")
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
    print("if your exercise induced angina type 1, or 2 if not")
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
    # Fill in the lines below: imputation
    from sklearn.impute import SimpleImputer

    # Fill in the lines below: imputation
    my_imputer = SimpleImputer(strategy = 'mean') # Your code here
    indexNames = heart_data[heart_data['target'] == 1].index
    heart_data_save=heart_data
    heart_data.drop(indexNames , inplace=True)
    Xt=heart_data
    Xt=Xt[features]
    Xt=np.array(Xt)
    skipped = 0
    patient=np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    for i in range (len(patient)):
        if(patient[i]==-1):
            patient[i]=float("Nan")
            skipped +=1
    Xt = np.vstack((Xt, patient))
    Xt = pd.DataFrame(Xt)
    imputed_Xt = pd.DataFrame(my_imputer.fit_transform(Xt))
    imputed_Xt=np.array(imputed_Xt)
    patient=imputed_Xt[-1]
    patient=normalize(patient.reshape(1, -1))
    patientsheart=model.predict(patient)
    score_disease=float(patientsheart)
    patientsheart=np.int64(np.around(patientsheart, decimals=0))
    patientsheart=int(patientsheart)
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
    
