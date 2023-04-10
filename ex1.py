# ランダムなデータに基づく，BPSK変調のベースバンド時間波形を生成する．なお，ベースバンド信号としては，シンボルタイミング点においてのみ信号が存在するインパルス信号を想定し，振幅は，例えば，平均信号電力が1となるように設定する

import numpy as np

# パラメータ
num_symbols = 30  # 生成するシンボル数
amp = 1  # インパルス信号の振幅

# ランダムなデータを生成
data = np.random.randint(0, 2, num_symbols)

# BPSK変調
modulated_data = 2 * data - 1  

# ベースバンド時間波形の生成
time_waveform = np.zeros(num_symbols)
time_waveform[:] = amp * modulated_data[:]

# 時間波形のプロット
import matplotlib.pyplot as plt
plt.stem(time_waveform)
plt.show()