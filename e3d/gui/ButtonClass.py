from .LabelClass import *
from .TextEnums import FontWeightEnum
from ..Colors import *
from .Styling import *


class Button(BaseControl):
    """
        Clickable button

       @rtype : Button
    """

    def __init__(self, left, top, width, height, text, parent, pinning=PinningEnum.TopLeft, color=None,
                 fontID='default', ID=None, rotation=None, style=None):
        """
        :param borderSize:
        :type borderSize:

        """
        style = style or DefaultStyle(color)
        styleHint = style.buttonStyleHint
        if color is None:
            color = style.backgroundColor
        if styleHint == StyleHintsEnum.Image:
            image = bgImgID
        else:
            image = None

        super(Button, self).__init__(left, top, width, height, parent, pinning, color, ID,
                                     image, rotation, style)

        if styleHint in (StyleHintsEnum.Raised, StyleHintsEnum.Sunken):
            self.gradientType = GradientTypesEnum.Horizontal
        else:
            self.gradientType = GradientTypesEnum.noGradient

        self.borderColor = style.borderColor
        borderSize = style.borderSize
        self._lastBorderSize = borderSize
        self._label = Label(borderSize, borderSize, width - (borderSize * 2), text, self,
                            pinning=PinningEnum.TopLeftRight, fontID=fontID, ID=self.ID + '_label',
                            outlineLength=OutlineLenghtEnum.NoOutline)
        label = self._label
        label.outlineColor = style.fontColor
        label.borderSize = 0
        label.color = vec4(0)
        x, y, z = self.getAlignedPosition(label.size, self.size, self.borderSize, hAlign=self._hTextAlign)
        label.top = y
        label.vTextAlign = Align2DEnum.Center

        self._styleHint = styleHint
        self._buildColors()

    def _hTextAlignGet(self):
        return self._label.hTextAlign

    def _vTextAlignGet(self):
        return self._label.vTextAlign

    def _hTextAlignSet(self, value):
        self._label.hTextAlign = value

    def _vTextAlignSet(self, value):
        self._label.vTextAlign = value

    @property
    def styleHint(self):
        return self._styleHint

    @styleHint.setter
    def styleHint(self, value):
        self._styleHint = value
        self._lastBorderSize = self.style.borderSize
        if value in (StyleHintsEnum.Raised, StyleHintsEnum.Sunken):
            self.gradientType = GradientTypesEnum.Horizontal
        else:
            self.gradientType = GradientTypesEnum.noGradient
        self._buildColors()

    @property
    def color(self):
        return super(Button, self)._getColor()

    @color.setter
    def color(self, val):
        super(Button, self)._setColor(val)

    def _buildColors(self):
        self._colorizeHover(False)

    def _getText(self):
        return self._label.text

    def _setText(self, val):
        self._label.text = val

    text = property(_getText, _setText)

    def _getFontColor(self):
        return self._label.fontColor

    def _setFontColor(self, val):
        label = self._label
        label.fontColor = val
        label.outlineColor = val

    fontColor = property(_getFontColor, _setFontColor)

    def _getfontWeight(self):
        return self._label.fontWeight

    def _setfontWeight(self, val):
        self._label.fontWeight = val

    fontWeight = property(_getfontWeight, _setfontWeight)

    def _setFont(self, fontID):
        self._label.fontID = fontID

    def _getFont(self):
        return self._label.fontID

    fontID = property(_getFont, _setFont)

    def _colorizeHover(self, isOverMe):
        style = self.style
        if isOverMe:
            if self.styleHint == StyleHintsEnum.Hover:
                self.borderSize = style.borderSize
                self.gradientType = GradientTypesEnum.Horizontal
                self.gradientColor0 = style.autoRaiseGradientColor0
                self.gradientColor1 = style.autoRaiseGradientColor1
            else:
                if self.gradientType == GradientTypesEnum.noGradient:
                    self.color = style.hoverColor
                else:
                    self.gradientColor0 = style.hoverGradientColor0
                    self.gradientColor1 = style.hoverGradientColor1
        else:
            if self.styleHint == StyleHintsEnum.Hover:
                self.borderSize = self._lastBorderSize
                self.gradientType = GradientTypesEnum.noGradient
            if self.gradientType == GradientTypesEnum.noGradient:
                self.color = style.backgroundColor
            else:
                self.gradientColor0 = style.raisedGradientColor0
                self.gradientColor1 = style.raisedGradientColor1

    def _handleMouseEnter(self, event):
        self._lastBorderSize = self._borderSize
        self._colorizeHover(True)

    def _handleMouseLeave(self, event):
        self._colorizeHover(False)

    def _handleMouseButtonDown(self, event):
        style = self.style
        if self.styleHint == StyleHintsEnum.Hover:
            self.borderSize = style.borderSize
        if self.gradientType == GradientTypesEnum.noGradient:
            self.color = style.pressedColor
        else:
            self.gradientColor0 = style.pressedGradientColor0
            self.gradientColor1 = style.pressedGradientColor1

    def _handleMouseButtonUp(self, event):
        if self.parent._findForegroundControl(event.x, event.y) == self:
            self._colorizeHover(True)
        else:
            self._colorizeHover(False)

    def _reStyle(self):
        super(Button, self)._reStyle()
        self._lastBorderSize = self.style.borderSize
        self._buildColors()
