"""
Esse codigo ouve o que você fala, transforma em texto e depois repete para você ouvir.

By: George Telles
+55 11 93290-7425
"""

import pyttsx3
import speech_recognition as sr

def falar(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)  # Ajuste de velocidade da fala

    selected_voice = 0
    engine.setProperty('voice', voices[selected_voice].id)

    text_to_speak = text
    engine.say(text_to_speak)
    engine.runAndWait()

def ouvir():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as fonte:
        print("Fale alguma coisa")
        audio = r.listen(fonte)
        print("Enviando para reconhecimento")

        try:
            texto = r.recognize_google(audio, language="pt-BR")  # idioma
            print("Texto reconhecido:", texto)
            return texto
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio")
            return ""
        except sr.RequestError as e:
            print("Erro ao solicitar resultados do Google Speech Recognition; {0}".format(e))
            return ""

if __name__ == "__main__":
    texto_ouvido = ouvir()
    falar(texto_ouvido)


