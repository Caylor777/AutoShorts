class scriptFile:
    def __init__(self, scriptFile: object, scriptFileDirectory: str, scriptFileText: str) -> None:
        self.scriptFile = scriptFile
        self.scriptFileDirectory = scriptFileDirectory
        self.scriptFileText = scriptFileText
    def setScriptFile(self, scriptFile: object) -> None:
        self.scriptFile = scriptFile
    def setScriptFileDirectory(self, scriptFileDirectory: str) -> None:
        self.scriptFileDirectory = scriptFileDirectory
    def setScriptFileText(self, scriptFileText: str) -> None:
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
        self.scriptsFolderName = scriptsFolderName
        self.ttsModel = ttsModel
        self.language = language
        self.emotion = emotion
        self.speed = speed
        self.whisperModel = whisperModel
        self.outputAudioName = outputAudioName
        self.subtitleOutputFileName = subtitleOutputFileName
        self.outputVideoName = outputVideoName
        self.videoBackgroundFolder = videoBackgroundFolder
        if loopAllModels.upper() == "TRUE":
            self.loopAllModels = True
        else:
            self.loopAllModels = False
        self.name = name
        self.fontName = fontName
        self.fontSize = fontSize
        self.primaryColour = primaryColour
        self.secondaryColour = secondaryColour
        self.outlineColour = outlineColour
        self.backColour = backColour
        if bold.upper() == "TRUE":
            self.bold = 1
        else:
            self.bold = 0
        if italic.upper() == "TRUE":
            self.italic = 1
        else:
            self.italic = 0
        if underLine.upper() == "TRUE":
            self.underLine = 1
        else:
            self.underLine = 0
        if strikeOut.upper() == "TRUE":
            self.strikeOut = 1
        else:
            self.strikeOut = 0
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.spacing = spacing
        self.angle = angle
        self.borderStyle = borderStyle
        self.outline = outline
        self.shadow = shadow
        self.alignment = alignment
        self.marginL = marginL
        self.marginR = marginR
        self.marginV = marginV
        self.encoding = encoding
    def setScriptsFolderName(self, scriptsFolderName: str) -> None:
        self.scriptsFolderName = scriptsFolderName
    def set_ttsModel(self, ttsModel: str) -> None:
        self.ttsModel = ttsModel
    def setLanguage(self, language: str) -> None:
        self.language = language
    def setSpeed(self, speed: float) -> None:
        self.speed = speed
    def setWhisperModel(self, whisperModel: str) -> None:
        self.whisperModel = whisperModel
    def setOutputAudioName(self, outputAudioName: str) -> None:
        self.outputAudioName = outputAudioName
    def setSubtitleOutputFileName(self, subtitleOutputFileName: str) -> None:
        self.subtitleOutputFileName = subtitleOutputFileName
    def setOutputVideoName(self, outputVideoName: str) -> None:
        self.outputVideoName = outputVideoName
    def setVideoBackgroundFolder(self, videoBackgroundFolder: str) -> None:
        self.videoBackgroundFolder = videoBackgroundFolder
    def setLoopAllModels(self, loopAllModels: bool) -> None:
        self.loopAllModels = loopAllModels
    def setName(self, name: str) -> None:
        self.name = name
    def setFontName(self, fontName: str) -> None:
        self.fontName = fontName
    def setFontSize(self, fontSize: int) -> None:
        self.fontSize = fontSize
    def setPrimaryColour(self, primaryColour: str) -> None:
        self.primaryColour = primaryColour
    def setSecondaryColour(self, secondaryColour: str) -> None:
        self.secondaryColour = secondaryColour
    def setOutlineColour(self, outlineColour: str) -> None:
        self.outlineColour = outlineColour
    def setBackColour(self, backColour: str) -> None:
        self.backColour = backColour
    def setBold(self, bold: bool) -> None:
        if bold.upper() == "TRUE":
            self.bold = 1
        else:
            self.bold = 0
    def setItalic(self, italic: bool) -> None:
        if italic.upper() == "TRUE":
            self.italic = 1
        else:
            self.italic = 0
    def setUnderLine(self, underLine: bool) -> None:
        if underLine.upper() == "TRUE":
            self.underLine = 1
        else:
            self.underLine = 0
    def setstrikeOut(self, strikeOut: bool) -> None:
        if strikeOut.upper() == "TRUE":
            self.strikeOut = 1
        else:
            self.strikeOut = 0
    def setScaleX(self, scaleX: int) -> None:
        self.scaleX = scaleX
    def setScaleY(self, scaleY: int) -> None:
        self.scaleY = scaleY
    def setSpacing(self, spacing: int) -> None:
        self.spacing = spacing
    def setAngle(self, angle: int) -> None:
        self.angle = angle
    def setBorderStyle(self, borderStyle: int) -> None:
        self.borderStyle = borderStyle
    def setOutline(self, outline: int) -> None:
        self.outline = outline
    def setShadow(self, shadow: int) -> None:
        self.shadow = shadow
    def setAlignment(self, alignment: int) -> None:
        self.alignment = alignment
    def setMarginL(self, marginL: int) -> None:
        self.marginL = marginL
    def setMarginR(self, marginR: int) -> None:
        self.marginR = marginR
    def setMarginV(self, marginV: int) -> None:
        self.marginV = marginV
    def setEncoding(self, encoding: int) -> None:
        self.encoding = encoding