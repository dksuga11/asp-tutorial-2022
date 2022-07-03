import numpy as np


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


fs = 16000
sec = 3
fin = 440
t = np.arange(sec * fs) / fs

x = np.sin(2.0 * np.pi * fin * t)

w = hamming(x.shape[0])

W = np.fft.fft(w)

print(W)
