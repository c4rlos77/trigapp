import streamlit as st
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 


st.title('Derivadas Trigonometricas')
st.markdown("""
En esta pagina encontraras la explicacion de las principales derivadas 
trigonometricas, con ejemplos y componentes interactivos.
""")

name = st.text_input('Antes de iniciar me gustaria saber cual es tu nombre:')
st.markdown(f"""Hola {name}! Espero que te encuentres muy bien. Como ya te mencione, aqui encontraras informacion sobre las derivadas trigonometricas. Empezaremos recordando que son las funciones trigonometricas. Espero te sea de ayuda.""")

x = np.linspace(-np.pi, np.pi, 1000) 

s = np.sin(x)
c = np.cos(x)

t = np.tan(x)
t[np.abs(t) > 10] = np.nan  # restringe los valores indeterminados
ct = 1 / np.tan(x)
ct[np.abs(ct) > 10] = np.nan  
sc = 1 / np.cos(x)
sc[np.abs(sc) > 10] = np.nan  
cs = 1 / np.sin(x)
cs[np.abs(cs) > 10] = np.nan  

fig, ax = plt.subplots(figsize=(16, 9))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')  

ax.plot(x, s, label="Seno", color="black", linestyle="-")
ax.plot(x, c, label="Coseno", color="red", linestyle="-")
ax.plot(x, t, label="Tangente", color="blue", linestyle="--")
ax.plot(x, ct, label="Cotangente", color="yellow", linestyle="--")
ax.plot(x, sc, label="Secante", color="green", linestyle=":")
ax.plot(x, cs, label="Cosecante", color="orange", linestyle=":")

ax.set_title("Funciones Trigonometricas")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.axhline(0, color='black', linewidth=0.5)  
ax.axvline(0, color='black', linewidth=0.5)  
ax.set_ylim(-3, 3)  
ax.legend()
ax.grid()
st.pyplot(fig)






