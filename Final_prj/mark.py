import sounddevice
import numpy as np
from scipy.io import wavfile
import os
import time

def record_audio(duration, fs=32000):
    audio_data = sounddevice.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
    sounddevice.wait()
    return audio_data.flatten(), fs  # Flatten dữ liệu âm thanh

def has_audible_sound(audio_data, threshold_factor=0.1):
    amplitude = np.max(np.abs(audio_data))
    # threshold = amplitude * threshold_factor
    return amplitude >= 1000

def mark():
    co = True
    while(co):
        print("Cảm biến...")
        audio_data, fs = record_audio(0.5)  # Ghi âm từ microphone trong 0.5 giây đầu tiên

        # Tạo thư mục để lưu các tệp tin âm thanh
        output_folder = "D:\Quang\Dien Tu\opto\Final_prj\Audio2"
        os.makedirs(output_folder, exist_ok=True)

        if has_audible_sound(audio_data):
            print("Nhận diện được âm thanh.")
            print("Nói gì đó...")

            # Ghi âm thêm 2 giây nếu có âm thanh nghe được
            audio_data, _ = record_audio(3)
            filename = f"{output_folder}\\sample.wav"
            wavfile.write(filename, fs, audio_data.astype('int16'))  # Chuyển đổi sang kiểu int16
            print(f"Dữ liệu âm thanh với âm thanh nghe được đã được lưu vào {filename}.")
            co = False
        else:
            print("Không có âm thanh.")
