import streamlit as st
import joblib

model = joblib.load('iris_classifier.joblib')

st.title('Iris Flower Predictor')
st.header('Enter Measurements:')

sl = st.number_input('Sepal Length (cm)')
sw = st.number_input('Sepal Width (cm)')
pl = st.number_input('Petal Length (cm)')
pw = st.number_input('Petal Width (cm)')

if st.button('Predict'):
    prediction = model.predict([[sl, sw, pl, pw]])
    species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    st.success(f'Predicted Species: {species[prediction[0]]}')