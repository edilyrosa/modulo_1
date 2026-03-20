
# Corre en la termina:
#? pip install streamlit
#* streamlit run 7_ejercicio.py

import streamlit as st 

#Creando credenciales
CORREO_ELECTRONICO = 'admin@gmail.com'
PASSWORD = '1234'

#Titulo de la website
st.title('Sitema de loging con Py 🐍')
correo = st.text_input('Digita tu correo 📧')
password = st.text_input('Digita tu contradena', type='password')

if st.button('Ingresar!'):
    if correo == CORREO_ELECTRONICO and password == PASSWORD:
        st.success('Acceso autorizado ')
    else:
        st.error('Acceso denegado ')


# TODO PROXIMO_TEMA:
    # TIPOS DE DATOS ESTRUCTURALES: LISTAS, TUPLAS, DICCIONARIOS, SETS
    # CILCLOS: FOR, WHILE, BREAK, CONTINUE, RANGE()