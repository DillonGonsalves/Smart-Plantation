
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Smart plantation',page_icon=":herb:")



# 1. as sidebar menu
#with st.sidebar:
 #   selected = option_menu("Main Menu", ["Home", 'Settings'], 
 #       icons=['house', 'gear'], menu_icon="cast", default_index=1)
 #   selected

# 2. horizontal menu
selected2 = option_menu(None, ["Home", "🌱Crop", "👨‍🌾️Fertilizer"], 
    icons=['house', 'corn', 'corn'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# 3. CSS style definitions
#selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    #icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #menu_icon="cast", default_index=0, orientation="horizontal",
    #styles={
    #   "container": {"padding": "0!important", "background-color": "#fafafa"},
    #    "icon": {"color": "orange", "font-size": "25px"}, 
    #    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #    "nav-link-selected": {"background-color": "green"},
    #}
#)
if selected2 == "Home":
    #st.set_page_config(page_title="Smart plantation",layout="wide")

#st.markdown("""
# Multi-Page App
#""")

# Add all your application here
#app.add_app("Crop recommendation", croprec.app)
#app.add_app("Fertilizers recommendation", fertilizer.app)

# The main app
#app.run()


#st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>🌴Welcome to Smart plantation🌴</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color:#2E8B57'>Smart Plantation  is  a  web application that will help farmers </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#2E8B57'> to perform the agro-marketing leading to achieve success</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#2E8B57'> and increase their standards of living . </h5>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("<h3 style='text-align: center;'>Here are some questions we'll answer  </h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#ADFF2F	'>1. What crop to plant here ? </h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#ADFF2F	'>2. What fertilizers to use ? </h5>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("<h3 style='text-align: center;'>How to use ? </h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color:#7CFC00'>1. Crop recommendation : </h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center-left; color:#3CB371 '>a.     Enter the Nitogen value of the soil <br>b.      Enter Phosphorous value <br>c.      Enter Potassium value <br>d.         Enter pH of the soil <br>e.      Enter Rainfall in the area (in mm) <br>f.        Enter State <br>g.      Enter City <br>h.       Click on the Predict button to get the crop </h5>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; color:#7CFC00'>2. Fertilizer recommendation : </h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center-left; color:#3CB371'>a.     Enter the Nitogen value of the soil <br>b.      Enter Phosphorous value <br>c.      Enter Potassium value<br>d.         Enter the crop you want to plant <br>e.       Click on the Predict button to get the fertilizer neede  </h5>", unsafe_allow_html=True)


if selected2 == "🌱Crop":
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
    City = st.selectbox('City:',('Mumbai','	Pune','Nagpur','Thane','Nashik','Aurangabad ','Solapur ','Jalgaon','Amravati','Nanded','Kolhapur ','Akola','Ulhasnagar','Sangli ','Malegaon','Latur','Dhule','Ahmednagar','Ichalkaranji','Miraj','Chandrapur','Parbhani','Jalna','Bhusawal','Navi Mumbai','Panvel','Satara','Beed','Yavatmal','Kamptee','Barshi','Achalpur','Osmanabad','Nandurbar','Wardha','Udgir','Hinganghat','','','',''))
    if st.button('predict'):
        temperature,humidity=weather_fetch(City)
        data = np.array([[Nitrogen,Phosphorous, Pottasium, temperature, humidity, ph, Rainfall]])
        prediction = model.predict(data)
        st.markdown(prediction)

if selected2 == "👨‍🌾️Fertilizer":
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