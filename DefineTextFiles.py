class scriptFile:
    def __init__(self, scriptFile: object, scriptFileDirectory: str, scriptFileText: str) -> None:
        self.scriptFile = scriptFile
        self.scriptFileDirectory = scriptFileDirectory
        self.scriptFileText = scriptFileText

class settingsFile:
    def __init__(
                self,
                scriptsFolderName: str,
                ttsModel: str, 
                language: str,
                emotion: str, 
                speed: float,
                whisperModel: str,
                outputAudioName: str,
                subtitleOutputFileName: str,
                outputVideoName: str,
                videoBackgroundFolder: str,
                videoBackgroundLinksFileName : str,
                downloadVideosInLinksFile: bool,
                loopAllModels: bool,
                name: str,
                fontName: str,
                fontSize: int,
                primaryColour: str,
                secondaryColour: str,
                outlineColour: str,
                backColour: str,
                bold: bool,
                italic: bool,
                underLine: bool,
                strikeOut: bool,
                scaleX: int,
                scaleY: int, 
                spacing: int,
                angle: int,
                borderStyle: int,
                outline: int,
                shadow: int,
                alignment: int,
                marginL: int,
                marginR: int,
                marginV: int, 
                encoding: int
                ) -> None:
        self._scriptsFolderName = scriptsFolderName
        self._ttsModel = ttsModel
        self._language = language
        self._emotion = emotion
        self._speed = speed
        self._whisperModel = whisperModel
        self._outputAudioName = outputAudioName
        self._subtitleOutputFileName = subtitleOutputFileName
        self._outputVideoName = outputVideoName
        self._videoBackgroundFolder = videoBackgroundFolder
        self._videoBackgroundLinksFileName = videoBackgroundLinksFileName
        if downloadVideosInLinksFile.upper() == "TRUE" or downloadVideosInLinksFile == True:
            self._downloadVideosInLinksFile = True
        else:
            self._downloadVideosInLinksFile = False
        if loopAllModels.upper() == "TRUE" or loopAllModels == True:
            self._loopAllModels = True
        else:
            self._loopAllModels = False
        self._name = name
        self._fontName = fontName
        self._fontSize = fontSize
        self._primaryColour = primaryColour
        self._secondaryColour = secondaryColour
        self._outlineColour = outlineColour
        self._backColour = backColour
        if bold.upper() == "TRUE" or bold == True:
            self._bold = 1
        else:
            self._bold = 0
        if italic.upper() == "TRUE" or italic == True:
            self._italic = 1
        else:
            self._italic = 0
        if underLine.upper() == "TRUE" or underLine == True:
            self._underLine = 1
        else:
            self._underLine = 0
        if strikeOut.upper() == "TRUE" or underLine == True:
            self._strikeOut = 1
        else:
            self._strikeOut = 0
        self._scaleX = scaleX
        self._scaleY = scaleY
        self._spacing = spacing
        self._angle = angle
        self._borderStyle = borderStyle
        self._outline = outline
        self._shadow = shadow
        self._alignment = alignment
        self._marginL = marginL
        self._marginR = marginR
        self._marginV = marginV
        self._encoding = encoding
    @property
    def downloadVideosInLinksFile(self):
        return self._downloadVideosInLinksFile
    @downloadVideosInLinksFile.setter
    def downloadVideosInLinksFile(self, downloadVideosInLinksFile: bool):
        if downloadVideosInLinksFile.upper() == "TRUE" or downloadVideosInLinksFile == True:
            self.downloadVideosInLinksFile = True
        else:
            self.downloadVideosInLinksFile = False

    @property
    def loopAllModels(self):
        return self._loopAllModels
    @loopAllModels.setter
    def loopAllModels(self, loopAllModels: bool) -> None:
        if loopAllModels.upper() == "TRUE" or loopAllModels == True:
            self._loopAllModels = True
        else:
            self._loopAllModels = False

    @property
    def bold(self):
        return self._bold
    @bold.setter
    def bold(self, bold: bool) -> None:
        if bold.upper() == "TRUE" or bold == True:
            self._bold = 1
        else:
            self._bold = 0

    @property
    def italic(self):
        return self._italic
    @italic.setter
    def italic(self, italic: bool) -> None:
        if italic.upper() == "TRUE" or italic == True:
            self._italic = 1
        else:
            self._italic = 0

    @property
    def underLine(self):
        return self._underLine
    @underLine.setter
    def underLine(self, underLine: bool) -> None:
        if underLine.upper() == "TRUE" or underLine == True:
            self._underLine = 1
        else:
            self._underLine = 0
    
    @property
    def strikeOut(self):
        return self._strikeOut
    @strikeOut.setter
    def strikeOut(self, strikeOut: bool) -> None:
        if strikeOut.upper() == "TRUE" or strikeOut == True:
            self._strikeOut = 1
        else:
            self._strikeOut = 0