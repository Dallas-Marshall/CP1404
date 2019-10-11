"""Program to convert miles to kilometers using kivy app."""
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometers(App):
    """MilesToKilometers is a kivy app that converts miles to kilometers."""
    result = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('convert_miles_to_kilometers.kv')
        return self.root

    def get_valid_miles(self):
        """Get input from user_miles_input (text box) and check valid float."""
        try:
            value = float(self.root.ids.user_miles_input.text)
            return value
        except ValueError:
            return 0

    def handle_convert(self):
        """Convert miles into kilometers."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.result = self.root.ids.output_label.text = str(result)

    def handle_increment(self, change_value):
        """Adjust the value of miles_value by change_value provided."""
        value = self.get_valid_miles() + change_value
        self.root.ids.user_miles_input.text = str(value)
        self.handle_convert()


MilesToKilometers().run()
