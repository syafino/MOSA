import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import pyttsx3
import speech_recognition as sr

kivy.require('2.3.0')
Window.clearcolor = (0.96, 0.96, 0.96, 1)

# Voice engine setup
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

class MainWidget(BoxLayout):
    def translate_text(self):
        input_text = self.ids.input_box.text.strip()
        if input_text:
            translated = self.fake_translate(input_text)
            self.ids.output_box.text = translated

    def fake_translate(self, text):
        # Placeholder: reverse string as mock translation
        return text[::-1]

    def speak_output(self):
        output_text = self.ids.output_box.text.strip()
        if output_text:
            tts_engine.say(output_text)
            tts_engine.runAndWait()

    def record_voice(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.ids.input_box.text = "Listening..."
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                self.ids.input_box.text = text
            except Exception as e:
                self.ids.input_box.text = f"Error: {str(e)}"

class MosaApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MosaApp().run()
