from .BaseControlClass import *
from .GuiManagerClass import DEFAULT2DTEXTSHADERID, NAMEFORMATSTRING
from .FontRendering.MSDFAtlasRenderer import CharData, AtlasInfo


class SingleChar(BaseControl):
    """
        Single Character object.

       @rtype : SingleChar
    """

    def __init__(self, left, top, height, char, parent, pinning=PinningEnum.TopLeft, color=vec4(.3, .3, .3, 1), ID=None,
                 imgID=None, rotation=None, borderSize=1, gradientType=GradientTypesEnum.noGradient, fontID='default',
                 fontColor=vec4(0, 0, 0, 1), fontBorderColor=vec4(1)):

        width = height
        super(SingleChar, self).__init__(left, top, width, height, parent, pinning, color, ID, imgID, rotation,
                                         borderSize, gradientType)
        self._char = char
        self._outlineLength = .18
        self._fontBorderColor = fontBorderColor
        self._fontColor = fontColor
        self._fontWeight = .56
        self._charCode = ord(char)
        self._fontID = fontID
        self._material._isText = True
        self._material.useDiffuseTexture = True
        self.isBuilt = False

        self._material.shaderProperties.append(FloatShaderProperty('outlineLength', self.outlineLength))
        self._material.shaderProperties.append(Vec4ShaderProperty('fontBorderColor', fontBorderColor))
        self._material.shaderProperties.append(Vec4ShaderProperty('fontColor', fontColor))
        self._material.shaderProperties.append(FloatShaderProperty('fontWeight', self.fontWeight))

    def _getOutlineLength(self):
        return self._outlineLength

    def _setOutlineLength(self, val):
        self._outlineLength = val
        self._material.shaderProperties['outlineLength'] = val

    outlineLength = property(_getOutlineLength, _setOutlineLength)

    def _getFontBorderColor(self):
        return self._fontBorderColor

    def _setFontBorderColor(self, val):
        self._fontBorderColor = val
        self._material.shaderProperties['fontBorderColor'] = val

    fontBorderColor = property(_getFontBorderColor, _setFontBorderColor)

    def _getFontColor(self):
        return self._fontColor

    def _setFontColor(self, val):
        self._fontColor = val
        self._material.shaderProperties['fontColor'] = val

    fontColor = property(_getFontColor, _setFontColor)

    def _getfontWeight(self):
        return self._fontWeight

    def _setfontWeight(self, val):
        self._fontWeight = val
        self._material.shaderProperties['fontWeight'] = val

    fontWeight = property(_getfontWeight, _setfontWeight)

    def _buildText(self):
        if not self.isBuilt:
            gui = self._guiMan
            self._material.diffuseTextureID = gui.fontTextureNames[self._fontID]
            info = gui.fontInfos[self._fontID]
            assert isinstance(info, AtlasInfo)
            hasChar = self._charCode in info.charDataDict
            if not hasChar:
                raise NotImplementedError('Add the char!!!!!!!')
            cData = info.charDataDict[self._charCode]
            assert isinstance(cData, CharData)
            x = cData.atlasOriginX / float(info.width)
            y = cData.atlasOriginY / float(info.height)
            z = info.fontSize / float(info.width)
            w = info.fontSize / float(info.height)
            self._material.uvOffset = (x, y, z, w)
            self.isBuilt = True

    def _setChar(self, char):
        self._char = char
        self._charCode = ord(char)
        self.isBuilt = False

    def _getChar(self):
        return self._char

    char = property(_getChar, _setChar)

    def _setFont(self, fontID):
        self._fontID = fontID
        self.isBuilt = False

    def _getFont(self):
        return self._fontID

    fontID = property(_getFont, _setFont)

    def __repr__(self):
        return self.char

    def _update(self):
        if not self.isBuilt:
            self._buildText()
        super(SingleChar, self)._update()
