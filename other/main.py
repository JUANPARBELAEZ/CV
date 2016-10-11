

import kivy
kivy.require('1.7.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Mindful_Sleep(BoxLayout):
    pass
    
class Mindful_SleepApp(App):
    def build(self):
        return Mindful_Sleep()
        
if __name__== "__main__":
    Mindful_SleepApp().run()
    
"""






#Simple calculator to grow from here    
import kivy
kivy.require('1.7.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class Calc(FloatLayout):
    # define the multiplication of a function
    def product(self, instance):
        # self.result, self.a and self.b where defined explicitely in the kv
        #self.result.text = str(int(self.a.text) * int(self.b.text))
        result = " Bitch"
        return ("say my name" + result)

class TestApp(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    TestApp().run()    
    
"""
