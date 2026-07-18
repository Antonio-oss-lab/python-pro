# ==========================
# IMPORTAR LIBRERÍAS
# ==========================
import speech_recognition as sr
from difflib import SequenceMatcher

# ==========================
# CONFIGURACIÓN
# ==========================
max_errors = 3
score = 0
errors = 0

# ==========================
# FUNCIÓN PARA ESCUCHAR VOZ
# ==========================
def escuchar(lenguaje):
    reconocedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙 Habla ahora...")
        reconocedor.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = reconocedor.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("⏱ No se detectó voz.")
            return ""

    try:
        texto = reconocedor.recognize_google(audio, language=lenguaje)
        print("🗣 Escuché:", texto)
        return texto.lower().strip()

    except sr.UnknownValueError:
        print("❌ No entendí lo que dijiste.")
        return ""

    except sr.RequestError:
        print("⚠ Error con el servicio de Google.")
        return ""

# ==========================
# FUNCIÓN PARA COMPARAR RESPUESTAS
# ==========================
def parecido(texto, respuesta):
    return SequenceMatcher(None, texto, respuesta.lower()).ratio()

# ==========================
# PREGUNTAS POR IDIOMA Y NIVEL
# ==========================
idiomas = {

    "ingles": {
        "lenguaje": "en-US",

        "facil": {
            "¿Cómo se dice 'perro' en inglés?": "dog",
            "¿Cómo se dice 'gato' en inglés?": "cat",
            "¿Cómo se dice 'hola' en inglés?": "hello"
        },

        "medio": {
            "¿Cuál es el pasado de go?": "went",
            "¿Cuál es el pasado de eat?": "ate",
            "¿Cuál es el pasado de see?": "saw"
        },

        "dificil": {
            "¿Cuál es el pasado de run?": "ran",
            "¿Cuál es el pasado de write?": "wrote",
            "¿Cuál es el pasado de speak?": "spoke"
        }
    },

    "frances": {
        "lenguaje": "fr-FR",

        "facil": {
            "¿Cómo se dice 'hola' en francés?": "bonjour",
            "¿Cómo se dice 'gracias' en francés?": "merci"
        },

        "medio": {
            "¿Cómo se dice 'adiós' en francés?": "au revoir",
            "¿Cómo se dice 'agua' en francés?": "eau"
        },

        "dificil": {
            "¿Cómo se dice 'biblioteca' en francés?": "bibliothèque",
            "¿Cómo se dice 'computadora' en francés?": "ordinateur"
        }
    },

    "Italiano": {
        "lenguaje": "it-IT",

        "facil": {
            "¿Cómo se dice 'hola' en italiano?": "ciao",
            "¿Cómo se dice 'gracias' en italiano?": "grazie"
        },

        "medio": {
            "¿Cómo se dice 'adiós' en italiano?": "arrivederci",
            "¿Cómo se dice 'agua' en italiano?": "acqua"
        },

        "dificil": {
            "¿Cómo se dice 'biblioteca' en italiano?": "biblioteca",
            "¿Cómo se dice 'computadora' en italiano?": "computer"
        }
    },

    "aleman": {
        "lenguaje": "de-DE",

        "facil": {
            "¿Cómo se dice 'hola' en alemán?": "hallo",
            "¿Cómo se dice 'gracias' en alemán?": "danke"
        },

        "medio": {
            "¿Cómo se dice 'adiós' en alemán?": "auf wiedersehen",
            "¿Cómo se dice 'agua' en alemán?": "wasser"
        },

        "dificil": {
            "¿Cómo se dice 'biblioteca' en alemán?": "bibliothek",
            "¿Cómo se dice 'computadora' en alemán?": "computer"
        }
    }
}

# ==========================
# INICIO
# ==========================
print("🎮 QUIZ POR VOZ")
print()

# ==========================
# ELEGIR IDIOMA
# ==========================
print("Idiomas disponibles:")
for idioma in idiomas:
    print("-", idioma)

idioma = input("\nElige un idioma: ").lower().strip()

while idioma not in idiomas:
    print("Idioma no válido.")
    idioma = input("Elige un idioma: ").lower().strip()

# ==========================
# ELEGIR NIVEL
# ==========================
print("\nNiveles disponibles:")
for nivel in idiomas[idioma]:
    if nivel != "lenguaje":
        print("-", nivel)

nivel = input("\nElige un nivel: ").lower().strip()

while nivel not in idiomas[idioma] or nivel == "lenguaje":
    print("Nivel no válido.")
    nivel = input("Elige un nivel: ").lower().strip()

# ==========================
# RESUMEN
# ==========================
lenguaje = idiomas[idioma]["lenguaje"]
quiz = idiomas[idioma][nivel]

print("\n==========================")
print("Idioma:", idioma.capitalize())
print("Nivel:", nivel.capitalize())
print("==========================")

# ==========================
# BUCLE PRINCIPAL
# ==========================
for pregunta, respuesta in quiz.items():

    print("\n❓", pregunta)
    texto = escuchar(lenguaje)

    if texto == "":
        errors += 1
        print("⚠ Se contará como error.")
        print(f"Errores: {errors}/{max_errors}")

    elif parecido(texto, respuesta) >= 0.80:
        score += 1
        print("✅ ¡Correcto!")
        print("⭐ Puntaje:", score)

    else:
        errors += 1
        print("❌ Incorrecto.")
        print("✔ Respuesta correcta:", respuesta)
        print(f"⚠ Errores: {errors}/{max_errors}")

    if errors >= max_errors:
        print("\n💀 GAME OVER")
        break

# ==========================
# RESULTADOS
# ==========================
print("\n==========================")
print("🏁 FIN DEL JUEGO")
print("==========================")
print("⭐ Puntaje:", score)
print("❌ Errores:", errors)
print("Gracias por jugar.")