from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.graphics import *
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.clock import Clock


import random
import time


speed = 30
X, Y = 400, 800
Config.set('graphics', 'width', str(X))
Config.set('graphics', 'height', str(Y))



    


class MusicApp(Widget):
    def addVideos(self, amount = 50):
        '''
        this function is only for testing as it adds new videos into "database"
        '''
        for n in range(amount):
            self.videos[self.videosLen] = (random.random(), random.random(), random.random())
            self.videosLen+= 1
        self.videosLen-=1
        
        
    def newVidToLenta(self, amount=10):
        i = amount
        n = 0
        while n < i:
            a = random.randint(0, self.videosLen)
            if not a in self.videosInLenta:
                self.lenta.append(a)
                self.videosInLenta[a] = True
            else:
                i += 1
            n+= 1
    def down(self, event):
        global Y
        global speed
        self.currentID += 1
        self.currentAdj = -Y + speed
        
    def up(self, event):
        global Y
        global speed
        self.currentID -= 1
        self.currentAdj = Y - speed
    
    def __init__(self, **kwargs):
        global speed
        global X
        global Y
        super(MusicApp, self).__init__(**kwargs)
        self.pos = (0, -Y)
        
        self.videos = {
        0: (255, 0, 0),
        1: (0, 189, 0),
        2: (0, 0, 130),
        3: (70, 70, 20)
        }
        self.videosLen = 3
        self.currentAdj = 100
        self.currentID = 0
        self.lenta = [2, 0, 1, 3]

        self.videosInLenta = {
            2:True,
            0:True,
            1:True,
            3:True
        }
        self.color = (0.0, 0.0, 1.0)
        self.pos = (200, 200)
        
        
        if self.currentAdj < -speed:
            self.currentAdj += speed
            
        elif self.currentAdj > speed:
            self.currentAdj -= speed
            
        else:
            self.currentAdj = 0
            
        
        
        
        

        with self.canvas:
            Color(self.videos[self.lenta[self.currentID-1]][0], self.videos[self.lenta[self.currentID-1]][1], self.videos[self.lenta[self.currentID-1]][2], mode="rgb")
            self.vid1 = Rectangle(pos=(0,Y + self.currentAdj), size=(X,Y))
            
            Color(self.videos[self.lenta[self.currentID]][0], self.videos[self.lenta[self.currentID]][1], self.videos[self.lenta[self.currentID]][2], mode="rgb")
            self.vid2 = Rectangle(pos=(0,0 + self.currentAdj), size=(X,Y))
            
            Color(self.videos[self.lenta[self.currentID+1]][0], self.videos[self.lenta[self.currentID+1]][1], self.videos[self.lenta[self.currentID+1]][2], mode="rgb")
            self.vid3 = Rectangle(pos=(0,-Y + self.currentAdj), size=(X,Y))
            
            print(2)
            self.btn1 = Button(text='down')
            self.add_widget(self.btn1)
            self.btn1.bind(on_press=self.down)
            
            self.btn2 = Button(text='up', pos=(0, 150))
            self.add_widget(self.btn2)
            self.btn2.bind(on_press=self.up)
            
        self.addVideos()
        
            
        
        
            
    
    def update(self, dt):
        
        with self.canvas:
            self.clear_widgets()
            self.canvas.clear()
            Color(self.videos[self.lenta[self.currentID-1]][0], self.videos[self.lenta[self.currentID-1]][1], self.videos[self.lenta[self.currentID-1]][2], mode="rgb")
            self.vid1 = Rectangle(pos=(0,Y + self.currentAdj), size=(X,Y))
            
            Color(self.videos[self.lenta[self.currentID]][0], self.videos[self.lenta[self.currentID]][1], self.videos[self.lenta[self.currentID]][2], mode="rgb")
            self.vid2 = Rectangle(pos=(0,0 + self.currentAdj), size=(X,Y))
            
            Color(self.videos[self.lenta[self.currentID+1]][0], self.videos[self.lenta[self.currentID+1]][1], self.videos[self.lenta[self.currentID+1]][2], mode="rgb")
            self.vid3 = Rectangle(pos=(0,-Y + self.currentAdj), size=(X,Y))
            
            
            self.btn1 = Button(text='down')
            self.add_widget(self.btn1)
            self.btn1.bind(on_press=self.down)
            
            self.btn2 = Button(text='up', pos=(0, 150))
            self.add_widget(self.btn2)
            self.btn2.bind(on_press=self.up)
        print(len(self.videos),len(self.lenta))
            
        if self.currentAdj < -speed:
            self.currentAdj += speed
            
        elif self.currentAdj > speed:
            self.currentAdj -= speed
            
        else:
            self.currentAdj = 0
        if len(self.lenta) - self.currentID < 5:
            self.newVidToLenta()
            
    

            
            
        
    



class MusicAppApp(App):
    def build(self):
        game = MusicApp()
        Clock.schedule_interval(game.update, 2.0/60.0)
        return game
    
    


if __name__ == '__main__':
    MusicAppApp().run()