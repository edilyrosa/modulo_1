# API: https://fakestoreapi.com/products
import streamlit as st
st.title("🛒 Producto destacado")

productos = [

    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        109.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ],
    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
        209.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ],
    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_t.png",
        309.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ],
    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        109.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ],
    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
        209.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ],
    [
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_t.png",
        309.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    ]
    
]
# producto[1]
for p in productos:
    st.image(p[1], width=300)
    st.subheader(p[0])
    st.write('💲Precio:', p[2])
    st.write('📋:', p[3])
    st.divider()