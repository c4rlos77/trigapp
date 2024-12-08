import streamlit as st

st.markdown("<h1 style='text-align: center; color: #000000;'>Mi Presentación Personal</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://scontent.fbga1-3.fna.fbcdn.net/v/t39.30808-6/465027005_8474547919308693_5979528301396813541_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeGqIwIVkRfSHJ49oFlx-j6sH2VxEHUpkmYfZXEQdSmSZs56r-hb-vWcnart9DRICtDfIqFIC08V-Jj_L3aoC80a&_nc_ohc=LmGIEmLd4VUQ7kNvgFYLfuc&_nc_zt=23&_nc_ht=scontent.fbga1-3.fna&_nc_gid=Ah2fGnqypRdWKZKeIzklcnS&oh=00_AYAS2_D3I-CtvVTaJ3FQZMqNnf5mnYwTqJ-nNyDTOVz-xw&oe=675B7A5A", caption="Holi, soy Carlos ")

with col2:
    st.markdown("""
    Soy estudiante de Matemáticas Puras de la **Universidad Industrial de Santander (UIS)**.  
    Desde mi primer semestre, he estado explorando cómo el conocimiento matemático puede abrir
    puertas a nuevas formas de entender el mundo.
    """)
    st.markdown("""
    Mi interés por las matemáticas va más allá del aula: disfruto investigando temas complejos,
    jugando ajedrez y manteniéndome activo con el deporte.
    """)

st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.markdown("<h2 style='text-align: center; color: #000000;'>Mis intereses</h2>", unsafe_allow_html=True)
    st.write("""
    Mis intereses abarcan tanto los aspectos teóricos como prácticos de las matemáticas.  
    Por ahora, siento una gran afinidad por **Algebra lineal** y **Calculo**, pero me entusiasma
    seguir descubriendo más ramas matemáticas que me ayuden a crecer como científico.
    """)

st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    st.markdown("<h2 style='text-align: center; color: #000000;'>Programación I</h2>", unsafe_allow_html=True)
    st.write("""
    Este curso me ha permitido desarrollar habilidades en **pensamiento lógico** y aprender a usar herramientas computacionales en el lenguaje Python. Considero que estas habilidades serán esenciales para futuros desafíos académicos y profesionales.
    """)
    if st.button("Ver proyectos realizados"):
        st.write("Durante el desarrollo de todo el curso, he creado bloques de código para resolver problemas específicos, como desafíos matemáticos, lógicos y de análisis de datos, entre otros. El único proyecto grande, por así decirlo, es la página que acabas de ver. Sin embargo, me interesa adquirir más proyectos que pongan a prueba mis conocimientos y habilidades lógicas.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Gracias por visitar mi presentación 😊</h3>", unsafe_allow_html=True)
if st.button("Conectar conmigo"):
    st.write("¡Puedes contactarme en [erikonta77@gmail.com]!")
