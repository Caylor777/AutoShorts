from TTS.api import TTS
from videoFunctionsFFMPEG import videoFunctionsFFMPEG
from deleteGeneratedFiles import deleteGeneratedFiles
from utils import loadingFunction
from utils import topLevelWindowError
from pytubefix import YouTube
import sys, os, simpleaudio, random, atexit, ffmpeg, json

modelList = ["tts_models/bg/cv/vits", "tts_models/cs/cv/vits", "tts_models/da/cv/vits", "tts_models/et/cv/vits", "tts_models/ga/cv/vits", "tts_models/en/ek1/tacotron2", "tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/ljspeech/tacotron2-DDC_ph", "tts_models/en/ljspeech/glow-tts", "tts_models/en/ljspeech/speedy-speech", "tts_models/en/ljspeech/tacotron2-DCA", "tts_models/en/ljspeech/vits", "tts_models/en/ljspeech/vits--neon", "tts_models/en/ljspeech/fast_pitch", "tts_models/en/ljspeech/overflow", "tts_models/en/ljspeech/neural_hmm", "tts_models/en/sam/tacotron-DDC", "tts_models/en/blizzard2013/capacitron-t2-c50", "tts_models/en/blizzard2013/capacitron-t2-c150_v2", "tts_models/en/multi-dataset/tortoise-v2", "tts_models/en/jenny/jenny", "tts_models/es/mai/tacotron2-DDC", "tts_models/es/css10/vits", "tts_models/fr/mai/tacotron2-DDC", "tts_models/fr/css10/vits", "tts_models/uk/mai/glow-tts", "tts_models/uk/mai/vits", "tts_models/zh-CN/baker/tacotron2-DDC-GST", "tts_models/nl/mai/tacotron2-DDC", "tts_models/nl/css10/vits", "tts_models/de/thorsten/tacotron2-DCA", "tts_models/de/thorsten/vits", "tts_models/de/thorsten/tacotron2-DDC", "tts_models/de/css10/vits-neon", "tts_models/ja/kokoro/tacotron2-DDC", "tts_models/tr/common-voice/glow-tts", "tts_models/it/mai_female/glow-tts", "tts_models/it/mai_female/vits", "tts_models/it/mai_male/glow-tts", "tts_models/it/mai_male/vits", "tts_models/ewe/openbible/vits", "tts_models/hau/openbible/vits", "tts_models/lin/openbible/vits", "tts_models/tw_akuapem/openbible/vits", "tts_models/tw_asante/openbible/vits", "tts_models/yor/openbible/vits", "tts_models/hu/css10/vits", "tts_models/el/cv/vits", "tts_models/fi/css10/vits", "tts_models/hr/cv/vits", "tts_models/lt/cv/vits", "tts_models/lv/cv/vits", "tts_models/mt/cv/vits", "tts_models/pl/mai_female/vits", "tts_models/pt/cv/vits", "tts_models/ro/cv/vits", "tts_models/sk/cv/vits", "tts_models/sl/cv/vits", "tts_models/sv/cv/vits", "tts_models/ca/custom/vits", "tts_models/fa/custom/glow-tts", "tts_models/bn/custom/vits-male", "tts_models/bn/custom/vits-female", "tts_models/be/common-voice/glow-tts"]

