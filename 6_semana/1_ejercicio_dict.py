import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Garficas desder listas para crear un DataFrame')
categorias = st.text_input('Digita las categorias, separadas por coma:', 'Ana, Luis, Carlos, Maria' )
datos = st.text_input('Digita los DATOS, separadas por coma:', '18, 15, 12, 20' )

with st.expander('Opciones de graficos'):
    tipo_grafico = st.selectbox(
        'Elige el tipo de grafico',
        ('Lineal', 'Dispercion', 'Barras V', 'Barras H', )
    )

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
    if tipo_grafico == 'Lineal':
        ax.plot(df['Categorias'], df['Datos'])
    elif tipo_grafico == 'Dispercion':
        ax.scatter(df['Categorias'], df['Datos'], color='Red')
    
    elif tipo_grafico == 'Barras V':
        ax.bar(df['Categorias'], df['Datos'], color='Red')
    
    elif tipo_grafico == 'Barras H':
        ax.barh(df['Categorias'], df['Datos'], color='Red')
    
    #TODO: Dibujar según la selección del usuario
    
    ax.set_title('Grafico de datos')
    ax.set_xlabel('Categorias')
    ax.set_xlabel('Datos')
        
    st.pyplot(fig)