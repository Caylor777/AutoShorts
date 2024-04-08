def startUpScreen():
    print("          ___        _          _   _       _             ___  ___      _                   ")
    print("         / _ \      | |        | | | (_)   | |            |  \/  |     | |                  ")
    print("        / /_\ \_   _| |_ ___   | | | |_  __| | ___  ___   | .  . | __ _| | _____ _ __       ")
    print("        |  _  | | | | __/ _ \  | | | | |/ _` |/ _ \/ _ \  | |\/| |/ _` | |/ / _ \ '__|      ")
    print("        | | | | |_| | || (_) | \ \_/ / | (_| |  __/ (_) | | |  | | (_| |   <  __/ |         ")
    print("        \_| |_/\__,_|\__\___/   \___/|_|\__,_|\___|\___/  \_|  |_/\__,_|_|\_\___|_|         ")
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
                    settingsList[19].split(" = ")[1],
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
                    settingsList[41].split(" = ")[1]
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
    with open(f"{programDirectory}/{videoBackgroundLinksFileName}") as inp:
        videoBackgroundLinkList = inp.read().splitlines()
    if len(videoBackgroundLinkList) <= 0:
        sys.exit(f"No videos in \"{videoBackgroundLinkList}\" file")
    for videoLink in videoBackgroundLinkList:
        try:
            YouTube(videoLink).streams.first().download(output_path=f"{programDirectory}/{videoBackgroundFolder}")
        except:
            print("Error saving video\nRetrying...")
            try:
                YouTube(videoLink).streams.first().download(output_path=f"{programDirectory}/{videoBackgroundFolder}")
            except:
                sys.exit("ERROR: Failed to save video")
            
def loopAllModels(language: str, outputAudioName: str) -> None:
    for i in modelList:
        if i.find(language) == 11:
            print(f"Writing TTS Model {i}")
            createAudioFile(i, "My name is, " + i.replace("/", " ").replace("_", " ").replace("-", " "))
            print(f"Current TTS Model: {i}")
            audioFile = simpleaudio.WaveObject.from_wave_file(f"{programDirectory}/{outputAudioName}")
            audioPlay = audioFile.play()
            audioPlay.wait_done()
        else:
            pass
    sys.exit("All TTS models Played")
    
def createAudioFile(model: str, scriptText: str, language: str, speed: int, outputAudioName: str) -> None:
    logging.info(f"Writing file with \"{model}\" model")
    tts = TTS(model)
    if model.find("tts_models/multilingual") == 0:
        tts.tts_to_file(text=scriptText, language=language, speed=speed, file_path=outputAudioName)
    else:
        tts.tts_to_file(text=scriptText, speed=speed, file_path=outputAudioName)
        
def createSubtitles(whisperModel: str, outputAudioName: str, subtitleOutputFileName: str, language: str) -> None:
    model = WhisperModel(whisperModel)
    segments, info = model.transcribe(f"{programDirectory}/{outputAudioName}")
    language = info[0]
    print("Transcription language", info[0])
    segments = list(segments)
    for segment in segments:
        # print(segment)
        print("[%.2fs -> %.2fs] %s" %
              (segment.start, segment.end, segment.text))
    subtitle_file = f"sub-{subtitleOutputFileName}.{language}.srt"
    text = ""
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        text += f"{str(index+1)} \n"
        text += f"{segment_start} --> {segment_end} \n"
        text += f"{segment.text} \n"
        text += "\n"
    f = open(subtitle_file, "w")
    f.write(text)
    f.close()
    (
    ffmpeg
    .input(f"{programDirectory}/sub-titles.{language}.srt")
    .output(f"{programDirectory}/sub-titles.{language}.ass")
    .run(overwrite_output = True)
    )
    with open(f"{programDirectory}/sub-titles.{language}.ass") as inp:
        subtitleFileContent = inp.read().splitlines()
    subtitleFileContent[10] = f"Style: {str(settings._name)},{str(settings._fontName)},{str(settings._fontSize)},{str(settings._primaryColour)},{str(settings._secondaryColour)},{str(settings._outlineColour)},{str(settings._backColour)},{str(settings._bold)},{str(settings._italic)},{str(settings._underLine)},{str(settings._strikeOut)},{str(settings._scaleX)},{str(settings._scaleY)},{str(settings._spacing)},{str(settings._angle)},{str(settings._borderStyle)},{str(settings._outline)},{str(settings._shadow)},{str(settings._alignment)},{str(settings._marginL)},{str(settings._marginR)},{str(settings._marginV)},{str(settings._encoding)}"
    test = "\n".join(subtitleFileContent)
    f = open(f"{programDirectory}/sub-titles.{language}.ass", "w")
    f.write(test)
    f.close()
    
def makeBackgroundVideoSegment(videoBackgroundFolder: str, outputAudioName: str) -> None:
    backgroundVideoList = os.listdir(f"{programDirectory}/{videoBackgroundFolder}")
    if len(backgroundVideoList) <= 0:
        sys.exit(f"No videos in \"{videoBackgroundFolder}\" folder")
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
        sys.exit("Video background file not long enough")
    timeStamp = random.randrange(1, int(timeAvailable))
    timeStamp = timeStamp - 1
    timeStamp = int(timeStamp)
    (
    ffmpeg
    .input(f"{programDirectory}/{videoBackgroundFolder}/{videoBackground}", ss=timeStamp, t=durationAudio)
    .output('temp.mp4')
    .run(overwrite_output = True)
    )
    
