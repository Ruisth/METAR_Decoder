from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from HomePage import HomeScreen
from ICAO import ICAOScreen
from Decoder import DecoderScreen


class MetarDecoder(App):
    def build(self):
        self.icon = 'Resources/METAR_Decoder_Logo.png'
        screen_manager = ScreenManager()

        # Adding screens here
        screen_manager.add_widget(HomeScreen(name='Home Page'))
        screen_manager.add_widget(ICAOScreen(name='ICAO Input'))
        #screen_manager.add_widget(DecoderScreen(name='METAR Decoder'))

        return screen_manager


if __name__ == "__main__":
    metardecoder = MetarDecoder()
    metardecoder.run()
