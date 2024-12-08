
import streamlit as st
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

st.title("Ejercicios Interactivos: Derivadas Trigonometricas")
st.markdown("A continuacion realizaremos ejemplos ayudandonos de los resultados obtenidos de las derivadas trigonometricas, nos sera muy util recordarlos: ")
with st.expander("Derivadas trigonometricas"):
    st.latex("sen(x) = cos(x)")
    st.latex("cos(x) = -sen(x)")
    st.latex("tan(x) = sec(x)^2")
    st.latex("cot(x) = -csc(x)^2")
    st.latex("sec(x) = sec(x)/tan(x)")
    st.latex("csc(x) = -csc(x)cot((x)")

st.markdown("¡Ahora practiquemos con estos ejercicios para obtener un hermoso 5 en ese parcial ^^!")

st.subheader("Ejercicio 1: Derivada de una funcion trigonometrica")
st.latex(r"f(x) = sin(x) + cos(x)")

opciones = {
    "1": r"f'(x) = cos(x) - sin(x)",
    "2": r"f'(x) = cos(x) + sin(x)",
    "3": r"f'(x) = sin(x) - cos(x)"
}
answer = "1"

respuesta = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones.keys()),
    format_func=lambda x: opciones[x]
)

if st.button("Verificar"):
    if respuesta == answer:
        st.success("Excelente, cada vez mas cerca de ese 5 ^^.")
    else:
        st.error("Vamos, tu puedes, intentalo de nuevo, revisa las reglas de derivacion si es necesario ^^")

st.subheader("Ejercicio 2: Derivemos esta funcion fraccionaria y miremos su grafica ^^")
st.latex(r"f(x) = \frac{\sec(x)}{\csc(x)}")

if st.checkbox("Mostrar simplificacion"):
    st.markdown("Sabemos que:")
    st.latex(r"\frac{sec(x)}{csc(x)} = tan(x)")
    st.markdown("Entonces, derivamos:")
    st.latex(r"f'(x) = sec^2(x)")

st.subheader("Grafica de las funciones")
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
t = np.tan(x)
t[np.abs(t) > 40] = np.nan
s = np.tan(x) ** 2

fig, ax = plt.subplots(figsize=(8, 4))
fig.set_facecolor('#edeccd')  
ax.set_facecolor('#ffffff')  
ax.plot(x, t, label=r"$f(x) = \tan(x)$", color="blue")
ax.plot(x, s, label=r"$f'(x) = \sec^2(x)$", color="#25792b")
ax.set_ylim(-10, 10)
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.legend()
ax.grid()
st.pyplot(fig)

st.subheader("Ejercicio 3: Deriva esta funcion tu mismo")
st.latex(r"f(x) = tan(x) + sec(x)")
 
opciones = {
    "1": r"f'(x) = sec^2(x)+sec(x)tan(x)",
    "2": r"f'(x) = sec^2(x)+sec(x)",
    "3": r"f'(x) = sec^2(x)−sec(x)tan(x)"
}

answer = "3"

respuesta = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones.keys()),
    format_func=lambda x: opciones[x]
)
if st.button("Verifiquemos^^"):
    if respuesta == answer:
        st.success("Excelente, cada vez mas cerca de ese 5 ^^.")
    else:
        st.error("Vamos, tu puedes, intentalo de nuevo, revisa las reglas de derivacion si es necesario ^^")

st.subheader("Ejercicio 4: Deriva esta funcion con un angulo todo rarito^^")
st.latex(r"f(x) = sen(3x^2)")

opciones = {
    "1": r"f'(x) = cos(3x^2)",
    "2": r"f'(x) = cos(6x)",
    "3": r"f'(x) = cos(3x^2)*6x"
}

answer = "3"

respuesta = st.radio(
    "¿Cual es la derivada correcta?",
    options=list(opciones.keys()),
    format_func=lambda x: opciones[x]
)
if st.button("Verifiquemos><"):
    if respuesta == answer:
        st.success("Excelente, cada vez mas cerca de ese 5 ^^.")
    else:
        st.error("Vamos, tu puedes, intentalo de nuevo, depronto sea util recordar la regla de la cadena.... ")

st.subheader("Ejercicio 5: Excelente, vas muy bien, ahora que tal este ¡CHALLENGE!")
st.latex(r"f(x) = e^{sen(cos(3x^2)})")

answ = {
    "1": r"f'(x)= 6x*e^(sen(cos(3x^2))*cos(cos(3x^2)*sen(3x^2)))",
    "2": r"f'(x)= -6x*cos(cos(3x^2)*sen(3x^2))",
    "3": r"f'(x)= -6x*e^(sen(cos(3x^2))*cos(cos(3x^2)*sen(3x^2))) "
}

rt = "3"

rtt = st.radio(
    "¿Cual es la derivada correcta???",
    options=list(answ.keys()),
    format_func=lambda x: answ[x]
)

if st.button("Verificar:3"):
    if rtt == rt:
         st.success("Excelente, cada vez mas cerca de ese 5 ^^.")
    else:
        st.error("Vamos, tu puedes, intentalo de nuevo, depronto sea util recordar la regla de la cadena.... ")

if st.checkbox("Mostrar proceso"):
    st.markdown("""Pasitos:

    Para este problema debemos usar:

    1. Las derivadas que ya conocemos
    2. Derivacion implicita
    3. Regla de la cadena
    4. Propiedades de los logaritmos

    Empezamos reescribiendo la funcion para una mejor notacion
    luego aplicamos Ln (logaritmo natural) a ambos lados de la funcion
    para bajar el exponente de la e, ya que es la funcion que nos interesa derivar:
    """)

    st.latex(r"y=e^{sen(cos(3x^2)})")
    st.latex(r"ln(y) = ln(e^{sen(cos(3x^2)})")
    st.latex(r"ln(y) = sen(cos(3x^2))")

    st.markdown("Ahora aplicamos el concepto de la derivada implicita y regla de la cadena donde sea necesario, y por ultimo despejamos dy/dx para obtener la derivada, recordando quien era y inicialmente: ")

    st.latex(r"\frac{d}{dx}(ln(y) = \frac{d}{dx}(sen(cos(3x^2))) ")
    st.latex(r"\frac{1}{y}\frac{dy}{dx} = cos(cos(3x^2)(-sen(3x^2)6x))")
    st.latex(r"\frac{dy}{dx} = -6xe^{sen(cos(3x^2))}cos(cos(3x^2)sen(3x^2))")

