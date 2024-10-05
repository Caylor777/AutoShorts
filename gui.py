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
        self.backgroundVideoLink_input_comboBox = customtkinter.CTkComboBox(self.scrollable_frame_settings_tab, width=300, values=["Background Video Links:", ""], command=self.backgroundVideoListActiveIndexSetter)
        self.backgroundVideoLink_input_comboBox.grid(row=10, column=0, padx=0, pady=10)
        self.backgroundVideoLink_input_comboBox.bind("<KeyRelease>", self.backgroundVideoListHandler)
        #Subtitle Settings tab
        self.scrollable_frame_subtitle_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Subtitle Settings"), height=420)
        self.scrollable_frame_subtitle_tab.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_subtitle_tab.grid_columnconfigure(0, weight=1)
        self.name_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Name: N/A", command=self.nameHandler)
        self.name_input_button.grid(row=0, column=0, padx=0, pady=10)
        self.fontname_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Font Name: N/A", command=self.fontnameHandler)
        self.fontname_input_button.grid(row=1, column=0, padx=0, pady=10)
        self.fontsize_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Font Size: N/A", command=self.fontsizeHandler)
        self.fontsize_input_button.grid(row=2, column=0, padx=0, pady=10)
        self.primaryColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Primary Color: N/A", command=self.primaryColorHandler)
        self.primaryColor_input_button.grid(row=3, column=0, padx=0, pady=10)
        self.secondaryColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Secondary Color: N/A", command=self.secondaryColorHandler)
        self.secondaryColor_input_button.grid(row=4, column=0, padx=0, pady=10)
        self.outlineColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Outline Color: N/A", command=self.outlineColorHandler)
        self.outlineColor_input_button.grid(row=5, column=0, padx=0, pady=10)
        self.backColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Back Color: N/A", command=self.backColorHandler)
        self.backColor_input_button.grid(row=5, column=0, padx=0, pady=10)
        self.scaleX_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Scale X: N/A", command=self.scaleXHandler)
        self.scaleX_input_button.grid(row=6, column=0, padx=0, pady=10)
        self.scaleY_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Scale Y: N/A", command=self.scaleYHandler)
        self.scaleY_input_button.grid(row=7, column=0, padx=0, pady=10)
        self.spacing_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Spacing: N/A", command=self.spacingHandler)
        self.spacing_input_button.grid(row=8, column=0, padx=0, pady=10)
        self.angle_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Angle: N/A", command=self.angleHandler)
        self.angle_input_button.grid(row=9, column=0, padx=0, pady=10)
        self.borderStyle_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Border Style: N/A", command=self.borderStyleHandler)
        self.borderStyle_input_button.grid(row=10, column=0, padx=0, pady=10)
        self.outline_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Outline: N/A", command=self.outlineHandler)
        self.outline_input_button.grid(row=11, column=0, padx=0, pady=10)
        self.shadow_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Shadow: N/A", command=self.shadowHandler)
        self.shadow_input_button.grid(row=12, column=0, padx=0, pady=10)
        self.alignment_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Alignment: N/A", command=self.alignmentHandler)
        self.alignment_input_button.grid(row=13, column=0, padx=0, pady=10)
        self.marginL_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Left: N/A", command=self.marginLHandler)
        self.marginL_input_button.grid(row=14, column=0, padx=0, pady=10)
        self.marginR_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Right: N/A", command=self.marginRHandler)
        self.marginR_input_button.grid(row=15, column=0, padx=0, pady=10)
        self.marginV_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Vertical: N/A", command=self.marginVHandler)
        self.marginV_input_button.grid(row=16, column=0, padx=0, pady=10)
        self.encoding_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Encoding: N/A", command=self.encodingHandler)
        self.encoding_input_button.grid(row=17, column=0, padx=0, pady=10)
        self.bold_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="Bold", command=self.boldHandler)
        self.bold_checkbox.grid(row=18, column=0, padx=0, pady=10)
        self.italic_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="Italic", command=self.italicHandler)
        self.italic_checkbox.grid(row=19, column=0, padx=0, pady=10)
        self.underLine_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="UnderLine", command=self.underLineHandler)
        self.underLine_checkbox.grid(row=20, column=0, padx=0, pady=10)
        self.strikeOut_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="StrikeOut", command=self.strikeOutHandler)
        self.strikeOut_checkbox.grid(row=21, column=0, padx=0, pady=10)
        #Dictionary tab
        self.dictEntrys = 0
        self.scrollable_frame_dictionary_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Dictionary"), height=420)
        self.scrollable_frame_dictionary_tab.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_dictionary_tab.grid_columnconfigure(0, weight=1)
        self.dictionary_entry_placehold = customtkinter.CTkBaseClass(self.scrollable_frame_dictionary_tab, height=10)
        self.dictionary_entry_placehold.grid(row=0, column=0, padx=0, pady=10)
        self.dictionaryKey_entry = customtkinter.CTkEntry(self.scrollable_frame_dictionary_tab, placeholder_text="Key", width=75)
        self.dictionaryKey_entry.place_configure(x=0)
        self.dictionary_colon_label = customtkinter.CTkLabel(self.scrollable_frame_dictionary_tab, text=":")
        self.dictionary_colon_label.place(x=77)
        self.dictionaryDef_entry = customtkinter.CTkEntry(self.scrollable_frame_dictionary_tab, placeholder_text="Def", width=75)
        self.dictionaryDef_entry.place_configure(x=125)
        self.dictionary_add_button = customtkinter.CTkButton(self.scrollable_frame_dictionary_tab, width=50, text="add", command=self.addDictionaryEntry)
        self.dictionary_add_button.place(x=165)
        
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
        
    def backgroundVideoListActiveIndexSetter(self, value):
        options = self.backgroundVideoLink_input_comboBox._values
        index = options.index(value)
        self.backgroundVideoLink_input_comboBox._index = index
    
    def backgroundVideoListHandler(self, value):
        input = self.backgroundVideoLink_input_comboBox.get()
        options = self.backgroundVideoLink_input_comboBox._values
        options[self.backgroundVideoLink_input_comboBox._index] = input
        empty = False
        for i in options:
            if i == "":
                empty = True
        if not empty:
            options.append("")
        self.backgroundVideoLink_input_comboBox.configure(values=options)

    def nameHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter subtitle name: ", title="Subtitle.name")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.name_input_button.configure(text=f"Name: {dialogInput}")
        
    def fontnameHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter font name: ", title="Subtitle.fontname")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.fontname_input_button.configure(text=f"Font Name: {dialogInput}")
        
    def fontsizeHandler(self):
        numeric = False
        prompt = "Enter Font Size: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.fontsize")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.fontsize_input_button.configure(text=f"Font Size: {dialogInput}")
    
    def primaryColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Primary Color: ", title="Subtitle.primaryColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.primaryColor_input_button.configure(text=f"Primary Color: {dialogInput}")
        
    def secondaryColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Secondary Color: ", title="Subtitle.secondaryColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.secondaryColor_input_button.configure(text=f"Secondary Color: {dialogInput}")
        
    def outlineColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Outline Color: ", title="Subtitle.outlineColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.outlineColor_input_button.configure(text=f"Outline Color: {dialogInput}")
        
    def backColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Back Color: ", title="Subtitle.backColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.backColor_input_button.configure(text=f"Back Color: {dialogInput}")
        
    def scaleXHandler(self):
        numeric = False
        prompt = "Enter Scale X: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.scaleX")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.scaleX_input_button.configure(text=f"Scale X: {dialogInput}")
        
    def scaleYHandler(self):
        numeric = False
        prompt = "Enter Scale Y: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.scaleY")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.scaleY_input_button.configure(text=f"Scale Y: {dialogInput}")
        
    def spacingHandler(self):
        numeric = False
        prompt = "Enter Spacing: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.spacing")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.spacing_input_button.configure(text=f"Spacing: {dialogInput}")
        
    def angleHandler(self):
        numeric = False
        prompt = "Enter Angle: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.angle")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.angle_input_button.configure(text=f"Angle: {dialogInput}")
        
    def borderStyleHandler(self):
        numeric = False
        prompt = "Enter border Style: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.borderStyle")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.borderStyle_input_button.configure(text=f"Border Style: {dialogInput}")
        
    def outlineHandler(self):
        numeric = False
        prompt = "Enter Outline: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.outline")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.outline_input_button.configure(text=f"Outline: {dialogInput}")
        
    def shadowHandler(self):
        numeric = False
        prompt = "Enter Shadow: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.shadow")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.shadow_input_button.configure(text=f"Shadow: {dialogInput}")
        
    def alignmentHandler(self):
        numeric = False
        prompt = "Enter Alignment: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.alignment")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.alignment_input_button.configure(text=f"Alignment: {dialogInput}")
        
    def marginLHandler(self):
        numeric = False
        prompt = "Enter Margin Left: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginL")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.marginL_input_button.configure(text=f"Margin Left: {dialogInput}")
        
    def marginRHandler(self):
        numeric = False
        prompt = "Enter Margin Right: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginR")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.marginR_input_button.configure(text=f"Margin Right: {dialogInput}")
        
    def marginVHandler(self):
        numeric = False
        prompt = "Enter Margin Vertical: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginV")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.marginV_input_button.configure(text=f"Margin Vertical: {dialogInput}")
        
    def encodingHandler(self):
        numeric = False
        prompt = "Enter Encoding: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.encoding")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.encoding_input_button.configure(text=f"Encoding: {dialogInput}")
        
    def boldHandler(self):
        print(f"Bold: {self.bold_checkbox.get()}")
        
    def italicHandler(self):
        print(f"Italic: {self.italic_checkbox.get()}")
        
    def underLineHandler(self):
        print(f"UnderLine: {self.underLine_checkbox.get()}")
        
    def strikeOutHandler(self):
        print(f"StrikeOut: {self.strikeOut_checkbox.get()}")
        
    class dictEntry:
        def __init__(self, dictKey, dictDef, row):
            self.dictKey = dictKey
            self.dictDef = dictDef
            self.row = row
            self.entry = customtkinter.CTkFrame(app.scrollable_frame_dictionary_tab, height=30)
            self.entry.grid(row=row, column=0, padx=0, pady=10)
            app.dictEntrys = app.dictEntrys
            self.label = customtkinter.CTkLabel(self.entry, text=f"{dictKey} : {dictDef}", wraplength=200)
            self.label.place(x=0)
            self.button = customtkinter.CTkButton(self.entry, width=15, text="delete", command=self.deleteEntry)
            self.button.place(x=150)
        
        def deleteEntry(self):
            self.entry.destroy()
        
    def addDictionaryEntry(self):
        self.dictEntrys += 1
        dictKey = self.dictionaryKey_entry.get()
        self.dictionaryKey_entry.delete(0, len(dictKey))
        dictDef = self.dictionaryDef_entry.get()
        self.dictionaryDef_entry.delete(0, len(dictDef))
        entry = self.dictEntry(dictKey, dictDef, self.dictEntrys)
        
            
            
    
        
if __name__ == "__main__":
    app = App()
    app.mainloop()