import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.patches as patches
import pandas as pd 


st.title("Identidades trigonometricas")

st.markdown("Las identidades trigonométricas son ecuaciones que involucran funciones trigonométricas (como seno, coseno, tangente, etc.) que son siempre verdaderas para cualquier valor del ángulo, dentro de su dominio. Estas identidades son herramientas matemáticas fundamentales que permiten simplificar expresiones trigonométricas y resolver problemas en diferentes áreas de las matemáticas, especialmente en el análisis, la geometría y la física.")

with st.expander("Identidades Trigonométricas"):
    st.markdown("Aquí encontrarás las identidades trigonométricas fundamentales y cómo las funciones tangente, cotangente, secante y cosecante se expresan en términos de seno y coseno.")
    st.latex(r"tan(x) = \frac{sen(x)}{cos(x)}")
    st.latex(r"cot(x) = \frac{cos(x)}{sen(x)}")
    st.latex(r"sec(x) = \frac{1}{cos(x)}")
    st.latex(r"csc(x) = \frac{1}{sen(x)}")
    st.latex(r"sen^2(x) + cos^2(x) = 1")
    st.latex(r"sen(A \pm B) = sen(A) \cdot cos(B) \pm cos(A) \cdot sen(B)")
    st.latex(r"cos(A \pm B) = cos(A) \cdot cos(B) \mp sen(A) \cdot sen(B)")


st.title("Limites especiales trigonometricos")

st.markdown("Los límites especiales trigonométricos son valores límite que resultan ser fundamentales cuando se estudian funciones trigonométricas en el cálculo. Estos límites se utilizan para entender el comportamiento de funciones como el seno, el coseno y la tangente cuando el ángulo se acerca a ciertos valores, como 0.")


a1, a2 = st.columns(2)
with a1:
    st.latex(r"\lim_{h \to 0} \frac{sen(h)}{h} = 1")

with a2:
    x = np.linspace(-np.pi, np.pi, 100)  
    a = np.sin(x)  
    y = a/x

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='blue')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("Grafica limite del sen(x)")
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)

a1, a2 = st.columns(2)
with a1:
    st.latex(r"\lim_{h \to 0} \frac{1 - cos(h)}{h} = 0")

with a2:
    x = np.linspace(-np.pi, np.pi, 100)  
    a = np.cos(x)  
    y = (1-a)/x

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.set_facecolor('#edeccd')  
    ax.set_facecolor('#ffffff')  
    ax.plot(x, y, color='blue')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Gráfica del limite del cos(x)')
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1)  
    st.pyplot(fig)



    



st.markdown("""Estos límites son esenciales en el cálculo diferencial e integral, pues se utilizan para encontrar derivadas de funciones trigonométricas y resolver problemas de continuidad, entre otros.

En resumen, las identidades trigonométricas simplifican y transforman expresiones, mientras que los límites especiales son clave para el análisis del comportamiento de funciones trigonométricas en el cálculo.""")

st.divider()
with st.expander("Leonhard Euler (Funciones Trigonométricas e Identidades)"):
    st.markdown("""
    Leonhard Euler (1707-1783) fue uno de los matemáticos más prolíficos y fundamentales en el desarrollo de la matemática moderna. Con respecto a las funciones trigonométricas, Euler las abordó desde una perspectiva algebraica y analítica.

    Euler introdujo las relaciones fundamentales entre las funciones trigonométricas y el número complejo. Su fórmula:
    """)
    st.latex(r"e^{ix} = cos(x) + isen(x)")
    st.markdown("""
    conocida como la fórmula de Euler, ha sido crucial para conectar las funciones trigonométricas con la teoría de números complejos, ampliando enormemente el campo de estudio de estas funciones.

    En sus trabajos también ayudó a simplificar las identidades trigonométricas y las aplicaciones de estas funciones en ecuaciones diferenciales, lo que permitió el desarrollo de la transformada de Fourier.
    
    """)