import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import numpy as np
def heart():
    heart_data = pd.read_csv('heart.csv')
    y = heart_data.target
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    X = heart_data[features]
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    heart_model = RandomForestRegressor(random_state=1, min_samples_leaf = 6)
    heart_model.fit(train_X, train_y)
    predictions = heart_model.predict(val_X)
    predictions = np.int64(np.around(predictions, decimals = 0))
    val_mae = accuracy_score(predictions, val_y)
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
    my_imputer = SimpleImputer(strategy = 'mean') # Your code here
    Xt=np.array(X)
    patient=np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    for i in range (len(patient)):
        if(patient[i]==-1):
            patient[i]=float("Nan")
    Xt = np.vstack((Xt, patient))
    Xt = pd.DataFrame(Xt)
    imputed_Xt = pd.DataFrame(my_imputer.fit_transform(Xt))
    imputed_Xt=np.array(imputed_Xt)
    patient=imputed_Xt[-1]
    patient=patient.reshape(1, -1)
    patientsheart=heart_model.predict(patient)
    patientsheart=np.int64(np.around(patientsheart, decimals=0))
    patientsheart=int(patientsheart)
    if(patientsheart==1):
        print("Most likely you have a heart-disease")
        print("you need to undergo a comprehensive examination to determine the cause of your heart disease")
        print("dont worry, its fixable :*")
    else:
        print("I did not find any reason to be worry")
        print("have a nice day :3")
    
