import tkinter
import tkinter.messagebox
import customtkinter
import main, json, os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
modelList = ["tts_models/bg/cv/vits", "tts_models/cs/cv/vits", "tts_models/da/cv/vits", "tts_models/et/cv/vits", "tts_models/ga/cv/vits", "tts_models/en/ek1/tacotron2", "tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/ljspeech/tacotron2-DDC_ph", "tts_models/en/ljspeech/glow-tts", "tts_models/en/ljspeech/speedy-speech", "tts_models/en/ljspeech/tacotron2-DCA", "tts_models/en/ljspeech/vits", "tts_models/en/ljspeech/vits--neon", "tts_models/en/ljspeech/fast_pitch", "tts_models/en/ljspeech/overflow", "tts_models/en/ljspeech/neural_hmm", "tts_models/en/sam/tacotron-DDC", "tts_models/en/blizzard2013/capacitron-t2-c50", "tts_models/en/blizzard2013/capacitron-t2-c150_v2", "tts_models/en/multi-dataset/tortoise-v2", "tts_models/en/jenny/jenny", "tts_models/es/mai/tacotron2-DDC", "tts_models/es/css10/vits", "tts_models/fr/mai/tacotron2-DDC", "tts_models/fr/css10/vits", "tts_models/uk/mai/glow-tts", "tts_models/uk/mai/vits", "tts_models/zh-CN/baker/tacotron2-DDC-GST", "tts_models/nl/mai/tacotron2-DDC", "tts_models/nl/css10/vits", "tts_models/de/thorsten/tacotron2-DCA", "tts_models/de/thorsten/vits", "tts_models/de/thorsten/tacotron2-DDC", "tts_models/de/css10/vits-neon", "tts_models/ja/kokoro/tacotron2-DDC", "tts_models/tr/common-voice/glow-tts", "tts_models/it/mai_female/glow-tts", "tts_models/it/mai_female/vits", "tts_models/it/mai_male/glow-tts", "tts_models/it/mai_male/vits", "tts_models/ewe/openbible/vits", "tts_models/hau/openbible/vits", "tts_models/lin/openbible/vits", "tts_models/tw_akuapem/openbible/vits", "tts_models/tw_asante/openbible/vits", "tts_models/yor/openbible/vits", "tts_models/hu/css10/vits", "tts_models/el/cv/vits", "tts_models/fi/css10/vits", "tts_models/hr/cv/vits", "tts_models/lt/cv/vits", "tts_models/lv/cv/vits", "tts_models/mt/cv/vits", "tts_models/pl/mai_female/vits", "tts_models/pt/cv/vits", "tts_models/ro/cv/vits", "tts_models/sk/cv/vits", "tts_models/sl/cv/vits", "tts_models/sv/cv/vits", "tts_models/ca/custom/vits", "tts_models/fa/custom/glow-tts", "tts_models/bn/custom/vits-male", "tts_models/bn/custom/vits-female", "tts_models/be/common-voice/glow-tts"]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Auto Shorts")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Auto Shorts", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.saveScripts_button = customtkinter.CTkButton(self.sidebar_frame, text="Save Script Edits", command=self.updateScripts)
        self.saveScripts_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_script_select = customtkinter.CTkOptionMenu(self.sidebar_frame, command=self.scriptSelectHandler, values=["test", "Test2"])
        self.sidebar_script_select.grid(row=2, column=0, padx=20, pady=10)
        #place hold
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, state="normal")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=15, rowspan=3, sticky="nsew")
        self.tabview.add("Settings")
        self.tabview.add("Subtitle Settings")
        self.tabview.add("Dictionary")
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Subtitle Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Dictionary").grid_columnconfigure(0, weight=1) 
        #settings tab
        self.scrollable_frame_settings_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Settings"), height=420)
        self.scrollable_frame_settings_tab.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_settings_tab.grid_columnconfigure(0, weight=1)
        self.ttsModel_dropdown = customtkinter.CTkOptionMenu(self.scrollable_frame_settings_tab, values=["TTS Model:"] + modelList, command=self.ttsModelHandler)
        self.ttsModel_dropdown.grid(row=1, column=0, padx=0, pady=10)
        self.whisperModel_input_dropdown = customtkinter.CTkOptionMenu(self.scrollable_frame_settings_tab, values=["Whisper Model:", "tiny", "base", "small", "medium", "large"], command=self.whisperModelHandler)
        self.whisperModel_input_dropdown.grid(row=2, column=0, padx=0, pady=10)
        self.scriptsFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Scripts Folder Name: N/A", command=self.scriptsFolderHandler)
        self.scriptsFolderName_input_button.grid(row=3, column=0, padx=0, pady=10)
        self.speed_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="TTS Speed: N/A", command=self.ttsSpeedHandler)
        self.speed_input_button.grid(row=4, column=0, padx=0, pady=10)
        self.outputAudioFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Audio File Name: N/A", command=self.outputAudioHandler)
        self.outputAudioFileName_input_button.grid(row=5, column=0, padx=0, pady=10)
        self.subtitleOutputFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Subtitle File Name: N/A", command=self.outputSubtitleHandler)
        self.subtitleOutputFileName_input_button.grid(row=6, column=0, padx=0, pady=10)
        self.outputVideoFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Video File Name: N/A", command=self.outputVideoHandler)
        self.outputVideoFileName_input_button.grid(row=7, column=0, padx=0, pady=10)
        self.outputVideoFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Video Folder Name: N/A", command=self.outputVideoFolderHandler)
        self.outputVideoFolderName_input_button.grid(row=8, column=0, padx=0, pady=10)
        self.backgroundVideoFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Background Video Folder Name: N/A", command=self.backgroundVideoFolderHandler)
        self.backgroundVideoFolderName_input_button.grid(row=9, column=0, padx=0, pady=10)
        self.test = customtkinter.CTkBaseClass(self.scrollable_frame_settings_tab, height=25)
        self.test.grid(row=10, column=0, padx=0, pady=10)
        self.backgroundVideoList_input_feild = customtkinter.CTkEntry(self.scrollable_frame_settings_tab, placeholder_text="Youtube Video Link")
        self.backgroundVideoList_input_feild.place_configure(x=10, y=665)
        self.backgroundVideoList_input_feild_submit_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, anchor="e", width=50, text="Submit", command=self.backgroundVideoListHandler)
        self.backgroundVideoList_input_feild_submit_button.place_configure(x=235, y=665)
        #Subtitle Settings tab
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Subtitle Settings"), text="CTkLabel on Subtitle Settings")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        #Dictionary tab
        self.scrollable_frame_Tab3 = customtkinter.CTkScrollableFrame(self.tabview.tab("Dictionary"), height=420)
        self.scrollable_frame_Tab3.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_Tab3.grid_columnconfigure(0, weight=0)
        self.scrollable_frame_switches_Tab3 = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame_Tab3, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches_Tab3.append(switch)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")
        
        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        self.scriptsFolderName_input_button.configure(text="Scripts Folder Name: %(scriptsFolderName)s" % settings)
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3", "Value 4", "Vaule 5"])
        self.seg_button_1.set("Value 2")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def updateScripts(self):
        print("update scripts")

    def scriptSelectHandler(self, value):
        print(f"selected {value}")
        
    def scriptsFolderHandler(self):
        pathExists = False
        prompt = "Enter Scripts Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.ScriptsFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.scriptsFolderName_input_button.configure(text=f"Scripts Folder Name: {dialogInput}")
    
    def ttsModelHandler(self, value):
        print(f"tts model: {value}")
        
    def ttsSpeedHandler(self):
        numeric = False
        prompt = "Enter TTS Speed: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.ttsSpeed")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.speed_input_button.configure(text=f"TTS Speed: {dialogInput}")
        
    def whisperModelHandler(self, value):
        print(f"whisper model: {value}")
        
    def outputAudioHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Audio File Name:", title="Settings.outputAudioFileName")
        dialogInput = dialog.get_input()
        dialogInput = dialogInput.split(".")[0]
        dialogInput = f"{dialogInput}.mp3"
        self.outputAudioFileName_input_button.configure(text=f"Output Audio File Name: {dialogInput}")
        
    def outputSubtitleHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Subtitle File Name:", title="Settings.outputSubtitleFileName")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.subtitleOutputFileName_input_button.configure(text=f"Output Subtitle File Name: {dialogInput}")
        
    def outputVideoHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Video File Name:", title="Settings.outputVideoFileName")
        dialogInput = dialog.get_input()
        dialogInput = dialogInput.split(".")[0]
        dialogInput = f"{dialogInput}.mp4"
        self.outputVideoFileName_input_button.configure(text=f"Output Video File Name: {dialogInput}")
        
    def outputVideoFolderHandler(self):
        pathExists = False
        prompt = "Enter Video Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.outputVideoFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.outputVideoFolderName_input_button.configure(text=f"Output Video Folder Name: {dialogInput}")
        
    def backgroundVideoFolderHandler(self):
        pathExists = False
        prompt = "Enter Background Video Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.backgroundVideoFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.backgroundVideoFolderName_input_button.configure(text=f"Background Video Folder Name: {dialogInput}")
    
    def backgroundVideoListHandler(self):
        input = self.backgroundVideoList_input_feild.get()
        self.backgroundVideoList_input_feild.clear

if __name__ == "__main__":
    app = App()
    app.mainloop()
