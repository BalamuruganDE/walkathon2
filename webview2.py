import streamlit as st
import pandas as pd
import joblib as jlb
import json
import requests

st.title('Prediction App')

st.write("This is a test")

df = pd.read_csv('data.csv')

min_year = df['YEAR'].min()
max_year = df['YEAR'].max()


# CONSOLE = st.text_input('CONSOLE') 
CONSOLE = st.selectbox('CONSOLE',pd.unique(df['CONSOLE']))
# YEAR = st.number_input('YEAR',step=1,min_value=min_year,max_value=max_year,value=min_year)
YEAR = st.number_input('YEAR',step=1,min_value=df['YEAR'].min(),max_value=df['YEAR'].max(),value=df['YEAR'].min())
CATEGORY = st.selectbox('CATEGORY',pd.unique(df['CATEGORY']))
PUBLISHER = st.selectbox('PUBLISHER',pd.unique(df['PUBLISHER']))
RATING = st.selectbox('RATING',pd.unique(df['RATING']))
CRITICS_POINTS = st.number_input('CRITICS_POINTS',step=0.1,min_value=0.000)
USER_POINTS = st.number_input('USER_POINTS',step=0.1,min_value=0.000)

inputs={
    'CONSOLE':CONSOLE,
    'YEAR':YEAR,
    'CATEGORY':CATEGORY,
    'PUBLISHER':PUBLISHER,
    'RATING':RATING,
    'CRITICS_POINTS':CRITICS_POINTS,
    'USER_POINTS':USER_POINTS
}


if st.button('predict'):
    # res=requests.post(url='http://127.0.0.1:8000/predict',data=json.dumps(inputs))
    # st.json(res.text)


    model = jlb.load('vgsales_pipeline_model.pkl')
    print(type(inputs),inputs)

    X_input = pd.DataFrame(inputs,index=[0])


    print(X_input)
    prediction = model.predict(X_input)

    st.write(prediction)

