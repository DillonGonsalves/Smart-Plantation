import streamlit as st
import pandas as pd
from Utils.fertilizer import fertilizer_dic

st.markdown("<h4 style='text-align: center;'>Get informed advice on fertilizer based on soil  </h4>", unsafe_allow_html=True)
N=int(st.number_input('Nitrogen:'))
P=int(st.number_input('Phosphorous:'))
K=int(st.number_input('Pottasium:'))
crop_name = st.selectbox('Crop you want to grow:',('rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean','blackgram','lentil','pomegranate','banana','mango','grapes','watermelon','muskmelon','apple','orange','papaya','coconut','cotton','jute','coffee'))
if st.button("Submit"):
    df = pd.read_csv('Data/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]
    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"
    st.markdown(fertilizer_dic[key],unsafe_allow_html=True)