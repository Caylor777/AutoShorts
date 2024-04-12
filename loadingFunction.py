class loadingFunction:
    import sys, time, threading
    def __init__(self) -> None:
        self.isLoading = False
        self.currentCharacterList = ["| ", "/ ", "- ", "\\ "]
        self.currentCharacter = 0
        self.loadingThread = self.threading.Thread(target=self.loadingAnimation)
        self.description = "loading"
    def setLoading(self, isLoading: bool) -> None:
        self.isLoading = isLoading
    def loadingAnimation(self) -> None:
        print("\n")
        while self.isLoading:
            self.sys.stdout.write(f"\r{self.description} {self.currentCharacterList[self.currentCharacter]}")
            self.sys.stdout.flush()
            self.time.sleep(0.1)
            if self.currentCharacter >= len(self.currentCharacterList) - 1:
                self.currentCharacter = 0
            else:
                self.currentCharacter = self.currentCharacter + 1
    def startLoadingAnimation(self) -> None:
        self.isLoading = True
        self.loadingThread.start()
    def endLoadingAnimation(self) -> None:
        self.isLoading = False
        self.loadingThread.join()
    def setDescription(self, description: str):
        self.description = description
    def clearDescription(self):
        self.description = "loading"       