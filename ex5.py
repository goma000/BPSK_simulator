# 得られたBPSK信号のビット誤り率特性を用いて，BPSK信号の通信路容量を取得するとともに，シャノンの通信路容量（シャノン限界）と比較・考察する

import numpy as np
from scipy.special import erfc

num_symbols = 1000000  # 生成するシンボル数
amp = 1  # インパルス信号の振幅（平均信号電力）
snr_db = np.arange(0, 11)  # SNRの値 (0～10dB)
ber = np.zeros(len(snr_db))  # ビット誤り率特性
p_e = np.zeros(len(snr_db))  # 理論BER特性
noise_e = np.zeros(len(snr_db))   #平均雑音電力
c = np.zeros(len(snr_db)) #通信路容量
c_p = np.zeros(len(snr_db)) #通信路容量（理論BER）
c_limit = np.zeros(len(snr_db)) #シャノン限界

# ランダムなデータを生成
data = np.random.randint(0, 2, num_symbols)

# BPSK変調
modulated_data = 2 * data - 1  

# ベースバンド時間波形の生成
time_waveform = np.zeros(num_symbols)
time_waveform[:] = amp * modulated_data[:]

for i, snr in enumerate(snr_db):
    # 雑音の分散を計算
    noise_var = (amp ** 2) / (10 ** (snr / 10))
    noise_e[i] = noise_var * 2

    
    # 正規分布に従う雑音を生成
    noise = np.random.normal(0, np.sqrt(noise_var), num_symbols)
    
    # 雑音を加えた受信信号を生成
    received_signal = time_waveform + noise

    # 弁別レベルを0に設定して、データを判定
    received_data = np.zeros(num_symbols)
    received_data[received_signal > 0] = 1

    # ビット誤り率を計算
    ber[i] = np.sum(data != received_data) / num_symbols

    #理論BERを計算
    p_e[i] = 1/2 * erfc(np.sqrt(10**(snr_db[i]/10)/2))

    #通信路容量を計算
    c[i] = 1 - (- ber[i]*np.log2(ber[i]) - (1-ber[i])*np.log2(1-ber[i]))
    c_p[i] = 1 - (- p_e[i]*np.log2(p_e[i]) - (1-p_e[i])*np.log2(1-p_e[i]))

    #シャノン・ハレーの定理によりシャノン限界を計算
    c_limit[i] = np.log2(1+1/noise_e[i])

plt.semilogy(snr_db, c, 'o-', label='simulation')
plt.semilogy(snr_db, c_p, 'x-', label='theory')
plt.semilogy(snr_db, c_limit, 's-', label='limit')
plt.xlabel('SNR [dB]')
plt.ylabel('Capacity')
plt.legend()
plt.grid()
plt.show()
  