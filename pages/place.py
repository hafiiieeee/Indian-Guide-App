import pandas as pd
import pymysql
import warnings
import streamlit as st
from PIL import Image


def place():
    st.title("INDIAN PLACE RECOMMENDER")

    img = Image.open('pages/place.jpg')
    st.image(img)

    warnings.filterwarnings('ignore')
    conn = pymysql.connect(host='localhost', user='root', password='root', database='project')
    querry = ("select * from place")
    df = pd.read_sql(querry, conn)
    city = st.selectbox('Enter The State', ('Delhi', 'Maharastra', 'Karnataka', 'Telangana', 'West Bengal',
                                            'Goa', 'Gujarat', 'Rajasthan', 'Punjab', 'Kerala', 'Maharashtra',
                                            'Madhya Pradesh', 'Himachal Pradesh', 'Uttarakhand',
                                            'Uttar Pradesh', 'Jammu and Kashmir', 'Ladakh', 'Odisha',
                                            'Tamil Nadu', 'Andhra Pradesh', 'Sikkim', 'Assam',
                                            'Arunachal Pradesh', 'Tripura', 'Chhattisgarh', 'Nagaland',
                                            'Puducherry', 'Andaman and Nicobar Islands', 'Daman and Diu',
                                            'Jharkhand', 'Bihar', 'Haryana', 'Meghalaya'))
    pred = st.button("SHOW BEST PLACES TO VISIT")
    if pred:
        result = df.loc[df['State'] == city]
        result = result.drop(['MyUnknownColumn', 'Establishment Year', 'Google review rating', 'Weekly Off',
                              'Number of google review in lakhs'], axis=1)
        print(result)
        st.write("HERE IS THE BEST PLACE FOR YOU TO VISIT", result)
    else:
        print("TRY AGAIN")


place()
