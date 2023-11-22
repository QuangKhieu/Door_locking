import speech_recognition as sr
from gtts import gTTS
import tempfile
from pygame import mixer

# Hàm chuyển đổi văn bản thành giọng nói (TTS) và phát ra âm thanh
def text_to_speech(text):
    tts = gTTS(text, lang='vi')
    tts.save(f"D:/Quang/Dien tu/opto/output1.mp3")
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        mixer.init()
        mixer.music.load(f"D:/Quang/Dien tu/opto/output1.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass

# Hàm chuyển đổi giọng nói thành văn bản (STT)
def speech_to_text(max_listen_time=5):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Hãy nói gì đó...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=max_listen_time)

    try:
        text = recognizer.recognize_google(audio, language="vi-VN")
        return text
    except sr.UnknownValueError:
        return "Không nhận dạng được giọng nói."
    except sr.RequestError as e:
        return f"Lỗi trong quá trình gửi yêu cầu: {str(e)}"
