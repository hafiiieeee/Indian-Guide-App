import streamlit as st
import pickle
from PIL import Image

def plane():
    st.markdown(
        f"""<style>
            .stApp {{
                background-image: url("https://unsplash.com/photos/photo-of-taj-mahal-_WuPjE-MPHo");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>""", unsafe_allow_html=True

    )
    new_title = '<p style="font-family:sans-serif; font-size: 48px; text-align: center">FLIGHT PRICE PREDICTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    img = Image.open('pages/airplane.jpg')
    st.image(img)
    airline = st.selectbox('Enter The Airline', ('SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo',
                                                 'Air_India'))
    if airline == 'SpiceJet':
        c = 4
    elif airline == 'AirAsia':
        c = 0
    elif airline == 'Vistara':
        c = 5
    elif airline == 'GO_FIRST':
        c = 2
    elif airline == 'Indigo':
        c = 3
    else:
        c = 1
    city = st.selectbox('Enter Departure City', ('Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'))
    if city == 'Delhi':
        d = 2
    elif city == 'Mumbai':
        d = 5
    elif city == 'Bangalore':
        d = 0
    elif city == 'Kolkata':
        d = 4
    elif city == 'Hyderabad':
        d = 3
    else:
        d = 1
    city2 = st.selectbox('Enter Arrival City', ('Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'))
    if city2 == 'Delhi':
        dc = 2
    elif city2 == 'Mumbai':
        dc = 5
    elif city2 == 'Bangalore':
        dc = 0
    elif city2 == 'Kolkata':
        dc = 4
    elif city2 == 'Hyderabad':
        dc = 3
    else:
        dc = 1
    time2 = st.selectbox('Enter Departure Time', ('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
                                                  'Late_Night'))
    if time2 == 'Evening':
        dt = 2
    elif time2 == 'Early_Morning':
        dt = 1
    elif time2 == 'Morning':
        dt = 4
    elif time2 == 'Afternoon':
        dt = 0
    elif time2 == 'Night':
        dt = 5
    else:
        dt = 3
    time = st.selectbox('Enter Arrival Time', ('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
                                               'Late_Night'))
    if time == 'Evening':
        t = 2
    elif time == 'Early_Morning':
        t = 1
    elif time == 'Morning':
        t = 4
    elif time == 'Afternoon':
        t = 0
    elif time == 'Night':
        t = 5
    else:
        t = 3
    classair = st.selectbox('Enter Departure Time', ('Economy', 'Business'))
    if classair == 'Economy':
        e=1
    else:
        e=0
    features = [c,d,dt,t,dc,e]
    scaler = pickle.load(open('pages\scalerplane.sav', 'rb'))
    model = pickle.load(open('pages\modelplane.sav', 'rb'))
    pred = st.button("PREDICT")
    if pred:
        result = model.predict(scaler.transform([features]))
        st.write("total price", result)


plane()
