def startUpScreen():
    print("                     ___        _          _____ _                _                         ")
    print("                    / _ \      | |        /  ___| |              | |                        ")
    print("                   / /_\ \_   _| |_ ___   \ `--.| |__   ___  _ __| |_ ___                   ")
    print("                   |  _  | | | | __/ _ \   `--. \ '_ \ / _ \| '__| __/ __|                  ")
    print("                   | | | | |_| | || (_) | /\__/ / | | | (_) | |  | |_\__ \                  ")
    print("                   \_| |_/\__,_|\__\___/  \____/|_| |_|\___/|_|   \__|___/                  ")
    print("                        __________                                                          ")
    print("                       |          \                                         ____________    ")
    print("                       |           \_____                               ___/            \_  ")
    print("                       |                 \                        ____/                   \ ")
    print("                       |                  |                   ___/                        / ")
    print("                       |                  |               ___/                           /  ")
    print("      ___________      |         _________/            __/         ___                 _/   ")
    print("     /           \     |        /                     |            |   \__         ___/     ")
    print("    /             |    |        |                     |            |      \__     |___      ")
    print("   /    __________|    |        |                     |            |         \        \___  ")
    print("  /    /               |        |                     \_           |       __/            \ ")
    print(" /    /                |        |                       \____      |    __/               / ")
    print("|    /                 |        |                         __/      |___/                 /  ")
    print("|   |                 /         |                      __/                            _/    ")
    print(" \   \               /          |                     |                           ___/      ")
    print("  \   \             /           /                     |                      ____/          ")
    print("   \   \___________/           /                      \                 ___/                ")
    print("    \                         /                        \           ____/                    ")
    print("     \_______            ____/                          \_________/                         ")
    print("             \__________/                                                                   ")

def crashHandler():
    loadingClass.clearDescription()
    loadingClass.endLoadingAnimation()
def exitHandler(exitCode: str):
    loadingClass.clearDescription()
    loadingClass.endLoadingAnimation()
    sys.exit(exitCode)
    
def format_time(seconds):
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
    return formatted_time

def getSettingsFileClass(programDirectory: str, settingsFileName: str) -> object:
    with open(f"{programDirectory}/{settingsFileName}") as inp:
        settingsList = inp.read().splitlines()
    settings = settingsFile(
                    settingsList[3].split(" = ")[1],
                    settingsList[4].split(" = ")[1],
                    settingsList[5].split(" = ")[1],
                    settingsList[6].split(" = ")[1],
                    settingsList[7].split(" = ")[1],
                    settingsList[8].split(" = ")[1],
                    settingsList[9].split(" = ")[1],
                    settingsList[10].split(" = ")[1],
                    settingsList[11].split(" = ")[1],
                    settingsList[12].split(" = ")[1],
                    settingsList[13].split(" = ")[1],
                    settingsList[14].split(" = ")[1],
                    settingsList[15].split(" = ")[1],
                    settingsList[16].split(" = ")[1],
                    settingsList[20].split(" = ")[1],
                    settingsList[21].split(" = ")[1],
                    settingsList[22].split(" = ")[1],
                    settingsList[23].split(" = ")[1],
                    settingsList[24].split(" = ")[1],
                    settingsList[25].split(" = ")[1],
                    settingsList[26].split(" = ")[1],
                    settingsList[27].split(" = ")[1],
                    settingsList[28].split(" = ")[1],
                    settingsList[29].split(" = ")[1],
                    settingsList[30].split(" = ")[1],
                    settingsList[31].split(" = ")[1],
                    settingsList[32].split(" = ")[1],
                    settingsList[33].split(" = ")[1],
                    settingsList[34].split(" = ")[1],
                    settingsList[35].split(" = ")[1],
                    settingsList[36].split(" = ")[1],
                    settingsList[37].split(" = ")[1],
                    settingsList[38].split(" = ")[1],
                    settingsList[39].split(" = ")[1],
                    settingsList[40].split(" = ")[1],
                    settingsList[41].split(" = ")[1],
                    settingsList[42].split(" = ")[1]
                    )
    return settings

def getScripFileClass(programDirectory: str, scriptsFolderName:str, ScriptFileName: str) -> object:
    script = scriptFile(
                        open(f"{programDirectory}/{scriptsFolderName}/{ScriptFileName}", 'r', encoding='utf-8'),
                        f"{programDirectory}/{scriptsFolderName}/{ScriptFileName}",
                        "N/A"
                       )
    script.scriptFileText = script.scriptFile.read()
    script.scriptFile.close()
    return script

