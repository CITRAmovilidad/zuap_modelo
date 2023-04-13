import pandas as pd 
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title ="Gráficos citra",
    page_icon="ⒸⒾⓉⓇⒶ",
    layout="wide"
)

path_logo = 'img/Logo-CITRA-2022-01.png'

logo = Image.open(path_logo)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.write(' ')

with col2:
    st.write(' ')

with col3:
    st.write(' ')

with col4:
    st.write(' ')

with col5:
    st.write(' ')
    
with col6:
    st.image(logo, width=180, use_column_width = "always")


#comment

st.title("Zona ZUAP (zona urbana de aire protegido)")


st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <iframe src="https://www.google.com/maps/d/embed?mid=1I7u66AdsOeryXxQFpYy6R3xyfQ8o14Y&ehbc=2E312F" width="100%" height="800"></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

#df = pd.read_csv("zuap_zonas_v2.csv")
#df['tipoalerta'] = df['tipoalerta'].astype('string')
#df['poligono'] = df['poligono'].astype('string')
#df = df.drop(['Unnamed: 0'], axis=1)
#df = df.set_index('date_only')


#st.bar_chart(df,y=df['tipoalerta'].str.count('ACCIDENT'),x="poligono")
#st.bar_chart(df,y=df['tipoalerta'].value_counts(),x='poligono')
