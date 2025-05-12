import tkinter
import tkinter.messagebox
import customtkinter
import json, os, threading
from Main import shortsUtils
from Main import autoShorts
from utils import tkTopLevelWinodwLoadingAnimation

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
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Auto Shorts", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.run_button = customtkinter.CTkButton(self.sidebar_frame, text="Generate Sh*t posts", command=self.runMainProgram)
        self.run_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_script_select = customtkinter.CTkOptionMenu(self.sidebar_frame, command=self.changeScript, values=[])
        self.sidebar_script_select.grid(row=2, column=0, padx=20, pady=10)
        self.newScript_button = customtkinter.CTkButton(self.sidebar_frame, text="New Script File", command=self.newScriptFile)
        self.newScript_button.grid(row=3, column=0, padx=20, pady=10)
        self.removeScript_button = customtkinter.CTkButton(self.sidebar_frame, text="Delete Selected Script", command=self.deleteScriptFile)
        self.removeScript_button.grid(row=4, column=0, padx=20, pady=10)
        #place hold
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=350, state="normal")
        self.textbox.grid(row=0, rowspan=3, column=1, padx=(20, 0), pady=(32, 15), sticky="nsew")
        self.textbox.bind("<KeyRelease>", self.updateScripts)
        self.updateScriptSelect()
        self.sidebar_script_select.set(self.sidebar_script_select._values[0])
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        f = open("%s/%s" %(settings["scriptsFolderName"], self.sidebar_script_select.get()), "r")
        text = f.read()
        f.close()
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert(tkinter.END, text)
        self.updateScripts("")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=400)
        self.tabview.grid(row=0, column=2, padx=(20, 20), pady=15, rowspan=6, sticky="nsew")
        self.tabview.add("Settings")
        self.tabview.add("Subtitle Settings")
        self.tabview.add("Dictionary")
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Subtitle Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Subtitle Settings").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Dictionary").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("Dictionary").grid_rowconfigure(0, weight=1)
        #settings tab
        self.scrollable_frame_settings_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Settings"))
        self.scrollable_frame_settings_tab.grid(padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_settings_tab.grid_columnconfigure(0, weight=1)
        self.ttsModel_dropdown = customtkinter.CTkOptionMenu(self.scrollable_frame_settings_tab, values=["TTS Model:"] + modelList, command=self.ttsModelHandler, width=400)
        self.ttsModel_dropdown.grid(row=1, column=0, padx=0, pady=10)
        self.whisperModel_input_dropdown = customtkinter.CTkOptionMenu(self.scrollable_frame_settings_tab, values=["Whisper Model:", "tiny", "base", "small", "medium", "large"], command=self.whisperModelHandler, width=400)
        self.whisperModel_input_dropdown.grid(row=2, column=0, padx=0, pady=10)
        self.scriptsFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Scripts Folder Name: N/A", command=self.scriptsFolderHandler, width=400)
        self.scriptsFolderName_input_button.grid(row=3, column=0, padx=0, pady=10)
        self.speed_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="TTS Speed: N/A", command=self.ttsSpeedHandler, width=400)
        self.speed_input_button.grid(row=4, column=0, padx=0, pady=10)
        self.outputAudioFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Audio File Name: N/A", command=self.outputAudioHandler, width=400)
        self.outputAudioFileName_input_button.grid(row=5, column=0, padx=0, pady=10)
        self.subtitleOutputFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Subtitle File Name: N/A", command=self.outputSubtitleHandler, width=400)
        self.subtitleOutputFileName_input_button.grid(row=6, column=0, padx=0, pady=10)
        self.outputVideoFileName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Video File Name: N/A", command=self.outputVideoHandler, width=400)
        self.outputVideoFileName_input_button.grid(row=7, column=0, padx=0, pady=10)
        self.outputVideoFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Output Video Folder Name: N/A", command=self.outputVideoFolderHandler, width=400)
        self.outputVideoFolderName_input_button.grid(row=8, column=0, padx=0, pady=10)
        self.backgroundVideoFolderName_input_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Background Video Folder Name: N/A", command=self.backgroundVideoFolderHandler, width=400)
        self.backgroundVideoFolderName_input_button.grid(row=9, column=0, padx=0, pady=10)
        self.backgroundVideoLink_input_comboBox = customtkinter.CTkComboBox(self.scrollable_frame_settings_tab, values=["Background Video Links:", ""], command=self.backgroundVideoListActiveIndexSetter, width=400)
        self.backgroundVideoLink_input_comboBox.grid(row=10, column=0, padx=0, pady=10)
        self.backgroundVideoLink_input_comboBox.bind("<KeyRelease>", self.backgroundVideoListHandler)
        self.downloadBackgroundVidoes_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Download Background Vidoes", command=self.downloadBackgroundVidoes)
        self.downloadBackgroundVidoes_button.grid(row=11, column=0, padx=20, pady=10)
        self.resetSettings_button = customtkinter.CTkButton(self.scrollable_frame_settings_tab, text="Reset Settings", command=self.resetSettings)
        self.resetSettings_button.grid(row=12, column=0, padx=0, pady=10)
        #Subtitle Settings tab
        self.scrollable_frame_subtitle_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Subtitle Settings"))
        self.scrollable_frame_subtitle_tab.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_subtitle_tab.grid_columnconfigure(0, weight=1)
        self.name_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Name: N/A", command=self.nameHandler, width=400) 
        self.name_input_button.grid(row=0, column=0, padx=0, pady=10)
        self.fontname_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Font Name: N/A", command=self.fontnameHandler, width=400)
        self.fontname_input_button.grid(row=1, column=0, padx=0, pady=10)
        self.fontsize_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Font Size: N/A", command=self.fontsizeHandler, width=400)
        self.fontsize_input_button.grid(row=2, column=0, padx=0, pady=10)
        self.primaryColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Primary Color: N/A", command=self.primaryColorHandler, width=400)
        self.primaryColor_input_button.grid(row=3, column=0, padx=0, pady=10)
        self.secondaryColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Secondary Color: N/A", command=self.secondaryColorHandler, width=400)
        self.secondaryColor_input_button.grid(row=4, column=0, padx=0, pady=10)
        self.outlineColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Outline Color: N/A", command=self.outlineColorHandler, width=400)
        self.outlineColor_input_button.grid(row=5, column=0, padx=0, pady=10)
        self.backColor_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Back Color: N/A", command=self.backColorHandler, width=400)
        self.backColor_input_button.grid(row=6, column=0, padx=0, pady=10)
        self.scaleX_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Scale X: N/A", command=self.scaleXHandler, width=400)
        self.scaleX_input_button.grid(row=7, column=0, padx=0, pady=10)
        self.scaleY_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Scale Y: N/A", command=self.scaleYHandler, width=400)
        self.scaleY_input_button.grid(row=8, column=0, padx=0, pady=10)
        self.spacing_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Spacing: N/A", command=self.spacingHandler, width=400)
        self.spacing_input_button.grid(row=9, column=0, padx=0, pady=10)
        self.angle_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Angle: N/A", command=self.angleHandler, width=400)
        self.angle_input_button.grid(row=10, column=0, padx=0, pady=10)
        self.borderStyle_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Border Style: N/A", command=self.borderStyleHandler, width=400)
        self.borderStyle_input_button.grid(row=11, column=0, padx=0, pady=10)
        self.outline_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Outline: N/A", command=self.outlineHandler, width=400)
        self.outline_input_button.grid(row=12, column=0, padx=0, pady=10)
        self.shadow_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Shadow: N/A", command=self.shadowHandler, width=400)
        self.shadow_input_button.grid(row=13, column=0, padx=0, pady=10)
        self.alignment_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Alignment: N/A", command=self.alignmentHandler, width=400)
        self.alignment_input_button.grid(row=14, column=0, padx=0, pady=10)
        self.marginL_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Left: N/A", command=self.marginLHandler, width=400)
        self.marginL_input_button.grid(row=15, column=0, padx=0, pady=10)
        self.marginR_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Right: N/A", command=self.marginRHandler, width=400)
        self.marginR_input_button.grid(row=16, column=0, padx=0, pady=10)
        self.marginV_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Margin Vertical: N/A", command=self.marginVHandler, width=400)
        self.marginV_input_button.grid(row=17, column=0, padx=0, pady=10)
        self.encoding_input_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Encoding: N/A", command=self.encodingHandler, width=400)
        self.encoding_input_button.grid(row=18, column=0, padx=0, pady=10)
        self.bold_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="Bold", command=self.boldHandler, width=400)
        self.bold_checkbox.grid(row=19, column=0, padx=0, pady=10)
        self.italic_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="Italic", command=self.italicHandler, width=400)
        self.italic_checkbox.grid(row=20, column=0, padx=0, pady=10)
        self.underLine_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="UnderLine", command=self.underLineHandler, width=400)
        self.underLine_checkbox.grid(row=21, column=0, padx=0, pady=10)
        self.strikeOut_checkbox = customtkinter.CTkCheckBox(self.scrollable_frame_subtitle_tab, text="StrikeOut", command=self.strikeOutHandler, width=400)
        self.strikeOut_checkbox.grid(row=22, column=0, padx=0, pady=10)
        self.resetSubtitleSettings_button = customtkinter.CTkButton(self.scrollable_frame_subtitle_tab, text="Reset Subtitle Settings", command=self.resetSubtitleSettings)
        self.resetSubtitleSettings_button.grid(row=23, column=0, padx=0, pady=10)
        #Dictionary tab
        self.dictEntrys = []
        self.scrollable_frame_dictionary_tab = customtkinter.CTkScrollableFrame(self.tabview.tab("Dictionary"))
        self.scrollable_frame_dictionary_tab.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.scrollable_frame_dictionary_tab.grid_columnconfigure(0, weight=1)
        self.dictionary_entry_placehold = customtkinter.CTkBaseClass(self.scrollable_frame_dictionary_tab, height=10)
        self.dictionary_entry_placehold.grid(row=0, column=0, padx=0, pady=10)
        self.dictionaryKey_entry = customtkinter.CTkEntry(self.scrollable_frame_dictionary_tab, placeholder_text="Key", width=140)
        self.dictionaryKey_entry.place_configure(x=0)
        self.dictionary_colon_label = customtkinter.CTkLabel(self.scrollable_frame_dictionary_tab, text=":")
        self.dictionary_colon_label.place(x=145)
        self.dictionaryDef_entry = customtkinter.CTkEntry(self.scrollable_frame_dictionary_tab, placeholder_text="Def", width=140)
        self.dictionaryDef_entry.place_configure(x=232)
        self.dictionary_add_button = customtkinter.CTkButton(self.scrollable_frame_dictionary_tab, width=50, text="add", command=self.addDictionaryEntry)
        self.dictionary_add_button.place(x=305)
        
        # set values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.updateSettings()
        
    class dictEntry:
        def __init__(self, dictKey, dictDef, row, app):
            self.dictKey = dictKey
            self.dictDef = dictDef
            self.row = row
            self.entry = customtkinter.CTkFrame(app.scrollable_frame_dictionary_tab, height=30, width=500)
            self.entry.grid(row=row, column=0, padx=0, pady=10)
            self.label = customtkinter.CTkLabel(self.entry, text=f"{dictKey} : {dictDef}", wraplength=500)
            self.label.place(x=10)
            self.button = customtkinter.CTkButton(self.entry, width=15, text="delete", command=self.deleteEntry)
            self.button.place(x=305)
        def deleteEntry(self):
            self.entry.destroy()
            app.dictEntrys.remove(self)
            f = open("dictionary.json")
            dictionary = json.load(f)
            f.close()
            del dictionary[self.dictKey]
            dumped = json.dumps(dictionary, indent="  ")
            f = open("dictionary.json", "w")
            f.write(dumped)
            f.close()
        
    #Sidebar Functions   
        
    def runMainProgram(value):
        main = autoShorts()
        window = tkTopLevelWinodwLoadingAnimation(main.run, "loading", "Sh*t post(s) created", "roboto", 50)
        window.loadingWindow()
        
    def newScriptFile(self):
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        scriptsFolderName = settings["scriptsFolderName"]
        scriptCount = len(self.sidebar_script_select._values) + 1
        with open(f"{scriptsFolderName}/Script({scriptCount}).txt", "w") as file:
            file.write(f"New Script {scriptCount}")
        self.updateScriptSelect()
        self.sidebar_script_select.set(f"Script({scriptCount}).txt")
        self.changeScript(None)
        
    def deleteScriptFile(self):
        if not (len(self.sidebar_script_select._values) <= 1):
            f = open("settings.json")
            settings = json.load(f)
            f.close()
            scriptsFolderName = settings["scriptsFolderName"]
            os.remove(f"{scriptsFolderName}/{self.sidebar_script_select.get()}")    
            self.updateScriptSelect()
            self.sidebar_script_select.set(self.sidebar_script_select._values[0])
            self.changeScript(None)
    #Updates
    
    def updateSettings(self):
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        #settings
        self.ttsModel_dropdown.set(settings["ttsModel"])
        self.whisperModel_input_dropdown.set(settings["whisperModel"])
        self.scriptsFolderName_input_button.configure(text="Scripts Folder Name: %(scriptsFolderName)s" % settings)
        self.speed_input_button.configure(text="TTS Speed: %(speed)s" % settings)
        self.outputAudioFileName_input_button.configure(text="Output Audio File Name: %(outputAudioName)s" % settings)
        self.subtitleOutputFileName_input_button.configure(text="Output Subtitle File Name: %(subtitleOutputFileName)s" % settings)
        self.outputVideoFileName_input_button.configure(text="Output Video File Name: %(outputVideoName)s" % settings)
        self.outputVideoFolderName_input_button.configure(text="Output Video Folder Name: %(outputVideoFolderName)s" % settings)
        self.backgroundVideoFolderName_input_button.configure(text="Background Video Folder Name: %(backgroundVideoFolderName)s" % settings)
        self.backgroundVideoLink_input_comboBox.configure(values=["Background Video Links:"] + settings["backgroundVideoList"] + [""])
        #subtitles
        self.name_input_button.configure(text="Name: %(Name)s" % settings)
        self.fontname_input_button.configure(text="Font Name: %(Fontname)s" % settings)
        self.fontsize_input_button.configure(text="Font Size: %(Fontsize)s" % settings)
        self.primaryColor_input_button.configure(text="Primary Color: %(PrimaryColour)s" % settings)
        self.secondaryColor_input_button.configure(text="Secondary Color: %(SecondaryColour)s" % settings)
        self.outlineColor_input_button.configure(text="Outline Color: %(OutlineColour)s" % settings)
        self.backColor_input_button.configure(text="Back Color: %(BackColour)s" % settings)
        self.scaleX_input_button.configure(text="Scale X: %(ScaleX)s" % settings)
        self.scaleY_input_button.configure(text="Scale Y: %(ScaleY)s" % settings)
        self.spacing_input_button.configure(text="Spacing: %(Spacing)s" % settings)
        self.angle_input_button.configure(text="Angle: %(Angle)s" % settings)
        self.borderStyle_input_button.configure(text="Border Style: %(BorderStyle)s" % settings)
        self.outline_input_button.configure(text="Outline: %(Outline)s" % settings)
        self.shadow_input_button.configure(text="Shadow: %(Shadow)s" % settings)
        self.alignment_input_button.configure(text="Alignment: %(Alignment)s" % settings)
        self.marginL_input_button.configure(text="Margin Left: %(MarginL)s" % settings)
        self.marginR_input_button.configure(text="Margin Right: %(MarginR)s" % settings)
        self.marginV_input_button.configure(text="Margin Vertical: %(MarginV)s" % settings)
        self.encoding_input_button.configure(text="Encoding: %(Encoding)s" % settings)
        if bool(settings["Bold"]):
            self.bold_checkbox.select()
        else:
            self.bold_checkbox.deselect()
        if bool(settings["Italic"]):
            self.italic_checkbox.select()
        else:
            self.italic_checkbox.deselect()
        if bool(settings["UnderLine"]):
            self.underLine_checkbox.select()
        else:
            self.underLine_checkbox.deselect()
        if bool(settings["StrikeOut"]):
            self.strikeOut_checkbox.select()
        else:
            self.strikeOut_checkbox.deselect()
        #dictionary
        f = open("dictionary.json")
        dictionary = json.load(f)
        f.close()
        for key in dictionary:
            entry = self.dictEntry(key, dictionary[key], len(self.dictEntrys)+1, self)
            self.dictEntrys.append(entry)
        
    def updateScriptSelect(self):
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        unfilteredScripts = os.listdir(settings["scriptsFolderName"])
        scripts = []
        for dir in unfilteredScripts:
            if not(dir.find(".txt") == -1):
                scripts.append(dir)
        self.sidebar_script_select.configure(values=scripts)
        
    def updateScripts(self, value):
        self.applyDictionary()
        self.updateScriptSelect()
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        f = open("%s/%s" %(settings["scriptsFolderName"], self.sidebar_script_select.get()), "w")
        f.write(self.textbox.get("1.0", tkinter.END))
        f.close()
        f = open("%s/%s" %(settings["scriptsFolderName"], self.sidebar_script_select.get()), "r")
        text = f.read()
        f.close()
        text = text[:-1]
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert(tkinter.END, text)

    def applyDictionary(self):
        f = open("dictionary.json")
        dictionary = json.load(f)
        f.close()
        checkList = ["?", ",", ".", " "]
        for entry in dictionary:
            for i in checkList:  
                try:
                    text = self.textbox.get("1.0", tkinter.END).replace(f" {entry}{i}", " " + dictionary[entry] + i)
                    text = text[:-1]
                    self.textbox.delete("1.0", tkinter.END)
                    self.textbox.insert(tkinter.END, text)
                except:
                    pass

    def changeScript(self, value):
        f = open("settings.json")
        settings = json.load(f)
        f.close()
        f = open("%s/%s" %(settings["scriptsFolderName"], self.sidebar_script_select.get()), "r")
        text = f.read()
        f.close()
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert(tkinter.END, text)
        self.updateScripts("")
        
    def updateDictionary(self):
        f = open("dictionary.json")
        dictionary = json.load(f)
        f.close()
        for entry in self.dictEntrys:
            dictionary[entry.dictKey] = entry.dictDef
        dumped = json.dumps(dictionary, indent="  ")
        f = open("dictionary.json", "w")
        f.write(dumped)
        f.close()
            
    #settings setters
    def writeToJSON(self, setting: str, value: str):
        f = open("settings.json", "r")
        settings = json.load(f)
        f.close()
        f = open("settings.json", "w")
        settings[setting] = value
        dumped = json.dumps(settings, indent="  ")
        f.write(dumped)
        f.close()
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def scriptsFolderHandler(self):
        pathExists = False
        prompt = "Enter Scripts Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.ScriptsFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.writeToJSON("scriptsFolderName", dialogInput)
        self.updateSettings()
    
    def ttsModelHandler(self, value):
        print(f"tts model: {value}")
        self.writeToJSON("ttsModel", value)
        
    def ttsSpeedHandler(self):
        numeric = False
        prompt = "Enter TTS Speed: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.ttsSpeed")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("speed", int(dialogInput))
        self.updateSettings()
        
    def whisperModelHandler(self, value):
        print(f"whisper model: {value}")
        self.writeToJSON("whisperModel", value)
        
    def outputAudioHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Audio File Name:", title="Settings.outputAudioFileName")
        dialogInput = dialog.get_input()
        dialogInput = dialogInput.split(".")[0]
        dialogInput = f"{dialogInput}.mp3"
        self.writeToJSON("outputAudioName", dialogInput)
        self.updateSettings()
        
    def outputSubtitleHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Subtitle File Name:", title="Settings.outputSubtitleFileName")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("subtitleOutputFileName", dialogInput)
        self.updateSettings()
        
    def outputVideoHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Video File Name:", title="Settings.outputVideoFileName")
        dialogInput = dialog.get_input()
        dialogInput = dialogInput.split(".")[0]
        dialogInput = f"{dialogInput}.mp4"
        self.writeToJSON("outputVideoName", dialogInput)
        self.updateSettings()
        
    def outputVideoFolderHandler(self):
        pathExists = False
        prompt = "Enter Video Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.outputVideoFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.writeToJSON("outputVideoFolderName", dialogInput)
        self.updateSettings()
        
    def backgroundVideoFolderHandler(self):
        pathExists = False
        prompt = "Enter Background Video Folder Name: "
        while not pathExists:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Settings.backgroundVideoFolderName")
            dialogInput = dialog.get_input()
            pathExists = os.path.exists(dialogInput)
            prompt = "Enter a vaild path or folder name in program directory: "
        self.writeToJSON("backgroundVideoFolderName", dialogInput)
        self.updateSettings()
        
    def backgroundVideoListActiveIndexSetter(self, value):
        options = self.backgroundVideoLink_input_comboBox._values
        index = options.index(value)
        self.backgroundVideoLink_input_comboBox._index = index
    
    def backgroundVideoListHandler(self, value):
        input = self.backgroundVideoLink_input_comboBox.get()
        options = self.backgroundVideoLink_input_comboBox._values
        options[self.backgroundVideoLink_input_comboBox._index] = input
        empty = False
        count = 0
        for i in options:
            if i == "":
                empty = True
                count = count + 1
        if not empty:
            options.append("")
        for i in range(0, count-1):
            options.remove("")
        self.backgroundVideoLink_input_comboBox.configure(values=options)
        videoList = []
        for i in options:
            if not (i == "" or i == "Background Video Links:" or options.index(i) == 0):
                videoList.append(i)
        self.writeToJSON("backgroundVideoList", videoList)
        
    def resetSettings(self):
        f = open("settings.json", "r")
        settings = json.load(f)
        f.close()
        settings["scriptsFolderName"] = "Scripts"
        settings["ttsModel"] = "tts_models/en/jenny/jenny"
        settings["language"] = "en"
        settings["emotion"] =  None
        settings["speed"] =  1
        settings["whisperModel"] = "small"
        settings["outputAudioName"] = "outputAudio.mp3"
        settings["subtitleOutputFileName"] = "titles"
        settings["outputVideoName"] = "videoOutput.mp4"
        settings["outputVideoFolderName"] = "outputVideos"
        settings["backgroundVideoFolderName"] = "backgroundVideos"
        settings["downloadVideosInLinksFile"] = True
        settings["loopAllModels"] = False
        settings["backgroundVideoList"] = ["https://www.youtube.com/watch?v=u7kdVe8q5zs"]
        f = open("settings.json", "w")
        dumped = json.dumps(settings, indent="  ")
        f.write(dumped)
        f.close()
        self.updateSettings()

    #subtitle setters
    
    def nameHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter subtitle name: ", title="Subtitle.name")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("Name", dialogInput)
        self.updateSettings()
        
    def fontnameHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter font name: ", title="Subtitle.fontname")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("Fontname", dialogInput)
        self.updateSettings()
        
    def fontsizeHandler(self):
        numeric = False
        prompt = "Enter Font Size: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.fontsize")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Fontsize", int(dialogInput))
        self.updateSettings()
    
    def primaryColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Primary Color: ", title="Subtitle.primaryColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("PrimaryColour", dialogInput)
        self.updateSettings()
        
    def secondaryColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Secondary Color: ", title="Subtitle.secondaryColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("SecondaryColour", dialogInput)
        self.updateSettings()
        
    def outlineColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Outline Color: ", title="Subtitle.outlineColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("OutlineColour", dialogInput)
        self.updateSettings()
        
    def backColorHandler(self):
        dialog = customtkinter.CTkInputDialog(text="Enter Back Color: ", title="Subtitle.backColor")
        dialogInput = dialog.get_input()
        if dialogInput == None:
            return
        self.writeToJSON("BackColour", dialogInput)
        self.updateSettings()
        
    def scaleXHandler(self):
        numeric = False
        prompt = "Enter Scale X: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.scaleX")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("ScaleX", int(dialogInput))
        self.updateSettings()
        
    def scaleYHandler(self):
        numeric = False
        prompt = "Enter Scale Y: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.scaleY")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("ScaleY", int(dialogInput))
        self.updateSettings()
        
    def spacingHandler(self):
        numeric = False
        prompt = "Enter Spacing: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.spacing")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Spacing", int(dialogInput))
        self.updateSettings()
        
    def angleHandler(self):
        numeric = False
        prompt = "Enter Angle: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.angle")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Angle", int(dialogInput))
        self.updateSettings()
        
    def borderStyleHandler(self):
        numeric = False
        prompt = "Enter border Style: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.borderStyle")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("BorderStyle", int(dialogInput))
        self.updateSettings()
        
    def outlineHandler(self):
        numeric = False
        prompt = "Enter Outline: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.outline")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Outline", int(dialogInput))
        self.updateSettings()
        
    def shadowHandler(self):
        numeric = False
        prompt = "Enter Shadow: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.shadow")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Shadow", int(dialogInput))
        self.updateSettings()
        
    def alignmentHandler(self):
        numeric = False
        prompt = "Enter Alignment: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.alignment")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Alignment", int(dialogInput))
        self.updateSettings()
        
    def marginLHandler(self):
        numeric = False
        prompt = "Enter Margin Left: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginL")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("MarginL", int(dialogInput))
        self.updateSettings()
        
    def marginRHandler(self):
        numeric = False
        prompt = "Enter Margin Right: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginR")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("MarginR", int(dialogInput))
        self.updateSettings()
        
    def marginVHandler(self):
        numeric = False
        prompt = "Enter Margin Vertical: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.marginV")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("MarginV", int(dialogInput))
        self.updateSettings()
        
    def encodingHandler(self):
        numeric = False
        prompt = "Enter Encoding: "
        while not numeric:
            dialog = customtkinter.CTkInputDialog(text=prompt, title="Subtitle.encoding")
            dialogInput = dialog.get_input()
            numeric = dialogInput.isnumeric()
            prompt = "Enter a number: "
        self.writeToJSON("Encoding", int(dialogInput))
        self.updateSettings()
        
    def boldHandler(self):
        print(f"Bold: {self.bold_checkbox.get()}")
        self.writeToJSON("Bold", bool(self.bold_checkbox.get()))
        
    def italicHandler(self):
        print(f"Italic: {self.italic_checkbox.get()}")
        self.writeToJSON("Italic", bool(self.italic_checkbox.get()))
        
    def underLineHandler(self):
        print(f"UnderLine: {self.underLine_checkbox.get()}")
        self.writeToJSON("UnderLine", bool(self.underLine_checkbox.get()))
        
    def strikeOutHandler(self):
        print(f"StrikeOut: {self.strikeOut_checkbox.get()}")
        self.writeToJSON("StrikeOut", bool(self.strikeOut_checkbox.get()))
        
    def resetSubtitleSettings(self):
        f = open("settings.json", "r")
        settings = json.load(f)
        f.close()
        settings["Name"] = "Default"
        settings["Fontname"] = "Arial"
        settings["Fontsize"] = 16
        settings["PrimaryColour"] = "&Hffffff"
        settings["SecondaryColour"] = "&Hffffff"
        settings["OutlineColour"] = "&H0"
        settings["BackColour"] = "&H0"
        settings["Bold"] = False
        settings["Italic"] = False
        settings["UnderLine"] = False
        settings["StrikeOut"] = False
        settings["ScaleX"] = 100
        settings["ScaleY"] = 100
        settings["Spacing"] = 0
        settings["Angle"] = 0
        settings["BorderStyle"] = 1
        settings["Outline"] = 1
        settings["Shadow"] = 0
        settings["Alignment"] = 2
        settings["MarginL"] = 10
        settings["MarginR"] = 10
        settings["MarginV"] = 150
        settings["Encoding"] = 1
        f = open("settings.json", "w")
        dumped = json.dumps(settings, indent="  ")
        f.write(dumped)
        f.close()
        self.updateSettings()
        
    #Dictionary setter
    
    def addDictionaryEntry(self):
        dictKey = self.dictionaryKey_entry.get()
        self.dictionaryKey_entry.delete(0, len(dictKey))
        dictDef = self.dictionaryDef_entry.get()
        self.dictionaryDef_entry.delete(0, len(dictDef))
        entry = self.dictEntry(dictKey, dictDef, len(self.dictEntrys) + 1, self)
        self.dictEntrys.append(entry)
        self.updateDictionary()
        
    def downloadBackgroundVidoes(self):
        self.loadingFunction = tkTopLevelWinodwLoadingAnimation(shortsUtils.downloadBackgroudVidoes, "Downloading Video(s)", "Video(s) Saved", "Roboto", 50)
        threading.Thread(target=self.loadingFunction.loadingWindow).start()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()