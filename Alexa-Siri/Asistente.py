import speech_recognition as sr
import pyttsx3 as tsx
import os
#os.environ["TF_USE_LEGACY_KERAS"] = "1"

Asistant = tsx.init()
Asistant.setProperty('rate', 150)

def hablar(texto):
    Asistant.say(texto)
    Asistant.runAndWait()

def Escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as souce:
        #print ("Escuchar")
        audio = recognizer.listen(souce)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        hablar (f"{comando}")
        return comando.lower()
    except sr.UnknownValueError:
        hablar ("Hable bien,que no se le entiende nada")
        return ""
    except sr.RequestError:
        hablar ("No anda el microfono")
        return ""

#def Responder(Comando):
#    if "salir" in Comando or "adios" in Comando:
#        exit()

def procesar_pregunta(pregunta):
    response = ai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def Aistente_voz () :
    while True:
        Comando = Escuchar()
        if Comando:
            respuesta = procesar_pregunta(Comando)
            print(f"Asistente: {respuesta}")
            hablar(respuesta)

if __name__ == "__main__":
    hablar("que quieres")
    Aistente_voz()