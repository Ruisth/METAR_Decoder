from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen


class ICAO_Gui(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Search METAR info", on_release=self.search_METAR))


    #def search_METAR(self, instance):
        # Search for METAR infor for ICAO inserted

