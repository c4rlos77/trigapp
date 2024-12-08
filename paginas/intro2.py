import streamlit as st
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 
import math

st.title("Derivadas Trigonométricas")
st.markdown("""
Las derivadas trigonométricas son el resultado de aplicar las reglas de derivación a las funciones trigonométricas (como seno, coseno, tangente, etc.). Estas derivadas son fundamentales en cálculo diferencial, ya que las funciones trigonométricas aparecen frecuentemente en la resolución de problemas de física, ingeniería y otros campos.

A continuación, explicamos cómo derivar las funciones trigonométricas principales. Antes de comenzar, recordemos una identidad muy importante y unos límites especiales que serán útiles para desarrollar las derivadas trigonométricas:
""")




# seno
st.header("Derivada de sen(x)")
st.markdown("Primero, reemplazamos la función ( sen(x) ) en la definición formal de derivada y simplificamos para eliminar la indeterminación:")
st.latex(r"\lim_{h \to 0} \frac{sen(x+h) - sen(x)}{h} = \lim_{h \to 0} \frac{sen(x)cos(h) + sen(h)cos(x) - sen(x)}{h}")
st.markdown("Factorizando y utilizando los límites especiales:")
st.latex(r"\lim_{h \to 0} \frac{-sen(x)(1 - cos(h))}{h} + \frac{sen(h)cos(x)}{h} = cos(x)")

#deslizador 
st.slider("Selecciona un ángulo x para evaluar sen'(x)", 0, 360, 45, key="sen_slider")
angulo = st.session_state.sen_slider
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: cos({angulo}) = {round(math.cos(math.radians(angulo)), 2)}")

#grafica del deslizador 
x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.plot(x, y, label='y = math.cos(math.radians(angulo))', color='#25792b')
ax.scatter([math.radians(angulo)], [math.cos(math.radians(angulo))])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada del Seno')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1)  
st.pyplot(fig)



# coseno 
st.header("Derivada de  cos(x) ")
st.markdown("Siguiendo el mismo proceso que con  sen(x) :")
st.latex(r"\lim_{h \to 0} \frac{cos(x+h) - cos(x)}{h} = \lim_{h \to 0} \frac{cos(x)cos(h) - sen(x)sen(h) - cos(x)}{h}")
st.markdown("Simplificando y utilizando los límites especiales:")
st.latex(r"\lim_{h \to 0} \frac{cos(x)(1 - cos(h))}{h} - \frac{sen(x)sen(h)}{h} = -sen(x)")


# deslizador 
x =  sp.symbols('x')
func = sp.cos(x)
funcion = func.diff(x)
st.slider("Selecciona un ángulo x para evaluar cos'(x)", 0, 360, 45, key="cos_slider")
angulo = st.session_state.cos_slider
m = funcion.subs(x, math.radians(angulo))
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: -sen({angulo}) = {round(m,2)}")
# grafica 

x = np.linspace(0, 2*np.pi, 100)
y = -np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label='y = -np.sin(x)', color='#25792b')
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.scatter([math.radians(angulo)], [-np.sin(math.radians(angulo))])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada del coseno ')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1)  
st.pyplot(fig)
######
st.divider()

st.markdown("**A partir de aquí, derivaremos las demás funciones trigonométricas utilizando las derivadas ya obtenidas y las reglas de derivación.**")

# tangente
st.header("Derivada de  tan(x) ")
st.markdown("Reescribimos la función en términos de  sen(x)  y cos(x) :")
st.latex(r"tan(x) = \frac{sen(x)}{cos(x)}")
st.markdown("Aplicando la regla del cociente:")
st.latex(r"\frac{d}{dx}\left(\frac{sen(x)}{cos(x)}\right) = \frac{cos(x) \cdot sen'(x) - sen(x) \cdot cos'(x)}{cos^2(x)}")
st.markdown("Sustituyendo las derivadas de ( sen(x) ) y ( cos(x) ):")
st.latex(r"\frac{cos(x)cos(x) + sen(x)sen(x)}{cos^2(x)}")
st.markdown("Utilizando la identidad ( sen^2(x) + cos^2(x) = 1 ):")
st.latex(r"\frac{1}{cos^2(x)} = sec^2(x)")

# deslizador 
x =  sp.symbols('x')
func = sp.tan(x)
funcion = func.diff(x)
st.slider("Selecciona un ángulo x para evaluar cos'(x)", 0, 360, 45, key="tan_slider")
angulo = st.session_state.tan_slider
m = funcion.subs(x, math.radians(angulo))
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: sec^2({angulo}) = {round(m,2)}")
# grafica 

x = np.linspace(0, 6, 500)
y = (1/np.cos(x))**2
y[np.abs(y) > 200] = np.nan  

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.plot(x, y, label='y = (1/np.cos(x))**2', color='#25792b')
ax.scatter([math.radians(angulo)], [(1/np.cos(math.radians(angulo)))**2])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada de la tangente')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1)  
ax.set_ylim(-1, 50)
st.pyplot(fig)

# cotangente
st.header("Derivada de  cot(x) ")
st.markdown("Reescribimos la función en términos de  sen(x)  y  cos(x) :")
st.latex(r"cot(x) = \frac{cos(x)}{sen(x)}")
st.markdown("Aplicando la regla del cociente:")
st.latex(r"\frac{d}{dx}\left(\frac{cos(x)}{sen(x)}\right) = \frac{sen(x) \cdot cos'(x) - cos(x) \cdot sen'(x)}{sen^2(x)}")
st.markdown("Sustituyendo las derivadas de  sen(x)  y  cos(x) :")
st.latex(r"\frac{-sen(x)cos(x) - cos(x)cos(x)}{sen^2(x)}")
st.markdown("Factorizando y simplificando:")
st.latex(r"-\frac{1}{sen^2(x)} = -csc^2(x)")

