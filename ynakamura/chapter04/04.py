import numpy as np
import matplotlib.pyplot as plt


def zero_pad(x, L, S):
    x_pad = np.pad(x, L - S)
    if x_pad.shape[0] % S != 0:
        x_pad = np.pad(x_pad, ((0, S - (x_pad.shape[0] % S))))
    return x_pad


def frame_div(x, L, S):
    x_pad = zero_pad(x, L, S)
    T = (x_pad.shape[0] - L) // S
    x_div = []
    for nT in range(T):
        x_t = []
        for nL in range(L):
            x_t.append(x_pad[nT * S + nL])
        x_div.append(x_t)
    return np.array(x_div)


def stft(x, L, S, win):
    x_div = frame_div(x, L, S)
    T = x_div.shape[0]
    X = []
    for t in range(T):
        tmp = x_div[t, :]
        tmp = tmp * win
        tmp = np.fft.rfft(tmp)
        X.append(tmp)
    return np.array(X).T


fs = 16000  # サンプリング周波数
sec = 0.1  # 秒数
fin = 440  # 入力信号の周波数
a = 1.0  # 振幅
t = np.linspace(0.0, sec, int(fs * sec))
x = a * np.cos(np.pi * fin * t)

L = 1000
S = 500
win = np.hamming(L)
X = stft(x, L, S, win)


plt.pcolormesh(np.abs(X))
plt.show()

plt.pcolormesh(np.angle(X))
plt.show()
