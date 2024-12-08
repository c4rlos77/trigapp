
import streamlit as st
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

st.title("Evaluemos lo que has aprendido")
st.markdown("")


#1
st.subheader("1. Deriva la siguiente expresion: ")
st.latex(r"f(x) = tan(x) - sen(x)")
opciones1 = {
    "1": r"f'(x) = sec^2(x) - cos(x)",
    "2": r"f'(x) = sec^2(x) + cos(x)",
    "3": r"f'(x) = sen(x) - cos(x)"
}
pre1 = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones1.keys()),
    format_func=lambda x: opciones1[x],
)

#2
st.subheader("2. ¿La funcion f'(x) = sen(X) en que puntos es igual a 0? ")
opciones2 = {
    "1": r"x = n*pi, con n en Z",
    "2": r"x = pi/2 + n\pi, con n en Z ",
    "3": r"x = 2n/pi, con n en Z"
}
pre2 = st.radio(
    "¿Cuales son los puntos? Recuerda que la funcion sen(x) es ciclica",
    options=list(opciones2.keys()),
    format_func=lambda x: opciones2[x]
)

#3
st.subheader("3. Deriva la siguiente funcion: ")
st.latex(r"f(x) = tan(sen(7x^3))")
opciones3 = {
    "1": "f'(x) = 21x^2sec^2(sen(7x^3))cos(7x^3)",
    "2": "f'(x) = 21x^2sec^2(7x^3)cos(sen(7x^3))",
    "3": "f'(x) = 21x^2sec^2(sen(7x^3))7x^2cos(7x^3)"
}
pre3 = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones3.keys()),
    format_func=lambda x: opciones3[x]
)

#4
st.subheader("4. Deriva la siguiente funcion: ")
st.latex(r"f(x) = e^sen(x)")
opciones4 = {
     "1": r"f'(x) = cos(x)e^sen(x)",
    "2": r"f'(x) = sen(x)e^cos(x)",
    "3": r"f'(x) = sen(x)e^sen(x)"
}
pre4 = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones4.keys()),
    format_func=lambda x: opciones4[x]
)

#5
st.subheader("5. Cual de las siguientes graficas corresponde a la siguiente derivada: d/dx cos(2x) ")

x = np.linspace(0, 2*np.pi, 100)
y = -np.sin(x)*3
fig1, ax1 = plt.subplots(figsize=(6, 2))
ax1.plot(x, y, label='y = -np.sin(x)*3', color='#25792b')
fig1.set_facecolor('#edeccd')  
ax1.set_facecolor('#ffffff')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title("Grafica 1")
ax1.grid(True)
ax1.axhline(0, color='black',linewidth=1)  
ax1.axvline(0, color='black',linewidth=1)  


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)*2
fig2, ax2 = plt.subplots(figsize=(6, 2))
ax2.plot(x, y, label='y = np.sin(x)*2', color='#25792b')
fig2.set_facecolor('#edeccd')  
ax2.set_facecolor('#ffffff')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("Grafica 2")
ax2.grid(True)
ax2.axhline(0, color='black',linewidth=1)  
ax2.axvline(0, color='black',linewidth=1)


x = np.linspace(0, 2*np.pi, 100)
y = -np.sin(x)*2
fig3, ax3 = plt.subplots(figsize=(6,2))
ax3.plot(x, y, label='y = -np.sin(x)*2', color='#25792b')
fig3.set_facecolor('#edeccd')  
ax3.set_facecolor('#ffffff')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title("Grafica 3")
ax3.grid(True)
ax3.axhline(0, color='black',linewidth=1)  
ax3.axvline(0, color='black',linewidth=1)

st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
opciones5 = {
    "1": f"Grafica 1",
    "2": f"Grafica 2",
    "3": f"Grafica 3"
}
pre5 = st.radio(
    "¿Selecciona la grafica correcta a la funcion anterior?",
    options=list(opciones5.keys()),
    format_func=lambda x: opciones5[x]
)


rt1 = "2"
rt2 = "1"
rt3 = "1"
rt4 = "1"
rt5 = "3"

k = 0
mal = []
if st.button("Verificar"):
    if pre1 == rt1:
        k +=1
    else:
        mal.append("Pregunta 1")
    if pre2 == rt2:
        k +=1
    else:
        mal.append("Pregunta 2")
    if pre3 == rt3:
        k +=1
    else:
        mal.append("Pregunta 3")
    if pre4 == rt4:
        k +=1
    else:
        mal.append("Pregunta 4")
    if pre5 == rt5:
        k +=1
    else:
        mal.append("Pregunta 5")
    if k < 5:
        st.markdown(f"""
        Tu puntuacion fue de {k}/5
        Las que te quedaron mal fueron: {mal}
        """)
    else:
        st.markdown("Felicidades, sigue asi,")









