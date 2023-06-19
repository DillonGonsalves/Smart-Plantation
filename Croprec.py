import streamlit as st
import pickle
import numpy as np 
import requests
model = pickle.load(open('./Models/DecisionTree.pkl',mode='rb'))

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = "9d7cde1f6d07ec55650544be1631307e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


#st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.nationalgeographic.org%2Fassets%2Fphotos%2F120%2F983%2F091a0e2f-b93d-481b-9a60-db520c87ec33.jpg&imgrefurl=https%3A%2F%2Fwww.nationalgeographic.org%2Fencyclopedia%2Fcrops%2F&tbnid=uDs4hLmX-nDCWM&vet=12ahUKEwiMxeqCjMD2AhV7QWwGHV8mBoEQMygAegUIARDUAQ..i&docid=GEproQ-Y0UisOM&w=2000&h=1333&q=crop%20image&ved=2ahUKEwiMxeqCjMD2AhV7QWwGHV8mBoEQMygAegUIARDUAQhttps://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.nationalgeographic.org%2Fassets%2Fphotos%2F120%2F983%2F091a0e2f-b93d-481b-9a60-db520c87ec33.jpg&imgrefurl=https%3A%2F%2Fwww.nationalgeographic.org%2Fencyclopedia%2Fcrops%2F&tbnid=uDs4hLmX-nDCWM&vet=12ahUKEwiMxeqCjMD2AhV7QWwGHV8mBoEQMygAegUIARDUAQ..i&docid=GEproQ-Y0UisOM&w=2000&h=1333&q=crop%20image&ved=2ahUKEwiMxeqCjMD2AhV7QWwGHV8mBoEQMygAegUIARDUAQ")
st.markdown("<h4 style='text-align: center;'>Find out the most suitable crop to grow in your farm  </h4>", unsafe_allow_html=True)
Nitrogen=st.text_input('Nitrogen:',  placeholder = 'Enter the value(example:50)')
Phosphorous=st.text_input('Phosphorous:',  placeholder = 'Enter the value(example:50)')
Pottasium=st.text_input('Pottasium:',  placeholder = 'Enter the value(example:50)')
ph=st.text_input('ph level:',  placeholder = 'Enter the value')
Rainfall=st.text_input('Rainfall (in mm):',  placeholder = 'Enter the value')
State = st.selectbox('State:',('Maharastra','',''))
City = st.selectbox('City:',('Mumbai','',''))
if st.button('predict'):
    temperature,humidity=weather_fetch(City)
    data = np.array([[Nitrogen,Phosphorous, Pottasium, temperature, humidity, ph, Rainfall]])
    prediction = model.predict(data)
    st.markdown(prediction)