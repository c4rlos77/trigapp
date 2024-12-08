import streamlit as st

home = st.Page('paginas/inicio.py', title='Página Principal', icon="🏠", default=True)

intro_functrig = st.Page('paginas/intro_functrig.py', title="Introducción a las Funciones Trigonométricas", icon="🔢")
intro_ident = st.Page("paginas/intro_ident.py", title="Identidades y Límites Especiales", icon="🔗")
intro_deriv = st.Page("paginas/intro_deriv.py", title="Introducción a las Derivadas", icon="📐")

derivadastrig = st.Page("paginas/intro2.py", title="Derivadas Trigonométricas", icon="🧮")
ejercicios = st.Page('paginas/inter.py', title='Ejercicios Prácticos', icon="✍️")

quiz = st.Page("paginas/quiz.py", title="Evalúa tu Conocimiento", icon="📝")

presentacion = st.Page("paginas/presentacion.py", title="Sobre Mí", icon="👤")

pg = st.navigation({
    "Inicio": [home, intro_functrig, intro_ident, intro_deriv],
    "Derivadas Trigonométricas": [derivadastrig, ejercicios, quiz],
    "Sobre Mí": [presentacion]
})

pg.run()