import speech_recognition as sr
from gtts import gTTS
import tempfile
from pygame import mixer

output_path = "D:/Quang/Dien tu/opto/output{}.mp3"
count = 1
# Hàm chuyển đổi văn bản thành giọng nói (TTS) và phát ra âm thanh
def text_to_speech(text):
    global count
    tts = gTTS(text, lang='vi')
    file = output_path.format(count)
    tts.save(file)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    count += 1

# Hàm chuyển đổi giọng nói thành văn bản (STT)
def speech_to_text(max_listen_time=5):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    temp = 0;
    while True:

        with microphone as source:
            print("Hãy nói gì đó...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=max_listen_time)

        try:
            text = recognizer.recognize_google(audio, language="vi-VN")
            return text
        except sr.UnknownValueError:
            if temp >= 5:
                return "Không nhận dạng được giọng nói."
        except sr.RequestError as e:
            return f"Lỗi trong quá trình gửi yêu cầu: {str(e)}"
