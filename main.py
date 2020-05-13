from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')


class MyApp(App):
    def build(self):
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .7))
        bl = BoxLayout(orientation='vertical', padding=[25])

        self.lable = Label(text='0', font_size=40, size_hint=(1, .3),valign='center', halign='right', text_size=(400 - 50, 500 * .3 - 50))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_number))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_number))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_number))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.eq))

        bl.add_widget(self.lable)
        bl.add_widget(gl)

        return bl

    def add_number(self, instance):
        if self.lable.text == '0':
            self.lable.text = ''
        self.lable.text += instance.text

    def eq(self, instance):
        self.lable.text = str(eval(self.lable.text))
        

if __name__ == '__main__':
    MyApp().run()
