import os
import speech_recognition as sr
from gtts import gTTS
import tempfile
from pygame import mixer

def text_to_speech(text):
    tts = gTTS(text, lang='vi')
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        tts.save(f"D:/quang điện tử/output.mp3")
        mixer.init()
        mixer.music.load(f"D:/quang điện tử/output.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass

def again_text_to_speech():
    mixer.init()
    mixer.music.load(f"D:/quang điện tử/output.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        pass

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

def process_input():
    while True:
        choice = input("Chọn tác vụ (0: Nghe lại, 1: Tiếp tục, 2: Kết thúc): ").strip().lower()
        if choice == "0":
            again_text_to_speech()
        elif choice == "1":
            spoken_text = speech_to_text()
            print("Văn bản từ giọng nói: ", spoken_text)
            if "có" in spoken_text.lower():
                return 1
            elif "ko" in spoken_text.lower():
                return 0
        elif choice == "2":
            return -1
        else:
            print("Chọn tác vụ không hợp lệ. Vui lòng chọn lại.")

def main(input_text):
    text_to_speech(input_text)
    while True:
        result = process_input()
        if result == -1:
            break
    print("Kết thúc chương trình.")

if __name__ == "__main__":
    input_text = input("Nhập văn bản bạn muốn chuyển đổi thành giọng nói: ")
    main(input_text)
