from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from GUI_Interface.ICAO_Gui import icao


class Homepage(App):
    def build(self):
        return Label(text="METAR Decoder")


Homepage().run()