class autoShorts:
    def __init__(self):
        self.programDirectory = os.path.dirname(os.path.abspath(__file__))
        self.loadingClass = loadingFunction()
        self.startUpScreen()
        atexit.register(self.crashHandler)
        f = open("settings.json")
        self.settings = json.load(f)
        f.close()
        self.deleteGeneratedFilesClass = deleteGeneratedFiles([])
        self.startUpScreen()
        
    def run(self):
        self.loadingClass.startLoadingAnimation()
        scriptFileList = os.listdir(self.settings["scriptsFolderName"])
        for i in range(0, len(scriptFileList)):
            script = self.getScripFile(self.programDirectory, self.settings["scriptsFolderName"], scriptFileList[i])
            self.deleteGeneratedFilesClass.deleteGeneratedFiles()
            self.createAudioFile(self.settings["ttsModel"], script, self.settings["language"], self.settings["speed"], self.settings["outputAudioName"])
            videoFunctionsFFMPEG.createSubtitles(self.programDirectory, self.settings["whisperModel"], self.settings["outputAudioName"], self.settings["subtitleOutputFileName"], self.settings["language"])
            videoFunctionsFFMPEG.formatAssFile("sub-titles.%(language)s.ass" % self.settings, self.settings["Name"], self.settings["Fontname"], self.settings["Fontsize"], self.settings["PrimaryColour"], self.settings["SecondaryColour"], self.settings["OutlineColour"], self.settings["BackColour"], self.settings["Bold"], self.settings["Italic"], self.settings["UnderLine"], self.settings["StrikeOut"], self.settings["ScaleX"], self.settings["ScaleY"], self.settings["Spacing"], self.settings["Angle"], self.settings["BorderStyle"], self.settings["Outline"], self.settings["Shadow"], self.settings["Alignment"], self.settings["MarginL"], self.settings["MarginR"], self.settings["MarginV"], self.settings["Encoding"])
            self.makeBackgroundVideoSegment(self.settings["backgroundVideoFolderName"], self.settings["outputAudioName"])
            videoFunctionsFFMPEG.changeVideoResolution("9:16", "TEMP.mp4", self.settings["outputVideoName"])
            videoFunctionsFFMPEG.applySubtitlesToVideo("sub-titles.%(language)s.ass" % self.settings, self.settings["outputVideoName"], "TEMP.mp4")
            videoName = self.settings["outputVideoName"].split(".")
            videoName1 = videoName[0] + str(i + 1)
            for i in range(1, len(videoName)):
                videoName1 = f"{videoName1}.{videoName[i]}"
            videoFunctionsFFMPEG.applyAudioToVideo(f"{self.programDirectory}/TEMP.mp4", self.settings["outputAudioName"], videoName1)
            os.replace(videoName1, self.settings["outputVideoFolderName"] + "\\" + videoName1)
            os.remove(f"{self.programDirectory}/TEMP.mp4")
        self.deleteGeneratedFilesClass.deleteGeneratedFiles()
        self.loadingClass.endLoadingAnimation()
        self.exitHandler("All Tasks Completed")
           
    def startUpScreen(self):
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
    def crashHandler(self):
        self.loadingClass.clearDescription()
        self.loadingClass.endLoadingAnimation()
    def exitHandler(self, exitCode: str):
        self.loadingClass.clearDescription()
        self.loadingClass.endLoadingAnimation()
        sys.exit(exitCode)
        
    def getScripFile(self, programDirectory: str, scriptsFolderName:str, ScriptFileName: str) -> object:
        f = (open(f"{programDirectory}/{scriptsFolderName}/{ScriptFileName}", 'r', encoding='utf-8'))
        script = f.read()
        f.close()
        return script
        
    def createAudioFile(self, model: str, scriptText: str, language: str, speed: int, outputAudioName: str) -> None:
        print(f"Writing file with \"{model}\" model")
        tts = TTS(model)
        if model.find("tts_models/multilingual") == 0:
            tts.tts_to_file(text=scriptText, language=language, speed=speed, file_path=outputAudioName)
        else:
            tts.tts_to_file(text=scriptText, speed=speed, file_path=outputAudioName)
            
    def makeBackgroundVideoSegment(self, videoBackgroundFolder: str, outputAudioName: str) -> None:
        backgroundVideoList = os.listdir(f"{self.programDirectory}/{videoBackgroundFolder}")
        backgroundVideoList.remove("ignoreMe")
        if len(backgroundVideoList) <= 0:
            self.exitHandler(f"No videos in \"{videoBackgroundFolder}\" folder")
        elif len(backgroundVideoList) <= 1:
            videoBackground = backgroundVideoList[0]
        else:
            videoBackground = backgroundVideoList[random.randrange(0, len(backgroundVideoList) - 1, 1)]
        #probe audio
        probeAudio = ffmpeg.probe(f"{self.programDirectory}/{outputAudioName}")
        streamAudio = next((stream for stream in probeAudio['streams'] if stream['codec_type'] == 'audio'), None)
        durationAudio = float(streamAudio['duration'])
        #probe video
        probeVideo = ffmpeg.probe(f"{self.programDirectory}/{videoBackgroundFolder}/{videoBackground}")
        streamVideo = next((stream for stream in probeVideo['streams'] if stream['codec_type'] == 'video'), None)
        durationVideo = float(streamVideo['duration'])
        #get random time stamp
        timeAvailable = (durationVideo - durationAudio) - 1
        if timeAvailable < durationAudio:
            if __name__ == "__main__":
                autoShorts.exitHandler("Video background file not long enough")
            else:
                topLevelWindowError.raiseError("Video background file not long enough")
        timeStamp = random.randrange(1, int(timeAvailable))
        timeStamp = timeStamp - 1
        timeStamp = int(timeStamp)
        (
        ffmpeg
        .input(f"{self.programDirectory}/{videoBackgroundFolder}/{videoBackground}", ss=timeStamp, t=durationAudio)
        .output('TEMP.mp4')
        .run(overwrite_output = True)
        )
        
