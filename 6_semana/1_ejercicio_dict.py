import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Garficas desder listas para crear un DataFrame')
categorias = st.text_input('Digita las categorias, separadas por coma:', 'Ana, Luis, Carlos, Maria' )
datos = st.text_input('Digita los DATOS, separadas por coma:', '18, 15, 12, 20' )

if st.button('Generar Grafico'):
    #* CASTING
    # √ categorias → str a lista de strs → 'Ana, Luis, Carlos, Maria' → ['Ana', 'Luis', 'Carlos', 'Maria']
    # √ datos → str a lista de strs → lista de float 
    lista_categorias = categorias.split(',')
    lista_datos = datos.split(',') # ['18', '15', '12', '20']
    lista_datos_num = [float(n) for n in lista_datos]
    
    #*Creamos el DataFrame
    df = pd.DataFrame({
        'Categorias':lista_categorias,
        'Datos':lista_datos_num
    })
    
    st.write('📊DataFrame Generado')
    #TODO if st.select_slider('bar', 'barh'....):
    fig, ax = plt.subplots()
    ax.plot(df['Categorias'], df['Datos'])
    ax.scatter(df['Categorias'], df['Datos'], color='Red')
    ax.bar(df['Categorias'], df['Datos'], color='Red')
    ax.barh(df['Categorias'], df['Datos'], color='Red')
    
    ax.set_title('Grafico de datos')
    ax.set_xlabel('Categorias')
    ax.set_xlabel('Datos')
        
    st.pyplot(fig)