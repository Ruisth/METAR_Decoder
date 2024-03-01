import requests
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class ICAOScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = RelativeLayout()

        # Background Image
        background_image = Image(source='Resources/METAR_Decoder_Image.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)

        # Input Box
        icao_box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100))
        icao_box.pos_hint = {'center_x': 0.5, 'center_y': 0.8}
        self.icao_input = TextInput(hint_text="Enter ICAO code", size_hint=(0.5, 1),
                                    background_color=(0.082, 0.322, 0.388, 1))
        icao_box.add_widget(self.icao_input)

        # Response Box
        response_box = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100))
        response_box.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        self.response_label = Label(text="")
        response_box.add_widget(self.response_label)

        # Buttons Layout
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(600, 100), spacing=50)
        buttons_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.1}

        # Button to Search
        search_button = Button(text='Search', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        search_button.bind(on_press=self.fetch_metar_data)

        # Button to go Back
        back_button = Button(text='Back', size_hint=(0.5, 1), background_color=(0.082, 0.322, 0.388, 1))
        back_button.bind(on_press=self.home_screen)

        buttons_layout.add_widget(search_button)
        buttons_layout.add_widget(back_button)
        layout.add_widget(icao_box)
        layout.add_widget(response_box)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def fetch_metar_data(self, instance):
        icao_code = self.icao_input.text
        url = f"https://aviationweather.gov/api/data/metar?ids={icao_code}&format=raw&taf=false&date=0"
        response = requests.get(url)
        if response.status_code == 200:
            metar_data = response.text
            self.response_label.text = metar_data
            print("METAR Data: ")
            print(metar_data)
            return response.text
        else:
            print("Failed to fetch METAR data.")
            return None

    def home_screen(self, instance):

        self.manager.current = 'Home Page'
        self.icao_input.text = ""
        self.response_label.text = ""
