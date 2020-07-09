from pyglet import image, window
import pyglet

class Te(object):
    def __init__(self, image):
        super.__init__(object)

        self.animation = super.image.load_animation(image)
        self.animSprite = super.sprite.Sprite(self.animation)
        self.width = self.animSprite.width
        self.height = self.animSprite.height
        self.windows = super.window.Window(self.width, self.height)
        self.r, self.g, self.b, self.aplha = 0.5, 0.5, 0.8, 0.5
        super.gl.glClearColor(self.r, self.g, self.b, self.aplha)

    
    def on_draw(self):
        self.windows.clear()
        self.animSprite.draw()



    def run(self):
        self.pyglet.app.run()



t=Te("tenor.gif")