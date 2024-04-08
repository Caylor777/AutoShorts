# Auto Shorts
Convert any script(s) to a TTS video with subtitles

## Installation
Works in python 3.11.5<br>
clone or download zip of the repository<br>
Install before using:<br>
"https://visualstudio.microsoft.com/visual-cpp-build-tools/" and download C++ tools<br>
"https://github.com/espeak-ng/espeak-ng/releases/tag/1.51" and download the .msi

## Usage
How to Use:<br>
    Use "settings.txt" to config the program (Note: Must keep space after "=")<br>
    Put ".txt" Files in the "Scripts" Folder and the program will make a new video per script in the folder<br>
    Youtube(only) links in the "backgroundVideoList.txt" file will downloaded if the "downloadVideosInLinksFile" setting is "True"<br>
    "downloadVideosInLinksFile = True" will prevent the main program from running and only download the videos<br>
    (Note: "downloadVideosInLinksFile" is for easily downloading background videos)<br>
How it works:<br>
    For evey script in "Scripts" folder a video is made<br>
    Videos in the "backgroundVideos" folder will be randomly chosen for each script<br>
    Run "Main.py" to use program<br>
All TTS Voices:<br>
    1: tts_models/multilingual/multi-dataset/xtts_v2<br>
    2: tts_models/multilingual/multi-dataset/xtts_v1.1<br>
    3: tts_models/multilingual/multi-dataset/your_tts<br>
    4: tts_models/multilingual/multi-dataset/bark<br>
    5: tts_models/bg/cv/vits<br>
    6: tts_models/cs/cv/vits<br>
    7: tts_models/da/cv/vits<br>
    8: tts_models/et/cv/vits<br>
    9: tts_models/ga/cv/vits<br>
    10: tts_models/en/ek1/tacotron2<br>
    11: tts_models/en/ljspeech/tacotron2-DDC<br>
    12: tts_models/en/ljspeech/tacotron2-DDC_ph<br>
    13: tts_models/en/ljspeech/glow-tts<br>
    14: tts_models/en/ljspeech/speedy-speech<br>
    15: tts_models/en/ljspeech/tacotron2-DCA<br>
    16: tts_models/en/ljspeech/vits<br>
    17: tts_models/en/ljspeech/vits--neon<br>
    18: tts_models/en/ljspeech/fast_pitch<br>
    19: tts_models/en/ljspeech/overflow<br>
    20: tts_models/en/ljspeech/neural_hmm<br>
    23: tts_models/en/sam/tacotron-DDC<br>
    24: tts_models/en/blizzard2013/capacitron-t2-c50<br>
    25: tts_models/en/blizzard2013/capacitron-t2-c150_v2<br>
    26: tts_models/en/multi-dataset/tortoise-v2<br>
    27: tts_models/en/jenny/jenny<br>
    28: tts_models/es/mai/tacotron2-DDC<br>
    29: tts_models/es/css10/vits<br>
    30: tts_models/fr/mai/tacotron2-DDC<br>
    31: tts_models/fr/css10/vits<br>
    32: tts_models/uk/mai/glow-tts<br>
    33: tts_models/uk/mai/vits<br>
    34: tts_models/zh-CN/baker/tacotron2-DDC-GST<br>
    35: tts_models/nl/mai/tacotron2-DDC<br>
    36: tts_models/nl/css10/vits<br>
    37: tts_models/de/thorsten/tacotron2-DCA<br>
    38: tts_models/de/thorsten/vits<br>
    39: tts_models/de/thorsten/tacotron2-DDC<br>
    40: tts_models/de/css10/vits-neon<br>
    41: tts_models/ja/kokoro/tacotron2-DDC<br>
    42: tts_models/tr/common-voice/glow-tts<br>
    43: tts_models/it/mai_female/glow-tts<br>
    44: tts_models/it/mai_female/vits<br>
    45: tts_models/it/mai_male/glow-tts<br>
    46: tts_models/it/mai_male/vits<br>
    47: tts_models/ewe/openbible/vits<br>
    48: tts_models/hau/openbible/vits<br>
    49: tts_models/lin/openbible/vits<br>
    50: tts_models/tw_akuapem/openbible/vits<br>
    51: tts_models/tw_asante/openbible/vits<br>
    52: tts_models/yor/openbible/vits<br>
    53: tts_models/hu/css10/vits<br>
    54: tts_models/el/cv/vits<br>
    55: tts_models/fi/css10/vits<br>
    56: tts_models/hr/cv/vits<br>
    57: tts_models/lt/cv/vits<br>
    58: tts_models/lv/cv/vits<br>
    59: tts_models/mt/cv/vits<br>
    60: tts_models/pl/mai_female/vits<br>
    61: tts_models/pt/cv/vits<br>
    62: tts_models/ro/cv/vits<br>
    63: tts_models/sk/cv/vits<br>
    64: tts_models/sl/cv/vits<br>
    65: tts_models/sv/cv/vits<br>
    66: tts_models/ca/custom/vits<br>
    67: tts_models/fa/custom/glow-tts<br>
    68: tts_models/bn/custom/vits-male<br>
    69: tts_models/bn/custom/vits-female<br>
    70: tts_models/be/common-voice/glow-tts<br>

## Dependencies
"https://visualstudio.microsoft.com/visual-cpp-build-tools/"<br>
"https://github.com/espeak-ng/espeak-ng/releases/tag/1.51"<br>
pip packages: "pytube", "TTS", "faster_whisper", "ffmpeg-python" or requirements.txt

## Contributing
https://github.com/Caylor777

## License
MIT License

## Contact
https://github.com/Caylor777/AutoShorts
