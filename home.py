import streamlit as st
import pickle
from PIL import Image
import base64
def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image = get_image("taj.jpg")
url="https://colab.research.google.com/drive/1iqWlhSEwqY3L0xJysGxX6sZ8VoawJSXE#scrollTo=jewbkke-5p1e"
url2="https://colab.research.google.com/drive/14huNBl2JESQWurwWT4tJNJKbFTfv7_mo"
def home():
    st.markdown(
        f"""<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>""", unsafe_allow_html=True
    )
    new_title = '<p style="font-family:sans-serif; font-size: 48px; ">INTRODUCTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown(''' 
        Welcome to the Trip Guide App!''')
    st.markdown('''
        This app helps you to guide in travel to india.
        ''')

    new_title = '<p style="font-family:sans-serif; font-size: 25px;">PROJECT OVERVIEW</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        This project aims is to designed to provide travelers 
        with a comprehensive guide to exploring India. 
        The app aims to offer personalized recommendations, real-time information, 
        and immersive experiences to make traveling in India seamless and enjoyable.
        ''')

    new_title = '<p style="font-family:sans-serif; font-size: 25px;">MODEL DESCRIPTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        The dataset used in this project is google_hotel_dataset for indian hotel price prediction
        and used clean_dataset for price prediction of cost charge by planes which travel through in specified airports,
         at last Top indian places to visit used for recommend places for travel
         which has been thoroughly cleaned and prepared for analysis.
        Each row in the dataset represents and guide traveller with its features.
        ''')

    new_title = '<p style="font-family:sans-serif; ; font-size: 25px;">MODEL PERFORMANCE</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; ; font-size: 15px;">HOTEL PRICE PREDICTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        Our hotel price prediction model achieved outstanding performance, ensuring accurate forecasts for hotel prices.
        most performing algorithms is GradientBoostingRegressor with the feature set ensures accurate and 
        reliable predictions.It provide
        ''')
    st.markdown("""
                <table>
                <thead>
                <tr>
                    <th><b>Measure</b></th>
                    <th><b>Score</b></th>
                </tr>
                </thead>
                <tbody>
                <tr><td>r2_score</td><td>0.7691</td></tr>
                <tr><td>mean_abs_error</td><td>996.16</td></tr>
                <tr><td>mean_sqrd_error</td><td>2277996</td></tr>
                <tr><td>root_mean_error</td><td>1509.30</td></tr>
                </tbody>
                </table>
                """, unsafe_allow_html=True)
    st.write("")
    st.write("google colab:[hotel prediction](%s)" %url)
    new_title = '<p style="font-family:sans-serif;  font-size: 15px;">PLANE PRICE PREDICTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""
            Our Plane price prediction model achieved outstanding performance, ensuring accurate forecasts for hotel prices.
            most performing algorithms is Random Forest algorithm with the feature set ensures accurate and 
            reliable predictions.It provide
            """)
    st.markdown("""
                    <table>
                    <thead>
                    <tr>
                        <th><b>Measure</b></th>
                        <th><b>Score</b></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr><td>r2_score</td><td>0.9479</td></tr>
                    <tr><td>mean_abs_error</td><td>3264.45</td></tr>
                    <tr><td>mean_sqrd_error</td><td>26754450</td></tr>
                    <tr><td>root_mean_error</td><td>5172.47</td></tr>
                    </tbody>
                    </table>
                    """, unsafe_allow_html=True)
    st.write("google colab:[plane prediction](%s)" % url2)

home()