def person():    
    print("Hello, my name is Indi")
    
    print("I am going give you advices based on your analysis results")
    print("to talk about your health prepare latests analysis +_+")

    print("If you have not some analysis, type -1 instead of result")
  
    print("Firstly, how old are you?")
  
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
    patient=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    return patient