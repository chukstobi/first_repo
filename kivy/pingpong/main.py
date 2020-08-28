from kivy.app import App
from kivy.uix.widget import Widget
import kivy.properties as kp
from kivy.vector import Vector
from kivy.clock import Clock
import random
class PongBall(Widget):
    velocity_x = kp.NumericProperty(0)
    velocity_y = kp.NumericProperty(0)
    velocity = kp.ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = kp.ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(random.randint(0,360))
    def update(self,dt):
        self.ball.move()

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game

PongApp().run()
# import kivy 
# kivy.require('1.9.1') # replace with your current kivy version !

# from kivy.app import App
# from kivy.uix.label import Label

# # add the following 2 lines to solve OpenGL 2.0 bug
# from kivy import Config
# Config.set('graphics', 'multisamples', '0')


# class MyApp(App):

#     def build(self):
#         return Label(text='Hello world')

# if __name__ == '__main__':
#     MyApp().run()