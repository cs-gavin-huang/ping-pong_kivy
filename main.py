from kivy.app import App
from kivy.uix.widget import widget

# class of pingpong game wdiget, root of tree
class PingPongGame(Widget):
    pass

# return pingponggame and use it as root
class PingPongApp(App):
    def build(self):
        return PingPongGame()
    
if __name__ == '__main__':
    PingPongApp().run()