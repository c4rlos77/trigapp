import streamlit as st

st.title("La Derivada")
st.markdown("""
En el estudio de las matematicas, especialmente en el calculo, una derivada es una herramienta fundamental que nos ayuda a comprender como cambian las funciones. 
De manera intuitiva, la derivada nos indica la tasa de cambio de una funcion en un punto especifico. En otras palabras, nos dice que tan rapido o lento cambia una variable con respecto a otra. 
Por ejemplo, si tenemos una funcion que describe el movimiento de un objeto, la derivada nos dira que tan rapido se mueve el objeto en un instante dado.
""")

st.header("Definicion Formal de Derivada")
st.markdown("""
La derivada de una funcion ( f(x) ) en un punto ( x = a ) se define como el limite de la tasa de cambio promedio de la funcion cuando el intervalo se hace muy pequeno. 
La derivada de ( f(x) ) en el punto ( a ), que se denota como ( f'(a) ), se define como el siguiente limite, si la funcion es continua en ( x = a ):
""")
st.latex(r"\displaystyle \lim_{h \to 0} \frac{f(a+h)-f(a)}{h}")

st.header("Metodos de Derivacion")
st.markdown("""
Para resolver derivadas de manera mas facil, es importante conocer algunas reglas que nos ayudan a hacer el trabajo mas rapido. Aqui te muestro algunas de las reglas mas comunes:
""")

st.subheader("Derivada de una constante:")
st.markdown("""
Si ( f(x) = c ), donde ( c ) es una constante, la derivada de esa constante es igual a cero, es decir:
""")
st.latex(r"f'(x) = 0")
st.markdown("""
Esto pasa porque una constante no cambia, y como la derivada nos mide el cambio, el cambio es cero.
""")

st.subheader("Regla de la suma:")
st.markdown("""
Si tenemos la suma de dos funciones, es decir, ( f(x) = g(x) + h(x) ), la derivada de esta suma es simplemente la suma de las derivadas de cada funcion:
""")
st.latex(r"f'(x) = g'(x) + h'(x)")
st.markdown("""
La derivada de una suma es igual a la suma de las derivadas. Es muy sencillo, ya que solo derivamos cada termino por separado.
""")

st.subheader("Regla del producto:")
st.markdown("""
Si ( f(x) = g(x) \cdot h(x) ), es decir, tenemos dos funciones multiplicadas, la derivada de esta multiplicacion se calcula con la siguiente formula:
""")
st.latex(r"f'(x) = g'(x) \cdot h(x) + g(x) \cdot h'(x)")
st.markdown("""
Esta regla es util cuando tenemos funciones multiplicadas. Lo que hacemos es derivar cada una por separado y luego aplicar la formula para combinarlas.
""")

st.subheader("Regla del cociente:")
st.markdown("""
Si ( f(x) = g(x)/h(x) ), es decir, una funcion que es un cociente de dos funciones, la derivada se calcula de la siguiente manera:
""")
st.latex(r"f'(x) = \frac{h(x) \cdot g'(x) - h'(x) \cdot g(x)}{(h(x))^2}")
st.markdown("""
Esta regla es util cuando tenemos funciones divididas. Nos dice como derivar el cociente de dos funciones de forma rapida.
""")

st.subheader("Regla de la Cadena:")
st.markdown("""
La Regla de la Cadena es una tecnica para derivar la composicion de funciones. Si tenemos una funcion compuesta f(x) = g(h(x)), 
donde (g) y (h) son funciones diferenciables, la derivada de f(x) se calcula de la siguiente manera:
""")
st.latex(r"f'(x) = g'(h(x)) \cdot h'(x)")
st.markdown("""
Esta regla es demasiado util cuando queremos derivar funciones que son composiciones de otras
""")

st.subheader("Derivacion Implicita:")

st.markdown("""
La Derivacion Implicita es un metodo que se utiliza cuando una ecuacion involucra dos o mas variables y no se puede despejar explicitamente 
una de ellas en terminos de la otra. Por ejemplo, si tenemos una ecuacion como (F(x,y) = 0), podemos derivar implicitamente respecto a (x), 
considerando (y) como una funcion de (x).
""")

st.latex(r"\frac{d}{dx}\left( F(x, y) = 0 \right)")
st.markdown("En la practica es mas lindo...")

st.divider()
st.markdown("""
Las derivadas son una herramienta muy importante en el calculo, y saber como derivar funciones usando las reglas basicas es fundamental para entender como cambian las funciones. 
Con las reglas de la constante, la suma, el producto, el cociente puedes derivar muchas funciones de manera rapida y sencilla.
""")
