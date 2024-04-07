from DefineTextFiles import settingsFile
import os
class deleteGeneratedFiles:
    def __init__(self, tempFiles: list) -> None:
        self.tempFiles = tempFiles
        self.programDirectory = (__file__.replace("\\", "/").removesuffix("/deleteGeneratedFiles.py"))
        with open(f"{self.programDirectory}/settings.txt") as inp:
            self.settingsList = inp.read().splitlines()
        self.settings = settingsFile(
                                    self.settingsList[3].split(" = ")[1],
                                    self.settingsList[4].split(" = ")[1],
                                    self.settingsList[5].split(" = ")[1],
                                    self.settingsList[6].split(" = ")[1],
                                    self.settingsList[7].split(" = ")[1],
                                    self.settingsList[8].split(" = ")[1],
                                    self.settingsList[9].split(" = ")[1],
                                    self.settingsList[10].split(" = ")[1],
                                    self.settingsList[11].split(" = ")[1],
                                    self.settingsList[12].split(" = ")[1],
                                    self.settingsList[13].split(" = ")[1],
                                    self.settingsList[14].split(" = ")[1],
                                    self.settingsList[15].split(" = ")[1],
                                    self.settingsList[19].split(" = ")[1],
                                    self.settingsList[20].split(" = ")[1],
                                    self.settingsList[21].split(" = ")[1],
                                    self.settingsList[22].split(" = ")[1],
                                    self.settingsList[23].split(" = ")[1],
                                    self.settingsList[24].split(" = ")[1],
                                    self.settingsList[25].split(" = ")[1],
                                    self.settingsList[26].split(" = ")[1],
                                    self.settingsList[27].split(" = ")[1],
                                    self.settingsList[28].split(" = ")[1],
                                    self.settingsList[29].split(" = ")[1],
                                    self.settingsList[30].split(" = ")[1],
                                    self.settingsList[31].split(" = ")[1],
                                    self.settingsList[32].split(" = ")[1],
                                    self.settingsList[33].split(" = ")[1],
                                    self.settingsList[34].split(" = ")[1],
                                    self.settingsList[35].split(" = ")[1],
                                    self.settingsList[36].split(" = ")[1],
                                    self.settingsList[37].split(" = ")[1],
                                    self.settingsList[38].split(" = ")[1],
                                    self.settingsList[39].split(" = ")[1],
                                    self.settingsList[40].split(" = ")[1],
                                    self.settingsList[41].split(" = ")[1]
                                   )
    def deleteGeneratedFiles(self) -> None:
        try:
            os.remove(f"{self.programDirectory}/{self.settings._outputAudioName}")
        except:
            pass
        try:
            os.remove(f"{self.programDirectory}/sub-titles.{self.settings._language}.srt")
        except:
            pass
        try:
            os.remove(f"{self.programDirectory}/sub-titles.{self.settings._language}.ass")
        except:
            pass
        try:
            os.remove(f"{self.programDirectory}/{self.settings._outputVideoName}")
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