import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import wikipedia

# Inicializa el motor de voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    # Inicializa el reconocimiento de voz
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            # Usa Google Speech Recognition
            command = recognizer.recognize_google(audio, language='es-ES')
            print(f"Tú dijiste: {command}")
        except sr.UnknownValueError:
            print("No entendí lo que dijiste")
            command = ""
        except sr.RequestError:
            print("No se pudo acceder al servicio de reconocimiento de voz")
            command = ""
        return command.lower()

def execute_command(command):
    if "abre google" in command:
        webbrowser.open("https://www.google.com")
        speak("Abriendo Google")
    elif "wikipedia" in command:
        speak("Buscando en Wikipedia")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2, auto_suggest=False)
        print(result)
        speak(result)
    elif "abre calculadora" in command:
        speak("Abriendo la calculadora")
        os.system("calc" if os.name == 'nt' else "gnome-calculator")
    elif "adiós" in command:
        speak("Adiós, que tengas un buen día!")
        exit()
    else:
        speak("No entendí el comando")

if __name__ == "__main__":
    speak("Hola, soy tu asistente. ¿En qué puedo ayudarte?")
    while True:
        command = listen()
        if command:
            execute_command(command)