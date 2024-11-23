from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934


class ConverterApp(App):
    message = StringProperty('0 km')

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        miles = self.get_miles()
        km = miles * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = f'{km:.2f} km'

    def handle_increment(self, increment):
        miles = self.get_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


ConverterApp().run()
