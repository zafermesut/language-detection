import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer

pipeline = load('pipeline.joblib')

cv = CountVectorizer()

st.title('Language Detection App')

text = st.text_area('Enter some text')

if st.button('Predict'):
    prediction = pipeline.predict([text])
    st.write(f'The language is: {prediction[0]}')

