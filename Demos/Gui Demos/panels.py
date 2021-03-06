from cycgkit.cgtypes import vec3, vec4

from _set_path import setPath
setPath()
from _base._BaseDemo import _Demo_Base, runDemo, triangleMODEL
from e3d.gui import Panel, GradientTypesEnum, PinningEnum
from e3d import Colors
from math import sin
from os import path


class Demo(_Demo_Base):
    def __init__(self, winSize):
        super(Demo, self).__init__(winSize)
        self.dorot = False
        self.texturesToLoad.append([path.join(path.dirname(__file__), path.pardir, 'textures/Grass.jpg'), 'grass'])

    def loadModels(self):
        engine = self.engine

        camera = self.camera
        camera.position = vec3(0, 100, 290)
        camera.rotateX(20)

        engine.models.loadModel(triangleMODEL, "trianglemodel", forceStatic=True)
        self.triangle = self.scene1.addModel('trianglemodel', 'triangle1', vec3(0, 0, 0), vec3(0), 1.5)
        mat = self.triangle.getMaterialByIndex(0)
        mat.useDiffuseTexture = True

    def keydown(self, e):
        if e.eventName == 'keyUp':
            return
        keyName = e.keyName
        try:
            e.keyName = keyName.decode()
        except Exception:
            pass

        if keyName == 'escape':  # ESC
            self.close()
        if 'ctrl' in keyName:
            self.dorot = not self.dorot
        if keyName.__contains__('space'):
            self.window.setFullScreen(not self.window.isFullScreen())
        if keyName == 'f1':  # F1
            np = [round(d, 3) for d in self.camera.position]
            print('Camera pos:{0}'.format(str(np)))

    def scene1Update(self, ev):
        ft = ev[0] + .01
        movespeed = ft / 10.0
        self.lastspeed = movespeed
        self.scrollingPanel._material.uvOffset.x += .01
        self.movingPanel.moveLeft(sin(ev[1] / 1000.0))
        if self.dorot:
            self.rotatingPanel.rotate2D(1)
            self.rotatingPanel2.rotate2D(-1)
            if self.triangle:
                self.triangle.rotateY(.1 * ft)

    def buildGui(self):
        self.onelayer = self.window.gui.addLayer('one')
        super(Demo, self).buildGui()

        PANELSIZE = 100

        longPanel = Panel(110, 0, PANELSIZE * 2.5, PANELSIZE, self.onelayer, color=vec4(0, 0, 1, 1))
        longPanel.borderColor = vec4(.2, .5, 1, 1)
        longPanel.borderSize = 2

        self.rotatingPanel = Panel(420, 0, PANELSIZE, PANELSIZE, self.onelayer, imgID='grass')
        self.rotatingPanel.opacity = .8

        for i in range(9):
            p = Panel(110 * i, 105, PANELSIZE, PANELSIZE, self.onelayer)
            p.opacity = .9
            p.borderColor = vec4(1)
            p.borderSize = 1
            p.gradientType = i
            p.gradientColor0 = Colors.RED
            p.gradientColor1 = Colors.BLUE

        PINNEDW = PANELSIZE + 220
        PINNEDH = PANELSIZE + 100
        CORNERSIZE = 20
        rightBorder = PINNEDW - CORNERSIZE
        bottomBorder = PINNEDH - CORNERSIZE

        pinnedPanel = Panel(280, 300, PINNEDW, PINNEDH, self.onelayer, color=vec4(0, 1, 0, .5), ID='pinned')
        pinnedPanel.pinning = PinningEnum.all
        bs = pinnedPanel.borderSize = 8
        self.rotatingPanel2 = pinnedPanel

        pinnedCorners = (Panel(bs, bs, CORNERSIZE, CORNERSIZE, pinnedPanel),
                         Panel(rightBorder - bs, bs, CORNERSIZE, CORNERSIZE, pinnedPanel, PinningEnum.all),
                         Panel(bs, bottomBorder - bs, CORNERSIZE, CORNERSIZE, pinnedPanel, PinningEnum.all),
                         Panel(rightBorder - bs, bottomBorder - bs, CORNERSIZE, CORNERSIZE, pinnedPanel, PinningEnum.BottomRight))
        for panel in pinnedCorners:
            panel.color = vec4(.9, .4, 0, 1)
            panel.borderSize = 2
            panel.borderColor = vec4(1, 1, 0, 1)

        self.scrollingPanel = Panel(600, 0, PANELSIZE, PANELSIZE, self.onelayer, imgID='grass')
        self.scrollingPanel.borderSize = 0

        for i in range(4):
            p = Panel(10 + (20 * i), 220 + (20 * i), PANELSIZE, PANELSIZE, self.onelayer, color=vec4(1, 1, 0, 1))
            if i == 2:
                self.movingPanel = p

        print('Press CTRL to show rotation.')
                

if __name__ == '__main__':
    runDemo(Demo((980, 600)), 'GUI Demo - Panels')
