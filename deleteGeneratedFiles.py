import os, json
class deleteGeneratedFiles:
    def __init__(self, tempFiles: list) -> None:
        self.tempFiles = tempFiles
        self.programDirectory = (__file__.replace("\\", "/").removesuffix("/deleteGeneratedFiles.py"))
        f = open("settings.json")
        self.settings = json.load(f)
        f.close()
    def deleteGeneratedFiles(self) -> None:
        try:
            os.remove(self.programDirectory + "/%(outputAudioName)s" % self.settings)
        except:
            pass
        try:
            os.remove(self.programDirectory + "/sub-titles.%(language)s.srt" % self.settings)
        except:
            pass
        try:
            os.remove(self.programDirectory + "/sub-titles.%(language)s.ass" % self.settings)
        except:
            pass
        try:
            os.remove(self.programDirectory + "/%(outputVideoName)s" % self.settings)
        except:
            pass
        if self.tempFiles == []:
            pass
        else:
            for i in self.tempFiles:
                try:
                    os.remove(f"{self.programDirectory}/{i}")
                except:
                    pass

#If you want to run the file stand alone
if __name__ == '__main__':
    from deleteGeneratedFiles import deleteGeneratedFiles
    deleteGeneratedFilesClass = deleteGeneratedFiles([])
    deleteGeneratedFilesClass.deleteGeneratedFiles()