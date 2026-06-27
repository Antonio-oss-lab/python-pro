# Importa librerías necesarias
# sounddevice: permite grabar audio desde el micrófono
import sounddevice as sd

# scipy.io.wavfile: permite guardar archivos de audio en formato .wav
import scipy.io.wavfile as wav

# speech_recognition: convierte audio en texto usando reconocimiento de voz
import speech_recognition as sr

# googletrans: traduce texto entre idiomas
from googletrans import Translator

preguntas = {
    "¿Cuál es el pasado de go?": "went",
    "¿Cuál es el pasado de eat?": "ate",
    "¿Cuál es el pasado de see?": "saw",
    "¿Como se dice 'perro' en inglés?": "dog",
    "¿como se dice 'gato' en inglés?": "cat",
    "¿como se dice 'hola' en inglés?": "hello",
    "¿cual es el pasado de 'run'?": "ran",
    "¿cual es el pasado de 'write'?": "wrote",

}

# Duración de la grabación en segundos
duration = 5

# Frecuencia de muestreo del audio (calidad del sonido)
# 44100 Hz = calidad tipo CD
sample_rate = 44100

for pregunta, respuesta in preguntas.items():
    # Mensaje indicando que el usuario debe hablar
    print("🎤 Pregunta:", pregunta)
    print("🎙 Habla ahora...")

    # Graba audio desde el micrófono:
    # - duration * sample_rate = cantidad total de muestras
    # - channels=1 = audio mono (un solo canal)
    # - dtype="int16" = formato estándar de audio WAV
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    # Espera a que termine la grabación antes de continuar
    sd.wait()

    # Guarda el audio grabado en un archivo WAV llamado "output.wav"
    wav.write("output.wav", sample_rate, recording)

    # Mensaje informando que empieza el reconocimiento de voz
    print("✅ Grabación completa, reconociendo...")


    # Crea el objeto reconocedor de voz
    recognizer = sr.Recognizer()


    # Abre el archivo de audio grabado
    with sr.AudioFile("output.wav") as source:
        # Lee TODO el audio del archivo
        audio = recognizer.record(source)


    try:
        # Convierte el audio a texto usando Google Speech Recognition
        # language="en-US" indica inglés de Estados Unidos
        text = recognizer.recognize_google(audio, language="en-US")

        # Muestra el texto reconocido
        print("📝 Dijiste:", text)

        if text.lower() == list(preguntas.values())[0].lower():
            print("🎉 ¡Correcto! La respuesta es:", list(preguntas.values())[0])
        else:
            print("❌ Incorrecto. La respuesta correcta es:", list(preguntas.values())[0])


    # Error cuando Google no puede entender el audio (ruido, silencio, etc.)
    except sr.UnknownValueError:
        print("😕 No se pudo reconocer la voz.")


    # Error cuando no hay conexión o falla el servicio de Google Speech API
    except sr.RequestError as e:
        print(f"❗ Error del servicio: {e}")