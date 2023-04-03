import pandas as pd 
import streamlit as st

st.set_page_config(
    page_title ="Gráficos citra",
    page_icon="📈",
    layout="wide"
)

#comment

st.title("Inicio")
st.sidebar.success("Seleccione una página")


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
