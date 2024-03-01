import requests
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class DecoderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = RelativeLayout()

        # Background Image
        background_image = Image(source='Resources/METAR_Decoder_Image.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)

        # Input Box
        metar_box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100))
        metar_box.pos_hint = {'center_x': 0.5, 'center_y': 0.8}
        self.metar_input = TextInput(hint_text="Enter METAR code here...", size_hint=(0.5, 1),
                                     background_color=(0.082, 0.322, 0.388, 1))
        metar_box.add_widget(self.metar_input)

        response_box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100), opacity=1)
        response_box.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        self.response_label = Label(text="")
        self.response_label.bind(size=lambda instance, value: setattr(self.response_label, 'text_size', value))
        response_box.add_widget(self.response_label)

        # Buttons Layout
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100), spacing=50)
        buttons_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.1}

        # Button to Search
        decode_button = Button(text='Decode', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        decode_button.bind(on_press=self.decode_metar)

        # Button to go Back
        home_button = Button(text='Home', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        home_button.bind(on_press=self.home_screen)

        buttons_layout.add_widget(decode_button)
        buttons_layout.add_widget(home_button)
        layout.add_widget(metar_box)
        layout.add_widget(response_box)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def decode_metar(self, instance):
        decoded_metar = {}

        # Split METAR string into individual components
        metar = self.metar_input.text
        components = metar.split()

        # Extracting basic information
        decoded_metar['station'] = components[0]
        decoded_metar['time'] = components[1]
        decoded_metar['wind_direction'] = components[3]
        decoded_metar['wind_speed'] = components[4]
        decoded_metar['visibility'] = components[5]
        decoded_metar['weather'] = components[6]

        # If present, extract temperature and dew point
        if 'M' in components[7] or 'M' in components[8]:
            temperature_index = 7
            decoded_metar['temperature'] = components[7]
            decoded_metar['dew_point'] = components[8]
        else:
            temperature_index = 8
            decoded_metar['temperature'] = components[8]
            decoded_metar['dew_point'] = components[9]

        # Convert wind direction and speed to more readable format
        decoded_metar['wind_direction'] = decoded_metar['wind_direction'] + ' degrees'
        decoded_metar['wind_speed'] = decoded_metar['wind_speed'] + ' knots'

        # Convert visibility to more readable format
        if decoded_metar['visibility'].startswith('M'):
            decoded_metar['visibility'] = 'Less than ' + decoded_metar['visibility'][1:] + ' meters'
        else:
            decoded_metar['visibility'] = decoded_metar['visibility'] + ' meters'

        self.response_label.text = str(decoded_metar)
        print("Decoded METAR : ")
        print(decoded_metar)

    def home_screen(self, instance):
        self.manager.current = 'Home Page'
        self.metar_input.text = ""
        self.response_label.text = ""
