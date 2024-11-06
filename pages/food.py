import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model

model = load_model("pages/foodmodel.h5")
new_title = '<p style="font-family:sans-serif; font-size: 48px; text-align: center">INDIAN FOOD DETECTION</p>'
st.markdown(new_title, unsafe_allow_html=True)
img = Image.open('pages/foodimg.jpg')
st.image(img)

uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
categories=['masala_dosa', 'pizza', 'chapati', 'idli', 'fried_rice', 'burger', 'chai']

def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((150, 150))
    img = np.array(img)
    img = img / 255.0
    return img


def make_prediction(image):
    img = preprocess_image(image)
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    return predictions


if uploaded_file is not None:
    image = uploaded_file
    predictions = make_prediction(image)
    st.image(image, caption="Uploaded Image", width=300)
    ind = predictions.argmax()
    categories[ind]