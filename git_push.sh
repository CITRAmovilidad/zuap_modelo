#!/bin/bash

cd /home/MDE/Documents/streamlit_pruebas/deploy/
fecha=$(date '+%Y-%m-%d')
git add distribucion_multinomial_grafico.pkl
git commit -m "Actualización diaria del archivo distribucion_multinomial_grafico.pkl - $fecha"
git push https://github.com/CITRAmovilidad/PrediccionZUAP.git master