def applySubtitlesToVideo(language: str, outputVideoName: str) -> None:
    (
    ffmpeg
    .input("temp.mp4")
    .filter("ass", f"sub-titles.{language}.ass")
    .output(f"{programDirectory}/TEMP{outputVideoName}")
    .run(overwrite_output = True)
    )
    os.remove(f"{programDirectory}/temp.mp4")
    
def applyAudioToVideo(outputVideoName: str, outputAudioName: str) -> None:
    (
        ffmpeg
        .input(f"{programDirectory}/TEMP{outputVideoName}")
        .concat(ffmpeg.input(f"{outputAudioName}"), a=1)
        .output(f"{programDirectory}/{outputVideoName}")
        .run(overwrite_output=True)
    )
    os.remove(f"{programDirectory}/TEMP{outputVideoName}")

if __name__ == "__main__":
    startUpScreen()
    from TTS.api import TTS
    from DefineTextFiles import scriptFile, settingsFile
    from deleteGeneratedFiles import deleteGeneratedFiles
    from loadingFunction import loadingFunction
    from faster_whisper import WhisperModel
    from pytube import YouTube
    import sys, os, logging, simpleaudio, math, ffmpeg, random
    programDirectory = (__file__.replace("\\", "/").removesuffix("/Main.py"))
    modelList = ["tts_models/bg/cv/vits", "tts_models/cs/cv/vits", "tts_models/da/cv/vits", "tts_models/et/cv/vits", "tts_models/ga/cv/vits", "tts_models/en/ek1/tacotron2", "tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/ljspeech/tacotron2-DDC_ph", "tts_models/en/ljspeech/glow-tts", "tts_models/en/ljspeech/speedy-speech", "tts_models/en/ljspeech/tacotron2-DCA", "tts_models/en/ljspeech/vits", "tts_models/en/ljspeech/vits--neon", "tts_models/en/ljspeech/fast_pitch", "tts_models/en/ljspeech/overflow", "tts_models/en/ljspeech/neural_hmm", "tts_models/en/sam/tacotron-DDC", "tts_models/en/blizzard2013/capacitron-t2-c50", "tts_models/en/blizzard2013/capacitron-t2-c150_v2", "tts_models/en/multi-dataset/tortoise-v2", "tts_models/en/jenny/jenny", "tts_models/es/mai/tacotron2-DDC", "tts_models/es/css10/vits", "tts_models/fr/mai/tacotron2-DDC", "tts_models/fr/css10/vits", "tts_models/uk/mai/glow-tts", "tts_models/uk/mai/vits", "tts_models/zh-CN/baker/tacotron2-DDC-GST", "tts_models/nl/mai/tacotron2-DDC", "tts_models/nl/css10/vits", "tts_models/de/thorsten/tacotron2-DCA", "tts_models/de/thorsten/vits", "tts_models/de/thorsten/tacotron2-DDC", "tts_models/de/css10/vits-neon", "tts_models/ja/kokoro/tacotron2-DDC", "tts_models/tr/common-voice/glow-tts", "tts_models/it/mai_female/glow-tts", "tts_models/it/mai_female/vits", "tts_models/it/mai_male/glow-tts", "tts_models/it/mai_male/vits", "tts_models/ewe/openbible/vits", "tts_models/hau/openbible/vits", "tts_models/lin/openbible/vits", "tts_models/tw_akuapem/openbible/vits", "tts_models/tw_asante/openbible/vits", "tts_models/yor/openbible/vits", "tts_models/hu/css10/vits", "tts_models/el/cv/vits", "tts_models/fi/css10/vits", "tts_models/hr/cv/vits", "tts_models/lt/cv/vits", "tts_models/lv/cv/vits", "tts_models/mt/cv/vits", "tts_models/pl/mai_female/vits", "tts_models/pt/cv/vits", "tts_models/ro/cv/vits", "tts_models/sk/cv/vits", "tts_models/sl/cv/vits", "tts_models/sv/cv/vits", "tts_models/ca/custom/vits", "tts_models/fa/custom/glow-tts", "tts_models/bn/custom/vits-male", "tts_models/bn/custom/vits-female", "tts_models/be/common-voice/glow-tts"]
    loadingClass = loadingFunction()
    deleteGeneratedFilesClass = deleteGeneratedFiles([])
    loadingClass.startLoadingAnimation()
    settings = getSettingsFileClass(programDirectory, "settings.txt")
    scriptFileList = os.listdir(f"{programDirectory}/{settings._scriptsFolderName}")
    if settings._downloadVideosInLinksFile:
        downloadBackgroudVidoes(settings._videoBackgroundLinksFileName, settings._videoBackgroundFolder)
    if settings._loopAllModels:
        loopAllModels(settings._language, settings._outputAudioName)
        loadingClass.endLoadingAnimation()
    else:
        for script in scriptFileList:
            script = getScripFileClass(programDirectory, settings._scriptsFolderName, script)
            deleteGeneratedFilesClass.deleteGeneratedFiles()
            createAudioFile(settings._ttsModel, script.scriptFileText, settings._language, settings._speed, settings._outputAudioName)
            createSubtitles(settings._whisperModel, settings._outputAudioName, settings._subtitleOutputFileName, settings._language)
            makeBackgroundVideoSegment(settings._videoBackgroundFolder, settings._outputAudioName)
            applySubtitlesToVideo(settings._language, settings._outputVideoName)
            applyAudioToVideo(settings._outputVideoName, settings._outputAudioName)
        loadingClass.endLoadingAnimation()
else:
    import sys
    sys.exit("ERROR: This is the main file, not to be imported")