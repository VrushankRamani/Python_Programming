from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
       
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.counter = 0
        self.counter_label = Label(text=f"Counter: {self.counter}", font_size=32)
        layout.add_widget(self.counter_label)

        increment_button = Button(text="Increment", font_size=24)
        increment_button.bind(on_press=self.increment_counter)
        layout.add_widget(increment_button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = f"Counter: {self.counter}"

if __name__ == '__main__':
    CounterApp().run()