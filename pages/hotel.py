import streamlit as st
import pickle
from PIL import Image


def main():
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
    global k, l, j, h, g, m
    new_title = '<p style="font-family:sans-serif; font-size: 48px;">HOTEL PRICE PREDICTION</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    img = Image.open('pages\hotelwelcome.jpg')
    st.image(img)
    r = st.text_input("Enter the Rating", "Out of 5")
    city = st.selectbox('Enter City', ('kochi', 'trivandrum', 'kumarakom', 'pune', 'chennai', 'delhi',
                                       'bhubaneswar', 'goa', 'mumbai', 'lucknow', 'kolkata', 'bangalore',
                                       'hyderabad', 'pondicherry', 'patna', 'nagpur', 'indore', 'jaipur',
                                       'nashik', 'kanpur', 'chandigarh', 'guwahati', 'mangalore',
                                       'mysore', 'dehradun', 'srinagar', 'jamshedpur', 'gwalior',
                                       'amravati', 'durgapur', 'ranchi', 'aurangabad', 'ahmedabad',
                                       'amritsar', 'ludhiana', 'meerut', 'vadodara', 'raipur',
                                       'vijayawada', 'coimbatore', 'ghaziabad', 'allahabad', 'faridabad',
                                       'hazaribagh', 'gandhinagar', 'varanasi', 'noida', 'kanyakumari',
                                       'kashmir', 'sikkim', 'varkala'))
    if city == 'kochi':
        c = 27
    elif city == 'trivandrum':
        c = 46
    elif city == 'kumarakom':
        c = 29
    elif city == 'pune':
        c = 41
    elif city == 'chennai':
        c = 8
    elif city == 'delhi':
        c = 11
    elif city == 'bhubaneswar':
        c = 6
    elif city == 'goa':
        c = 16
    elif city == 'mumbai':
        c = 34
    elif city == 'lucknow':
        c = 30
    elif city == 'kolkata':
        c = 28
    elif city == 'bangalore':
        c = 5
    elif city == 'hyderabad':
        c = 20
    elif city == 'pondicherry':
        c = 40
    elif city == 'patna':
        c = 39
    elif city == 'nagpur':
        c = 36
    elif city == 'indore':
        c = 21
    elif city == 'jaipur':
        c = 22
    elif city == 'nashik':
        c = 37
    elif city == 'kanpur':
        c = 24
    elif city == 'chandigarh':
        c = 7
    elif city == 'guwahati':
        c = 17
    elif city == 'mangalore':
        c = 32
    elif city == 'mysore':
        c = 35
    elif city == 'dehradun':
        c = 10
    elif city == 'srinagar':
        c = 45
    elif city == 'jamshedpur':
        c = 23
    elif city == 'gwalior':
        c = 18
    elif city == 'amravati':
        c = 2
    elif city == 'durgapur':
        c = 12
    elif city == 'ranchi':
        c = 43
    elif city == 'aurangabad':
        c = 4
    elif city == 'ahmedabad':
        c = 0
    elif city == 'amritsar':
        c = 3
    elif city == 'ludhiana':
        c = 31
    elif city == 'meerut':
        c = 33
    elif city == 'vadodara':
        c = 47
    elif city == 'raipur':
        c = 42
    elif city == 'vijayawada':
        c = 50
    elif city == 'coimbatore':
        c = 9
    elif city == 'ghaziabad':
        c = 15
    elif city == 'allahabad':
        c = 1
    elif city == 'faridabad':
        c = 13
    elif city == 'hazaribagh':
        c = 19
    elif city == 'gandhinagar':
        c = 14
    elif city == 'varanasi':
        c = 48
    elif city == 'noida':
        c = 38
    elif city == 'kanyakumari':
        c = 25
    elif city == 'kashmir':
        c = 26
    elif city == 'sikkim':
        c = 44
    else:
        c = 49
    feature1 = st.selectbox('Enter The facilities', ('5-star hotel', 'Apartment', '4-star hotel', 'Free breakfast',
                                                     '3-star hotel', 'Sleeps 4', 'Free Wi-Fi', '2-star hotel',
                                                     'Breakfast', 'None', 'Sleeps 5', 'Sleeps 6', 'Sleeps 3',
                                                     'Sleeps 8',
                                                     'Villa', 'House', '1-star hotel', 'Sleeps 9', 'Bungalow', 'Pool',
                                                     'Sleeps 13', 'Sleeps 12', 'Sleeps 2', 'Sleeps 17', 'Sleeps 7',
                                                     'Sleeps 16', 'Sleeps 24', 'Sleeps 11', 'Free parking',
                                                     'Paid parking', 'Sleeps 10', 'Kid-friendly'))
    if feature1 == '5-star hotel':
        d = 5
    elif feature1 == 'Apartment':
        d = 6
    elif feature1 == '4-star hotel':
        d = 4
    elif feature1 == 'Free breakfast':
        d = 10
    elif feature1 == '3-star hotel':
        d = 3
    elif feature1 == 'Sleeps 4':
        d = 25
    elif feature1 == 'Free Wi-Fi':
        d = 9
    elif feature1 == '2-star hotel':
        d = 2
    elif feature1 == 'Breakfast':
        d = 7
    elif feature1 == 'None':
        d = 0
    elif feature1 == 'Sleeps 5':
        d = 26
    elif feature1 == 'Sleeps 6':
        d = 27
    elif feature1 == 'Sleeps 3':
        d = 24
    elif feature1 == 'Sleeps 8':
        d = 29
    elif feature1 == 'Villa':
        d = 31
    elif feature1 == 'House':
        d = 12
    elif feature1 == '1-star hotel':
        d = 1
    elif feature1 == 'Sleeps 9':
        d = 30
    elif feature1 == 'Bungalow':
        d = 8
    elif feature1 == 'Pool':
        d = 15
    elif feature1 == 'Sleeps 13':
        d = 19
    elif feature1 == 'Sleeps 12':
        d = 18
    elif feature1 == 'Sleeps 2':
        d = 22
    elif feature1 == 'Sleeps 17':
        d = 21
    elif feature1 == 'Sleeps 7':
        d = 28
    elif feature1 == 'Sleeps 16':
        d = 20
    elif feature1 == 'Sleeps 24':
        d = 23
    elif feature1 == 'Sleeps 11':
        d = 17
    elif feature1 == 'Free parking':
        d = 11
    elif feature1 == 'Paid parking':
        d = 14
    elif feature1 == 'Sleeps 10':
        d = 16
    else:
        d = 13
    feature2 = st.selectbox('Enter 2nd facilities', ('Free breakfast', 'Sleeps 10', 'Breakfast', 'Wi-Fi', '2 bedrooms',
                                                     'Free Wi-Fi', 'Paid parking', 'Air conditioning', 'Free parking',
                                                     'None', '1 bedroom', '3 bedrooms', 'Sleeps 2', 'Sleeps 4',
                                                     'Sleeps 8',
                                                     'Sleeps 28', 'Sleeps 3', '6 bedrooms', '4 bedrooms', 'Sleeps 7',
                                                     'Pool', 'Airport shuttle', 'Kitchen', 'Sleeps 9', '12 bedrooms',
                                                     '7 bedrooms'))
    if feature2 == 'Free breakfast':
        e = 12
    elif feature2 == 'Sleeps 10':
        e = 17
    elif feature2 == 'Breakfast':
        e = 10
    elif feature2 == 'Wi-Fi':
        e = 25
    elif feature2 == '2 bedrooms':
        e = 3
    elif feature2 == 'Free Wi-Fi':
        e = 11
    elif feature2 == 'Paid parking':
        e = 15
    elif feature2 == 'Air conditioning':
        e = 8
    elif feature2 == 'Free parking':
        e = 13
    elif feature2 == 'None':
        e = 0
    elif feature2 == '1 bedroom':
        e = 1
    elif feature2 == '3 bedrooms':
        e = 4
    elif feature2 == 'Sleeps 2':
        e = 18
    elif feature2 == 'Sleeps 4':
        e = 21
    elif feature2 == 'Sleeps 8':
        e = 23
    elif feature2 == 'Sleeps 28':
        e = 19
    elif feature2 == 'Sleeps 3':
        e = 20
    elif feature2 == '6 bedrooms':
        e = 6
    elif feature2 == '4 bedrooms':
        e = 5
    elif feature2 == 'Sleeps 7':
        e = 22
    elif feature2 == 'Pool':
        e = 16
    elif feature2 == 'Airport shuttle':
        e = 9
    elif feature2 == 'Kitchen':
        e = 14
    elif feature2 == 'Sleeps 9':
        e = 24
    elif feature2 == '12 bedrooms':
        e = 2
    else:
        e = 7
    feature3 = st.selectbox('Enter 3rd facilities', ('Free Wi-Fi', 'Wi-Fi', 'Free parking', 'Air conditioning',
                                                     'Pet-friendly', 'Kitchen', 'None', 'Paid parking', 'Pool',
                                                     '4 bedrooms', '1 bedroom', '2 bedrooms', '5 bedrooms',
                                                     '3 bedrooms', '28 bedrooms', 'Restaurant', 'Room service',
                                                     '4 bathrooms', 'Breakfast', 'Kid-friendly', 'Fireplace',
                                                     'Cable TV', 'Full-service laundry', '12 bathrooms', '3 bathrooms',
                                                     'Beach access'))
    if feature3 == 'Free Wi-Fi':
        f = 15
    elif feature3 == 'Wi-Fi':
        f = 25
    elif feature3 == 'Free parking':
        f = 16
    elif feature3 == 'Air conditioning':
        f = 10
    elif feature3 == 'Pet-friendly':
        f = 21
    elif feature3 == 'Kitchen':
        f = 19
    elif feature3 == 'None':
        f = 0
    elif feature3 == 'Paid parking':
        f = 20
    elif feature3 == 'Pool':
        f = 22
    elif feature3 == '4 bedrooms':
        f = 8
    elif feature3 == '1 bedroom':
        f = 1
    elif feature3 == '2 bedrooms':
        f = 3
    elif feature3 == '5 bedrooms':
        f = 9
    elif feature3 == '3 bedrooms':
        f = 6
    elif feature3 == '28 bedrooms':
        f = 4
    elif feature3 == 'Restaurant':
        f = 23
    elif feature3 == 'Room service':
        f = 24
    elif feature3 == '4 bathrooms':
        f = 7
    elif feature3 == 'Breakfast':
        f = 12
    elif feature3 == 'Kid-friendly':
        f = 18
    elif feature3 == 'Fireplace':
        f = 14
    elif feature3 == 'Cable TV':
        f = 13
    elif feature3 == 'Full-service laundry':
        f = 17
    elif feature3 == '12 bathrooms':
        f = 2
    elif feature3 == '3 bathrooms':
        f = 5
    else:
        f = 11
    feature4 = st.selectbox('Enter 4th facilities', ('Free parking', 'Free Wi-Fi', 'Air conditioning', 'Fireplace',
                                                     'Pool', 'Beach access', 'Paid parking', 'Breakfast',
                                                     'Full-service laundry', 'Restaurant', '0', 'Kitchen',
                                                     'Pet-friendly', 'Room service', '7 bathrooms', '1 bathroom',
                                                     'Airport shuttle', '5 bathrooms', 'Elevator', 'Spa', '2 bathrooms',
                                                     'No outdoor grill', 'Bar', 'Smoke-free', 'Wheelchair accessible',
                                                     'Hot tub', 'Wi-Fi', 'Kid-friendly', 'Cable TV',
                                                     'No air conditioning'))
    index = 0
    lst = (['Free parking', 'Free Wi-Fi', 'Air conditioning', 'Fireplace',
            'Pool', 'Beach access', 'Paid parking', 'Breakfast',
            'Full-service laundry', 'Restaurant', '0', 'Kitchen',
            'Pet-friendly', 'Room service', '7 bathrooms', '1 bathroom',
            'Airport shuttle', '5 bathrooms', 'Elevator', 'Spa', '2 bathrooms',
            'No outdoor grill', 'Bar', 'Smoke-free', 'Wheelchair accessible',
            'Hot tub', 'Wi-Fi', 'Kid-friendly', 'Cable TV',
            'No air conditioning'])
    lst.sort()
    for i in lst:
        if feature4 == i:
            g = index
            break
        index += 1
    feature5 = st.selectbox('Enter 5th facilities', ('Pool', 'No air conditioning', 'Restaurant', 'Air conditioning',
                                                     'Paid parking', 'Hot tub', 'Kitchen', 'Kid-friendly',
                                                     'Room service', 'Full-service laundry', '0', 'Airport shuttle',
                                                     'Cable TV', 'Free parking', 'Beach access', 'Fitness center',
                                                     '2 beds', 'Elevator', 'Breakfast', 'Pet-friendly', 'Fireplace',
                                                     'Free Wi-Fi', 'Bar', 'Spa', 'Not pet-friendly', 'Smoke-free',
                                                     'Wi-Fi', '1 bed', 'No airport shuttle'))
    index1 = 0
    lst1 = (['Pool', 'No air conditioning', 'Restaurant', 'Air conditioning',
             'Paid parking', 'Hot tub', 'Kitchen', 'Kid-friendly',
             'Room service', 'Full-service laundry', '0', 'Airport shuttle',
             'Cable TV', 'Free parking', 'Beach access', 'Fitness center',
             '2 beds', 'Elevator', 'Breakfast', 'Pet-friendly', 'Fireplace',
             'Free Wi-Fi', 'Bar', 'Spa', 'Not pet-friendly', 'Smoke-free',
             'Wi-Fi', '1 bed', 'No airport shuttle'])
    lst1.sort()
    for i in lst1:
        if feature5 == i:
            h = index1
            break
        index1 += 1
    feature6 = st.selectbox('Enter 6th facilities', ('Hot tub', 'Air conditioning', 'No airport shuttle', 'Kitchen',
                                                     'Restaurant', 'Airport shuttle', 'No crib', 'Beach access', 'Bar',
                                                     'Full-service laundry', '0', 'Kid-friendly', 'Room service',
                                                     'Paid parking', 'Pet-friendly', 'Fitness center', 'Free Wi-Fi',
                                                     'Cable TV', 'Pool', 'Fireplace', 'Spa', 'Breakfast', 'Smoke-free',
                                                     'No air conditioning', 'Not smoke-free', 'Accessible',
                                                     'Free parking', 'No beach access'))
    index2 = 0
    lst2 = (['Hot tub', 'Air conditioning', 'No airport shuttle', 'Kitchen',
             'Restaurant', 'Airport shuttle', 'No crib', 'Beach access', 'Bar',
             'Full-service laundry', '0', 'Kid-friendly', 'Room service',
             'Paid parking', 'Pet-friendly', 'Fitness center', 'Free Wi-Fi',
             'Cable TV', 'Pool', 'Fireplace', 'Spa', 'Breakfast', 'Smoke-free',
             'No air conditioning', 'Not smoke-free', 'Accessible',
             'Free parking', 'No beach access'])
    lst2.sort()
    for i in lst2:
        if feature6 == i:
            j = index2
            break
        index2 += 1
    feature7 = st.selectbox('Enter 7th facilities', ('Air conditioning', 'Fitness center', 'No beach access',
                                                     'Full-service laundry', 'Airport shuttle', 'Pet-friendly', 'Spa',
                                                     'No elevator', 'Room service', 'Restaurant', 'Kid-friendly', '0',
                                                     'Smoke-free', 'Free Wi-Fi', 'No crib', 'Paid parking', 'Kitchen',
                                                     'Bar', 'Crib', 'Business center', 'No airport shuttle',
                                                     'Free parking', 'No air conditioning', 'Not wheelchair accessible',
                                                     'Cable TV', 'Accessible', 'Beach access'))
    index3 = 0
    lst3 = (['Air conditioning', 'Fitness center', 'No beach access',
             'Full-service laundry', 'Airport shuttle', 'Pet-friendly', 'Spa',
             'No elevator', 'Room service', 'Restaurant', 'Kid-friendly', '0',
             'Smoke-free', 'Free Wi-Fi', 'No crib', 'Paid parking', 'Kitchen',
             'Bar', 'Crib', 'Business center', 'No airport shuttle',
             'Free parking', 'No air conditioning', 'Not wheelchair accessible',
             'Cable TV', 'Accessible', 'Beach access'])
    lst3.sort()
    for i in lst3:
        if feature7 == i:
            k = index3
            break
        index3 += 1
    feature8 = st.selectbox('Enter 8th facilities', ('Fitness center', 'Spa', 'No elevator', 'Bar', 'Kid-friendly',
                                                     'Full-service laundry', 'Restaurant', 'No fitness center',
                                                     'Airport shuttle', 'Room service', '0', 'Accessible', 'No crib',
                                                     'Kitchen', 'Free Wi-Fi', 'Smoke-free', 'Hot tub',
                                                     'No beach access', 'Beach access', 'Breakfast', 'Pet-friendly',
                                                     'Business center', 'Free parking', 'No airport shuttle',
                                                     'No fireplace', 'Golf', 'Paid parking', 'Balcony'))
    index4 = 0
    lst4 = (['Fitness center', 'Spa', 'No elevator', 'Bar', 'Kid-friendly',
             'Full-service laundry', 'Restaurant', 'No fitness center',
             'Airport shuttle', 'Room service', '0', 'Accessible', 'No crib',
             'Kitchen', 'Free Wi-Fi', 'Smoke-free', 'Hot tub',
             'No beach access', 'Beach access', 'Breakfast', 'Pet-friendly',
             'Business center', 'Free parking', 'No airport shuttle',
             'No fireplace', 'Golf', 'Paid parking', 'Balcony'])
    lst4.sort()
    for i in lst4:
        if feature8 == i:
            m = index4
            break
        index4 += 1

    feature9 = st.selectbox('Enter 9th facilities', ('Spa', 'Restaurant', 'No fireplace', 'Bar', '0', 'Kid-friendly',
                                                     'Beach access', 'Smoke-free', 'Room service', 'No ironing board',
                                                     'Accessible', 'Full-service laundry', 'No elevator',
                                                     'Airport shuttle', 'Kitchen', 'No fitness center',
                                                     'Business center', 'No crib', 'Free parking', 'Heating',
                                                     'No beach access', 'No airport shuttle', 'Fitness center',
                                                     'Breakfast', 'No air conditioning', 'Free Wi-Fi', 'Crib'))
    index5 = 0
    lst5 = (['Spa', 'Restaurant', 'No fireplace', 'Bar', '0', 'Kid-friendly',
             'Beach access', 'Smoke-free', 'Room service', 'No ironing board',
             'Accessible', 'Full-service laundry', 'No elevator',
             'Airport shuttle', 'Kitchen', 'No fitness center',
             'Business center', 'No crib', 'Free parking', 'Heating',
             'No beach access', 'No airport shuttle', 'Fitness center',
             'Breakfast', 'No air conditioning', 'Free Wi-Fi', 'Crib'])
    lst5.sort()
    for i in lst5:
        if feature9 == i:
            l = index5
            break
        index5 += 1
    features = [r, c, d, e, f, g, h, j, k, m, l]
    scaler = pickle.load(open('pages\scalerprojecthotel.sav', 'rb'))
    model = pickle.load(open('pages\modelprojecthotel.sav', 'rb'))
    pred = st.button("PREDICT")
    if pred:
        result = model.predict(scaler.transform([features]))
        st.write("total price", result)


main()
