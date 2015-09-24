import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

p = [0, 0]

class TestApp(App):

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        global p
        animation = Animation(pos=(p[0], p[1]))
        #for i in range(1,5):
        change = [100, 100]
        animation += Animation(pos= (change[0], change[1]))
        #pos=(i*50, i*50))
        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        p[0] += change[0]
        p[1] += change[1]
        animation.start(instance)
        print(instance) 

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = Button(size_hint=(None, None), text='plop',
                        on_press=self.animate)
        return button

if __name__ == '__main__':
    TestApp().run()
