import numpy as np
import soundfile as sf


# Function to calculate SNR
def calc_snr(s, x):
    return 10 * np.log10(np.sum(s**2) / np.sum(x**2))


# Function to adjust the amplitude of white noise to match the SNR
def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
x = np.random.rand(round(sec * sr))  # ホワイトノイズの生成

y, sr = sf.read("outputs/02.wav")
s = x + y

adj_x = adjust_snr(s, x, 6)
print(calc_snr(s, adj_x))

print("success!")
