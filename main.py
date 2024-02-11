from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image


class HomePage(App):
    def build(self):
        boxLayout = BoxLayout(orientation='vertical')

        backgroundImage = Image(source='Resources/METAR_Decoder_Image.png', size_hint=(1, 0.7), allow_stretch=True)
        boxLayout.add_widget(backgroundImage)

        buttonsLayout = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))

        # Button to input ICAO
        input_icao_button = Button(text='Input ICAO', size_hint=(0.5, 1))
        input_icao_button.bind(on_press=self.input_icao)

        # Button to METAR Decode
        metar_decode_button = Button(text='METAR Decode', size_hint=(0.5, 1))
        metar_decode_button.bind(on_press=self.metar_decode)

        buttonsLayout.add_widget(input_icao_button)
        buttonsLayout.add_widget(metar_decode_button)
        boxLayout.add_widget(buttonsLayout)

        return boxLayout

    def input_icao(self, instance):
        # Replace this section with the code to ICAO input
        print("Input ICAO button pressed")

    def metar_decode(self, instance):
        # Replace this section with te code to METAR Decoder
        print("METAR decode button pressed")


if __name__ == "__main__":
    HomePage().run()