def downloadBackgroudVidoes(videoBackgroundLinksFileName: str, videoBackgroundFolder: str) -> None:
    loadingClass.description = "Downloading requested video"
    with open(f"{programDirectory}/{videoBackgroundLinksFileName}") as inp:
        videoBackgroundLinkList = inp.read().splitlines()
    if len(videoBackgroundLinkList) <= 0:
        exitHandler(f"No videos in \"{videoBackgroundLinkList}\" file")
    for videoLink in videoBackgroundLinkList:
        try:
            YouTube(videoLink).streams.get_highest_resolution().download(output_path=f"{programDirectory}/{videoBackgroundFolder}")
        except:
            print("Error saving video\nRetrying...")
            try:
                YouTube(videoLink).streams.get_highest_resolution().download(output_path=f"{programDirectory}/{videoBackgroundFolder}")
            except:
                exitHandler("ERROR: Failed to save video")
    exitHandler("Download Complete")

def loopAllModels(language: str, outputAudioName: str) -> None:
    for model in modelList:
        if model.find(language) == 11:
            print(f"Writing TTS Model {model}")
            createAudioFile(model, "My name is, " + model.replace("/", " ").replace("_", " ").replace("-", " "))
            print(f"Current TTS Model: {model}")
            audioFile = simpleaudio.WaveObject.from_wave_file(f"{programDirectory}/{outputAudioName}")
            audioPlay = audioFile.play()
            audioPlay.wait_done()
        else:
            pass
    exitHandler("All TTS models Played")
    
def createAudioFile(model: str, scriptText: str, language: str, speed: int, outputAudioName: str) -> None:
    print(f"Writing file with \"{model}\" model")
    tts = TTS(model)
    if model.find("tts_models/multilingual") == 0:
        tts.tts_to_file(text=scriptText, language=language, speed=speed, file_path=outputAudioName)
    else:
        tts.tts_to_file(text=scriptText, speed=speed, file_path=outputAudioName)
        
def makeBackgroundVideoSegment(videoBackgroundFolder: str, outputAudioName: str) -> None:
    backgroundVideoList = os.listdir(f"{programDirectory}/{videoBackgroundFolder}")
    backgroundVideoList.remove("ignoreMe")
    if len(backgroundVideoList) <= 0:
        exitHandler(f"No videos in \"{videoBackgroundFolder}\" folder")
    elif len(backgroundVideoList) <= 1:
        videoBackground = backgroundVideoList[0]
    else:
        videoBackground = backgroundVideoList[random.randrange(0, len(backgroundVideoList) - 1, 1)]
    #probe audio
    probeAudio = ffmpeg.probe(f"{programDirectory}/{outputAudioName}")
    streamAudio = next((stream for stream in probeAudio['streams'] if stream['codec_type'] == 'audio'), None)
    durationAudio = float(streamAudio['duration'])
    #probe video
    probeVideo = ffmpeg.probe(f"{programDirectory}/{videoBackgroundFolder}/{videoBackground}")
    streamVideo = next((stream for stream in probeVideo['streams'] if stream['codec_type'] == 'video'), None)
    durationVideo = float(streamVideo['duration'])
    #get random time stamp
    timeAvailable = (durationVideo - durationAudio) - 1
    if timeAvailable < durationAudio:
        exitHandler("Video background file not long enough")
    timeStamp = random.randrange(1, int(timeAvailable))
    timeStamp = timeStamp - 1
    timeStamp = int(timeStamp)
    (
    ffmpeg
    .input(f"{programDirectory}/{videoBackgroundFolder}/{videoBackground}", ss=timeStamp, t=durationAudio)
    .output('TEMP.mp4')
    .run(overwrite_output = True)
    )
    
