import json
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import rgba
with open('./json/encrypt-decrypt.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open('./json/encrypt-decrypt.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']


class Luna23(App):
    def build(self):
        # set window
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        Window.clearcolor =  rgba(127, 255, 212)
        # labels
        #add input widget
        self.input = TextInput(
            multiline = True,
            size_hint = (0.5,0.5),
            background_color = '#7feaff',
        )
        self.window.add_widget(self.input)
        self.output = TextInput(
            size_hint = (0.5,0.5),
            background_color = '#7feaff',
        )
        self.window.add_widget(self.output)
        # add decrypt and encrypt buttons
        self.button_encrypt = Button(
            text="Encrypt",
            size_hint = (0.5,0.5),
            bold = True,
            background_color = '#7fffd4'
        )
        self.window.add_widget(self.button_encrypt)
        self.button_encrypt.bind(on_press = self.encrypt)
        self.button_decrypt = Button(
            text="Decrypt",
            size_hint = (0.5,0.5),
            bold = True,
            background_color ='#7fffd4'
        )
        self.window.add_widget(self.button_decrypt)
        self.button_decrypt.bind(on_press = self.decrypt)
        return self.window
    def encrypt(self, instance):
        counter = 0
        self.output.text = ""
        while counter < len(self.input.text):
            self.output.text = self.output.text + encrypt[self.input.text[counter]]
            counter = counter + 1
    def decrypt(self, instance):
        counter = 0
        self.output.text = ""
        while counter < len(self.input.text):
            self.output.text = self.output.text + decrypt[self.input.text[counter]]
            counter = counter + 1

if __name__ == "__main__":
    Luna23().run()