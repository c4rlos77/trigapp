
import streamlit as st
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 
import math
st.title("Funciones trigonometricas")
a1, a2 = st.columns(2)
with a1:
    st.markdown("""Las funciones trigonometricas son herramientas fundamentales en matematicas, especialmente en geometria y analisis, que relacionan los angulos de un triangulo rectangulo con las longitudes de sus lados. Estas funciones tambien se extienden mas alla de los triangulos, aplicandose a circulos y ondas, pero a continuacion te explico como funcionan en el caso de un triangulo rectangulo:""")
with a2:
   st.image("https://w7.pngwing.com/pngs/208/260/png-transparent-right-triangle-trigonometry-geometry-triangle-angle-text-rectangle.png")
   h = sp.symbols("Hipotenusa")
   cop = sp.symbols("Cateto opuesto")
   cad = sp.symbols("Cateto adyacente")



#seno 

a1, a2 = st.columns(2)
with a1:
    st.header("Seno")
    st.markdown("Seno (sen): Es la relacion entre el cateto opuesto al angulo y la h (el lado mas largo del triangulo).")
    st.latex(r"sen(θ) = \frac{cateto opuesto}{hipotenusa}")
with a2:
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('seno')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)

#coseno
c1, c2 = st.columns(2)
with c1:
    st.header("Coseno")
    st.markdown("Coseno (cos): Es la relacion entre el cateto adyacente al angulo y la h.")
    st.latex(r"cos(θ) = \frac{cateto adyacente}{hipotenusa}")
with c2:
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Coseno')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)

# tangente 
c1, c2 = st.columns(2)
with c1:
    st.header("Tangente")
    st.markdown("Tangente (tan): Es la relacion entre el cateto opuesto y el cateto adyacente.")
    st.latex(r"tan(θ) = \frac{cateto opuesto}{cateto adyacente}")
with c2:
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)/np.cos(x)
    y[np.abs(y) > 10] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Tangente')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)
# cotangente 
c1, c2 = st.columns(2)
with c1:
    st.header("Cotangente")
    st.markdown("Cotangente (cot): Es la inversa de la tangente, es decir, la relacion entre el cateto adyacente y el cateto opuesto")
    st.latex(r"cot(θ) = \frac{cateto adyacente}{cateto opuesto}")
with c2:
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)/np.sin(x)
    y[np.abs(y) > 10] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Cotangente')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)

# secante 
c1, c2 = st.columns(2)
with c1:
    st.header("Secante")
    st.markdown("Secante (sec): Es la inversa del coseno, es decir, la relacion entre la h y el cateto adyacente.")
    st.latex(r"sec(θ) = \frac{hipotenusa}{cateto adyacente}")
with c2:
    x = np.linspace(0, 2*np.pi, 100)
    y = 1/np.cos(x)
    y[np.abs(y) > 10] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Secante')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)
#cosecante 
c1, c2 = st.columns(2)
with c1:
    st.header("Cosecante")
    st.markdown("Cosecante (csc): Es la inversa del seno, es decir, la relacion entre la h y el cateto opuesto.")
    st.latex(r"csc(θ) = \frac{hipotenusa}{cateto opuesto}")
with c2:
    x = np.linspace(0, 2*np.pi, 100)
    y = 1/np.sin(x)
    y[np.abs(y) > 10] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='#25792b')
   
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Cosecante')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)

st.divider()
with st.expander("El 'Padre de las Funciones Trigonométricas' Hiparco de Nicea"):
    st.markdown("""
    El título de "padre de las funciones trigonométricas" generalmente se atribuye a Hiparco de Nicea (190 a.C. - 120 a.C.), un astrónomo y matemático griego que desarrolló el primer tabla trigonométrica para ayudar en la resolución de problemas astronómicos.

    Hiparco utilizó las funciones trigonométricas en el contexto de los triángulos rectángulos. Aunque no usaba los términos modernos, desarrolló métodos para relacionar los ángulos con las longitudes de los lados de los triángulos. Este tipo de relaciones se convirtió en la base de lo que hoy conocemos como las funciones seno, coseno y tangente.

    Hiparco fue también pionero en la construcción de tablas trigonométricas, las cuales servían para calcular los ángulos y lados de los triángulos en astronomía. Esto fue fundamental para el desarrollo posterior de la trigonometría.
    """)
    

