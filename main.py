from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from GUI_Interface.ICAO_Gui import icao


class Homepage(App):
    def build(self):
        return Button(text="Welcome to LikeGeeks!", background_color=(255, 0, 0, 100))


Homepage().run()
