# SNRを0dB～10dBまで1dB刻みで変化させたときのBPSK信号のビット誤り率特性を取得する．また, 得られたBPSK信号のビット誤り率特性が，誤差補関数により与えられる理論BER特性と概ね一致することを確認する

import numpy as np
from scipy.special import erfc

num_symbols = 1000000 # 生成するシンボル数
amp = 1 # インパルス信号の振幅
snr_db = np.arange(0, 11) # SNR の値 (0～10dB)
ber = np.zeros(len(snr_db)) # ビット誤り率
p_e = np.zeros(len(snr_db))


# ランダムなデータを生成
data = np.random.randint(0, 2, num_symbols)
# BPSK 変調
modulated_data = 2 * data - 1
# ベースバンド時間波形の生成
time_waveform = np.zeros(num_symbols)
time_waveform[:] = amp * modulated_data[:]

for i, snr in enumerate(snr_db):
  # 雑音の分散を計算
  noise_var = (amp ** 2) / (10 ** (snr / 10))
  # 正規分布に従う雑音を生成
  noise = np.random.normal(0, np.sqrt(noise_var), num_symbols)
  # 雑音を加えた受信信号を生成
  received_signal = time_waveform + noise
  # 弁別レベルを 0 に設定して、データを判定
  received_data = np.zeros(num_symbols)
  received_data[received_signal > 0] = 1

  # ビット誤り率を計算して表示
  ber[i] = np.sum(data != received_data) / num_symbols
  #理論 BER を計算
  p_e[i] = 1/2 * erfc(np.sqrt(10**(snr_db[i]/10)/2))
  #表示(6 桁)
  print(str(snr_db[i]), 'dB :', str(ber[i]), str('{:.6f}'.format(p_e[i])))