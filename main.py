import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

# Import Model
pipe = pickle.load(open('/Users/jayeshpatel/Documents/Jupyter Notebook/pipe.pkl', 'rb'))
df = pickle.load(open('/Users/jayeshpatel/Documents/Jupyter Notebook/df.pkl','rb'))

st.title('Laptop Price Predictor')

brand = st.selectbox('Brand',df['Company'].unique())
type = st.selectbox('Type',df['TypeName'].unique())
os = st.selectbox('Operating System',df['os'].unique())
cpu_comp = st.selectbox('CPU',df['cpu'].unique())
cpu_freq = st.number_input(label='CPU Frequency (Hz)',min_value=0.1,step=0.1)
gpu_comp = st.selectbox('GPU Company',df['GPU_Company'].unique())
ram = st.number_input(label='RAM (GB)',min_value=1,step=1)
weight = st.number_input(label='Weight (Kg)',min_value=0.1,step=0.1)
ips = st.selectbox('IPS Pannel',['Yes','No'])
screen_size = st.number_input('Screen Size',min_value=0.1,step=0.1)
srh = st.number_input('Screen Resolution (Horizontal)',min_value=1,step=1)
srv = st.number_input('Screen resolution (Vertical)',min_value=1,step=1)
ssd = st.selectbox('SSD Size (GB)',sorted(df['ssd'].unique()))
hdd = st.selectbox('HDD Size (GB)',sorted(df['hdd'].unique()))
hybrid = st.selectbox('Hybrid Size (GB)',sorted(df['hybrid'].unique()))
flash_storage = st.selectbox('Flash Storage Size (GB)',sorted(df['flash_storage'].unique()))

if st.button('Predict'):
    ppi = None
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    ppi = ((srh**2)+(srv**2))**0.5/screen_size
    query = np.array([brand, type, cpu_freq, ram, gpu_comp, weight, cpu_comp, ips, ppi, ssd, hdd, hybrid, flash_storage,os])
    query = query.reshape(1,14)
    st.subheader("The predicted price of this configuration is: " + str(int(np.exp(pipe.predict(query)[0]))*93.25) + ' Rupees')
