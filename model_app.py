#import necessart libraries

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI()

class Input(BaseModel):
    CONSOLE:object
    YEAR:int
    CATEGORY:object
    PUBLISHER:object
    RATING:object
    CRITICS_POINTS:float
    USER_POINTS:float

class Output(BaseModel):
    SalesInMillions:float

@app.post("/predict")

def predict(data:Input)->Output:
    #input
    X_input = pd.DataFrame([[data.CONSOLE,data.YEAR,data.CATEGORY,data.PUBLISHER,data.RATING,data.CRITICS_POINTS,data.USER_POINTS]])
    X_input.columns = ['CONSOLE','YEAR','CATEGORY','PUBLISHER','RATING','CRITICS_POINTS','USER_POINTS']
    
    # X_input=pd.DataFrame([data.model_dump()])
    
    # X_input = pd.DataFrame([{'CONSOLE':  data.CONSOLE,'YEAR':  data.YEAR,'CATEGORY':  data.CATEGORY,'PUBLISHER':  data.PUBLISHER,'RATING':  data.RATING,'CRITICS_POINTS':  data.CRITICS_POINTS,'USER_POINTS':  data.USER_POINTS}])


    model = joblib.load('vgsales_pipeline_model.pkl')

    #predict using model
    prediction=model.predict(X_input)
    type(prediction)
    print(prediction)

    #output
    return Output(SalesInMillions=prediction)


'''
{
  "CONSOLE": "ds",
  "YEAR": 2008,
  "CATEGORY": "role-playing",
  "PUBLISHER": "Nintendo",
  "RATING": "E",
  "CRITICS_POINTS": 2.833333333,
  "USER_POINTS": 0.303703704
}


 % uvicorn model_app:app --reload

 curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "CONSOLE": "ds",
  "YEAR": 2008,
  "CATEGORY": "role-playing",
  "PUBLISHER": "Nintendo",
  "RATING": "E",
  "CRITICS_POINTS": 2.833333333,
  "USER_POINTS": 0.303703704
}'


'''