class shortsUtils(autoShorts):
    def loopAllModels(self, language: str, outputAudioName: str) -> None:
            for model in modelList:
                if model.find(language) == 11:
                    try:
                        print(f"Writing TTS Model {model}")
                        autoShorts.createAudioFile(model, "My name is, " + model.replace("/", " ").replace("_", " ").replace("-", " "), settings._language, settings._speed, f"{self.programDirectory}/sample.wav")
                        print(f"Current TTS Model: {model}")
                        audioFile = simpleaudio.WaveObject.from_wave_file(f"{self.programDirectory}/sample.wav")
                        audioPlay = audioFile.play()
                        audioPlay.wait_done()
                    except:
                        pass
                else:
                    pass
            autoShorts.exitHandler("All TTS models Played")
            
    def downloadBackgroudVidoes() -> None: 
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        loadingClass = loadingFunction()
        loadingClass.startLoadingAnimation()
        loadingClass.description = "Downloading requested video(s)"
        if len(settings["backgroundVideoList"]) <= 0:
            loadingClass.endLoadingAnimation()
            if __name__ == "__main__":
                raise Exception("No videos in background videos list")
            else:
                topLevelWindowError.raiseError("ERROR: No videos in background videos list")
        for videoLink in settings["backgroundVideoList"]:
            try:
                yt = YouTube(videoLink)
            except:
                if __name__ == "__main__":
                    raise Exception("Connection Error")
                else:
                    topLevelWindowError.raiseError("ERROR: Connection Error")
            downloadVideo = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            try:
                downloadVideo.download(output_path=settings["backgroundVideoFolderName"])
            except:
                if __name__ == "__main__":
                    print("Failed to download video(s)")
                else:
                    topLevelWindowError.raiseError("ERROR: Failed To Download Video(s)")
        print("Video(s) Saved")
        loadingClass.endLoadingAnimation()
    
if __name__ == "__main__":
    f = open("settings.json")
    settings = json.load(f)
    f.close()
    if (sys.argv.count("downloadVideos") > 0):
            shortsUtils.downloadBackgroudVidoes()
    elif (sys.argv.count("loopAllModels") > 0):
        shortsUtils.loopAllModels(settings["language"], settings["outputAudioName"])
        raise Exception("Opreation Complete")
    elif (sys.argv.count("run") > 0):
        main = autoShorts()
        main.run()
    else:
        raise Exception("no vaild arguments recived")