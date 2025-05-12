import customtkinter, time

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
        
class tkTopLevelWinodwLoadingAnimation:
    import customtkinter, time, threading
    def __init__(self, function: object, description: str, successMessage: str, font: str, fontSize: int):
        self.function = function
        self.description = description
        self.successMessage = successMessage
        self.font = font
        self.fontSize = fontSize
        
    
    def loadingWindow(self):
        currentCharacterList = ["|", "/", "-", "\\"]
        currentCharacter = 0
        new_window=self.customtkinter.CTkToplevel()
        new_window.title("Loading Animation")
        label=self.customtkinter.CTkLabel(new_window, font=(self.font, self.fontSize), text=f"{self.description} \\ ")
        label.pack()
        new_window.after(20, new_window.lift)
        downloading = self.threading.Thread(target=self.function)
        downloading.start()
        while downloading.is_alive():
            label.configure(text=f"{self.description} {currentCharacterList[currentCharacter]} ")
            self.time.sleep(0.1)
            if currentCharacter >= len(currentCharacterList) - 1:
                currentCharacter = 0
            else:
                currentCharacter = currentCharacter + 1
        label.configure(text=self.successMessage)
        self.time.sleep(1)
        new_window.destroy()
        
class topLevelWindowError:
    def raiseError(description):
        new_window=customtkinter.CTkToplevel()
        new_window.title("ERROR")
        label = customtkinter.CTkLabel(new_window, font=("Roboto", 50), text=f"{description}")
        label.pack()
        new_window.after(20, new_window.lift)
        time.sleep(3)
        new_window.destroy()