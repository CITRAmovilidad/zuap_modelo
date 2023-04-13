import streamlit as st
import pandas as pd 
import pickle
import plotly.graph_objects as go
import plotly.figure_factory as ff
from PIL import Image

st.set_page_config(
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

st.write('## Descripción')
st.write("Los siguientes gráficos representan la probabilidad futura de que ocurran **JAM**, **ACCIDENT** o **WEATHERHAZARD** en la subzona seleccionada dentro de la zona **ZUAP**. Siendo:")
st.write("- JAM : congestión")
st.write("- ACCIDENT : incidente víal")
st.write("- WEATHERHAZARD : otros... (bache o hueco en la vía, semaforo dañado, peligro meteorológico en la carretera)")


# Importar el diccionario desde el archivo binario
with open('distribucion_multinomial_grafico.pkl', 'rb') as handle:
    distribucion_multinomial_grafico = pickle.load(handle)


options = st.multiselect(
        'Seleccione una o varias zonas para visualizar sus gráficos',
        ['Zona1', 'Zona2', 'Zona3', 'Zona4', 'Zona5', 'Zona6', 'Zona7'], )

intervalos = ["4-6", "7-9", "10-12", "13-15", "16-18", "19-22", "noche"]
zonas = ['Zona1', 'Zona2', 'Zona3', 'Zona4', 'Zona5', 'Zona6', 'Zona7']

# Definir los datos de los ejes
axis_labels = ['JAM', 'ACCIDENT', 'WEATHERHAZARD']

# Definir el diagrama ternario
ternary_data = {
    'sum': 1,
    'aaxis': {'title': axis_labels[0]},
    'baxis': {'title': axis_labels[1]},
    'caxis': {'title': axis_labels[2]}
}

# Generar los gráficos para cada zona y cada intervalo
for zona in zonas:
    if zona in options:
        st.write(f"<p style='font-size: 35px; font-weight: bold; font-family: 'Gill Sans Extrabold';'>{zona}</p>", unsafe_allow_html=True)

        if zona == "Zona1":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=16GTQV2oujPM9HYyr20HXumbhvup_RTY&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona2":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1dxI9bB_qWlV3Y4lO1Eu9XAT-m6o23OU&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona3":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                              <iframe src="https://www.google.com/maps/d/embed?mid=1qmXYDQBGvWcpjrhKYqRbN8QyVWVlB40&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona4":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1Ie-Qkar4vMQhXLN1g4sOV7H4mJONlXk&hl=es&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona5":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1Xwykv6g9V7EVdgGDIwvYA5qY81ghaUQ&hl=es&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona6":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=18EIxeOgKcCgq6C9jwpoK33Q4Uj7cJZ4&hl=es&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        if zona == "Zona7":
                    st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <iframe src="https://www.google.com/maps/d/embed?mid=1gO6rWM7UVuxmAkC3Ic08YJxNGYzARHo&ehbc=2E312F" width="100%" height="480"></iframe>
                            </div>
                            """,
                            unsafe_allow_html=True,
                    )
        
        st.write("___________________________________________________________________________________")
        # Crear dos columnas en el contenedor
        col1, col2 = st.columns(2)

        for intervalo in intervalos:
            #nombre del dataframe actual
            nombre_df = f"{zona}_{intervalo}"
            #Dataframe actual 
            df = distribucion_multinomial_grafico[nombre_df]
            # Crear el gráfico
            fig = go.Figure()
            # Añadir el diagrama ternario
            fig.add_trace(go.Scatterternary({
                'mode': 'markers',
                'a': df['JAM'],
                'b': df['ACCIDENT'],
                'c': df['WEATHERHAZARD'],
                'marker': {
                    'color': df['JAM'],
                    'colorscale': 'YlOrRd',
                    'size': 10,
                    'colorscale': 'Hot',
                    'line': {
                        'width': 1,
                        'color': 'black'

                    },
                    'colorbar': {'title': 'JAM', 'len': 1, 'y': 0.6}
                },
                'name': 'Puntos'
            }))
            # Configurar el layout
            fig.update_layout({
                'title': f'Ternary Heatmap para - {nombre_df}',
                'ternary': ternary_data,
                'showlegend': False,
                'width': 500
            })
            # Mostrar el gráfico en la columna correspondiente


            if intervalo in ["4-6", "7-9", "10-12"]:
                
                col1.plotly_chart(fig, use_container_width=True)
            else:
                col2.plotly_chart(fig, use_container_width=True)
    


