import streamlit as st
import pickle

MODEL_FILE = "modelKualitasUdaraRFC.pkl" #Random Forest Classifier dengan akurasi 99%
pickle_in = open(MODEL_FILE, 'rb')
classifier = pickle.load(pickle_in)

st.set_page_config(
    page_title="Klasifikasi Kualitas Udara - Kelompok 7",
    page_icon="7️⃣"
)

st.title("Klasifikasi Kualitas Udara")
st.markdown('By kelompok 7:')
st.markdown("1. Arya Pangestu")
st.markdown("2. Husni Fadhilah Dhiya Ul Haq")
st.markdown("3. Muhammad Hanief")

st.write("Kualitas udara sekarang:")

st.sidebar.markdown('## Atur Parameter Variabel')
pm10 = st.sidebar.slider('pm10: Partikulat', 0, 150, 30) 
pm25 = st.sidebar.slider('pm25: Partikulat', 0, 150, 48) 
so2 = st.sidebar.slider('so2: Sulfida', 0, 150, 24)
co = st.sidebar.slider('co: Carbon Monoksida', 0, 150, 4)
o3 = st.sidebar.slider('o3: Ozon', 0, 150, 32)
no2 = st.sidebar.slider('no2: Nitrogen dioksida', 0, 150, 7)

prediction = classifier.predict([[pm10, pm25, so2, co, o3, no2]])
if (prediction[0] == 0) :
    st.success("Baik")
elif (prediction[0] == 1) :
    st.success("Sedang")
elif (prediction[0] == 2) :
    st.success("Tidak Sehat")
