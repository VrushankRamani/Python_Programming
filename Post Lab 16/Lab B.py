from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TextInputApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.text_input = TextInput(hint_text="Type something here...", multiline=False, font_size=20)
        layout.add_widget(self.text_input)

        submit_button = Button(text="Submit", font_size=20)
        submit_button.bind(on_press=self.display_text)
        layout.add_widget(submit_button)

        self.output_label = Label(text="Your text will appear here", font_size=24)
        layout.add_widget(self.output_label)

        return layout

    def display_text(self, instance):
        user_text = self.text_input.text
        self.output_label.text = f"You typed: {user_text}"

if __name__ == '__main__':
    TextInputApp().run()