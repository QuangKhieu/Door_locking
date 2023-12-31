from scipy.io import wavfile
import librosa
import numpy as np
import scipy.spatial.distance as dist
import sounddevice as sd
import scipy.io.wavfile as wav
import unidecode
from Com import com_serial
import speech_recognition as sr
from gtts import gTTS
#import librosa.feature as mel
import time
import mark

def dp(dist_mat):
    """
    Find minimum-cost path through matrix `dist_mat` using dynamic programming.

    """

    N, M = dist_mat.shape

    # Initialize the cost matrix
    cost_mat = np.zeros((N + 1, M + 1))
    for i in range(1, N + 1):
        cost_mat[i, 0] = np.inf
    for i in range(1, M + 1):
        cost_mat[0, i] = np.inf

    # Fill the cost matrix while keeping traceback information
    traceback_mat = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            penalty = [
                cost_mat[i, j],  # match (0)
                cost_mat[i, j + 1],  # insertion (1)
                cost_mat[i + 1, j]]  # deletion (2)
            i_penalty = np.argmin(penalty)
            cost_mat[i + 1, j + 1] = dist_mat[i, j] + penalty[i_penalty]
            traceback_mat[i, j] = i_penalty

    # Traceback from bottom right
    i = N - 1
    j = M - 1
    path = [(i, j)]
    while i > 0 or j > 0:
        tb_type = traceback_mat[i, j]
        if tb_type == 0:
            # Match
            i = i - 1
            j = j - 1
        elif tb_type == 1:
            # Insertion
            i = i - 1
        elif tb_type == 2:
            # Deletion
            j = j - 1
        path.append((i, j))

    # Strip infinity edges from cost_mat before returning
    cost_mat = cost_mat[1:, 1:]
    return (path[::-1], cost_mat)

def DTW_vec_cal(x,y,f_s): #y sound_data, fs tan so lay mau
    # Mel-scale spectrogram
    n_fft = int(1 * f_s)  # 25 ms
    hop_length = int(0.25 * f_s)  # 10 ms
    mel_spec_y = librosa.feature.melspectrogram(
        y = y / 1.0, sr=f_s, S=None,
        n_fft=n_fft, hop_length=hop_length, power=2, n_mels=60
    )
    log_mel_spec_y = np.log(mel_spec_y)
    y_seq = log_mel_spec_y.T

    mel_spec_x = librosa.feature.melspectrogram(
        y = x / 1.0, sr=f_s, S=None,
        n_fft=n_fft, hop_length=hop_length, power=2, n_mels=60
    )
    log_mel_spec_x = np.log(mel_spec_x)
    x_seq = log_mel_spec_x.T
    M = y_seq.shape[0]
    N = x_seq.shape[0]

    dist_mat = dist.cdist(x_seq, y_seq, "cosine")
    path, cost_mat = dp(dist_mat)
    return cost_mat[-1,-1], cost_mat[-1, -1]/(M+N)
# def record_audio(duration=2, sample_rate=32000, filename="output.wav"):
#     print("Ghi âm...")
#
#     # Ghi âm
#     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
#     sd.wait()
#
#     print("Recording complete.")
#
#     # Lưu vào tệp âm thanh
#     wav.write('D:\Quang\Dien Tu\opto\Final_prj\Audio2\sample.wav', sample_rate, audio_data)
#
#     print(f"Audio saved as {filename}")

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union if union != 0 else 0  # Tránh chia cho 0
    return similarity
def check(text):
    set1 = set(list(unidecode.unidecode(text.lower())))
    set2 = set(list("mo cua"))
    check = jaccard_similarity(set1, set2)
    return check

com_serial.reset()

while(True):
    mark.mark()
    # record_audio(duration=2)
    x_fn = "Audio2/Ref_sample.wav"
    f_s, x = wavfile.read(x_fn)
    y_fn = "Audio2/sample.wav"
    f_s, y = wavfile.read(y_fn)
    # print(f_s)
    a, b = DTW_vec_cal(x, y, f_s)
    print(a, b)
    time.sleep(1)
    if a < 0.02 or b < 0.0025:
        com_serial.pta_serial('COM3', 9600)
        break




#
# r = sr.Recognizer()
# time.sleep(2)
# with sr.AudioFile("Audio2/sample.wav") as source:
#     audio = r.record(source)
#     try:
#         s = r.recognize_google(audio, language="vi-VN")
#         print("Text: "+s)
#     except Exception as e:
#         print("Exception: "+str(e))
#
# check = check(s)
# print(check)
#if (a , b, check blala)
## com_serial.pta_serial("COM3", 9600)
      #  print("yes")


