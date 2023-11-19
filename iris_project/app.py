from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')

def fun():
    
    return "Testing API"

@app.route('/predict')

def iris_pred():
    
 
    
 with open("D:\iris project\iris_project\logistic_clf.pkl", "rb") as f:
    model=pickle.load(f) 
        
    SepalLengthCm=2.9 
    SepalWidthCm=4.5 
    PetalLengthCm=3.5 
    PetalWidthCm=1  
    
    result= model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])  
    print("result is :", result) 

    return list(result)
 
@app.route('/welcome')

def index1():
    
    return "welcome flask"


if __name__=="__main__":


 app.run(debug=True)
 
 