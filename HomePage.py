from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = RelativeLayout()
        self.icon = 'Resources/METAR_Decoder_Logo.png'

        # Background Image
        background_image = Image(source='Resources/METAR_Decoder_Image.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)

        # Buttons Layout
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100), spacing=50)
        buttons_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.1}

        # Button to input ICAO
        input_icao_button = Button(text='Input ICAO', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        input_icao_button.bind(on_press=self.input_icao)

        # Button to METAR Decode
        metar_decode_button = Button(text='METAR Decode', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        metar_decode_button.bind(on_press=self.metar_decode)

        buttons_layout.add_widget(input_icao_button)
        buttons_layout.add_widget(metar_decode_button)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def input_icao(self, instance):
        # Replace this section with the code to ICAO input
        self.manager.current = 'ICAO Input'

    def metar_decode(self, instance):
        # Replace this section with te code to METAR Decoder
        self.manager.current = 'METAR Decoder'