if __name__ == "__main__":
    startUpScreen()
    from TTS.api import TTS
    from videoFunctionsFFMPEG import videoFunctionsFFMPEG as editor
    from DefineTextFiles import scriptFile, settingsFile
    from deleteGeneratedFiles import deleteGeneratedFiles
    from loadingFunction import loadingFunction
    from pytube import YouTube
    import sys, os, simpleaudio, math, random, atexit, ffmpeg
    atexit.register(crashHandler)
    programDirectory = (__file__.replace("\\", "/").removesuffix("/Main.py"))
    modelList = ["tts_models/bg/cv/vits", "tts_models/cs/cv/vits", "]tts_models/da/cv/vits", "tts_models/et/cv/vits", "tts_models/ga/cv/vits", "tts_models/en/ek1/tacotron2", "tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/ljspeech/tacotron2-DDC_ph", "tts_models/en/ljspeech/glow-tts", "tts_models/en/ljspeech/speedy-speech", "tts_models/en/ljspeech/tacotron2-DCA", "tts_models/en/ljspeech/vits", "tts_models/en/ljspeech/vits--neon", "tts_models/en/ljspeech/fast_pitch", "tts_models/en/ljspeech/overflow", "tts_models/en/ljspeech/neural_hmm", "tts_models/en/sam/tacotron-DDC", "tts_models/en/blizzard2013/capacitron-t2-c50", "tts_models/en/blizzard2013/capacitron-t2-c150_v2", "tts_models/en/multi-dataset/tortoise-v2", "tts_models/en/jenny/jenny", "tts_models/es/mai/tacotron2-DDC", "tts_models/es/css10/vits", "tts_models/fr/mai/tacotron2-DDC", "tts_models/fr/css10/vits", "tts_models/uk/mai/glow-tts", "tts_models/uk/mai/vits", "tts_models/zh-CN/baker/tacotron2-DDC-GST", "tts_models/nl/mai/tacotron2-DDC", "tts_models/nl/css10/vits", "tts_models/de/thorsten/tacotron2-DCA", "tts_models/de/thorsten/vits", "tts_models/de/thorsten/tacotron2-DDC", "tts_models/de/css10/vits-neon", "tts_models/ja/kokoro/tacotron2-DDC", "tts_models/tr/common-voice/glow-tts", "tts_models/it/mai_female/glow-tts", "tts_models/it/mai_female/vits", "tts_models/it/mai_male/glow-tts", "tts_models/it/mai_male/vits", "tts_models/ewe/openbible/vits", "tts_models/hau/openbible/vits", "tts_models/lin/openbible/vits", "tts_models/tw_akuapem/openbible/vits", "tts_models/tw_asante/openbible/vits", "tts_models/yor/openbible/vits", "tts_models/hu/css10/vits", "tts_models/el/cv/vits", "tts_models/fi/css10/vits", "tts_models/hr/cv/vits", "tts_models/lt/cv/vits", "tts_models/lv/cv/vits", "tts_models/mt/cv/vits", "tts_models/pl/mai_female/vits", "tts_models/pt/cv/vits", "tts_models/ro/cv/vits", "tts_models/sk/cv/vits", "tts_models/sl/cv/vits", "tts_models/sv/cv/vits", "tts_models/ca/custom/vits", "tts_models/fa/custom/glow-tts", "tts_models/bn/custom/vits-male", "tts_models/bn/custom/vits-female", "tts_models/be/common-voice/glow-tts"]
    loadingClass = loadingFunction()
    deleteGeneratedFilesClass = deleteGeneratedFiles([])
    loadingClass.startLoadingAnimation()
    settings = getSettingsFileClass(programDirectory, "settings.txt")
    scriptFileList = os.listdir(f"{programDirectory}/{settings._scriptsFolderName}")
    if settings._downloadVideosInLinksFile:
        downloadBackgroudVidoes(settings._videoBackgroundLinksFileName, settings._videoBackgroundFolderName)
    if settings._loopAllModels:
        loopAllModels(settings._language, settings._outputAudioName)
        loadingClass.endLoadingAnimation()
        exitHandler()
    else:
        for i in range(0, len(scriptFileList)):
            script = getScripFileClass(programDirectory, settings._scriptsFolderName, scriptFileList[i])
            deleteGeneratedFilesClass.deleteGeneratedFiles()
            createAudioFile(settings._ttsModel, script.scriptFileText, settings._language, settings._speed, settings._outputAudioName)
            editor.createSubtitles(programDirectory, settings._whisperModel, settings._outputAudioName, settings._subtitleOutputFileName, settings._language)
            editor.formatAssFile(f"{programDirectory}/sub-titles.{settings._language}.ass", settings._name, settings._fontName, settings._fontSize, settings._primaryColour, settings._secondaryColour, settings._outlineColour, settings._backColour, settings._bold, settings._italic, settings._underLine, settings._strikeOut, settings._scaleX, settings._scaleY, settings._spacing, settings._angle, settings._borderStyle, settings._outline, settings._shadow, settings._alignment, settings._marginL, settings._marginR, settings._marginV, settings._encoding)
            makeBackgroundVideoSegment(settings._videoBackgroundFolderName, settings._outputAudioName)
            editor.changeVideoResolution("9:16", f"{programDirectory}/TEMP.mp4", f"{programDirectory}/{settings._outputVideoName}")
            editor.applySubtitlesToVideo(f"sub-titles.{settings._language}.ass", f"{programDirectory}/{settings._outputVideoName}", f"{programDirectory}/TEMP.mp4")
            editor.applyAudioToVideo(f"{programDirectory}/TEMP.mp4", f"{programDirectory}/{settings._outputAudioName}", f"{programDirectory}/{settings._outputVideoFolderName}/#{i + 1}{settings._outputVideoName}")
            os.remove(f"{programDirectory}/TEMP.mp4")
        deleteGeneratedFilesClass.deleteGeneratedFiles()
        loadingClass.endLoadingAnimation()
        exitHandler("All Tasks Completed")
else:
    import sys
    sys.exit("ERROR: This is the main file, not to be imported")