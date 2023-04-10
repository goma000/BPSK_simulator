# SNRが0dBと10dBのときのベースバンド時間波形を図示する

import numpy as np
import matplotlib.pyplot as plt

num_symbols = 30  # 生成するシンボル数
amp = 1  # インパルス信号の振幅
snr_db = [0, 10] # SNRの値 (dB)
markers = ['s r', 'P r'] #プロット時に見やすくするため

# ランダムなデータを生成
data = np.random.randint(0, 2, num_symbols)

# BPSK変調
modulated_data = 2 * data - 1  

# ベースバンド時間波形の生成
time_waveform = np.zeros(num_symbols)
time_waveform[:] = amp * modulated_data[:]

# 元の信号のプロット
plt.stem(time_waveform, label='original')

# SNRが異なる場合の雑音を付加
for i, snr in enumerate(snr_db):
    # 雑音の分散を計算
    noise_var = (amp ** 2) / (10 ** (snr / 10))
    print('分散',snr,'dB : ',noise_var)
    
    # 正規分布に従う雑音を生成
    noise = np.random.normal(0, np.sqrt(noise_var), num_symbols)

    # 雑音を信号に足し合わせる
    noisy_signal = time_waveform + noise

    # 雑音を加えた信号のプロット
    plt.stem(noisy_signal, label='SNR = '+str(snr)+' dB',linefmt='None',markerfmt=markers[i])

plt.legend()
plt.show()