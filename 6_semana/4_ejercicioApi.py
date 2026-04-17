import streamlit as st
import requests 


def obtener_productos():
    url = 'https://fakestoreapi.com/products'
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status() # si el codigo del sttaus es 400 o 500 tanza una excepcion
        return respuesta.json(), None
    except Exception as e:
        print('An exception occurred')
        return None, str(e)
        
        
productos, error = obtener_productos()

if error:
    st.error('❌ Oops ha ocurrido un error!')

elif productos:
    for producto in productos:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(producto["image"], use_container_width=True)
        with col2:
            st.write(producto["title"])