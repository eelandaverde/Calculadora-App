from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Set the app size
Window.size = (360,600)

#Designate our .kv design file
Builder.load_file('calc.kv')

class MyLayout(Widget):
    
    def clear(self):
        self.ids.calc_input.text = '0'
    #Create a button pressing function
    def button_press(self,button): 
        #Create a variable that contains whatever in the text-box already
        prior = self.ids.calc_input.text 

        if "Error" in prior:
            prior = ''

        #determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text =  ''
            self.ids.calc_input.text =  f'{button}'
        
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    #Create an erase button
    def erase(self):
        prior = self.ids.calc_input.text
        #Remove the last item in the textbox
        prior = prior[:-1]
        #Output
        self.ids.calc_input.text = prior

    #Create function to make textbox positive and negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    #Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        #   Add decimal at the end of the text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.' 
            self.ids.calc_input.text = prior

    #Create addition function
    def math_sign (self, sign):
        prior = self.ids.calc_input.text
        #Slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'
    #Create Substraction function
    
    def equal(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
    
class CalculatorApp (App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()