# deslizador 
x =  sp.symbols('x')
func = sp.cot(x)
funcion = func.diff(x)
st.slider("Selecciona un ángulo x para evaluar cos'(x)", 0, 360, 45, key="cot_slider")
angulo = st.session_state.cot_slider
m = funcion.subs(x, math.radians(angulo))
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: -csc^2({angulo}) = {round(m,2)}")
# grafica 

x = np.linspace(-6, 6, 500)
y = (1/-np.sin(x))**2
y[np.abs(y) > 200] = np.nan  

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.plot(x, y, label='y = (1/np.cos(x))**2', color='#25792b')
ax.scatter([math.radians(angulo)], [(1/-np.sin(math.radians(angulo)))**2])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada de cotangente')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1) 
ax.set_ylim(-1, 20) 
st.pyplot(fig)



# sec
st.header("Derivada de  sec(x) ")
st.markdown("Reescribimos la función en términos de  cos(x) :")
st.latex(r"sec(x) = \frac{1}{cos(x)}")
st.markdown("Aplicando la regla de la derivada de recíprocos:")
st.latex(r"sec'(x) = \frac{0 \cdot cos(x) - 1 \cdot (-sen(x))}{cos^2(x)}")
st.latex(r"sec'(x) = \frac{sen(x)}{cos^2(x)} = sec(x)tan(x)")

# deslizador 
x =  sp.symbols('x')
func = sp.sec(x)
funcion = func.diff(x)
st.slider("Selecciona un ángulo x para evaluar cos'(x)", 0, 360, 45, key="sec_slider")
angulo = st.session_state.sec_slider
m = funcion.subs(x, math.radians(angulo))
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: sec({angulo})tan({angulo}) = {round(m,2)}")
# grafica 

x = np.linspace(-6, 6, 500)
y = np.sin(x)/(np.cos(x)**2)
y[np.abs(y) > 200] = np.nan  

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.plot(x, y, label='y = np.sin(x)/(np.cos(x)**2)', color='#25792b')
ax.scatter([math.radians(angulo)], [np.sin(math.radians(angulo))/(np.cos(math.radians(angulo))**2)])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada de secante')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1)  
ax.set_ylim(-20, 20)
st.pyplot(fig)

# csc
st.header("Derivada de  csc(x) ")
st.markdown("Reescribimos la función en términos de sen(x) :")
st.latex(r"csc(x) = \frac{1}{sen(x)}")
st.markdown("Aplicando la regla de la derivada de recíprocos:")
st.latex(r"csc'(x) = \frac{0 \cdot sen(x) - 1 \cdot cos(x)}{sen^2(x)}")
st.latex(r"csc'(x) = -\frac{cos(x)}{sen^2(x)} = -csc(x)cot(x)")

# deslizador 
x =  sp.symbols('x')
func = sp.csc(x)
funcion = func.diff(x)
st.slider("Selecciona un ángulo x para evaluar cos'(x)", 0, 360, 45, key="csc_slider")
angulo = st.session_state.csc_slider
m = funcion.subs(x, math.radians(angulo))
st.write(f"Para x = {angulo} grados, la derivada es aproximadamente: -csc({angulo})cot({angulo}) = {round(m,2)}")
# grafica 

x = np.linspace(-0.5, 4, 500)
y = (1/-np.cos(x))*(np.cos(x)/(np.sin(x)))
y[np.abs(y) > 40] = np.nan  

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')
ax.plot(x, y, color='#25792b')
ax.scatter([math.radians(angulo)], [(1/-np.cos(math.radians(angulo)))*(np.cos(math.radians(angulo))/np.sin(math.radians(angulo)))])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Derivada de cosecante')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)  
ax.axvline(0, color='black',linewidth=1)  
ax.set_ylim(-20, 20)
st.pyplot(fig)

st.divider()

with st.expander(" Karl Weierstrass (Teoría de Límites y Continuidad)"):
    st.markdown("""
    Karl Weierstrass (1815-1897) fue un matemático alemán que desempeñó un papel crucial en el desarrollo del análisis real, especialmente en la formalización de conceptos como continuidad y derivadas. Aunque Cauchy fue fundamental para la formalización de las ideas de derivada y límite, Weierstrass proporcionó una mayor claridad y rigurosidad.

    En sus estudios, Weierstrass introdujo el concepto de función continua pero no derivable, lo que amplió el campo de las funciones analíticas y ayudó a refinar las condiciones bajo las cuales las derivadas podrían ser aplicadas. Su trabajo proporcionó las bases para la comprensión de las funciones en términos de límites y continuidad, conceptos que son esenciales para las derivadas, especialmente cuando se aplican a funciones más complejas.
    """)
with st.expander(" Joseph Fourier (Series de Fourier y Aplicaciones Trigonométricas)"):
    st.markdown("""
    Jean-Baptiste Joseph Fourier (1768-1830) fue un matemático y físico francés conocido principalmente por desarrollar la transformada de Fourier, una herramienta que permite representar funciones periódicas como una suma infinita de funciones trigonométricas. Esta idea fue revolucionaria en el análisis de fenómenos periódicos, como el calor, y abrió el camino para el análisis de señales.

    Fourier utilizó las funciones trigonométricas para descomponer funciones complicadas en componentes sinusoidales. Esta descomposición sigue siendo esencial en áreas como la ingeniería eléctrica, la física y las telecomunicaciones. Las series de Fourier son fundamentales para comprender cómo las derivadas pueden aplicarse a funciones periódicas.
    """)




