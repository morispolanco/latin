import streamlit as st
import random
from cltk import NLP
from cltk.languages import Latin

# Configuración de la aplicación
st.title("Historias en latín con análisis gramatical")

# Función para generar una historia en latín
def generar_historia():
    # Lista de oraciones en latín
    oraciones = [
        "Gallia est omnis divisa in partes tres.",
        "Hic sunt dracones.",
        "Veni, Vidi, Vici.",
        # Agrega más oraciones...
    ]
    
    # Selecciona una oración al azar
    oracion = random.choice(oraciones)
    
    return oracion

# Función para realizar el análisis gramatical
def analisis_gramatical(oracion):
    # Crea un objeto NLP para latín
    nlp = NLP(language="lat")
    
    # Realiza el análisis gramatical
    analisis = nlp.analyze(oracion)
    
    return analisis

# Interfaz de usuario
st.write("Seleccione una opción:")
opciones = ["Generar historia", "Analizar oración"]
opcion = st.selectbox("", opciones)

if opcion == "Generar historia":
    oracion = generar_historia()
    st.write("Historia en latín:")
    st.write(oracion)
elif opcion == "Analizar oración":
    oracion = st.text_input("Ingrese una oración en latín:")
    if oracion:
        analisis = analisis_gramatical(oracion)
        st.write("Análisis gramatical:")
        st.write(analisis)

# Ejecuta la aplicación
if __name__ == "__main__":
    st.run()
