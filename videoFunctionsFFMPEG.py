def format_time(seconds):
        from math import floor
        hours = floor(seconds / 3600)
        seconds %= 3600
        minutes = floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - floor(seconds)) * 1000)
        seconds = floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
        return formatted_time
    
import ffmpeg
class videoFunctionsFFMPEG:
    def createSubtitles(workingDirectory: str, whisperModel: str, outputAudioName: str, subtitleOutputFileName: str, language: str) -> None:
        import os
        "whisperModel-\"tiny\", \"base\", \"small\", \"medium\", \"large\", \"large-v3\""
        from faster_whisper import WhisperModel
        model = WhisperModel(whisperModel)
        segments, info = model.transcribe(f"{workingDirectory}/{outputAudioName}")
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
        .input(f"{workingDirectory}/sub-titles.{language}.srt")
        .output(f"{workingDirectory}/sub-titles.{language}.ass")
        .run(overwrite_output = True)
        )
        os.remove(f"{workingDirectory}/sub-titles.{language}.srt")
        
    def formatAssFile(assFilePath: str, name: str, fontName: str, fontSize: int, primaryColour: str, secondaryColour: str, outlineColour: str, backColour: str, bold: bool, italic: bool, underLine: bool, strikeOut: bool, scaleX: int, scaleY: int, spacing: int, angle: int, borderStyle: int, outline: int, shadow: int, alignment:int, marginL: int, marginR: int, marginV: int, encoding: int) -> None:
        if bold:
            bold = 1
        else:
            bold = 0
        if italic:
            italic = 1
        else:
            italic = 0
        if underLine:
            underLine = 1
        else:
            underLine = 0
        if strikeOut:
            strikeOut = 1
        else:
            strikeOut = 0
        with open(assFilePath) as inp:
            subtitleFileContent = inp.read().splitlines()
            subtitleFileContent[10] = f"Style: {str(name)},{str(fontName)},{str(fontSize)},{str(primaryColour)},{str(secondaryColour)},{str(outlineColour)},{str(backColour)},{str(bold)},{str(italic)},{str(underLine)},{str(strikeOut)},{str(scaleX)},{str(scaleY)},{str(spacing)},{str(angle)},{str(borderStyle)},{str(outline)},{str(shadow)},{str(alignment)},{str(marginL)},{str(marginR)},{str(marginV)},{str(encoding)}"
            formatedStyle = "\n".join(subtitleFileContent)
            f = open(assFilePath, "w")
            f.write(formatedStyle)
            f.close()
        
    def changeVideoResolution(aspectRatio: str, inputVideoPath: str, outputVideoPath: str) -> None:
        "aspectRatio-x:y"
        aspectRatio = aspectRatio.replace(":", "/")
        (
        ffmpeg
        .input(inputVideoPath)
        .filter("crop", f"{aspectRatio}*ih", "ih")
        .output(outputVideoPath)
        .run(overwrite_output = True)
        )
        
    def applySubtitlesToVideo(assFileName: str, inputVideoPath: str, outputVideoPath: str) -> None:
        ".ass file must be in the same directory as the input video"
        (
        ffmpeg
        .input(inputVideoPath)
        .filter("ass", assFileName)
        .output(outputVideoPath)
        .run(overwrite_output = True)
        )
        
    def applyAudioToVideo(inputVideoPath: str, inputAudioPath: str, outputVideoPath: str) -> None:
        (
        ffmpeg
        .input(inputVideoPath)
        .concat(ffmpeg.input(f"{inputAudioPath}"), a=1)
        .output(outputVideoPath)
        .run(overwrite_output=True)
        )