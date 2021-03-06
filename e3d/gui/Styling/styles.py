from .StyleClass import DefaultStyle, GradientTypesEnum
from ...Colors import *

from cycgkit.cgtypes import vec4


class ColorfullStyle(DefaultStyle):
    def __init__(self):
        super(ColorfullStyle, self).__init__(RGB1(.5, 0, .5))
        self.name = 'Colorfull'

        self.baseColor = fromRGB1_A(RED / 2.0 + BLUE, 1)
        self.borderColor = YELLOW
        self.borderSize = 3
        self.fontColor = ORANGE
        self.gradientType = GradientTypesEnum.LeftCorner
        self.raisedGradientColor0 = BLUE
        self.raisedGradientColor1 = GREEN
        self.hoverGradientColor0 = YELLOW
        self.hoverGradientColor1 = RED
        self.pressedGradientColor0 = BLACK
        self.pressedGradientColor1 = WHITE
        self.autoRaiseGradientColor0 = RGB1(.5, 0, .9)
        self.autoRaiseGradientColor1 = RGB1(0, 1, .5)
        self.activeColor = fromRGB1_A((RED + BLUE) / 2.0, 1.0)

        self.pressedColor = RGB1(1, .5, .5)

